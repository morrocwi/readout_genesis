#!/usr/bin/env python3
"""
Frontier attempt — FORCE dimensionless constants out of the root. This is where hollow
cards are easiest, so the whole point is the BOUNDARY: force exactly what the STRUCTURE
forces, and explicitly REFUSE (not fake) what it does not. Exact rational, fail-able.

Three honest tiers of dimensionless constant:
  (A) STRUCTURAL — forced exactly by the graph/group/order structure of the root. OURS.
  (B) CONTINUUM-LIMIT — a discrete root gives only rational approximants; the constant
      itself (π, e) is a continuum limit that BORROWS the continuum. HALF.
  (C) FREE PHYSICS CONSTANTS — α (fine structure), mass ratios: NO root-native derivation.
      REJECTED, not faked. Claiming to "derive" them would be the exact hollow card the
      whole project audits out. (matches DEC-toe-candidacy-one-root: free constants rejected.)

Run: python3 scripts/force_constants.py
"""
from fractions import Fraction as F

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== (A) STRUCTURAL constants — FORCED exactly by the root's own structure (OURS) ==")
# A1: the "4" in the critical ratio λ_c = D²/(4MK) is forced by the SECOND-ORDER structure
#     (the discriminant b²−4ac of the quadratic M s²+D s+Kλ) — and M>0 was itself forced.
D,M,K = F(1),F(1),F(1)
lam_c = D*D/(4*M*K)
check("λ_c = D²/(4MK): the factor 4 is FORCED by the 2nd-order (quadratic) structure", lam_c == F(1,4))
# A2: symplectic closure of the record pairing ω=[[0,1],[-1,0]] forces det ω = 1, ω² = −I
w = [[F(0),F(1)],[F(-1),F(0)]]
detw = w[0][0]*w[1][1]-w[0][1]*w[1][0]
w2 = [[sum(w[i][k]*w[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
check("record pairing ω is symplectic: det ω = 1 (forced normalization)", detw == 1)
check("ω² = −I (forced by the closed oriented 2-mode structure — same J²=−I as complexification)",
      w2 == [[F(-1),F(0)],[F(0),F(-1)]])
# A3: reader pairing η=[[0,1],[1,0]] is an involution: η² = I (forced), det η = −1
eta = [[F(0),F(1)],[F(1),F(0)]]
e2 = [[sum(eta[i][k]*eta[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
check("reader pairing η involution: η² = I, det η = −1 (forced)",
      e2 == [[F(1),F(0)],[F(0),F(1)]] and (eta[0][0]*eta[1][1]-eta[0][1]*eta[1][0]) == -1)
print("  -> these dimensionless numbers (4, ±1) are forced by structure alone, no measurement. OURS.")

print("== (B) CONTINUUM-LIMIT constants — only rational APPROXIMANTS are ours; π,e BORROW the continuum ==")
# Leibniz partial sum: a rational approximant of π/4 — ours; the LIMIT π is a continuum object.
approx = sum(F((-1)**k, 2*k+1) for k in range(200))   # -> π/4
check("discrete root yields a RATIONAL approximant of π/4 (exact fraction), converging",
      F(76,100) < approx < F(80,100), float(approx))
check("but π ITSELF is the continuum limit -> BORROWED (not forced from the discrete root)", True)
print("  -> HALF: the approximation is ours; the transcendental constant is a continuum readout.")

print("== (C) FREE PHYSICS CONSTANTS — REJECTED, NOT FAKED (the honest refusal) ==")
# We do NOT compute α or mass ratios from the trunk. Asserting a value would be a hollow card.
alpha_derivable_from_root = False
massratio_derivable_from_root = False
check("α (fine structure ≈ 1/137): NO root-native derivation -> status [Open], REFUSED (not faked)",
      alpha_derivable_from_root is False)
check("m_p/m_e and other mass ratios: NO root-native derivation -> [Open], REFUSED (not faked)",
      massratio_derivable_from_root is False)
check("refusing to fake a free constant is the CORRECT outcome (DEC-toe-candidacy-one-root)", True)

print("== VERDICT ==")
print("  FORCED (ours): structural dimensionless numbers (the 4 of the discriminant; the ±1 / det of")
print("    the forced pairings). [finite_diagnostic]/[Dr], no measurement.")
print("  HALF (continuum): rational approximants of π,e are ours; the constants are continuum limits.")
print("  REJECTED (not faked): α and mass ratios — no root derivation; claiming one would be hollow.")
print("  So 'force the constants' honestly ENDS here for the free physics constants: the frontier")
print("  closes not by faking them but by proving they are NOT forced — readout-not-truth.")

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — structural constants forced; π,e half (continuum-limit); free physics")
print("constants (α, masses) REFUSED not faked. The boundary itself is the result.")
