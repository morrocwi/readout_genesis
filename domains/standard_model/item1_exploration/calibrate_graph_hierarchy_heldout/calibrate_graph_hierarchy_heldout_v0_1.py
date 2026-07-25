"""Calibrate the graph accumulation to real mass ratios, with a HELD-OUT test. v0.1.

EQ-069/070/071 established that the graph's mass-ratio hierarchy is a readout of the graph's own
constants, and that pinning those constants is a legitimately-calibratable internal question
(fit_calibrated, DEV-SM-001). This file DOES that calibration and adds the held-out test Attempt 17
never ran: calibrate the accumulation constant to ONE real consecutive-generation mass ratio, then
PREDICT a DIFFERENT ratio the calibration never saw, and report the computed held-out error.

The condition number (mass-ratio analog) of the accumulated graph grows as exp(rate * accumulation);
if generation g sits at accumulation milestone n_g, the ratio between consecutive generations is
exp(rate * dn). This file reads the real PDG masses (fit_calibrated_registry.py), forms each
branch's two consecutive-generation ratios R1=(gen2/gen1), R2=(gen3/gen2), calibrates the graph
accumulation to R1, and predicts R2 held-out.

*** COMPUTED FACTS (reported per the materialist-bias guard, ZERO_INFINITY_DUAL_DIAGNOSIS.md Part 4b
    -- no works/fails value-words; a fit_calibrated constant is not a defect):

    FACT A: the real consecutive-generation ratios are NON-UNIFORM within every branch --
    up (588.0, 135.8), down (20.0, 44.8), lepton (206.8, 16.8). The per-branch shape differs: the
    up-type and lepton branches DECELERATE across generations (R2 < R1), the down-type ACCELERATES
    (R2 > R1). This is a measured property of the real masses, not of any model.

    FACT B: a single accumulation constant calibrated to R1 reproduces R1 exactly (1 constant -> 1
    number, trivially) but its HELD-OUT prediction of R2 is off by 55%-1130% across branches,
    because the uniform-step accumulation gives R2=R1 while reality is non-uniform.

    FACT C (the structural finding, corrected after review to ONLY what is computed here): a
    UNIFORM-step accumulation gives consecutive-generation ratio R2/R1 = 1 exactly (computed here,
    FACT B: the calibrated constant makes R2 = R1). But the up-type and lepton branches DECELERATE
    (R2/R1 < 1, computed here from PDG masses). So a uniform (constant-rate) accumulation CANNOT
    produce a decelerating branch -- reproducing up/lepton would require the accumulation RATE to
    DECREASE across generations. Separately, the accumulation mechanisms already on record trend the
    OTHER way, toward acceleration: EQ-070 (affine_graph_noncompact_growth) measured the per-step
    growth as "mildly accelerating"; EQ-071 (field_sourced_accumulation) has a condition number that
    compounds strongly with accumulation. So no accumulation profile tested so far can produce
    R2/R1 < 1 -- a computed structural fact identifying WHAT a graph accumulation would need (a
    per-branch profile whose rate can DECREASE across generations) to reproduce the held-out ratios
    of the decelerating branches. (No specific ">>1" per-generation magnitude is asserted; that was
    an unbacked, mis-cited overstatement in an earlier draft, corrected here.)

    FRAMEWORK-NATIVE reading (stance_for('mass'): mass ratios = spectral-gap ratios of L_R): these
    ratios ARE graph readouts; calibrating the graph constant to them is legitimate. What the
    held-out test shows is a COMPUTED structural property -- the number of constants needed equals
    the number of independent ratios under a uniform/accelerating profile (no compression), and the
    profile shape must be enrichable to decelerate -- an OPEN internal question about the graph's
    accumulation profile, NOT a failure. This file neither claims the hierarchy is reproduced nor
    claims it is underivable; it reports the calibration, the held-out numbers, and the shape
    mismatch. ***

Tier: fit_calibrated (the accumulation constant fit to R1; the PDG masses, reused). finite_diagnostic
(the held-out ratios and the shape comparison). NOT Th_coqc.
"""
from __future__ import annotations

import json
import math

from domains.standard_model.fit_calibrated_registry import PDG_MASSES_GEV

# real consecutive-generation triples (gen1, gen2, gen3) per branch, from PDG_MASSES_GEV
BRANCHES = {
    "up": ("u", "c", "t"),
    "down": ("d", "s", "b"),
    "lepton": ("e", "mu", "tau"),
}

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


def real_ratios(branch):
    g1, g2, g3 = (PDG_MASSES_GEV[k] for k in BRANCHES[branch])
    return g2 / g1, g3 / g2      # (R1, R2)


def calibrate_and_predict(branch):
    """Calibrate the (uniform) accumulation to R1; predict R2 held-out. Under a uniform-step
    accumulation the calibrated constant makes the predicted per-gen ratio a single value = R1,
    so the held-out prediction of R2 is R1 (the honest content: one constant, one reproduced
    ratio, no held-out compression)."""
    r1, r2 = real_ratios(branch)
    if r1 <= 0 or r2 <= 0:
        raise ValueError(f"branch {branch} has a non-positive mass ratio")
    # calibrate: rate = ln(R1)/dn ; with equal generation spacing dn, the same rate predicts R2=R1
    predicted_r2 = r1
    held_out_error = abs(predicted_r2 - r2) / r2
    return {
        "R1_fit": r1,
        "R2_real": r2,
        "R2_predicted_heldout": predicted_r2,
        "held_out_relative_error": held_out_error,
        "shape_real": "decelerating" if r2 < r1 else "accelerating",
    }


def run_fixture():
    print("== 0. TIER TAG (mandatory) ==")
    print("  fit_calibrated (accumulation constant fit to R1; PDG masses reused) / finite_diagnostic")
    print("  (held-out ratios, shape comparison). NOT Th_coqc. Reported as computed facts + tier per")
    print("  the materialist-bias guard -- a fit_calibrated constant is not a defect.")

    print("\n== 1. FACT A: real consecutive-generation ratios are non-uniform (measured, not a model) ==")
    shapes = {}
    for br in BRANCHES:
        r1, r2 = real_ratios(br)
        shapes[br] = "decelerating" if r2 < r1 else "accelerating"
        print(f"   {br:7s}: R1={r1:8.1f}  R2={r2:8.1f}  R2/R1={r2/r1:.3f}  ({shapes[br]})")
    ck("real ratios are non-uniform in every branch (R2 != R1) -- a measured property of the masses",
       all(abs(real_ratios(br)[1] - real_ratios(br)[0]) > 1e-6 for br in BRANCHES))
    ck("branches have DIFFERENT shapes -- up/lepton decelerate (R2<R1), down accelerates (R2>R1) -- "
       "so no single monotone profile fits all three",
       shapes["up"] == "decelerating" and shapes["down"] == "accelerating", shapes)

    print("\n== 2. FACT B: calibrate accumulation to R1, predict R2 HELD-OUT (Attempt 17 lacked this) ==")
    results = {}
    for br in BRANCHES:
        res = calibrate_and_predict(br)
        results[br] = res
        print(f"   {br:7s}: fit R1={res['R1_fit']:.1f} -> predict R2={res['R2_predicted_heldout']:.1f}, "
              f"real R2={res['R2_real']:.1f}, held-out error={res['held_out_relative_error']*100:.1f}%")
    ck("the held-out prediction of R2 (from a single constant calibrated to R1) is off by >50% in "
       "every branch -- a computed fact: one constant reproduces one ratio, with no held-out "
       "compression under a uniform-step accumulation",
       all(r["held_out_relative_error"] > 0.5 for r in results.values()),
       {br: round(r["held_out_relative_error"], 3) for br, r in results.items()})

    print("\n== 3. FACT C (structural): a uniform accumulation gives R2/R1=1; up/lepton need R2/R1<1 ==")
    print("   uniform-step accumulation -> R2/R1 = 1 (computed here, = FACT B's R2=R1);")
    print("   the up-type and lepton branches have R2/R1 < 1 (decelerating) -- so a constant-rate")
    print("   accumulation cannot produce them; reproducing them needs a rate that DECREASES per gen:")
    for br in ("up", "lepton"):
        r1, r2 = real_ratios(br)
        print(f"     {br}: real R2/R1={r2/r1:.3f} (< 1, decelerating) vs uniform accumulation R2/R1 = 1")
    print("   (EQ-070's affine growth is 'mildly accelerating', EQ-071's field-sourced compounds --")
    print("    both trend toward acceleration, neither toward deceleration; no ''>>1'' magnitude asserted)")
    ck("a uniform accumulation gives R2/R1=1 while up/lepton have R2/R1<1 -- a computed structural "
       "fact: a constant-rate accumulation cannot decelerate; reproducing those branches needs a "
       "per-branch rate that DECREASES across generations",
       real_ratios("up")[1] < real_ratios("up")[0] and real_ratios("lepton")[1] < real_ratios("lepton")[0])

    if FAILS:
        print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
    else:
        print("\nAll checks PASS.")

    report = {
        "schema": "calibrate-graph-hierarchy-heldout-report-v0.1",
        "status": "COMPUTED_calibration_plus_heldout_and_shape_facts",
        "tier": "fit_calibrated (accumulation constant, PDG masses) / finite_diagnostic (held-out, shape)",
        "real_ratios": {br: {"R1": real_ratios(br)[0], "R2": real_ratios(br)[1],
                             "R2_over_R1": real_ratios(br)[1] / real_ratios(br)[0], "shape": shapes[br]}
                        for br in BRANCHES},
        "held_out": {br: results[br] for br in BRANCHES},
        "honest_verdict": (
            "COMPUTED FACTS (no works/fails judgment, per the materialist-bias guard). (A) Real "
            "consecutive-generation ratios are non-uniform in every branch, with DIFFERENT shapes: "
            "up/lepton decelerate (R2<R1), down accelerates (R2>R1). (B) A single accumulation "
            "constant calibrated to R1 reproduces R1 exactly but its held-out prediction of R2 is "
            "off by 55%-1130% -- one constant, one ratio, no held-out compression under a uniform "
            "profile. (C) A uniform accumulation gives consecutive-ratio R2/R1 = 1 (computed here), "
            "while the up-type and lepton hierarchies have R2/R1 < 1 (decelerating) -- so a "
            "constant-rate accumulation cannot produce them, and the accumulation mechanisms on "
            "record (EQ-070 'mildly accelerating', EQ-071 compounding) trend toward acceleration, "
            "not deceleration; reproducing those branches needs a per-branch rate that DECREASES "
            "across generations (no specific '>>1' magnitude is asserted -- an earlier draft's "
            "mis-cited overstatement, corrected). FRAMEWORK "
            "reading (stance_for('mass')): the ratios are graph readouts and calibrating the graph "
            "constant to them is legitimate (fit_calibrated); the held-out miss and shape mismatch "
            "are computed structural properties of the current accumulation, an OPEN internal "
            "question about the accumulation PROFILE -- not a failure. This file reports the "
            "calibration, the held-out numbers, and the shape mismatch; it does not claim the "
            "hierarchy is reproduced and does not claim it is underivable."
        ),
        "claim_boundary": [
            "the accumulation constant is fit_calibrated to R1 (reproduces it trivially, 1 param -> "
            "1 number); the held-out R2 prediction is the honest test of predictive content",
            "COMPUTED: held-out R2 off by 55%-1130% (uniform profile gives R2/R1=1), while up/lepton "
            "have R2/R1<1 (decelerating) -- so a constant-rate accumulation cannot reproduce them; "
            "reproducing them needs a per-branch rate that DECREASES across generations. Structural "
            "facts, not a works/fails verdict. No '>>1' per-gen magnitude asserted (an earlier draft "
            "mis-cited this to EQ-071; corrected -- EQ-070 measured only 'mild' acceleration)",
            "MATERIALIST-BIAS GUARD (this file follows it): a fit_calibrated graph constant is not a "
            "defect; the ratios are graph readouts (stance_for('mass')); what is OPEN is an internal "
            "question about the accumulation PROFILE (can it be enriched per-branch to decelerate), "
            "legitimately calibratable -- NOT an external-derivation demand and NOT a failure",
            "does NOT reduce the free-parameter count (a decelerating per-branch profile would need "
            "more structure than one constant); does NOT bridge to GeV (ratios only, EQ-068 open); "
            "n<->generation remains Attempt 13's unproven conjecture",
            "consistent with Attempt 17 (per-branch geometric-mean r missed the middle generation "
            "50-71%) -- this file adds the explicit held-out number and the accelerate/decelerate "
            "shape diagnosis Attempt 17 did not have",
        ],
    }
    print("\nHONEST FENCE:")
    print(f"  {report['honest_verdict']}")
    return report


if __name__ == "__main__":
    r = run_fixture()
    print("\n" + json.dumps({k: v for k, v in r.items() if k not in ("honest_verdict", "claim_boundary")},
                            indent=2, sort_keys=True, default=str))
