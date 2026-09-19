#!/usr/bin/env python3
"""RD-to-GeV fit_calibrated bridge v0.1, and an independent (non-circular) Higgs-mass test.

Stacked on the merged native vacuum-amplitude closure. Per the founder's own explicit direction
(2026-07-25, following this project's standing DEV-SM-001 "fit is fine, real SM fits ~19 values
too" precedent -- see item1_exploration/attempt17_r_fit_calibrated_v1.py for the prior instance of
this exact epistemic move): fits ONE physical-unit conversion factor `Lambda_RD_to_GeV` against
ONE known physical observable (the real electroweak vacuum expectation value, v=246 GeV), tagged
`fit_calibrated`, NOT claimed as a derivation.

*** CIRCULARITY, STATED PLAINLY: fitting Lambda from v=246 GeV and then "predicting" v=246 GeV
    back from Lambda would be entirely circular -- Lambda is DEFINED to make that true. This file
    never does that. The only thing Lambda is used for, after being fit, is converting a SEPARATE
    native-unit quantity (the radial-curvature proxy from the merged order-vacuum closure, already
    tagged there as "not a physical Higgs pole mass") into a predicted Higgs mass in GeV, and
    comparing it against the REAL, independently measured Higgs mass. That comparison was NEVER
    used to fit Lambda -- it is the actual, non-circular test of whether this construction's scale
    means anything physically. ***

Tier: fit_calibrated for Lambda_RD_to_GeV itself (a calibration, not a derivation, exactly like
r_U/r_D/r_E in Attempt 17). finite_diagnostic for the resulting Higgs-mass comparison -- a real
number is computed and compared, honestly, whichever way it comes out.
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

VEV_DIR = ROOT / "domains" / "standard_model" / "item1_exploration" / "native_vacuum_amplitude_closure"
ORDER_DIR = ROOT / "domains" / "standard_model" / "item1_exploration" / "order_vacuum_threshold_closure"
for directory in (VEV_DIR, ORDER_DIR):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from domains.standard_model.item1_exploration.native_vacuum_amplitude_closure.native_vacuum_amplitude_v0_1 import (  # noqa: E402
    run_fixture as run_vev_fixture,
)
from domains.standard_model.item1_exploration.order_vacuum_threshold_closure.order_vacuum_threshold_closure_v0_1 import (  # noqa: E402
    run_fixture as run_order_fixture,
)

EPS = 1e-15

# Real-world calibration input (external, not fit to anything in this construction):
# electroweak vacuum expectation value v = (sqrt(2) G_F)^-1/2, G_F=1.1663787e-5 GeV^-2 (CODATA
# 2022), matching the value already registered/used in electroweak_decoder_v0_3.py per
# docs/root/EQUATION_REGISTRY.md -- reused here, not re-derived.
V_PHYSICAL_GEV = 246.0

# Real-world comparison target (external, NEVER used to fit Lambda): Higgs boson mass, Particle
# Data Group 2024 combination, m_H = 125.20 GeV.
M_HIGGS_PHYSICAL_GEV = 125.20


class RdToGevBridgeError(ValueError):
    """Fail-closed RD-to-GeV bridge contract error."""


def derive_lambda_rd_to_gev(v_native: float, v_physical_gev: float = V_PHYSICAL_GEV) -> Mapping[str, object]:
    """Lambda = v_physical / v_native. This DEFINES Lambda -- it is a calibration against one
    external observable, not a derivation, and using it to reproduce v_physical again would be
    circular (see module docstring). Refuses on non-finite/non-positive v_native."""
    if not math.isfinite(v_native) or v_native <= 0:
        raise RdToGevBridgeError("v_native must be finite and positive")
    if not math.isfinite(v_physical_gev) or v_physical_gev <= 0:
        raise RdToGevBridgeError("v_physical_gev must be finite and positive")
    lam = v_physical_gev / v_native
    return {
        "bridge_id": "rd-to-gev-fit-calibrated-v0.1",
        "tier": "fit_calibrated",
        "v_native": v_native,
        "v_physical_gev_input": v_physical_gev,
        "Lambda_RD_to_GeV": lam,
        "status": "FIT_CALIBRATED_NOT_DERIVED",
        "circularity_note": "Lambda is DEFINED so that Lambda*v_native == v_physical_gev_input "
        "exactly -- using it to 're-predict' v_physical_gev_input is circular and must never be "
        "cited as evidence. The only valid use of Lambda downstream is converting a DIFFERENT "
        "native-unit quantity not used in this fit.",
    }


def predict_higgs_mass_gev(lam: float, radial_curvature_proxy_native: float) -> Mapping[str, object]:
    """m_Higgs_native := sqrt(radial_curvature_proxy) (mass-dimension quantity in native units,
    per order_vacuum_threshold_closure_v0_1.py's own m_sigma^2 = 2 r* V''(r*) identification --
    see intertwiner_order_vacuum_v1_13.py). m_Higgs_predicted_gev := Lambda * m_Higgs_native
    (Lambda converts one power of mass-dimension, same as it converts v). This is an INDEPENDENT,
    non-circular prediction -- radial_curvature_proxy was never used to fit Lambda."""
    if not math.isfinite(lam) or lam <= 0:
        raise RdToGevBridgeError("Lambda_RD_to_GeV must be finite and positive")
    if not math.isfinite(radial_curvature_proxy_native) or radial_curvature_proxy_native <= 0:
        raise RdToGevBridgeError("radial_curvature_proxy must be finite and positive "
                                  "(non-positive means no real Higgs-like mode exists)")
    m_higgs_native = math.sqrt(radial_curvature_proxy_native)
    m_higgs_predicted_gev = lam * m_higgs_native
    return {
        "radial_curvature_proxy_native": radial_curvature_proxy_native,
        "m_higgs_native": m_higgs_native,
        "m_higgs_predicted_gev": m_higgs_predicted_gev,
        "status": "COMPUTED_INDEPENDENT_PREDICTION",
    }


def run_fixture() -> Mapping[str, object]:
    vev_report = run_vev_fixture()
    v_native = vev_report["vacuum_amplitude_bridge"]["v_native"]
    # native_vacuum_amplitude_v0_1.py's own report does not carry radial_curvature_proxy --
    # pulled directly from the order-vacuum fixture it itself is built on, not assumed/duplicated.
    order_report = run_order_fixture()
    radial_curvature_proxy = order_report["phase"]["radial_curvature_proxy"]

    lam_report = derive_lambda_rd_to_gev(v_native)
    prediction = predict_higgs_mass_gev(lam_report["Lambda_RD_to_GeV"], radial_curvature_proxy)

    m_pred = prediction["m_higgs_predicted_gev"]
    relative_error = abs(m_pred - M_HIGGS_PHYSICAL_GEV) / M_HIGGS_PHYSICAL_GEV
    passes_5pct = relative_error < 0.05

    return {
        "schema": "rd-to-gev-fit-calibrated-bridge-report-v0.1",
        "status": "FIT_CALIBRATED_WITH_INDEPENDENT_TEST",
        "tier": "fit_calibrated (Lambda) / finite_diagnostic (Higgs-mass comparison)",
        "lambda_bridge": lam_report,
        "higgs_mass_prediction": prediction,
        "higgs_mass_comparison": {
            "m_higgs_physical_gev_pdg2024": M_HIGGS_PHYSICAL_GEV,
            "m_higgs_predicted_gev": m_pred,
            "relative_error": relative_error,
            "passes_5_percent_band": passes_5pct,
            "honest_verdict": (
                "PASSES a 5% band around the real Higgs mass -- a genuine, non-circular success"
                if passes_5pct else
                "FAILS a 5% band around the real Higgs mass -- the fitted scale does NOT "
                "reproduce the real Higgs mass from this construction's radial-curvature proxy. "
                "This is a real, disclosed negative result, not hidden or reframed."
            ),
        },
        "claim_boundary": [
            "Lambda_RD_to_GeV is fit_calibrated against v=246 GeV, exactly like r_U/r_D/r_E in "
            "Attempt 17 -- NOT a root-native derivation",
            "using Lambda to 're-predict' v=246 GeV would be circular and is never done or cited",
            "the Higgs-mass prediction uses radial_curvature_proxy, which was NEVER used to fit "
            "Lambda -- this specific comparison is the genuine, falsifiable test",
            "the honest_verdict field above reports whatever this test actually found, without "
            "softening a failure or inflating a pass",
            "inherits every upstream claim_boundary unchanged, including the ORDERED_READY "
            "structural-guarantee disclosure and the disclosed-arbitrary branch initial "
            "conditions -- a passing OR failing Higgs-mass test here does not change either of "
            "those upstream findings",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_fixture(), indent=2, sort_keys=True))
