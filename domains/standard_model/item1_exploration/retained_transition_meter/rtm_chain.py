#!/usr/bin/env python3
"""
RTM v1 -- rtm_chain.py: the cost chain built on TOP of a fit_calibrated M_hat.

    c_n        = (1/Delta_t) * DeltaPhi_n * M_hat * DeltaPsi_n           (scalar case, d=1)
    Delta_j_eff = sum_{n in path} c_n
    lambda_j    = exp(-Delta_j_eff)
    Pi_0        = 3*lambda_U + 3*lambda_D + lambda_E                    (v1.13's own formula, untouched)

*** TIER: fit_calibrated throughout (inherits M_hat's tier -- every downstream number here is at
    LEAST as uncertain as the M_hat it was built from; never re-tagged to a stronger tier). ***

Pi_0 CAVEAT (must not be skipped or softened): v1.13's Pi_0 formula is defined over THREE
real fermion branches (U, D, E) from item1_fit_calibrated_v1.py's own PDG-mass fit. RTM's tape is a
SINGLE scalar (Phi, Psi) pair -- it has no U/D/E branch structure, no connection to real quark/
lepton masses, and does not attempt to build one. Plugging RTM's one fit-calibrated lambda_j into
all three slots of the Pi_0 formula below is done ONLY as an internal-consistency demonstration
(does RTM's own chain, run through v1.13's aggregation formula, land inside the SAME no-go bound
item1_fit_calibrated_v1.py already reports for the real PDG-mass fit?) -- it is explicitly NOT a
claim about real fermion generations, NOT a re-derivation of Pi_0, and NOT a connection to the
separate, untouched, out-of-scope generation-multiplicity item.
"""
from dataclasses import dataclass
from typing import List

import numpy as np


@dataclass
class ChainResult:
    c_n: np.ndarray
    Delta_j_eff: float
    lambda_j: float
    path_used: List[int]
    tier: str = "fit_calibrated"


def cost_chain(tape: dict, M_hat: float, path: List[int] = None) -> ChainResult:
    """c_n over the given `path` (a list of tape indices n such that n, n+1 are both valid);
    default path = the whole tape. Delta_j_eff = sum of c_n over the path; lambda_j = exp(-Delta_j_eff)."""
    dt = tape["meta"]["dt"]
    phi, psi = tape["Phi"], tape["Psi"]
    N = len(phi)
    if path is None:
        path = list(range(N - 1))
    path = [n for n in path if 0 <= n < N - 1]

    d_phi = phi[np.array(path) + 1] - phi[np.array(path)]
    d_psi = psi[np.array(path) + 1] - psi[np.array(path)]
    c_n = (1.0 / dt) * d_phi * M_hat * d_psi

    Delta_j_eff = float(np.sum(c_n))
    # exp(-Delta_j_eff) can overflow/underflow for large |Delta_j_eff| (e.g. Psi's own instability,
    # attempt1's documented runaway growth) -- clip and DISCLOSE, never silently return inf/0 as if
    # it were a normal finite fit_calibrated number.
    if Delta_j_eff > 700:
        lambda_j = 0.0
    elif Delta_j_eff < -700:
        lambda_j = float("inf")
    else:
        lambda_j = float(np.exp(-Delta_j_eff))

    return ChainResult(c_n=c_n, Delta_j_eff=Delta_j_eff, lambda_j=lambda_j, path_used=path)


def pi0(lambda_U: float, lambda_D: float, lambda_E: float) -> float:
    """v1.13's own formula, untouched. See module docstring for the Pi_0 caveat -- RTM plugs the
    SAME single lambda_j into all three slots as an internal-consistency demonstration only."""
    return 3 * lambda_U + 3 * lambda_D + lambda_E
