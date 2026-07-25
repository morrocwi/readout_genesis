#!/usr/bin/env python3
"""Affine graph G[Theta_n] = G_0 + Theta_n * G_a with a non-compact generator, v0.1.

Closes the explicit faithfulness caveat left by the merged accumulating_graph_dynamic_range
candidate (both repos, 2026-07-25): that candidate showed a non-compact ACCUMULATING operator
unlocks dynamic range, but used G = boost(Theta) = exp(Theta*L) -- a matrix EXPONENTIAL, which is
NOT literally the mother equation's operator form. The mother equation's actual operator is AFFINE
in the geometry state: G[Theta_n] = G_0 + sum_a Theta_n^a * G_a
(source_root/READOUT_GENESIS_CORE_SNAPSHOT.md:1090). This file tests whether that FAITHFUL affine
form -- NOT an exponential -- ALSO produces the unbounded growth when the geometry state Theta
accumulates (founder-chosen Option A).

CONSTRUCTION (all faithful to the mother equation's affine operator, verified before building):
  G_0 = I (base operator)
  G_a = [[0,1],[1,0]]  -- the SAME so(1,1) boost-direction generator as Attempt 13, but used
                          AFFINELY here (G_0 + Theta*G_a), NOT exponentiated. Non-compact character.
  G[Theta] = I + Theta*G_a = [[1, Theta],[Theta, 1]]  -- singular values 1 +/- Theta, genuinely
                          NON-ORTHOGONAL (anisotropic: stretches one axis, shrinks the other).
  Theta accumulates: Theta_{n+1} = Theta_n + d_theta  -- the simplest instance of the spec's
                          Theta_{n+1} = A_Theta*Theta_n + source (A_Theta=1, constant source), i.e.
                          the graph genuinely CHANGES CUMULATIVELY every step, as the founder noted.

MEASURE: the CONDITION NUMBER (sv_max/sv_min) of the accumulated product prod_k G[Theta_k]. This
is the RATIO of the operator's two principal scales -- the faithful dimensionless analog of a mass
RATIO / spectral-gap ratio (exactly what falsify_particle_graph.py identifies as the meaningful
comparison, not absolute values). A non-compact (anisotropic) generator makes this ratio grow
unboundedly; a compact (isotropic) one keeps it at exactly 1.

CLEAN single-variable control: the SAME affine form with a COMPACT generator [[0,-1],[1,0]]
(rotation direction). G = I + Theta*[[0,-1],[1,0]] is a scaled rotation -- isotropic -- condition
number stays exactly 1. Only the generator direction changes; the affine form, the accumulation,
and every parameter are identical. This isolates non-compactness as the single driver.

Tier: finite_diagnostic (exact numerical linear algebra on the affine operator; the generator's
boost/rotation character is standard external math, Borrowed/+reals, same tiering as Attempt 13 --
NOT Th_coqc). Dr for the item-1 interpretation.

HONEST FENCE up front: this CLOSES the prior faithfulness caveat (the mother equation's ACTUAL
affine form, not an exponential, gives the growth) -- a real step forward. But it is STILL NOT
PREDICTIVE by itself: the accumulation rate d_theta is a free parameter (like Attempt 13's theta,
Attempt 17's r), so any condition number is reachable. Removing the ceiling faithfully is
NECESSARY, not SUFFICIENT; value-selection stays the open item Attempts 15-17 left.
"""
from __future__ import annotations

import json
import math

import numpy as np

N_STEPS = 80            # accumulation steps
D_THETA = 0.002         # per-step Theta increment -- free parameter, NOT derived (fit_calibrated status)
BASELINE_58X = 57.84    # today's native dynamic-range ceiling
FERMION_MASS_SPREAD = 10 ** 5.5   # ~3.16e5, electron-to-top mass ratio (the range to beat)

G0 = np.eye(2)
G_NONCOMPACT = np.array([[0.0, 1.0], [1.0, 0.0]])    # boost-direction generator (used affinely)
G_COMPACT = np.array([[0.0, -1.0], [1.0, 0.0]])      # rotation-direction control (compact)

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


def singular_values(matrix):
    return sorted(np.linalg.svd(matrix, compute_uv=False), reverse=True)


def condition_number(matrix) -> float:
    s = singular_values(matrix)
    return s[0] / s[-1] if s[-1] > 0 else float("inf")


def accumulate_affine(generator, n_steps: int, d_theta: float):
    """Walk the affine graph G[Theta_n] = G_0 + Theta_n*generator with Theta accumulating by
    d_theta each step; return the accumulated product and the per-step condition-number trace."""
    if not math.isfinite(d_theta) or d_theta <= 0:
        raise ValueError("d_theta must be finite and positive (Theta must genuinely accumulate)")
    prod = np.eye(2)
    theta = 0.0
    cond_trace = []
    for _ in range(n_steps):
        theta += d_theta
        g = G0 + theta * generator          # AFFINE, not exp(theta*generator)
        prod = g @ prod
        cond_trace.append(condition_number(prod))
    return prod, cond_trace, theta


def run_fixture():
    print("== 0. TIER TAG (mandatory) ==")
    print("  finite_diagnostic (exact linear algebra on the AFFINE mother-equation operator;")
    print("  generator character Borrowed/+reals, same as Attempt 13 -- NOT Th_coqc). Dr for the")
    print("  item-1 interpretation. d_theta is a free parameter, NOT derived (Attempts 15-17).")

    print("\n== 1. single-step AFFINE operator is genuinely non-orthogonal (the mother's form) ==")
    theta_probe = 0.3
    g = G0 + theta_probe * G_NONCOMPACT
    sv = singular_values(g)
    print(f"   G[Theta={theta_probe}] = I + Theta*[[0,1],[1,0]] = {g.tolist()}")
    print(f"   singular values = {[round(x, 4) for x in sv]}  (expected 1+Theta, 1-Theta)")
    ck("affine G[Theta] is NON-orthogonal (G G^T != I) -- a real anisotropic operator, not a "
       "rotation", not np.allclose(g @ g.T, np.eye(2)))
    ck("singular values are exactly 1+Theta and 1-Theta (non-compact stretch/shrink signature)",
       abs(sv[0] - (1 + theta_probe)) < 1e-12 and abs(sv[1] - (1 - theta_probe)) < 1e-12, sv)

    print("\n== 2. AFFINE NON-COMPACT accumulation (mother's actual form, no exponential) ==")
    prod_nc, trace_nc, theta_final = accumulate_affine(G_NONCOMPACT, N_STEPS, D_THETA)
    cond_nc = condition_number(prod_nc)
    print(f"   after {N_STEPS} steps (Theta accumulated 0 -> {theta_final:.3f}):")
    print(f"   condition number (sv_max/sv_min) of accumulated product = {cond_nc:.6g}")
    print(f"   log10(condition number) = {math.log10(cond_nc):.3f}")
    ck("min singular value did NOT underflow (result is within clean double precision, not a "
       "precision artifact)", singular_values(prod_nc)[-1] > 1e-100, singular_values(prod_nc)[-1])

    print("\n== 3. AFFINE COMPACT control (SAME affine form, only generator -> compact) ==")
    prod_c, _, _ = accumulate_affine(G_COMPACT, N_STEPS, D_THETA)
    cond_c = condition_number(prod_c)
    print(f"   condition number of accumulated product = {cond_c:.10f}")
    ck("MODE compact-affine stays at EXACTLY 1x condition number (isotropic scaling) -- the clean "
       "single-variable regime check: IDENTICAL affine form + accumulation + parameters, only the "
       "generator direction changed compact<->non-compact, isolates non-compactness as the driver",
       abs(cond_c - 1.0) < 1e-9, cond_c)

    print("\n== 4. THE CLAIM: the FAITHFUL affine form (not exp) unlocks the ratio range ==")
    print(f"   frozen G=I:            1x")
    print(f"   affine COMPACT:        {cond_c:.6g}x")
    print(f"   affine NON-COMPACT:    {cond_nc:.6g}x")
    print(f"   today's native ceiling: {BASELINE_58X}x")
    print(f"   fermion mass spread:    ~{FERMION_MASS_SPREAD:.3g}x (electron-to-top)")
    ck("affine non-compact condition number EXCEEDS today's ~58x ceiling by orders of magnitude",
       cond_nc > BASELINE_58X * 100, cond_nc)
    ck("affine non-compact condition number reaches at least the fermion mass spread ~10^5.5 -- "
       "showing the mother's ACTUAL affine operator, not just an exponential, spans the needed "
       "ratio range", cond_nc >= FERMION_MASS_SPREAD, cond_nc)

    print("\n== 5. growth is genuine exponential anisotropy (log-linear), robust to precision ==")
    # log10(condition number) grows linearly in step count -> constant-slope exponential stretch
    logs = [math.log10(c) for c in trace_nc if c > 0]
    early_slope = logs[len(logs) // 4] - logs[len(logs) // 4 - 1] if len(logs) > 8 else 0
    late_slope = logs[-1] - logs[-2]
    print(f"   log10(cond) grows from {logs[0]:.4f} to {logs[-1]:.4f} over {len(logs)} steps")
    print(f"   per-step slope stays positive, growth mildly accelerating (early {early_slope:.4f}, late {late_slope:.4f})")
    ck("log10(condition number) is monotonically increasing (genuine unbounded anisotropic growth, not a "
       "one-off numerical spike)", all(logs[i] <= logs[i + 1] + 1e-9 for i in range(len(logs) - 1)))

    print("\n== 6. d_theta sweep (range is FREELY TUNABLE -- the honest not-predictive point) ==")
    sweep = {}
    for dth in (0.001, 0.002, 0.004):
        p, _, _ = accumulate_affine(G_NONCOMPACT, N_STEPS, dth)
        sweep[dth] = condition_number(p)
        print(f"   d_theta={dth}: condition number = {sweep[dth]:.4g}x")
    print("   -> any target ratio is reachable by tuning d_theta. Faithful ceiling-removal is")
    print("      NECESSARY but NOT PREDICTIVE; value-selection stays open (Attempts 15-17).")

    if FAILS:
        print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
    else:
        print("\nAll checks PASS.")

    report = {
        "schema": "affine-graph-noncompact-growth-report-v0.1",
        "tier": "finite_diagnostic (affine operator linear algebra, Borrowed/+reals generator) / Dr (item-1 interpretation)",
        "n_steps": N_STEPS,
        "d_theta_free_not_derived": D_THETA,
        "theta_final": theta_final,
        "affine_noncompact_condition_number": cond_nc,
        "affine_compact_control_condition_number": cond_c,
        "frozen_baseline": 1.0,
        "native_ceiling": BASELINE_58X,
        "fermion_mass_spread": FERMION_MASS_SPREAD,
        "d_theta_sweep": sweep,
        "honest_verdict": (
            f"CLOSED the prior faithfulness caveat: the mother equation's ACTUAL affine operator "
            f"G[Theta]=G_0+Theta*G_a (NOT a matrix exponential) with a non-compact generator, walked "
            f"through a genuine Theta-accumulation, produces condition number {cond_nc:.4g}x -- past "
            f"today's ~58x ceiling and past the ~10^5.5 fermion-mass spread. The compact-affine "
            f"control (identical form, only generator direction changed) stays at exactly 1x, "
            f"isolating non-compactness as the driver. This is a REAL step forward from the merged "
            f"accumulating_graph candidate (which used an exponential). BUT still NOT predictive: "
            f"d_theta is free (sweep reaches any range), so faithful ceiling-removal is necessary, "
            f"not sufficient -- value-selection remains the open item Attempts 15-17 left."
        ),
        "claim_boundary": [
            "this uses the mother equation's ACTUAL affine operator form G_0+Theta*G_a (closing the "
            "explicit faithfulness caveat the merged accumulating_graph candidate left open) -- NOT "
            "a matrix exponential",
            "condition number (sv_max/sv_min) is the dimensionless mass-RATIO analog "
            "(spectral-gap-ratio, per falsify_particle_graph.py) -- NOT an absolute mass; no "
            "GeV/unit conversion is attempted, that problem stays open",
            "the compact-affine control (condition number exactly 1x) is a genuine single-variable "
            "regime check: same affine form, same accumulation, same parameters, only the generator "
            "direction changed -- non-compactness is proven to be the driver",
            "d_theta (accumulation rate) is a FREE parameter, NOT derived -- same status as Attempt "
            "13's theta and Attempt 17's r; removing the ceiling is necessary but NOT predictive",
            "the n<->generation identification remains Attempt 13's UNPROVEN conjecture -- not "
            "assumed or tested here; this measures dynamic RANGE only",
            "does not attempt the real (non-uniform) mass hierarchy (Option B, not chosen) -- known "
            "hard: Attempt 17's fit missed the middle generation 50-71%",
        ],
    }
    print("\nHONEST FENCE:")
    print(f"  {report['honest_verdict']}")
    return report


if __name__ == "__main__":
    r = run_fixture()
    print("\n" + json.dumps({k: v for k, v in r.items() if k not in ("honest_verdict", "claim_boundary")},
                            indent=2, sort_keys=True, default=str))
