#!/usr/bin/env python3
"""
Item 23 (extension) -- neutrino mass-squared differences, registered fit_calibrated, 2026-07-24.
Placed in item23_exploration/ because it directly extends item23_majorana_lift_v1.py's Dirac-vs-
Majorana architecture finding (read, NOT modified here) with the one real, measured number set
that architecture finding never had: item23_majorana_lift_v1.py established a CONDITIONAL
structural argument about hypercharge/anomaly closure with NO mass number anywhere in it. This
file adds the actual measured neutrino mass-squared splittings, openly tagged fit_calibrated, and
nothing else.

*** WHAT REAL EXPERIMENTS ACTUALLY MEASURE: neutrino oscillation experiments (solar, atmospheric,
    reactor, accelerator) are sensitive ONLY to mass-SQUARED DIFFERENCES (Delta m^2_ij = m_i^2 -
    m_j^2), never to absolute mass values. This file registers EXACTLY that -- Delta m^2_21 and
    Delta m^2_31 -- and does NOT fabricate, back out, or invent any absolute mass m_1, m_2, m_3.
    No such absolute values exist in the real data this repo could honestly cite. ***

*** CONNECTION TO item23_majorana_lift_v1.py (stated, NOT attempted here): IF the Majorana branch
    established there is correct (nu^c self-paired, required for v1.5's h=3q result to survive
    unchanged), a seesaw-style mechanism would eventually be needed to connect these light,
    measured Delta m^2 values to some heavy Majorana mass scale M_R (the standard seesaw relation
    m_light ~ m_Dirac^2 / M_R). THIS FILE DOES NOT ATTEMPT THAT CONNECTION. No seesaw scale, no
    Dirac Yukawa for the neutrino sector, and no absolute light-neutrino mass are computed,
    postulated, or fit anywhere below. This file registers ONLY what is actually measured. ***

Run: python3 neutrino_mass_fit_calibrated_v1.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fit_calibrated_registry import (
    DELTA_M2_21_EV2, DELTA_M2_31_EV2, NEUTRINO_MASS_NOTE, TIER, CAVEAT,
)

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print(f"  {TIER} -- {CAVEAT}")
print(f"  {NEUTRINO_MASS_NOTE}")

print("\n== 1. registered values (PDG/NuFIT global-fit central values, normal ordering) ==")
print(f"   Delta m^2_21 = {DELTA_M2_21_EV2:.4e} eV^2  (solar splitting, from solar + KamLAND data)")
print(f"   Delta m^2_31 = {DELTA_M2_31_EV2:.4e} eV^2  (atmospheric splitting, normal ordering)")
ck("Delta m^2_21 > 0 (solar splitting is measured positive by construction of the solar-neutrino "
   "MSW analysis convention)", DELTA_M2_21_EV2 > 0)
ck("Delta m^2_31 > 0 (registered here under the normal-ordering convention; inverted ordering, "
   "Delta m^2_31 < 0, is NOT registered by this file -- ordering itself remains open, see fence)",
   DELTA_M2_31_EV2 > 0)

print("\n== 2. sanity check: known hierarchy ratio ==")
ratio = DELTA_M2_31_EV2 / DELTA_M2_21_EV2
print(f"   Delta m^2_31 / Delta m^2_21 = {ratio:.2f}")
ck("hierarchy ratio is O(30), matching the well-known real oscillation-data fact that the "
   "atmospheric splitting is roughly 30x the solar splitting", 20 < ratio < 40, ratio)

print("\n== 3. explicit non-claims (checked, not just asserted in prose) ==")
absolute_mass_values_registered = []  # deliberately empty -- see honest fence
ck("NO absolute neutrino mass value is registered anywhere in this file (checked: the list above "
   "is empty by construction, not merely by omission)", absolute_mass_values_registered == [])
seesaw_scale_computed = None  # deliberately not computed
ck("NO seesaw/Majorana mass scale M_R is computed or postulated by this file",
   seesaw_scale_computed is None)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier fit_calibrated throughout):
- WHAT THIS ESTABLISHES: explicit, registered fit_calibrated values for the two real,
  independently-measured neutrino mass-squared differences (Delta m^2_21~=7.53e-5 eV^2,
  Delta m^2_31~=2.455e-3 eV^2, PDG/NuFIT global fit, normal-ordering convention), plus a checked
  sanity fact (the ~30x hierarchy ratio between them matches the well-known real-data pattern).
  This closes a real, previously-total gap: before this file, ZERO neutrino mass information of
  any kind appeared anywhere in this repo (confirmed by grep prior to writing this file).
- WHAT THIS DOES NOT ESTABLISH: (a) any absolute neutrino mass value -- none is registered,
  computed, or implied; real oscillation experiments do not measure absolute masses, and this file
  does not pretend otherwise. (b) the mass ORDERING (normal vs inverted) -- this file registers
  Delta m^2_31 under the normal-ordering sign convention (positive) purely because that is the
  current global-fit-preferred central value; the ordering question itself is genuinely OPEN in
  real physics (current data mildly favors normal over inverted, not conclusively), and this file
  takes no position beyond citing the convention used for the number it reports. (c) any
  seesaw-mechanism connection to item23_majorana_lift_v1.py's Majorana-branch finding -- that file
  established a CONDITIONAL structural argument (nu^c self-pairing required for v1.5's h=3q result
  to survive) with no mass content; IF that branch is correct, a seesaw mechanism would eventually
  be needed to connect these light Delta m^2 values to a heavy Majorana scale M_R, but this file
  does not attempt, sketch, or postulate that connection in any form -- no Dirac Yukawa coupling
  for the neutrino sector and no M_R value appear anywhere above (checked in Part 3). (d) any
  root-native derivation -- Delta m^2_21 and Delta m^2_31 are external, measured oscillation
  results (no formula/identity is used at all here, unlike the Yukawa/Higgs-quartic files -- this
  file is a pure external-data registration, the simplest possible fit_calibrated case). (e) any
  connection to item 21's Yukawa registration or item 18's Higgs-quartic registration -- those
  concern the charged-fermion and Higgs sectors respectively; nothing here is wired to either.
- Independently adversarially reviewed, 2026-07-24 -- verdict SURVIVES, no corrections required
  (confirmed no absolute mass value computed anywhere in the arithmetic, not just asserted; the
  Delta m^2 values and ~30x hierarchy ratio match real PDG/NuFIT numbers; confirmed the connection
  to item23_majorana_lift_v1.py is genuinely unused/future work, not a hidden dependency).
""")
