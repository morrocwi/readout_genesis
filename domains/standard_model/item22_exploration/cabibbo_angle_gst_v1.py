#!/usr/bin/env python3
"""
Item 22 (CKM/PMNS mixing angles) -- theta_12 (Cabibbo angle) via Gatto-Sartori-Tonin, 2026-07-24.
Tier fit_calibrated, per DRIFT_CONTRACT.json DEV-SM-003.

*** TAG: fit_calibrated. NOT derived from the root. FITTED (borrowed 1968 formula + real PDG
    masses), not derived; consistent-with, not forced-by. ***

*** THIS BYPASSES ITEM 21 (Yukawa coefficients, still fully [Open] per HANDOFF_NEXT_SESSION.md) --
    it substitutes externally-measured PDG quark masses directly for the not-yet-derived Yukawa
    couplings. Never cite this as if item 21 were closed or unnecessary. ***

Founder authorization (2026-07-24, chat): fitting broadly is fine for this item, matching the real
Standard Model's own ~19+ fitted free parameters -- "คำนวนตรงไหมกผ้พอ sm ก็ฟิตตั้ง19 ค่า" (what
matters is correct calculation, not purity). A root-native-formula construction was attempted
first (mixing_angle_from_L_R_v1.py / v2 overlap-fraction "fix") and REFUTED on its core claims by
independent review -- logged, not deleted, in ITEM22_EXPLORATION_LOG.md. This file is the
alternative, working, openly-borrowed-formula track the founder then authorized instead.

CONSTRUCTION: sin(theta_C) ~= sqrt(m_d/m_s) (Gatto-Sartori-Tonin 1968, Phys. Lett. 28B 128-130,
DOI 10.1016/0370-2693(68)90150-0 -- citation verified via primary-source search 2026-07-24),
using ONLY masses already present in fit_calibrated_registry.py (zero new free parameters beyond
what item 1's own fit already introduced). Compared against the CURRENT PDG |Vus| central value
(verified via primary-source search 2026-07-24, PDG 2024 summary-table value, NOT the earlier,
now-superseded 0.22431 figure an earlier draft of this work used).

Philosophy-translation note (per founder's own question, 2026-07-24): m_d, m_s translate directly
to this project's root-native tau_c (causal memory time, m=hbar/2*tau_c*c^2, Th_coqc per
engine/lexicon.py) -- the GST formula is, underneath its "mass" language, already a ratio of
tau_c-type quantities, i.e. it already speaks in this framework's own vocabulary at the level of
WHICH quantities are involved. What remains genuinely open -- in BOTH this framework's own terms
(H2's mass-ratio-as-relational-fixed-point hypothesis, docs/OPEN_PROBLEM_HYPOTHESES.md, tier Open)
and in real physics -- is WHY this particular ratio (not some other function of m_d,m_s) predicts
the mixing angle. This file does not close that gap; it uses the borrowed formula exactly as
declared, no more.

Run: python3 cabibbo_angle_gst_v1.py
"""
import math

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory, DEV-SM-003) ==")
print("  fit_calibrated -- FITTED (borrowed 1968 formula + PDG masses), not derived from the")
print("  root; consistent-with, not forced-by. BYPASSES item 21 (Yukawa, still [Open]).")

print("\n== 1. inputs: same PDG masses already in fit_calibrated_registry.py ==")
m_d, m_s = 0.00467, 0.0934  # GeV, PDG 2024, same values item1's work already uses
print(f"   m_d = {m_d} GeV, m_s = {m_s} GeV")

print("\n== 2. Gatto-Sartori-Tonin: sin(theta_C) ~= sqrt(m_d/m_s) ==")
sin_theta_c = math.sqrt(m_d / m_s)
theta_c_deg = math.degrees(math.asin(sin_theta_c))
print(f"   sin(theta_C) predicted = {sin_theta_c:.6f}")
print(f"   theta_C predicted = {theta_c_deg:.4f} deg  (this IS a physics-textbook angle citation,")
print(f"   not a claim about this project's own root vocabulary -- see philosophy-translation note")
print(f"   above; theta_12 is real physics's own natural readout of this externally-borrowed formula)")

print("\n== 3. compare to PDG |Vus| (verified current value, 2026-07-24) ==")
Vus_pdg = 0.2250  # PDG 2024 summary-table central value, +/-0.0004 (primary-source verified)
Vus_pdg_unc = 0.0004
rel_err = abs(Vus_pdg - sin_theta_c) / Vus_pdg
sigma = abs(Vus_pdg - sin_theta_c) / Vus_pdg_unc
print(f"   |Vus|_PDG = {Vus_pdg} +/- {Vus_pdg_unc}")
print(f"   relative error on sin(theta_C) = {rel_err*100:.3f}%  ({sigma:.1f} sigma on PDG's own quoted uncertainty)")
ck("prediction lands within a few percent of the real PDG value (point comparison only -- PDG "
   "uncertainties on m_d,m_s themselves NOT propagated into a predicted-value error band)",
   rel_err < 0.02, rel_err)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier fit_calibrated, per DRIFT_CONTRACT.json DEV-SM-003 -- read that entry's "risk"
field before citing this result anywhere):
- WHAT THIS ESTABLISHES: a genuinely minimal-free-parameter (zero NEW free parameters beyond
  item 1's own already-fit_calibrated m_d,m_s) match between a borrowed 1968 phenomenological
  relation and this repo's own PDG masses, landing within ~0.6% of the current PDG |Vus| central
  value.
- WHAT THIS DOES NOT ESTABLISH: (a) any derivation of theta_12's value from the root -- the GST
  relation is an externally-borrowed 1968 formula, cited not derived. (b) theta_13 or theta_23 --
  both tested analogous mass-ratio candidates (sqrt(m_c/m_t), sqrt(m_s/m_b), and their product)
  failed by factors of 2-5x against real PDG values; reported Open, not forced. (c) any PMNS
  angle -- untouched, blocked on item 23 (neutrino architecture, Dirac vs Majorana), itself fully
  Open; PMNS angles are also numerically near-maximal (~33deg,~49deg,~8.5deg) rather than
  hierarchical like CKM, so this small-mixing-ratio ansatz has no reason to apply even
  heuristically. (d) that item 21 (Yukawa coefficients) is closed -- this BYPASSES it by
  substituting measured masses; every citation of this result must say so. (e) statistical rigor
  -- the ~0.6% agreement is a point-value comparison only; PDG uncertainties on m_d,m_s themselves
  (both O(few-to-tens-of-percent) for these light-quark masses) are NOT propagated into a
  predicted-value error band. (f) any claim that the mass-ratio-relation APPROACH generalizes --
  it works for theta_12 only; the same approach fails for theta_13/theta_23, an asymmetry reported
  honestly, not smoothed over.
- Does not weaken DRIFT_CONTRACT.json hard_fail_conditions[4] (mixing-angle-derived-from-root
  ban); nothing here claims theta_12 is forced or proven, or that the mixing angle has a root-
  native definition (the attempt at one, mixing_angle_from_L_R_v1/v2.py, was REFUTED -- see
  ITEM22_EXPLORATION_LOG.md).
""")
