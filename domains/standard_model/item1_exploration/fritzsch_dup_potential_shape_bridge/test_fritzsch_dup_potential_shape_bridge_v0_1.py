#!/usr/bin/env python3
"""Regression and adversarial tests for the Fritzsch D_up potential-shape bridge v0.1."""
from __future__ import annotations

import math
import unittest

from fritzsch_dup_potential_shape_bridge_v0_1 import (
    FritzschBridgeError,
    D_UP_GEV,
    M_C_GEV,
    derive_b_new,
    run_fixture,
)


class FritzschDupPotentialShapeBridgeTests(unittest.TestCase):
    def test_D_up_and_m_c_match_their_sourced_values(self):
        self.assertAlmostEqual(D_UP_GEV, 5.5200, places=4)
        self.assertAlmostEqual(M_C_GEV, 1.27, places=4)

    def test_b_new_matches_hand_computation(self):
        bridge = derive_b_new()
        self.assertAlmostEqual(bridge["b_new"], D_UP_GEV / M_C_GEV, places=12)
        self.assertEqual(bridge["status"], "MODELING_CHOICE_NOT_DERIVED")

    def test_derive_b_new_refuses_nonpositive_inputs(self):
        with self.assertRaises(FritzschBridgeError):
            derive_b_new(d_up_gev=0.0)
        with self.assertRaises(FritzschBridgeError):
            derive_b_new(d_up_gev=-1.0)
        with self.assertRaises(FritzschBridgeError):
            derive_b_new(m_c_gev=math.nan)

    def test_fixture_produces_a_different_nontrivial_r_star(self):
        report = run_fixture()
        comparison = report["comparison"]
        # real, disclosed result as of 2026-07-25: r_star shrinks to ~38.5% of baseline
        self.assertLess(comparison["r_star_ratio"], 1.0)
        self.assertGreater(comparison["r_star_ratio"], 0.0)
        self.assertAlmostEqual(comparison["r_star_ratio"], 0.3846467276691078, places=8)
        self.assertGreater(report["experiment_phase"]["r_star"], 0.0)
        self.assertEqual(report["experiment_phase"]["status"], "ORDERED_READY")

    def test_alpha_order_unchanged_by_this_experiment(self):
        report = run_fixture()
        self.assertEqual(report["baseline_phase"]["alpha_order"], report["experiment_phase"]["alpha_order"])

    def test_regime_check_disclosed_not_identifying_Dup_with_M(self):
        report = run_fixture()
        self.assertTrue(
            any("does NOT identify D_up with M" in item for item in report["claim_boundary"])
        )
        self.assertTrue(
            any("MODELING CHOICE, not a derivation" in item for item in report["claim_boundary"])
        )


if __name__ == "__main__":
    unittest.main()
