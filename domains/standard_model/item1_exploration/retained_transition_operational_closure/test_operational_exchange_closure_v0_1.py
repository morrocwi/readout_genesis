#!/usr/bin/env python3
"""Regression tests for RTM operational closure candidate."""
import unittest

from operational_exchange_closure_v0_1 import run_fixture


class OperationalClosureTests(unittest.TestCase):
    def test_low_and_medium_noise_close(self):
        for sigma in (2e-6, 1e-5):
            report = run_fixture(sigma=sigma)
            self.assertEqual(report["selected_joint"]["status"], "CALIBRATED_READY")
            m = report["selected_joint"]["M_joint"]
            self.assertIsNotNone(m)
            self.assertLess(abs(m - 1.0), 0.05)

    def test_high_noise_reader_fails_closed(self):
        report = run_fixture(sigma=1e-4)
        reader = report["moment_corrected"]["reader"]
        self.assertEqual(reader["status"], "UNRESOLVED")
        selected = report["selected_joint"]
        if selected["status"] == "CALIBRATED_READY":
            self.assertLess(abs(selected["M_joint"] - 1.0), 0.05)

    def test_observed_trajectory_does_not_emit_lambda(self):
        report = run_fixture(sigma=1e-5)
        path = report["path_diagnostic"]
        self.assertIsNotNone(path)
        self.assertEqual(path["status"], "DIAGNOSTIC_ONLY")
        self.assertIsNone(path["lambda"])


if __name__ == "__main__":
    unittest.main()
