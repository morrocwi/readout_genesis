#!/usr/bin/env python3
"""Regression and adversarial tests for the native branch-time lifetime bridge v0.1."""
from __future__ import annotations

import math
import unittest

from native_tau_c_lifetime_bridge_v0_1 import (
    LifetimeBridgeError,
    REAL_LIFETIMES_S,
    native_branch_times,
    run_fixture,
)


class NativeTauCLifetimeBridgeTests(unittest.TestCase):
    def test_native_branch_times_matches_hand_computation(self):
        out = native_branch_times({"U": 0.01, "D": 0.05, "E": 0.5}, t_traj=2.0)
        self.assertAlmostEqual(out["U"], 200.0, places=8)
        self.assertAlmostEqual(out["D"], 40.0, places=8)
        self.assertAlmostEqual(out["E"], 4.0, places=8)

    def test_native_branch_times_refuses_nonpositive_inputs(self):
        with self.assertRaises(LifetimeBridgeError):
            native_branch_times({"U": 0.0}, t_traj=2.0)
        with self.assertRaises(LifetimeBridgeError):
            native_branch_times({"U": -0.5}, t_traj=2.0)
        with self.assertRaises(LifetimeBridgeError):
            native_branch_times({"U": 0.5}, t_traj=0.0)
        with self.assertRaises(LifetimeBridgeError):
            native_branch_times({"U": math.nan}, t_traj=2.0)

    def test_5_real_lifetimes_present_spanning_wide_range(self):
        self.assertEqual(len(REAL_LIFETIMES_S), 5)
        self.assertLess(min(REAL_LIFETIMES_S.values()), 1e-10)
        self.assertGreater(max(REAL_LIFETIMES_S.values()), 100.0)

    def test_fixture_produces_15_rows_with_exactly_one_fit_row(self):
        report = run_fixture()
        rows = report["full_table_sorted_by_error"]
        self.assertEqual(len(rows), 15)
        fit_rows = [r for r in rows if r["used_for_fit"]]
        self.assertEqual(len(fit_rows), 1)
        self.assertAlmostEqual(fit_rows[0]["relative_error_pct"], 0.0, places=6)

    def test_honest_result_no_heldout_match_disclosed(self):
        """Real, disclosed result as of 2026-07-25: 0/14 held-out rows under 5%, only 4/14 under
        even 1000%. If a future upstream change ever produces a genuine held-out match, update
        this test's asserted numbers -- do not silently loosen it to force a pass."""
        report = run_fixture()
        self.assertEqual(report["n_held_out_rows"], 14)
        self.assertEqual(report["n_held_out_under_5_percent"], 0)
        self.assertEqual(report["n_held_out_under_1000_percent"], 4)

    def test_dynamic_range_argument_is_numerically_correct(self):
        report = run_fixture()
        native_span = max(report["tau_native_by_branch"].values()) / min(report["tau_native_by_branch"].values())
        real_span = max(REAL_LIFETIMES_S.values()) / min(REAL_LIFETIMES_S.values())
        # native span (~tens) is many orders of magnitude smaller than the real span (~1e21)
        self.assertLess(native_span, 1000.0)
        self.assertGreater(real_span, 1e14)


if __name__ == "__main__":
    unittest.main()
