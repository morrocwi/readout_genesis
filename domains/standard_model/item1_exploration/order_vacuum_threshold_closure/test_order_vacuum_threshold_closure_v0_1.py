#!/usr/bin/env python3
"""Regression and adversarial tests for order-vacuum threshold closure v0.1."""
from __future__ import annotations

import math
import unittest

from order_vacuum_threshold_closure_v0_1 import (
    OrderThresholdError,
    derive_order_coefficients,
    run_fixture,
    solve_phase,
)


class DummyStepper:
    a = -1.0
    b = 1.0


class OrderVacuumThresholdClosureTests(unittest.TestCase):
    def test_exact_mother_potential_bridge(self):
        bridge = derive_order_coefficients(DummyStepper())
        self.assertEqual(bridge["alpha_order"], -0.5)
        self.assertEqual(bridge["beta_order"], 0.25)
        self.assertEqual(bridge["status"], "INHERITED_NOT_NEW_DIALS")

    def test_fixture_is_ordered_and_accurate(self):
        report = run_fixture()
        self.assertEqual(report["status"], "ORDERED_READY")
        phase = report["phase"]
        self.assertGreater(phase["order_margin"], 6.0)
        self.assertGreater(phase["r_star"], 0.0)
        self.assertLess(abs(phase["r_star"] - 3.823356105009073), 1e-10)
        comparison = report["known_fixture_comparison"]
        self.assertLess(comparison["Pi0_relative_error"], 1e-4)
        self.assertLess(comparison["r_star_relative_error"], 1e-4)
        self.assertLess(comparison["radial_curvature_proxy_relative_error"], 1e-4)
        reduction = report["parameter_reduction"]
        self.assertEqual(reduction["removed_count_this_stage"], 2)
        self.assertEqual(reduction["cumulative_operational_sm_subchain"], "7 -> 0 new/fitted dials")

    def test_unordered_control(self):
        lambdas = {"U": 0.1, "D": 0.1, "E": 0.1}
        report = solve_phase(alpha=1.0, beta=0.25, lambdas=lambdas)
        self.assertEqual(report["status"], "UNORDERED_READY")
        self.assertEqual(report["r_star"], 0.0)
        self.assertLessEqual(report["order_margin"], 0.0)

    def test_nonconvex_bare_potential_fails_closed(self):
        class BadStepper:
            a = -1.0
            b = 0.0

        with self.assertRaises(OrderThresholdError):
            derive_order_coefficients(BadStepper())

    def test_invalid_lambda_fails_closed(self):
        with self.assertRaises((OrderThresholdError, ValueError, ZeroDivisionError)):
            solve_phase(-0.5, 0.25, {"U": math.nan, "D": 0.8, "E": 0.7})


if __name__ == "__main__":
    unittest.main()
