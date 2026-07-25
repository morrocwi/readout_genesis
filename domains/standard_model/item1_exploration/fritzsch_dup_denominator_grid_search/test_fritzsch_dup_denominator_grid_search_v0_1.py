#!/usr/bin/env python3
"""Regression and adversarial tests for the Fritzsch D_up denominator grid search v0.1."""
from __future__ import annotations

import math
import unittest

from fritzsch_dup_denominator_grid_search_v0_1 import (
    DENOMINATORS,
    GridSearchError,
    TARGETS,
    native_mass_for_denominator,
    run_fixture,
)


class FritzschDupDenominatorGridSearchTests(unittest.TestCase):
    def test_all_6_quark_denominators_present(self):
        self.assertEqual(set(DENOMINATORS.keys()), {"u", "c", "t", "d", "s", "b"})

    def test_all_8_targets_present(self):
        self.assertEqual(len(TARGETS), 8)
        self.assertIn("Higgs", TARGETS)
        self.assertIn("v_EW", TARGETS)

    def test_native_mass_refuses_nonpositive_denominator(self):
        with self.assertRaises(GridSearchError):
            native_mass_for_denominator({"U": 0.5, "D": 0.5, "E": 0.5}, 0.0)
        with self.assertRaises(GridSearchError):
            native_mass_for_denominator({"U": 0.5, "D": 0.5, "E": 0.5}, -1.0)
        with self.assertRaises(GridSearchError):
            native_mass_for_denominator({"U": 0.5, "D": 0.5, "E": 0.5}, math.nan)

    def test_full_table_is_48_pairs_no_dropped_rows(self):
        report = run_fixture()
        self.assertEqual(report["n_total_pairs"], 48)
        self.assertEqual(len(report["full_table_sorted_by_error"]), 48)

    def test_table_is_sorted_ascending_by_error(self):
        report = run_fixture()
        errs = [r["relative_error_pct"] for r in report["full_table_sorted_by_error"]]
        self.assertEqual(errs, sorted(errs))

    def test_honest_result_no_subfivepercent_match(self):
        """Real, disclosed result as of 2026-07-25: 0/48 pairs under 5%. If a future change to
        upstream inputs (D_up, Lambda, or the branch lambdas) ever produces a sub-5% pair, this
        test should be updated to reflect that -- do not silently loosen it to force a pass."""
        report = run_fixture()
        self.assertEqual(report["n_pairs_under_5_percent"], 0)
        self.assertEqual(report["n_pairs_under_10_percent"], 2)
        self.assertAlmostEqual(report["best_pair"]["relative_error_pct"], 6.951945833845237, places=6)

    def test_claim_boundary_warns_against_isolated_citation(self):
        report = run_fixture()
        self.assertTrue(
            any("NEVER be quoted in isolation" in item for item in report["claim_boundary"])
        )


if __name__ == "__main__":
    unittest.main()
