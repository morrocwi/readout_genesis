#!/usr/bin/env python3
"""
RTM v3 (synthesis) -- rtm_validate.py: validation suite combining BOTH candidate PRs' negative
controls (they test genuinely different failure modes, neither supersedes the other) plus v0.1/
PR#67's fail-closed gate discipline plus v1/PR#26's "report holdout as-is, no forced verdict"
honesty for the one check (holdout) that has no principled fixed threshold.

- Negative control A (v1/PR#26's design): shuffle the tape's VALUE SEQUENCE within each path before
  recomputing central differences, so a_n/y_n are rebuilt from newly-adjacent, physically unrelated
  neighbors. Targets: does the fit depend on genuine TEMPORAL/DYNAMICAL structure at all?
- Negative control B (v0.1/PR#67's design): keep the acceleration (a_n) side fixed to its real
  event, but pair it with the LOAD (y_n) from a rotated, mismatched donor. Targets: does the fit
  depend on correct EVENT-TO-LOAD ALIGNMENT (the realistic failure mode for a real lab/QuTiP
  dataset with a labeling bug)?
  Required degradation for both: >= 3.0x the holdout RMSE (v0.1/PR#67's own threshold, kept).
- Dual agreement: v0.1/PR#67's <=5% "agree" bar, with v1/PR#26's finer PARTIAL (5-20%) / DISAGREE
  (>20%) banding on top, both raw numbers always reported, never averaged into one at either end.
- Path additivity (v1/PR#26 only, v0.1/PR#67 has no equivalent): near-machine-precision requirement
  (<1e-6 relative) -- a violation here is a BUG in the chain code, not a physics finding, and is
  reported as such.
- Lambda-range gate: v0.1/PR#67's "abs-lambda must lie in (0,1]" is gated; the SIGNED lambda is
  reported but NOT gated, since v3 does not silently discard the signed convention v0.1 chose to
  drop -- both conventions' honest consequences stay visible.
"""
from dataclasses import dataclass
from typing import Dict

import numpy as np

from . import rtm_fit
from . import rtm_chain

NEGATIVE_CONTROL_MARGIN = 3.0
DUAL_AGREEMENT_GOOD = 0.05
DUAL_AGREEMENT_PARTIAL = 0.20
ADDITIVITY_MAX_REL = 1e-6


@dataclass
class ValidationReport:
    holdout_normalized_residual: float                 # reported, NOT gated (no principled threshold)
    dual_agreement_ratio: float
    dual_agreement_label: str                           # AGREE / PARTIAL_AGREEMENT / DISAGREE
    negative_control_a_ratio: float                     # shuffle-value degradation ratio
    negative_control_b_ratio: float                     # rotate-donor degradation ratio
    additivity_relative_diff: float
    lambda_abs_in_range: bool
    gates: Dict[str, bool]
    decision: str                                       # PASS / FAIL, from `gates` only
    tier: str = "finite_diagnostic"


def _holdout_split(paths, frac=0.5):
    train, hold = [], []
    for p in paths:
        n = len(p["Phi"])
        cut = int(n * frac)
        train.append({**p, "Phi": p["Phi"][:cut], "Psi": p["Psi"][:cut],
                      "J": p["J"][:cut], "R_Phi": p["R_Phi"][:cut], "R_Psi": p["R_Psi"][:cut]})
        hold.append({**p, "Phi": p["Phi"][cut:], "Psi": p["Psi"][cut:],
                      "J": p["J"][cut:], "R_Phi": p["R_Phi"][cut:], "R_Psi": p["R_Psi"][cut:]})
    return train, hold


def _rmse_on(tape, paths, M_hat, mode="joint"):
    a_all, y_all = [], []
    dt = tape["meta"]["dt"]
    D, K = tape["meta"]["D"], tape["meta"]["K"]
    for p in paths:
        if mode in ("reader", "joint"):
            a, y = rtm_fit._path_reader_ay(p, dt, D, K)
            a_all.append(a); y_all.append(y)
        if mode in ("record", "joint"):
            a, y = rtm_fit._path_record_ay(p, dt, D, K)
            a_all.append(a); y_all.append(y)
    a = np.concatenate(a_all); y = np.concatenate(y_all)
    resid = a * M_hat - y
    scale = np.std(y) if np.std(y) > 1e-300 else 1.0
    return float(np.sqrt(np.mean(resid**2)) / scale)


def _shuffle_value_paths(paths, seed):
    """Negative control A: shuffle each path's VALUE sequence (both Phi and Psi, same permutation
    per path) before any differencing happens -- rebuilds a_n/y_n from unrelated neighbors."""
    rng = np.random.default_rng(seed)
    out = []
    for p in paths:
        perm = rng.permutation(len(p["Phi"]))
        out.append({**p, "Phi": p["Phi"][perm], "Psi": p["Psi"][perm],
                     "J": p["J"][perm], "R_Phi": p["R_Phi"][perm], "R_Psi": p["R_Psi"][perm]})
    return out


def _rotate_donor_rmse(tape, paths, mode="joint"):
    """Negative control B: fit M using a_n from real events, but y_n taken from a ROTATED donor
    (offset by one path in the list) -- tests event/load alignment specifically, distinct from
    control A's temporal-structure test."""
    dt = tape["meta"]["dt"]
    D, K = tape["meta"]["D"], tape["meta"]["K"]
    donors = paths[1:] + paths[:1]
    a_all, y_all = [], []
    for p, donor in zip(paths, donors):
        if mode in ("reader", "joint"):
            a_p, _ = rtm_fit._path_reader_ay(p, dt, D, K)
            _, y_d = rtm_fit._path_reader_ay(donor, dt, D, K)
            n = min(len(a_p), len(y_d))
            a_all.append(a_p[:n]); y_all.append(y_d[:n])
        if mode in ("record", "joint"):
            a_p, _ = rtm_fit._path_record_ay(p, dt, D, K)
            _, y_d = rtm_fit._path_record_ay(donor, dt, D, K)
            n = min(len(a_p), len(y_d))
            a_all.append(a_p[:n]); y_all.append(y_d[:n])
    a = np.concatenate(a_all); y = np.concatenate(y_all)
    sum_aa = float(np.sum(a * a))
    if sum_aa <= 1e-300:
        raise ValueError("negative-control-B acceleration rank is zero")
    m_rot = float(np.sum(a * y) / sum_aa)
    resid = a * m_rot - y
    scale = np.std(y) if np.std(y) > 1e-300 else 1.0
    return float(np.sqrt(np.mean(resid**2)) / scale)


def run_validation_suite(tape: dict, paths, M_hat_joint: float, chain_result) -> ValidationReport:
    train_paths, hold_paths = _holdout_split(paths)
    fit_train = rtm_fit.fit_M(tape, train_paths, mode="joint")
    holdout_resid = _rmse_on(tape, hold_paths, fit_train.M_hat, mode="joint")

    fit_reader = rtm_fit.fit_M(tape, paths, mode="reader")
    fit_record = rtm_fit.fit_M(tape, paths, mode="record")
    agreement = abs(fit_reader.M_hat - fit_record.M_hat) / max(abs(M_hat_joint), 1e-300)
    if agreement < DUAL_AGREEMENT_GOOD:
        agreement_label = "AGREE"
    elif agreement < DUAL_AGREEMENT_PARTIAL:
        agreement_label = "PARTIAL_AGREEMENT"
    else:
        agreement_label = "DISAGREE"

    shuffled_train = _shuffle_value_paths(train_paths, seed=20260725)
    fit_shuffled = rtm_fit.fit_M(tape, shuffled_train, mode="joint")
    shuffled_resid = _rmse_on(tape, hold_paths, fit_shuffled.M_hat, mode="joint")
    neg_a_ratio = shuffled_resid / max(holdout_resid, 1e-300)

    rotated_resid = _rotate_donor_rmse(tape, train_paths, mode="joint")
    neg_b_ratio = rotated_resid / max(holdout_resid, 1e-300)

    lambda_abs_in_range = all(0 < v <= 1 for v in chain_result.branch_lambda_abs.values())

    gates = {
        "M_joint_positive_and_determined": (not fit_train.underdetermined) and M_hat_joint > 0,
        "dual_agreement_le_20pct": agreement < DUAL_AGREEMENT_PARTIAL,
        "additivity_near_machine_precision": chain_result.additivity_relative_diff < ADDITIVITY_MAX_REL,
        "negative_control_a_worse": neg_a_ratio >= NEGATIVE_CONTROL_MARGIN,
        "negative_control_b_worse": neg_b_ratio >= NEGATIVE_CONTROL_MARGIN,
        "lambda_abs_in_0_1": lambda_abs_in_range,
    }
    decision = "PASS" if all(gates.values()) else "FAIL"

    return ValidationReport(
        holdout_normalized_residual=holdout_resid,
        dual_agreement_ratio=agreement,
        dual_agreement_label=agreement_label,
        negative_control_a_ratio=neg_a_ratio,
        negative_control_b_ratio=neg_b_ratio,
        additivity_relative_diff=chain_result.additivity_relative_diff,
        lambda_abs_in_range=lambda_abs_in_range,
        gates=gates,
        decision=decision,
    )
