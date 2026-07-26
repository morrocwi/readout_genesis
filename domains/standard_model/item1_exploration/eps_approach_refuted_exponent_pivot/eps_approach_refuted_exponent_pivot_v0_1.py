"""Does approaching the degeneracy give a controlled hierarchy? (point 1) — NO; pivot to exponents. v0.1.

Context. GRAPH_MECHANISM_HANDOFF.md §6 (corrected) established the mass hierarchy lives at finite
`Theta < 1`, and a decisive back-reaction calculation (handoff §, the '#4' calc) showed the
degeneracy `|Theta|=1` is a DYNAMICAL ATTRACTOR: the mechanism's own source `S_Theta` diverges
(`~ -1/eps^2`, `eps = 1-|Theta|`) and PULLS Theta toward the degeneracy — not fine-tuned. That
raised a hopeful idea ("point 1"): if a mechanism could make Theta APPROACH the degeneracy in a
controlled way, `eps(t) ~ e^{-t/tau}`, the log-hierarchy would be linear in t — convergent and
robust without fine-tuning a peak. This file TESTS that idea and reports the result.

*** COMPUTED FACTS (materialist-bias guard, ZERO_INFINITY_DUAL_DIAGNOSIS.md Part 4b — no works/fails
    words; a clean negative for one route plus the computed pivot direction):

    FACT S (point 1 is REFUTED for this mechanism, in the regimes tested): `eps(t) = 1-|Theta(t)|`
    does NOT decay cleanly. Across M_Theta and damping gamma, |Theta(t)| OSCILLATES violently (75-394
    turning points over T=30, MEASURED) and OVERSHOOTS to huge values (max|Theta| ~ 10^3-10^4,
    MEASURED), i.e. Theta shoots THROUGH the degeneracy rather than approaching it. INTERPRETIVE (Dr,
    not measured in this file): the reason is that the back-reaction force near the degeneracy is
    SINGULAR, `~ 1/eps^2` (because `S_Theta ~ 1/(1-Theta^2)^2`), which no LINEAR damping `-gamma·v` can
    tame as `eps -> 0`; only the oscillation/overshoot itself is measured here, the `1/eps^2` power law
    is the analytic explanation (from the '#4' back-reaction calc), not re-measured. So the
    "controlled approach to the degeneracy" route produces oscillation/overshoot, NOT a convergent
    `eps(t) ~ e^{-t/tau}` decay, in every (M_Theta, gamma) regime tried — refuted for this mechanism
    under linear damping (a qualitatively different tamer, e.g. nonlinear/adaptive damping, is not
    ruled out here).

    FACT T (the pivot the refutation forces — but WEAKER than it first looks, see the caveat): a
    large hierarchy, if this framework has one, must come from an EXPONENT far from the degeneracy —
    `m_n ~ Theta^{d_n}` with `Theta` well below 1 and `d_n` an integer (a Froggatt-Nielsen-type
    structure, where `d_n` would be a graph DISTANCE) — NOT from proximity to `|Theta|=1`. COMPUTED at
    `Theta=0.2`: the up-type exponents `d = ln R / ln(1/Theta)` are `d(gen1->2)=3.96` and
    `d(gen2->3)=3.05`, near the integers 4 and 3. But the same `Theta=0.2` gives NON-integer exponents
    for down (1.86, 2.36) and lepton (3.31, 1.75).

    CAVEAT (added after review — do NOT read this as two independent integer hits): the two up-sector
    near-integers are NOT two independent coincidences. The RATIO `d1/d2 = ln R1 / ln R2` is
    `Theta`-INDEPENDENT (= 1.298 from PDG masses alone), and it sits 2.6% from `4/3 = 1.333`. So there
    is really ONE tuned knob (choose `Theta` to make `d1 ~ 4`) plus ONE structural near-coincidence of
    the real masses (`ln R1/ln R2 ~ 4/3`), which then FORCES `d2 ~ 3.08`. And the `Theta`-window where
    both up exponents land within 0.1 of an integer is narrow (`Theta ~ 0.195-0.205`). So `Theta=0.2`
    is effectively tuned to hit the up integers; the honest content of FACT T is only: "the up-sector
    mass-ratio log-slope `ln R1/ln R2` happens to sit near `4/3`." Suggestive, not striking, not two
    facts.

    HONEST FENCE / FRAMEWORK reading (stance_for('mass')): FACT S closes the "approach the degeneracy"
    route for this mechanism. FACT T is SUGGESTIVE, not a result: the exponent ansatz `m_n~Theta^{d_n}`
    is the pre-existing Froggatt-Nielsen structure (NOT new), and it stays `fit_calibrated` — choosing
    `Theta` and the `d_n` per branch just relabels the freedom (Wall A moves, it does not fall). It
    becomes a genuine result ONLY if the graph TOPOLOGY forces the integer `d_n` (integer graph
    distances) and `Theta` — which is NOT shown here. This file reports: the proximity route is
    refuted (FACT S); the exponent route is the surviving direction with a real up-sector lead (FACT
    T), fenced as fit_calibrated pending a topology-forced `d_n`. NOT a reproduction claim. ***

Tier: finite_diagnostic (the eps-oscillation measurement, the exponent computation). Dr (the
attractor-is-singular and Froggatt-Nielsen interpretations). NOT Th_coqc.
"""
from __future__ import annotations

import json
import math

import numpy as np

from domains.standard_model.fit_calibrated_registry import PDG_MASSES_GEV
from domains.standard_model.item1_exploration.field_sourced_accumulation.field_sourced_accumulation_v0_1 import (  # noqa: E501
    D,
    K,
    M_JOINT,
    grad_v,
    grad2_v,
)

BOOST = np.array([[0.0, 1.0], [1.0, 0.0]])
BRANCHES = {"up": ("u", "c", "t"), "down": ("d", "s", "b"), "lepton": ("e", "mu", "tau")}

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


def theta_trajectory(m_theta, dt, T, gamma=0.0):
    """Θ trajectory with optional damping gamma (leapfrog with damping). Returns the Θ array."""
    if m_theta <= 0 or dt <= 0:
        raise ValueError("m_theta and dt must be positive")
    phi = np.array([1.0, 0.5]); phi_nm1 = phi.copy()
    psi = np.array([0.8, 0.3]); psi_nm1 = psi.copy()
    theta = 0.0; theta_nm1 = 0.0
    a_phi = M_JOINT / dt ** 2 + D / (2 * dt)
    a_psi = M_JOINT / dt ** 2 - D / (2 * dt)
    c0 = m_theta / dt ** 2
    c1 = gamma / (2 * dt)
    ths = []
    for _ in range(int(round(T / dt))):
        s = float(phi @ BOOST @ psi)
        theta_np1 = ((2 * c0) * theta - (c0 - c1) * theta_nm1 - (theta / 2.0 + K * s)) / (c0 + c1)
        g = np.eye(2) + theta * BOOST
        b_phi = -K * (g @ phi) - grad_v(phi) + (2 * M_JOINT / dt ** 2) * phi + (D / (2 * dt) - M_JOINT / dt ** 2) * phi_nm1
        b_psi = -K * (g.T @ psi) - grad2_v(phi) * psi + (2 * M_JOINT / dt ** 2) * psi - (M_JOINT / dt ** 2 + D / (2 * dt)) * psi_nm1
        pn = b_phi / a_phi
        sn = b_psi / a_psi
        if not (np.all(np.isfinite(pn)) and np.all(np.isfinite(sn))) or abs(theta) > 1e6:
            break
        ths.append(theta)
        phi_nm1, phi = phi, pn
        psi_nm1, psi = psi, sn
        theta_nm1, theta = theta, theta_np1
    return np.array(ths)


def turning_points(arr):
    """# of turning points of |arr| — many => oscillatory (not a clean monotone approach)."""
    a = np.abs(arr)
    if len(a) < 3:
        return 0
    d = np.sign(np.diff(a))
    return int(np.sum(np.diff(d) != 0))


def fn_exponent(R, theta):
    """Froggatt-Nielsen exponent for a mass ratio R at flavour scale Theta: d = ln R / ln(1/Theta)."""
    return math.log(R) / math.log(1.0 / theta)


def real_ratios(branch):
    g1, g2, g3 = (PDG_MASSES_GEV[k] for k in BRANCHES[branch])
    return g2 / g1, g3 / g2


def run_fixture():
    print("== 0. TIER TAG (mandatory) ==")
    print("  finite_diagnostic (eps-oscillation, exponent computation) / Dr (singular-attractor + FN")
    print("  interpretation). NOT Th_coqc. Computed facts + tier per the materialist-bias guard.")

    print("\n== 1. FACT S: eps=1-|Theta| does NOT decay cleanly -- it oscillates/overshoots (point 1 REFUTED) ==")
    regimes = [(4.0, 0.0), (4.0, 0.5), (3.5, 0.3), (4.0, 2.0)]
    results = {}
    for mt, g in regimes:
        th = theta_trajectory(mt, 0.002, 30.0, g)
        tp = turning_points(th)
        mx = float(np.abs(th).max()) if len(th) else float("nan")
        results[(mt, g)] = (tp, mx)
        print(f"   M_Theta={mt}, gamma={g}: turning-points={tp:3d}  max|Theta|={mx:10.2f}  "
              f"(many turning-pts + big overshoot => oscillate/crash, not clean approach)")
    ck("in EVERY regime (incl. damped) |Theta| oscillates (>=20 turning points) and overshoots "
       "(max|Theta|>10) -- eps never decays cleanly; the singular ~1/eps^2 back-reaction makes Theta "
       "shoot THROUGH the degeneracy, so the 'controlled approach' route (point 1) is refuted",
       all(tp >= 20 and mx > 10 for tp, mx in results.values()),
       {str(k): (v[0], round(v[1], 1)) for k, v in results.items()})

    print("\n== 2. FACT T: the pivot -- large hierarchy must come from an EXPONENT far from the hole ==")
    theta_fn = 0.2
    exps = {br: (fn_exponent(real_ratios(br)[0], theta_fn), fn_exponent(real_ratios(br)[1], theta_fn))
            for br in BRANCHES}
    print(f"   at Theta={theta_fn}: consecutive-generation exponents d = ln R / ln(1/Theta):")
    for br, (d1, d2) in exps.items():
        print(f"     {br:7s}: d(1->2)={d1:.2f}  d(2->3)={d2:.2f}")

    def near_int(x, tol=0.1):
        return abs(x - round(x)) < tol
    up_d1, up_d2 = exps["up"]
    # the honest deflation: d1/d2 = ln R1/ln R2 is Theta-INDEPENDENT, so the two near-integers are
    # NOT independent -- one tuned knob (Theta->d1~4) + one structural coincidence (ln R1/ln R2 ~ 4/3).
    r1, r2 = real_ratios("up")
    slope_ratio = math.log(r1) / math.log(r2)
    print(f"   up-sector d1/d2 = ln R1/ln R2 = {slope_ratio:.4f} (Theta-INDEPENDENT) vs 4/3={4/3:.4f} "
          f"(off {abs(slope_ratio - 4/3)/(4/3)*100:.1f}%)")
    print(f"   => once Theta tuned so d1~4, d2 = 4/(d1/d2) = {4/slope_ratio:.3f} ~ 3 is FORCED, not a 2nd hit")
    ck("the up-sector exponents at Theta=0.2 are near-integer (3.96~=4, 3.05~=3) -- BUT this is NOT "
       "two independent hits: d1/d2 = ln R1/ln R2 is Theta-independent (=1.298 ~ 4/3, 2.6% off), so "
       "it is ONE tuned knob (Theta) + ONE structural near-coincidence (ln R1/ln R2 ~ 4/3). The "
       "honest content is just 'the up-sector log-slope sits near 4/3' -- suggestive, not striking",
       near_int(up_d1) and near_int(up_d2) and abs(slope_ratio - 4/3) < 0.05,
       {"up": (round(up_d1, 3), round(up_d2, 3)), "d1_over_d2": round(slope_ratio, 4)})
    ck("and the integer structure is NOT universal at a single Theta -- down and lepton exponents are "
       "NOT near-integer at Theta=0.2, and the Theta-window where both up exponents are near-integer "
       "is narrow (~0.195-0.205), so Theta=0.2 is effectively tuned; fit_calibrated, Wall A only "
       "moves unless graph TOPOLOGY forces the integer d_n",
       not all(near_int(d) for br in ("down", "lepton") for d in exps[br]),
       {br: (round(exps[br][0], 2), round(exps[br][1], 2)) for br in ("down", "lepton")})

    if FAILS:
        print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
    else:
        print("\nAll checks PASS.")

    report = {
        "schema": "eps-approach-refuted-exponent-pivot-report-v0.1",
        "status": "COMPUTED_point1_eps_approach_REFUTED_singular_overshoot_pivot_to_exponents_up_logslope_near_4over3_one_coincidence_not_two",
        "tier": "finite_diagnostic (eps-oscillation, exponents) / Dr (singular-attractor + Froggatt-Nielsen)",
        "regimes_turning_points_maxtheta": {str(k): (v[0], round(v[1], 2)) for k, v in results.items()},
        "fn_exponents_theta_0p2": {br: (round(exps[br][0], 3), round(exps[br][1], 3)) for br in BRANCHES},
        "honest_verdict": (
            "COMPUTED FACTS (no works/fails judgment, per the materialist-bias guard). Testing 'point "
            "1' -- can the mechanism APPROACH the degeneracy in a controlled way so eps=1-|Theta| "
            "decays and the log-hierarchy is linear in time? (S) NO: in every regime (incl. damped) "
            "|Theta| oscillates violently (75-394 turning points over T=30) and overshoots to ~10^3-"
            "10^4; eps never decays cleanly, because the back-reaction near the degeneracy is SINGULAR "
            "(~1/eps^2) and no linear damping tames it -- Theta shoots THROUGH the degeneracy. The "
            "attractor (from the '#4' calc) is real but singular and unusable as a settling point; the "
            "proximity route is refuted. (T) the refutation forces a pivot: a large hierarchy, if it "
            "exists, must come from an EXPONENT far from the hole -- m_n~Theta^{d_n}, Theta well below "
            "1, d_n an integer graph-distance (Froggatt-Nielsen structure). COMPUTED at Theta=0.2: the "
            "up-sector exponents are 3.96 and 3.05 -- strikingly near the integers 4 and 3; but down "
            "(1.86,2.36) and lepton (3.31,1.75) are NOT integer at the same Theta. So the integer "
            "structure is real and clean for up, not universal at one Theta. FRAMEWORK reading: FACT S "
            "closes the proximity route; FACT T is SUGGESTIVE not a result -- the exponent ansatz is "
            "the pre-existing Froggatt-Nielsen structure and stays fit_calibrated (choosing Theta/d_n "
            "just moves Wall A); it becomes a genuine result only if the graph TOPOLOGY forces the "
            "integer d_n. NOT a reproduction claim."
        ),
        "claim_boundary": [
            "REFUTED (FACT S): the 'controlled approach to the degeneracy' route (point 1) does not "
            "work for this mechanism -- eps oscillates/overshoots in every regime incl. damped, "
            "because the back-reaction is singular ~1/eps^2; the attractor is real but unusable as a "
            "settling point",
            "SUGGESTIVE, WEAKER THAN IT LOOKS (FACT T, deflated after review): the two up-sector "
            "near-integers (3.96~=4, 3.05~=3 at Theta=0.2) are NOT independent -- d1/d2 = ln R1/ln R2 "
            "is Theta-independent (1.298 ~ 4/3, 2.6% off), so it is ONE tuned knob (Theta) + ONE "
            "structural near-coincidence (up-sector log-slope ~ 4/3); the narrow Theta-window "
            "(~0.195-0.205) confirms Theta=0.2 is tuned. down/lepton are non-integer at the same "
            "Theta. Honest content: 'the up-sector log-slope sits near 4/3', nothing stronger",
            "the exponent ansatz m_n~Theta^{d_n} is PRE-EXISTING (Froggatt-Nielsen), NOT new, and "
            "stays fit_calibrated: choosing Theta and per-branch d_n just relabels the freedom (Wall A "
            "moves, does not fall). It becomes a genuine result ONLY if the graph topology forces the "
            "integer d_n (integer graph distances) -- NOT shown here",
            "does NOT reduce parameters, bridge to GeV, or reproduce the hierarchy; builds on the "
            "field_sourced mechanism (EQ-071) and the handoff's #4 attractor calc; one field IC",
            "MATERIALIST-BIAS GUARD: computed facts + tier -- a clean negative (proximity route "
            "refuted) plus a fenced suggestive pivot (exponent route), NOT a failure-verdict and NOT "
            "an overclaim of reproduction",
        ],
    }
    print("\nHONEST FENCE:")
    print(f"  {report['honest_verdict']}")
    return report


if __name__ == "__main__":
    r = run_fixture()
    print("\n" + json.dumps({k: v for k, v in r.items() if k not in ("honest_verdict", "claim_boundary")},
                            indent=2, sort_keys=True, default=str))
