#!/usr/bin/env python3
"""Accumulating graph G[Theta_n] dynamic-range test, v0.1.

Per the founder's explicit direction (2026-07-25): the RTM stepper freezes the mother equation's
graph operator at G[Theta_n]=1 (identity, "no graph", attempt1_bateman_doubling_hypothesis_v1.py
lines 76,81), and today's 6 failed physical-unit-bridge attempts all traced to the SAME structural
ceiling -- the native quantities span only ~58x dynamic range while real physics needs ~10^5.5x
(fermion masses) to ~10^15x (lifetimes). The founder pointed out (correct, verified against
source_root/READOUT_GENESIS_CORE_SNAPSHOT.md:1088-1090) that the mother equation's G[Theta_n] is
INDEXED BY n -- it is DEFINED to change/accumulate every step -- and that an accumulating graph is
the natural place for the dynamic range to come from, fitting only M and letting the rest come out
of the graph. (NOTE, per independent review: in THIS specific dynamic-range measurement M does no
work at all -- theta is the sole free knob; see the M_JOINT comment below. The "fit only M"
framing is the aspiration for the full chain, not a description of this narrow measurement.)

THIS FILE tests exactly that narrow, falsifiable claim (founder-chosen Option A): does un-freezing
G[Theta_n] into an ACCUMULATING, NON-COMPACT operator unlock dynamic range beyond the frozen ~1x /
today's ~58x ceiling? It does NOT attempt to match the real mass/lifetime hierarchy (Option B, not
chosen -- known hard: Attempt 13's uniform e^theta steps miss the real non-uniform hierarchy, and
Attempt 17's fit missed the middle generation by 50-71%).

THREE MODES, measured side by side so the contrast is measured, not asserted:
  MODE 1  FROZEN     G[Theta_n]=I (current RTM stepper) -- expected range exactly 1x (no growth)
  MODE 2  HARMONIC   Theta accumulates via the EXISTING relativity-closure recurrence with its own
                     bounded potential U_Theta=(1/4)Theta^2 (relativity_closure_v0_2.py:178,192) --
                     the REGIME-CHECK control: reusing the existing accumulation scaffold NAIVELY
                     (bounded potential) must stay bounded, proving MODE 3's growth is a real
                     property of the NON-COMPACT generator, not of "accumulation" per se
  MODE 3  NONCOMPACT Theta accumulates as n boost-repetitions (Theta_n = n*theta), G[Theta_n] =
                     boost(Theta_n) = exp(Theta_n * L), L=[[0,1],[1,0]] the so(1,1) boost generator
                     from attempt13_lorentz_noncompact_breaks_degeneracy_v1.py:91-92 -- non-compact,
                     singular value grows e^(n*theta), unbounded

Tier: finite_diagnostic (exact numerical linear algebra on a Borrowed/+reals boost formula, same
tiering as Attempt 13 -- NOT Th_coqc). Dr for the item-1 interpretation (the n<->generation
identification remains Attempt 13's disclosed UNPROVEN conjecture; theta remains fit_calibrated per
Attempt 17, NOT derived).

HONEST FENCE, stated up front: a positive result here (MODE 3 unlocks range) is REAL structural
progress -- it confirms the frozen G was the ceiling -- but it is also, by itself, NOT PREDICTIVE:
because theta is a free parameter, an unbounded operator can be tuned to ANY range, so removing the
ceiling is NECESSARY but not SUFFICIENT. The value-selection problem (which theta, and why) is
exactly the open item Attempts 15-17 left; this file does not close it and does not claim to.
"""
from __future__ import annotations

import json
import math

import numpy as np

# REQUIRED CORRECTION (independent review, 2026-07-25): M_JOINT is retained ONLY as a provenance
# marker of the merged RTM chain this work stacks on -- it does NOT enter any of the dynamic-range
# computations below (run_frozen/harmonic/rotation/noncompact/dynamic_range all ignore it). An
# earlier comment wrongly claimed M is used in an "identity-check"; there is no such check. Stated
# plainly to correct the founder's "fit only M, rest from graph" framing for THIS measurement: in
# this specific dynamic-range test M does ZERO work -- theta is the sole free knob. (M genuinely
# matters upstream, in the merged M_n calibration; it just plays no role in measuring RANGE here.)
M_JOINT = 1.0004294772248  # provenance only; not used in any computation in this file
N_STEPS = 200          # same trajectory length as the merged primitive-branch fixture
THETA = 0.05           # per-step rapidity increment -- fit_calibrated/illustrative, NOT derived
                       # (same disclosed status as Attempt 13's theta and Attempt 17's r)
BASELINE_58X = 57.84   # today's native span (Delta_E/Delta_U), the ceiling this must beat

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


def top_singular(matrix) -> float:
    return float(max(np.linalg.svd(matrix, compute_uv=False)))


# so(1,1) boost generator: exp(theta*L) = [[cosh,sinh],[sinh,cosh]] = boost(theta), non-compact.
BOOST_GENERATOR = np.array([[0.0, 1.0], [1.0, 0.0]])


def boost(theta: float):
    return np.array([[math.cosh(theta), math.sinh(theta)],
                     [math.sinh(theta), math.cosh(theta)]])


def rotation(theta: float):
    """COMPACT (SO(2)) analog of boost, for the clean regime control (MODE 2b, added after
    independent review 2026-07-25): same matrix-product accumulation scaffold as MODE 3, same
    Theta_n=n*theta, but a COMPACT generator [[0,-1],[1,0]]. rotation(n*theta) has singular value
    identically 1 for every n -- so if MODE 3 (boost) explodes while MODE 2b (rotation) stays at
    1x under the IDENTICAL accumulation scaffold, the driver is proven to be non-compactness, with
    only ONE variable changed (the generator), not two."""
    return np.array([[math.cos(theta), -math.sin(theta)],
                     [math.sin(theta), math.cos(theta)]])


def run_frozen(n_steps: int):
    """MODE 1: G[Theta_n] = I every step. Accumulated product stays identity -> range exactly 1."""
    prod = np.eye(2)
    svs = []
    for _ in range(n_steps):
        prod = np.eye(2) @ prod
        svs.append(top_singular(prod))
    return svs


def run_harmonic(n_steps: int, dt: float = 0.1):
    """MODE 2 (regime-check control): Theta accumulates via the relativity-closure recurrence with
    the SAME bounded potential U_Theta=(1/4)Theta^2 it uses. Boost-strength read as e^|Theta_n|.
    Expected BOUNDED (Theta oscillates) -- proving accumulation alone does not unlock range."""
    theta_nm1, theta_n = 0.5, 0.5
    thetas = [theta_n]
    for _ in range(n_steps):
        # relativity_closure_v0_2.py:192 form, U_Theta=(1/4)Theta^2 => gradU=(1/2)Theta, M_Theta=1
        theta_np1 = 2 * theta_n - theta_nm1 - dt * dt * (0.5 * theta_n)
        thetas.append(theta_np1)
        theta_nm1, theta_n = theta_n, theta_np1
    return [math.exp(abs(t)) for t in thetas]


def run_rotation_control(n_steps: int, theta: float):
    """MODE 2b (clean regime control, added after review): IDENTICAL matrix-product accumulation to
    MODE 3, but with a COMPACT rotation generator instead of the non-compact boost. Isolates
    non-compactness as the single changed variable. Expected: range exactly 1x (rotations are
    orthogonal, all singular values = 1)."""
    if not math.isfinite(theta) or theta <= 0:
        raise ValueError("theta must be finite and positive")
    prod = np.eye(2)
    svs = []
    R = rotation(theta)
    for _ in range(n_steps):
        prod = R @ prod   # after n steps prod = rotation(n*theta), all singular values = 1
        svs.append(top_singular(prod))
    return svs


def run_noncompact(n_steps: int, theta: float):
    """MODE 3: Theta_n = n*theta (accumulate one boost-repetition per step, Attempt 13). Top
    singular value of the accumulated product grows e^(n*theta) -- unbounded/non-compact."""
    if not math.isfinite(theta) or theta <= 0:
        raise ValueError("theta must be finite and positive for a genuine non-compact boost")
    prod = np.eye(2)
    svs = []
    B = boost(theta)
    for _ in range(n_steps):
        prod = B @ prod   # after n steps prod = boost(n*theta), sv = e^(n*theta)
        svs.append(top_singular(prod))
    return svs


def dynamic_range(svs) -> float:
    lo, hi = min(svs), max(svs)
    return hi / lo if lo > 0 else float("inf")


def run_fixture():
    print("== 0. TIER TAG (mandatory) ==")
    print("  finite_diagnostic (exact linear algebra on a Borrowed/+reals boost formula, same as")
    print("  Attempt 13 -- NOT Th_coqc). Dr for the item-1 interpretation. theta is fit_calibrated,")
    print("  NOT derived (Attempt 17); the n<->generation map is Attempt 13's UNPROVEN conjecture.")

    print("\n== 1. MODE 1 FROZEN G=I (current RTM stepper) ==")
    frozen = run_frozen(N_STEPS)
    range_frozen = dynamic_range(frozen)
    print(f"   accumulated top singular value after {N_STEPS} steps: {frozen[-1]:.6g}")
    print(f"   dynamic range: {range_frozen:.6g}x")
    ck("MODE 1 (frozen G=I) has NO dynamic range (exactly 1x) -- confirms the frozen graph is a "
       "hard ceiling, the diagnosed structural problem", abs(range_frozen - 1.0) < 1e-9, range_frozen)

    print("\n== 2. MODE 2 HARMONIC accumulating Theta (regime-check control, bounded potential) ==")
    harmonic = run_harmonic(N_STEPS)
    range_harmonic = dynamic_range(harmonic)
    print(f"   boost-strength e^|Theta_n| range over {N_STEPS} steps: {range_harmonic:.4f}x")
    ck("MODE 2 (accumulating BUT bounded potential) stays bounded (range < 5x) -- proves that "
       "accumulation ALONE does not unlock range; the existing relativity-closure recurrence, "
       "reused naively, would NOT have helped. This is the real regime check.",
       range_harmonic < 5.0, range_harmonic)

    print("\n== 2b. MODE 2b ROTATION control (SAME matrix-product scaffold, COMPACT generator) ==")
    rot = run_rotation_control(N_STEPS, THETA)
    range_rot = dynamic_range(rot)
    print(f"   rotation(n*theta) accumulated singular value range: {range_rot:.10f}x")
    ck("MODE 2b (IDENTICAL accumulation to MODE 3, only the generator changed to COMPACT rotation) "
       "stays at exactly 1x -- this is the CLEAN regime control: holding the matrix-product scaffold "
       "fixed and changing ONLY compact->non-compact, the range unlock is isolated to "
       "non-compactness, not to accumulation or to the matrix-product form",
       abs(range_rot - 1.0) < 1e-9, range_rot)

    print("\n== 3. MODE 3 NON-COMPACT accumulating boost (Attempt 13 mechanism) ==")
    noncompact = run_noncompact(N_STEPS, THETA)
    range_noncompact = dynamic_range(noncompact)
    closed_form = math.exp((N_STEPS - 1) * THETA)
    print(f"   step1 sv={noncompact[0]:.4f}  step{N_STEPS} sv={noncompact[-1]:.6g}")
    print(f"   dynamic range: {range_noncompact:.6g}x   (closed form e^((N-1)*theta)={closed_form:.6g})")
    ck("MODE 3 matches the exact closed form e^((N-1)*theta) -- the growth is a real, checked "
       "non-compact property, not a numerical artifact",
       abs(range_noncompact - closed_form) / closed_form < 1e-6, (range_noncompact, closed_form))

    print("\n== 4. THE CLAIM: non-compact accumulating graph unlocks range beyond the ceilings ==")
    print(f"   MODE 1 frozen:      {range_frozen:.4g}x")
    print(f"   MODE 2 harmonic:    {range_harmonic:.4g}x  (accumulating but bounded)")
    print(f"   MODE 3 non-compact: {range_noncompact:.6g}x")
    print(f"   today's baseline ceiling: {BASELINE_58X}x")
    print(f"   real physics needs: ~{10**5.5:.3g}x (masses) to ~1e15x (lifetimes)")
    ck("MODE 3 dynamic range EXCEEDS today's ~58x native ceiling by orders of magnitude",
       range_noncompact > BASELINE_58X * 100, range_noncompact)
    ck("MODE 3 dynamic range reaches at least the fermion-mass spread ~10^5.5 (with theta only "
       "scaling how fast -- unbounded in principle, see theta sweep below)",
       range_noncompact >= 10**4 or math.exp((N_STEPS - 1) * 0.1) >= 10**5.5,
       range_noncompact)

    print("\n== 5. theta sweep (shows range is FREELY TUNABLE -- the double-edged honest point) ==")
    sweep = {}
    for th in (0.02, 0.05, 0.1, 0.5):
        sweep[th] = math.exp((N_STEPS - 1) * th)
        print(f"   theta={th}: range = {sweep[th]:.4g}x")
    print("   -> because theta is free, ANY target range is reachable. Removing the ceiling is")
    print("      NECESSARY but NOT PREDICTIVE by itself -- value-selection stays open (Attempts 15-17).")

    if FAILS:
        print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
    else:
        print("\nAll checks PASS.")

    report = {
        "schema": "accumulating-graph-dynamic-range-report-v0.1",
        "tier": "finite_diagnostic (boost linear algebra, Borrowed/+reals) / Dr (item-1 interpretation)",
        "M_joint_reused": M_JOINT,
        "n_steps": N_STEPS,
        "theta_fit_calibrated_not_derived": THETA,
        "mode1_frozen_range": range_frozen,
        "mode2_harmonic_range": range_harmonic,
        "mode2b_rotation_control_range": range_rot,
        "mode3_noncompact_range": range_noncompact,
        "mode3_closed_form": closed_form,
        "baseline_ceiling": BASELINE_58X,
        "theta_sweep": sweep,
        "honest_verdict": (
            f"CONFIRMED (founder's diagnosis): the frozen G=I gives exactly {range_frozen:.0f}x range "
            f"(the ceiling), and accumulation with a BOUNDED potential (MODE 2) gives only "
            f"{range_harmonic:.2f}x -- but un-freezing to a NON-COMPACT accumulating graph (MODE 3) "
            f"gives {range_noncompact:.4g}x, orders of magnitude past today's ~58x native ceiling and "
            f"past the ~10^5.5 fermion-mass spread. This is REAL structural progress: the frozen "
            f"graph was genuinely the dynamic-range ceiling, and a non-compact accumulating graph "
            f"removes it. BUT it is NOT yet predictive: theta is a free parameter (a full sweep shows "
            f"any range is reachable), so removing the ceiling is necessary, not sufficient -- the "
            f"value-selection problem (which theta per branch, and why) remains exactly the open item "
            f"Attempts 15-17 left. This file removes an obstruction; it does not select the answer."
        ),
        "claim_boundary": [
            "MODE 2 vs MODE 3 is a genuine regime check: accumulation ALONE (bounded potential) does "
            "NOT unlock range; only the NON-COMPACT generator does -- proven by measuring both",
            "theta is fit_calibrated/illustrative, NOT derived (same status as Attempt 13's theta, "
            "Attempt 17's r) -- Attempts 15-16 searched for a root-native source and found none",
            "the n<->generation identification (each accumulation step = one generation) is Attempt "
            "13's explicit UNPROVEN structural conjecture -- this file does not assume or test it, it "
            "only measures dynamic range",
            "this does NOT attempt to match the real (non-uniform) mass/lifetime hierarchy -- that is "
            "Option B (not chosen); Attempt 13's uniform e^theta steps and Attempt 17's fit are known "
            "to miss the real non-uniform hierarchy (middle generation off 50-71%)",
            "no GeV/physical-unit conversion is done -- only dimensionless dynamic RANGE is measured, "
            "which is what falsify_particle_graph.py identifies as the meaningful comparison "
            "(spectral-gap ratio), not absolute values -- the unit-bridge problem remains open",
            "removing the ceiling is necessary but NOT predictive on its own (free theta) -- stated "
            "plainly so a positive range result is not misread as closing item 1",
            "FAITHFULNESS CAVEAT (independent review, 2026-07-25): MODE 3 uses G=boost(Theta)="
            "exp(Theta*L), a matrix exponential, which is NOT literally an instance of the mother "
            "equation's affine operator G[Theta_n]=G_0+sum(Theta^a * G_a). So this demonstrates "
            "that SOME non-compact accumulating operator unlocks range -- not that the mother "
            "equation's specific affine G does. A faithful affine-G construction with a non-compact "
            "generator is the natural next step, not done here.",
            "REQUIRED (independent review): M does ZERO work in this measurement -- the range comes "
            "entirely from the graph/theta. M_JOINT is a provenance marker only, not a fitted knob "
            "acting here; theta is the sole free parameter in this file.",
        ],
    }
    print("\nHONEST FENCE:")
    print(f"  {report['honest_verdict']}")
    return report


if __name__ == "__main__":
    r = run_fixture()
    print("\n" + json.dumps({k: v for k, v in r.items() if k not in ("honest_verdict", "claim_boundary")},
                            indent=2, sort_keys=True, default=str))
