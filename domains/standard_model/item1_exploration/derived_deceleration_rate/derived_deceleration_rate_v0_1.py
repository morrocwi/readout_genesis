"""Derive the deceleration rate q from the graph mechanism -- do NOT fit it. v0.1.

The decelerating-profile candidate (decelerating_accumulation_profile/) computed FACT E: a
per-branch decelerating rate q reproduces the shapes, but q was an INDEPENDENT hand-set constant
(no single law q=f(r); down accelerates while up/lepton decelerate, flipping the trend vs r). This
file takes the qualitatively different step the arc had never taken: instead of FITTING q, it asks
whether the mother equation's own geometry-source mechanism DERIVES q -- i.e. whether q comes out
as a readout of a graph constant already in the model, rather than a new free parameter.

THE MECHANISM (reused verbatim from field_sourced_accumulation, EQ-071 -- no new physics). Theta
accumulates by the mother equation's geometry-source law with a confining potential:
    Theta_{n+1} = 2*Theta_n - Theta_{n-1} - dt^2 * (1/M_Theta) * (gradU_Theta(Theta_n) + K*S_Theta)
    S_Theta = Phi_n^T G_a Psi_n     (the affine geometry source; Phi/Psi evolve M-calibrated)
The graph operator is G[Theta_n] = I + Theta_n * G_a. We read the condition number (the mass-RATIO
analog, stance_for('mass')) of the accumulated product at three equally-spaced milestones n1<n2<n3
(the three 'generations'), form R1=C(n2)/C(n1), R2=C(n3)/C(n2), and take q = R2/R1 -- computed
ENTIRELY from the mechanism (M_JOINT, M_Theta, K, the generator, the field ICs). q is never tuned
to any real value.

*** COMPUTED FACTS (materialist-bias guard, ZERO_INFINITY_DUAL_DIAGNOSIS.md Part 4b -- no
    works/fails value-words; a derived-in-principle result with an honest quantitative limit):

    FACT F: with a NON-COMPACT (boost) generator the mechanism produces a non-trivial q (log q != 0)
    that varies with M_Theta -- so q is not a value set by hand, it is read out of the accumulation.
    A compact ROTATION generator (control) gives q = 1 exactly (log q = 0), but note this is a
    GENERIC LINEAR-ALGEBRA IDENTITY, not a dynamical result: g = I + Theta*ROTATION with the
    skew generator [[0,-1],[1,0]] is always a scalar multiple of an orthogonal matrix, so its
    condition number is identically 1 for ANY Theta trajectory, ANY M_Theta, ANY IC. The control
    therefore proves only the necessary structural point -- a compact generator CANNOT produce ANY
    ratio spread, so whatever spread appears MUST come from the non-compact character -- it does NOT
    show the mechanism "generates isotropy." The dynamical content of FACT F is only the boost side:
    non-compact accumulation yields an M_Theta-dependent q.

    FACT G: with the non-compact generator the mechanism produces BOTH signs -- small M_Theta gives
    log q > 0 (accelerate, down-like), large M_Theta gives log q < 0 (decelerate, up/lepton-like).
    So the accel/decel sign-flip FACT E showed no law q=f(r) could give is PRODUCIBLE here from
    M_Theta rather than from the mass ratio r. HONESTY BOUND: (i) the real targets (down +0.35, up
    -0.64, lepton -1.09) lie inside the produced range, but that range spans ~8 log-decades sampled
    at only two M_Theta points, so "inside the range" is a WEAK necessary check (almost any
    non-degenerate output would pass it), NOT evidence the values are hit; (ii) tested at only ONE
    field IC -- the sibling field_sourced_accumulation found the condition-number output moves ~1e8x
    under IC changes, so the sign-flip's IC-robustness is UNTESTED here.

    FACT H (the honest limit -- this substantially bounds FACT F/G): the map q = f(M_Theta) is NOT a
    clean or even locally-monotone law. The measured sweep sign-flips THREE times in the narrow
    window M_Theta = 5->7->9->11 (+1.99, -6.19, +1.17, -1.77), and the settled decel branch (11-100)
    is itself non-monotone (min ~ -3.6 near M_Theta ~ 18, rising back to ~ -1.1 by 100). The cause is
    TRAJECTORY INSTABILITY: the coupled Phi/Psi/Theta system blows up at different (chaotic-in-
    M_Theta) step counts, and the milestones are fractions of the trajectory-length-until-blowup, so
    what the milestone-q actually reads is closer to "the numerical blowup TIMING, which correlates
    only loosely with M_Theta" than "a clean function of M_Theta." Consequence: this does NOT
    establish "q is a clean readout of M_Theta"; it establishes only that a non-compact accumulation
    with a confining source can PRODUCE EITHER SIGN of q, with the outcome depending on M_Theta
    through an unstable, non-invertible map. It does not pin per-branch M_Theta and does not replace
    fitting.

    FRAMEWORK-NATIVE reading (stance_for('mass')): q, M_Theta, and the ratios are all graph
    readouts. The honest net step beyond FACT E (where q was an independent hand-set constant) is
    modest but real: q's sign is PRODUCIBLE by the mechanism from an existing graph constant rather
    than imposed. What remains OPEN -- and what FACT H shows is the actual blocker -- is stabilizing
    the coupled Phi/Psi/Theta system so that q = f(M_Theta) becomes a clean, IC-robust, invertible
    law; only then could q be said to be derived (not merely sign-produced). NOT a failure, NOT a
    claim the hierarchy is reproduced, and NOT yet a clean derivation. This file reports exactly:
    the sign is producible from M_Theta (FACT F/G), bounded by a pervasive instability that makes the
    quantitative map non-invertible (FACT H). ***

Tier: finite_diagnostic (the measured q-signs, the rotation control, the both-signs sweep). Dr
(item-1 interpretation of q as a readout of M_Theta). NOT Th_coqc, NOT a reproduction claim.
"""
from __future__ import annotations

import json
import math

import numpy as np

from domains.standard_model.item1_exploration.field_sourced_accumulation.field_sourced_accumulation_v0_1 import (  # noqa: E501
    D,
    DT,
    K,
    M_JOINT,
    grad_u_theta,
    grad_v,
    grad2_v,
)

BOOST = np.array([[0.0, 1.0], [1.0, 0.0]])       # non-compact generator (so(1,1))
ROTATION = np.array([[0.0, -1.0], [1.0, 0.0]])   # compact generator (so(2)) -- control
DEFAULT_IC = ([1.0, 0.5], [0.8, 0.3])

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


def derived_log_q(phi0, psi0, generator, m_theta, n_steps=600):
    """Evolve the coupled Phi/Psi/Theta mechanism and read log10(q)=log10(R2/R1) from the condition
    number at three equally-spaced milestones. Returns None if the trajectory yields too few finite
    steps. q is computed from the mechanism ONLY -- never tuned to a target."""
    if m_theta <= 0:
        raise ValueError("m_theta must be positive")
    phi = np.array(phi0, float); phi_nm1 = phi.copy()
    psi = np.array(psi0, float); psi_nm1 = psi.copy()
    theta = 0.0; theta_nm1 = 0.0
    prod = np.eye(2)
    a_phi = M_JOINT / DT ** 2 + D / (2 * DT)
    a_psi = M_JOINT / DT ** 2 - D / (2 * DT)
    logc = []
    for _ in range(n_steps):
        s_theta = float(phi @ generator @ psi)
        theta_np1 = 2 * theta - theta_nm1 - DT * DT * (1.0 / m_theta) * (grad_u_theta(theta) + K * s_theta)
        g = np.eye(2) + theta * generator
        prod = g @ prod
        nrm = np.linalg.norm(prod)
        if nrm > 1e150 or not np.isfinite(nrm):
            break
        sv = np.linalg.svd(prod, compute_uv=False)
        if sv[-1] <= 0:
            break
        logc.append(math.log10(sv[0] / sv[-1]))
        b_phi = -K * (g @ phi) - grad_v(phi) + (2 * M_JOINT / DT ** 2) * phi + (D / (2 * DT) - M_JOINT / DT ** 2) * phi_nm1
        b_psi = -K * (g.T @ psi) - grad2_v(phi) * psi + (2 * M_JOINT / DT ** 2) * psi - (M_JOINT / DT ** 2 + D / (2 * DT)) * psi_nm1
        phi_nm1, phi = phi, b_phi / a_phi
        psi_nm1, psi = psi, b_psi / a_psi
        theta_nm1, theta = theta, theta_np1
    lc = np.array(logc)
    if len(lc) < 9:
        return None
    L = len(lc)
    i1, i2, i3 = L // 3, 2 * L // 3, L - 1
    return (lc[i3] - lc[i2]) - (lc[i2] - lc[i1])      # log q = log R2 - log R1


def run_fixture():
    print("== 0. TIER TAG (mandatory) ==")
    print("  finite_diagnostic (measured q-signs, rotation control, both-signs sweep) / Dr (q as a")
    print("  readout of M_Theta). NOT Th_coqc, NOT a reproduction claim. Reported as computed facts +")
    print("  tier per the materialist-bias guard -- q derived from an existing constant is not a")
    print("  'win'; the instability limit is not a 'failure'.")

    phi0, psi0 = DEFAULT_IC

    print("\n== 1. FACT F: boost yields an M_Theta-dependent q; rotation q=1 is a generic algebra identity ==")
    lq_rot = derived_log_q(phi0, psi0, ROTATION, 2.0)
    lq_boost = derived_log_q(phi0, psi0, BOOST, 2.0)
    print(f"   compact ROTATION generator (control): log q = {lq_rot:.4f}  (q = {10**lq_rot:.4g})")
    print(f"   non-compact BOOST generator         : log q = {lq_boost:.4f}  (q = {10**lq_boost:.4g})")
    ck("compact rotation control gives q=1 exactly (log q=0) -- but this is a GENERIC LINEAR-ALGEBRA "
       "identity (I+Theta*skew is always scalar*orthogonal, cond#=1 for ANY dynamics), NOT a "
       "mechanism result; it proves only that a compact generator cannot produce ANY spread, so any "
       "spread must come from the non-compact character",
       abs(lq_rot) < 1e-9, lq_rot)
    ck("non-compact boost yields a non-trivial q (log q != 0) -- the dynamical content of FACT F: "
       "q is read out of the non-compact accumulation, not set by hand",
       abs(lq_boost) > 0.5, lq_boost)

    print("\n== 2. FACT G: the mechanism produces BOTH signs from M_Theta -- the sign-flip FACT E needed ==")
    lq_small = derived_log_q(phi0, psi0, BOOST, 2.0)      # small M_Theta -> accelerate
    lq_large = derived_log_q(phi0, psi0, BOOST, 15.0)     # large M_Theta -> decelerate
    print(f"   M_Theta=2.0  (small): log q = {lq_small:.4f}  ({'ACCEL' if lq_small > 0 else 'DECEL'})")
    print(f"   M_Theta=15.0 (large): log q = {lq_large:.4f}  ({'ACCEL' if lq_large > 0 else 'DECEL'})")
    print("   real targets lie inside the produced range (WEAK check -- see below): down +0.35, up -0.64, lepton -1.09")
    ck("small M_Theta ACCELERATES (log q>0, down-like) while large M_Theta DECELERATES (log q<0, "
       "up/lepton-like) -- the accel/decel sign-flip is PRODUCIBLE from M_Theta (an existing graph "
       "constant), NOT from the branch mass ratio r (FACT E showed no q=f(r) gives this)",
       lq_small > 0 and lq_large < 0, (lq_small, lq_large))
    ck("the real targets lie inside the produced range -- but this is a WEAK necessary check only: "
       "the range spans ~8 log-decades sampled at 2 points, so almost any non-degenerate output "
       "would pass; it is NOT evidence the values are hit, and IC-robustness is untested (one IC)",
       lq_large < -1.09 < 0.35 < lq_small, (lq_large, lq_small))

    print("\n== 3. FACT H (bounds F/G): q=f(M_Theta) is instability-dominated -- reads blowup timing, not a clean law ==")
    sweep = {mt: derived_log_q(phi0, psi0, BOOST, mt) for mt in (5.0, 7.0, 9.0, 11.0, 15.0, 18.0, 30.0, 100.0)}
    for mt, lq in sweep.items():
        print(f"   M_Theta={mt:6.1f}: log q = {'None' if lq is None else f'{lq:+.3f}'}"
              f"  {'' if lq is None else ('ACCEL' if lq > 0 else 'DECEL')}")
    vals = [v for v in sweep.values() if v is not None]
    monotone = all(vals[i] >= vals[i + 1] - 1e-9 for i in range(len(vals) - 1))
    # count sign flips in the low window 5->7->9->11 to show instability is pervasive, not localized
    low = [sweep[mt] for mt in (5.0, 7.0, 9.0, 11.0) if sweep[mt] is not None]
    sign_flips = sum(1 for i in range(len(low) - 1) if low[i] * low[i + 1] < 0)
    print(f"   sign flips in the window M_Theta=5->7->9->11: {sign_flips} (pervasive, not one isolated region)")
    print("   milestones are fractions of trajectory-length-until-blowup, and blowup timing is chaotic")
    print("   in M_Theta -- so milestone-q reads the numerical BLOWUP TIMING (loosely correlated with")
    print("   M_Theta), NOT a clean function of M_Theta. This bounds FACT F/G: sign is producible, but")
    print("   the quantitative map is non-invertible.")
    ck("q=f(M_Theta) is neither monotone nor clean -- it sign-flips 3x in the narrow window 5->7->9->11 "
       "(pervasive instability, not one isolated region) and the decel branch is itself non-monotone; "
       "milestone-q reads numerical blowup timing (loosely correlated with M_Theta), so the map is "
       "non-invertible and does NOT pin per-branch M_Theta -- sign is producible, derivation is not clean",
       (not monotone) and sign_flips >= 3, {"monotone": monotone, "sign_flips_5to11": sign_flips})

    if FAILS:
        print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
    else:
        print("\nAll checks PASS.")

    report = {
        "schema": "derived-deceleration-rate-report-v0.1",
        "status": "COMPUTED_q_sign_is_producible_from_M_Theta_but_map_is_instability_dominated_non_invertible",
        "tier": "finite_diagnostic (q-signs, sweep, blowup-timing dependence) / Dr (item-1 interpretation)",
        "log_q_rotation_control": lq_rot,
        "log_q_boost_small_m_theta": lq_small,
        "log_q_boost_large_m_theta": lq_large,
        "real_targets_log_q": {"down": 0.350, "up": -0.636, "lepton": -1.090},
        "honest_verdict": (
            "COMPUTED FACTS (no works/fails judgment, per the materialist-bias guard). This is the "
            "arc's first attempt to DERIVE the deceleration rate q from the graph mechanism rather "
            "than FIT it -- and the honest outcome is a MODEST real step bounded by a hard limit. "
            "(F) With a non-compact (boost) generator the mechanism yields an M_Theta-dependent q "
            "(not a hand-set value). The compact rotation control gives q=1 exactly, but that is a "
            "GENERIC linear-algebra identity (I+Theta*skew is always scalar*orthogonal), NOT a "
            "mechanism result -- it proves only that any spread MUST come from the non-compact "
            "character. (G) The non-compact mechanism PRODUCES BOTH signs: small M_Theta accelerates "
            "(down-like), large decelerates (up/lepton-like) -- the sign-flip FACT E showed no "
            "q=f(r) could give, here producible from M_Theta. But 'real targets lie inside the "
            "produced range' is a WEAK check (8 log-decades, 2 sample points) and IC-robustness is "
            "untested (one IC; sibling found ~1e8x IC sensitivity). (H, and this BOUNDS F/G) the map "
            "q=f(M_Theta) is NOT clean: it sign-flips 3x in the narrow window M_Theta=5->7->9->11 "
            "and the decel branch is non-monotone; because milestones are fractions of the "
            "trajectory-length-until-blowup and blowup timing is chaotic in M_Theta, the milestone-q "
            "reads the numerical BLOWUP TIMING (loosely correlated with M_Theta), not a clean "
            "function of it. So this does NOT establish 'q is a clean readout of M_Theta'; it "
            "establishes only that a non-compact accumulation with a confining source can PRODUCE "
            "EITHER SIGN of q via a non-invertible, unstable map. FRAMEWORK reading "
            "(stance_for('mass')): the honest net step beyond FACT E is that q's SIGN is producible "
            "from an existing graph constant rather than imposed -- modest but real. OPEN, and shown "
            "by FACT H to be the actual blocker: stabilize the coupled Phi/Psi/Theta system so "
            "q=f(M_Theta) becomes a clean, IC-robust, invertible law; only then is q derived (not "
            "merely sign-produced). NOT a failure, NOT a reproduction claim, NOT a clean derivation."
        ),
        "claim_boundary": [
            "the honest net step: q's SIGN is PRODUCIBLE by the mechanism from M_Theta (an existing "
            "graph constant) rather than hand-set as in FACT E -- q is read from the mechanism, never "
            "tuned to a real value (test_derived_q_is_not_tuned_to_target guards this). This is "
            "modest: sign-producible, NOT quantitatively derived",
            "the rotation-control q=1 is a GENERIC algebra identity (skew generator -> scalar* "
            "orthogonal -> cond#=1 for any dynamics), NOT evidence the mechanism generates isotropy; "
            "its only content is that a compact generator cannot produce ANY spread",
            "HARD LIMIT (FACT H, bounds F/G): the map q=f(M_Theta) sign-flips 3x in M_Theta=5-11 and "
            "is non-monotone; milestone-q reads numerical BLOWUP TIMING (loosely correlated with "
            "M_Theta), so the map is non-invertible -- it does NOT pin per-branch M_Theta and does "
            "NOT replace fitting. The blocker is stabilizing the coupled system, which is OPEN",
            "UNTESTED: only one field IC is used; the sibling field_sourced_accumulation found ~1e8x "
            "IC sensitivity, so the IC-robustness of the sign-flip (FACT G) is unverified. 'real "
            "targets inside produced range' is a weak necessary check (8 decades, 2 points), not "
            "evidence the values are hit",
            "does NOT reduce the free-parameter count; does NOT bridge to GeV (ratios only, EQ-068 "
            "open); n<->generation remains Attempt 13's conjecture. Builds on "
            "decelerating_accumulation_profile (FACT E) and reuses field_sourced_accumulation "
            "(EQ-071) verbatim -- no new physics",
            "MATERIALIST-BIAS GUARD (this file follows it): q, M_Theta, ratios are graph readouts "
            "(stance_for('mass')); the instability limit is an internal calibratable question "
            "(stabilize the system), NOT a failure and NOT a reproduction claim -- but ALSO not "
            "oversold: the step is only sign-producibility, explicitly not clean derivation",
        ],
    }
    print("\nHONEST FENCE:")
    print(f"  {report['honest_verdict']}")
    return report


if __name__ == "__main__":
    r = run_fixture()
    print("\n" + json.dumps({k: v for k, v in r.items() if k not in ("honest_verdict", "claim_boundary")},
                            indent=2, sort_keys=True, default=str))
