"""Regression + fail-closed tests for the eps-approach-refuted / exponent-pivot candidate v0.1."""
import math
import unittest

from domains.standard_model.item1_exploration.eps_approach_refuted_exponent_pivot.eps_approach_refuted_exponent_pivot_v0_1 import (  # noqa: E501
    fn_exponent,
    real_ratios,
    run_fixture,
    theta_trajectory,
    turning_points,
)


class TestEpsApproachRefuted(unittest.TestCase):
    def test_eps_oscillates_and_overshoots_all_regimes(self):
        # FACT S: |Theta| oscillates (many turning points) and overshoots (>10) in every regime.
        for mt, g in [(4.0, 0.0), (4.0, 0.5), (3.5, 0.3)]:
            th = theta_trajectory(mt, 0.002, 30.0, g)
            self.assertGreaterEqual(turning_points(th), 20)     # oscillatory
            self.assertGreater(abs(th).max(), 10.0)             # overshoots the degeneracy

    def test_damping_does_not_settle(self):
        # even with strong damping the marble does not settle near the degeneracy.
        th = theta_trajectory(4.0, 0.002, 30.0, 2.0)
        self.assertGreater(abs(th).max(), 10.0)

    def test_up_sector_exponents_near_integer(self):
        # FACT T: at Theta=0.2 the up-sector exponents are ~4 and ~3.
        d1 = fn_exponent(real_ratios("up")[0], 0.2)
        d2 = fn_exponent(real_ratios("up")[1], 0.2)
        self.assertLess(abs(d1 - 4.0), 0.1)
        self.assertLess(abs(d2 - 3.0), 0.1)

    def test_down_lepton_not_integer_at_same_theta(self):
        # FACT T: the integer structure is NOT universal at a single Theta.
        non_integer = False
        for br in ("down", "lepton"):
            for R in real_ratios(br):
                d = fn_exponent(R, 0.2)
                if abs(d - round(d)) >= 0.1:
                    non_integer = True
        self.assertTrue(non_integer)

    def test_two_up_integers_are_not_independent(self):
        # deflation caveat: d1/d2 = ln R1/ln R2 is Theta-independent, so tuning Theta to d1~4 FORCES
        # d2~3 (because ln R1/ln R2 ~ 4/3). Not two independent hits.
        r1, r2 = real_ratios("up")
        slope_ratio = math.log(r1) / math.log(r2)
        self.assertLess(abs(slope_ratio - 4.0 / 3.0), 0.05)          # ~4/3
        # invariance: the ratio of exponents is the same at any Theta
        for th in (0.1, 0.2, 0.3):
            d1 = fn_exponent(r1, th)
            d2 = fn_exponent(r2, th)
            self.assertAlmostEqual(d1 / d2, slope_ratio, places=9)

    def test_up_integer_window_is_narrow(self):
        # Theta=0.2 is effectively tuned: the window where both up exponents are near-integer is narrow.
        r1, r2 = real_ratios("up")
        def both_near_int(th):
            d1, d2 = fn_exponent(r1, th), fn_exponent(r2, th)
            return abs(d1 - round(d1)) < 0.1 and abs(d2 - round(d2)) < 0.1
        window = [round(0.05 + i * 0.005, 3) for i in range(90) if both_near_int(0.05 + i * 0.005)]
        # a handful of isolated Theta values, not a broad range
        self.assertLess(len(window), 8)
        self.assertIn(0.2, window)

    def test_fn_exponent_formula(self):
        # d = ln R / ln(1/Theta); a pure power R=Theta^-d recovers d.
        self.assertAlmostEqual(fn_exponent(0.2 ** -3, 0.2), 3.0, places=9)

    def test_fail_closed_on_bad_input(self):
        with self.assertRaises(ValueError):
            theta_trajectory(0.0, 0.002, 10.0)
        with self.assertRaises(ValueError):
            theta_trajectory(4.0, 0.0, 10.0)

    def test_report_records_refutation_and_pivot(self):
        report = run_fixture()
        self.assertIn("REFUTED", report["status"])
        self.assertIn("exponent", report["status"])
        # up-sector exponents recorded near-integer
        up = report["fn_exponents_theta_0p2"]["up"]
        self.assertLess(abs(up[0] - 4.0), 0.1)
        self.assertLess(abs(up[1] - 3.0), 0.1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
