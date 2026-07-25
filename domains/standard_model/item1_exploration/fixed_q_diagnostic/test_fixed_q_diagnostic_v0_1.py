"""Regression + fail-closed tests for the fixed q-diagnostic v0.1."""
import math
import unittest

from domains.standard_model.item1_exploration.fixed_q_diagnostic.fixed_q_diagnostic_v0_1 import (
    _evolve,
    cond_graph_operator,
    fixed_diagnostic_cond,
    old_diagnostic_logcond,
    run_fixture,
)


class TestFixedQDiagnostic(unittest.TestCase):
    def test_old_diagnostic_diverges_as_one_over_dt(self):
        # FACT L: step-product log-cond doubles per dt-halving at FIXED physical time.
        old = [old_diagnostic_logcond(15.0, dt, 1.0) for dt in (0.004, 0.002, 0.001, 0.0005)]
        self.assertTrue(all(v is not None for v in old))
        ratios = [old[i + 1] / old[i] for i in range(len(old) - 1)]
        self.assertTrue(all(r > 1.8 for r in ratios))          # ~2 => 1/dt divergence

    def test_fixed_diagnostic_converges(self):
        # FACT M: cond#(G[Theta(t)]) converges under dt-refinement.
        fixed = [fixed_diagnostic_cond(15.0, dt, 1.0) for dt in (0.004, 0.002, 0.001, 0.0005)]
        self.assertTrue(all(v is not None for v in fixed))
        self.assertLess(max(fixed) - min(fixed), 1e-3)         # dt-independent

    def test_theta_itself_converges(self):
        # the reason the fix works: Theta(t) is a convergent ODE solution.
        thetas = [_evolve(15.0, dt, 1.0, product=False) for dt in (0.004, 0.002, 0.001, 0.0005)]
        self.assertTrue(all(t is not None for t in thetas))
        self.assertLess(max(thetas) - min(thetas), 1e-4)

    def test_fixed_cond_is_small_for_confining_mechanism(self):
        # FACT N: correctly-read cond# stays O(1) -- the big ranges were the artifact.
        cond_max = max(
            cond_graph_operator(_evolve(15.0, 0.001, t, product=False))
            for t in (1.0, 2.0, 3.0, 4.0, 5.0)
        )
        self.assertLess(cond_max, 5.0)
        self.assertGreater(cond_max, 1.0)                      # non-trivial but small

    def test_cond_graph_operator_formula(self):
        # cond#(I+Theta*boost) = (1+|Theta|)/|1-|Theta||; peaks near |Theta|=1, ->1 far from it.
        self.assertAlmostEqual(cond_graph_operator(0.0), 1.0)
        self.assertAlmostEqual(cond_graph_operator(0.5), 1.5 / 0.5)      # 3.0
        self.assertAlmostEqual(cond_graph_operator(-0.5), 3.0)          # depends on |Theta|
        self.assertEqual(cond_graph_operator(1.0), float("inf"))        # singular crossing
        self.assertLess(cond_graph_operator(25.0), 1.1)                # large |Theta| -> ~1 again

    def test_fail_closed_on_bad_input(self):
        with self.assertRaises(ValueError):
            _evolve(0.0, 0.01, 1.0)
        with self.assertRaises(ValueError):
            _evolve(15.0, 0.0, 1.0)

    def test_report_records_the_fix(self):
        report = run_fixture()
        self.assertIn("COMPUTED", report["status"])
        self.assertIn("artifact", report["status"])
        # old diverges (values grow), fixed is dt-stable
        old_vals = list(report["old_diagnostic_logcond_t1_m15"].values())
        fixed_vals = list(report["fixed_diagnostic_cond_t1_m15"].values())
        self.assertGreater(max(old_vals), 3 * min(old_vals))       # divergent
        self.assertLess(max(fixed_vals) - min(fixed_vals), 1e-3)   # convergent


if __name__ == "__main__":
    unittest.main(verbosity=2)
