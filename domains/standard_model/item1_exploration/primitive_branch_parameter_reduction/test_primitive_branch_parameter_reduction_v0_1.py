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

    def test_parameter_reduction_scope_is_disclosed(self):
        """Required correction (2026-07-25 review): 'after_count=0' must not be read as 'zero
        remaining degrees of freedom' -- the report must disclose where the freedom relocated."""
        reduction = self.report["parameter_reduction"]
        self.assertIn("relocated_not_eliminated", reduction)
        self.assertTrue(len(reduction["relocated_not_eliminated"]) >= 1)
        self.assertTrue(
            any("initial condition" in item for item in reduction["relocated_not_eliminated"])
        )
        self.assertTrue(
            any("self-declared" in item and "not independently verified" in item.lower()
                for item in self.report["claim_boundary"])
        )

    def test_self_declared_certificate_is_not_cross_verified_against_trajectory(self):
        """Required correction (2026-07-25 review), documented not silently patched: a SUBTLE
        internal discontinuity ('reset') still passes validate_payload as long as its
        primitive_certificate asserts no_internal_reset=True -- the gate checks the DECLARATION,
        not the DATA. (A GROSS discontinuity happens to be caught incidentally by the unrelated
        segmentation-invariance gate -- confirmed separately, factor>=1.01 on this fixture is
        rejected; this test deliberately uses a subtle 0.1% single-sample perturbation, factor
        1.001, that stays under that gate's 1% threshold, to isolate the actual certificate gap
        from the segmentation gate's incidental, coarser catch.) This test locks in that known,
        disclosed limitation so a future change cannot silently narrow or widen it without this
        test noticing; it does NOT assert this is acceptable, only that it is accurately
        documented."""
        tampered = copy.deepcopy(self.payload)
        phi = tampered["branches"][0]["phi"]
        mid = len(phi) // 2
        phi[mid] = phi[mid] * 1.001
        tampered["branches"][0]["phi"] = phi
        # certificate still (falsely) asserts no reset occurred -- unchanged from the original
        self.assertTrue(tampered["branches"][0]["primitive_certificate"]["no_internal_reset"])
        try:
            analyze(tampered)
        except ContractError:
            self.fail(
                "validate_payload rejected a falsely-certified, subtly-tampered tape -- if this "
                "now fails, the self-certification gap has been closed (good!) and this test, "
                "plus the SELF_DECLARED_UNVERIFIED_CERTIFICATE_FIELDS disclosure, should be "
                "updated to match the new, stronger behavior instead of being deleted."
            )


if __name__ == "__main__":
    unittest.main()
