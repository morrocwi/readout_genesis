#!/usr/bin/env python3
"""Mass-ratio test, zero fitted parameters, v0.1.

Stacked on the merged order-vacuum threshold closure + native vacuum-amplitude closure. Per the
project's own information-philosophy stance on mass (`engine.lexicon.stance_for("mass")`,
`engine/tau_c.py`): mass is not fundamental, it is a READOUT of causal-memory time
(`m=hbar/(2 c^2 tau_c)`), and the framework's actual machine-checked (Th_coqc) claim is that MASS
RATIOS equal spectral-gap RATIOS of L_R -- absolute mass in physical units (GeV) is explicitly
`[Open]` in that same stance, requiring an externally-measured tau_c the framework does not derive.

This candidate follows that guidance directly: it tests the RATIO `m_higgs_native / v_native`
against the REAL ratio `m_Higgs_physical / v_physical` (both PDG-style external inputs), WITHOUT
introducing `Lambda_RD_to_GeV` or any other fitted conversion factor at all. This is a STRICTLY
CLEANER test than rd_to_gev_fit_calibrated_bridge_v0_1.py (the prior, sibling candidate): zero
free/fitted parameters appear anywhere in this file.

*** EXPECTED, DISCLOSED ALGEBRAIC FACT: because `Lambda_RD_to_GeV` (had it been introduced) would
    cancel exactly out of this ratio (`Lambda*m_higgs_native / Lambda*v_native ==
    m_higgs_native/v_native`), this test's relative error is MATHEMATICALLY IDENTICAL to the
    sibling candidate's Higgs-mass relative error (74.13%). This is not a new independent failure
    -- it is the SAME underlying discrepancy, now demonstrated via a route that needs no fitted
    input at all, confirming the earlier finding was not an artifact of a badly-chosen Lambda. ***

Tier: finite_diagnostic throughout -- no fit_calibrated tag needed anywhere in this file, since
there is nothing fitted.
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

# Real-world inputs (external, not fit to anything in this construction). Same sourcing as the
# sibling candidate rd_to_gev_fit_calibrated_bridge_v0_1.py -- reused, not re-derived.
V_PHYSICAL_GEV = 246.0
M_HIGGS_PHYSICAL_GEV = 125.20


class MassRatioTestError(ValueError):
    """Fail-closed mass-ratio-test contract error."""


def native_mass_ratio(v_native: float, radial_curvature_proxy_native: float) -> Mapping[str, object]:
    """m_higgs_native/v_native, both computed from the same declared architecture, no fitted
    conversion factor involved anywhere. Refuses on non-finite/non-positive inputs."""
    if not math.isfinite(v_native) or v_native <= 0:
        raise MassRatioTestError("v_native must be finite and positive")
    if not math.isfinite(radial_curvature_proxy_native) or radial_curvature_proxy_native <= 0:
        raise MassRatioTestError("radial_curvature_proxy must be finite and positive")
    m_higgs_native = math.sqrt(radial_curvature_proxy_native)
    ratio = m_higgs_native / v_native
    return {
        "m_higgs_native": m_higgs_native,
        "v_native": v_native,
        "ratio_native": ratio,
    }


def physical_mass_ratio(m_higgs_gev: float = M_HIGGS_PHYSICAL_GEV,
                         v_gev: float = V_PHYSICAL_GEV) -> float:
    if not math.isfinite(m_higgs_gev) or m_higgs_gev <= 0:
        raise MassRatioTestError("m_higgs_gev must be finite and positive")
    if not math.isfinite(v_gev) or v_gev <= 0:
        raise MassRatioTestError("v_gev must be finite and positive")
    return m_higgs_gev / v_gev


def run_fixture() -> Mapping[str, object]:
    vev_report = run_vev_fixture()
    v_native = vev_report["vacuum_amplitude_bridge"]["v_native"]
    order_report = run_order_fixture()
    radial_curvature_proxy = order_report["phase"]["radial_curvature_proxy"]

    native = native_mass_ratio(v_native, radial_curvature_proxy)
    ratio_physical = physical_mass_ratio()
    ratio_native = native["ratio_native"]

    relative_error = abs(ratio_native - ratio_physical) / ratio_physical
    passes_5pct = relative_error < 0.05

    return {
        "schema": "mass-ratio-test-no-fit-report-v0.1",
        "status": "COMPUTED_ZERO_FIT_TEST",
        "tier": "finite_diagnostic",
        "native_ratio": native,
        "physical_ratio": {
            "m_higgs_physical_gev_pdg2024": M_HIGGS_PHYSICAL_GEV,
            "v_physical_gev": V_PHYSICAL_GEV,
            "ratio_physical": ratio_physical,
        },
        "comparison": {
            "ratio_native": ratio_native,
            "ratio_physical": ratio_physical,
            "relative_error": relative_error,
            "passes_5_percent_band": passes_5pct,
            "honest_verdict": (
                "PASSES a 5% band -- a genuine, zero-fitted-parameter success"
                if passes_5pct else
                "FAILS a 5% band -- the native construction's mass ratio does NOT reproduce the "
                "real Higgs/vev ratio. Algebraically identical discrepancy (74.13%) to the "
                "sibling rd_to_gev_fit_calibrated_bridge_v0_1.py candidate's absolute-GeV test, "
                "as expected since any linear conversion factor cancels exactly in a ratio -- "
                "this confirms the earlier failure was a real discrepancy, not an artifact of "
                "the particular Lambda chosen there."
            ),
        },
        "claim_boundary": [
            "zero fitted/free parameters appear anywhere in this file -- this is a stricter test "
            "than the sibling Lambda-based candidate, not a looser one",
            "the numeric relative_error is expected, by algebra, to equal the sibling candidate's "
            "Higgs-mass relative error exactly -- this is disclosed as a mathematical fact, not "
            "presented as new independent confirmation of failure",
            "per this project's own mass philosophy (engine.lexicon.stance_for('mass')), the "
            "framework's actual proven (Th_coqc) claim is about RATIOS via spectral-gap ratios of "
            "L_R -- absolute GeV scale remains explicitly Open even in the framework's own "
            "established tau_c-based machinery (engine/tau_c.py, mass_from_tau_c)",
            "does not establish which native mode (if any) genuinely corresponds to the physical "
            "Higgs boson -- that particle-to-mode mapping is explicitly named as Open by the "
            "framework's own mass stance, independent of this specific numeric result",
            "inherits every upstream claim_boundary unchanged, including the ORDERED_READY "
            "structural-guarantee disclosure and the disclosed-arbitrary branch initial "
            "conditions",
            "REQUIRED SCOPE (independent review, 2026-07-25): \"zero fitted parameters\" is "
            "scoped to THIS file only -- M itself is a calibrated/fitted quantity upstream "
            "(the merged RTM operational closure requires m_calibration.status == "
            "CALIBRATED_READY and an M_joint estimate before anything downstream, including "
            "v_native and radial_curvature_proxy, can be computed). This file introduces no "
            "NEW fitted parameter on top of that, but the chain as a whole is not fit-free "
            "end-to-end.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_fixture(), indent=2, sort_keys=True))
