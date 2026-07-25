"""Regression + fail-closed tests for the decelerating accumulation profile v0.1."""
import unittest

from domains.standard_model.item1_exploration.decelerating_accumulation_profile.decelerating_accumulation_profile_v0_1 import (  # noqa: E501
    BRANCHES,
    decelerating_profile,
    real_ratios,
    run_fixture,
)


class TestDeceleratingProfile(unittest.TestCase):
    def test_reconstructs_both_ratios_exactly(self):
        # FACT D: r=R1, q=R2/R1 by construction -> exact reconstruction of both ratios.
        for br in BRANCHES:
            r1, r2 = real_ratios(br)
            p = decelerating_profile(br)
            self.assertAlmostEqual(p["recon_R1"], r1, places=9)
            self.assertAlmostEqual(p["recon_R2"], r2, places=9)
            self.assertLess(p["recon_R1_err"], 1e-9)
            self.assertLess(p["recon_R2_err"], 1e-9)

    def test_q_equals_R2_over_R1(self):
        for br in BRANCHES:
            r1, r2 = real_ratios(br)
            p = decelerating_profile(br)
            self.assertAlmostEqual(p["q"], r2 / r1, places=12)
            self.assertAlmostEqual(p["r"], r1, places=12)

    def test_up_and_lepton_decelerate(self):
        # FACT D: the profile reaches the decelerating shapes FACT C said uniform accumulation cannot.
        self.assertLess(decelerating_profile("up")["q"], 1.0)
        self.assertLess(decelerating_profile("lepton")["q"], 1.0)
        self.assertEqual(decelerating_profile("up")["shape"], "decelerating")
        self.assertEqual(decelerating_profile("lepton")["shape"], "decelerating")

    def test_down_accelerates(self):
        # The sign-flip vs r: down has the smallest r yet accelerates (q>1).
        self.assertGreater(decelerating_profile("down")["q"], 1.0)
        self.assertEqual(decelerating_profile("down")["shape"], "accelerating")

    def test_q_not_a_single_shared_constant(self):
        # FACT E: q spans >10x across branches -> no single shared q.
        qs = [decelerating_profile(br)["q"] for br in BRANCHES]
        self.assertGreater(max(qs) / min(qs), 10.0)

    def test_q_flips_sign_of_trend_vs_r(self):
        # FACT E: down (smallest r) accelerates while up/lepton (larger r) decelerate -> no q=f(r).
        p = {br: decelerating_profile(br) for br in BRANCHES}
        self.assertLess(p["down"]["r"], p["up"]["r"])
        self.assertLess(p["down"]["r"], p["lepton"]["r"])
        self.assertGreater(p["down"]["q"], 1.0)
        self.assertLess(p["up"]["q"], 1.0)
        self.assertLess(p["lepton"]["q"], 1.0)

    def test_fail_closed_on_bad_branch(self):
        with self.assertRaises(KeyError):
            decelerating_profile("nonexistent")

    def test_report_status_is_computed_facts_not_a_verdict(self):
        report = run_fixture()
        # guard: status is a computed-facts string, no works/fails value-word.
        self.assertIn("COMPUTED", report["status"])
        self.assertNotIn("FAIL", report["status"].upper().replace("FACT", ""))
        self.assertGreater(report["q_spread_max_over_min"], 10.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
