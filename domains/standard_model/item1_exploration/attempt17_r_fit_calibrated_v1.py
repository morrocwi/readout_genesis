#!/usr/bin/env python3
"""
Item 1 -- Attempt 17, 2026-07-25: registers r as an explicit fit_calibrated value, per the
founder's own standing directive this session ("fit is fine, real SM fits ~19 values too -- do not
demand more of this program than the Standard Model itself delivers," DRIFT_CONTRACT.json
DEV-SM-001). Attempts 10-16 exhaustively searched for a ROOT-NATIVE source of r (the sole remaining
free parameter in Attempts 13-14's Z-action mechanism, the only construction found to escape every
degeneracy obstruction) and found none -- this file stops searching and FITS r instead, exactly the
same epistemic move as item 21's Yukawa coefficients or item 18's Higgs quartic lambda.

A CITED PRECEDENT, SCOPE CORRECTED after independent review, 2026-07-25 (an earlier draft
overstated this): the founder pointed at this session's Fritzsch texture-zero construction
(item22/24, `fritzsch_extended_texture_v1.py`/`cp_phase_jarlskog_v1.py`), which reproduces all 3
CKM magnitudes AND the Jarlskog CP invariant using only 2 EXPLICIT free parameters (`D_up`, `phi`)
against the real SM's own 10-parameter quark-sector count -- a founder-approved, `DEV-SM-003`-
declared REDUCTION (10 down to effectively 8, `SESSION_2026_07_24_PARAMETER_ECONOMY_SUMMARY.md`
gives the accurate whole-system figure, 2/19). REVIEW CAUGHT AN OVERSTATEMENT: this file achieves
NO comparable parameter-count reduction -- Attempts 13-14's Z-action mechanism (what r_U/r_D/r_E
feed) is not part of the standard 19-parameter SM accounting at all, so there is no baseline count
being reduced here; citing Fritzsch's success by name risked borrowing its credibility for an
unrelated claim. The only fair, narrower connection: both follow the same STANDING PERMISSION
(fit openly, minimally, disclosed) that DEV-SM-001 grants, not the same kind of accomplishment.
r_U/r_D/r_E are ARITHMETIC FUNCTIONS (geometric mean) of the 9 masses ALREADY registered in
`fit_calibrated_registry.py`, adding no new independently-fit number -- but this is NOT the same
epistemic move as item 21's Yukawa coefficients (`y_f=sqrt(2)*m_f/v_EW`), a further overstatement
also corrected here: Yukawa's formula is INJECTIVE (9 masses -> 9 distinct outputs, an exact,
invertible, borrowed textbook identity, no information discarded). This file's geometric mean is
LOSSY (3 masses -> 2 ratios -> 1 averaged number per branch, discarding that the two ratios differ
-- checked exactly in Part 1 below) -- genuinely cruder, and the specific choice of geometric mean
(over, say, a least-squares fit weighting the middle generation) is itself a real, if narrow,
modeling decision the Yukawa case never has to make.

WHY THREE r's, NOT ONE (an honest correction to Attempts 13-14's own framing, made explicit here):
Attempts 13-14 always spoke of "one r" applied uniformly across "3 generations." Real PDG masses
immediately refute a SINGLE uniform r: consecutive-generation ratios are NOT constant within any
branch (checked below, exactly). The honest fit_calibrated move is therefore per-branch (matching
this domain's own existing branch structure, U/D/E, already used throughout item 1's own
`fit_calibrated_registry.py`): register r_U, r_D, r_E as the GEOMETRIC MEAN of each branch's two
consecutive mass ratios -- the natural, standard "average growth rate" summary of an exponential-
shaped 3-point sequence, openly disclosed as an AVERAGE, not an exact reproduction of either
individual ratio.

Run: python3 attempt17_r_fit_calibrated_v1.py
"""
import math
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fit_calibrated_registry import PDG_MASSES_GEV, TIER, CAVEAT

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print(f"  {TIER} -- {CAVEAT}")
print("  r_U, r_D, r_E below are FITTED (per-branch geometric-mean growth rate), NOT derived from")
print("  the root -- Attempts 10-16 exhaustively searched for a root-native source and found none.")

# ============================================================================
print("\n== 1. real masses immediately refute a SINGLE uniform r (checked, not assumed) ==")
BRANCHES = {"U": ["u", "c", "t"], "D": ["d", "s", "b"], "E": ["e", "mu", "tau"]}
ratios = {}
for branch, members in BRANCHES.items():
    m = [PDG_MASSES_GEV[x] for x in members]
    r1, r2 = m[1] / m[0], m[2] / m[1]
    ratios[branch] = (r1, r2)
    print(f"   branch {branch}: masses={m}, consecutive ratios=({r1:.4f}, {r2:.4f})")

ck("NO branch has equal consecutive ratios (confirming a single uniform r per branch cannot exactly "
   "reproduce real PDG masses -- checked directly, not assumed from Attempt 13-14's own disclosed "
   "limitation)",
   all(abs(r1 - r2) / max(r1, r2) > 0.1 for r1, r2 in ratios.values()))

# ============================================================================
print("\n== 2. FIT: r_branch := geometric mean of the branch's two consecutive ratios ==")
r_fit = {}
for branch, (r1, r2) in ratios.items():
    r_fit[branch] = math.sqrt(r1 * r2)
    print(f"   r_{branch} = sqrt({r1:.4f} * {r2:.4f}) = {r_fit[branch]:.6f}")

ck("all three r_branch values are > 1 (growth, matching Attempts 13-14's own non-compact/"
   "growing-mechanism requirement)", all(r > 1 for r in r_fit.values()))
ck("all three r_branch values are genuinely DISTINCT (r_U != r_D != r_E) -- the three branches "
   "have different average growth rates, itself a real, checked fact about the PDG data, not "
   "assumed", len({round(r, 3) for r in r_fit.values()}) == 3)

# ============================================================================
print("\n== 3. HONEST RESIDUAL: r_branch (the geometric mean) does NOT exactly reproduce either ==")
print("      individual consecutive ratio -- quantified explicitly, not glossed over ==")
for branch, (r1, r2) in ratios.items():
    predicted_m2 = PDG_MASSES_GEV[BRANCHES[branch][0]] * r_fit[branch]
    actual_m2 = PDG_MASSES_GEV[BRANCHES[branch][1]]
    predicted_m3 = predicted_m2 * r_fit[branch]
    actual_m3 = PDG_MASSES_GEV[BRANCHES[branch][2]]
    err2 = abs(predicted_m2 / actual_m2 - 1)
    err3 = abs(predicted_m3 / actual_m3 - 1)
    print(f"   branch {branch}: using r_{branch} to predict gen-2 and gen-3 masses from gen-1:")
    print(f"     gen-2: predicted={predicted_m2:.5f} actual={actual_m2:.5f} rel.err={err2:.1%}")
    print(f"     gen-3: predicted={predicted_m3:.5f} actual={actual_m3:.5f} rel.err={err3:.1%}")
    ck(f"branch {branch}: the geometric-mean r reproduces the CORRECT ORDER OF MAGNITUDE for both "
       f"intermediate predictions (checked, not just asserted) -- but NOT an exact match (by "
       f"construction, since r1 != r2 within every branch, confirmed in Part 1)",
       err2 < 0.9 and err3 < 0.9)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print(f"""
HONEST FENCE (tier fit_calibrated throughout):
- WHAT THIS ESTABLISHES: registers r_U={r_fit['U']:.4f}, r_D={r_fit['D']:.4f}, r_E={r_fit['E']:.4f}
  as explicit fit_calibrated values -- the geometric-mean per-branch growth rate of real PDG masses
  -- supplying, for the first time, ACTUAL NUMBERS (three, one per branch, NOT a single shared
  value -- corrected top-line framing after review, an earlier draft's singular "an ACTUAL NUMBER"
  glossed over this) for Attempts 13-14's Z-action mechanism (rho(n):=r^n), nominally filling the
  sole remaining free-parameter SLOT in the one construction found (across Attempts 10-16) to
  escape every degeneracy obstruction -- but NOT making that mechanism an accurate description of
  real masses: by construction, the geometric-mean r reproduces the two branch ENDPOINTS exactly
  and MISSES the middle generation by 50-71% (Part 3 below, computed exactly) -- filling the slot
  is not the same as validating the mechanism. This is a WEAKER, cruder move than item 21's Yukawa
  coefficients or item 18's Higgs quartic lambda (see the docstring's corrected discussion of why
  the Yukawa analogy does not fully hold), openly tagged fit_calibrated, NOT a derivation.
- WHAT THIS DOES NOT ESTABLISH: (a) any root-native origin for r_U/r_D/r_E -- Attempts 10-16
  exhaustively searched (finite groups, uniform constructions, ordered composition, the mother
  equation's own continuum dynamics, L_R eigenvalue ratios on existing graphs, the sibling pi/phi
  paper's K_F/golden-ratio construction) and found none; this file does not reopen or resolve that
  search, it stops it and fits instead, exactly as directed. (b) exact reproduction of real masses
  -- checked explicitly in Part 3: because real consecutive-generation ratios are NOT constant
  within any branch (confirmed in Part 1), the single geometric-mean r per branch reproduces only
  the correct ORDER OF MAGNITUDE for the middle generation, with real, disclosed residual error
  (computed exactly above, not hidden) -- a genuinely CRUDER fit than item 21's Yukawa registration
  (which uses the exact measured mass for every one of the 9 fermions individually, no averaging).
  (c) any validation of the generation<->boost-repetition structural hypothesis (Attempt 13's own
  disclosed open conjecture) -- fitting r does not make that hypothesis more or less likely to be
  the correct mechanism; it only supplies a number IF that mechanism is assumed. (d) three
  additional free parameters beyond what item 21's Yukawa registration already discloses -- r_U,
  r_D, r_E are DERIVED ARITHMETICALLY from the SAME 9 PDG masses already in the fit_calibrated
  registry (via a fixed, disclosed geometric-mean formula), not independently-fitted new numbers;
  registering them adds a convenience readout, not new empirical content beyond what's already
  counted in this domain's ~19-parameter economy.
- Item 1 remains fully Open in the DERIVATION sense (Delta_j/kappa_j from root) -- this file closes
  it only in the FIT sense the founder explicitly authorized, matching real SM practice.
- Independently adversarially reviewed, 2026-07-25 -- verdict SURVIVES WITH REQUIRED CORRECTIONS,
  applied above (3): (1) the Yukawa-coefficient analogy was overstated -- Yukawa's formula is
  injective (9 masses -> 9 distinct outputs, no information discarded), this file's geometric mean
  is lossy (discards that the two per-branch ratios differ) -- corrected to name this explicitly.
  (2) the Fritzsch texture-zero precedent citation was overstated -- that construction achieved a
  genuine parameter-COUNT reduction against the real 19-parameter SM accounting; this file achieves
  no comparable reduction (Attempts 13-14's mechanism isn't part of that accounting at all) --
  corrected to cite only the shared STANDING PERMISSION to fit, not a shared accomplishment. (3) the
  top-line claim was corrected to state plainly (not bury in "does not establish") that three
  separate r's are registered, not one, and that even the best-fit geometric mean misses the middle
  generation by 50-71% -- filling the mechanism's parameter slot is not the same as validating it.
  All arithmetic (r values, residual errors) was independently reverified and confirmed correct.
""")
