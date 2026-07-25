#!/usr/bin/env python3
"""Executable U/D/E primitive-branch parameter-reduction fixture v0.1."""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
OPERATIONAL_DIR = ROOT / "domains" / "standard_model" / "item1_exploration" / "retained_transition_operational_closure"
if str(OPERATIONAL_DIR) not in sys.path:
    sys.path.insert(0, str(OPERATIONAL_DIR))

from domains.standard_model.item1_exploration.primitive_branch_parameter_reduction.primitive_branch_parameter_reduction_v0_1 import analyze  # noqa: E402
from domains.standard_model.item1_exploration.retained_transition_operational_closure.operational_exchange_closure_v0_1 import (  # noqa: E402
    load_stepper,
    run_fixture as run_operational_fixture,
)

N_STEPS = 200
SIGMA = 1e-5
SEED = 20260725
CALIBRATION_ID = "rtm-operational-closure-v0.1:sigma-1e-5:seeds-20260725-20260726"

BRANCH_INITIAL_CONDITIONS = {
    "U": (0.2, 0.201, -0.2, -0.201),
    "D": (0.5, 0.502, -0.5, -0.502),
    "E": (0.8, 0.801, -0.8, -0.801),
}


def simulate_branch(stepper, initial, n_steps=N_STEPS):
    phi0, phi1, psi0, psi1 = initial
    phi = np.zeros(n_steps)
    psi = np.zeros(n_steps)
    phi[0], phi[1] = phi0, phi1
    psi[0], psi[1] = psi0, psi1
    for n in range(1, n_steps - 1):
        phi[n + 1] = stepper.step_reader(phi[n], phi[n - 1])
        psi[n + 1] = stepper.step_record(psi[n], psi[n - 1], phi[n])
    if not np.all(np.isfinite(phi)) or not np.all(np.isfinite(psi)):
        raise FloatingPointError("branch simulation produced nonfinite values")
    return phi, psi


def build_payload():
    stepper = load_stepper()
    calibration = run_operational_fixture(sigma=SIGMA, seed=SEED)
    selected = calibration["selected_joint"]
    if selected["status"] != "CALIBRATED_READY" or selected["M_joint"] is None:
        raise RuntimeError("operational M calibration did not close")

    times = (np.arange(N_STEPS) * stepper.dt).tolist()
    branches = []
    for branch, initial in BRANCH_INITIAL_CONDITIONS.items():
        phi, psi = simulate_branch(stepper, initial)
        branches.append({
            "branch": branch,
            "path_semantics": "primitive_closure",
            "delta_is_dimensionless": True,
            "provenance": {
                "path_id": f"fixture-{branch}-primitive-200",
                "source_id": "attempt1-bateman-reader-record-stepper-v1",
                "adapter_id": "primitive-branch-fixture-adapter-v0.1",
                "calibration_id": CALIBRATION_ID,
                "initial_condition_id": f"fixture-{branch}-ic-{initial}",
            },
            "primitive_certificate": {
                "rule_id": "maximal-uninterrupted-retained-path-v0.1",
                "no_internal_reset": True,
                "orientation_quotiented": True,
                "branch_encoding_tier": "declared_finite_architecture",
            },
            "times": times,
            "phi": phi.tolist(),
            "psi": psi.tolist(),
        })

    return {
        "schema": "primitive-branch-tape-set-v0.1",
        "native_unit": {
            "unit_id": "native-rd-v1",
            "cost_unit_rd": 1.0,
            "is_tunable": False,
        },
        "delta_is_dimensionless": True,
        "m_calibration": {
            "status": "CALIBRATED_READY",
            "M_joint": float(selected["M_joint"]),
            "calibration_id": CALIBRATION_ID,
            "method": "independent-replicate-IV preferred; moment-correction fallback",
        },
        "branches": branches,
    }, stepper


def relative_error(estimate, truth):
    return abs(float(estimate) - float(truth)) / max(abs(float(truth)), 1e-15)


def run_fixture():
    payload, stepper = build_payload()
    calibrated = analyze(payload)

    truth_payload = copy.deepcopy(payload)
    truth_payload["m_calibration"]["M_joint"] = float(stepper.M)
    truth_payload["m_calibration"]["calibration_id"] = CALIBRATION_ID
    truth = analyze(truth_payload)

    errors = {}
    for branch in ("U", "D", "E"):
        estimate = calibrated["branches"][branch]
        exact = truth["branches"][branch]
        errors[branch] = {
            "Delta_relative_error": relative_error(estimate["Delta"], exact["Delta"]),
            "lambda_relative_error": relative_error(estimate["lambda"], exact["lambda"]),
            "signed_exchange_relative_error": relative_error(
                estimate["signed_exchange_total_rd"], exact["signed_exchange_total_rd"]
            ),
        }

    calibrated["known_fixture_comparison"] = {
        "M_true": float(stepper.M),
        "M_estimated": float(calibrated["M_joint"]),
        "M_relative_error": relative_error(calibrated["M_joint"], stepper.M),
        "Pi0_true": float(truth["Pi0"]),
        "Pi0_estimated": float(calibrated["Pi0"]),
        "Pi0_relative_error": relative_error(calibrated["Pi0"], truth["Pi0"]),
        "branch_errors": errors,
    }
    return calibrated


if __name__ == "__main__":
    print(json.dumps(run_fixture(), indent=2, sort_keys=True))
