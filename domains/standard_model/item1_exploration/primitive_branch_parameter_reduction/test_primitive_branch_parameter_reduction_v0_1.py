#!/usr/bin/env python3
"""Regression tests for primitive-branch parameter reduction v0.1."""
from __future__ import annotations

import copy
import unittest

from primitive_branch_fixture_v0_1 import build_payload, run_fixture
from primitive_branch_parameter_reduction_v0_1 import ContractError, analyze


class PrimitiveBranchParameterReductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload, _ = build_payload()
        cls.report = run_fixture()

    def test_full_subchain_closes_and_removes_five_dials(self):
        report = self.report
        self.assertEqual(report["status"], "CALIBRATED_READY")
        self.assertEqual(report["native_unit"]["C_RD"], 1.0)
        self.assertEqual(report["native_unit"]["status"], "GAUGE_FIXED_NOT_TUNABLE")
        reduction = report["parameter_reduction"]
        self.assertEqual(reduction["before_count"], 5)
        self.assertEqual(reduction["after_count"], 0)
        self.assertEqual(set(report["branches"]), {"U", "D", "E"})

    def test_actual_fixture_accuracy_is_low_error(self):
        comparison = self.report["known_fixture_comparison"]
        self.assertLess(comparison["M_relative_error"], 5e-4)
        self.assertLess(comparison["Pi0_relative_error"], 5e-5)
        for branch, errors in comparison["branch_errors"].items():
            self.assertLess(errors["Delta_relative_error"], 5e-4, branch)
            self.assertLess(errors["signed_exchange_relative_error"], 5e-4, branch)
            self.assertLess(errors["lambda_relative_error"], 3e-4, branch)

    def test_branch_outputs_and_segmentation_gates(self):
        report = self.report
        self.assertAlmostEqual(report["Pi0"], 6.328453553371575, places=10)
        for branch in ("U", "D", "E"):
            item = report["branches"][branch]
            self.assertEqual(item["status"], "CALIBRATED_READY")
            self.assertGreater(item["lambda"], 0.0)
            self.assertLessEqual(item["lambda"], 1.0)
            self.assertLess(max(item["segmentation_relative_gap"].values()), 0.01)

    def test_native_cost_unit_cannot_be_tuned(self):
        bad = copy.deepcopy(self.payload)
        bad["native_unit"]["cost_unit_rd"] = 2.0
        with self.assertRaises(ContractError):
            analyze(bad)

    def test_observed_trajectory_cannot_masquerade_as_primitive(self):
        bad = copy.deepcopy(self.payload)
        bad["branches"][0]["path_semantics"] = "observed_trajectory"
        with self.assertRaises(ContractError):
            analyze(bad)

    def test_duplicate_branch_path_is_rejected(self):
        bad = copy.deepcopy(self.payload)
        bad["branches"][1]["provenance"]["path_id"] = bad["branches"][0]["provenance"]["path_id"]
        with self.assertRaises(ContractError):
            analyze(bad)

    def test_unresolved_M_cannot_enter_downstream_chain(self):
        bad = copy.deepcopy(self.payload)
        bad["m_calibration"]["status"] = "UNRESOLVED"
        with self.assertRaises(ContractError):
            analyze(bad)


if __name__ == "__main__":
    unittest.main()
