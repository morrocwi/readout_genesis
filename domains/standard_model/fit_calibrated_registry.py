#!/usr/bin/env python3
"""
fit_calibrated_registry.py -- the SINGLE shared source of every fit_calibrated (DEV-SM-001)
external number used anywhere in domains/standard_model/. Built 2026-07-24 in direct response
to a real, confirmed gap: before this file, `item1_fit_calibrated_v1.py` was the ONLY consumer
of any fit_calibrated value anywhere in this domain (confirmed by grep: no other .py file
referenced lambda_j/Pi0/v_EW) -- i.e. no cross-computation, no shared registry, every fit was an
island. This file exists so future fit_calibrated scripts import ONE consistent set of numbers
instead of each hand-copying its own constants (which would silently drift and violate
DEV-SM-001's own "same caveat on every citation" compensating control).

*** TIER: every value below is `fit_calibrated` (DRIFT_CONTRACT.json DEV-SM-001). FITTED /
    externally measured, NOT derived from the root; consistent-with, not forced-by. Importing
    this module does NOT upgrade any downstream computation's tier -- the importer inherits
    fit_calibrated status for anything it computes FROM these values, and must say so. ***

Sources: PDG 2024 central values (fermion masses, sin^2(theta_W), alpha_EM); v_EW is the
real-world electroweak vacuum expectation value. None of these are derived anywhere in this
repo -- order_higgs_closure_v1_12.py explicitly leaves its own symbolic scale [Open]/"NOT
predicted" (checked 2026-07-24, see item1_exploration/ITEM1_EXPLORATION_LOG.md Attempt 5).
"""
import math

TIER = "fit_calibrated"
CAVEAT = "FITTED/measured, NOT derived from the root; consistent-with, not forced-by (DEV-SM-001)"

# ---- PDG 2024 fermion masses (GeV), central values ----
PDG_MASSES_GEV = {
    'u': 0.00216, 'c': 1.27,   't': 172.5,
    'd': 0.00467, 's': 0.0934, 'b': 4.18,
    'e': 0.000511, 'mu': 0.1057, 'tau': 1.777,
}

# ---- electroweak sector, real-world values ----
V_EW_GEV = 246.0                 # real electroweak vacuum expectation value
SIN2_THETA_W = 0.23122           # PDG, MSbar scheme at M_Z
ALPHA_EM = 1/137.035999          # PDG, low-energy fine-structure constant

# ---- PDG boson masses, for comparison ONLY (never used as an input to any computation below --
#      kept here purely as the independent check target for downstream consumers) ----
PDG_MW_GEV = 80.377
PDG_MZ_GEV = 91.1876


def branch_geomean(members):
    """Geometric mean of PDG_MASSES_GEV[name] for name in members. Same convention as Attempt 5."""
    vals = [PDG_MASSES_GEV[m] for m in members]
    prod = 1.0
    for v in vals:
        prod *= v
    return prod ** (1.0 / len(vals))


def branch_lambdas(v_ew=V_EW_GEV):
    """lambda_j := exp(-geomean(branch)/v_ew) for U,D,E -- same formula as item1_fit_calibrated_v1.py,
    now sourced from this shared registry instead of a hand-copied literal."""
    gm_U = branch_geomean(['u', 'c', 't'])
    gm_D = branch_geomean(['d', 's', 'b'])
    gm_E = branch_geomean(['e', 'mu', 'tau'])
    return {
        'U': math.exp(-gm_U / v_ew),
        'D': math.exp(-gm_D / v_ew),
        'E': math.exp(-gm_E / v_ew),
    }


def pi0(v_ew=V_EW_GEV):
    """Pi0 = 3*lambda_U + 3*lambda_D + lambda_E, v1.13's own formula, fed from this registry."""
    lam = branch_lambdas(v_ew)
    return 3*lam['U'] + 3*lam['D'] + lam['E']


if __name__ == "__main__":
    print(f"TIER: {TIER} -- {CAVEAT}")
    lam = branch_lambdas()
    print(f"lambda_U={lam['U']:.8f} lambda_D={lam['D']:.8f} lambda_E={lam['E']:.8f}")
    print(f"Pi0 = {pi0():.8f}")
    print(f"v_EW = {V_EW_GEV} GeV, sin2(theta_W) = {SIN2_THETA_W}, alpha_EM = {ALPHA_EM:.8f}")
    print(f"PDG comparison targets (not inputs): m_W={PDG_MW_GEV} GeV, m_Z={PDG_MZ_GEV} GeV")
