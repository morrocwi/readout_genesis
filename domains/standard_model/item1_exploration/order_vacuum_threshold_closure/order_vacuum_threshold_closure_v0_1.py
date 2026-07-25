#!/usr/bin/env python3
"""Order-vacuum threshold closure v0.1.

Stacked on the primitive-branch parameter-reduction candidate.  This module removes
alpha_order and beta_order as independent Standard-Model-sector dials by inheriting
them from the already-declared scalar mother potential

    V(x) = (a/2) x^2 + (b/4) x^4

under the declared amplitude bridge r = x^2:

    V_bare(r) = alpha_order r + beta_order r^2,
    alpha_order = a/2,
    beta_order  = b/4.

It then combines the computed primitive-branch Pi0 with the exact v1.13 criterion
Pi0 > alpha_order and solves the unique convex minimum r_*.

Tier: exact algebraic bridge inside a declared finite architecture + calibrated
finite diagnostic for Pi0.  This is not an unrestricted-root derivation or a
physical Higgs pole-mass prediction.

REQUIRED CORRECTION (independent scientific-methodology review, 2026-07-25): the ORDERED_READY
result on this fixture is STRUCTURALLY GUARANTEED, not data-dependent. Because pi0_from_report
requires every lambda_j in (0,1], Pi0 = 3*lambda_U+3*lambda_D+lambda_E is unconditionally > 0 for
ANY legitimate branch-tape input. Since alpha_order = a/2 = -0.5 on this stepper (a=-1 is fixed by
the mother potential, not by the branch data), Pi0 > alpha_order holds for every possible
legitimate lambda_U/D/E -- the branch-tape construction could not have produced UNORDERED_READY on
this stepper no matter what the U/D/E data said. See `min_possible_pi0_this_alpha_gate` in
run_fixture()'s output and `test_alpha_order_is_below_pi0_unconditional_lower_bound` for a direct
demonstration. This does not mean the code is wrong -- Pi0, r_star, and the branch lambdas are
still real, correctly-computed, and non-trivial numbers -- but the ORDERED_READY status itself is
not evidence that the primitive-branch construction "worked" to produce order; it is a consequence
of this potential's sign, disclosed here and in claim_boundary rather than left implicit.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

PARAM_DIR = (
    ROOT
    / "domains"
    / "standard_model"
    / "item1_exploration"
    / "primitive_branch_parameter_reduction"
)
OPERATIONAL_DIR = (
    ROOT
    / "domains"
    / "standard_model"
    / "item1_exploration"
    / "retained_transition_operational_closure"
)
for directory in (PARAM_DIR, OPERATIONAL_DIR):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from domains.standard_model.item1_exploration.primitive_branch_parameter_reduction.primitive_branch_fixture_v0_1 import (  # noqa: E402
    run_fixture as run_branch_fixture,
)
from domains.standard_model.item1_exploration.retained_transition_operational_closure.operational_exchange_closure_v0_1 import (  # noqa: E402
    load_stepper,
)

EPS = 1e-15


class OrderThresholdError(ValueError):
    """Fail-closed order-threshold contract error."""


def derive_order_coefficients(stepper: object) -> Mapping[str, float | str]:
    """Inherit order-sector coefficients from V(x) using r=x^2 exactly."""
    try:
        a = float(stepper.a)
        b = float(stepper.b)
    except (AttributeError, TypeError, ValueError) as exc:
        raise OrderThresholdError("stepper must disclose finite scalar potential coefficients a,b") from exc
    if not math.isfinite(a) or not math.isfinite(b):
        raise OrderThresholdError("mother-potential coefficients must be finite")

    alpha_order = 0.5 * a
    beta_order = 0.25 * b
    if beta_order <= 0:
        raise OrderThresholdError("beta_order=b/4 must be positive for the v1.13 convexity theorem")

    return {
        "bridge_id": "scalar-amplitude-order-bridge-r-equals-x2-v0.1",
        "source_potential": "V(x)=(a/2)x^2+(b/4)x^4",
        "coordinate_map": "r=x^2",
        "a": a,
        "b": b,
        "alpha_order": alpha_order,
        "beta_order": beta_order,
        "status": "INHERITED_NOT_NEW_DIALS",
    }


def pi0_from_report(report: Mapping[str, object]) -> tuple[float, dict[str, float]]:
    if report.get("status") != "CALIBRATED_READY":
        raise OrderThresholdError("primitive-branch report must be CALIBRATED_READY")
    branches = report.get("branches")
    if not isinstance(branches, dict):
        raise OrderThresholdError("primitive-branch report is missing branches")
    lambdas: dict[str, float] = {}
    for branch in ("U", "D", "E"):
        item = branches.get(branch)
        if not isinstance(item, dict):
            raise OrderThresholdError(f"missing branch {branch}")
        try:
            value = float(item["lambda"])
        except (KeyError, TypeError, ValueError) as exc:
            raise OrderThresholdError(f"branch {branch} lambda is invalid") from exc
        if not math.isfinite(value) or value <= 0 or value > 1:
            raise OrderThresholdError(f"branch {branch} lambda must lie in (0,1]")
        lambdas[branch] = value
    pi0 = 3.0 * lambdas["U"] + 3.0 * lambdas["D"] + lambdas["E"]
    disclosed = float(report.get("Pi0", float("nan")))
    if not math.isfinite(disclosed) or abs(disclosed - pi0) > 1e-12:
        raise OrderThresholdError("disclosed Pi0 does not match branch lambdas")
    return pi0, lambdas


def vprime(r: float, alpha: float, beta: float, lambdas: Mapping[str, float]) -> float:
    return (
        alpha
        + 2.0 * beta * r
        - 3.0 * lambdas["U"] / (1.0 + lambdas["U"] * r)
        - 3.0 * lambdas["D"] / (1.0 + lambdas["D"] * r)
        - lambdas["E"] / (1.0 + lambdas["E"] * r)
    )


def vsecond(r: float, beta: float, lambdas: Mapping[str, float]) -> float:
    return (
        2.0 * beta
        + 3.0 * lambdas["U"] ** 2 / (1.0 + lambdas["U"] * r) ** 2
        + 3.0 * lambdas["D"] ** 2 / (1.0 + lambdas["D"] * r) ** 2
        + lambdas["E"] ** 2 / (1.0 + lambdas["E"] * r) ** 2
    )


def veffective(r: float, alpha: float, beta: float, lambdas: Mapping[str, float]) -> float:
    return (
        alpha * r
        + beta * r * r
        - 3.0 * math.log1p(lambdas["U"] * r)
        - 3.0 * math.log1p(lambdas["D"] * r)
        - math.log1p(lambdas["E"] * r)
    )


def solve_phase(alpha: float, beta: float, lambdas: Mapping[str, float]) -> Mapping[str, object]:
    if not math.isfinite(alpha) or not math.isfinite(beta) or beta <= 0:
        raise OrderThresholdError("alpha must be finite and beta must be finite and positive")
    pi0 = 3.0 * lambdas["U"] + 3.0 * lambdas["D"] + lambdas["E"]
    margin = pi0 - alpha
    s2 = 3.0 * lambdas["U"] ** 2 + 3.0 * lambdas["D"] ** 2 + lambdas["E"] ** 2

    if margin <= 0:
        return {
            "status": "UNORDERED_READY",
            "criterion": "Pi0 <= alpha_order",
            "Pi0": pi0,
            "alpha_order": alpha,
            "beta_order": beta,
            "order_margin": margin,
            "r_star": 0.0,
            "V_eff_r_star": 0.0,
            "V_eff_second_r_star": vsecond(0.0, beta, lambdas),
            "radial_curvature_proxy": 0.0,
            "lower_bound_r_star": 0.0,
            "upper_bound_r_star": 0.0,
        }

    lo, hi = 0.0, 1.0
    while vprime(hi, alpha, beta, lambdas) < 0:
        hi *= 2.0
        if hi > 1e12:
            raise OrderThresholdError("failed to bracket the unique convex minimum")
    for _ in range(256):
        mid = 0.5 * (lo + hi)
        if vprime(mid, alpha, beta, lambdas) < 0:
            lo = mid
        else:
            hi = mid
    r_star = 0.5 * (lo + hi)
    curvature = vsecond(r_star, beta, lambdas)
    if r_star <= 0 or curvature <= 0 or abs(vprime(r_star, alpha, beta, lambdas)) > 1e-11:
        raise OrderThresholdError("ordered minimum did not satisfy convex stationary-point gates")

    lower = margin / (2.0 * beta + s2)
    upper = margin / (2.0 * beta)
    if not (lower <= r_star < upper):
        raise OrderThresholdError("r_star violates the exact v1.13 bounds")

    return {
        "status": "ORDERED_READY",
        "criterion": "Pi0 > alpha_order",
        "Pi0": pi0,
        "alpha_order": alpha,
        "beta_order": beta,
        "order_margin": margin,
        "r_star": r_star,
        "V_eff_r_star": veffective(r_star, alpha, beta, lambdas),
        "V_eff_second_r_star": curvature,
        "radial_curvature_proxy": 2.0 * r_star * curvature,
        "lower_bound_r_star": lower,
        "upper_bound_r_star": upper,
    }


def relative_error(estimate: float, truth: float) -> float:
    return abs(float(estimate) - float(truth)) / max(abs(float(truth)), EPS)


def run_fixture() -> Mapping[str, object]:
    stepper = load_stepper()
    bridge = derive_order_coefficients(stepper)
    branch_report = run_branch_fixture()
    pi0, lambdas = pi0_from_report(branch_report)
    phase = solve_phase(
        float(bridge["alpha_order"]),
        float(bridge["beta_order"]),
        lambdas,
    )

    comparison = branch_report.get("known_fixture_comparison")
    if not isinstance(comparison, dict):
        raise OrderThresholdError("fixture comparison is required for the disclosed error audit")
    pi0_true = float(comparison["Pi0_true"])
    # M affects every branch Delta linearly.  Reconstruct the true fixture lambdas from
    # the disclosed branch Delta and the disclosed M ratio without introducing new inputs.
    m_est = float(comparison["M_estimated"])
    m_true = float(comparison["M_true"])
    true_lambdas = {
        branch: math.exp(-float(branch_report["branches"][branch]["Delta"]) * m_true / m_est)
        for branch in ("U", "D", "E")
    }
    pi0_true_reconstructed = 3.0 * true_lambdas["U"] + 3.0 * true_lambdas["D"] + true_lambdas["E"]
    if abs(pi0_true - pi0_true_reconstructed) > 1e-11:
        raise OrderThresholdError("true-lambda reconstruction does not match disclosed Pi0_true")
    true_phase = solve_phase(
        float(bridge["alpha_order"]),
        float(bridge["beta_order"]),
        true_lambdas,
    )

    return {
        "schema": "order-vacuum-threshold-closure-report-v0.1",
        "status": phase["status"],
        "tier": "declared_finite_architecture / exact_bridge / calibrated_readout / finite_diagnostic",
        "mother_potential_bridge": bridge,
        "primitive_branch_source": {
            "status": branch_report["status"],
            "M_joint": branch_report["M_joint"],
            "Pi0": pi0,
            "lambdas": lambdas,
        },
        "phase": phase,
        "known_fixture_comparison": {
            "Pi0_true": pi0_true,
            "Pi0_estimated": pi0,
            "Pi0_relative_error": relative_error(pi0, pi0_true),
            "r_star_true": true_phase["r_star"],
            "r_star_estimated": phase["r_star"],
            "r_star_relative_error": relative_error(float(phase["r_star"]), float(true_phase["r_star"])),
            "radial_curvature_proxy_true": true_phase["radial_curvature_proxy"],
            "radial_curvature_proxy_estimated": phase["radial_curvature_proxy"],
            "radial_curvature_proxy_relative_error": relative_error(
                float(phase["radial_curvature_proxy"]),
                float(true_phase["radial_curvature_proxy"]),
            ),
        },
        "parameter_reduction": {
            "new_sm_sector_dials_before": ["alpha_order", "beta_order"],
            "new_sm_sector_dials_after": [],
            "removed_count_this_stage": 2,
            "inheritance": {
                "alpha_order": "mother_potential.a / 2",
                "beta_order": "mother_potential.b / 4",
            },
            "cumulative_operational_sm_subchain": "7 -> 0 new/fitted dials",
            "global_parameters_not_eliminated": ["mother_potential.a", "mother_potential.b"],
        },
        "falsifiability_note": {
            "min_possible_pi0_given_lambda_domain": 0.0,
            "alpha_order": float(bridge["alpha_order"]),
            "ordered_outcome_is_data_independent": float(bridge["alpha_order"]) < 0.0,
            "explanation": (
                "lambda_j in (0,1] forces Pi0 in (0,7]; since alpha_order=a/2=-0.5 on this "
                "stepper is below the unconditional lower bound of Pi0, Pi0>alpha_order holds "
                "for EVERY legitimate branch-tape input -- ORDERED_READY on this stepper is "
                "structurally guaranteed by the mother potential's sign, not evidence that the "
                "specific U/D/E branch data produced order. See "
                "test_alpha_order_is_below_pi0_unconditional_lower_bound."
            ),
        },
        "claim_boundary": [
            "the order-sector alpha and beta are not independent once r=x^2 and the mother potential are declared",
            "the fixture satisfies Pi0>alpha_order and therefore has a unique ordered minimum",
            "REQUIRED (2026-07-25 review): on THIS stepper, alpha_order=-0.5 is below Pi0's "
            "unconditional lower bound (0), so ORDERED_READY is structurally guaranteed "
            "regardless of the branch-tape data -- see falsifiability_note; do not cite this "
            "fixture's ORDERED_READY status as evidence the branch construction is predictive",
            "the radial curvature is a local architecture output, not a physical Higgs pole mass",
            "mother-potential coefficients a,b remain global declared/calibrated quantities",
            "no unrestricted-root or laboratory Standard-Model claim",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_fixture(), indent=2, sort_keys=True))
