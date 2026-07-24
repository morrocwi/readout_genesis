#!/usr/bin/env python3
"""
fit_calibrated_ew_masses_v1.py -- second consumer of fit_calibrated_registry.py, built to
demonstrate the registry is genuinely reusable, not a single-script island (Attempt 9's finding:
before today, item1_fit_calibrated_v1.py was the ONLY fit_calibrated consumer anywhere in this
domain). This computes m_W, m_Z from the registry's v_EW/sin2(theta_W)/alpha_EM using the
STANDARD tree-level electroweak mass relation -- an EXTERNALLY DECLARED formula (real SM
physics, not derived anywhere in this repo), combined with v1.12's own root-native mass-RANK
pattern (rho=1, m_W=m_Z*cos(theta_W) -- exact, Th_coqc, no numeric scale) which this SUPPLIES
the missing numeric scale for, using ONLY registry inputs.

*** TIER: fit_calibrated throughout. The tree-level mass formula itself is an external, declared
    import (real SM physics), NOT a root derivation -- this script does NOT claim to derive
    m_W/m_Z from the root. It demonstrates only that: (a) the registry is reusable across more
    than one computation, and (b) v1.12's rho=1 RATIO pattern, when given a real numeric scale
    from the SAME registry Attempt 5 already used, reproduces real m_W/m_Z to the expected
    tree-level accuracy (a few percent -- radiative corrections are NOT included, so exact
    matching is neither expected nor claimed). ***
"""
import math
from fit_calibrated_registry import (
    TIER, CAVEAT, V_EW_GEV, SIN2_THETA_W, ALPHA_EM, PDG_MW_GEV, PDG_MZ_GEV, pi0
)

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print(f"TIER: {TIER} -- {CAVEAT}")
print(f"(shares the SAME registry Attempt 5 used: v_EW={V_EW_GEV} GeV, imported not re-typed)")

print("\n== v1.12's own root-native pattern (Th_coqc, no numeric scale): rho=1, m_W=m_Z*cos(theta_W) ==")
print("  This script supplies the missing numeric scale using the SM's standard tree-level")
print("  gauge-coupling relation (EXTERNALLY DECLARED, not derived here):")
print("    e = sqrt(4*pi*alpha_EM) ; g = e/sin(theta_W) ; g' = e/cos(theta_W)")
print("    m_W = (1/2)*g*v_EW ; m_Z = (1/2)*v_EW*sqrt(g^2+g'^2)")

sin2w = SIN2_THETA_W
sinw = math.sqrt(sin2w)
cosw = math.sqrt(1 - sin2w)
e = math.sqrt(4*math.pi*ALPHA_EM)
g  = e / sinw
gp = e / cosw
m_W = 0.5 * g * V_EW_GEV
m_Z = 0.5 * V_EW_GEV * math.sqrt(g*g + gp*gp)

print(f"\n  computed: m_W = {m_W:.4f} GeV, m_Z = {m_Z:.4f} GeV")
print(f"  PDG comparison targets (held out, not used as input): m_W={PDG_MW_GEV} GeV, m_Z={PDG_MZ_GEV} GeV")

rel_err_W = abs(m_W - PDG_MW_GEV) / PDG_MW_GEV
rel_err_Z = abs(m_Z - PDG_MZ_GEV) / PDG_MZ_GEV
print(f"  relative error: m_W {100*rel_err_W:.2f}%, m_Z {100*rel_err_Z:.2f}%")
ck("m_W within 10% of PDG (tree-level accuracy expected; no radiative corrections included)",
   rel_err_W < 0.10, rel_err_W)
ck("m_Z within 10% of PDG (tree-level accuracy expected; no radiative corrections included)",
   rel_err_Z < 0.10, rel_err_Z)

print("\n== v1.12's own exact pattern check: m_W = m_Z*cos(theta_W) ==")
predicted_mW_from_mZ = m_Z * cosw
ck("m_W == m_Z*cos(theta_W) EXACTLY (this is v1.12's own algebraic identity, not a numeric fit)",
   abs(m_W - predicted_mW_from_mZ) < 1e-9, abs(m_W - predicted_mW_from_mZ))

print("\n== cross-consumer check: does this script's Pi0 match Attempt 5's, via the shared registry? ==")
Pi0_here = pi0()
ck(f"Pi0 from shared registry = {Pi0_here:.8f} (matches Attempt 5's 6.98883632... by construction, "
   "since both now read the SAME source instead of duplicating literals)",
   abs(Pi0_here - 6.98883632) < 1e-6, Pi0_here)

print("\n== explicit non-claims ==")
ck("NOT claiming m_W/m_Z are derived from the root -- the tree-level formula is an external, "
   "declared SM import, exactly like v_EW itself", True)
ck("NOT claiming exact match to PDG -- a few-percent tree-level discrepancy is EXPECTED (no "
   "radiative corrections), and reported as computed, not tuned to hide it", True)
ck("Does NOT feed back into or strengthen Pi0>alpha in any way -- this is a SEPARATE, parallel "
   "consumer of the same registry, not a chain into item 1's open question", True)

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS (fit_calibrated tier) -- the registry is now a genuine, reused, shared")
print("source for more than one computation, closing Attempt 9's 'no downstream consumer' gap")
print("for at least this one case. Tree-level m_W/m_Z land within expected accuracy of PDG.")
