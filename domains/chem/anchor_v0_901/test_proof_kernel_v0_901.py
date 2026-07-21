import unittest
from fractions import Fraction
from proof_kernel_v0_901 import (
    run_proof_suite, ledger_conservation_certificate, kernel_basis_certificate,
    positivity_interval_1d, refine_partition, additivity_no_free_countermodel,
    observational_stationarity_counterexample
)

class ProofKernelTests(unittest.TestCase):
    def test_full_suite(self):
        result = run_proof_suite()
        self.assertEqual(result["decision"], "PASS")
        self.assertTrue(all(result["statuses"].values()))

    def test_ledger_failure_detected(self):
        cert = ledger_conservation_certificate([[1, 1]], [1, 1], [2, 1])
        self.assertFalse(cert["closed_boundary_holds"])
        self.assertNotEqual(cert["residual"], ["0"])

    def test_non_kernel_basis_detected(self):
        cert = kernel_basis_certificate([[1, 1]], [[1, 0]], [1])
        self.assertFalse(cert["all_basis_in_kernel"])

    def test_empty_positivity_region(self):
        cert = positivity_interval_1d([-1], [0])
        self.assertFalse(cert["admissible"])

    def test_refinement_splits_hidden_readout(self):
        states = ["x", "y"]
        F = {"x":"x", "y":"y"}
        O = {"x":0, "y":1}
        cert = refine_partition(states, F, O, [states])
        self.assertEqual(len(cert["partition"]), 2)

    def test_no_free_additivity(self):
        cert = additivity_no_free_countermodel()
        self.assertTrue(cert["additive_passes"])
        self.assertTrue(cert["nonadditive_fails"])

    def test_hidden_motion_counterexample(self):
        cert = observational_stationarity_counterexample()
        self.assertTrue(cert["quotient_is_fixed"])
        self.assertTrue(cert["source_has_hidden_motion"])

if __name__ == '__main__':
    unittest.main()
