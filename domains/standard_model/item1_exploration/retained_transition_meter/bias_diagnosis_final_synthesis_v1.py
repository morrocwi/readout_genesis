#!/usr/bin/env python3
"""
RTM bias diagnosis -- FINAL SYNTHESIS, 2026-07-25: consolidates two INDEPENDENTLY-CONVERGED
diagnoses of the scalar OLS estimator's bias mechanism into one closed finding, before any
estimator-selection work begins.

Provenance of the two independent lines (both confirmed to agree to the digit, re-verified here a
third time from scratch):
1. This branch's own `bias_diagnosis_v1.py` (2026-07-25): ruled out a nonlinear "cubic
   rectification" hypothesis (self-caught wrong, ~1e-10 relative effect), then confirmed classic
   LINEAR errors-in-variables (EIV) attenuation via `Var(a_true)/(Var(a_true)+Var(noise))`,
   independently adversarially reviewed -- SURVIVES.
2. A parallel team's `readout_genesis` PR #71 ("Diagnose RTM OLS bias before estimator
   selection"): ran the SAME real Reader/Record stepper, SAME parameters (M=1, D=0.3, K=1,
   dt=0.01), and reproduced this branch's noise-sweep table to the digit. Independently added a
   4-way ablation (EIV-only / target-only / linearized / full-nonlinear) that this branch's own
   diagnosis had not run, isolating exactly how much of the bias comes from noise in the
   REGRESSOR (a_n) versus noise passing through the NONLINEAR target (gradV(Phi)).

THIS FILE re-derives PR #71's 4-way ablation numbers independently (not copied from their report)
to confirm the two lines are genuinely the same finding from two independent implementations, not
two different findings that happen to share a name.

Tier: finite_diagnostic (all numeric checks below, reproducible). Dr for the synthesis narrative.
"""
import numpy as np

from . import stepper_reuse as stepper
from . import rtm_fit
from . import tape_generator as tg

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


print("== 0. TIER TAG (mandatory) ==")
print("  finite_diagnostic for all numeric checks (reproducible, fixed seed). Dr for the")
print("  cross-team convergence narrative.")

print("\n== 1. independently re-derive PR #71's 4-way ablation (not copied from their report) ==")
sigma = 1e-5
dt = stepper.dt
t0 = tg.build_tape(n_steps=2000, phi0=1.0, phi1=1.01, psi0=-1.0, psi1=-1.01,
                    seed_note="final-synthesis", obs_noise_sigma=0.0)
a_true, y_true, idx = rtm_fit._reader_ay(t0, slice(None))

rng = np.random.default_rng(20260725)
eps = rng.normal(0.0, sigma, size=len(t0["Phi"]))
phi_noisy = t0["Phi"] + eps


def _d2(x):
    return (x[2:] - 2 * x[1:-1] + x[:-2]) / dt**2


def _d1(x):
    return (x[2:] - x[:-2]) / (2 * dt)


a_noisy = _d2(phi_noisy)
d1_noisy = _d1(phi_noisy)
phi_n_noisy = phi_noisy[1:-1]
y_full_noisy = -stepper.D * d1_noisy - stepper.K * phi_n_noisy - stepper.gradV(phi_n_noisy)

M_eiv_only = float(np.sum(a_noisy * y_true) / np.sum(a_noisy * a_noisy))
M_target_only = float(np.sum(a_true * y_full_noisy) / np.sum(a_true * a_true))
M_full = float(np.sum(a_noisy * y_full_noisy) / np.sum(a_noisy * a_noisy))

print(f"   M_eiv_only   (noisy regressor, CLEAN target): {M_eiv_only:.8f}")
print(f"   M_target_only (clean regressor, noisy NONLINEAR target): {M_target_only:.8f}")
print(f"   M_full        (both noisy, the actual estimator): {M_full:.8f}")
print(f"   true M: {stepper.M}")

print("   CAVEAT applied after independent review (2026-07-25): the exact-digit match to PR #71's")
print("   numbers below is a DETERMINISTIC REPRODUCTION, not independent statistical convergence")
print("   -- both this file and PR #71 use the SAME disclosed RNG seed (20260725, already this")
print("   repo's own tape_generator.py default). A 5-seed sweep (run separately, see Part 1b")
print("   below) confirms M_eiv_only is genuinely SEED-SENSITIVE (varies ~0.781-0.795 across 5")
print("   seeds, ~2% spread) -- so matching PR #71's specific digits only shows both files")
print("   correctly implemented the SAME computation on the SAME input, not that two independent")
print("   random processes agreed. What IS seed-robust (checked below, Part 1b) is the QUALITATIVE")
print("   pattern: M_target_only stays within ~3e-6 of true M=1 regardless of seed, while")
print("   M_eiv_only stays biased regardless of seed -- THAT pattern is the genuine, non-circular")
print("   corroboration, not the specific decimal digits.")
ck("reproduces PR #71's specific M_eiv_only=0.79470963 GIVEN the same disclosed seed (a "
   "reproducibility check, not independent statistical evidence -- see caveat above)",
   abs(M_eiv_only - 0.79470963) < 1e-6, M_eiv_only)
ck("reproduces PR #71's specific M_target_only=0.99999907 GIVEN the same disclosed seed "
   "(reproducibility check, same caveat)",
   abs(M_target_only - 0.99999907) < 1e-6, M_target_only)
ck("M_full is close to M_eiv_only (EIV-in-regressor dominates the bias, not the nonlinear-"
   "target-noise path -- confirms PR #71's own conclusion, not merely repeating it unverified)",
   abs(M_full - M_eiv_only) < 0.01, abs(M_full - M_eiv_only))
ck("M_target_only is close to the true M=1 (nonlinear-target-noise ALONE contributes negligible "
   "bias -- the cubic gradV(Phi) path is confirmed NOT the dominant mechanism, matching this "
   "branch's own earlier self-caught-wrong 'cubic rectification' finding from a different angle)",
   abs(M_target_only - stepper.M) < 0.01, M_target_only)

print("\n== 1b. seed-robustness check (the genuinely non-circular corroboration) ==")
_seeds = [1, 42, 12345, 20260725, 99999]
_m_eiv_vals, _m_target_vals = [], []
for _seed in _seeds:
    _rng = np.random.default_rng(_seed)
    _eps = _rng.normal(0.0, sigma, size=len(t0["Phi"]))
    _phi_noisy = t0["Phi"] + _eps
    _a_noisy = _d2(_phi_noisy)
    _m_eiv = float(np.sum(_a_noisy * y_true) / np.sum(_a_noisy * _a_noisy))
    _d1n = _d1(_phi_noisy)
    _phi_n = _phi_noisy[1:-1]
    _y_full = -stepper.D * _d1n - stepper.K * _phi_n - stepper.gradV(_phi_n)
    _m_target = float(np.sum(a_true * _y_full) / np.sum(a_true * a_true))
    _m_eiv_vals.append(_m_eiv)
    _m_target_vals.append(_m_target)
    print(f"   seed={_seed:>8}  M_eiv_only={_m_eiv:.6f}  M_target_only={_m_target:.8f}")
_eiv_spread = max(_m_eiv_vals) - min(_m_eiv_vals)
_target_max_dev = max(abs(v - stepper.M) for v in _m_target_vals)
print(f"   M_eiv_only spread across 5 seeds: {_eiv_spread:.6f} (genuinely seed-sensitive)")
print(f"   M_target_only max deviation from true M across 5 seeds: {_target_max_dev:.2e} "
      f"(genuinely seed-robust, stays near-perfect)")
ck("M_eiv_only IS seed-sensitive (spread > 0.01) -- confirming the exact-digit match above is a "
   "reproducibility artifact of the shared seed, not evidence the estimator itself is stable",
   _eiv_spread > 0.01, _eiv_spread)
ck("M_target_only stays near-true (< 1e-4 deviation) for EVERY seed tested -- THIS is the "
   "genuine, seed-robust, non-circular corroboration: nonlinear-target-noise negligibility holds "
   "regardless of which specific noise draw is used",
   _target_max_dev < 1e-4, _target_max_dev)

print("\n== 2. cross-check the S_a (signal power) ratio both lines independently computed ==")
a_psi_true, y_psi_true, _ = rtm_fit._record_ay(t0, slice(None))
S_a_phi = float(np.sum(a_true**2))
S_a_psi = float(np.sum(a_psi_true**2))
ratio = S_a_psi / S_a_phi
print(f"   S_a_phi={S_a_phi:.4f}   S_a_psi={S_a_psi:.4f}   ratio={ratio:.4f}")
ck("S_a ratio matches PR #71's independently-computed ~423.15 to within 1%",
   abs(ratio - 423.15) < 4.2, ratio)

print("\n== 3. what is and is NOT genuine cross-team corroboration (corrected after review) ==")
print("   REQUIRED CORRECTION applied 2026-07-25, after independent review: an earlier draft of")
print("   this section claimed 'two independent implementations converge to 6+ decimal places' as")
print("   if that were strong statistical evidence. The reviewer correctly pointed out this is")
print("   MISLEADING for the noise-dependent numbers: both this file and PR #71 use the SAME")
print("   disclosed seed (20260725), so an exact digit match there is a REPRODUCIBILITY check")
print("   (did both files correctly implement the same computation on the same input?), not")
print("   independent statistical confirmation. Corrected framing:")
print("   - SEED-DEPENDENT exact-digit matches (M_eiv_only, M_full): reproducibility only.")
print("   - SEED-INDEPENDENT findings, genuinely non-circular: the S_a ratio (~423, a pure")
print("     function of the noiseless deterministic trajectory, no randomness involved at all),")
print("     and the QUALITATIVE pattern from Part 1b's 5-seed sweep -- M_target_only stays within")
print("     3e-6 of true M for every seed tested, M_eiv_only stays biased (spread >0.01) for")
print("     every seed tested. THAT pattern-level agreement, reached via two differently-designed")
print("     methodologies (this branch's attenuation-formula route; PR #71's 4-way-ablation")
print("     route), is the genuine corroboration.")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (finite_diagnostic for the numeric checks, Dr for the cross-team synthesis):

- WHAT THIS ESTABLISHES: two independently-designed diagnostic methodologies (this branch's
  attenuation-formula route; readout_genesis PR #71's 4-way-ablation route) agree, at the
  QUALITATIVE/seed-robust level (Part 1b, 5 seeds), on the SAME bias mechanism for the scalar OLS
  estimator used by every parallel M_n-fitting candidate (this repo's v1/v3, and readout_genesis
  PR #67/#69): classic linear errors-in-variables attenuation, caused by the Reader (Phi) channel
  losing acceleration signal power (~423x less than Record/Psi, a seed-independent, purely
  deterministic ratio) as Phi settles toward the double-well fixed point -- NOT by noise passing
  through the nonlinear gradV(Phi) term (confirmed negligible, seed-robustly, by the target-only
  ablation AND this branch's earlier cubic-rectification-correction test, ~1e-10 relative effect).
  The exact-digit matches to PR #71's specific reported numbers are a REPRODUCIBILITY check (both
  files share the same disclosed seed convention already used throughout this repo's tape
  generator), not independent statistical evidence on their own -- corrected here after review,
  which is the honest, useful distinction, not a weakening of the underlying finding.
- WHAT THIS DOES NOT ESTABLISH -- restated per the founder-relayed scope from the parallel team
  (2026-07-25), taken at face value, not softened: the exchange rate `M_n` is **NOT CLOSED**.
  Specifically, still open: (a) no noise-robust estimator exists yet -- the current OLS `M_hat` is
  known-biased, and every downstream quantity (`c_n`, `Delta_j`, `lambda_j`, `Pi_0`) inherits that
  bias uncorrected; (b) the semantic/encoding bridge `M_DRL_exchange =? M_primitive_retained_
  transition` is entirely unproven -- measuring a coefficient in the Reader/Record equation is not
  the same as showing it IS "the price per elementary retained-distinction transition" the SM
  chain needs; (c) the cost definition `c_n` itself remains a candidate, not a fact (signed vs
  abs, `cost_unit_rd`'s origin, which path is a genuine primitive closure, segmentation-invariance
  of the definition -- all open, which is WHY PR #69 correctly refuses to emit `lambda`/`Pi_0` at
  all unless `path_semantics=primitive_closure` is explicitly declared). None of `M_hat`, `c_n`,
  `Delta_j`, `lambda_j`, or `Pi_0` computed by ANY of the three parallel candidates should be read
  as a physical prediction -- every one is `finite_diagnostic`/`candidate`/`fit_calibrated`, a
  software-recovery number on a fixture, not a derived or measured Standard-Model quantity. Also
  unaffected as always: item 1's actual root-derivation question, generation multiplicity, real
  fermion masses/couplings/mixing -- unrelated, out of scope.
- FIVE CRITERIA that would need to be met before `M_n` could be considered closed (relayed from
  the parallel team, endorsed here as the correct bar, not lowered): (1) a noise-robust estimator
  that is fail-closed when data is insufficient, not just the current biased OLS; (2) testing
  against multiple trajectories/noise models/parameters, not one fixture; (3) a real external
  adapter (QuTiP or experimental data), not only synthetic tapes; (4) proven invariance under
  segmentation, coordinate relabeling, and admissible re-encoding; (5) using a fitted `M` to
  predict a held-out observable that was NOT used in the fit itself. None of these are met yet by
  any of the three parallel candidates.
- WHAT IS SAFE TO USE NOW, correctly tagged: software-recovery numbers on simulated fixtures,
  effective-`M`-per-tape measurements, noise sensitivity curves, Reader/Record disagreement
  reports, transport-failure findings, segmentation-dependence findings, signed-vs-absolute
  exchange comparisons, and PROVISIONAL `Delta`/`lambda`/`Pi0` values for testing the pipeline's
  own plumbing -- all under the `finite_diagnostic`/`candidate`/`not a physical prediction` tag,
  never as "this is nature's exchange rate" or "this is `Delta_U/Delta_D/Delta_E`" or "this is
  `Pi_0`" in the sense item 1's derivation question means.
- This is a diagnosis-synthesis file, not a new candidate estimator -- opened as its own PR,
  separate from candidate/retained-transition-meter-v1-2026-07-25 and
  candidate/retained-transition-meter-v3-synthesis-2026-07-25, since it makes no estimator
  proposal of its own. It closes the DIAGNOSIS question (why is OLS biased) with real
  cross-methodology confidence; it explicitly does NOT close the `M_n` question itself.
""")
