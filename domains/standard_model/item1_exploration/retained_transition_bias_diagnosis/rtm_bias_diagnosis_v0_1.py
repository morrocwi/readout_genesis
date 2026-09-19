#!/usr/bin/env python3
"""RTM bias diagnosis v0.1.

Diagnoses OLS attenuation in the scalar Reader/Record stepper under additive
observation noise. This is a finite diagnostic, not an estimator replacement.

It separates:
  * noisy-regressor / clean-target attenuation (EIV-only),
  * clean-regressor / noisy-target propagation,
  * first-order target-noise propagation,
  * full nonlinear noisy fit,
  * analytic second-difference attenuation prediction.
"""
from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import json
import math
from pathlib import Path
from typing import Dict, Iterable, Tuple

import numpy as np

DEFAULT_SIGMAS = (2e-6, 1e-5, 1e-4)
DEFAULT_SEED = 20260725
DEFAULT_MC_SEEDS = 200


def load_stepper():
    here = Path(__file__).resolve()
    path = here.parents[2] / "matter_antimatter_exploration" / "attempt1_bateman_doubling_hypothesis_v1.py"
    if not path.exists():
        raise FileNotFoundError(f"required existing stepper not found: {path}")
    spec = importlib.util.spec_from_file_location("attempt1_bateman_doubling_hypothesis_v1", path)
    module = importlib.util.module_from_spec(spec)
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        assert spec.loader is not None
        spec.loader.exec_module(module)
    return module, path, captured.getvalue()


def simulate(stepper, n_steps: int = 2000) -> Tuple[np.ndarray, np.ndarray]:
    phi = np.zeros(n_steps)
    psi = np.zeros(n_steps)
    phi[0], phi[1] = 1.0, 1.01
    psi[0], psi[1] = -1.0, -1.01
    for n in range(1, n_steps - 1):
        phi[n + 1] = stepper.step_reader(phi[n], phi[n - 1])
        psi[n + 1] = stepper.step_record(psi[n], psi[n - 1], phi[n])
    if not np.all(np.isfinite(phi)) or not np.all(np.isfinite(psi)):
        raise FloatingPointError("clean stepper trajectory is non-finite")
    return phi, psi


def diffs(x: np.ndarray, dt: float) -> Tuple[np.ndarray, np.ndarray]:
    d2 = (x[2:] - 2.0 * x[1:-1] + x[:-2]) / dt**2
    d1 = (x[2:] - x[:-2]) / (2.0 * dt)
    return d2, d1


def fit_ratio(acc: np.ndarray, target: np.ndarray) -> float:
    den = float(np.dot(acc, acc))
    return float(np.dot(acc, target) / den) if den > 0.0 else float("nan")


def clean_terms(stepper, phi: np.ndarray, psi: np.ndarray) -> Dict[str, np.ndarray]:
    dt, D, K = float(stepper.dt), float(stepper.D), float(stepper.K)
    acc_phi, d1_phi = diffs(phi, dt)
    acc_psi, d1_psi = diffs(psi, dt)
    y_phi = -D * d1_phi - K * phi[1:-1] - stepper.gradV(phi[1:-1])
    y_psi = D * d1_psi - K * psi[1:-1] - stepper.grad2V(phi[1:-1]) * psi[1:-1]
    return {"acc_phi": acc_phi, "acc_psi": acc_psi, "y_phi": y_phi, "y_psi": y_psi}


def one_noise_realization(stepper, phi: np.ndarray, psi: np.ndarray, clean: Dict[str, np.ndarray],
                          sigma: float, seed: int) -> Dict[str, float]:
    rng = np.random.default_rng(seed)
    eps_phi = rng.normal(0.0, sigma, len(phi))
    eps_psi = rng.normal(0.0, sigma, len(psi))
    phi_obs, psi_obs = phi + eps_phi, psi + eps_psi
    dt, D, K = float(stepper.dt), float(stepper.D), float(stepper.K)

    acc_phi_obs, d1_phi_obs = diffs(phi_obs, dt)
    acc_psi_obs, d1_psi_obs = diffs(psi_obs, dt)
    y_phi_obs = -D * d1_phi_obs - K * phi_obs[1:-1] - stepper.gradV(phi_obs[1:-1])
    y_psi_obs = D * d1_psi_obs - K * psi_obs[1:-1] - stepper.grad2V(phi_obs[1:-1]) * psi_obs[1:-1]

    d1_eps_phi = (eps_phi[2:] - eps_phi[:-2]) / (2.0 * dt)
    d1_eps_psi = (eps_psi[2:] - eps_psi[:-2]) / (2.0 * dt)
    onsite = K + stepper.grad2V(phi[1:-1])
    y_phi_linear = clean["y_phi"] - D * d1_eps_phi - onsite * eps_phi[1:-1]
    hessian_slope = 6.0 * float(stepper.b) * phi[1:-1]
    y_psi_linear = (clean["y_psi"] + D * d1_eps_psi - onsite * eps_psi[1:-1]
                    - hessian_slope * psi[1:-1] * eps_phi[1:-1])

    return {
        "reader_full": fit_ratio(acc_phi_obs, y_phi_obs),
        "reader_eiv_only": fit_ratio(acc_phi_obs, clean["y_phi"]),
        "reader_target_only": fit_ratio(clean["acc_phi"], y_phi_obs),
        "reader_linearized": fit_ratio(acc_phi_obs, y_phi_linear),
        "record_full": fit_ratio(acc_psi_obs, y_psi_obs),
        "record_eiv_only": fit_ratio(acc_psi_obs, clean["y_psi"]),
        "record_target_only": fit_ratio(clean["acc_psi"], y_psi_obs),
        "record_linearized": fit_ratio(acc_psi_obs, y_psi_linear),
    }


def analytic_prediction(stepper, phi: np.ndarray, clean: Dict[str, np.ndarray], sigma: float) -> Dict[str, float]:
    dt = float(stepper.dt)
    n = len(phi) - 2
    noise_acc_power = n * 6.0 * sigma**2 / dt**4
    onsite = float(stepper.K) + stepper.grad2V(phi[1:-1])
    covariance_numerator = float(np.sum(2.0 * onsite * sigma**2 / dt**2))
    output = {"noise_acc_power": noise_acc_power, "covariance_numerator": covariance_numerator}
    for channel, key in (("reader", "acc_phi"), ("record", "acc_psi")):
        signal = float(np.dot(clean[key], clean[key]))
        output[f"{channel}_acceleration_energy"] = signal
        output[f"{channel}_attenuation_prediction"] = signal / (signal + noise_acc_power)
        output[f"{channel}_first_order_prediction"] = (
            float(stepper.M) * signal + covariance_numerator
        ) / (signal + noise_acc_power)
        output[f"{channel}_noise_floor_ratio"] = signal / noise_acc_power if noise_acc_power > 0 else float("inf")
    return output


def finite_stats(values: Iterable[float]) -> Dict[str, float]:
    arr = np.asarray([x for x in values if math.isfinite(float(x))], dtype=float)
    if arr.size == 0:
        return {"mean": float("nan"), "median": float("nan"), "std": float("nan"), "n": 0}
    return {"mean": float(arr.mean()), "median": float(np.median(arr)), "std": float(arr.std()), "n": int(arr.size)}


def diagnose(mc_seeds: int = DEFAULT_MC_SEEDS) -> Dict[str, object]:
    stepper, stepper_path, captured = load_stepper()
    phi, psi = simulate(stepper)
    clean = clean_terms(stepper, phi, psi)
    clean_reader_error = float(np.max(np.abs(clean["y_phi"] - float(stepper.M) * clean["acc_phi"])))
    clean_record_error = float(np.max(np.abs(clean["y_psi"] - float(stepper.M) * clean["acc_psi"])))

    sweep = {}
    gates = {
        "clean_reader_equation_exact": clean_reader_error < 1e-8,
        "clean_record_equation_exact": clean_record_error < 1e-8,
    }
    for sigma in DEFAULT_SIGMAS:
        deterministic = one_noise_realization(stepper, phi, psi, clean, sigma, DEFAULT_SEED)
        analytic = analytic_prediction(stepper, phi, clean, sigma)
        runs = [one_noise_realization(stepper, phi, psi, clean, sigma, DEFAULT_SEED + i)
                for i in range(mc_seeds)]
        mc = {name: finite_stats(run[name] for run in runs) for name in deterministic}
        label = f"{sigma:.0e}"
        sweep[label] = {
            "sigma": sigma,
            "deterministic_seed": DEFAULT_SEED,
            "deterministic": deterministic,
            "analytic": analytic,
            "monte_carlo": mc,
            "decomposition": {
                "reader_full_minus_eiv_only": deterministic["reader_full"] - deterministic["reader_eiv_only"],
                "reader_full_minus_linearized": deterministic["reader_full"] - deterministic["reader_linearized"],
                "record_full_minus_eiv_only": deterministic["record_full"] - deterministic["record_eiv_only"],
                "record_full_minus_linearized": deterministic["record_full"] - deterministic["record_linearized"],
            },
        }
        for channel in ("reader", "record"):
            pred = analytic[f"{channel}_first_order_prediction"]
            mean_full = mc[f"{channel}_full"]["mean"]
            gates[f"{label}_{channel}_analytic_matches_mc"] = abs(mean_full - pred) <= 0.02
            gates[f"{label}_{channel}_target_only_near_true"] = abs(
                mc[f"{channel}_target_only"]["mean"] - float(stepper.M)
            ) <= 0.005
            gates[f"{label}_{channel}_higher_order_nonlinear_small"] = abs(
                mc[f"{channel}_full"]["mean"] - mc[f"{channel}_linearized"]["mean"]
            ) <= 0.005

    reader_energy = float(np.dot(clean["acc_phi"], clean["acc_phi"]))
    record_energy = float(np.dot(clean["acc_psi"], clean["acc_psi"]))
    energy_ratio = record_energy / reader_energy
    gates["record_acceleration_energy_gt_100x_reader"] = energy_ratio > 100.0
    gates["all_diagnostic_gates"] = all(gates.values())

    return {
        "schema": "rtm-bias-diagnosis-report-v0.1",
        "tier": "finite_diagnostic / candidate",
        "claim_boundary": {
            "establishes": "For this disclosed scalar stepper fixture and tested noise range, OLS bias is dominated by second-difference regressor noise; Reader/Record asymmetry is explained primarily by acceleration-energy/SNR asymmetry.",
            "does_not_establish": "A universal bias law, a final corrected estimator, a physical value of M, or that nonlinear propagation is negligible for other potentials, trajectories, dimensions, or noise models.",
        },
        "provenance": {
            "stepper_path": str(stepper_path),
            "stepper_parameters": {"M": stepper.M, "D": stepper.D, "K": stepper.K, "dt": stepper.dt,
                                   "a": stepper.a, "b": stepper.b},
            "stepper_import_stdout_lines_captured": len(captured.splitlines()),
            "trajectory": {"n_steps": len(phi), "phi0": phi[0], "phi1": phi[1], "psi0": psi[0], "psi1": psi[1]},
            "observation_noise": "independent iid Gaussian noise added separately to recorded Phi and Psi",
            "monte_carlo_seeds": mc_seeds,
        },
        "clean_equation_max_error": {"reader": clean_reader_error, "record": clean_record_error},
        "acceleration_energy": {"reader": reader_energy, "record": record_energy, "record_to_reader_ratio": energy_ratio},
        "sweep": sweep,
        "interpretation": {
            "primary_mechanism": "classical errors-in-variables attenuation caused by d2 observation noise scaling as sigma/dt^2",
            "asymmetry_mechanism": "Record has far larger clean acceleration energy on this anti-damped trajectory, so the same noise power produces much less attenuation than for the settled Reader trajectory",
            "nonlinear_mechanism": "Full nonlinear and first-order-linearized fits are nearly identical over the tested range; nonlinear target propagation is secondary here, not ruled out elsewhere",
            "next_estimator_decision": "Do not choose EIV/state-space implementation until tested on multiple trajectories. Any candidate must model latent states or known derivative-noise covariance and must fail near the identifiability threshold.",
        },
        "gates": gates,
        "decision": "PASS" if gates["all_diagnostic_gates"] else "FAIL",
    }


def print_pretty(report: Dict[str, object]) -> None:
    print("RTM Bias Diagnosis v0.1")
    print(f"decision: {report['decision']}")
    energy = report["acceleration_energy"]
    print(f"acceleration energy Reader={energy['reader']:.6f}, Record={energy['record']:.6f}, ratio={energy['record_to_reader_ratio']:.2f}x")
    print("sigma      Reader(full/eiv/target)       Record(full/eiv/target)      analytic(first-order)")
    for item in report["sweep"].values():
        d, a = item["deterministic"], item["analytic"]
        print(f"{item['sigma']:<10.1e} "
              f"{d['reader_full']:.6f}/{d['reader_eiv_only']:.6f}/{d['reader_target_only']:.6f}   "
              f"{d['record_full']:.6f}/{d['record_eiv_only']:.6f}/{d['record_target_only']:.6f}   "
              f"{a['reader_first_order_prediction']:.6f}/{a['record_first_order_prediction']:.6f}")
    print("primary mechanism:", report["interpretation"]["primary_mechanism"])
    print("asymmetry mechanism:", report["interpretation"]["asymmetry_mechanism"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pretty", action="store_true")
    parser.add_argument("--mc-seeds", type=int, default=DEFAULT_MC_SEEDS)
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.mc_seeds < 20:
        raise SystemExit("--mc-seeds must be at least 20")
    report = diagnose(args.mc_seeds)
    if args.pretty:
        print_pretty(report)
    else:
        print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
    if args.output:
        Path(args.output).write_text(json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    return 0 if report["decision"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
