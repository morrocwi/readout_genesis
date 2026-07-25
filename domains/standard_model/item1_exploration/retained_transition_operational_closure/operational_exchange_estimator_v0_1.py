#!/usr/bin/env python3
"""Noise-aware operational estimator for the scalar Reader/Record exchange coefficient M.

Tier: calibrated_readout / finite_diagnostic.
This module does not derive M from the unrestricted root. It estimates an effective coefficient
under explicit observation-noise assumptions and fails closed when corrected information is weak.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Mapping, Optional, Sequence

import numpy as np

EPS = 1e-15


@dataclass(frozen=True)
class EstimateResult:
    method: str
    status: str
    M_hat: float
    M_ols: float
    denominator_observed: float
    noise_power_expected: float
    denominator_corrected: float
    total_to_noise_ratio: float
    corrected_to_noise_ratio: float
    n_used: int
    assumptions: tuple[str, ...]
    reason: str

    @property
    def ready(self) -> bool:
        return self.status == "CALIBRATED_READY" and math.isfinite(self.M_hat) and self.M_hat > 0


def acceleration_noise_variance_iid(sigma: float, dt: float) -> float:
    """Var[(e[n+1]-2e[n]+e[n-1])/dt^2] for iid zero-mean noise of std sigma."""
    sigma = float(sigma)
    dt = float(dt)
    if not math.isfinite(sigma) or sigma < 0:
        raise ValueError("sigma must be finite and nonnegative")
    if not math.isfinite(dt) or dt <= 0:
        raise ValueError("dt must be finite and positive")
    return 6.0 * sigma * sigma / (dt ** 4)


def _arrays(a_obs: Sequence[float], y_obs: Sequence[float]) -> tuple[np.ndarray, np.ndarray]:
    a = np.asarray(a_obs, dtype=float)
    y = np.asarray(y_obs, dtype=float)
    if a.ndim != 1 or y.ndim != 1 or len(a) != len(y) or len(a) < 3:
        raise ValueError("a_obs and y_obs must be one-dimensional, equal-length, and contain >=3 points")
    if not np.all(np.isfinite(a)) or not np.all(np.isfinite(y)):
        raise ValueError("a_obs and y_obs must be finite")
    return a, y


def fit_moment_corrected(
    a_obs: Sequence[float],
    y_obs: Sequence[float],
    *,
    obs_noise_sigma: float,
    dt: float,
    min_total_to_noise_ratio: float = 4.0,
    min_corrected_to_noise_ratio: float = 3.0,
) -> EstimateResult:
    """Correct scalar OLS attenuation by subtracting known iid derivative-noise power.

    Model used for operational calibration:
        a_obs = a_true + u
        y_obs = M a_true + v
    with E[u]=0 and known Var(u)=6 sigma^2/dt^4. The correction is:
        M_hat = sum(a_obs*y_obs) / (sum(a_obs^2) - n Var(u))

    This is admissible only when noise provenance is explicit and corrected information remains
    well above the expected derivative-noise power.
    """
    a, y = _arrays(a_obs, y_obs)
    n = len(a)
    var_u = acceleration_noise_variance_iid(obs_noise_sigma, dt)
    noise_power = n * var_u
    denom_obs = float(np.dot(a, a))
    numerator = float(np.dot(a, y))
    m_ols = numerator / denom_obs if denom_obs > EPS else float("nan")
    denom_corr = denom_obs - noise_power
    total_ratio = denom_obs / noise_power if noise_power > EPS else float("inf")
    corrected_ratio = denom_corr / noise_power if noise_power > EPS else float("inf")
    assumptions = (
        "observation noise is iid, zero-mean, homoscedastic, and sigma is known",
        "sample spacing is uniform",
        "target-noise cross-covariance is negligible or separately validated",
        "one scalar M is valid over the fitted segment",
    )
    if denom_obs <= EPS:
        return EstimateResult(
            "moment_corrected_eiv", "UNRESOLVED", float("nan"), m_ols,
            denom_obs, noise_power, denom_corr, total_ratio, corrected_ratio, n,
            assumptions, "observed acceleration rank is zero",
        )
    if denom_corr <= EPS:
        return EstimateResult(
            "moment_corrected_eiv", "UNRESOLVED", float("nan"), m_ols,
            denom_obs, noise_power, denom_corr, total_ratio, corrected_ratio, n,
            assumptions, "expected derivative-noise power exhausts the observed denominator",
        )
    if total_ratio < min_total_to_noise_ratio or corrected_ratio < min_corrected_to_noise_ratio:
        return EstimateResult(
            "moment_corrected_eiv", "UNRESOLVED", float("nan"), m_ols,
            denom_obs, noise_power, denom_corr, total_ratio, corrected_ratio, n,
            assumptions,
            "corrected acceleration information is too close to the noise floor",
        )
    m_hat = numerator / denom_corr
    if not math.isfinite(m_hat) or m_hat <= 0:
        return EstimateResult(
            "moment_corrected_eiv", "UNRESOLVED", float("nan"), m_ols,
            denom_obs, noise_power, denom_corr, total_ratio, corrected_ratio, n,
            assumptions, "corrected estimate is non-finite or non-positive",
        )
    return EstimateResult(
        "moment_corrected_eiv", "CALIBRATED_READY", float(m_hat), float(m_ols),
        denom_obs, noise_power, denom_corr, total_ratio, corrected_ratio, n,
        assumptions, "known-noise attenuation correction passed information gates",
    )


def fit_replicate_iv(
    a_obs_1: Sequence[float],
    y_obs_1: Sequence[float],
    a_obs_2: Sequence[float],
    y_obs_2: Sequence[float],
    *,
    min_cross_information: float = 1e-10,
) -> EstimateResult:
    """Symmetric independent-replicate instrumental-variable estimator.

    Two observations must measure the same latent trajectory with independent observation noise:
        M_hat = [a1·y2 + a2·y1] / [2 a1·a2]
    Cross-products remove the additive regressor-noise power in expectation.
    """
    a1, y1 = _arrays(a_obs_1, y_obs_1)
    a2, y2 = _arrays(a_obs_2, y_obs_2)
    if len(a1) != len(a2):
        raise ValueError("replicates must have equal length")
    denom_cross = float(np.dot(a1, a2))
    numerator = 0.5 * float(np.dot(a1, y2) + np.dot(a2, y1))
    denom_obs = 0.5 * float(np.dot(a1, a1) + np.dot(a2, a2))
    m_ols = 0.5 * (
        float(np.dot(a1, y1) / np.dot(a1, a1)) +
        float(np.dot(a2, y2) / np.dot(a2, a2))
    )
    assumptions = (
        "replicates observe the same latent trajectory",
        "replicate observation noises are independent",
        "time alignment and calibration are shared",
        "one scalar M is valid over the fitted segment",
    )
    if not math.isfinite(denom_cross) or denom_cross <= min_cross_information:
        return EstimateResult(
            "replicate_iv", "UNRESOLVED", float("nan"), m_ols, denom_obs, 0.0,
            denom_cross, float("inf"), float("inf"), len(a1), assumptions,
            "replicate cross-information is non-positive or too small",
        )
    m_hat = numerator / denom_cross
    if not math.isfinite(m_hat) or m_hat <= 0:
        return EstimateResult(
            "replicate_iv", "UNRESOLVED", float("nan"), m_ols, denom_obs, 0.0,
            denom_cross, float("inf"), float("inf"), len(a1), assumptions,
            "replicate-IV estimate is non-finite or non-positive",
        )
    return EstimateResult(
        "replicate_iv", "CALIBRATED_READY", float(m_hat), m_ols, denom_obs, 0.0,
        denom_cross, float("inf"), float("inf"), len(a1), assumptions,
        "independent-replicate IV passed cross-information gate",
    )


def relative_gap(a: float, b: float) -> float:
    return abs(float(a) - float(b)) / max(abs(float(a)), abs(float(b)), EPS)


def combine_reader_record(
    reader: EstimateResult,
    record: EstimateResult,
    *,
    max_relative_gap: float = 0.05,
) -> Mapping[str, object]:
    """Return a fail-closed joint operational coefficient."""
    if not reader.ready or not record.ready:
        return {
            "status": "UNRESOLVED",
            "M_joint": None,
            "relative_gap": None,
            "reason": "reader and record must both be CALIBRATED_READY",
        }
    gap = relative_gap(reader.M_hat, record.M_hat)
    if gap > max_relative_gap:
        return {
            "status": "UNRESOLVED",
            "M_joint": None,
            "relative_gap": gap,
            "reason": f"reader/record disagreement exceeds {max_relative_gap:.1%}",
        }
    return {
        "status": "CALIBRATED_READY",
        "M_joint": 0.5 * (reader.M_hat + record.M_hat),
        "relative_gap": gap,
        "reason": "both corrected channels pass and agree",
    }


def exchange_path(
    phi: Sequence[float],
    psi: Sequence[float],
    times: Sequence[float],
    *,
    M_value: float,
    cost_unit_rd: float,
    path_semantics: str,
    delta_is_dimensionless: bool,
) -> Mapping[str, object]:
    """Compute signed exchange and a candidate nonnegative closure load.

    lambda is emitted only for declared primitive_closure paths with dimensionless Delta.
    """
    p = np.asarray(phi, dtype=float)
    q = np.asarray(psi, dtype=float)
    t = np.asarray(times, dtype=float)
    if p.ndim != 1 or q.ndim != 1 or t.ndim != 1 or not (len(p) == len(q) == len(t)) or len(p) < 2:
        raise ValueError("phi, psi, and times must be equal-length one-dimensional arrays")
    if not np.all(np.isfinite(p)) or not np.all(np.isfinite(q)) or not np.all(np.isfinite(t)):
        raise ValueError("path arrays must be finite")
    if not math.isfinite(M_value) or M_value <= 0:
        raise ValueError("M_value must be finite and positive")
    if not math.isfinite(cost_unit_rd) or cost_unit_rd <= 0:
        raise ValueError("cost_unit_rd must be finite and positive")
    dt = np.diff(t)
    if np.any(dt <= 0):
        raise ValueError("times must be strictly increasing")
    signed_steps = M_value * np.diff(p) * np.diff(q) / (dt * cost_unit_rd)
    signed_total = float(np.sum(signed_steps))
    delta_candidate = float(np.sum(np.abs(signed_steps)))
    result: dict[str, object] = {
        "signed_exchange_total_rd": signed_total,
        "Delta_candidate": delta_candidate,
        "orientation_cancellation_fraction": (
            0.0 if delta_candidate <= EPS else 1.0 - abs(signed_total) / delta_candidate
        ),
        "lambda": None,
        "status": "DIAGNOSTIC_ONLY",
    }
    if path_semantics == "primitive_closure" and delta_is_dimensionless:
        result["lambda"] = math.exp(-delta_candidate) if delta_candidate < 745 else 0.0
        result["status"] = "CALIBRATED_READY"
    return result


def pi0_from_branch_lambdas(branch_lambdas: Mapping[str, float]) -> Optional[float]:
    if not all(key in branch_lambdas for key in ("U", "D", "E")):
        return None
    values = {key: float(branch_lambdas[key]) for key in ("U", "D", "E")}
    if any(not math.isfinite(v) or v <= 0 or v > 1 for v in values.values()):
        raise ValueError("branch lambdas must lie in (0,1]")
    return 3.0 * values["U"] + 3.0 * values["D"] + values["E"]
