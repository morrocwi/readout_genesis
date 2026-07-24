#!/usr/bin/env python3
"""
Item 21 -- Yukawa coefficients, fit_calibrated tier, 2026-07-24. Closes the "bypass" that
cabibbo_angle_gst_v1.py, gst_mechanism_texture_zero_v1.py, fritzsch_texture_3x3_v1.py, and
fritzsch_two_sector_ckm_v1.py all explicitly disclosed: those files substitute real PDG MASSES
for the not-yet-derived Yukawa COUPLINGS. This file makes that substitution EXPLICIT and
COMPUTED, rather than an implicit bypass -- the standard-model relation between mass and Yukawa
coupling is exact and trivial once v_EW is taken as given (already fit_calibrated in this repo,
DEV-SM-001): y_f := sqrt(2)*m_f/v_EW. There is no new physics content here beyond that one
textbook identity; what this file adds is making the number EXIST and be REGISTERED, so future
work can cite y_f directly instead of re-deriving it ad hoc or leaving item 21 an unexamined gap.

*** TAG: fit_calibrated. NOT derived from the root. The masses (fit_calibrated, DEV-SM-001) and
    the relation y_f=sqrt(2)m_f/v_EW (a standard, borrowed SM identity, tree-level, cited not
    derived) combine to give y_f its own fit_calibrated tier -- never cite y_f as "derived." ***

WHAT THIS DOES NOT CLOSE: item 21's actual open content is WHY the Yukawa couplings have the
values they do (the mass-hierarchy problem) -- this file only COMPUTES them from already-known
masses via an exact, standard, tree-level relation. It is exactly as open afterward as the mass
values themselves were before it ran; it converts "item 21 is an unexamined bypass" into "item 21
is an explicit, registered fit_calibrated number with the same open status as item 1's masses,"
which is real, disclosed progress (removes 4 files' worth of implicit bypassing) but not a
derivation of anything new.

Run: python3 yukawa_coefficients_v1.py
"""
import math
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fit_calibrated_registry import PDG_MASSES_GEV, V_EW_GEV

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print("  fit_calibrated -- FITTED (real masses + standard tree-level SM relation), not derived")
print("  from the root; consistent-with, not forced-by.")

print("\n== 1. y_f := sqrt(2)*m_f/v_EW for all 9 fermions in the shared registry ==")
print(f"   v_EW = {V_EW_GEV} GeV (fit_calibrated_registry.py, DEV-SM-001)")
yukawa = {}
for f, m in PDG_MASSES_GEV.items():
    y = math.sqrt(2) * m / V_EW_GEV
    yukawa[f] = y
    print(f"   y_{f:4s} = sqrt(2)*{m}/{V_EW_GEV} = {y:.8e}")
    ck(f"y_{f} > 0 (a real Yukawa coupling)", y > 0)

print("\n== 2. sanity checks against known SM facts (reproduced, not fitted separately) ==")
ck("y_t (top) is O(1) -- the well-known fact that the top Yukawa is close to unity",
   0.9 < yukawa['t'] < 1.1, yukawa['t'])
ck("y_e (electron) is the smallest Yukawa coupling among all 9 (real PDG fact: the electron is "
   "the lightest of all 9 fermions, lighter even than the up quark) -- an earlier draft of this "
   "check wrongly assumed y_u would be smallest; self-caught and corrected before review",
   min(yukawa, key=yukawa.get) == 'e', min(yukawa, key=yukawa.get))
ck("Yukawa couplings preserve the same branch-internal ordering as the masses themselves "
   "(monotonic, since y_f=sqrt(2)m_f/v_EW is linear in m_f)",
   yukawa['u'] < yukawa['c'] < yukawa['t'] and
   yukawa['d'] < yukawa['s'] < yukawa['b'] and
   yukawa['e'] < yukawa['mu'] < yukawa['tau'])

print("\n== 3. cross-reference: does this match item 1's own Pi0/lambda machinery? ==")
print("   item1_fit_calibrated_v1.py uses lambda_j := exp(-m_j/v_EW) (an EXPONENTIAL order-")
print("   parameter, v1.13's own intertwiner-order construction) -- a DIFFERENT functional form")
print("   of m_j/v_EW than y_f=sqrt(2)*m_j/v_EW (LINEAR, the standard SM Yukawa relation).")
print("   Both are legitimate, independently-motivated readouts of the SAME ratio m_j/v_EW for")
print("   DIFFERENT purposes (lambda_j = order/closure parameter; y_f = coupling strength) -- NOT")
print("   claimed to be the same quantity or convertible into one another without a stated map.")
lam_t_style = math.exp(-PDG_MASSES_GEV['t'] / V_EW_GEV)
print(f"   (illustration only: exp(-m_t/v_EW) = {lam_t_style:.6f}, vs y_t = {yukawa['t']:.6f} --")
print(f"   visibly different numbers from the same m_t/v_EW input, confirming these are genuinely")
print(f"   different constructions, not a relabeling of one number.)")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier fit_calibrated throughout):
- WHAT THIS ESTABLISHES: an explicit, registered fit_calibrated value for all 9 Standard-Model
  Yukawa couplings, computed via the standard tree-level relation y_f=sqrt(2)*m_f/v_EW from
  already-fit_calibrated masses and v_EW (DEV-SM-001). Removes the implicit bypass that 4 other
  files in this domain (cabibbo_angle_gst_v1.py, gst_mechanism_texture_zero_v1.py,
  fritzsch_texture_3x3_v1.py, fritzsch_two_sector_ckm_v1.py) each separately disclosed but never
  made explicit or registered.
- WHAT THIS DOES NOT ESTABLISH: (a) any explanation of WHY the Yukawa couplings have the values
  they do -- this is the SAME open mass-hierarchy problem as before, merely renamed/re-expressed;
  y_f is exactly as unexplained as m_f was. (b) any root-native derivation -- the relation
  y_f=sqrt(2)m_f/v_EW is a standard, borrowed, tree-level SM identity (cited, needs registering in
  docs/root/EQUATION_REGISTRY.md if not already covered by the existing electroweak-mixing/Fermi-
  coupling rows there), not built from this project's own primitives. (c) any connection to item
  1's lambda_j (intertwiner order parameter) -- confirmed in Part 3 above to be a DIFFERENT
  functional form of the same input ratio, not the same quantity; do not conflate the two in any
  downstream citation (a fresh instance of the Cross-Role Readout Contamination pattern this
  domain's checklist warns about, avoided here by explicit comparison). (d) that this closes item
  21's backlog entry -- item 21 asks for the Yukawa coefficients to be DERIVED (needs items 1, 18,
  both still Open); this file only computes their fit_calibrated VALUES from already-known masses,
  which is a real but limited form of progress (an explicit registered number instead of an
  implicit bypass), not a derivation.
- Not yet independently adversarially reviewed -- per house discipline, needs that review before
  being treated as more than a first-pass draft.
""")
