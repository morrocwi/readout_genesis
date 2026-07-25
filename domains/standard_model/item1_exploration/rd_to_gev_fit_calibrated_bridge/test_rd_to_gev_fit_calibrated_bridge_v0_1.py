#!/usr/bin/env python3
"""Regression and adversarial tests for the RD-to-GeV fit_calibrated bridge v0.1."""
from __future__ import annotations

import math
import unittest

from rd_to_gev_fit_calibrated_bridge_v0_1 import (
    RdToGevBridgeError,
    derive_lambda_rd_to_gev,
    predict_higgs_mass_gev,
    run_fixture,
)


class RdToGevBridgeTests(unittest.TestCase):
    def test_lambda_is_defined_exactly_by_construction(self):
        report = derive_lambda_rd_to_gev(v_native=2.0, v_physical_gev=246.0)
        self.assertEqual(report["Lambda_RD_to_GeV"], 123.0)
        self.assertEqual(report["tier"], "fit_calibrated")
        # circularity check: Lambda * v_native must reproduce v_physical EXACTLY (it is a
        # definition, not independent evidence -- this test locks in that it stays a definition)
        self.assertAlmostEqual(report["Lambda_RD_to_GeV"] * 2.0, 246.0, places=10)

    def test_lambda_refuses_nonpositive_v_native(self):
        with self.assertRaises(RdToGevBridgeError):
            derive_lambda_rd_to_gev(v_native=0.0)
        with self.assertRaises(RdToGevBridgeError):
            derive_lambda_rd_to_gev(v_native=-1.0)
        with self.assertRaises(RdToGevBridgeError):
            derive_lambda_rd_to_gev(v_native=math.nan)

    def test_higgs_prediction_refuses_nonpositive_curvature(self):
        with self.assertRaises(RdToGevBridgeError):
            predict_higgs_mass_gev(lam=100.0, radial_curvature_proxy_native=0.0)
        with self.assertRaises(RdToGevBridgeError):
            predict_higgs_mass_gev(lam=100.0, radial_curvature_proxy_native=-5.0)

    def test_higgs_prediction_is_not_circular_with_lambda_fit(self):
        """Lambda is fit ONLY from v_native and v_physical_gev=246 -- confirm the Higgs
        prediction changes when radial_curvature_proxy changes, with Lambda held fixed, proving
        the two computations are genuinely independent (radial_curvature_proxy plays no role in
        fitting Lambda)."""
        lam = derive_lambda_rd_to_gev(v_native=2.7652689218262565)["Lambda_RD_to_GeV"]
        low = predict_higgs_mass_gev(lam, radial_curvature_proxy_native=1.0)
        high = predict_higgs_mass_gev(lam, radial_curvature_proxy_native=100.0)
        self.assertNotEqual(low["m_higgs_predicted_gev"], high["m_higgs_predicted_gev"])
        self.assertAlmostEqual(
            high["m_higgs_predicted_gev"] / low["m_higgs_predicted_gev"], 10.0, places=8
        )  # sqrt(100/1) = 10, confirming the sqrt relation, not a fitted/tuned ratio

    def test_fixture_reports_the_real_disclosed_outcome_honestly(self):
        """This is a REAL test result, not a fixture of convenience -- it must report whatever
        this construction actually produces, whether that is a pass or a fail. As of this
        candidate's own disclosed run: FAILS the 5% band (predicted ~218 GeV vs real 125.20 GeV).
        If a future upstream change causes this to start passing, update this test's asserted
        numbers and honest_verdict expectation to match -- do not delete the test."""
        report = run_fixture()
        comparison = report["higgs_mass_comparison"]
        self.assertGreater(comparison["m_higgs_predicted_gev"], 0.0)
        self.assertEqual(comparison["m_higgs_physical_gev_pdg2024"], 125.20)
        # disclosed as of 2026-07-25: this does NOT match real physics within 5%
        self.assertFalse(comparison["passes_5_percent_band"])
        self.assertIn("FAILS", comparison["honest_verdict"])
        self.assertGreater(comparison["relative_error"], 0.05)

    def test_lambda_bridge_discloses_its_own_circularity(self):
        report = run_fixture()
        self.assertIn("circular", report["lambda_bridge"]["circularity_note"].lower())
        self.assertTrue(
            any("would be circular" in item for item in report["claim_boundary"])
        )


if __name__ == "__main__":
    unittest.main()
