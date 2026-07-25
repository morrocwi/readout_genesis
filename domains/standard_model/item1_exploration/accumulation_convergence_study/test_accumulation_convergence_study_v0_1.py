"""Regression + fail-closed tests for the accumulation convergence study v0.1."""
import unittest

from domains.standard_model.item1_exploration.accumulation_convergence_study.accumulation_convergence_study_v0_1 import (  # noqa: E501
    BOOST,
    DEFAULT_IC,
    _lq,
    log_q,
    run_fixture,
)


class TestAccumulationConvergenceStudy(unittest.TestCase):
    def test_sign_flips_vanish_under_refinement(self):
        # FACT I: coarse dt has sign-flip chaos; fine dt removes it.
        def flips(dt):
            vals = [_lq(mt, dt) for mt in (5.0, 7.0, 9.0, 11.0)]
            vals = [v for v in vals if v is not None]
            return sum(1 for i in range(len(vals) - 1) if vals[i] * vals[i + 1] < 0)
        self.assertGreaterEqual(flips(0.01), 3)
        self.assertEqual(flips(0.002), 0)

    def test_acceleration_positive_but_not_cleanly_converged(self):
        # FACT J (corrected): log q(m=15) stays POSITIVE across 5 refinements but its increments are
        # NON-MONOTONE -- plausible-but-not-established convergent. Same refinement depth as the
        # deceleration test (4+ points), so the accel bar is as strict as the decel bar.
        seq = [_lq(15.0, dt) for dt in (0.002, 0.001, 0.0005, 0.00025, 0.000125)]
        self.assertTrue(all(v > 0 for v in seq))              # stays large-positive: no 1/dt blowup
        incs = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
        non_monotone = not all(abs(incs[i + 1]) <= abs(incs[i]) + 1e-9 for i in range(len(incs) - 1))
        self.assertTrue(non_monotone, "increments unexpectedly monotone -- would falsely imply clean convergence")
        # and crucially NOT the 1/dt doubling that the deceleration branch shows
        ratios = [seq[i + 1] / seq[i] for i in range(len(seq) - 1)]
        self.assertTrue(all(r < 1.5 for r in ratios))         # bounded drift, not systematic doubling

    def test_deceleration_diverges_as_dt_shrinks(self):
        # FACT K: large-M_Theta 'decel' diverges ~ 1/dt (log q roughly doubles each dt-halving).
        div = [_lq(300.0, dt) for dt in (0.002, 0.001, 0.0005, 0.00025)]
        self.assertTrue(all(v < 0 for v in div))              # stays 'decel' but never settles
        ratios = [div[i + 1] / div[i] for i in range(len(div) - 1)]
        self.assertTrue(all(r > 1.5 for r in ratios))         # doubling => 1/dt divergence, not physical

    def test_moderate_m_theta_decel_is_coarse_dt_artifact(self):
        # FACT K(a): M_Theta=15 reads decel at coarse dt but flips to accel under refinement.
        self.assertLess(_lq(15.0, 0.005), 0.0)                # coarse: DECEL
        self.assertGreater(_lq(15.0, 0.0005), 0.0)            # refined: ACCEL

    def test_fail_closed_on_bad_input(self):
        phi0, psi0 = DEFAULT_IC
        with self.assertRaises(ValueError):
            log_q(phi0, psi0, BOOST, 0.0, 0.01, 100)
        with self.assertRaises(ValueError):
            log_q(phi0, psi0, BOOST, 5.0, 0.0, 100)

    def test_report_records_retraction(self):
        report = run_fixture()
        self.assertIn("COMPUTED", report["status"])
        self.assertIn("artifact", report["status"])
        self.assertIn("FACT G", report["retracts"])
        # acceleration stays positive across the drift; the 300-divergence recorded
        self.assertTrue(all(v > 0 for v in report["accel_positive_but_drifting_log_q"]["m_theta_15"]))
        self.assertTrue(all(v < 0 for v in report["decel_divergence_m_theta_300"].values()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
