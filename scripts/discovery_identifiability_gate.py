#!/usr/bin/env python3
"""
[finite_diagnostic] Discovery identifiability gate — synthetic fixture only, NOT a claim
about any real regression / system-identification pipeline.

Requires rank(design_matrix) == n_candidate_coefficients over Q for a declared monomial
basis before reporting a discovered law. If the design matrix built from the observation
tape is rank-deficient, the gate must return UNDERDETERMINED / ABSTAIN rather than let the
underlying linear solve return an arbitrary (non-unique) particular solution dressed up as
"the" law.

Reuses the exact-rational rank/solve/discover machinery from domain_discovery_battery.py
(same directory) rather than re-deriving it — that module is the canonical exact-Gauss-
Jordan-over-Q implementation and is imported unchanged.

Run: python3 scripts/discovery_identifiability_gate.py
"""
from fractions import Fraction as F
import io, contextlib
# import silently — domain_discovery_battery runs its own battery at module level
with contextlib.redirect_stdout(io.StringIO()):
    from domain_discovery_battery import rank_exact, solve_exact, discover, basis_eval

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

BASIS2 = ["1", "N", "S", "N^2", "N*S", "S^2"]         # 6 candidate coefficients
law1 = lambda N, S: (N + N * S / 8, S - N * S / 8)     # planted law, conserves N+S

def make_tape(pts):
    return [({"N": F(a), "S": F(b)}, law1(F(a), F(b))) for a, b in pts]

PTS6 = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]   # 6 rows -> exactly full rank
PTS5 = PTS6[:5]                                            # 5 rows -> rank-deficient for 6 coeffs

# =============================================================== PASSING: full rank -> reported
tape6 = make_tape(PTS6)
A6 = [basis_eval(BASIS2, inp) for inp, _ in tape6]
rank6 = rank_exact(A6)
check("PASSING: 6-row tape / 6-coeff basis -> rank(design matrix) == 6 (full rank)",
      rank6 == 6, rank6)

cN = discover(tape6, ("N", "S"), BASIS2, 0)
check("PASSING: identifiable -> law IS reported (not None)", cN is not None, cN)
check("PASSING: reported law = N + (1/8)N*S (exact)",
      cN == [F(0), F(1), F(0), F(0), F(1, 8), F(0)], cN)

# ============================================================ FAILING: rank-deficient -> abstain
tape5 = make_tape(PTS5)
A5 = [basis_eval(BASIS2, inp) for inp, _ in tape5]
rank5 = rank_exact(A5)
check("FAILING: 5-row tape / 6-coeff basis -> rank(design matrix) == 5 < 6 (deficient)",
      rank5 == 5, rank5)
check("FAILING: rank(A) < n_coeffs -> UNDERDETERMINED", rank5 < len(BASIS2), (rank5, len(BASIS2)))

cN_short = discover(tape5, ("N", "S"), BASIS2, 0)
check("FAILING: gate correctly returns ABSTAIN (None), not a guessed law",
      cN_short is None, cN_short)

# sanity: solve_exact directly on the deficient system also refuses (defense in depth)
b5 = [out[0] for _, out in tape5]
check("FAILING: solve_exact on the SAME deficient system also returns None",
      solve_exact(A5, b5) is None, solve_exact(A5, b5))

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — identifiability gate reports the law only when rank(design)==n_coeffs")
print("(6-row tape) and correctly ABSTAINS (UNDERDETERMINED) on a rank-deficient 5-row tape.")
print("[finite_diagnostic] on a synthetic fixture ONLY.")
