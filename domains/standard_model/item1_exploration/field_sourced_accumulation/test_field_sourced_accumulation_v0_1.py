#!/usr/bin/env python3
"""Regression and adversarial tests for the field-sourced accumulation test v0.1 (NEGATIVE result)."""
from __future__ import annotations

import math
import unittest

import numpy as np

from field_sourced_accumulation_v0_1 import (
    FIELD_ICS,
    G_COMPACT,
    G_NONCOMPACT,
    M_THETA_SWEEP,
    condition_number,
    run_coupled,
    run_fixture,
)


class FieldSourcedAccumulationTests(unittest.TestCase):
    def test_hierarchy_is_strongly_sensitive_to_graph_constant_M_theta(self):
        """Computed fact (not a works/fails judgment): the hierarchy is strongly sensitive to the
        graph constant M_Theta -- sweeping it moves the output by many orders of magnitude. This is
        a measured sensitivity; M_Theta is a consequential constant OF the graph that would need
        calibrating to pin a specific hierarchy."""
        ic = FIELD_ICS[0]
        conds = [run_coupled(ic["phi0"], ic["psi0"], G_NONCOMPACT, m_theta=mth)[1]
                 for mth in M_THETA_SWEEP]
        self.assertGreater(max(conds) / min(conds), 1e6)   # spans >6 orders of magnitude

    def test_result_also_depends_on_field_ics(self):
        conds = [run_coupled(ic["phi0"], ic["psi0"], G_NONCOMPACT)[1] for ic in FIELD_ICS]
        self.assertGreater(max(conds) / min(conds), 5.0)

    def test_compact_control_stays_one(self):
        for ic in FIELD_ICS[:2]:
            _, mc = run_coupled(ic["phi0"], ic["psi0"], G_COMPACT)
            self.assertAlmostEqual(mc, 1.0, places=6)

    def test_theta_accumulates_via_source(self):
        for ic in FIELD_ICS:
            tf, _ = run_coupled(ic["phi0"], ic["psi0"], G_NONCOMPACT)
            self.assertGreater(abs(tf), 1e-6)

    def test_condition_number_helper_is_sane(self):
        self.assertAlmostEqual(condition_number(np.eye(2)), 1.0, places=12)
        self.assertAlmostEqual(condition_number(np.diag([3.0, 1.0])), 3.0, places=12)

    def test_faithful_record_term_is_grad2v_not_gradv(self):
        """Physics fidelity (review-required): the Record term must be grad2V(phi)*psi, not
        grad_v(psi). Confirm the module computes grad2V = a + 3b*phi^2 correctly."""
        from field_sourced_accumulation_v0_1 import grad2_v, grad_v, A_POT, B_POT
        x = 0.7
        self.assertAlmostEqual(grad2_v(x), A_POT + 3.0 * B_POT * x ** 2, places=12)
        self.assertNotAlmostEqual(grad2_v(x), grad_v(x), places=6)  # genuinely different terms

    def test_fixture_reports_computed_facts_not_a_works_fails_verdict(self):
        report = run_fixture()
        # per-step free theta is genuinely gone, but the parameter COUNT is not reduced -- both facts
        self.assertEqual(report["per_step_free_theta_removed"], True)
        self.assertEqual(report["free_parameter_count_reduced"], False)
        # neutral, computation-focused framing (no materialist works/fails label)
        self.assertIn("COMPUTED", report["honest_verdict"].upper())
        self.assertIn("READOUT", report["honest_verdict"].upper())
        # the framework-native reading (masses are names/readouts on the one graph) is disclosed
        self.assertTrue(
            any("constants of the one graph" in item.lower() or "constants OF the one graph" in item
                for item in report["claim_boundary"])
        )
        self.assertTrue(
            any("legitimately calibratable" in item.lower() or "fit_calibrated status" in item
                for item in report["claim_boundary"])
        )


if __name__ == "__main__":
    unittest.main()
