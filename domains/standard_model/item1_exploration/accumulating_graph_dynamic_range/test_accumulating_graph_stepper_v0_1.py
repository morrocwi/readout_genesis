#!/usr/bin/env python3
"""Regression and adversarial tests for the accumulating-graph dynamic-range test v0.1."""
from __future__ import annotations

import math
import unittest

from accumulating_graph_stepper_v0_1 import (
    BASELINE_58X,
    N_STEPS,
    THETA,
    boost,
    dynamic_range,
    rotation,
    run_fixture,
    run_frozen,
    run_harmonic,
    run_noncompact,
    run_rotation_control,
)


class AccumulatingGraphDynamicRangeTests(unittest.TestCase):
    def test_boost_is_the_so11_generator_exponential(self):
        B = boost(0.5)
        self.assertAlmostEqual(B[0][0], math.cosh(0.5), places=12)
        self.assertAlmostEqual(B[0][1], math.sinh(0.5), places=12)
        # Minkowski-preserving: B^T eta B = eta (genuine boost, not arbitrary matrix)
        import numpy as np
        eta = np.diag([1.0, -1.0])
        self.assertTrue(np.allclose(B.T @ eta @ B, eta))

    def test_frozen_mode_has_no_range(self):
        svs = run_frozen(N_STEPS)
        self.assertAlmostEqual(dynamic_range(svs), 1.0, places=9)

    def test_harmonic_control_stays_bounded(self):
        """A regime check: accumulation with a bounded potential does NOT unlock range."""
        svs = run_harmonic(N_STEPS)
        self.assertLess(dynamic_range(svs), 5.0)

    def test_rotation_control_is_the_clean_single_variable_regime_check(self):
        """The CLEAN control (added after review): IDENTICAL matrix-product accumulation to the
        non-compact mode, only the generator changed compact<->non-compact. Rotation (compact)
        must stay at exactly 1x while boost (non-compact) explodes -- isolating non-compactness as
        the single driver, holding the matrix-product scaffold fixed."""
        import numpy as np
        # rotation is genuinely compact/orthogonal
        R = rotation(0.3)
        self.assertTrue(np.allclose(R @ R.T, np.eye(2)))
        r_rot = dynamic_range(run_rotation_control(N_STEPS, THETA))
        r_boost = dynamic_range(run_noncompact(N_STEPS, THETA))
        self.assertAlmostEqual(r_rot, 1.0, places=9)          # compact -> no range, same scaffold
        self.assertGreater(r_boost, 1000.0)                   # non-compact -> huge range
        # the ONLY difference between the two runs is compact vs non-compact generator
        self.assertGreater(r_boost / r_rot, 1000.0)

    def test_rotation_control_refuses_nonpositive_theta(self):
        with self.assertRaises(ValueError):
            run_rotation_control(N_STEPS, 0.0)

    def test_noncompact_matches_closed_form_exactly(self):
        svs = run_noncompact(N_STEPS, THETA)
        closed = math.exp((N_STEPS - 1) * THETA)
        self.assertAlmostEqual(dynamic_range(svs) / closed, 1.0, places=9)

    def test_noncompact_strictly_exceeds_frozen_and_harmonic_and_baseline(self):
        """Core claim, measured not asserted: non-compact >> frozen, harmonic, and the 58x ceiling."""
        r_frozen = dynamic_range(run_frozen(N_STEPS))
        r_harmonic = dynamic_range(run_harmonic(N_STEPS))
        r_noncompact = dynamic_range(run_noncompact(N_STEPS, THETA))
        self.assertGreater(r_noncompact, r_frozen)
        self.assertGreater(r_noncompact, r_harmonic)
        self.assertGreater(r_noncompact, BASELINE_58X * 100)

    def test_noncompact_refuses_nonpositive_theta(self):
        with self.assertRaises(ValueError):
            run_noncompact(N_STEPS, 0.0)
        with self.assertRaises(ValueError):
            run_noncompact(N_STEPS, -0.1)
        with self.assertRaises(ValueError):
            run_noncompact(N_STEPS, math.nan)

    def test_range_is_freely_tunable_by_theta(self):
        """The honest double-edge: range scales with theta, so it is not predictive on its own."""
        small = dynamic_range(run_noncompact(N_STEPS, 0.02))
        large = dynamic_range(run_noncompact(N_STEPS, 0.1))
        self.assertGreater(large, small * 1000)  # 5x theta -> vastly larger range

    def test_fixture_reports_honest_not_predictive_caveat(self):
        report = run_fixture()
        self.assertIn("NOT yet predictive", report["honest_verdict"])
        self.assertTrue(
            any("necessary but NOT predictive" in item for item in report["claim_boundary"])
        )
        self.assertTrue(
            any("regime check" in item for item in report["claim_boundary"])
        )


if __name__ == "__main__":
    unittest.main()
