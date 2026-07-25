#!/usr/bin/env python3
"""
RTM v3 (synthesis) -- rtm_fit.py: fits M_hat from a multi-path tape, combining:
- v1's (PR #26) analytic noise-floor underdetermination gate (stricter than a bare nonzero check;
  empirically verified during v1's own development to catch a garbage late-segment fit a naive
  gate misses).
- readout_genesis PR #67's JOINT fit: pool the Reader equation's (a,y) pairs and the Record
  equation's (a,y) pairs into ONE simultaneous least-squares estimate, used as the actual value fed
  downstream, while the separate Reader-only and Record-only fits are kept ONLY as an independent
  self-consistency diagnostic (dual agreement) -- not averaged into the final answer, not discarded.

*** TIER: fit_calibrated throughout. Same open quantity as v1/PR#26 and v0.1/PR#67 -- M_n, POSITED
    not derived (HANDOFF_NEXT_SESSION.md ~line 91, 8 failed derivation attempts on record). ***

Discretization convention (identical to v1, re-verified against the reused stepper, not re-derived
here -- see rtm_fit.py in candidate/retained-transition-meter-v1-2026-07-25 for the by-hand
derivation, independently adversarially reviewed there):
    delta_t^2 X_n := (X_{n+1} - 2 X_n + X_{n-1}) / dt^2
    delta_t^c X_n := (X_{n+1} - X_{n-1}) / (2 dt)
    Reader: a_n := delta_t^2 Phi_n,  y_n := R_Phi,n + J_n - D*delta_t^c Phi_n - K*Phi_n - gradV(Phi_n)
    Record: a_n := delta_t^2 Psi_n,  y_n := R_Psi,n + D*delta_t^c Psi_n - K*Psi_n - grad2V(Phi_n)*Psi_n
"""
from dataclasses import dataclass
from typing import List

import numpy as np

from . import stepper_reuse as stepper

NOISE_FLOOR_MARGIN = 3.0
ABSOLUTE_RANK_FLOOR = 1e-12


@dataclass
class FitResult:
    mode: str                # "reader", "record", or "joint"
    M_hat: float
    sum_aa: float
    underdetermined: bool
    n_used: int
    noise_floor_expected: float
    noise_floor_ratio: float
    tier: str = "fit_calibrated"


def _discrete_diffs(x: np.ndarray, dt: float):
    d2 = (x[2:] - 2 * x[1:-1] + x[:-2]) / dt**2
    d1 = (x[2:] - x[:-2]) / (2 * dt)
    idx = np.arange(1, len(x) - 1)
    return d2, d1, idx


def _path_reader_ay(path: dict, dt: float, D: float, K: float):
    phi = path["Phi"]
    d2phi, d1phi, idx = _discrete_diffs(phi, dt)
    R_Phi = path["R_Phi"][idx]
    J = path["J"][idx]
    phi_n = phi[idx]
    a = d2phi
    y = R_Phi + J - D * d1phi - K * phi_n - stepper.gradV(phi_n)
    return a, y


def _path_record_ay(path: dict, dt: float, D: float, K: float):
    psi = path["Psi"]
    phi = path["Phi"]
    d2psi, d1psi, idx = _discrete_diffs(psi, dt)
    R_Psi = path["R_Psi"][idx]
    psi_n = psi[idx]
    phi_n = phi[idx]
    a = d2psi
    y = R_Psi + D * d1psi - K * psi_n - stepper.grad2V(phi_n) * psi_n
    return a, y


def _noise_floor(n_used: int, dt: float, sigma: float) -> float:
    if not sigma or sigma <= 0 or n_used <= 0:
        return 0.0
    # Var[central 2nd diff of iid N(0,sigma^2)] = 6*sigma^2/dt^4 per point (v1's own derivation)
    return n_used * 6.0 * sigma**2 / dt**4


def fit_M(tape: dict, paths: List[dict], mode: str = "joint") -> FitResult:
    """Fits M_hat pooling all supplied `paths` together (a genuine multi-path fit, not one path
    re-used as a stand-in for the whole tape). mode in {"reader","record","joint"}."""
    if mode not in ("reader", "record", "joint"):
        raise ValueError(f"mode must be reader/record/joint, got {mode!r}")
    dt = tape["meta"]["dt"]
    D, K = tape["meta"]["D"], tape["meta"]["K"]
    sigma = tape["meta"].get("obs_noise_sigma", 0.0)

    a_all, y_all = [], []
    for p in paths:
        if mode in ("reader", "joint"):
            a_r, y_r = _path_reader_ay(p, dt, D, K)
            a_all.append(a_r); y_all.append(y_r)
        if mode in ("record", "joint"):
            a_p, y_p = _path_record_ay(p, dt, D, K)
            a_all.append(a_p); y_all.append(y_p)

    a = np.concatenate(a_all) if a_all else np.array([])
    y = np.concatenate(y_all) if y_all else np.array([])
    n_used = len(a)
    sum_aa = float(np.sum(a * a)) if n_used else 0.0
    noise_floor_expected = _noise_floor(n_used, dt, sigma)
    noise_floor_ratio = (sum_aa / noise_floor_expected) if noise_floor_expected > 0 else float("inf")

    underdetermined = (
        n_used == 0
        or sum_aa < ABSOLUTE_RANK_FLOOR
        or (noise_floor_expected > 0 and noise_floor_ratio < NOISE_FLOOR_MARGIN)
    )
    M_hat = float("nan") if underdetermined else float(np.sum(a * y) / sum_aa)

    return FitResult(mode=mode, M_hat=M_hat, sum_aa=sum_aa, underdetermined=underdetermined,
                      n_used=n_used, noise_floor_expected=noise_floor_expected,
                      noise_floor_ratio=noise_floor_ratio)
