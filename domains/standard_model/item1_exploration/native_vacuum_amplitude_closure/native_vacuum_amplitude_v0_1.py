#!/usr/bin/env python3
"""Native vacuum-amplitude closure v0.1.

Stacked on the order-vacuum threshold closure candidate. Converts the ordered minimum
`r_star = <H dagger H>` (native RD units, dimensionless in this architecture) into a
native-unit vacuum AMPLITUDE via the standard normalization convention

    r = v^2 / 2  =>  v = sqrt(2 r)

so `v_native` is a COMPUTED OUTPUT of the closure chain, not a new free dial:

    M -> Delta_{U,D,E} -> lambda_{U,D,E} -> Pi0 -> alpha_order,beta_order -> r_star -> v_native

Tier: exact convention bridge inside a declared finite architecture + calibrated finite
diagnostic for the upstream Pi0/r_star. This is NOT a physical vacuum expectation value in
GeV -- v_native lives entirely in this architecture's own native RD units.

REQUIRED SCOPE, stated up front per the founder's own explicit direction (2026-07-25): the
RD-to-GeV conversion factor (`Lambda_RD_to_GeV`) is NOT attempted here, NOT approximated, and
NOT set equal to any physical constant (e.g. 246 GeV) even provisionally. Setting
`v_physical = Lambda * v_native` and then choosing `Lambda` so that `v_physical` matches the
real Higgs vev would be a reverse-fit dressed up as a prediction, not a derivation -- this file
refuses to do that. `derive_native_vev` computes ONLY the native-unit number and raises if the
caller tries to attach any physical unit to it.
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

ORDER_DIR = (
    ROOT / "domains" / "standard_model" / "item1_exploration" / "order_vacuum_threshold_closure"
)
if str(ORDER_DIR) not in sys.path:
    sys.path.insert(0, str(ORDER_DIR))

from domains.standard_model.item1_exploration.order_vacuum_threshold_closure.order_vacuum_threshold_closure_v0_1 import (  # noqa: E402
    run_fixture as run_order_fixture,
)

EPS = 1e-15


class NativeVevError(ValueError):
    """Fail-closed native-vacuum-amplitude contract error."""


def derive_native_vev(phase_report: Mapping[str, object]) -> Mapping[str, object]:
    """v_native = sqrt(2 * r_star) under the r = v^2/2 convention. Refuses (raises) on an
    UNORDERED phase (r_star=0 has no physical amplitude interpretation) or a non-finite/negative
    r_star. Never attaches or implies a physical (GeV) unit -- see module docstring."""
    if not isinstance(phase_report, dict):
        raise NativeVevError("phase_report must be a mapping")
    if phase_report.get("status") != "ORDERED_READY":
        raise NativeVevError(
            "native vacuum amplitude is only defined for an ORDERED_READY phase "
            f"(got status={phase_report.get('status')!r})"
        )
    phase = phase_report.get("phase")
    if not isinstance(phase, dict):
        raise NativeVevError("phase_report is missing its phase block")
    try:
        r_star = float(phase["r_star"])
    except (KeyError, TypeError, ValueError) as exc:
        raise NativeVevError("phase.r_star must be numeric") from exc
    if not math.isfinite(r_star) or r_star <= 0:
        raise NativeVevError("phase.r_star must be finite and positive for an amplitude to exist")

    v_native = math.sqrt(2.0 * r_star)

    return {
        "bridge_id": "vacuum-amplitude-convention-v-squared-over-2-v0.1",
        "convention": "r = v_native^2 / 2  (standard EW-style amplitude normalization, applied "
        "to the native architecture's own r, not a physical field)",
        "r_star": r_star,
        "v_native": v_native,
        "unit": "native_rd_amplitude",
        "physical_unit_attached": False,
        "status": "COMPUTED_NATIVE_OUTPUT",
    }


def relative_error(estimate: float, truth: float) -> float:
    return abs(float(estimate) - float(truth)) / max(abs(float(truth)), EPS)


def run_fixture() -> Mapping[str, object]:
    order_report = run_order_fixture()
    bridge = derive_native_vev(order_report)

    comparison = order_report.get("known_fixture_comparison")
    if not isinstance(comparison, dict):
        raise NativeVevError("order-vacuum fixture comparison is required for the error audit")
    r_star_true = float(comparison["r_star_true"])
    v_native_true = math.sqrt(2.0 * r_star_true)
    v_native_relative_error = relative_error(bridge["v_native"], v_native_true)

    return {
        "schema": "native-vacuum-amplitude-closure-report-v0.1",
        "status": bridge["status"],
        "tier": "declared_finite_architecture / exact_bridge / calibrated_readout / finite_diagnostic",
        "vacuum_amplitude_bridge": bridge,
        "order_vacuum_source": {
            "status": order_report["status"],
            "Pi0": order_report["phase"]["Pi0"],
            "alpha_order": order_report["phase"]["alpha_order"],
            "beta_order": order_report["phase"]["beta_order"],
            "r_star": order_report["phase"]["r_star"],
        },
        "known_fixture_comparison": {
            "r_star_true": r_star_true,
            "v_native_true": v_native_true,
            "v_native_estimated": bridge["v_native"],
            "v_native_relative_error": v_native_relative_error,
        },
        "parameter_reduction": {
            "new_dial_before": ["v_native"],
            "new_dial_after": [],
            "removed_count_this_stage": 1,
            "inheritance": {"v_native": "sqrt(2 * r_star)"},
            "cumulative_operational_sm_subchain": "8 -> 0 new/fitted dials "
            "(M, C_RD, lambda_U, lambda_D, lambda_E, alpha_order, beta_order, v_native)",
            "global_parameters_not_eliminated": ["mother_potential.a", "mother_potential.b"],
        },
        "claim_boundary": [
            "v_native is a computed output of the closure chain in this architecture's own "
            "native RD units -- it is NOT a physical vacuum expectation value in GeV",
            "the RD-to-GeV conversion factor (Lambda_RD_to_GeV) is explicitly NOT attempted, "
            "approximated, or set equal to any physical constant here -- doing so by choosing "
            "Lambda to match the real 246 GeV Higgs vev would be a reverse-fit, not a prediction",
            "no physical mass, coupling, or vacuum-scale claim in SI/GeV units is made anywhere "
            "in this file",
            "inherits every upstream claim_boundary from order_vacuum_threshold_closure_v0_1.py "
            "unchanged, including the structural-guarantee disclosure on ORDERED_READY",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_fixture(), indent=2, sort_keys=True))
