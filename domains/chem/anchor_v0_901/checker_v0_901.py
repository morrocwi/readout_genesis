from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def mv(A, x):
    return tuple(sum(Fraction(a)*Fraction(b) for a, b in zip(row, x)) for row in A)


def independent_checks():
    checks = {}

    A = ((1, 1, 0), (0, 1, 1))
    n0 = (2, 0, 2)
    n1 = (1, 1, 1)
    delta = tuple(b-a for a, b in zip(n0, n1))
    checks["P1"] = mv(A, n0) == mv(A, n1) and mv(A, delta) == (0, 0)

    v = (-1, 1, -1)
    checks["P2"] = mv(A, v) == (0, 0)
    checks["P3"] = tuple(a+b for a, b in zip(n0, v)) == n1

    feasible = [Fraction(i, 10) for i in range(-30, 31) if all(Fraction(a)+Fraction(d)*Fraction(i,10) >= 0 for a,d in zip(n0, v))]
    checks["P4"] = max(feasible) == 2 and min(feasible) == 0

    # Independent finite refinement by exhaustive equivalence signature iteration.
    states = ("a", "b", "c", "d")
    F = {"a":"b", "b":"b", "c":"d", "d":"d"}
    O = {"a":0, "b":1, "c":0, "d":2}
    labels = {s: O[s] for s in states}
    for _ in range(len(states)+1):
        signatures = {s: (O[s], labels[F[s]]) for s in states}
        canon = {sig:i for i,sig in enumerate(sorted(set(signatures.values()), key=str))}
        new_labels = {s: canon[signatures[s]] for s in states}
        if new_labels == labels:
            break
        labels = new_labels
    checks["P5"] = all(O[a] == O[b] and labels[F[a]] == labels[F[b]] for a in states for b in states if labels[a] == labels[b])

    additive = lambda n: n
    nonlinear = lambda n: n*n
    checks["P6"] = additive(2) == additive(1)+additive(1) and nonlinear(2) != nonlinear(1)+nonlinear(1)

    source_F = {"a":"b", "b":"a"}
    q = {"a":"z", "b":"z"}
    checks["P7"] = all(q[source_F[s]] == "z" for s in source_F) and any(source_F[s] != s for s in source_F)

    receipt = json.loads((ROOT / "PROOF_RECEIPT_v0_901.json").read_text(encoding="utf-8"))
    receipt_statuses = receipt["result"]["statuses"]
    checks["receipt_agreement"] = all(receipt_statuses[k] == checks[k] for k in ["P1","P2","P3","P4","P5","P6","P7"])

    drift = json.loads((ROOT / "DRIFT_AUDIT_v0_901.json").read_text(encoding="utf-8"))
    checks["drift_contract"] = drift["decision"] == "PASS"

    claim = json.loads((ROOT / "CLAIM_BOUNDARY_v0_901.json").read_text(encoding="utf-8"))
    checks["claim_is_foundational_only"] = claim["tier"] == "FORMAL_FOUNDATION_ONLY" and bool(claim["not_established"])

    return {
        "version": "0.901",
        "checker_type": "INTERNAL_DUAL_IMPLEMENTATION_CHECKER",
        "checks": checks,
        "decision": "PASS" if all(checks.values()) else "FAIL",
        "independence_boundary": "Different implementation, same release authoring environment; not external peer review."
    }


if __name__ == "__main__":
    result = independent_checks()
    (ROOT / "CHECKER_DECISION_v0_901.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
