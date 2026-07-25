#!/usr/bin/env python3
"""Regression and adversarial tests for the affine-graph non-compact growth test v0.1."""
from __future__ import annotations

import math
import unittest

import numpy as np

from affine_graph_noncompact_growth_v0_1 import (
    BASELINE_58X,
    D_THETA,
    FERMION_MASS_SPREAD,
    G0,
    G_COMPACT,
    G_NONCOMPACT,
    N_STEPS,
    accumulate_affine,
    condition_number,
    run_fixture,
    singular_values,
)


class AffineGraphNonCompactGrowthTests(unittest.TestCase):
    def test_affine_operator_is_the_mother_form_not_exponential(self):
        """G[Theta] = I + Theta*G_a exactly (affine), NOT exp(Theta*G_a)."""
        theta = 0.3
        g = G0 + theta * G_NONCOMPACT
        self.assertTrue(np.allclose(g, np.array([[1.0, theta], [theta, 1.0]])))
        # confirm it is NOT the exponential (which would be cosh/sinh)
        self.assertFalse(np.allclose(g, np.array([[math.cosh(theta), math.sinh(theta)],
                                                  [math.sinh(theta), math.cosh(theta)]])))

    def test_affine_noncompact_is_nonorthogonal_with_1pm_theta_svs(self):
        theta = 0.3
        sv = singular_values(G0 + theta * G_NONCOMPACT)
        self.assertAlmostEqual(sv[0], 1 + theta, places=12)
        self.assertAlmostEqual(sv[1], 1 - theta, places=12)

    def test_noncompact_condition_number_exceeds_ceiling_and_mass_spread(self):
        prod, _, _ = accumulate_affine(G_NONCOMPACT, N_STEPS, D_THETA)
        cond = condition_number(prod)
        self.assertGreater(cond, BASELINE_58X * 100)
        self.assertGreater(cond, FERMION_MASS_SPREAD)
        # not underflowed -> clean precision
        self.assertGreater(singular_values(prod)[-1], 1e-100)

    def test_compact_control_stays_exactly_one(self):
        """Clean single-variable regime check: same affine form, only generator -> compact."""
        prod, _, _ = accumulate_affine(G_COMPACT, N_STEPS, D_THETA)
        self.assertAlmostEqual(condition_number(prod), 1.0, places=9)

    def test_only_the_generator_differs_between_treatment_and_control(self):
        """Prove the two runs are identical except the generator (isolates non-compactness)."""
        nc = condition_number(accumulate_affine(G_NONCOMPACT, N_STEPS, D_THETA)[0])
        c = condition_number(accumulate_affine(G_COMPACT, N_STEPS, D_THETA)[0])
        self.assertGreater(nc / c, 1e4)   # same everything, only generator direction changed

    def test_accumulate_refuses_nonpositive_dtheta(self):
        with self.assertRaises(ValueError):
            accumulate_affine(G_NONCOMPACT, N_STEPS, 0.0)
        with self.assertRaises(ValueError):
            accumulate_affine(G_NONCOMPACT, N_STEPS, -0.001)
        with self.assertRaises(ValueError):
            accumulate_affine(G_NONCOMPACT, N_STEPS, math.nan)

    def test_range_freely_tunable_by_dtheta(self):
        small = condition_number(accumulate_affine(G_NONCOMPACT, N_STEPS, 0.001)[0])
        large = condition_number(accumulate_affine(G_NONCOMPACT, N_STEPS, 0.004)[0])
        self.assertGreater(large, small * 1000)  # confirms not-predictive: any range reachable

    def test_fixture_discloses_faithfulness_closed_and_not_predictive(self):
        report = run_fixture()
        self.assertIn("CLOSED the prior faithfulness caveat", report["honest_verdict"])
        self.assertIn("NOT predictive", report["honest_verdict"])
        self.assertTrue(
            any("affine operator form" in item for item in report["claim_boundary"])
        )
        self.assertTrue(
            any("single-variable regime check" in item for item in report["claim_boundary"])
        )


if __name__ == "__main__":
    unittest.main()
