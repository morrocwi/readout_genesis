#!/usr/bin/env python3
"""
RTM v1 -- rtm_validate.py: the 5 REQUIRED validation tests, tier finite_diagnostic throughout.

Every function below returns a dataclass carrying the RAW numbers (not just a pass/fail bool) --
per both position papers' explicit requirement that thresholds only ANNOTATE numbers already
reported, never replace them.

Test 4 (negative control) reconciliation note (System vs Design papers): the System position paper
correctly flags that the raw scalar M_hat = sum(a_n y_n)/sum(a_n a_n) is PERMUTATION-INVARIANT over
a fixed, correctly-time-ordered set of (a_n, y_n) pairs -- shuffling which INDEX a pair is labeled
with, while keeping each pair's own (a_n, y_n) values intact and evaluating on the SAME fixed set,
would trivially not degrade the scalar sum-fit at all, and would not demonstrate anything. Design's
spec is followed here in the way that actually tests temporal structure: the tape's VALUE SEQUENCE
itself (Phi, Psi arrays) is shuffled BEFORE recomputing the discrete central differences, so a_n and
y_n are recomputed from newly-adjacent (and now physically unrelated) neighbor values -- this is a
genuine test of whether the central-difference construction depends on real temporal adjacency, not
a vacuous relabeling. This reconciles the two papers: Design's exact numeric spec (shuffle, refit,
RMSE ratio >= 3.0) is implemented, using the mechanism the System paper flagged as necessary for the
test to mean anything.
"""
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from . import rtm_fit as fit


@dataclass
class ValidationResult:
    name: str
    value: dict            # raw numbers, always present
    threshold: str          # human-readable threshold description
    verdict: str            # e.g. "PASS", "FAIL", "PARTIAL", "REPORTED_AS_IS" -- never hidden
    tier: str = "finite_diagnostic"


def _rmse(y_true, y_pred):
    return float(np.sqrt(np.mean((y_pred - y_true) ** 2)))


def test1_fit_holdout(tape: dict, mode: str = "reader") -> ValidationResult:
    N = len(tape["Phi"])
    half = N // 2
    fit_train = fit.fit_M(tape, slice(0, half), mode=mode)
    y_true_train, y_pred_train, _ = fit.predict_y(tape, slice(0, half), fit_train.M_hat, mode=mode)
    rmse_train = _rmse(y_true_train, y_pred_train)
    norm_train = rmse_train / (np.std(y_true_train) + 1e-300)

    y_true_hold, y_pred_hold, _ = fit.predict_y(tape, slice(half, N), fit_train.M_hat, mode=mode)
    rmse_hold = _rmse(y_true_hold, y_pred_hold)
    norm_hold = rmse_hold / (np.std(y_true_hold) + 1e-300)

    train_sane = norm_train < 0.3
    return ValidationResult(
        name="1_fit_holdout",
        value={
            "M_hat_train": fit_train.M_hat, "n_train": fit_train.n_used,
            "RMSE_train": rmse_train, "RMSE_train_normalized": norm_train,
            "RMSE_holdout": rmse_hold, "RMSE_holdout_normalized": norm_hold,
        },
        threshold="training-half normalized residual < 0.3 (sanity only); holdout number reported "
                   "as-is with no pass/fail gate -- a bad transport result IS the finding",
        verdict="TRAIN_SANE" if train_sane else "TRAIN_INSANE (fit itself did not even converge on "
                "its own training half -- treat all downstream numbers as suspect)",
    )


def test2_dual_agreement(tape: dict) -> ValidationResult:
    r = fit.fit_M(tape, slice(None), mode="reader")
    p = fit.fit_M(tape, slice(None), mode="record")
    if r.underdetermined or p.underdetermined:
        return ValidationResult(
            name="2_dual_agreement",
            value={"M_hat_phi": r.M_hat, "M_hat_psi": p.M_hat, "agreement_ratio": float("nan")},
            threshold="ratio<0.05 agree / 0.05-0.20 partial / >0.20 disagree",
            verdict="UNDERDETERMINED (one or both fits could not be computed -- see rank_AAt/sum_aa)",
        )
    denom = (abs(r.M_hat) + abs(p.M_hat)) / 2.0
    ratio = abs(r.M_hat - p.M_hat) / denom if denom > 0 else float("inf")
    if ratio < 0.05:
        verdict = "AGREE"
    elif ratio < 0.20:
        verdict = "PARTIAL_AGREEMENT (report both, do not average)"
    else:
        verdict = "DISAGREE (report as-is, do not select the more convenient one)"
    return ValidationResult(
        name="2_dual_agreement",
        value={"M_hat_phi": r.M_hat, "M_hat_psi": p.M_hat, "agreement_ratio": ratio},
        threshold="ratio<0.05 agree / 0.05-0.20 partial / >0.20 disagree",
        verdict=verdict,
    )


def test3_path_additivity(tape: dict, M_hat: float, path=None) -> ValidationResult:
    dt = tape["meta"]["dt"]
    phi, psi = tape["Phi"], tape["Psi"]
    N = len(phi)
    if path is None:
        path = list(range(N - 1))

    d_phi = phi[np.array(path) + 1] - phi[np.array(path)]
    d_psi = psi[np.array(path) + 1] - psi[np.array(path)]
    c_n_vectorized = (1.0 / dt) * d_phi * M_hat * d_psi
    summed = float(np.sum(c_n_vectorized))

    # "direct": an INDEPENDENT code path (explicit Python accumulation loop, not numpy.sum) computing
    # the same quantity -- a genuine reassociation-of-floating-point-sum check, not a different
    # physical quantity (a total-delta-times-total-delta bilinear would NOT equal this sum in
    # general, since the bilinear form does not telescope that way -- using that instead would be
    # testing a false mathematical identity, not this file's actual additivity claim).
    direct = 0.0
    for n in path:
        direct += (1.0 / dt) * (phi[n + 1] - phi[n]) * M_hat * (psi[n + 1] - psi[n])

    rel_diff = abs(summed - direct) / (abs(direct) + 1e-300)
    is_bug = rel_diff > 1e-6
    return ValidationResult(
        name="3_path_additivity",
        value={"Delta_j_eff_summed": summed, "Delta_j_eff_direct": direct, "relative_diff": rel_diff},
        threshold="relative_diff < 1e-6 (near machine precision expected -- same sum reassociated; "
                   "if exceeded, that is a BUG, not a physics finding)",
        verdict="BUG_SUSPECTED (relative_diff exceeds float-reassociation tolerance)" if is_bug else "ADDITIVE",
    )


def _shuffle_tape(tape: dict, seed: int) -> dict:
    """Shuffles the VALUE SEQUENCE (Phi, Psi, ...) so recomputed central differences use newly
    (and physically unrelated) adjacent neighbors -- see module docstring reconciliation note."""
    N = len(tape["Phi"])
    rng = np.random.default_rng(seed)
    perm = rng.permutation(N)
    shuffled = dict(tape)
    for key in ("Phi", "Psi", "J", "R_Phi", "R_Psi", "t"):
        shuffled[key] = tape[key][perm]
    shuffled["meta"] = dict(tape["meta"])
    shuffled["meta"]["shuffled"] = True
    shuffled["meta"]["shuffle_seed"] = seed
    return shuffled


def test4_negative_control_shuffle(tape: dict, holdout_result: ValidationResult, mode: str = "reader",
                                    seed: int = 20260725) -> ValidationResult:
    shuffled = _shuffle_tape(tape, seed)
    N = len(shuffled["Phi"])
    half = N // 2
    fit_shuf = fit.fit_M(shuffled, slice(0, half), mode=mode)
    y_true_s, y_pred_s, _ = fit.predict_y(shuffled, slice(half, N), fit_shuf.M_hat, mode=mode)
    rmse_shuffled = _rmse(y_true_s, y_pred_s)

    rmse_holdout = holdout_result.value["RMSE_holdout"]
    ratio = rmse_shuffled / (rmse_holdout + 1e-300)
    degrades = ratio >= 3.0

    verdict = "NEGATIVE_CONTROL_PASSED (degradation >= 3x, fit uses genuine temporal structure)" if degrades else (
        "NEGATIVE_CONTROL_FAILED -- fit does NOT measurably depend on genuine temporal order; "
        "do not claim c_n reflects transition structure from this test alone; tier for that "
        "specific claim is downgraded to Dr-narrative pending further evidence"
    )
    return ValidationResult(
        name="4_negative_control_shuffle",
        value={
            "M_hat_shuffled": fit_shuf.M_hat, "RMSE_shuffled": rmse_shuffled,
            "RMSE_holdout": rmse_holdout, "degradation_ratio": ratio, "seed": seed,
        },
        threshold="RMSE_shuffled / RMSE_holdout >= 3.0 required to call temporal structure 'used'",
        verdict=verdict,
    )


def test5_transport(tape: dict, mode: str = "reader") -> ValidationResult:
    N = len(tape["Phi"])
    third = N // 3
    seg_A = slice(0, third)
    seg_B = slice(third, 2 * third)

    fit_A = fit.fit_M(tape, seg_A, mode=mode)
    if fit_A.underdetermined:
        return ValidationResult(
            name="5_transport",
            value={"underdetermined_on_segment_A": True, "sum_aa_A": fit_A.sum_aa},
            threshold="RMSE_transport / std(y_true on B) < 0.5 transports; >=0.5 does NOT transport",
            verdict="UNDERDETERMINED (segment A itself could not be fit -- see sum_aa)",
        )
    y_true_B, y_pred_B, _ = fit.predict_y(tape, seg_B, fit_A.M_hat, mode=mode)
    rmse_transport = _rmse(y_true_B, y_pred_B)
    norm_transport = rmse_transport / (np.std(y_true_B) + 1e-300)
    transports = norm_transport < 0.5
    return ValidationResult(
        name="5_transport",
        value={
            "M_hat_segment_A": fit_A.M_hat, "RMSE_transport": rmse_transport,
            "RMSE_transport_normalized": norm_transport,
        },
        threshold="RMSE_transport / std(y_true on B) < 0.5 transports; >=0.5 does NOT transport",
        verdict="TRANSPORTS" if transports else "DOES_NOT_TRANSPORT (reported honestly, not averaged away)",
    )


def run_validation_suite(tape: dict, mode: str = "reader") -> dict:
    t1 = test1_fit_holdout(tape, mode=mode)
    t2 = test2_dual_agreement(tape)
    full_fit = fit.fit_M(tape, slice(None), mode=mode)
    t3 = test3_path_additivity(tape, full_fit.M_hat)
    t4 = test4_negative_control_shuffle(tape, t1, mode=mode)
    t5 = test5_transport(tape, mode=mode)
    return {r.name: r for r in (t1, t2, t3, t4, t5)}
