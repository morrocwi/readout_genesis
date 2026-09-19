#!/usr/bin/env python3
"""Regression and adversarial tests for the native causal-memory consistency test v0.1."""
from __future__ import annotations

import math
import unittest

from native_causal_memory_consistency_v0_1 import (
    CausalMemoryConsistencyError,
    mass_from_native_tau_c,
    native_tau_c,
    run_fixture,
)


class NativeCausalMemoryConsistencyTests(unittest.TestCase):
    def test_native_tau_c_matches_hand_computation(self):
        report = native_tau_c(m_joint=1.0004294772248, d_coefficient=0.3)
        self.assertAlmostEqual(report["tau_c_native"], 1.0004294772248 / 0.3, places=12)

    def test_native_tau_c_refuses_nonpositive_inputs(self):
        with self.assertRaises(CausalMemoryConsistencyError):
            native_tau_c(m_joint=0.0, d_coefficient=0.3)
        with self.assertRaises(CausalMemoryConsistencyError):
            native_tau_c(m_joint=1.0, d_coefficient=-0.1)
        with self.assertRaises(CausalMemoryConsistencyError):
            native_tau_c(m_joint=math.nan, d_coefficient=0.3)

    def test_mass_from_tau_c_refuses_nonpositive(self):
        with self.assertRaises(CausalMemoryConsistencyError):
            mass_from_native_tau_c(0.0)
        with self.assertRaises(CausalMemoryConsistencyError):
            mass_from_native_tau_c(-1.0)

    def test_mass_from_tau_c_matches_natural_units_formula(self):
        self.assertAlmostEqual(mass_from_native_tau_c(2.0), 0.25, places=12)
        self.assertAlmostEqual(mass_from_native_tau_c(3.3347649240826667),
                                1.0 / (2.0 * 3.3347649240826667), places=12)

    def test_fixture_reports_the_real_disclosed_outcome_honestly(self):
        """Real test result as of 2026-07-25: NOT consistent (ratio ~0.0612, ~94% deviation
        from unity). If a future upstream change (e.g. a different D, or a different
        radial_curvature_proxy) causes this to become consistent, update the asserted numbers --
        do not delete this test or silently loosen its tolerance to force a pass."""
        report = run_fixture()
        check = report["consistency_check"]
        self.assertGreater(check["ratio_tau_c_mass_over_curvature_mass"], 0.0)
        self.assertFalse(check["consistent_within_5_percent"])
        self.assertIn("NOT CONSISTENT", check["honest_verdict"])
        self.assertGreater(check["relative_deviation_from_unity"], 0.5)

    def test_zero_external_physical_input_disclosed(self):
        report = run_fixture()
        self.assertEqual(report["tier"], "finite_diagnostic")
        self.assertTrue(
            any("zero external physical inputs" in item for item in report["claim_boundary"])
        )
        # confirm no GeV-scale magic numbers anywhere in the report values themselves
        flat_values = [
            report["tau_c_side"]["M_joint"], report["tau_c_side"]["D"],
            report["tau_c_side"]["tau_c_native"], report["tau_c_side"]["m_from_tau_c_native"],
            report["curvature_side"]["radial_curvature_proxy_native"],
            report["curvature_side"]["m_higgs_native"],
        ]
        self.assertTrue(all(v < 100.0 for v in flat_values))  # nothing GeV-scale (100s) sneaks in


if __name__ == "__main__":
    unittest.main()
