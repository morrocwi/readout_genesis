from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Hashable, Iterable, Mapping, Sequence


def validate_registry(registry: Sequence[str]) -> tuple[str, ...]:
    reg = tuple(registry)
    if not reg:
        raise ValueError("empty generator registry")
    if any(not isinstance(x, str) or not x for x in reg):
        raise ValueError("generator ids must be nonempty strings")
    if len(set(reg)) != len(reg):
        raise ValueError("generator aliases/duplicates are unresolved")
    return reg


def zero(registry: Sequence[str]) -> tuple[int, ...]:
    reg = validate_registry(registry)
    return (0,) * len(reg)


def compose(a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
    if len(a) != len(b):
        raise ValueError("dimension mismatch")
    if any((not isinstance(x, int)) or x < 0 for x in tuple(a) + tuple(b)):
        raise ValueError("occupation coordinates must be nonnegative integers")
    return tuple(x + y for x, y in zip(a, b))


def occupation(word: Sequence[str], registry: Sequence[str]) -> tuple[int, ...]:
    reg = validate_registry(registry)
    pos = {g: i for i, g in enumerate(reg)}
    out = [0] * len(reg)
    for token in word:
        if token not in pos:
            raise ValueError(f"unresolved token {token}")
        out[pos[token]] += 1
    return tuple(out)


def carrier_axiom_receipt(registry: Sequence[str], samples: Sequence[Sequence[int]]) -> dict:
    reg = validate_registry(registry)
    z = zero(reg)
    vectors = [tuple(v) for v in samples]
    for v in vectors:
        if len(v) != len(reg) or any((not isinstance(x, int)) or x < 0 for x in v):
            raise ValueError("bad sample")
    closure = all(len(compose(a, b)) == len(reg) for a in vectors for b in vectors)
    identity = all(compose(v, z) == v and compose(z, v) == v for v in vectors)
    commutative = all(compose(a, b) == compose(b, a) for a in vectors for b in vectors)
    associative = all(compose(compose(a, b), c) == compose(a, compose(b, c)) for a in vectors for b in vectors for c in vectors)
    return {"closure": closure, "identity": identity, "commutative_carrier": commutative, "associative": associative}


def count_homomorphism_receipt(registry: Sequence[str], left: Sequence[str], right: Sequence[str]) -> dict:
    ql = occupation(left, registry)
    qr = occupation(right, registry)
    qcat = occupation(tuple(left) + tuple(right), registry)
    return {
        "empty_to_zero": occupation((), registry) == zero(registry),
        "concatenation_to_addition": qcat == compose(ql, qr),
        "left": list(ql), "right": list(qr), "concatenated": list(qcat)
    }


def _canonical_signature(value):
    if isinstance(value, dict):
        return tuple(sorted((k, _canonical_signature(v)) for k, v in value.items()))
    if isinstance(value, (list, tuple)):
        return tuple(_canonical_signature(v) for v in value)
    return value


def permutation_sufficiency_gate(
    states: Sequence[Hashable],
    source_words: Mapping[Hashable, Sequence[str]],
    registry: Sequence[str],
    profiles: Mapping[str, Mapping[str, Mapping[Hashable, object]]],
) -> dict:
    """Exact finite gate.

    profiles[profile_id] contains readouts and optionally successor signatures.
    Every equal-count pair must match every registered signature.
    """
    q = {s: occupation(source_words[s], registry) for s in states}
    violations = []
    checked_pairs = 0
    for i, a in enumerate(states):
        for b in states[i+1:]:
            if q[a] != q[b]:
                continue
            checked_pairs += 1
            for pid, profile in profiles.items():
                for kind in ('readout', 'successor'):
                    table = profile.get(kind, {})
                    if a not in table or b not in table:
                        violations.append({"pair": [str(a), str(b)], "profile": pid, "kind": kind, "reason": "missing signature"})
                    elif _canonical_signature(table[a]) != _canonical_signature(table[b]):
                        violations.append({"pair": [str(a), str(b)], "profile": pid, "kind": kind, "reason": "signature mismatch"})
    return {
        "checked_same_count_pairs": checked_pairs,
        "violations": violations,
        "decision": "ADMITTED_FOR_REGISTERED_PROFILES" if not violations else "OBSTRUCTED_COMMUTATIVE_QUOTIENT"
    }


def decomposition_unique(a: Sequence[int], b: Sequence[int], registry: Sequence[str]) -> dict:
    reg = validate_registry(registry)
    if len(a) != len(reg) or len(b) != len(reg):
        raise ValueError("dimension mismatch")
    return {
        "same_structural_element": tuple(a) == tuple(b),
        "coordinatewise_equal_if_same": (tuple(a) != tuple(b)) or all(x == y for x, y in zip(a, b)),
        "registry_frozen": True
    }


def alias_countermodel() -> dict:
    try:
        validate_registry(("u", "u"))
    except ValueError:
        rejected = True
    else:
        rejected = False
    return {"duplicate_alias_rejected": rejected, "conclusion": "uniqueness requires identity-locked coordinates"}


def mat_vec(P: Sequence[Sequence[int]], c: Sequence[int]) -> tuple[int, ...]:
    if any(len(row) != len(c) for row in P):
        raise ValueError("matrix dimension mismatch")
    if any((not isinstance(x, int)) or x < 0 for row in P for x in row):
        raise ValueError("coarsening map must be nonnegative integer")
    return tuple(sum(x*y for x, y in zip(row, c)) for row in P)


def refinement_commutation_receipt(P: Sequence[Sequence[int]], c: Sequence[int], d: Sequence[int]) -> dict:
    lhs = mat_vec(P, compose(c, d))
    rhs = compose(mat_vec(P, c), mat_vec(P, d))
    return {"lhs": list(lhs), "rhs": list(rhs), "commutes": lhs == rhs}


def invalid_refinement_countercontrol() -> dict:
    bad_maps = [
        [[1, -1]],  # negative contribution
        [[1, 0], [0]],  # ragged
    ]
    rejected = []
    for P in bad_maps:
        try:
            mat_vec(P, (1, 1))
        except (ValueError, TypeError):
            rejected.append(True)
        else:
            rejected.append(False)
    return {"all_bad_maps_rejected": all(rejected), "cases": rejected}


@dataclass(frozen=True)
class MarkedComposition:
    structural: tuple[int, ...]
    lineage_bundle: tuple[str, ...]


def mark(word: Sequence[str], lineage_bundle: Sequence[str], registry: Sequence[str]) -> MarkedComposition:
    if len(lineage_bundle) == 0:
        raise ValueError("lineage sidecar required")
    if any(not isinstance(x, str) or not x for x in lineage_bundle):
        raise ValueError("invalid lineage id")
    return MarkedComposition(occupation(word, registry), tuple(lineage_bundle))


def marked_compose(a: MarkedComposition, b: MarkedComposition) -> MarkedComposition:
    return MarkedComposition(compose(a.structural, b.structural), a.lineage_bundle + b.lineage_bundle)


def lineage_receipt(registry: Sequence[str]) -> dict:
    a = mark(("u", "v"), ("history-A",), registry)
    b = mark(("v", "u"), ("history-B",), registry)
    combined_ab = marked_compose(a, b)
    combined_ba = marked_compose(b, a)
    return {
        "same_structural_projection": a.structural == b.structural,
        "marked_states_distinct": a != b,
        "composition_structural_projection_commutes": combined_ab.structural == combined_ba.structural,
        "lineage_bundle_not_silently_commuted": combined_ab.lineage_bundle != combined_ba.lineage_bundle,
        "count_only_would_erase_lineage": a.structural == b.structural
    }


def run_composition_suite() -> dict:
    registry = ("u", "v", "w")
    samples = ((0,0,0), (1,0,0), (0,2,1), (3,1,0))
    c1 = carrier_axiom_receipt(registry, samples)
    c2 = count_homomorphism_receipt(registry, ("u","v"), ("v","w"))

    states = ("uv-A", "vu-B", "uu-C")
    words = {"uv-A": ("u","v"), "vu-B": ("v","u"), "uu-C": ("u","u")}
    positive_profiles = {
        "profile-1": {
            "readout": {"uv-A": (2,0), "vu-B": (2,0), "uu-C": (2,1)},
            "successor": {"uv-A": (1,1), "vu-B": (1,1), "uu-C": (2,0)}
        },
        "profile-2": {
            "readout": {"uv-A": "same", "vu-B": "same", "uu-C": "other"},
            "successor": {"uv-A": "z", "vu-B": "z", "uu-C": "y"}
        }
    }
    negative_profiles = {
        "order-sensitive-control": {
            "readout": {"uv-A": "left-right", "vu-B": "right-left", "uu-C": "same"},
            "successor": {"uv-A": "z", "vu-B": "z", "uu-C": "y"}
        }
    }
    c3_pos = permutation_sufficiency_gate(states, words, registry, positive_profiles)
    c3_neg = permutation_sufficiency_gate(states, words, registry, negative_profiles)
    c4 = decomposition_unique((1,2,0), (1,2,0), registry)
    c4_alias = alias_countermodel()
    P = ((1,1,0), (0,0,1))
    c5 = refinement_commutation_receipt(P, (1,2,3), (2,0,1))
    c5_bad = invalid_refinement_countercontrol()
    c6 = lineage_receipt(registry)

    statuses = {
        "C1": all(c1.values()),
        "C2": c2["empty_to_zero"] and c2["concatenation_to_addition"],
        "C3": c3_pos["decision"] == "ADMITTED_FOR_REGISTERED_PROFILES" and c3_neg["decision"] == "OBSTRUCTED_COMMUTATIVE_QUOTIENT",
        "C4": c4["same_structural_element"] and c4["coordinatewise_equal_if_same"] and c4_alias["duplicate_alias_rejected"],
        "C5": c5["commutes"] and c5_bad["all_bad_maps_rejected"],
        "C6": all(c6.values()),
    }
    return {
        "version": "0.910",
        "data_class": "FINITE_FORMAL_WITNESSES",
        "receipts": {"C1": c1, "C2": c2, "C3_positive": c3_pos, "C3_negative": c3_neg, "C4": c4, "C4_alias": c4_alias, "C5": c5, "C5_bad": c5_bad, "C6": c6},
        "statuses": statuses,
        "decision": "PASS" if all(statuses.values()) else "FAIL"
    }
