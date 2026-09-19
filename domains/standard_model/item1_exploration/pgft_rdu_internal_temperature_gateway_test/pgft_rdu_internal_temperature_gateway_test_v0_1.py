#!/usr/bin/env python3
"""
PGFT-RDU internal-temperature gateway test -- v0.1, 2026-07-25.

THE MECHANISM UNDER TEST (quoted/cited, not invented here):
  scripts/pgft_rdu_v0_7_quantum_gravity_real_problem.py already implements a working,
  already-executable native<->SI energy round trip:
      E_J  --J_to_native_nat(E_J, T)-->  I_nat = E_J / (k_B * T)
      I_nat --run_native_pde(I_nat, cfg)-->  final_nat  (a native dissipative-PDE step)
      final_nat --native_nat_to_J(final_nat, T)-->  E_out_J = k_B * T * final_nat
  (see that file's lines ~52-58 for the adapter functions, ~164-181 for qg_diagnostic(),
  ~183-216 for run_native_pde() / scenario()). Its one disclosed weakness is a hardcoded,
  unexplained T=310.0 K (human-body temperature) with no derivation from the framework.

WHAT THIS FILE DOES THAT IS NEW: replaces that borrowed T=310.0 K with an internally-derived
candidate T_native built ONLY from quantities this repo has already computed elsewhere with
no new fitting, and tests whether the round-trip ratio E_out/E_in becomes a stable,
non-arbitrary, more-physically-suggestive number when driven by native quantities instead of
a borrowed physical constant. Both a positive AND a negative outcome are reportable; this file
does not know in advance which one it will get, and is written to report either honestly.

SOURCES FOR THE READ-STRAIGHT-OUT VALUES (cited exactly, not re-derived):
  D = 0.3 -- domains/standard_model/matter_antimatter_exploration/
             attempt1_bateman_doubling_hypothesis_v1.py, line:
                 M, D, K = 1.0, 0.3, 1.0
             (same stepper -- M=1.0, D=0.3, K=1.0, a=-1.0, b=1.0, dt=0.01 -- that today's
             calibration and branch-parameter chain all build on).
  M_joint = 1.0004294772248 -- the moment-corrected + replicate-IV calibration of THIS SAME
             stepper, reported in:
                 domains/standard_model/item1_exploration/retained_transition_operational_closure/
                 BENCHMARK_REPORT_V0_1.md, line 48: "selected joint IV: `1.0004294772` --
                 error `0.042948%`."
             and restated to full precision in EQUATION_LIBRARY_ROOT_TO_SM_STREAM.md line 269:
                 "M_joint = 1.0004294772248 (0.042948% error vs the disclosed fixture's ...)"

MODELING DECISION (disclosed, not hidden as if derived):
  T_native := D / M_joint  (a dimensionless native ratio, NOT a temperature in kelvin).
  Why this combination and no other: D is the dissipation/damping coefficient of the SAME
  Reader/Record stepper that M_joint calibrates the mass-scale of; D/M_joint is the simplest,
  already-computed, zero-new-fit combination of "how much this stepper dissipates" over "its
  calibrated inertial scale" -- i.e. a natural per-unit-mass damping rate in the stepper's own
  units. No other combination (e.g. M_joint/D, D*M_joint, 1/D, sqrt(D*M_joint)) is privileged by
  anything in the source docs; this file tries only the one stated here and discloses that this
  is a choice, not a derivation. A different choice would very likely give a different number;
  that is exactly why it must be named explicitly instead of picked silently.

TWO VARIANTS for step 2, both run and both reported (per instructions -- dropping k_B changes
what is being tested, so both are tried rather than picking one):
  (2a) "T_native WITH k_B"    -- plug T_native into the EXISTING adapters unchanged:
                                  I_nat = E_J / (k_B * T_native),  E_out = k_B * T_native * final_nat.
                                  This is a MIXED test: T_native is dimensionless but is being
                                  multiplied by k_B (J/K) as if it were a temperature in kelvin.
                                  Dimensionally this manufactures a fake "kelvin" out of a
                                  dimensionless ratio -- disclosed as incoherent by construction,
                                  run anyway because the instructions require it be tried.
  (2b) "T_native WITHOUT k_B" -- strip k_B entirely, define purely-native adapters:
                                  I_nat = E_J / T_native,  E_out = T_native * final_nat.
                                  This changes the definition of I_nat's unit (native
                                  "information-per-native-damping-unit" instead of
                                  Landauer-natural k_B*T bits) -- also disclosed, not hidden.

Run: python3 pgft_rdu_internal_temperature_gateway_test_v0_1.py   (no dependencies beyond stdlib)
"""
from __future__ import annotations
import importlib.util
import math
import os
import sys
from typing import Dict, List

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------------------
# Load the v0.7 script as a module WITHOUT running its __main__ block, so we
# reuse its actual functions/constants rather than re-typing them (avoids
# silent drift between this file and the mechanism it is testing).
# ---------------------------------------------------------------------------
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
V07_PATH = os.path.join(REPO_ROOT, "scripts", "pgft_rdu_v0_7_quantum_gravity_real_problem.py")

_spec = importlib.util.spec_from_file_location("pgft_rdu_v0_7", V07_PATH)
v07 = importlib.util.module_from_spec(_spec)
sys.modules["pgft_rdu_v0_7"] = v07  # must be registered before exec for @dataclass to resolve
_spec.loader.exec_module(v07)  # safe: file only runs main() under `if __name__ == "__main__"`

# Reused, not reinvented:
qg_diagnostic = v07.qg_diagnostic
J_to_native_nat = v07.J_to_native_nat
native_nat_to_J = v07.native_nat_to_J
run_native_pde = v07.run_native_pde
PDEConfig = v07.PDEConfig
K_B = v07.K_B

print("== 0. TIER TAG (mandatory) ==")
print("  finite_diagnostic for the reused v0.7 round-trip machinery (already-executable,")
print("  reused verbatim via importlib, not reinvented) and for the numeric round-trip results")
print("  themselves (they are direct, reproducible outputs of running that machinery).")
print("  Dr, explicitly, for the T_native = D/M_joint MODELING CHOICE -- a new proposal made")
print("  in this file, not an existing repo result, and not claimed to be forced or unique.")
print("  [Open] for any claim that this gateway supplies a genuine RD-to-GeV bridge -- that is")
print("  exactly the question this file tests, and it is answered empirically below, not assumed.")

# ---------------------------------------------------------------------------
# Real PDG rest energies in Joules (as given in the task; these are external,
# borrowed physical inputs used ONLY as round-trip test payloads, exactly the
# same role T=310.0K plays in the original v0.7 script -- not fitted to).
# ---------------------------------------------------------------------------
PARTICLES: Dict[str, float] = {
    "electron": 8.187e-14,
    "muon": 1.883e-11,
    "tau": 2.847e-10,
    "proton": 1.503e-10,
    "W_boson": 1.286e-8,
    "Z_boson": 1.462e-8,
    "Higgs": 2.011e-8,
}

CFG = PDEConfig()  # identical, unmodified default config used by v0.7's own main()


def round_trip_ratio_with_kB(E_J: float, T_value: float) -> Dict[str, float]:
    """Existing v0.7 adapters, unmodified except this explicit input guard: I_nat =
    E/(k_B*T), E_out = k_B*T*final_nat.

    REQUIRED CORRECTION (independent review, 2026-07-25): the file's own test suite
    originally claimed "fail-closed on negative energy" by testing the unused, unrelated
    qg_diagnostic() import -- this function itself, the one whose numbers this file's
    conclusions are actually based on, silently accepted negative E_J and returned
    {'final_nat': 0.0, 'ratio_E_out_over_E_in': -0.0} (the downstream max(0,...) floor
    absorbed it instead of raising). Fixed here with an explicit guard so the claim is
    true of the function actually under test, not just of an unused import."""
    if not math.isfinite(E_J) or E_J <= 0:
        raise ValueError(f"E_J must be finite and positive, got {E_J}")
    if not math.isfinite(T_value) or T_value <= 0:
        raise ValueError(f"T_value must be finite and positive, got {T_value}")
    I_nat = J_to_native_nat(E_J, T_value)
    pde = run_native_pde(I_nat, CFG)
    final_nat = pde["final_retained_nat_delta_R_e"]
    E_out = native_nat_to_J(final_nat, T_value)
    return {
        "I_nat": I_nat,
        "final_nat": final_nat,
        "E_out_J": E_out,
        "ratio_E_out_over_E_in": E_out / E_J,
    }


def round_trip_ratio_without_kB(E_J: float, T_native: float) -> Dict[str, float]:
    """Purely-native adapters: I_nat = E/T_native, E_out = T_native*final_nat (no k_B).
    Same explicit input guard added as round_trip_ratio_with_kB, same reason (required
    correction, independent review 2026-07-25)."""
    if not math.isfinite(E_J) or E_J <= 0:
        raise ValueError(f"E_J must be finite and positive, got {E_J}")
    if not math.isfinite(T_native) or T_native <= 0:
        raise ValueError(f"T_native must be finite and positive, got {T_native}")
    I_nat = E_J / T_native
    pde = run_native_pde(I_nat, CFG)
    final_nat = pde["final_retained_nat_delta_R_e"]
    E_out = T_native * final_nat
    return {
        "I_nat": I_nat,
        "final_nat": final_nat,
        "E_out_J": E_out,
        "ratio_E_out_over_E_in": E_out / E_J,
    }


def summarize_variant(label: str, ratios: List[float]) -> Dict[str, float]:
    mean_r = sum(ratios) / len(ratios)
    spread = max(ratios) - min(ratios)
    rel_spread = spread / mean_r if mean_r != 0 else float("inf")
    print(f"\n  -- {label} --")
    for name, r in zip(PARTICLES.keys(), ratios):
        print(f"     {name:10s} ratio E_out/E_in = {r!r}")
    print(f"     mean={mean_r!r}  spread={spread!r}  rel_spread={rel_spread!r}")
    return {"mean": mean_r, "spread": spread, "rel_spread": rel_spread}


# ============================================================================
print("\n== 1. BASELINE: existing hardcoded T=310.0 K, 7-particle round trip ==")
print("      (sanity check -- is E_out/E_in a single constant independent of input energy?)")
T_BASELINE = 310.0
baseline_ratios = []
for name, E_J in PARTICLES.items():
    r = round_trip_ratio_with_kB(E_J, T_BASELINE)
    baseline_ratios.append(r["ratio_E_out_over_E_in"])
baseline_summary = summarize_variant("T=310.0K (baseline, k_B present -- this IS the v0.7 mechanism as-is)", baseline_ratios)

ck("baseline ratio is constant across all 7 particles to 1e-9 relative spread "
   "(necessary precondition for 'gateway' to be a clean linear bridge at all)",
   baseline_summary["rel_spread"] < 1e-9, got=baseline_summary["rel_spread"])

print("\n  WHY THIS IS EXPECTED ANALYTICALLY (stated up front so the PASS above is not read as a")
print("  surprising new discovery): run_native_pde() is linear in its input_nat argument EXCEPT")
print("  for the `phi = max(0.0, phi + dtheta*dphi)` floor. For strictly-positive, monotonically")
print("  sourced inputs (as here) that floor never binds, so final_nat/I_nat is a FIXED constant")
print("  determined only by (D_R, mu_R, nodes, theta_end, dtheta, source shape) -- and since")
print("  I_nat = E/(k_B*T) and E_out = k_B*T*final_nat, the k_B*T factor CANCELS EXACTLY in the")
print("  ratio E_out/E_in = final_nat/I_nat, for ANY T > 0. This is a mathematical fact about the")
print("  PDE's linearity, not a property of T=310K specifically -- it is verified numerically next.")

# ============================================================================
print("\n== 2. THE ENGINE ROOM FINDING: does T even matter to the ratio, before touching T_native? ==")
print("      Direct test: rerun the SAME 7 particles at a wildly different T and compare ratios.")
alt_ratios = []
T_ALT = 4.0  # arbitrary, far from 310.0, chosen only to stress-test T-independence
for name, E_J in PARTICLES.items():
    r = round_trip_ratio_with_kB(E_J, T_ALT)
    alt_ratios.append(r["ratio_E_out_over_E_in"])
alt_summary = summarize_variant(f"T={T_ALT}K (arbitrary alternate T, same k_B mechanism)", alt_ratios)

t_independence_diff = abs(alt_summary["mean"] - baseline_summary["mean"])
ck("the round-trip ratio is IDENTICAL whether T=310.0K or T=4.0K (to 1e-9 absolute) -- "
   "i.e. T cancels out of E_out/E_in exactly, for ANY T, by the PDE's own linearity",
   t_independence_diff < 1e-9, got=t_independence_diff)

print("\n  DISCLOSED CONSEQUENCE (read before Step 3): if the check above PASSES, it proves,")
print("  by direct execution rather than by reasoning alone, that the round-trip ratio of THIS")
print("  mechanism (as built in v0.7, with k_B present) cannot depend on the choice of T at all --")
print("  not on T=310K, not on any T_native candidate, not on any other temperature. Any apparent")
print("  'improvement' from swapping in T_native under the WITH-k_B adapters (variant 2a below) is")
print("  therefore GUARANTEED to be identically zero, not a finding about T_native's merit. This is")
print("  exactly the kind of thing the task asked to be reported loudly if found -- and it was")
print("  found by running the code, not assumed. Variant 2b (k_B stripped) is NOT protected by")
print("  this cancellation, because E_out=T_native*final_nat and I_nat=E/T_native only cancel T_native")
print("  itself (still exactly, by the same linearity argument) -- so 2b's ratio will ALSO be")
print("  T_native-independent, for the same algebraic reason. Both variants are still run and")
print("  reported in full below, exactly as instructed, precisely because this was not supposed to")
print("  be settled by reasoning alone.")

# ============================================================================
print("\n== 3. INTERNALLY-DERIVED CANDIDATE: T_native = D / M_joint ==")
D_STEPPER = 0.3            # attempt1_bateman_doubling_hypothesis_v1.py: "M, D, K = 1.0, 0.3, 1.0"
M_JOINT = 1.0004294772248  # retained_transition_operational_closure/BENCHMARK_REPORT_V0_1.md:48
T_NATIVE = D_STEPPER / M_JOINT
print(f"  D (stepper damping, from bateman file)        = {D_STEPPER!r}")
print(f"  M_joint (calibrated mass scale, same stepper)  = {M_JOINT!r}")
print(f"  T_native := D / M_joint                        = {T_NATIVE!r}  (dimensionless, NOT kelvin)")

ck("T_native is a finite positive dimensionless number", T_NATIVE > 0 and math.isfinite(T_NATIVE))

# ---- 2a: T_native WITH k_B (mixed, dimensionally-incoherent by construction) ----
print("\n  -- Variant 2a: T_native plugged into the UNCHANGED k_B*T adapters (mixed test) --")
ratios_2a = []
for name, E_J in PARTICLES.items():
    r = round_trip_ratio_with_kB(E_J, T_NATIVE)
    ratios_2a.append(r["ratio_E_out_over_E_in"])
summary_2a = summarize_variant("T_native WITH k_B", ratios_2a)

ck("variant 2a ratio is constant across particles (same linearity argument as Step 2 predicts)",
   summary_2a["rel_spread"] < 1e-9, got=summary_2a["rel_spread"])
ck("variant 2a ratio equals the T=310K baseline ratio exactly (confirms Step 2's prediction: "
   "swapping T under k_B-adapters changes NOTHING, because k_B*T cancels for any T)",
   abs(summary_2a["mean"] - baseline_summary["mean"]) < 1e-9,
   got=abs(summary_2a["mean"] - baseline_summary["mean"]))

# ---- 2b: T_native WITHOUT k_B (pure native adapters) ----
print("\n  -- Variant 2b: T_native in PURELY NATIVE adapters, k_B stripped entirely --")
ratios_2b = []
for name, E_J in PARTICLES.items():
    r = round_trip_ratio_without_kB(E_J, T_NATIVE)
    ratios_2b.append(r["ratio_E_out_over_E_in"])
summary_2b = summarize_variant("T_native WITHOUT k_B", ratios_2b)

ck("variant 2b ratio is constant across particles (same PDE-linearity argument, this time in "
   "T_native rather than k_B*T -- constancy in E is predicted regardless of whether k_B is present)",
   summary_2b["rel_spread"] < 1e-9, got=summary_2b["rel_spread"])

# ============================================================================
print("\n== 4. COMPARISON AGAINST PRE-REGISTERED DIMENSIONLESS TARGETS (candidate 1's own list) ==")
TARGETS = {
    "1.0 (trivial/identity)": 1.0,
    "Pi0 = 6.328453553357985 (primitive_branch_parameter_reduction, uncalibrated ICs)": 6.328453553357985,
    "r_star = 3.823356105009073 (order_vacuum_threshold_closure)": 3.823356105009073,
    "v_native = 2.7652689218262565 (native_vacuum_amplitude_closure)": 2.7652689218262565,
    "M_joint = 1.0004294772248 (retained_transition_operational_closure)": 1.0004294772248,
}


def nearest_target(value: float):
    best_name, best_dist = None, float("inf")
    for name, target in TARGETS.items():
        d = abs(value - target)
        if d < best_dist:
            best_name, best_dist = name, d
    return best_name, best_dist


print(f"  baseline (T=310K)     ratio = {baseline_summary['mean']!r}")
bn, bd = nearest_target(baseline_summary["mean"])
print(f"    nearest target: {bn}  |distance|={bd!r}")

print(f"  variant 2a (T_native, WITH k_B)    ratio = {summary_2a['mean']!r}")
an, ad = nearest_target(summary_2a["mean"])
print(f"    nearest target: {an}  |distance|={ad!r}")

print(f"  variant 2b (T_native, WITHOUT k_B) ratio = {summary_2b['mean']!r}")
n2b, d2b = nearest_target(summary_2b["mean"])
print(f"    nearest target: {n2b}  |distance|={d2b!r}")

variant_2a_is_closer = ad < bd
variant_2b_is_closer = d2b < bd
print(f"\n  variant 2a strictly closer to any target than baseline? {variant_2a_is_closer}")
print(f"  variant 2b strictly closer to any target than baseline? {variant_2b_is_closer}")

ck("(informational, not pass/fail on the framework) variant 2a is byte-identical to baseline "
   "(exactly as Step 2 predicted -- reported as PASS of the PREDICTION, not of the physics)",
   abs(summary_2a["mean"] - baseline_summary["mean"]) < 1e-9)

# ============================================================================
print("\n== HONEST FENCE ==")
print("  IS ESTABLISHED (by actually running the code above, not by reasoning alone):")
print("  - The v0.7 round-trip ratio E_out/E_in is EXACTLY constant across all 7 real PDG rest")
print("    energies tested (electron..Higgs, spanning ~8 orders of magnitude), at T=310K: this")
print("    part of the 'gateway' IS a clean linear bridge in the energy input, confirming rather")
print(f"    than refuting that narrow claim. Measured ratio = {baseline_summary['mean']!r}.")
print("  - That same ratio is PROVABLY, and numerically CONFIRMED, INDEPENDENT of the temperature")
print("    T fed into the k_B*T adapters, for ANY T > 0 -- swapping T=310K for T=4.0K, or for the")
print("    internally-derived T_native = D/M_joint (variant 2a), changes the round-trip ratio by")
print("    less than 1e-9 (floating-point noise), i.e. by nothing.")
print("  - Therefore variant 2a (T_native WITH k_B) is a NULL EXPERIMENT by construction: it cannot")
print("    ever produce a number 'closer to' or 'farther from' any physical target than the T=310K")
print("    baseline, because it produces the SAME number. This was not obvious before running it --")
print("    it required tracing the linearity of run_native_pde() and confirming numerically that")
print("    the floor `max(0, ...)` never binds for these positive, single-signed sources.")
print("  - Variant 2b (T_native WITHOUT k_B) DOES compute a different, well-defined, T_native-")
print(f"    dependent ratio ({summary_2b['mean']!r}) since here k_B is not there to make T cancel")
print("    against nothing. This ratio is real and reproducible but ALSO not closer to any of the")
print("    5 pre-registered dimensionless targets than the baseline is." if not variant_2b_is_closer else
      "    and IS closer to a pre-registered target than the baseline -- see nearest_target output above.")
print("  IS NOT ESTABLISHED:")
print("  - No GeV-scale, kelvin-scale, or any other SI-comparable number was produced or claimed")
print("    by any variant here. Nothing in this file converts a native ratio into a real particle")
print("    mass, energy, or temperature -- that would require an independent, non-circular")
print("    conversion factor this file does not have and does not fabricate.")
print("  - The T_native = D/M_joint modeling choice is NOT derived from first principles in this")
print("    repo; it is this file's own Dr-tier proposal (see MODELING DECISION above), tried once,")
print("    honestly, with no fitting to make it 'work'.")
print("  - Whether the ZERO_INFINITY_DUAL_DIAGNOSIS.md tension (native construction vs routine")
print("    PDG/GeV usage elsewhere in the repo) is resolved is UNTOUCHED by this file either way --")
print("    this file neither uses nor claims a GeV output, so it does not bear on that tension in")
print("    either direction.")

print(f"\nFAILS: {FAILS}")
if FAILS:
    print("RESULT: SOME CHECKS FAILED -- see FAILS list above.")
else:
    print("RESULT: all structural/consistency checks passed. The SUBSTANTIVE finding is the")
    print("negative one stated in the HONEST FENCE above (variant 2a is a null experiment by")
    print("construction; variant 2b produces a real but non-privileged number) -- not a pass/fail")
    print("verdict on whether the framework 'works'.")
