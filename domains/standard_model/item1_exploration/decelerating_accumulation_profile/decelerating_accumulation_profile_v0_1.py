"""A DECELERATING accumulation profile -- the exact lever FACT C named. v0.1.

The calibrate-graph-hierarchy held-out test (EQ-072 candidate, calibrate_graph_hierarchy_heldout/)
computed FACT C: a UNIFORM-step accumulation gives consecutive-generation ratio R2/R1 = 1, but the
up-type and lepton branches have R2/R1 < 1 (decelerating). It named the concrete open lever:
"a per-branch accumulation rate that can DECREASE across generations." This file BUILDS that
profile and computes what it does -- and, crucially, what it costs.

THE MODEL. A uniform accumulation is g_n = g0 * r^n, so every consecutive ratio equals r
(R1 = R2 = r, R2/R1 = 1 -- FACT C). A DECELERATING profile lets the per-step rate shrink
geometrically by a factor q per generation:
    step-1 rate = r          -> R1 = g1/g0 = r
    step-2 rate = r * q      -> R2 = g2/g1 = r * q      (q < 1 => decelerating, q > 1 => accelerating)
    => R2 / R1 = q   EXACTLY, by construction.
So a decelerating profile reproduces ANY branch's R2/R1 -- but only by introducing q as a SECOND
per-branch constant. This is the honest content of this file, reported per the materialist-bias
guard (ZERO_INFINITY_DUAL_DIAGNOSIS.md Part 4b -- no works/fails words; a fit_calibrated constant
is not a defect, and reproducing-by-construction is not a "win"):

*** COMPUTED FACTS ***

    FACT D: the decelerating profile (r, q) reproduces BOTH consecutive ratios of every branch
    EXACTLY (r = R1, q = R2/R1). This is 2 constants fitting 2 numbers -- a FIT, not a held-out
    prediction. It closes the shape gap FACT C named (it CAN decelerate: up q=0.231, lepton q=0.081
    both < 1) but does NOT compress the parameter count: it trades the held-out miss for a second
    per-branch free constant. So "enrich the profile to decelerate" removes the structural
    OBSTRUCTION (FACT C's R2/R1=1 ceiling) without, by itself, reducing free parameters.

    FACT E (the non-trivial test): is q DETERMINED by the graph -- i.e. is there ONE law q = f(r)
    (or a single shared q) across all three branches, so q is not independently free? Computed
    answer: NO. A single shared q fails outright (the branches span q in [0.081, 2.24], a 27x
    spread). And q is not a monotone function of r either: the up and lepton branches DECELERATE
    (q < 1) while the down branch ACCELERATES (q = 2.24 > 1) despite down having the SMALLEST r --
    so q even flips SIGN of the trend relative to r. There is no single graph law q=f(r) that yields
    all three branches' shapes. This is the computed obstruction to compression: deceleration is
    reachable per branch, but its rate q is (so far) an independent per-branch readout, not a
    determined function of the branch's own r.

    FRAMEWORK-NATIVE reading (stance_for('mass'): mass ratios = spectral-gap ratios of L_R): both r
    and q are graph readouts and calibrating them is legitimate (fit_calibrated). What is OPEN is
    whether a richer single graph mechanism forces q from r (or from the branch's other invariants)
    so the second constant is not independent -- an internal calibratable question about the graph's
    accumulation law, NOT a failure and NOT a claim that the hierarchy is reproduced. This file
    reports: the decelerating profile exists and reaches the shapes (FACT D); its rate q is not yet
    a determined function of r across branches (FACT E).

Tier: fit_calibrated (r, q fit to the two real ratios; PDG masses reused). finite_diagnostic (the
q-spread and the sign-flip-vs-r structural facts). NOT Th_coqc.
"""
from __future__ import annotations

import json

from domains.standard_model.fit_calibrated_registry import PDG_MASSES_GEV

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


def decelerating_profile(branch):
    """Fit the decelerating profile (r, q) to a branch. By construction r=R1 and q=R2/R1, so the
    reconstructed ratios are exact -- the honest point is that this needs a SECOND constant q, not
    that it 'predicts' anything. Returns the fit constants and the (trivially exact) reconstruction."""
    r1, r2 = real_ratios(branch)
    if r1 <= 0 or r2 <= 0:
        raise ValueError(f"branch {branch} has a non-positive mass ratio")
    r = r1               # step-1 rate
    q = r2 / r1          # per-generation deceleration factor (< 1 decel, > 1 accel)
    recon_R1 = r
    recon_R2 = r * q
    return {
        "r": r,
        "q": q,
        "shape": "decelerating" if q < 1 else "accelerating",
        "recon_R1": recon_R1,
        "recon_R2": recon_R2,
        "recon_R1_err": abs(recon_R1 - r1) / r1,
        "recon_R2_err": abs(recon_R2 - r2) / r2,
    }


def run_fixture():
    print("== 0. TIER TAG (mandatory) ==")
    print("  fit_calibrated (r, q fit to the two real ratios; PDG masses reused) / finite_diagnostic")
    print("  (q-spread and sign-flip-vs-r facts). NOT Th_coqc. Reported as computed facts + tier per")
    print("  the materialist-bias guard -- reproducing-by-construction is not a 'win'; a second")
    print("  fit_calibrated constant is not a 'failure'.")

    profiles = {br: decelerating_profile(br) for br in BRANCHES}

    print("\n== 1. FACT D: the decelerating profile (r, q) reproduces BOTH ratios exactly (by construction) ==")
    for br, p in profiles.items():
        r1, r2 = real_ratios(br)
        print(f"   {br:7s}: r={p['r']:8.1f}  q={p['q']:.4f} ({p['shape']})  "
              f"-> recon R1={p['recon_R1']:.1f} (real {r1:.1f}), R2={p['recon_R2']:.1f} (real {r2:.1f})")
    ck("decelerating profile reconstructs R1 and R2 to machine precision in every branch -- FACT D: "
       "it CAN reach the decelerating shapes, but this is 2 constants (r,q) fitting 2 numbers, a FIT "
       "not a held-out prediction",
       all(p["recon_R1_err"] < 1e-9 and p["recon_R2_err"] < 1e-9 for p in profiles.values()),
       {br: (round(p["recon_R1_err"], 12), round(p["recon_R2_err"], 12)) for br, p in profiles.items()})
    ck("up and lepton profiles DECELERATE (q<1) -- the profile reaches exactly the shape FACT C said "
       "a uniform accumulation could not (uniform gives R2/R1=q=1)",
       profiles["up"]["q"] < 1 and profiles["lepton"]["q"] < 1,
       {br: round(profiles[br]["q"], 4) for br in ("up", "lepton")})

    print("\n== 2. FACT E: is q DETERMINED by the graph -- one law q=f(r), or a shared q? (the real test) ==")
    qs = {br: profiles[br]["q"] for br in BRANCHES}
    q_vals = list(qs.values())
    q_spread = max(q_vals) / min(q_vals)
    print(f"   per-branch q: " + ", ".join(f"{br}={qs[br]:.4f}" for br in BRANCHES))
    print(f"   q-spread (max/min) = {q_spread:.1f}x  -> a single SHARED q cannot fit all three")
    print("   q vs r (is q a monotone function of the branch's own r?):")
    for br in sorted(BRANCHES, key=lambda b: profiles[b]["r"]):
        p = profiles[br]
        print(f"     {br:7s}: r={p['r']:8.1f}  q={p['q']:.4f}  ({p['shape']})")
    print("   -> down has the SMALLEST r but ACCELERATES (q>1); up/lepton have larger r and DECELERATE")
    print("      (q<1): q flips sign-of-trend relative to r. No single law q=f(r) yields all three.")
    ck("a single shared q cannot fit all branches -- q spans >10x (0.081 to 2.24), a computed fact "
       "that deceleration rate is NOT one universal constant",
       q_spread > 10.0, round(q_spread, 2))
    ck("q is not a monotone function of r across branches -- down (smallest r) accelerates while "
       "up/lepton (larger r) decelerate, so q even flips the sign of the trend vs r: there is no "
       "single graph law q=f(r) reproducing all three shapes (the computed obstruction to "
       "compressing q away)",
       profiles["down"]["q"] > 1 and profiles["up"]["q"] < 1 and profiles["lepton"]["q"] < 1
       and profiles["down"]["r"] < profiles["up"]["r"] and profiles["down"]["r"] < profiles["lepton"]["r"],
       {br: (round(profiles[br]["r"], 1), round(profiles[br]["q"], 4)) for br in BRANCHES})

    if FAILS:
        print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
    else:
        print("\nAll checks PASS.")

    report = {
        "schema": "decelerating-accumulation-profile-report-v0.1",
        "status": "COMPUTED_decelerating_profile_reaches_shapes_but_rate_q_is_not_yet_determined_by_graph",
        "tier": "fit_calibrated (r, q; PDG masses) / finite_diagnostic (q-spread, sign-flip-vs-r)",
        "profiles": {br: profiles[br] for br in BRANCHES},
        "q_spread_max_over_min": q_spread,
        "honest_verdict": (
            "COMPUTED FACTS (no works/fails judgment, per the materialist-bias guard). (D) The "
            "decelerating profile g_n=g0*prod(r*q^k) reproduces BOTH consecutive-generation ratios of "
            "every branch EXACTLY -- r=R1, q=R2/R1 -- so it reaches the decelerating shapes FACT C "
            "said a uniform accumulation could not (up q=0.231, lepton q=0.081, both <1). But this is "
            "2 constants (r,q) fitting 2 numbers: a FIT, not a held-out prediction. Enriching the "
            "profile to decelerate removes FACT C's R2/R1=1 obstruction WITHOUT, by itself, reducing "
            "the free-parameter count -- it trades the held-out miss for a second per-branch constant "
            "q. (E) The non-trivial test is whether q is DETERMINED by the graph: is there one law "
            "q=f(r) or a shared q? Computed answer NO -- q spans 27x across branches (0.081 to 2.24), "
            "and down (smallest r) ACCELERATES while up/lepton (larger r) DECELERATE, so q flips the "
            "sign of the trend vs r; no single graph law q=f(r) yields all three shapes. FRAMEWORK "
            "reading (stance_for('mass')): r and q are graph readouts, calibrating them is legitimate "
            "(fit_calibrated); OPEN is whether a richer single graph mechanism FORCES q from r (or "
            "other branch invariants) so the second constant is not independent -- an internal "
            "calibratable question, NOT a failure and NOT a claim the hierarchy is reproduced. Net: "
            "deceleration is reachable per branch (obstruction removed), but its rate q is so far an "
            "independent per-branch readout, not a determined function of the branch's own r."
        ),
        "claim_boundary": [
            "the profile (r, q) reproduces R1 and R2 by construction (r=R1, q=R2/R1) -- this is a FIT "
            "of 2 constants to 2 numbers, NOT a held-out prediction; do not read FACT D as a "
            "'success' at reproducing masses",
            "COMPUTED: deceleration is reachable per branch (up/lepton q<1), removing FACT C's "
            "R2/R1=1 obstruction; but q is a SECOND per-branch free constant -- the free-parameter "
            "count is not reduced by this step alone",
            "COMPUTED (FACT E): no single graph law q=f(r) and no shared q fits all three branches "
            "(q spans 27x; down accelerates with the smallest r while up/lepton decelerate). The "
            "deceleration RATE is, so far, an independent per-branch readout",
            "MATERIALIST-BIAS GUARD (this file follows it): r and q are graph readouts "
            "(stance_for('mass')); calibrating them is legitimate (fit_calibrated); what is OPEN is "
            "an internal question -- can a richer single graph mechanism force q from r -- "
            "legitimately calibratable, NOT an external-derivation demand and NOT a failure",
            "does NOT bridge to GeV (ratios only, EQ-068 open); n<->generation remains Attempt 13's "
            "unproven conjecture; builds directly on the calibrate-graph-hierarchy held-out FACT C",
        ],
    }
    print("\nHONEST FENCE:")
    print(f"  {report['honest_verdict']}")
    return report


if __name__ == "__main__":
    r = run_fixture()
    print("\n" + json.dumps({k: v for k, v in r.items() if k not in ("honest_verdict", "claim_boundary")},
                            indent=2, sort_keys=True, default=str))
