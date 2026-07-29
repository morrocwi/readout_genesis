#!/usr/bin/env python3
"""Regression + adversarial tests for dimensionless_native_ratio_bridge_v1.py.

Imports the candidate module directly (executing it once, output captured)
so every assertion below checks the SAME numbers the script actually printed
-- not a re-typed copy of them.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import re
import unittest
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "dimensionless_native_ratio_bridge_v1.py"
FORMAL_DIR = HERE.parents[3] / "formal"


def _load_module_capturing_stdout():
    spec = importlib.util.spec_from_file_location("dnrb_v1_under_test", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            spec.loader.exec_module(module)  # type: ignore[union-attr]
        except SystemExit:
            pass  # the module calls sys.exit(1) only if FAILS is non-empty
    return module, buf.getvalue()


class DimensionlessNativeRatioBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module, cls.stdout = _load_module_capturing_stdout()

    # ---- regression: internal gates all passed (fail-closed) -------------
    def test_all_internal_ck_gates_passed(self):
        self.assertEqual(self.module.FAILS, [],
                          f"internal PASS/FAIL gates failed: {self.module.FAILS}")

    # ---- regression: lambda_gap, recomputed independently here -----------
    def test_lambda_gap_independently_recomputed(self):
        L = np.array([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]], dtype=float)
        eigvals = sorted(np.linalg.eigvalsh(L))
        nonzero = [e for e in eigvals if abs(e) > 1e-9]
        self.assertEqual(len(nonzero), 2)
        for e in nonzero:
            self.assertAlmostEqual(e, 3.0, places=9)
        self.assertEqual(self.module.lambda_gap, 3.0)

    # ---- adversarial: guard against the repo silently changing curl's def -
    @unittest.skipUnless(
        (FORMAL_DIR / "InfoDiscreteCurl_attempt.v").exists(),
        "readout_genesis (this repo) is a curated public export and does not carry the full "
        "formal/ Coq library -- InfoDiscreteCurl_attempt.v was independently verified to exist "
        "and read 'a + b + c' in research_universal_solver (the canonical repo) on 2026-07-25; "
        "this test skips here rather than failing on a repo-scoping difference that is not a "
        "regression. If this file IS ever added to this repo, this test should start running "
        "and passing automatically.",
    )
    def test_curl_definition_in_repo_is_still_a_plus_b_plus_c(self):
        curl_file = FORMAL_DIR / "InfoDiscreteCurl_attempt.v"
        self.assertTrue(curl_file.exists(), f"missing {curl_file}")
        text = curl_file.read_text()
        m = re.search(r"Definition curl \(a b c : Q\) : Q :=\s*(.+?)\.", text)
        self.assertIsNotNone(m, "could not find curl definition in InfoDiscreteCurl_attempt.v")
        defn = m.group(1).strip()
        self.assertEqual(defn, "a + b + c",
                          "repo's curl definition changed -- Section 2's disclosed "
                          "discrepancy note and the h1=4*l2 identity must be re-checked")

    # ---- regression: h1/l2=4 identity, recomputed independently with the --
    # ---- SAME (real, repo) curl/div definitions used by the module -------
    def test_sobolev_ratio_independently_recomputed_symbolically(self):
        a, b, c = sp.symbols("a b c", real=True)
        l2 = a**2 + b**2 + c**2
        curl = a + b + c
        div1, div2, div3 = a - c, b - a, c - b
        h1 = l2 + curl**2 + div1**2 + div2**2 + div3**2
        self.assertEqual(sp.simplify(h1 - 4 * l2), 0)
        self.assertEqual(self.module.sobolev_ratio, sp.Rational(4, 1))

    def test_sobolev_ratio_holds_numerically_for_random_values(self):
        rng = np.random.default_rng(1234)
        a, b, c = sp.symbols("a b c", real=True)
        l2 = a**2 + b**2 + c**2
        curl = a + b + c
        div1, div2, div3 = a - c, b - a, c - b
        h1 = l2 + curl**2 + div1**2 + div2**2 + div3**2
        h1_f = sp.lambdify((a, b, c), h1)
        l2_f = sp.lambdify((a, b, c), l2)
        for _ in range(20):
            av, bv, cv = rng.uniform(-10, 10, 3)
            self.assertAlmostEqual(h1_f(av, bv, cv), 4 * l2_f(av, bv, cv), places=8)

    # ---- adversarial: curl = a-b+c (the brief's stated, WRONG, formula) --
    # ---- must NOT also give a clean integer ratio, or the disclosed ------
    # ---- discrepancy note in Section 2 would be misleading ---------------
    def test_brief_stated_curl_formula_does_not_also_give_a_clean_ratio(self):
        a, b, c = sp.symbols("a b c", real=True)
        l2 = a**2 + b**2 + c**2
        wrong_curl = a - b + c  # what the originating brief claimed
        div1, div2, div3 = a - c, b - a, c - b
        wrong_h1 = l2 + wrong_curl**2 + div1**2 + div2**2 + div3**2
        diff = sp.expand(wrong_h1 - 4 * l2)
        self.assertNotEqual(diff, 0,
                             "the brief's curl=a-b+c formula unexpectedly also gives "
                             "h1=4*l2 -- Section 2's discrepancy framing would be wrong")

    # ---- regression: D and M_joint read from the repo's own files --------
    def test_D_read_from_bateman_file(self):
        self.assertEqual(self.module.D_read, 0.3)

    def test_M_joint_calibration_status_fail_closed(self):
        # adversarial: this is the fail-closed gate on the calibration pipeline
        # -- if the pipeline ever stops returning CALIBRATED_READY, ratio_A
        # would be built on an UNRESOLVED estimate and must not be trusted.
        self.assertEqual(self.module.joint_status, "CALIBRATED_READY")
        self.assertTrue(self.module.M_joint > 0)

    def test_damping_rate_and_ratio_A_are_internally_consistent(self):
        expected_damping = self.module.D_read / (2.0 * self.module.M_joint)
        self.assertAlmostEqual(self.module.damping_rate, expected_damping, places=12)
        expected_ratio_A = self.module.lambda_gap / self.module.damping_rate
        self.assertAlmostEqual(self.module.ratio_A, expected_ratio_A, places=12)

    # ---- adversarial: ck() harness itself must fail-closed on a bad cond -
    def test_ck_harness_fails_closed_on_false_condition(self):
        fails_before = len(self.module.FAILS)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            result = self.module.ck("adversarial probe -- deliberately false", False, got="bogus")
        self.assertFalse(result)
        self.assertIn("adversarial probe -- deliberately false", self.module.FAILS)
        self.assertIn("[FAIL]", buf.getvalue())
        # clean up so this probe doesn't corrupt the module's real FAILS state
        self.module.FAILS.pop()
        self.assertEqual(len(self.module.FAILS), fails_before)

    def test_ck_harness_passes_on_true_condition(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            result = self.module.ck("adversarial probe -- deliberately true", True)
        self.assertTrue(result)
        self.assertIn("[PASS]", buf.getvalue())

    # ---- regression: no cherry-picking -- full cartesian product ---------
    def test_cross_table_is_full_cartesian_product_no_cherry_picking(self):
        expected_len = len(self.module.NATIVE_NUMBERS) * len(self.module.PRE_REGISTERED_TARGETS)
        self.assertEqual(len(self.module.rows), expected_len)
        # every native x every target must appear exactly once
        seen = {(r[1], r[3]) for r in self.module.rows}
        self.assertEqual(len(seen), expected_len)

    def test_cross_table_sorted_ascending_by_deviation(self):
        devs = [r[0] for r in self.module.rows]
        self.assertEqual(devs, sorted(devs))

    # ---- regression: pre-registered targets match what the docstring/ -----
    # ---- brief promised, guarding against silent post-hoc editing --------
    def test_pre_registered_targets_match_expected_values(self):
        expected = {
            "m_p/m_e (PDG)": 1836.15267,
            "m_mu/m_e (PDG)": 206.7683,
            "m_tau/m_e (PDG)": 3477.15,
            "M_W/M_Z (PDG)": 0.88148,
            "alpha_EM_inverse (PDG, low-E)": 137.035999,
            "sin2_theta_W (PDG, on-shell)": 0.23122,
            "Ising_3D nu (crit. exponent)": 0.6301,
            "Ising_3D beta (crit. exponent)": 0.3265,
            "Ising_3D gamma (crit. exponent)": 1.2372,
            "Ising_3D eta (crit. exponent)": 0.0364,
        }
        for k, v in expected.items():
            self.assertIn(k, self.module.PRE_REGISTERED_TARGETS)
            self.assertEqual(self.module.PRE_REGISTERED_TARGETS[k], v)

    # ---- regression: today's actual honest verdict is a negative result --
    def test_todays_actual_verdict_is_no_sub_2pct_match(self):
        sub_2pct = [r for r in self.module.rows if r[0] < 0.02]
        self.assertEqual(sub_2pct, [],
                          "if this now fails, a sub-2% match appeared -- update the "
                          "honest verdict/report, do not just delete this test")
        self.assertIn("NO candidate match against the pre-registered target list", self.stdout)

    # ---- regression: the honest fence text is present and not silently ---
    # ---- stripped from the source ----------------------------------------
    def test_honest_fence_present_in_output(self):
        self.assertIn("HONEST FENCE", self.stdout)
        self.assertIn("IS NOT established by this file", self.stdout)
        self.assertIn("[Open]", self.stdout)


if __name__ == "__main__":
    unittest.main()
