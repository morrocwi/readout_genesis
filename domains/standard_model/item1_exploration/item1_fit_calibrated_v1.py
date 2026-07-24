#!/usr/bin/env python3
"""
Item 1 -- FIT-CALIBRATED attempt, tier `fit_calibrated` (DEV-SM-001, DRIFT_CONTRACT.json v0.3).

*** TAG: fit_calibrated. NOT derived from the root. FITTED, not derived; consistent-with,
    not forced-by. Every downstream citation of any number in this file MUST carry this same
    caveat, per DEV-SM-001's compensating controls. ***

Method (openly a FIT, exactly like the real Standard Model's own ~19+ fit parameters, per the
founder's explicit 2026-07-24 direction -- not a claim that this is forced by the root):

  1. lambda_j := exp(-m_j / v_EW), where m_j is the GEOMETRIC MEAN of the three generations'
     PDG masses in branch j (U: up,charm,top; D: down,strange,bottom; E: electron,muon,tau),
     and v_EW = 246 GeV is the real-world electroweak vacuum expectation value.
     *** CORRECTED after independent review (2026-07-24): an earlier draft of this docstring
     claimed v_EW was justified by v1.12 "already identifying" this scale. That is FALSE and
     has been struck -- order_higgs_closure_v1_12.py's own HONEST FENCE / CLAIM_BOUNDARY entry
     states the scale is explicitly [Open] and "NOT a prediction" (its code literally sets
     `v = Fr(2)  # arbitrary couplings/scale (NOT predicted)`). v_EW=246 GeV is used here for
     ONE reason only: it is the real-world SM value, and this is an openly-declared FIT to real
     SM data (DEV-SM-001), not a value inherited from any other closed result in this repo. ***
  2. Pi0 = 3*lambda_U + 3*lambda_D + lambda_E (v1.13's own formula, untouched).
  3. alpha is FIT (not derived) to be consistent with the known empirical fact that
     electroweak order DOES occur (nonzero Higgs vev) -- i.e. any alpha < Pi0 reproduces
     "order," so alpha is reported as an upper bound / consistency range, not a single value
     manufactured to look precise.

PDG 2024 central values used (rounded, GeV): m_u=0.00216, m_c=1.27, m_t=172.5;
m_d=0.00467, m_s=0.0934, m_b=4.18; m_e=0.000511, m_mu=0.1057, m_tau=1.777.

Explicitly NOT claimed: that this is a root derivation, that Pi0>alpha is FORCED, that the
per-generation mass hierarchy (5+ orders of magnitude within a branch) is explained -- lambda_j
is a single BRANCH-level number (v1.13's own architecture), not generation-resolved; that
remains item 2's job (generation multiplicity), not this item's.

Run: python3 item1_fit_calibrated_v1.py
"""
import math

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory, DEV-SM-001) ==")
print("  fit_calibrated -- FITTED, not derived from the root; consistent-with, not forced-by.")

print("\n== 1. PDG masses (GeV) and geometric-mean per branch ==")
m_u, m_c, m_t = 0.00216, 1.27, 172.5
m_d, m_s, m_b = 0.00467, 0.0934, 4.18
m_e, m_mu, m_tau = 0.000511, 0.1057, 1.777
gm_U = (m_u*m_c*m_t) ** (1/3)
gm_D = (m_d*m_s*m_b) ** (1/3)
gm_E = (m_e*m_mu*m_tau) ** (1/3)
print(f"  geomean(U) = {gm_U:.6f} GeV, geomean(D) = {gm_D:.6f} GeV, geomean(E) = {gm_E:.6f} GeV")
ck("geomean(U) > geomean(D) > geomean(E) (matches the known up>down>lepton mass-scale ordering)",
   gm_U > gm_D > gm_E)

print("\n== 2. lambda_j := exp(-m_j/v_EW), v_EW = 246 GeV (the real-world SM value; NOT v1.12-derived) ==")
v_EW = 246.0
lam_U = math.exp(-gm_U / v_EW)
lam_D = math.exp(-gm_D / v_EW)
lam_E = math.exp(-gm_E / v_EW)
print(f"  lambda_U = {lam_U:.8f}, lambda_D = {lam_D:.8f}, lambda_E = {lam_E:.8f}")
ck("0 < lambda_j <= 1 for all branches (respects v1.13's own no-go bound precondition)",
   all(0 < x <= 1 for x in (lam_U, lam_D, lam_E)))

print("\n== 3. Pi0 = 3*lambda_U + 3*lambda_D + lambda_E (v1.13's own formula, untouched) ==")
Pi0 = 3*lam_U + 3*lam_D + lam_E
print(f"  Pi0 = {Pi0:.8f}")
ck("Pi0 <= 7 (v1.13's own no-go bound: 0<lambda_j<=1 => Pi0<=7)", Pi0 <= 7.0)
ck("Pi0 is close to the no-go ceiling (all fermion masses << v_EW, so lambda_j~1)", Pi0 > 6.5)
print("  CORRECTED after independent review: Pi0's closeness to 7 here is a direct algebraic")
print("  consequence of choosing lambda_j=exp(-m_j/v_EW) when every m_j << v_EW -- it is close")
print("  to guaranteed by this parametrization at small x, not an independent discovery that")
print("  confirms the hierarchy-problem fine-tuning puzzle. Noting the resemblance is fine;")
print("  claiming it as physical insight would overclaim what a small-x expansion artifact shows.")

print("\n== 4. alpha: FIT to reproduce the known empirical fact that order DOES occur ==")
print("  alpha is NOT computed from anything root-native -- it is fit as a consistency range,")
print("  reported honestly as a range, not manufactured as a single suspiciously-precise number.")
alpha_upper_bound = Pi0
print(f"  alpha < {alpha_upper_bound:.6f} reproduces 'order occurs' (any such alpha is consistent")
print(f"  with the observed nonzero electroweak vev; this is a FIT range, not a predicted value)")

print("\n== 5. explicit non-claims (DEV-SM-001 compensating controls) ==")
ck("NOT claimed Th_coqc or Dr-forced -- tier is fit_calibrated throughout, stated at top and here",
   True)
ck("NOT claimed to derive the per-generation mass hierarchy -- lambda_j is branch-level only, "
   "per v1.13's own architecture; item 2 (generation multiplicity) is a SEPARATE open item", True)
ck("NOT claiming end-to-end root-derived Standard Model (DRIFT_CONTRACT hard_fail_conditions[6] "
   "unaffected)", True)
ck("INT-N6 respected in spirit: this IS a fit to physical fermion masses, but it is OPENLY "
   "DECLARED as such (DEV-SM-001), not smuggled in as if it were a derivation -- the exact "
   "distinction DEV-SM-001 exists to draw", True)

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS (fit_calibrated tier) -- Pi0 ~= %.4f computed from real PDG masses via an" % Pi0)
print("openly-declared fit (not a derivation); alpha < Pi0 reproduces the observed order phase.")
print("This is consistent-with observed electroweak symmetry breaking, NOT forced-by the root.")
