#!/usr/bin/env python3
"""
[finite_diagnostic] Geometry-dominance check — synthetic fixture only, NOT a claim about
any real basis-tracking / representation-learning system.

R_geo = |(V_{n+1} - V_n) phi_n| / |Delta_Phi_n|  measures how much of the readout step is
carried by the CHANGE IN BASIS (V_{n+1}-V_n) versus the declared coefficient update
Delta_Phi_n. When R_geo >~ 1 the fixed-basis approximation (which drops the
(V_{n+1}-V_n)phi_n term entirely) is no longer a minor correction — it is comparable to or
larger than the tracked signal — so the guard must REJECT the fixed-basis assumption.

All quantities are exact Fraction. Because both numerator and denominator are magnitudes
(square roots), the R_geo >= 1 threshold test is done via EXACT comparison of the squared
magnitudes (cross-multiplication-free since both are already over a common ground field) —
no float/sqrt needed for the accept/reject decision itself. A float sqrt is used ONLY to
report the human-readable ratio value ~1.099 for display, clearly flagged.

Run: python3 scripts/geometry_dominance_check.py
"""
from fractions import Fraction as F
import math

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

def sqnorm(v):
    return sum(x * x for x in v)

def R_geo_ge_one(dV, phi_n, dPhi_n):
    """Exact decision: R_geo >= 1  <=>  |dV.phi_n|^2 >= |dPhi_n|^2 (both magnitudes >= 0)."""
    num_vec = matvec(dV, phi_n)
    return sqnorm(num_vec) >= sqnorm(dPhi_n), num_vec

# ============================================================ FAILING control (must reject)
# "Failing" here = the fixed-basis assumption FAILS / must be rejected -> guard flags it.
I2 = [[F(1), F(0)], [F(0), F(1)]]
V_next = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]   # 3-4-5 rotation matrix
phi_n = [F(2), F(1)]
d_phi_n = [F(1, 2), F(-1, 4)]
dPhi_n = [F(-11, 10), F(29, 20)]                      # true coefficient increment (given)

dV = mat_sub(V_next, I2)
check("dV = V_{n+1} - V_n built exact = [[-2/5,-4/5],[4/5,-2/5]]",
      dV == [[F(-2, 5), F(-4, 5)], [F(4, 5), F(-2, 5)]], dV)

reject, geo_term = R_geo_ge_one(dV, phi_n, dPhi_n)
check("(V_{n+1}-V_n)phi_n = (-8/5, 6/5) exact", geo_term == [F(-8, 5), F(6, 5)], geo_term)
check("|(V_{n+1}-V_n)phi_n|^2 = 4 exact", sqnorm(geo_term) == F(4), sqnorm(geo_term))
check("|Delta_Phi_n|^2 = 53/16 exact", sqnorm(dPhi_n) == F(53, 16), sqnorm(dPhi_n))
check("R_geo^2 = 4 / (53/16) = 64/53 >= 1  ->  R_geo >= 1  (EXACT, no sqrt needed)",
      reject, (sqnorm(geo_term), sqnorm(dPhi_n)))

R_geo_float = math.sqrt(float(sqnorm(geo_term)) / float(sqnorm(dPhi_n)))
check("R_geo numerically ~ 1.099 = 8/sqrt(53) (tol 1e-3) [display only, NUMERIC]",
      abs(R_geo_float - 1.099) < 1e-3, R_geo_float)

check("FAILING control: fixed-basis assumption REJECTED (R_geo >= 1 threshold)", reject)

# dropped-term (fixed-basis) approximation predicts Delta_Phi_n ~ d_phi_n alone,
# i.e. it silently drops the (V_{n+1}-V_n)phi_n geometry term entirely.
check("dropped-term approx predicts first component = +1/2 (positive)",
      d_phi_n[0] == F(1, 2), d_phi_n[0])
check("true Delta_Phi_n first component = -11/10 (negative)", dPhi_n[0] == F(-11, 10), dPhi_n[0])
check("SIGN FLIP: dropped-term approx (+1/2) disagrees in sign with truth (-11/10)",
      (d_phi_n[0] > 0) != (dPhi_n[0] > 0))

# ========================================================= PASSING control (fixed-basis OK)
V_next_same = [row[:] for row in I2]                  # V_{n+1} = V_n  (no basis rotation)
dV_same = mat_sub(V_next_same, I2)
check("PASSING control: V_{n+1} = V_n  ->  dV = 0", all(x == 0 for row in dV_same for x in row))
allow, geo_term_same = R_geo_ge_one(dV_same, phi_n, dPhi_n)
check("PASSING control: (V_{n+1}-V_n)phi_n = (0,0) exact",
      geo_term_same == [F(0), F(0)], geo_term_same)
check("PASSING control: R_geo = 0 < 1  ->  fixed-basis assumption ALLOWED",
      not allow, allow)

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — geometry-dominance guard correctly REJECTS the fixed-basis")
print("assumption when R_geo >= 1 (rotation fixture, sign-flip demonstrated) and ALLOWS it")
print("when V_{n+1}=V_n (R_geo=0). [finite_diagnostic] on a synthetic fixture ONLY.")
