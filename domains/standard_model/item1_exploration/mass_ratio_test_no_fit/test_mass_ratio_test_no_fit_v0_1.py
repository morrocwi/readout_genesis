#!/usr/bin/env python3
"""Regression and adversarial tests for the zero-fit mass-ratio test v0.1."""
from __future__ import annotations

import math
import unittest

from mass_ratio_test_no_fit_v0_1 import (
    MassRatioTestError,
    native_mass_ratio,
    physical_mass_ratio,
    run_fixture,
)


class MassRatioTestNoFitTests(unittest.TestCase):
    def test_native_ratio_refuses_nonpositive_inputs(self):
        with self.assertRaises(MassRatioTestError):
            native_mass_ratio(v_native=0.0, radial_curvature_proxy_native=6.0)
        with self.assertRaises(MassRatioTestError):
            native_mass_ratio(v_native=2.0, radial_curvature_proxy_native=-1.0)
        with self.assertRaises(MassRatioTestError):
            native_mass_ratio(v_native=math.nan, radial_curvature_proxy_native=6.0)

    def test_physical_ratio_matches_hand_computation(self):
        self.assertAlmostEqual(physical_mass_ratio(125.20, 246.0), 125.20 / 246.0, places=12)

    def test_ratio_is_algebraically_scale_invariant(self):
        """Core claim of this candidate: multiplying BOTH v_native and radial_curvature_proxy's
        sqrt by the same factor (equivalent to inserting any linear Lambda) must leave the ratio
        unchanged -- this is what makes the test zero-fit and what predicts the exact-match to
        the sibling Lambda-based candidate's relative error."""
        base = native_mass_ratio(v_native=2.7652689218262565, radial_curvature_proxy_native=6.005340238045337)
        scaled_v = 2.7652689218262565 * 88.96060634765863
        scaled_curv = 6.005340238045337 * (88.96060634765863 ** 2)  # curvature is mass-dim 2
        scaled = native_mass_ratio(v_native=scaled_v, radial_curvature_proxy_native=scaled_curv)
        self.assertAlmostEqual(base["ratio_native"], scaled["ratio_native"], places=9)

    def test_fixture_reproduces_the_sibling_candidates_relative_error_exactly(self):
        """Disclosed, expected result: this ratio test's relative_error must equal the sibling
        rd_to_gev_fit_calibrated_bridge_v0_1.py candidate's Higgs-mass relative_error (0.7413
        as of 2026-07-25) to high precision -- confirming the cancellation claim, not merely
        asserting a pass/fail in isolation."""
        report = run_fixture()
        comparison = report["comparison"]
        self.assertAlmostEqual(comparison["relative_error"], 0.7412543499708927, places=6)
        self.assertFalse(comparison["passes_5_percent_band"])
        self.assertIn("FAILS", comparison["honest_verdict"])

    def test_zero_fitted_parameters_disclosed(self):
        report = run_fixture()
        self.assertEqual(report["tier"], "finite_diagnostic")
        self.assertTrue(
            any("zero fitted/free parameters" in item for item in report["claim_boundary"])
        )


if __name__ == "__main__":
    unittest.main()
