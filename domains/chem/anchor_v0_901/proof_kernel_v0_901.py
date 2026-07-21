from __future__ import annotations

from fractions import Fraction
from itertools import product
from typing import Dict, Hashable, Iterable, List, Mapping, Sequence, Tuple

Number = int | Fraction
Vector = Sequence[Number]
Matrix = Sequence[Sequence[Number]]


def mat_vec(A: Matrix, x: Vector) -> tuple[Fraction, ...]:
    if any(len(row) != len(x) for row in A):
        raise ValueError("shape mismatch")
    return tuple(sum(Fraction(a) * Fraction(b) for a, b in zip(row, x)) for row in A)


def sub(a: Vector, b: Vector) -> tuple[Fraction, ...]:
    if len(a) != len(b):
        raise ValueError("shape mismatch")
    return tuple(Fraction(x) - Fraction(y) for x, y in zip(a, b))


def add(a: Vector, b: Vector) -> tuple[Fraction, ...]:
    if len(a) != len(b):
        raise ValueError("shape mismatch")
    return tuple(Fraction(x) + Fraction(y) for x, y in zip(a, b))


def linear_combination(columns: Sequence[Vector], coordinates: Vector) -> tuple[Fraction, ...]:
    if len(columns) != len(coordinates):
        raise ValueError("basis/coordinate mismatch")
    if not columns:
        return ()
    dim = len(columns[0])
    if any(len(col) != dim for col in columns):
        raise ValueError("basis dimension mismatch")
    return tuple(
        sum(Fraction(columns[j][i]) * Fraction(coordinates[j]) for j in range(len(columns)))
        for i in range(dim)
    )


def ledger_conservation_certificate(A: Matrix, n0: Vector, n1: Vector) -> dict:
    before = mat_vec(A, n0)
    after = mat_vec(A, n1)
    delta = sub(n1, n0)
    residual = mat_vec(A, delta)
    return {
        "before": [str(x) for x in before],
        "after": [str(x) for x in after],
        "delta": [str(x) for x in delta],
        "residual": [str(x) for x in residual],
        "closed_boundary_holds": before == after,
        "algebraic_identity_holds": residual == tuple(a-b for a, b in zip(after, before)),
    }


def kernel_basis_certificate(A: Matrix, basis_columns: Sequence[Vector], coordinates: Vector) -> dict:
    basis_residuals = [mat_vec(A, col) for col in basis_columns]
    delta = linear_combination(basis_columns, coordinates)
    residual = mat_vec(A, delta)
    return {
        "basis_residuals": [[str(x) for x in row] for row in basis_residuals],
        "delta": [str(x) for x in delta],
        "residual": [str(x) for x in residual],
        "all_basis_in_kernel": all(all(x == 0 for x in row) for row in basis_residuals),
        "combination_in_kernel": all(x == 0 for x in residual),
    }


def extent_certificate(A: Matrix, n0: Vector, n1: Vector, basis_columns: Sequence[Vector], coordinates: Vector) -> dict:
    delta = sub(n1, n0)
    reconstructed = linear_combination(basis_columns, coordinates)
    kernel = kernel_basis_certificate(A, basis_columns, coordinates)
    return {
        "delta": [str(x) for x in delta],
        "reconstructed": [str(x) for x in reconstructed],
        "coordinates_reconstruct_change": delta == reconstructed,
        "change_preserves_ledger": kernel["combination_in_kernel"],
        "basis_completeness_assumed_not_proved_by_this_instance": True,
    }


def positivity_interval_1d(n0: Vector, direction: Vector) -> dict:
    if len(n0) != len(direction):
        raise ValueError("shape mismatch")
    lower = None
    upper = None
    constraints = []
    for i, (a0, d) in enumerate(zip(n0, direction)):
        a0 = Fraction(a0)
        d = Fraction(d)
        if d > 0:
            bound = -a0 / d
            lower = bound if lower is None or bound > lower else lower
            constraints.append((i, ">=", bound))
        elif d < 0:
            bound = a0 / (-d)
            upper = bound if upper is None or bound < upper else upper
            constraints.append((i, "<=", bound))
        elif a0 < 0:
            return {"admissible": False, "reason": "negative fixed component"}
    admissible = not (lower is not None and upper is not None and lower > upper)
    return {
        "admissible": admissible,
        "lower": None if lower is None else str(lower),
        "upper": None if upper is None else str(upper),
        "constraints": [[i, op, str(v)] for i, op, v in constraints],
    }


def _cell_index(partition: Sequence[Sequence[Hashable]]) -> dict:
    out = {}
    for idx, cell in enumerate(partition):
        for state in cell:
            if state in out:
                raise ValueError("state appears in multiple cells")
            out[state] = idx
    return out


def refine_partition(states: Sequence[Hashable], dynamics: Mapping[Hashable, Hashable], readout: Mapping[Hashable, Hashable], initial_partition: Sequence[Sequence[Hashable]]) -> dict:
    partition = [tuple(cell) for cell in initial_partition]
    seen = set()
    steps = []
    while True:
        key = tuple(sorted(tuple(sorted(map(str, cell))) for cell in partition))
        if key in seen:
            raise RuntimeError("unexpected refinement cycle")
        seen.add(key)
        idx = _cell_index(partition)
        new_partition = []
        split_happened = False
        for cell in partition:
            buckets: Dict[tuple, list] = {}
            for s in cell:
                signature = (readout[s], idx[dynamics[s]])
                buckets.setdefault(signature, []).append(s)
            if len(buckets) > 1:
                split_happened = True
            new_partition.extend(tuple(v) for _, v in sorted(buckets.items(), key=lambda kv: str(kv[0])))
        steps.append({"cell_count_before": len(partition), "cell_count_after": len(new_partition)})
        partition = new_partition
        if not split_happened:
            break
        if len(partition) > len(states):
            raise RuntimeError("partition cannot exceed state count")
    idx = _cell_index(partition)
    exact = all(
        readout[a] == readout[b] and idx[dynamics[a]] == idx[dynamics[b]]
        for cell in partition for a in cell for b in cell
    )
    return {
        "partition": [list(cell) for cell in partition],
        "steps": steps,
        "terminated": True,
        "exact_readout_and_dynamics_closure": exact,
        "cell_count_le_state_count": len(partition) <= len(states),
    }


def free_commutative_additive_representation(weights: Vector, composition: Sequence[int]) -> Fraction:
    if len(weights) != len(composition):
        raise ValueError("shape mismatch")
    if any(c < 0 for c in composition):
        raise ValueError("composition must be nonnegative")
    return sum(Fraction(w) * c for w, c in zip(weights, composition))


def additivity_no_free_countermodel() -> dict:
    # Retention alone permits both maps on the same retained count state.
    states = list(range(5))
    additive = {n: n for n in states}
    nonadditive = {n: n*n for n in states}
    witness = (1, 1)
    return {
        "shared_retained_states": states,
        "additive_map": additive,
        "nonadditive_map": nonadditive,
        "witness": list(witness),
        "additive_passes": additive[2] == additive[1] + additive[1],
        "nonadditive_fails": nonadditive[2] != nonadditive[1] + nonadditive[1],
        "conclusion": "Retention alone does not select additive readout semantics."
    }


def observational_stationarity_counterexample() -> dict:
    source_states = ["a", "b"]
    dynamics = {"a": "b", "b": "a"}
    quotient = {"a": "z", "b": "z"}
    readout = {"a": 0, "b": 0}
    quotient_successors = {quotient[dynamics[s]] for s in source_states}
    hidden_motion = any(dynamics[s] != s for s in source_states)
    return {
        "source_states": source_states,
        "source_dynamics": dynamics,
        "quotient": quotient,
        "readout": readout,
        "quotient_successors": sorted(quotient_successors),
        "quotient_is_fixed": quotient_successors == {"z"},
        "readout_is_stationary": len(set(readout.values())) == 1,
        "source_has_hidden_motion": hidden_motion,
        "conclusion": "Quotient fixed point establishes observational stationarity only."
    }


def run_proof_suite() -> dict:
    # All data are finite formal witnesses, not empirical chemistry data.
    A = [[1, 1, 0], [0, 1, 1]]
    n0 = [2, 0, 2]
    n1 = [1, 1, 1]
    basis = [[-1, 1, -1]]
    coords = [1]

    p1 = ledger_conservation_certificate(A, n0, n1)
    p2 = kernel_basis_certificate(A, basis, coords)
    p3 = extent_certificate(A, n0, n1, basis, coords)
    p4 = positivity_interval_1d([2, 0, 2], [-1, 1, -1])

    states = ["a", "b", "c", "d"]
    dynamics = {"a": "b", "b": "b", "c": "d", "d": "d"}
    readout = {"a": 0, "b": 1, "c": 0, "d": 2}
    p5 = refine_partition(states, dynamics, readout, [states])

    weights = [2, 3]
    comp = [4, 5]
    p6 = {
        "conditional_representation_value": str(free_commutative_additive_representation(weights, comp)),
        "no_free_countermodel": additivity_no_free_countermodel(),
    }
    p7 = observational_stationarity_counterexample()

    statuses = {
        "P1": p1["closed_boundary_holds"] and p1["algebraic_identity_holds"] and all(x == "0" for x in p1["residual"]),
        "P2": p2["all_basis_in_kernel"] and p2["combination_in_kernel"],
        "P3": p3["coordinates_reconstruct_change"] and p3["change_preserves_ledger"],
        "P4": p4["admissible"] and p4["upper"] == "2",
        "P5": p5["terminated"] and p5["exact_readout_and_dynamics_closure"] and p5["cell_count_le_state_count"],
        "P6": p6["conditional_representation_value"] == "23" and p6["no_free_countermodel"]["nonadditive_fails"],
        "P7": p7["quotient_is_fixed"] and p7["readout_is_stationary"] and p7["source_has_hidden_motion"],
    }
    return {
        "version": "0.901",
        "data_status": "FINITE_FORMAL_WITNESSES",
        "proofs": {"P1": p1, "P2": p2, "P3": p3, "P4": p4, "P5": p5, "P6": p6, "P7": p7},
        "statuses": statuses,
        "decision": "PASS" if all(statuses.values()) else "FAIL",
        "claim_boundary": "Formal conditional root layer only; no empirical chemistry law."
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_proof_suite(), indent=2, sort_keys=True))
