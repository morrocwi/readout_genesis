#!/usr/bin/env python3
"""
Panel A's proposed target: fit ONE global scale c, combined with v1.13's ALREADY ROOT-DERIVED
rank d_j=(3,3,1) (not fit -- from representation theory, Hom_G dimension counting), via
lambda_j := exp(-c*d_j). Test whether this correctly orders the three branches against real
PDG masses. Tier: fit_calibrated (DEV-SM-001). Result reported as-is, no outcome predicted
in advance (2026-07-24 discipline).
"""
import math

d = {'U': 3, 'D': 3, 'E': 1}   # v1.13's ROOT-DERIVED rank (Hom_G dim counting), NOT fit
gm = {'U': 0.779260, 'D': 0.122165, 'E': 0.045785}   # real PDG geometric means (GeV), from Attempt 5

print("== structural limitation, stated BEFORE running anything (not an outcome) ==")
print("  d_U = d_D = 3 (both branches share the SAME root-derived rank) => ANY function of")
print("  d_j alone gives lambda_U = lambda_D EXACTLY, for ANY choice of c. This form structurally")
print("  CANNOT distinguish U from D -- it can only test 'quarks (together) vs lepton'.")

print("\n== fit c: single free parameter, solved from ONE real data point (use geomean(U,D) vs E) ==")
# with lambda_j = exp(-c*d_j), only 2 distinct groups exist: quarks (d=3), lepton (d=1).
# fit c so lambda_quark/lambda_lepton ratio matches the real gm_quark/gm_lepton scale, using
# ONE equation (2 unknowns c and v cannot both be fit from 1 ratio; fix v_EW=246 as before,
# fit c to match the real geometric-mean RATIO of quark-to-lepton mass scale).
gm_quark = (gm['U'] * gm['D']) ** 0.5   # combine U,D into the single 'quark' group this model can see
ratio_real = gm_quark / gm['E']
print(f"  real gm_quark (sqrt(gm_U*gm_D)) = {gm_quark:.6f} GeV, gm_E = {gm['E']:.6f} GeV")
print(f"  real ratio gm_quark/gm_E = {ratio_real:.4f}")

v_EW = 246.0
# lambda_j = exp(-c*d_j) = exp(-m_j/v_EW)  =>  c*d_j = m_j/v_EW  =>  for the 'quark' group (d=3):
# c = m_quark/(3*v_EW); for lepton (d=1): c = m_E/v_EW. These 2 equations generally disagree
# (that disagreement IS the test) -- report both, do not average them away.
c_from_quark = gm_quark / (3 * v_EW)
c_from_lepton = gm['E'] / (1 * v_EW)
print(f"\n  c implied by quark branch (d=3): c = gm_quark/(3*v_EW) = {c_from_quark:.6f}")
print(f"  c implied by lepton branch (d=1): c = gm_E/(1*v_EW)     = {c_from_lepton:.6f}")
print(f"  ratio (quark-implied c) / (lepton-implied c) = {c_from_quark/c_from_lepton:.4f}")
print("  (if this were close to 1, ONE shared c would fit both groups; the actual ratio is the")
print("  real, unmassaged result of this test -- reported as computed, not adjusted)")

print("\n== ordering test: does d_j=(3,3,1) alone predict the correct qualitative ordering? ==")
qualitative_prediction = "m_quark > m_lepton (since d_quark=3 > d_lepton=1, more root-derived rank => more retained structure => this model's convention associates higher d_j with lower lambda_j => higher mass, IF c>0)"
real_ordering = gm_quark > gm['E']
print(f"  Prediction (structural, from d_j ordering alone, c>0 assumed): quarks heavier than lepton")
print(f"  Real data: gm_quark={gm_quark:.4f} GeV vs gm_E={gm['E']:.4f} GeV -> quarks heavier: {real_ordering}")
print(f"  QUALITATIVE (2-way) ordering test result: {'MATCHES' if real_ordering else 'DOES NOT MATCH'}")

print("\n== what this test explicitly does NOT check (stated, not hidden) ==")
print("  - Does NOT distinguish U from D (structurally impossible with d_j alone, d_U=d_D=3)")
print("  - Does NOT produce a single shared c (the two implied c values differ by the ratio above")
print("    -- this IS the quantitative content of the test, not swept under a fit)")
print("  - This is fit_calibrated tier: FITTED/checked against real data, NOT derived from the")
print("    root; consistent-with (if it matches) or inconsistent-with (if it doesn't), never forced-by")
