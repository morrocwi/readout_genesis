"""A principled generation->observable mapping: intrinsic peaks of cond#(Theta(t)). v0.1.

The dynamic_range_from_degeneracy candidate found (FACT O) that the accumulated Theta drives a large,
convergent cond#(G[Theta(t)]) by approaching the graph-operator degeneracy |Theta|=1, but (FACT P,
retracted) the accel/decel hierarchy SIGN was a slicing artifact -- cond#(t) oscillates and reading
'generations' at arbitrary physical times gives a sign that flips between adjacent windows. The named
open lever was: define a PRINCIPLED generation->observable mapping (not hand-picked times). This file
does that and reports what it yields.

THE MAPPING. cond#(Theta(t)) oscillates because Theta(t) is a driven oscillator; its LOCAL MAXIMA are
intrinsic, discrete, hand-pick-free landmarks -- each is a moment where the graph operator is locally
MOST degenerate (Theta closest to 1 within that oscillation) = a locally-heaviest mode. Generation k
:= the k-th local maximum of cond#(Theta(t)). This is the natural discrete analog, in the fixed
(convergent) diagnostic, of the arc's n<->generation convention (Attempt 13) -- discrete and intrinsic
to the trajectory, not an arbitrary time slice.

*** COMPUTED FACTS (materialist-bias guard, ZERO_INFINITY_DUAL_DIAGNOSIS.md Part 4b -- no works/fails
    words; a principled mapping that partly succeeds, with its limit stated):

    FACT Q (the positive result -- the MAPPING is principled; the ratio, where defined, converges):
    the two well-separated intrinsic peaks give a dt-CONVERGENT ratio. At M_Theta=4 the peak heights
    are ~1.346 and ~127.75, and their ratio converges to ~94.94x under dt-refinement: 94.86, 94.92,
    94.93, 94.93, 94.94 for dt = 0.004..0.00025 (a 16x dt range, spread < 0.1). The intrinsic-landmark
    generations give a well-defined, hand-pick-free ratio -- resolving FACT P's arbitrary-slicing
    (the sign no longer flips with the window). This is the arc's first stable, convergent,
    hand-pick-free mass-RATIO.

    FACT Q' (the SEVERE applicability limit -- caught by review, do NOT read ~94.94x as 'the
    mechanism's mass-ratio'): the convergent ratio is DEFINED at essentially the ISOLATED point
    M_Theta=4.0 only. Sweeping M_Theta in {3, 3.5, 4.5, 5, 6, 8, 10} at T=10, the mapping returns NO
    defined ratio at all (not a different value -- UNDEFINED): at M_Theta>=4.5 the intermediate
    generation never forms a peak above ~10 (peaks go straight from the near-singular spike to ~1.x:
    5.56, 3.29, 2.14, 1.57, 1.38), and at M_Theta=3.5 two peaks are both near-singular (19798, 9621).
    So a well-separated intermediate generation exists only in a razor-thin M_Theta window around 4.0.
    The convergent ~94.94x is therefore a single applicability point, NOT a robust mechanism output;
    the mapping CONCEPT is principled, but its applicability (a clean intermediate peak) is fragile.

    FACT R (the singular-generation limit): the peak that sits essentially AT the degeneracy
    |Theta|=1 is numerically HYPERSENSITIVE and does NOT converge -- its height is ~2400, ~5900,
    ~11000 at successive dt (a near-singular spike where cond# = (1+|Theta|)/|1-|Theta|| -> infinity
    as |Theta| -> 1). So the principled mapping gives convergent ratios only for generations BOUNDED
    AWAY from the singularity; the extreme ratios -- exactly where a ~10^5.5 fermion spread would come
    from -- are ill-defined at the degeneracy. There are only ~2 well-separated convergent peaks even
    at M_Theta=4 (then Theta decays and later peaks are ~1, noise), so this yields a convergent
    2-generation ratio (~95x), NOT a full convergent 3-generation hierarchy.

    FRAMEWORK-NATIVE reading (stance_for('mass')): a principled generation mapping DOES exist -- the
    intrinsic peaks of the spectral-gap readout -- and it yields a convergent ~95x mass-ratio between
    two generations (mode decouplings of increasing strength). What is OPEN (internal, calibratable):
    (1) the third generation would need Theta to approach 1 even more closely, where the readout is
    numerically ill-defined (a real degeneracy, not a bug) -- so reaching the extreme ratios needs a
    regularized reading AT the degeneracy; (2) ~95x is one convergent ratio, still short of the full
    fermion spread. NOT a failure and NOT a reproduction claim: a principled mapping that gives the
    arc's first stable convergent mass-ratio, with the singular-generation limit named. ***

Tier: finite_diagnostic (the convergent peak ratio, the singular-peak non-convergence). Dr (the
peaks-as-generations interpretation). NOT Th_coqc.
"""
from __future__ import annotations

import json

import numpy as np

from domains.standard_model.item1_exploration.field_sourced_accumulation.field_sourced_accumulation_v0_1 import (  # noqa: E501
    D,
    K,
    M_JOINT,
    grad_v,
    grad2_v,
)

# Self-contained (the sibling candidates fixed_q_diagnostic/dynamic_range_from_degeneracy live on
# separate unmerged branches; only field_sourced_accumulation is on main). BOOST and the graph
# operator's condition number are inlined here so this file imports only merged code.
BOOST = np.array([[0.0, 1.0], [1.0, 0.0]])


def cond_graph_operator(theta):
    """cond#(G[Theta]) for G[Theta] = I + Theta*boost: singular values |1+-Theta|, so
    cond = (1+|Theta|)/|1-|Theta||. Large only near the degeneracy |Theta|=1; ->1 far from it."""
    a = abs(theta)
    denom = abs(1.0 - a)
    if denom < 1e-300:
        return float("inf")
    return (1.0 + a) / denom


DEFAULT_IC = ([1.0, 0.5], [0.8, 0.3])
SINGULAR_SPIKE = 1000.0     # peaks above this sit essentially at |Theta|=1 (near-singular, ill-defined)

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


def cond_trajectory(m_theta, dt, T):
    """cond#(G[Theta(t)]) along the whole trajectory (the FIXED, convergent reader at each step's
    accumulated Theta -- NOT the step-product)."""
    if m_theta <= 0 or dt <= 0:
        raise ValueError("m_theta and dt must be positive")
    phi = np.array(DEFAULT_IC[0], float); phi_nm1 = phi.copy()
    psi = np.array(DEFAULT_IC[1], float); psi_nm1 = psi.copy()
    theta = 0.0; theta_nm1 = 0.0
    a_phi = M_JOINT / dt ** 2 + D / (2 * dt)
    a_psi = M_JOINT / dt ** 2 - D / (2 * dt)
    conds = []
    for _ in range(int(round(T / dt))):
        s_theta = float(phi @ BOOST @ psi)
        theta_np1 = 2 * theta - theta_nm1 - dt * dt * (1.0 / m_theta) * (theta / 2.0 + K * s_theta)
        g = np.eye(2) + theta * BOOST
        b_phi = -K * (g @ phi) - grad_v(phi) + (2 * M_JOINT / dt ** 2) * phi + (D / (2 * dt) - M_JOINT / dt ** 2) * phi_nm1
        b_psi = -K * (g.T @ psi) - grad2_v(phi) * psi + (2 * M_JOINT / dt ** 2) * psi - (M_JOINT / dt ** 2 + D / (2 * dt)) * psi_nm1
        phi_new = b_phi / a_phi
        psi_new = b_psi / a_psi
        if not (np.all(np.isfinite(phi_new)) and np.all(np.isfinite(psi_new))):
            break
        conds.append(cond_graph_operator(theta))
        phi_nm1, phi = phi, phi_new
        psi_nm1, psi = psi, psi_new
        theta_nm1, theta = theta, theta_np1
    return np.array(conds)


def generation_peaks(m_theta, dt, T):
    """Intrinsic generations = local maxima of cond#(Theta(t)), returned sorted high->low."""
    c = cond_trajectory(m_theta, dt, T)
    idx = [i for i in range(1, len(c) - 1) if c[i] > c[i - 1] and c[i] >= c[i + 1]]
    return sorted((c[i] for i in idx), reverse=True)


def convergent_ratio(m_theta, dt, T):
    """The ratio of the two well-separated peaks bounded AWAY from the singular spike (a hand-pick-
    free 2-generation mass-ratio). Returns (big_peak, small_peak, ratio)."""
    peaks = [h for h in generation_peaks(m_theta, dt, T) if h < SINGULAR_SPIKE]
    big = next((h for h in peaks if h > 10.0), None)          # the strong (near-degenerate) peak
    small = next((h for h in peaks if h < 10.0), None)        # the weak peak
    if big is None or small is None:
        return None
    return big, small, big / small


def run_fixture():
    print("== 0. TIER TAG (mandatory) ==")
    print("  finite_diagnostic (convergent peak ratio, singular-peak non-convergence) / Dr (peaks-as-")
    print("  generations interpretation). NOT Th_coqc. Computed facts + tier per the materialist-bias")
    print("  guard -- a principled mapping that partly succeeds, limit stated, no value-verdict.")

    print("\n== 1. FACT Q: intrinsic-peak generations give a dt-CONVERGENT ~95x mass-ratio (m_theta=4) ==")
    rows = {}
    for dt in (0.004, 0.002, 0.001, 0.0005, 0.00025):
        rows[dt] = convergent_ratio(4.0, dt, 10.0)
        big, small, r = rows[dt]
        print(f"   dt={dt:7.5f}: peaks = {small:.3f}, {big:.3f}   ratio = {r:.3f}")
    ratios = [rows[dt][2] for dt in rows]
    spread = max(ratios) - min(ratios)
    ck("the two well-separated intrinsic peaks give a dt-CONVERGENT ratio ~94.9x (spread < 0.1 across "
       "a 16x dt range) -- the arc's first stable, hand-pick-free mass-ratio, resolving FACT P's "
       "arbitrary-slicing (the sign no longer flips with an arbitrary window)",
       spread < 0.1 and 90 < ratios[-1] < 100, {"ratios": [round(r, 3) for r in ratios], "spread": round(spread, 4)})

    print("\n== 2. FACT R: the peak AT the degeneracy |Theta|=1 is hypersensitive (does NOT converge) ==")
    spikes = {}
    for dt in (0.002, 0.001, 0.0005):
        peaks = generation_peaks(4.0, dt, 10.0)
        spikes[dt] = peaks[0] if peaks and peaks[0] >= SINGULAR_SPIKE else None
        print(f"   dt={dt:7.5f}: near-singular spike height = "
              f"{'none' if spikes[dt] is None else round(spikes[dt], 1)}")
    vals = [v for v in spikes.values() if v is not None]
    ck("the peak sitting AT |Theta|=1 is numerically hypersensitive -- its height varies by >2x "
       "across dt (cond# -> infinity there), so it does NOT converge; the principled mapping is "
       "well-defined only for generations BOUNDED AWAY from the singularity, and the extreme ratios "
       "(where 10^5.5 would come from) are ill-defined at the real degeneracy",
       len(vals) >= 2 and max(vals) / min(vals) > 2.0,
       {str(k): (None if v is None else round(v, 1)) for k, v in spikes.items()})

    print("\n== 3. FACT Q': the convergent ratio is DEFINED only at an isolated M_Theta (fragile) ==")
    mt_scan = {mt: convergent_ratio(mt, 0.0005, 10.0) for mt in (3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0)}
    for mt, cr in mt_scan.items():
        print(f"   M_Theta={mt:5.1f}: ratio = {'UNDEFINED' if cr is None else f'{cr[2]:.3f}'}")
    defined = [mt for mt, cr in mt_scan.items() if cr is not None]
    ck("the convergent ratio is DEFINED (a well-separated intermediate peak forms) at essentially "
       "M_Theta=4.0 ALONE -- at every other M_Theta tested it is UNDEFINED (not different, undefined). "
       "So ~94.94x is a single applicability point, NOT a robust mechanism mass-ratio; the mapping "
       "CONCEPT is principled but its applicability is fragile",
       defined == [4.0], defined)

    print("\n== 4. HONEST LIMITS ==")
    print("   (a) only ~2 well-separated convergent generations even at M_Theta=4 -- a 2-generation")
    print("       ratio (~95x), NOT a full convergent 3-generation hierarchy")
    print("   (b) ~95x is one convergent ratio at ONE isolated M_Theta, far below the ~10^5.5 spread")
    print("   (c) the intermediate peak forms only in a razor-thin M_Theta window (FACT Q') -- not robust")
    print("   (d) the third generation needs Theta even closer to 1, where the reading is ill-defined")
    print("       (a real degeneracy, not a bug) -- reaching extreme ratios needs a regularized read")

    if FAILS:
        print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
    else:
        print("\nAll checks PASS.")

    big, small, r = rows[0.00025]
    report = {
        "schema": "principled-generation-mapping-report-v0.1",
        "status": "COMPUTED_principled_peak_mapping_gives_a_convergent_ratio_but_ONLY_at_isolated_m_theta_4_fragile",
        "tier": "finite_diagnostic (convergent peak ratio, M_Theta-fragility, singular-peak non-convergence) / Dr (peaks-as-generations)",
        "convergent_ratio_by_dt": {str(dt): round(rows[dt][2], 4) for dt in rows},
        "converged_ratio": round(r, 3),
        "peak_heights_m4": {"small": round(small, 4), "big": round(big, 4)},
        "m_theta_where_ratio_defined": [mt for mt, cr in mt_scan.items() if cr is not None],
        "honest_verdict": (
            "COMPUTED FACTS (no works/fails judgment, per the materialist-bias guard; corrected after "
            "review). Founder ask '2' -- define a PRINCIPLED generation->observable mapping (FACT P "
            "showed arbitrary time slices give a sign that flips with the window). THE MAPPING: "
            "generation k = the k-th local maximum of cond#(Theta(t)) -- intrinsic, discrete, "
            "hand-pick-free landmarks. (Q, positive) where a well-separated intermediate peak exists, "
            "the two peaks give a dt-CONVERGENT ratio ~94.94x (94.86->94.94 across a 16x dt range) -- "
            "the arc's first stable, hand-pick-free mass-RATIO, resolving FACT P's slicing artifact. "
            "(Q', SEVERE limit caught by review) but that convergent ratio is DEFINED only at "
            "essentially the ISOLATED point M_Theta=4.0 -- at every other M_Theta tested (3, 3.5, 4.5, "
            "5, 6, 8, 10) the mapping returns NO defined ratio (UNDEFINED, not different: the "
            "intermediate peak never forms above ~10, or two peaks are both near-singular). So "
            "~94.94x is a single applicability point, NOT a robust mechanism mass-ratio; the mapping "
            "CONCEPT is principled, its applicability is fragile. (R) the peak AT the degeneracy "
            "|Theta|=1 is numerically hypersensitive (non-convergent, cond#->infinity), so the extreme "
            "ratios are ill-defined at the real degeneracy. LIMITS: 2 generations not 3; one "
            "convergent ratio at one isolated M_Theta, far below 10^5.5. FRAMEWORK reading: a "
            "principled generation mapping (intrinsic peaks) exists and CAN give a convergent ratio, "
            "but only in a razor-thin M_Theta window; OPEN -- make the intermediate generation form "
            "robustly across M_Theta, regularize the reading at the degeneracy, reach the full spread. "
            "NOT a failure and NOT a reproduction claim: a principled mapping that yields a convergent "
            "ratio at one fragile point, with the fragility disclosed."
        ),
        "claim_boundary": [
            "POSITIVE (FACT Q): the principled mapping (intrinsic peaks of cond#(Theta(t))) gives a "
            "dt-CONVERGENT ~94.94x ratio between two generations WHERE APPLICABLE -- hand-pick-free, "
            "resolving FACT P's arbitrary-slicing (no more window-dependent sign)",
            "SEVERE LIMIT (FACT Q', caught by review): that ratio is DEFINED only at the isolated "
            "point M_Theta=4.0 -- at every other M_Theta tested (3, 3.5, 4.5, 5, 6, 8, 10) it is "
            "UNDEFINED (the intermediate peak does not form, or two peaks are both singular). So "
            "~94.94x is a single applicability point, NOT a robust mechanism mass-ratio; the mapping "
            "CONCEPT is principled but its applicability is fragile",
            "LIMIT (FACT R): the generation AT the degeneracy |Theta|=1 is numerically hypersensitive "
            "(non-convergent, cond#->infinity) -- well-defined only bounded away from the singularity; "
            "extreme ratios ill-defined there (a real degeneracy, not a bug)",
            "only ~2 well-separated convergent generations even at M_Theta=4 (not a full 3-gen "
            "hierarchy); ~95x is one convergent ratio at one M_Theta, far below the ~10^5.5 spread",
            "does NOT reduce parameters, bridge to GeV, or reproduce the hierarchy; builds on the "
            "degeneracy lever (FACT O) + field_sourced (EQ-071); self-contained (inlines "
            "cond_graph_operator); tested at one field IC. MATERIALIST-BIAS GUARD: computed facts + "
            "tier, a principled mapping with a convergent ratio (FACT Q) but a fragile applicability "
            "(FACT Q') and a singular-generation limit (FACT R), NOT a failure-verdict and NOT an "
            "overclaim of reproduction",
        ],
    }
    print("\nHONEST FENCE:")
    print(f"  {report['honest_verdict']}")
    return report


if __name__ == "__main__":
    rep = run_fixture()
    print("\n" + json.dumps({k: v for k, v in rep.items() if k not in ("honest_verdict", "claim_boundary")},
                            indent=2, sort_keys=True, default=str))
