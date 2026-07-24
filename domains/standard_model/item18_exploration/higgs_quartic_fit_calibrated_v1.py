#!/usr/bin/env python3
"""
Item 18 -- Higgs quartic coupling lambda, registered as an explicit fit_calibrated value,
2026-07-24. This file is DELIBERATELY SEPARATE from higgs_quartic_DOCUMENTED_NON_RESULT_v1.py
(same folder, NOT modified here, read not touched) and makes a DIFFERENT, WEAKER, honestly-labeled
claim than that file does or than this file itself could be mistaken for.

*** WHAT higgs_quartic_DOCUMENTED_NON_RESULT_v1.py ALREADY PROVED (read, not re-litigated here):
    reconstructing m_H from lambda=m_H^2/(2*v_EW^2) reproduces the input m_H EXACTLY, for ANY m_H
    and v_EW whatsoever -- i.e. trying to use this relation to DERIVE or PREDICT m_H is a proven
    tautology, carrying zero independent bits of information. That finding stands, is not disputed,
    and this file does NOT attempt to escape it. ***

*** LEAD WITH THE LIMIT, NOT THE PARALLEL (independent review, 2026-07-24 -- corrected wording
    order): numerically, this file re-expresses one already-measured number (m_H) as another
    (lambda) via a fixed, invertible identity -- it carries ZERO independent bits of information
    beyond m_H itself, exactly the same zero-information content the sibling NON_RESULT file
    already proved. A skimming reader who reads only the top-line claim below, not this fence,
    could easily mistake "registered" for "progressed." It has NOT: item 18's real backlog ask
    (predict m_H from microscopic parameters) is exactly as unmet after this file as before it.

    WHAT THIS FILE DOES INSTEAD (a genuinely different, legitimate, but narrow move, per founder's
    explicit 2026-07-24 ruling that fitting external numbers openly-disclosed is fine, same
    standing permission as DEV-SM-001/002/003): registers lambda as a fit_calibrated VALUE,
    computed from the real measured m_H via the same standard tree-level SM identity, the way real
    SM textbooks do it and the same epistemic move as item 21's Yukawa coefficients
    (y_f=sqrt(2)*m_f/v_EW, yukawa_coefficients_v1.py) -- we FIT lambda from a measured number, we
    do NOT claim to have derived or predicted m_H. This is not "escaping the circularity" of the
    NON_RESULT file; it is doing a DIFFERENT thing that was never circular in the first place:
    citing a known number and registering the standard identity used to re-express it, openly
    tagged, for downstream fit_calibrated consumers (same shape as v_EW, sin2(theta_W), alpha_EM
    already being consumed from fit_calibrated_registry.py). Its ONLY real utility is bookkeeping
    (a future file wanting "the SM Higgs self-coupling value" can cite one place), not physics
    progress. ***

Run: python3 higgs_quartic_fit_calibrated_v1.py
"""
import math
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fit_calibrated_registry import (
    V_EW_GEV, M_HIGGS_GEV, higgs_quartic_lambda, TIER, CAVEAT,
)

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print(f"  {TIER} -- {CAVEAT}")
print("  This file registers a FIT, not a derivation and not a re-attempt at escaping the")
print("  circularity higgs_quartic_DOCUMENTED_NON_RESULT_v1.py already proved (Part 3 there, read")
print("  not modified). We do not predict m_H. We fit lambda from measured m_H, openly tagged.")

print("\n== 1. inputs (from the shared registry, DEV-SM-001) ==")
print(f"   m_H (PDG 2024, measured) = {M_HIGGS_GEV} GeV")
print(f"   v_EW (fit_calibrated_registry.py) = {V_EW_GEV} GeV")
ck("m_H > 0", M_HIGGS_GEV > 0)
ck("v_EW > 0", V_EW_GEV > 0)

print("\n== 2. lambda = m_H^2/(2*v_EW^2), the standard tree-level SM identity (cited, not derived) ==")
lam = higgs_quartic_lambda()
print(f"   lambda = {M_HIGGS_GEV}^2 / (2*{V_EW_GEV}^2) = {lam:.8f}")
ck("lambda > 0 (a real, positive quartic coupling)", lam > 0)
ck("lambda is O(0.1), matching the well-known real-SM fact (Higgs self-coupling ~0.13)",
   0.05 < lam < 0.3, lam)

print("\n== 3. cross-check against the registry's own computation (no drift between the two call sites) ==")
lam_direct = M_HIGGS_GEV**2 / (2 * V_EW_GEV**2)
ck("registry function higgs_quartic_lambda() matches direct arithmetic exactly",
   abs(lam - lam_direct) < 1e-12)

print("\n== 4. SCOPE CHECK against higgs_quartic_DOCUMENTED_NON_RESULT_v1.py's own finding ==")
print("   THIS FILE DOES NOT DISPUTE OR RE-DERIVE that file's Part 3 tautology proof. We restate")
print("   it here explicitly so no reader mistakes this file for having escaped it: reconstructing")
print("   m_H from this lambda reproduces the input exactly, for ANY m_H/v_EW -- this file does")
print("   NOT use that reconstruction as evidence of anything; it is not attempted as a prediction.")
m_H_reconstructed = math.sqrt(2 * lam) * V_EW_GEV
ck("(same tautology as the NON_RESULT file, restated not re-claimed as new evidence) "
   "reconstructed m_H equals input m_H exactly",
   abs(m_H_reconstructed - M_HIGGS_GEV) < 1e-9)
print("   The difference between the two files is NOT in this arithmetic (identical) -- it is in")
print("   what is CLAIMED about it: the NON_RESULT file correctly refuses to call this a")
print("   'registration' because item 18's backlog ask is to PREDICT m_H, which this cannot do.")
print("   This file makes the narrower, different claim that a real-SM-textbook-style FIT of")
print("   lambda from measured m_H is legitimate to register for downstream fit_calibrated use")
print("   (e.g. any future file wanting 'the SM Higgs self-coupling value' the way it already")
print("   wants 'the SM top Yukawa value'), exactly as openly-disclosed and exactly as limited as")
print("   every other fit_calibrated number in this registry.")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier fit_calibrated throughout):
- WHAT THIS ESTABLISHES: an explicit, registered fit_calibrated value for the Higgs quartic
  coupling lambda~=0.1296, computed via the standard tree-level relation lambda=m_H^2/(2*v_EW^2)
  from the real measured m_H=125.25 GeV (PDG 2024) and the already-fit_calibrated v_EW=246 GeV
  (DEV-SM-001). This is the SAME epistemic move as item 21's Yukawa registration
  (yukawa_coefficients_v1.py): a real measured number, re-expressed via a standard, cited,
  tree-level SM identity, openly tagged fit_calibrated, for downstream use.
- WHAT THIS DOES NOT ESTABLISH: (a) any prediction or derivation of m_H -- m_H is an INPUT here,
  taken from PDG, exactly as v_EW and the fermion masses already are elsewhere in this registry.
  (b) any escape from, correction to, or dispute with
  higgs_quartic_DOCUMENTED_NON_RESULT_v1.py's Part 3 finding that reconstructing m_H from this
  lambda is an exact tautology for ANY m_H/v_EW pair -- that finding is TRUE and UNCHANGED; this
  file simply never attempts to use the reconstruction as evidence of anything, so the tautology
  is not a problem for the (narrower) claim actually made here. (c) any root-native content --
  lambda=m_H^2/(2*v_EW^2) is a standard, borrowed, tree-level SM identity (see
  docs/root/EQUATION_REGISTRY.md row added alongside this file), cited not derived. (d) any
  connection to item 1 (Delta_j/alpha/kappa_j, still fully Open) -- unlike item 21's y_f, which is
  consumed nowhere in item 1's own machinery, this file's lambda is likewise NOT wired into any
  Pi0/order-criterion computation; it is a standalone registered number. (e) that item 18's actual
  backlog ask ("Physical scalar (Higgs) mass from real microscopic parameters, once item 1 is
  closed") is closed -- it is not; predicting m_H from first principles remains fully Open and
  requires item 1 first, exactly as higgs_quartic_DOCUMENTED_NON_RESULT_v1.py already states.
- This file's actual, honest contribution is NARROW BOOKKEEPING, not physics progress: it registers
  a fit_calibrated lambda value, in the same PARALLEL shape item 21 already established for the
  Yukawa couplings, so a future consumer can cite "the SM Higgs self-coupling value" from one
  place -- without contradicting or reopening the settled circularity finding in the sibling
  NON_RESULT file. Both files coexist deliberately: one proves what does NOT work (deriving m_H),
  the other registers what legitimately DOES work (fitting lambda from m_H) -- and this file
  carries zero independent bits of information beyond the m_H input itself. Do not cite this file
  as if item 18's actual backlog ask (predict m_H) made any progress; it did not.
- Independently adversarially reviewed, 2026-07-24 -- verdict SURVIVES WITH ONE FLAG (not a
  required fix): the opening docstring originally led with the parallel-to-item-21 justification
  before the limitation, risking a skimming reader mistaking "registered" for "progressed" -- now
  reordered above and in this closing fence to lead with the limit.
""")
