"""Regression + fail-closed tests for dynamic range from graph-operator degeneracy v0.1."""
import unittest

from domains.standard_model.item1_exploration.dynamic_range_from_degeneracy.dynamic_range_from_degeneracy_v0_1 import (  # noqa: E501
    cond_at,
    max_abs_theta,
    run_fixture,
)


class TestDynamicRangeFromDegeneracy(unittest.TestCase):
    def test_mechanism_reaches_degeneracy_convergently(self):
        # FACT O: at M_Theta=4 the accumulated Theta reaches ~0.985 (near |Theta|=1), dt-converged.
        m1 = max_abs_theta(4.0, 0.002, 8.0)
        m2 = max_abs_theta(4.0, 0.001, 8.0)
        self.assertGreater(m2, 0.9)                 # approaches the degeneracy
        self.assertLess(m2, 1.0)                    # stays on the approach side
        self.assertLess(abs(m1 - m2), 0.01)         # dt-converged

    def test_generation_condnums_are_convergent(self):
        # FACT O: the generation cond# values converge under dt-refinement (not a step artifact).
        for t in (4.0, 5.0, 6.0):
            row = [cond_at(4.0, dt, t) for dt in (0.002, 0.001, 0.0005)]
            self.assertLess(max(row) - min(row), 0.04)

    def test_large_convergent_condnum(self):
        # FACT O: reaches ~10^2, well above the ~1.2 confining floor.
        c6 = cond_at(4.0, 0.0005, 6.0)
        self.assertGreater(c6, 10.0)

    def test_hierarchy_sign_is_a_slicing_artifact(self):
        # FACT P (corrected): cond#(t) oscillates, so the accel/decel sign flips between adjacent
        # generation-time windows -- (4,5,6) ACCEL vs (5,6,7) DECEL. The sign is NOT a stable result.
        ct = {t: cond_at(4.0, 0.0005, float(t)) for t in range(3, 9)}
        def q(w):
            c = [ct[t] for t in w]
            return (c[2] / c[1]) / (c[1] / c[0])
        self.assertGreater(q((4, 5, 6)), 1.0)      # this window: ACCEL
        self.assertLess(q((5, 6, 7)), 1.0)         # adjacent window: DECEL -- opposite sign
        # so no single sign can be claimed from this lever

    def test_still_short_of_fermion_spread(self):
        # HONEST LIMIT (b): reaches ~10^2, NOT the ~10^5.5 fermion mass-ratio spread.
        c6 = cond_at(4.0, 0.0005, 6.0)
        self.assertLess(c6, 1e3)

    def test_fine_tuned_near_singularity(self):
        # HONEST LIMIT (a): cond# swings by orders with small M_Theta changes near |Theta|=1.
        from domains.standard_model.item1_exploration.fixed_q_diagnostic.fixed_q_diagnostic_v0_1 import (
            cond_graph_operator,
        )
        c4 = cond_graph_operator(max_abs_theta(4.0, 0.001, 8.0))
        c2 = cond_graph_operator(max_abs_theta(2.0, 0.001, 8.0))
        self.assertGreater(c4 / c2, 10.0)           # big swing between M_Theta=4 and 2

    def test_report_is_constructive_with_named_limits(self):
        report = run_fixture()
        self.assertIn("COMPUTED", report["status"])
        self.assertIn("degeneracy", report["status"])
        self.assertIn("slicing_artifact", report["status"])          # sign is NOT stable
        self.assertGreater(report["condnum_over_time_m4"]["6"], 10.0)  # large convergent range (FACT O)
        # the sign flips across windows (FACT P): both signs present
        qs = report["hierarchy_q_by_window"]
        self.assertTrue(any(v > 1 for v in qs.values()) and any(v < 1 for v in qs.values()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
