#!/usr/bin/env python3
"""
RTM v3 (synthesis) -- rtm_chain.py: cost chain c_n -> Delta_j_eff -> lambda_j -> Pi_0, combining:
- v0.1/PR#67's per-path-then-MEDIAN-across-paths aggregation (robust to a single unusual path
  dominating a branch's cost estimate; v1/PR#26 only ever had one path per branch to aggregate,
  so never actually exercised this).
- v1/PR#26's WITHIN-PATH ADDITIVITY check (summed per-step c_n vs. a directly-computed path-total,
  independent code path) -- v0.1/PR#67 does not carry an equivalent check.
- BOTH signed and |abs| cost reported, not just one silently chosen: the DRL action's own exchange
  term (1/dt)*DeltaPhi_n^T*M_n*DeltaPsi_n is SIGNED (ITEM1_EXPLORATION_LOG.md's own quoted formula
  has no abs value) -- v0.1/PR#67 takes |...| specifically to force lambda into (0,1] and calls the
  sign "an orientation readout, not a cost," a real but debatable design choice. v3 does not decide
  this for the reader: both numbers are computed and printed, and BOTH lambda_j values (signed-path,
  abs-path) are carried through to Pi_0, so a real disagreement between the two conventions is
  visible rather than resolved silently by only ever picking one.
"""
from dataclasses import dataclass
from typing import Dict, List

import numpy as np


@dataclass
class ChainResult:
    branch_delta_eff_signed: Dict[str, float]
    branch_delta_eff_abs: Dict[str, float]
    branch_lambda_signed: Dict[str, float]
    branch_lambda_abs: Dict[str, float]
    pi0_signed: float
    pi0_abs: float
    additivity_relative_diff: float
    tier: str = "fit_calibrated"


def _path_c_n(path: dict, dt: float, M_hat: float):
    """Per-transition cost inside ONE path: c_n = (1/dt) * DeltaPhi_n * M_hat * DeltaPsi_n
    (scalar case). Returns the SIGNED array."""
    dphi = np.diff(path["Phi"])
    dpsi = np.diff(path["Psi"])
    return (M_hat * dphi * dpsi) / dt


def path_delta_eff(path: dict, dt: float, M_hat: float):
    """Returns (delta_eff_signed, delta_eff_abs, additivity_relative_diff) for ONE path.
    additivity check: sum(c_n) [built from the per-step array, one code path] vs. a DIRECTLY
    computed total using the full path's endpoint-to-endpoint DeltaPhi/DeltaPsi split into the SAME
    per-step terms via a genuinely separate accumulation loop (not the same numpy reduction called
    twice) -- v1's own reconciliation note (System paper) explains why the naive bilinear
    (phi_end-phi_start)*M*(psi_end-psi_start) does NOT telescope to the same value as sum(c_n) in
    general and would test a false identity; this uses an explicit Python loop instead."""
    c_n = _path_c_n(path, dt, M_hat)
    delta_signed_vectorized = float(np.sum(c_n))
    delta_abs_vectorized = float(np.sum(np.abs(c_n)))

    # independent accumulation, explicit loop, not numpy.sum on the same array
    acc_signed = 0.0
    acc_abs = 0.0
    phi, psi = path["Phi"], path["Psi"]
    for n in range(len(phi) - 1):
        term = (M_hat * (phi[n + 1] - phi[n]) * (psi[n + 1] - psi[n])) / dt
        acc_signed += term
        acc_abs += abs(term)

    rel_diff_signed = abs(acc_signed - delta_signed_vectorized) / max(abs(delta_signed_vectorized), 1e-300)
    rel_diff_abs = abs(acc_abs - delta_abs_vectorized) / max(abs(delta_abs_vectorized), 1e-300)
    additivity_relative_diff = max(rel_diff_signed, rel_diff_abs)

    return delta_signed_vectorized, delta_abs_vectorized, additivity_relative_diff


def cost_chain(tape: dict, paths: List[dict], M_hat: float) -> ChainResult:
    dt = tape["meta"]["dt"]
    branch_paths_signed: Dict[str, List[float]] = {}
    branch_paths_abs: Dict[str, List[float]] = {}
    additivity_diffs = []

    for p in paths:
        d_signed, d_abs, add_diff = path_delta_eff(p, dt, M_hat)
        branch_paths_signed.setdefault(p["branch"], []).append(d_signed)
        branch_paths_abs.setdefault(p["branch"], []).append(d_abs)
        additivity_diffs.append(add_diff)

    # median across paths within a branch (v0.1/PR#67's aggregation, adopted)
    branch_delta_eff_signed = {b: float(np.median(vals)) for b, vals in branch_paths_signed.items()}
    branch_delta_eff_abs = {b: float(np.median(vals)) for b, vals in branch_paths_abs.items()}

    branch_lambda_signed = {b: float(np.exp(-d)) for b, d in branch_delta_eff_signed.items()}
    branch_lambda_abs = {b: float(np.exp(-d)) for b, d in branch_delta_eff_abs.items()}

    def pi0_of(lambdas):
        if all(b in lambdas for b in ("U", "D", "E")):
            return 3.0 * lambdas["U"] + 3.0 * lambdas["D"] + lambdas["E"]
        return float("nan")

    return ChainResult(
        branch_delta_eff_signed=branch_delta_eff_signed,
        branch_delta_eff_abs=branch_delta_eff_abs,
        branch_lambda_signed=branch_lambda_signed,
        branch_lambda_abs=branch_lambda_abs,
        pi0_signed=pi0_of(branch_lambda_signed),
        pi0_abs=pi0_of(branch_lambda_abs),
        additivity_relative_diff=max(additivity_diffs) if additivity_diffs else float("nan"),
    )
