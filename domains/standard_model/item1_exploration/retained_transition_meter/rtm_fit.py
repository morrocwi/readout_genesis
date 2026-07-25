#!/usr/bin/env python3
"""
RTM v1 -- rtm_fit.py: FITS (does not derive) the scalar DRL exchange coefficient M_hat from a
transition tape, by rearranging the Reader equation (II.8a, EQ-022) and, independently, the Record
equation, to isolate the coefficient of the discrete second-difference term.

*** TIER: fit_calibrated. M_hat is FITTED from tape data, NEVER claimed root-derived. This is the
    SAME open quantity HANDOFF_NEXT_SESSION.md ~line 91 names "the price per elementary
    retained-distinction transition" (M_n in the DRL exchange term), POSITED not derived, 8 failed
    derivation attempts already on record for this quantity -- RTM does not attempt a 9th
    derivation, it fits a number from a tape and reports how well that fit holds up. ***

Discretization convention (recovered from, and must match, the reused stepper -- verified by
hand-deriving step_reader/step_record's own b_rhs formulas back to this form, see rtm module
docstring in rtm_v1.py for the derivation):
    delta_t^2 X_n := (X_{n+1} - 2*X_n + X_{n-1}) / dt^2      (central second difference)
    delta_t^c X_n := (X_{n+1} - X_{n-1}) / (2*dt)             (central first difference)

Reader equation rearranged (G[Theta_n] = identity, per the tape's disclosed simplification):
    M * delta_t^2 Phi_n = R_Phi,n + J_n - D*delta_t^c Phi_n - K*Phi_n - gradV(Phi_n)
    a_n := delta_t^2 Phi_n ,  y_n := RHS above
    M_hat_phi = sum(a_n * y_n) / sum(a_n * a_n)     (scalar least squares, d=1)

Record equation rearranged:
    M * delta_t^2 Psi_n = R_Psi,n + D*delta_t^c Psi_n - K*Psi_n - grad2V(Phi_n)*Psi_n
    a_n := delta_t^2 Psi_n ,  y_n := RHS above
    M_hat_psi = sum(a_n * y_n) / sum(a_n * a_n)

Rank/underdetermination gate (System paper risk #1, taken seriously, not just non-zero-gated):
Phi settles toward a fixed point over the tape (attempt1's own documented behavior), so late-tape
a_n = delta_t^2 Phi_n shrinks toward the SAME magnitude as the second-difference of pure
observation noise (obs_noise_sigma, see tape_generator.py) -- a segment can have sum(a_n^2) that is
technically nonzero yet be numerically DOMINATED by noise, producing a garbage M_hat that a naive
"nonzero" gate would wave through. The gate below compares sum(a_n^2) for the segment against the
EXPECTED sum(a_n^2) contributed by observation noise ALONE on a segment of that size (derived
analytically from obs_noise_sigma and dt: Var[central 2nd diff of iid noise] = 6*sigma^2/dt^4 per
point), and requires the segment's actual sum(a_n^2) to exceed that noise floor by a factor of
NOISE_FLOOR_MARGIN before trusting the fit -- this is what actually catches the "Phi has settled,
this segment carries no fit information" failure mode risk #1 warns about; a bare nonzero check
does not (confirmed empirically: a genuinely garbage late-tape fit was found to be NOT caught by a
naive 1e-6 nonzero gate during development of this file, and IS caught by the noise-floor gate).
"""
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from . import stepper_reuse as stepper

NOISE_FLOOR_MARGIN = 3.0    # segment's sum(a_n^2) must exceed the noise-floor-only expectation by this factor
ABSOLUTE_RANK_FLOOR = 1e-12  # backstop for segments/tapes with no declared obs_noise_sigma


@dataclass
class FitResult:
    mode: str                    # "reader" or "record"
    M_hat: float
    sum_aa: float                 # sum(a_n^2), the scalar "A A^T"
    rank_AAt: int                 # 0 or 1 for the scalar case
    cond_AAt: float                # 1.0 if well-posed (scalar, trivially well-conditioned when rank=1)
    underdetermined: bool
    n_used: int
    residual_rms: float            # RMS of (a_n*M_hat - y_n) over the FIT segment itself
    noise_floor_expected: float     # expected sum(a_n^2) from observation noise alone, this segment size
    noise_floor_ratio: float        # sum_aa / noise_floor_expected -- must exceed NOISE_FLOOR_MARGIN
    tier: str = "fit_calibrated"


def _discrete_diffs(x: np.ndarray, dt: float):
    """Central 2nd and 1st differences at interior points 1..N-2. Returns (d2, d1, idx)."""
    d2 = (x[2:] - 2 * x[1:-1] + x[:-2]) / dt**2
    d1 = (x[2:] - x[:-2]) / (2 * dt)
    idx = np.arange(1, len(x) - 1)
    return d2, d1, idx


def _reader_ay(tape: dict, sl: slice):
    dt = tape["meta"]["dt"]
    D, K = tape["meta"]["D"], tape["meta"]["K"]
    phi = tape["Phi"]
    d2phi, d1phi, idx = _discrete_diffs(phi, dt)
    keep = (idx >= (sl.start or 0)) & (idx < (sl.stop if sl.stop is not None else len(phi)))
    idx_k = idx[keep]
    a = d2phi[keep]
    R_Phi = tape["R_Phi"][idx_k]
    J = tape["J"][idx_k]
    phi_n = phi[idx_k]
    y = R_Phi + J - D * d1phi[keep] - K * phi_n - stepper.gradV(phi_n)
    return a, y, idx_k


def _record_ay(tape: dict, sl: slice):
    dt = tape["meta"]["dt"]
    D, K = tape["meta"]["D"], tape["meta"]["K"]
    psi = tape["Psi"]
    phi = tape["Phi"]
    d2psi, d1psi, idx = _discrete_diffs(psi, dt)
    keep = (idx >= (sl.start or 0)) & (idx < (sl.stop if sl.stop is not None else len(psi)))
    idx_k = idx[keep]
    a = d2psi[keep]
    R_Psi = tape["R_Psi"][idx_k]
    psi_n = psi[idx_k]
    phi_n = phi[idx_k]
    y = R_Psi + D * d1psi[keep] - K * psi_n - stepper.grad2V(phi_n) * psi_n
    return a, y, idx_k


def fit_M(tape: dict, segment: slice = slice(None), mode: str = "reader") -> FitResult:
    """Scalar least-squares fit of M_hat over `segment` (an index slice into the tape), from
    EITHER the Reader equation (mode="reader") or the Record equation (mode="record")."""
    if mode not in ("reader", "record"):
        raise ValueError(f"mode must be 'reader' or 'record', got {mode!r}")
    a, y, idx_k = (_reader_ay if mode == "reader" else _record_ay)(tape, segment)

    sum_aa = float(np.sum(a * a))
    n_used = len(a)

    dt = tape["meta"]["dt"]
    sigma = tape["meta"].get("obs_noise_sigma", 0.0)
    if sigma and sigma > 0 and n_used > 0:
        # Var[central 2nd diff of iid N(0,sigma^2)] = (1^2+(-2)^2+1^2)*sigma^2/dt^4 = 6*sigma^2/dt^4
        noise_floor_expected = n_used * 6.0 * sigma**2 / dt**4
    else:
        noise_floor_expected = 0.0
    noise_floor_ratio = (sum_aa / noise_floor_expected) if noise_floor_expected > 0 else float("inf")

    underdetermined = (
        n_used == 0
        or sum_aa < ABSOLUTE_RANK_FLOOR
        or (noise_floor_expected > 0 and noise_floor_ratio < NOISE_FLOOR_MARGIN)
    )

    if underdetermined:
        M_hat = float("nan")
        residual_rms = float("nan")
        rank_AAt = 0
    else:
        M_hat = float(np.sum(a * y) / sum_aa)
        resid = a * M_hat - y
        residual_rms = float(np.sqrt(np.mean(resid**2)))
        rank_AAt = 1

    return FitResult(
        mode=mode, M_hat=M_hat, sum_aa=sum_aa, rank_AAt=rank_AAt,
        cond_AAt=1.0 if rank_AAt == 1 else float("inf"),
        underdetermined=underdetermined, n_used=n_used, residual_rms=residual_rms,
        noise_floor_expected=noise_floor_expected, noise_floor_ratio=noise_floor_ratio,
    )


def predict_y(tape: dict, segment: slice, M_hat: float, mode: str = "reader"):
    """Returns (y_true, y_pred, idx) for RMSE/holdout evaluation on `segment` using a GIVEN M_hat
    (typically fit on a different segment) -- does not refit."""
    a, y_true, idx_k = (_reader_ay if mode == "reader" else _record_ay)(tape, segment)
    y_pred = a * M_hat
    return y_true, y_pred, idx_k
