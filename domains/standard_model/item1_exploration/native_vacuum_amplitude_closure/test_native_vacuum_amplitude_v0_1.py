#!/usr/bin/env python3
"""Regression and adversarial tests for native vacuum-amplitude closure v0.1."""
from __future__ import annotations

import math
import unittest

from native_vacuum_amplitude_v0_1 import NativeVevError, derive_native_vev, run_fixture


class NativeVacuumAmplitudeTests(unittest.TestCase):
    def test_fixture_computes_expected_v_native(self):
        report = run_fixture()
        self.assertEqual(report["status"], "COMPUTED_NATIVE_OUTPUT")
        bridge = report["vacuum_amplitude_bridge"]
        self.assertAlmostEqual(bridge["v_native"], 2.7652689218262565, places=10)
        self.assertFalse(bridge["physical_unit_attached"])
        comparison = report["known_fixture_comparison"]
        self.assertLess(comparison["v_native_relative_error"], 1e-4)

    def test_v_native_matches_sqrt_2r_star_exactly(self):
        report = run_fixture()
        bridge = report["vacuum_amplitude_bridge"]
        self.assertAlmostEqual(
            bridge["v_native"], math.sqrt(2.0 * bridge["r_star"]), places=12
        )

    def test_unordered_phase_refuses_to_produce_an_amplitude(self):
        fake_unordered = {
            "status": "UNORDERED_READY",
            "phase": {"r_star": 0.0, "status": "UNORDERED_READY"},
        }
        with self.assertRaises(NativeVevError):
            derive_native_vev(fake_unordered)

    def test_nonpositive_r_star_refuses(self):
        fake = {"status": "ORDERED_READY", "phase": {"r_star": -1.0}}
        with self.assertRaises(NativeVevError):
            derive_native_vev(fake)

    def test_no_physical_unit_is_ever_attached(self):
        report = run_fixture()
        self.assertFalse(report["vacuum_amplitude_bridge"]["physical_unit_attached"])
        self.assertTrue(
            any("NOT a physical vacuum expectation value in GeV" in item
                for item in report["claim_boundary"])
        )
        self.assertTrue(
            any("Lambda_RD_to_GeV" in item and "NOT attempted" in item
                for item in report["claim_boundary"])
        )

    def test_malformed_report_fails_closed(self):
        with self.assertRaises(NativeVevError):
            derive_native_vev({"status": "ORDERED_READY"})  # missing phase block
        with self.assertRaises(NativeVevError):
            derive_native_vev("not a dict")


if __name__ == "__main__":
    unittest.main()
