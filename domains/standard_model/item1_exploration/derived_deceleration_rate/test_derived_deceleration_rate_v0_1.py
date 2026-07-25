"""Regression + fail-closed tests for the derived deceleration rate v0.1."""
import unittest

from domains.standard_model.item1_exploration.derived_deceleration_rate.derived_deceleration_rate_v0_1 import (  # noqa: E501
    BOOST,
    DEFAULT_IC,
    ROTATION,
    derived_log_q,
    run_fixture,
)


class TestDerivedDecelerationRate(unittest.TestCase):
    def setUp(self):
        self.phi0, self.psi0 = DEFAULT_IC

    def test_rotation_control_gives_q_one(self):
        # FACT F: compact generator -> isotropic -> q=1 exactly (log q=0).
        lq = derived_log_q(self.phi0, self.psi0, ROTATION, 2.0)
        self.assertIsNotNone(lq)
        self.assertAlmostEqual(lq, 0.0, places=6)

    def test_boost_drives_q_away_from_one(self):
        # FACT F: non-compact generator drives q != 1.
        lq = derived_log_q(self.phi0, self.psi0, BOOST, 2.0)
        self.assertIsNotNone(lq)
        self.assertGreater(abs(lq), 0.5)

    def test_sign_flip_from_m_theta(self):
        # FACT G: small M_Theta accelerates, large M_Theta decelerates -- sign-flip from a graph constant.
        lq_small = derived_log_q(self.phi0, self.psi0, BOOST, 2.0)
        lq_large = derived_log_q(self.phi0, self.psi0, BOOST, 15.0)
        self.assertGreater(lq_small, 0.0)      # accelerate
        self.assertLess(lq_large, 0.0)         # decelerate

    def test_real_targets_inside_produced_range(self):
        # FACT G: down +0.35, up -0.64, lepton -1.09 all lie within [decel, accel].
        lq_small = derived_log_q(self.phi0, self.psi0, BOOST, 2.0)
        lq_large = derived_log_q(self.phi0, self.psi0, BOOST, 15.0)
        for target in (0.350, -0.636, -1.090):
            self.assertLess(lq_large, target)
            self.assertLess(target, lq_small)

    def test_map_is_not_clean_monotone(self):
        # FACT H (honest limit): q=f(M_Theta) is instability-dominated, not monotone.
        vals = [derived_log_q(self.phi0, self.psi0, BOOST, mt)
                for mt in (5.0, 7.0, 9.0, 11.0, 15.0, 18.0, 30.0, 100.0)]
        vals = [v for v in vals if v is not None]
        monotone = all(vals[i] >= vals[i + 1] - 1e-9 for i in range(len(vals) - 1))
        self.assertFalse(monotone, "map unexpectedly monotone -- FACT H (instability) would be false")

    def test_derived_q_is_not_tuned_to_target(self):
        # honesty guard: the boost small-M_Theta q is nowhere near any real target -> not fit.
        lq = derived_log_q(self.phi0, self.psi0, BOOST, 2.0)
        for target in (0.350, -0.636, -1.090):
            self.assertGreater(abs(lq - target), 1.0)   # far from every real value = not tuned

    def test_fail_closed_on_bad_m_theta(self):
        with self.assertRaises(ValueError):
            derived_log_q(self.phi0, self.psi0, BOOST, 0.0)
        with self.assertRaises(ValueError):
            derived_log_q(self.phi0, self.psi0, BOOST, -1.0)

    def test_report_status_is_computed_facts(self):
        report = run_fixture()
        self.assertIn("COMPUTED", report["status"])
        # honest bound: status names the instability/non-invertibility, not a clean derivation
        self.assertIn("instability", report["status"])
        self.assertIn("non_invertible", report["status"])
        # both signs present in the reported log-q values
        self.assertGreater(report["log_q_boost_small_m_theta"], 0.0)
        self.assertLess(report["log_q_boost_large_m_theta"], 0.0)
        self.assertAlmostEqual(report["log_q_rotation_control"], 0.0, places=6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
