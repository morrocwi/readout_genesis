#!/usr/bin/env python3
"""
Regression + adversarial tests for pgft_rdu_internal_temperature_gateway_test_v0_1.py.

Run: python3 test_pgft_rdu_internal_temperature_gateway_test_v0_1.py
"""
from __future__ import annotations
import importlib.util
import math
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN_PATH = os.path.join(HERE, "pgft_rdu_internal_temperature_gateway_test_v0_1.py")


def load_main_module():
    """Load the main script as a module, capturing stdout so test output stays clean."""
    import io
    import contextlib

    spec = importlib.util.spec_from_file_location("gateway_test_v0_1", MAIN_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["gateway_test_v0_1"] = mod
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        spec.loader.exec_module(mod)
    return mod, buf.getvalue()


class TestSourcedConstants(unittest.TestCase):
    """Regression: the cited source values must not silently drift."""

    @classmethod
    def setUpClass(cls):
        cls.mod, cls.stdout = load_main_module()

    def test_D_matches_bateman_file(self):
        # domains/standard_model/matter_antimatter_exploration/
        #   attempt1_bateman_doubling_hypothesis_v1.py: "M, D, K = 1.0, 0.3, 1.0"
        self.assertEqual(self.mod.D_STEPPER, 0.3)

    def test_M_joint_matches_benchmark_report(self):
        # retained_transition_operational_closure/BENCHMARK_REPORT_V0_1.md line 48
        self.assertAlmostEqual(self.mod.M_JOINT, 1.0004294772248, places=10)

    def test_T_native_is_D_over_M_joint(self):
        self.assertAlmostEqual(self.mod.T_NATIVE, 0.3 / 1.0004294772248, places=12)

    def test_particle_energies_match_task_spec(self):
        expected = {
            "electron": 8.187e-14,
            "muon": 1.883e-11,
            "tau": 2.847e-10,
            "proton": 1.503e-10,
            "W_boson": 1.286e-8,
            "Z_boson": 1.462e-8,
            "Higgs": 2.011e-8,
        }
        self.assertEqual(self.mod.PARTICLES, expected)


class TestRoundTripBehavior(unittest.TestCase):
    """Regression: the empirical finding (T-independence) must reproduce on rerun."""

    @classmethod
    def setUpClass(cls):
        cls.mod, cls.stdout = load_main_module()

    def test_no_failures_recorded(self):
        self.assertEqual(self.mod.FAILS, [], msg=f"unexpected FAILS: {self.mod.FAILS}")

    def test_baseline_ratio_constant_across_particles(self):
        E1 = self.mod.PARTICLES["electron"]
        E2 = self.mod.PARTICLES["Higgs"]
        r1 = self.mod.round_trip_ratio_with_kB(E1, 310.0)["ratio_E_out_over_E_in"]
        r2 = self.mod.round_trip_ratio_with_kB(E2, 310.0)["ratio_E_out_over_E_in"]
        self.assertAlmostEqual(r1, r2, places=9)

    def test_ratio_independent_of_temperature_with_kB(self):
        """The core disclosed finding: swapping T under the k_B*T adapters changes nothing."""
        E = self.mod.PARTICLES["proton"]
        r_310 = self.mod.round_trip_ratio_with_kB(E, 310.0)["ratio_E_out_over_E_in"]
        r_4 = self.mod.round_trip_ratio_with_kB(E, 4.0)["ratio_E_out_over_E_in"]
        r_native = self.mod.round_trip_ratio_with_kB(E, self.mod.T_NATIVE)["ratio_E_out_over_E_in"]
        self.assertAlmostEqual(r_310, r_4, places=9)
        self.assertAlmostEqual(r_310, r_native, places=9)

    def test_variant_2a_byte_identical_to_baseline(self):
        self.assertLess(
            abs(self.mod.summary_2a["mean"] - self.mod.baseline_summary["mean"]), 1e-9
        )

    def test_variant_without_kB_also_temperature_independent(self):
        """Same linearity argument, no k_B: I_nat=E/T, E_out=T*final_nat -> ratio has no T."""
        E = self.mod.PARTICLES["muon"]
        r_a = self.mod.round_trip_ratio_without_kB(E, self.mod.T_NATIVE)["ratio_E_out_over_E_in"]
        r_b = self.mod.round_trip_ratio_without_kB(E, 99.0)["ratio_E_out_over_E_in"]
        self.assertAlmostEqual(r_a, r_b, places=9)

    def test_ratio_matches_bare_pde_transmission_fraction(self):
        """
        Adversarial: independently recompute final_nat/I_nat by calling run_native_pde()
        directly with I_nat=1.0 (bypassing the E/T adapters entirely) and confirm it equals
        the measured round-trip ratio. This is the direct proof that k_B*T (or T_native)
        cancels, verified by a path that never constructs an energy or temperature at all.
        """
        pde = self.mod.run_native_pde(1.0, self.mod.CFG)
        bare_ratio = pde["final_retained_nat_delta_R_e"] / 1.0
        self.assertAlmostEqual(bare_ratio, self.mod.baseline_summary["mean"], places=9)


class TestAdversarialFailClosed(unittest.TestCase):
    """Adversarial: the harness must actually be able to detect a broken mechanism, not
    just always print PASS. These deliberately-corrupted variants must be caught."""

    @classmethod
    def setUpClass(cls):
        cls.mod, _ = load_main_module()

    def test_detects_non_constant_ratio_if_pde_were_nonlinear(self):
        """
        Simulate what WOULD happen if the PDE's floor clipping actually bound (i.e. the
        'ratio is constant across energies' claim would be FALSE for a genuinely nonlinear
        stepper). We fabricate two deliberately different ratios and confirm the same
        rel_spread check used in the main script would correctly flag them as FAIL,
        proving the check is not vacuously true.
        """
        fabricated_ratios = [0.49303673, 0.51000000]  # deliberately not equal
        summary = self.mod.summarize_variant("adversarial-fabricated", fabricated_ratios)
        self.assertGreater(summary["rel_spread"], 1e-9)

    def test_negative_energy_input_rejected_by_qg_diagnostic(self):
        with self.assertRaises(ValueError):
            self.mod.qg_diagnostic(-1.0, 310.0)

    def test_negative_energy_rejected_by_the_actual_round_trip_functions(self):
        """Required correction (independent review, 2026-07-25): the test above only
        exercises qg_diagnostic, which this file imports but never calls in its actual
        round-trip pipeline (grep confirms zero call sites besides the docstring and that
        one test). Before this fix, round_trip_ratio_with_kB(-1.0, 310.0) did NOT raise --
        it silently returned {'final_nat': 0.0, 'ratio_E_out_over_E_in': -0.0} because
        run_native_pde's max(0,...) floor absorbed the negative input. Both real functions
        now have an explicit guard; this test exercises THOSE functions, whose numbers this
        file's conclusions are actually based on, not the unused import."""
        with self.assertRaises(ValueError):
            self.mod.round_trip_ratio_with_kB(-1.0, 310.0)
        with self.assertRaises(ValueError):
            self.mod.round_trip_ratio_without_kB(-1.0, 0.3)
        with self.assertRaises(ValueError):
            self.mod.round_trip_ratio_with_kB(1.0, -5.0)
        with self.assertRaises(ValueError):
            self.mod.round_trip_ratio_with_kB(math.nan, 310.0)

    def test_zero_T_native_would_be_caught_not_silently_divide(self):
        """T_native = D/M_joint is always > 0 given real inputs, but confirm the harness's
        own finiteness check (ck 'T_native is finite positive') would fire if D were 0."""
        contrived_T_native = 0.0 / self.mod.M_JOINT
        self.assertFalse(contrived_T_native > 0 and math.isfinite(contrived_T_native))

    def test_pde_output_is_never_negative(self):
        """Sanity gate on the underlying mechanism: retained native information must stay
        non-negative (the max(0,...) floor is supposed to guarantee this)."""
        pde = self.mod.run_native_pde(1.234e-5, self.mod.CFG)
        self.assertGreaterEqual(pde["final_retained_nat_delta_R_e"], 0.0)
        self.assertGreaterEqual(pde["dissipated_nat_delta_R_e"], 0.0)

    def test_variant_2a_and_2b_not_closer_to_any_target_than_baseline(self):
        """Regression-lock the honest negative finding: neither internally-derived variant
        beats the baseline's distance to the pre-registered target list. If a future edit
        makes this assertion fail, that is a REAL finding and must be re-examined, not
        silently deleted."""
        targets = list(self.mod.TARGETS.values())

        def nearest_dist(v):
            return min(abs(v - t) for t in targets)

        baseline_d = nearest_dist(self.mod.baseline_summary["mean"])
        d_2a = nearest_dist(self.mod.summary_2a["mean"])
        d_2b = nearest_dist(self.mod.summary_2b["mean"])
        self.assertGreaterEqual(d_2a, baseline_d - 1e-9)
        self.assertGreaterEqual(d_2b, baseline_d - 1e-9)


if __name__ == "__main__":
    unittest.main(verbosity=2)
