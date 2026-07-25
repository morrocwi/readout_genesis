#!/usr/bin/env python3
"""
dimensionless_native_ratio_bridge_v1.py -- EXPLORATORY, single-attempt candidate.
(not part of any build; not wired into any aggregate; no repo engine imports
required beyond loading two sibling files as data sources -- see Section 3.)

MECHANISM UNDER TEST
--------------------
Three already-failed attempts today (rd_to_gev_fit_calibrated_bridge,
mass_ratio_test_no_fit, native_causal_memory_consistency) all tried to cross
from this repo's native discrete units into GeV via a fitted dimensionful
scale Lambda (v_EW=246 GeV). All three failed or were internally
inconsistent, because Lambda carries a real unit-conversion "infinity-carrying
bridge" in the sense of docs/root/ZERO_INFINITY_DUAL_DIAGNOSIS.md -- exactly
the kind of object that diagnosis document warns cannot be trusted to cross
cleanly.

This candidate tries a DIFFERENT route: skip unit conversion entirely by
comparing DIMENSIONLESS numbers on both sides.

  - lambda_gap = 3        : the K3 graph-Laplacian spectral gap, proven
                              Th_coqc in formal/InfoCompleteGraphSpectralGap_
                              attempt.v (energy == n*variance, n=3 for the
                              triangle), and literally the L_R spectral datum
                              exhibited in formal/InfoDiscreteDivergence_
                              attempt.v. Pure number, no units.
  - h1/l2   = 4           : the discrete Sobolev grading constant on the same
                              minimal triangle cell. REQUIRED CORRECTION
                              (independent review, 2026-07-25): formal/
                              InfoDiscreteSobolev_attempt.v proves only the
                              INEQUALITY l2<=h1 (h1_dominates_l2) as Th_coqc --
                              it does NOT prove the exact equality h1=4*l2.
                              The exact factor-of-4 identity is a genuinely
                              new algebraic fact, sympy-verified for all a,b,c
                              IN THIS FILE, but not yet a Coq theorem. Tier
                              here is therefore Dr (sympy-verified exact
                              identity, not Coq-checked), NOT Th_coqc -- the
                              weaker inequality l2<=h1 is the only Th_coqc
                              part. Pure number, no units, tier corrected.
  - ratio_A = lambda_gap / damping_rate, where damping_rate = D/(2*M_joint)
                              is this repo's own ALREADY-CALIBRATED native
                              damping rate for the toy Bateman-doubling
                              stepper (matter_antimatter_exploration/
                              attempt1_bateman_doubling_hypothesis_v1.py +
                              item1_exploration/retained_transition_
                              operational_closure/). Also dimensionless on
                              the native side (both lambda_gap and
                              damping_rate are pure numbers in native units).

These are compared, with ZERO new free parameters and ZERO unit-conversion
factor, against a PRE-REGISTERED (written before any comparison is run) list
of real dimensionless physics numbers: PDG mass ratios / coupling ratios, and
3D Ising critical exponents. If nothing matches within 2%, that is a valid,
loud, reportable NEGATIVE result -- exactly like this repo's existing
falsify_particle_graph.py convention. No cherry-picking: every native number
is tested against every target, and the FULL table is printed, not just the
best match.

TIER: every number below carries an explicit tag.
  - lambda_gap = 3          : Th_coqc (formal/InfoCompleteGraphSpectralGap_attempt.v)
  - h1/l2 = 4                : Dr (sympy-verified exact identity, NOT Coq-checked --
                                REQUIRED CORRECTION, independent review 2026-07-25: only
                                the inequality l2<=h1 is Th_coqc in
                                formal/InfoDiscreteSobolev_attempt.v, the exact
                                factor-of-4 equality is not a Coq theorem anywhere in
                                formal/, see module docstring MECHANISM section)
  - D, M_joint, damping_rate : finite_diagnostic (already-merged calibrated
                                readout of the toy stepper; re-read/recomputed
                                here, not re-derived from first principles)
  - the cross-table matches  : Dr (numerological comparison, honestly labeled
                                coincidence-suspect given the small
                                pre-registered set -- NOT a physics derivation
                                even if a sub-2% match appears)
  - GeV-scale absolute mass  : remains [Open] regardless of this file's
                                outcome (engine.lexicon.stance_for('mass'))

HARD CONSTRAINT HONORED: the comparison targets in Section 4 are hardcoded
BEFORE Section 5 computes anything, and Section 5 tests the FULL cross
product, not a search for the best-looking pair.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import numpy as np
import sympy as sp

FAILS: list[str] = []


def ck(name: str, cond: bool, got=None) -> bool:
    status = "PASS" if cond else "FAIL"
    suffix = f"  (got={got})" if got is not None else ""
    print(f"  [{status}] {name}{suffix}")
    if not cond:
        FAILS.append(name)
    return cond


# =============================================================================
print("== 1. lambda_gap -- K3 unweighted graph Laplacian spectral gap, recomputed from scratch ==")
# =============================================================================
L = np.array([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]], dtype=float)
eigvals = np.linalg.eigvalsh(L)
print(f"  L(K3) = {L.tolist()}")
print(f"  eigenvalues (numpy.linalg.eigvalsh) = {eigvals}")

n_zero = sum(1 for e in eigvals if abs(e) < 1e-9)
nonzero = sorted(e for e in eigvals if abs(e) >= 1e-9)
ck("exactly one (near-)zero eigenvalue (constant mode)", n_zero == 1, got=n_zero)
ck("the two nonzero eigenvalues are {3,3}", all(abs(e - 3.0) < 1e-9 for e in nonzero), got=nonzero)

lambda_gap = 3.0
print(f"  lambda_gap = {lambda_gap}")
print("  cross-check: matches formal/InfoCompleteGraphSpectralGap_attempt.v")
print("  (complete_graph_spectral_gap: complete_energy(K_n,x) == n*variance_sum(x), n=3), Th_coqc.")


# =============================================================================
print()
print("== 2. h1/l2 -- discrete Sobolev grading constant, recomputed symbolically with sympy ==")
# =============================================================================
a, b, c = sp.symbols("a b c", real=True)
l2 = a**2 + b**2 + c**2

# IMPORTANT DISCLOSED DISCREPANCY: the workflow brief that spawned this file
# stated curl = a-b+c. That is NOT what the repo actually defines. The real
# definition, read directly from formal/InfoDiscreteCurl_attempt.v line 48
# ("Definition curl (a b c : Q) : Q := a + b + c."), is the plain circulation
# sum a+b+c. Reported here rather than silently "corrected" in either
# direction, per the workflow's own instruction not to resolve discrepancies
# quietly. The computation below uses the REAL repo definition (a+b+c), and
# InfoDiscreteDivergence_attempt.v's div1/div2/div3 (which take the 1-form
# edge values a,b,c directly, not vertex potentials x_i -- the "2x_i-x_j-x_k"
# pattern in the brief is the *Laplacian* -div.grad on vertex potentials,
# a related but distinct object from div1/2/3 on edge 1-forms).
curl = a + b + c  # formal/InfoDiscreteCurl_attempt.v:48 (repo ground truth)
div1 = a - c      # formal/InfoDiscreteDivergence_attempt.v:36
div2 = b - a      # formal/InfoDiscreteDivergence_attempt.v:37
div3 = c - b      # formal/InfoDiscreteDivergence_attempt.v:38

h1 = l2 + curl**2 + div1**2 + div2**2 + div3**2

print(f"  l2(a,b,c)   = {l2}")
print(f"  curl(a,b,c) = {curl}   (repo definition, InfoDiscreteCurl_attempt.v:48)")
print(f"  div1,2,3    = {div1}, {div2}, {div3}   (InfoDiscreteDivergence_attempt.v:36-38)")
h1_expanded = sp.expand(h1)
print(f"  h1(a,b,c) expanded = {h1_expanded}")

diff = sp.simplify(h1 - 4 * l2)
print(f"  sympy.simplify(h1 - 4*l2) = {diff}  (symbolic, all a,b,c -- not hardcoded)")
ck("h1 - 4*l2 == 0 symbolically for all a,b,c", diff == 0, got=diff)

sobolev_ratio = sp.Rational(4, 1)
print(f"  h1/l2 = {sobolev_ratio}  (derived symbolically above, matches "
      "formal/InfoDiscreteSobolev_attempt.v's h1_dominates_l2 grading)")


# =============================================================================
print()
print("== 3. native damping rate D/(2*M_joint) -- read from the repo's own already-merged files ==")
# =============================================================================
HERE = Path(__file__).resolve()
STANDARD_MODEL_DIR = HERE.parents[2]          # .../domains/standard_model
ITEM1_DIR = HERE.parents[1]                   # .../item1_exploration
RTM_DIR = ITEM1_DIR / "retained_transition_operational_closure"
BATEMAN_PATH = STANDARD_MODEL_DIR / "matter_antimatter_exploration" / "attempt1_bateman_doubling_hypothesis_v1.py"

ck("bateman stepper file exists", BATEMAN_PATH.exists(), got=str(BATEMAN_PATH))
ck("retained_transition_operational_closure dir exists", RTM_DIR.exists(), got=str(RTM_DIR))


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


# 3a. read D directly out of the bateman stepper file's own module constants
#     (no repo-package import needed -- load by file path, exactly like the
#     already-merged retained_transition_operational_closure/*.py files do).
import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
    bateman = _load_module(BATEMAN_PATH, "bateman_stepper_for_ratio_bridge")

D_read = float(bateman.D)
M_bateman = float(bateman.M)
print(f"  read from attempt1_bateman_doubling_hypothesis_v1.py: D = {D_read}, M (fixture) = {M_bateman}")
D_EXPECTED = 0.3
if abs(D_read - D_EXPECTED) > 1e-12:
    print(f"  ** DISCREPANCY: brief expected D={D_EXPECTED}, file actually contains D={D_read} -- using the file's value. **")
else:
    print(f"  D matches the brief's expected value D={D_EXPECTED} -- no discrepancy.")

# 3b. re-run the repo's own already-merged M_joint calibration pipeline
#     (retained_transition_operational_closure/operational_exchange_closure_v0_1.py)
#     rather than paste its previously-printed number, so this file does not
#     silently drift from whatever that pipeline actually computes today.
sys.path.insert(0, str(RTM_DIR))
try:
    with contextlib.redirect_stdout(io.StringIO()):
        closure_mod = _load_module(RTM_DIR / "operational_exchange_closure_v0_1.py", "operational_exchange_closure_for_ratio_bridge")
        report = closure_mod.run_fixture()
finally:
    sys.path.remove(str(RTM_DIR))

M_joint = float(report["selected_joint"]["M_joint"])
joint_status = report["selected_joint"]["status"]
print(f"  re-ran retained_transition_operational_closure/operational_exchange_closure_v0_1.py:run_fixture()")
print(f"  -> selected_joint.status = {joint_status}, M_joint = {M_joint}")

M_JOINT_EXPECTED = 1.0004294772248
if abs(M_joint - M_JOINT_EXPECTED) > 1e-8:
    print(f"  ** DISCREPANCY: brief expected M_joint={M_JOINT_EXPECTED}, pipeline actually returned M_joint={M_joint} -- using the pipeline's value. **")
else:
    print(f"  M_joint matches the brief's expected value M_joint={M_JOINT_EXPECTED} (to 1e-8) -- no discrepancy.")

ck("M_joint calibration status is CALIBRATED_READY", joint_status == "CALIBRATED_READY", got=joint_status)

damping_rate = D_read / (2.0 * M_joint)
print(f"  damping_rate = D/(2*M_joint) = {D_read}/(2*{M_joint}) = {damping_rate}")

ratio_A = lambda_gap / damping_rate
print(f"  ratio_A = lambda_gap / damping_rate = {lambda_gap}/{damping_rate} = {ratio_A}")


# =============================================================================
print()
print("== 4. PRE-REGISTERED comparison targets (written BEFORE any comparison below is computed) ==")
# =============================================================================
# Dated 2026-07-25, hardcoded before Section 5 runs. PDG = Particle Data Group
# 2024 review values (rounded to the precision commonly quoted); critical
# exponents = standard 3D Ising universality-class values (Pelissetto &
# Vicari 2002 conformal-bootstrap-era consensus figures, as commonly cited).
PRE_REGISTERED_TARGETS = {
    "m_p/m_e (PDG)": 1836.15267,
    "m_mu/m_e (PDG)": 206.7683,
    "m_tau/m_e (PDG)": 3477.15,
    "M_W/M_Z (PDG)": 0.88148,
    "v_EW/m_H (PDG, 246/125.20 GeV)": 1.9644,
    "alpha_EM_inverse (PDG, low-E)": 137.035999,
    "sin2_theta_W (PDG, on-shell)": 0.23122,
    "Ising_3D nu (crit. exponent)": 0.6301,
    "Ising_3D beta (crit. exponent)": 0.3265,
    "Ising_3D gamma (crit. exponent)": 1.2372,
    "Ising_3D eta (crit. exponent)": 0.0364,
}
for k, v in PRE_REGISTERED_TARGETS.items():
    print(f"  {k:32s} = {v}")


# =============================================================================
print()
print("== 5. FULL cross table: every native dimensionless number x every pre-registered target ==")
# =============================================================================
NATIVE_NUMBERS = {
    "lambda_gap (=3)": lambda_gap,
    "h1/l2 (=4)": float(sobolev_ratio),
    "3/4": 0.75,
    "4/3": 4.0 / 3.0,
    "ratio_A (=lambda_gap/damping_rate)": ratio_A,
    "1/ratio_A": 1.0 / ratio_A,
}

rows = []
for nname, nval in NATIVE_NUMBERS.items():
    for tname, tval in PRE_REGISTERED_TARGETS.items():
        dev = abs(nval - tval) / abs(tval)
        rows.append((dev, nname, nval, tname, tval))

rows.sort(key=lambda r: r[0])

print(f"  {len(rows)} pairs tested ({len(NATIVE_NUMBERS)} native numbers x {len(PRE_REGISTERED_TARGETS)} targets), sorted by relative deviation:")
print(f"  {'rel.dev':>10s}  {'native (value)':40s}  {'target (value)':40s}")
for dev, nname, nval, tname, tval in rows:
    flag = ""
    if dev < 0.02:
        flag = "  <-- candidate match -- treat as coincidence-suspect given small pre-registered comparison set (~{}) pairs tested), no statistical significance claimed".format(len(rows))
    print(f"  {dev*100:9.4f}%  {nname:20s}({nval:.6f})  {tname:28s}({tval:.6f}){flag}")


# =============================================================================
print()
print("== 6. VERDICT ==")
# =============================================================================
sub_2pct = [r for r in rows if r[0] < 0.02]
if sub_2pct:
    print(f"  RESULT: {len(sub_2pct)} pair(s) out of {len(rows)} fall under the 2% deviation line.")
    for dev, nname, nval, tname, tval in sub_2pct:
        print(f"    - {nname} ({nval:.6f}) vs {tname} ({tval:.6f}): {dev*100:.4f}% deviation -- "
              "candidate match, coincidence-suspect, no statistical significance claimed "
              f"(small pre-registered set, {len(rows)} pairs tested).")
    print("  VERDICT: at least one sub-2% match exists -- flagged above as coincidence-suspect,")
    print("           NOT claimed as a physics derivation or GeV-scale bridge.")
else:
    best = rows[0]
    print(f"  RESULT: no pair falls under the 2% deviation line ({len(rows)} pairs tested).")
    print(f"  Best (still non-matching) pair: {best[1]} ({best[2]:.6f}) vs {best[3]} ({best[4]:.6f}) "
          f"-> {best[0]*100:.4f}% deviation.")
    print("  VERDICT: this dimensionless-native-ratio-bridge mechanism, as tested here, produces")
    print("           NO candidate match against the pre-registered target list. Negative result.")


# =============================================================================
print()
print("== HONEST FENCE ==")
# =============================================================================
print("""
  IS established here (Th_coqc, re-verified in this file):
    - lambda_gap = 3 is the exact K3 graph-Laplacian spectral gap (numpy
      eigenvalue computation, matches the existing Coq proof).

  IS established here (Dr -- sympy-verified, NOT Coq-checked; REQUIRED
  CORRECTION applied 2026-07-25, was mislabeled Th_coqc in an earlier draft):
    - h1/l2 = 4 is an exact symbolic identity on the triangle 1-form Sobolev
      norm (sympy.simplify confirms h1 - 4*l2 == 0 for ALL a,b,c, not just a
      spot-check), using the repo's REAL curl/div definitions (curl=a+b+c,
      not the a-b+c stated in this file's originating brief -- discrepancy
      disclosed in Section 2, not silently resolved). formal/
      InfoDiscreteSobolev_attempt.v proves only l2<=h1 (Th_coqc); the exact
      factor-of-4 equality has never been formalized in Coq -- this file's
      sympy proof is real and correct but is a DIFFERENT, weaker tier.

  IS established here (finite_diagnostic, re-run not re-derived):
    - damping_rate = D/(2*M_joint) using D and M_joint re-read/re-run from
      this repo's own already-merged calibration files today.

  IS NOT established by this file, regardless of the verdict above:
    - No claim that lambda_gap, h1/l2, or ratio_A stand for any specific
      physical quantity. A sub-2% numeric coincidence (if any) is reported
      as coincidence-suspect, not as a derivation, given the small
      pre-registered comparison set and the absence of any independent
      statistical significance test.
    - No unit-conversion factor was invented or fitted; that is the entire
      point of testing dimensionless numbers, but it also means this file
      cannot and does not produce a GeV-scale (or any absolute physical
      unit) prediction, matching or contradicting the 3 already-failed
      GeV-anchor attempts from today's chain, which this file deliberately
      does not repeat.
    - engine.lexicon.stance_for('mass') is unaffected: absolute mass scale
      remains [Open] whether or not a sub-2% match is found above.
    - The docs/root/ZERO_INFINITY_DUAL_DIAGNOSIS.md tension (readout-vs-
      readout only vs. this project's routine use of PDG GeV inputs
      elsewhere, e.g. item22_exploration/cabibbo_angle_gst_v1.py) is NOT
      resolved by this file either way. This file's targets ARE PDG
      dimensionless RATIOS (not raw GeV numbers), which sidesteps the
      dimensional half of that tension but does not adjudicate it.
""")

if FAILS:
    print(f"FAILS ({len(FAILS)}): {FAILS}")
    sys.exit(1)
else:
    print("All internal PASS/FAIL gates (Sections 1-3) passed. See Section 6 for the physics verdict.")
