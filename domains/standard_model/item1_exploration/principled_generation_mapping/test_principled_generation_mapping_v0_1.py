"""Regression + fail-closed tests for the principled generation mapping v0.1."""
import unittest

from domains.standard_model.item1_exploration.principled_generation_mapping.principled_generation_mapping_v0_1 import (  # noqa: E501
    SINGULAR_SPIKE,
    convergent_ratio,
    cond_trajectory,
    generation_peaks,
    run_fixture,
)


class TestPrincipledGenerationMapping(unittest.TestCase):
    def test_convergent_two_generation_ratio(self):
        # FACT Q: the two well-separated intrinsic peaks give a dt-convergent ~94.9x ratio.
        ratios = [convergent_ratio(4.0, dt, 10.0)[2] for dt in (0.004, 0.002, 0.001, 0.0005)]
        self.assertTrue(all(90 < r < 100 for r in ratios))
        self.assertLess(max(ratios) - min(ratios), 0.1)          # dt-convergent

    def test_ratio_is_not_hand_picked(self):
        # the ratio comes from intrinsic peaks (local maxima), not chosen time points.
        peaks = generation_peaks(4.0, 0.0005, 10.0)
        self.assertGreaterEqual(len(peaks), 2)
        # the two used peaks are the strong (>10) and weak (<10) bounded-away-from-singular ones
        big, small, r = convergent_ratio(4.0, 0.0005, 10.0)
        self.assertGreater(big, 10.0)
        self.assertLess(small, 10.0)
        self.assertLess(big, SINGULAR_SPIKE)

    def test_ratio_is_defined_only_at_isolated_m_theta(self):
        # FACT Q' (caught by review): the convergent ratio exists only near M_Theta=4.0; at every
        # other M_Theta tested the intermediate peak does not form, so the ratio is UNDEFINED (None).
        defined = [mt for mt in (3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 8.0, 10.0)
                   if convergent_ratio(mt, 0.0005, 10.0) is not None]
        self.assertEqual(defined, [4.0])            # fragile: one isolated applicability point

    def test_singular_peak_does_not_converge(self):
        # FACT R: the peak at |Theta|=1 is hypersensitive -- height varies >2x across dt.
        spikes = []
        for dt in (0.002, 0.001, 0.0005):
            peaks = generation_peaks(4.0, dt, 10.0)
            if peaks and peaks[0] >= SINGULAR_SPIKE:
                spikes.append(peaks[0])
        self.assertGreaterEqual(len(spikes), 2)
        self.assertGreater(max(spikes) / min(spikes), 2.0)       # non-convergent

    def test_cond_trajectory_oscillates(self):
        # the readout oscillates (why a principled landmark is needed, not arbitrary times).
        c = cond_trajectory(4.0, 0.001, 10.0)
        self.assertGreater(c.max(), 10.0)                        # reaches near the degeneracy
        # has multiple local maxima (oscillatory), not monotone
        idx = [i for i in range(1, len(c) - 1) if c[i] > c[i - 1] and c[i] >= c[i + 1]]
        self.assertGreaterEqual(len(idx), 3)

    def test_fail_closed_on_bad_input(self):
        with self.assertRaises(ValueError):
            cond_trajectory(0.0, 0.001, 10.0)
        with self.assertRaises(ValueError):
            cond_trajectory(4.0, 0.0, 10.0)

    def test_report_records_the_convergent_ratio_and_limit(self):
        report = run_fixture()
        self.assertIn("COMPUTED", report["status"])
        self.assertIn("convergent", report["status"])
        self.assertTrue(90 < report["converged_ratio"] < 100)
        # convergent across dt
        rv = list(report["convergent_ratio_by_dt"].values())
        self.assertLess(max(rv) - min(rv), 0.1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
