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

# ---- strong sector, real-world value (added for item18/25/26 fit_calibrated registration sweep,
#      2026-07-24) ----
ALPHA_S_MZ = 0.1180               # PDG 2024, strong coupling constant alpha_s(M_Z), MSbar scheme

# ---- QCD vacuum angle -- an UPPER BOUND, NOT a measured central value. Real neutron-EDM
#      non-observation experiments (nEDM Collaboration and predecessors) constrain |theta_QCD| to
#      be extremely small; no experiment has ever measured a nonzero value. This is the "strong CP
#      problem": WHY theta_QCD is so small (or exactly zero) is a famous OPEN question in real
#      physics itself, not resolved by any mechanism in this repo or by registering the bound. Do
#      NOT treat this as a point value with false precision -- it is a one-sided experimental
#      constraint. ----
THETA_QCD_UPPER_BOUND = 1e-10     # PDG-cited neutron EDM bound (order-of-magnitude; |theta_QCD| <~ 1e-10)
THETA_QCD_NOTE = ("theta_QCD is an EXPERIMENTAL UPPER BOUND (neutron EDM non-observation), not a "
                   "measured central value. WHY it is this small (the 'strong CP problem') is a "
                   "genuinely open question in real physics -- registering the bound here is NOT a "
                   "resolution of that question, and this repo does not attempt one.")

# ---- Higgs sector, real-world value (added for item18 fit_calibrated registration sweep,
#      2026-07-24) ----
M_HIGGS_GEV = 125.25               # PDG 2024, real measured Higgs boson mass


def higgs_quartic_lambda(m_h=M_HIGGS_GEV, v_ew=V_EW_GEV):
    """Tree-level SM identity lambda = m_H^2/(2*v_EW^2). fit_calibrated -- see
    item18_exploration/higgs_quartic_fit_calibrated_v1.py for the honest-fence discussion of why
    this is a FIT (both m_H and this relation are cited, not derived), not a prediction of m_H."""
    return m_h**2 / (2.0 * v_ew**2)


# ---- neutrino oscillation sector, real-world values. Real experiments measure ONLY mass-SQUARED
#      DIFFERENCES, never absolute masses -- do not fabricate absolute values here. NuFIT/PDG 2024
#      global-fit central values (normal ordering), in eV^2. ----
DELTA_M2_21_EV2 = 7.53e-5          # PDG/NuFIT global fit, solar mass-squared splitting (eV^2)
DELTA_M2_31_EV2 = 2.455e-3         # PDG/NuFIT global fit, atmospheric mass-squared splitting, normal ordering (eV^2)
NEUTRINO_MASS_NOTE = ("Only mass-SQUARED DIFFERENCES (Delta m^2) are measured by real oscillation "
                       "experiments. The absolute neutrino mass scale and the mass ordering "
                       "(normal vs inverted) remain genuinely OPEN in real physics -- no absolute "
                       "mass value is registered here because none exists in the data.")


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
    print(f"alpha_s(M_Z) = {ALPHA_S_MZ}")
    print(f"theta_QCD <~ {THETA_QCD_UPPER_BOUND:.0e} (UPPER BOUND, not a point value) -- {THETA_QCD_NOTE}")
    print(f"m_H = {M_HIGGS_GEV} GeV -> lambda (tree-level, fit_calibrated) = {higgs_quartic_lambda():.8f}")
    print(f"Delta m^2_21 = {DELTA_M2_21_EV2:.4e} eV^2, Delta m^2_31 = {DELTA_M2_31_EV2:.4e} eV^2 -- {NEUTRINO_MASS_NOTE}")
