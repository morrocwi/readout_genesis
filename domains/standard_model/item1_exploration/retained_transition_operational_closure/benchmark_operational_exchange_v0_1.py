#!/usr/bin/env python3
"""Reproducible 500-pair-seed benchmark for RTM operational exchange closure v0.1.

Runs the repository's existing Reader/Record stepper once, then measures raw OLS,
known-noise moment correction, independent-replicate IV, and the fail-closed selected
joint coefficient across disclosed iid-noise levels.

Tier: finite_diagnostic benchmark of the existing scalar fixture; not laboratory validation.
"""
from __future__ import annotations

import json
import math
from statistics import mean, median

import numpy as np

from operational_exchange_closure_v0_1 import (
    load_stepper,
    noisy_pair,
    reader_ay,
    record_ay,
    simulate,
)
from operational_exchange_estimator_v0_1 import (
    combine_reader_record,
    fit_moment_corrected,
    fit_replicate_iv,
)

N_SEED_PAIRS = 500
BASE_SEED = 20260725
NOISE_LEVELS = (2e-6, 5e-6, 1e-5, 2e-5, 5e-5, 1e-4)


def quantile(values, q):
    return float(np.quantile(np.asarray(values, dtype=float), q))


def summarize(values, true_value=1.0):
    values = np.asarray(values, dtype=float)
    errors = np.abs(values - true_value)
    signed = values - true_value
    return {
        "n": int(len(values)),
        "mean_M": float(np.mean(values)),
        "mean_absolute_percent_error": float(100.0 * np.mean(errors)),
        "rmse_percent": float(100.0 * math.sqrt(float(np.mean(signed * signed)))),
        "median_absolute_percent_error": float(100.0 * np.median(errors)),
        "p95_absolute_percent_error": float(100.0 * quantile(errors, 0.95)),
        "maximum_absolute_percent_error": float(100.0 * np.max(errors)),
    }


def run_benchmark():
    stepper = load_stepper()
    phi, psi = simulate(stepper)
    true_M = float(stepper.M)
    results = {}

    for sigma in NOISE_LEVELS:
        values = {
            "reader_ols": [],
            "record_ols": [],
            "joint_moment_corrected": [],
            "joint_replicate_iv": [],
            "selected_joint": [],
        }
        ready_counts = {
            "joint_moment_corrected": 0,
            "joint_replicate_iv": 0,
            "selected_joint": 0,
        }

        for i in range(N_SEED_PAIRS):
            seed = BASE_SEED + 2 * i
            phi1, psi1 = noisy_pair(phi, psi, sigma, seed)
            phi2, psi2 = noisy_pair(phi, psi, sigma, seed + 1)

            ar1, yr1 = reader_ay(stepper, phi1)
            ap1, yp1 = record_ay(stepper, phi1, psi1)
            ar2, yr2 = reader_ay(stepper, phi2)
            ap2, yp2 = record_ay(stepper, phi2, psi2)

            reader_mc = fit_moment_corrected(
                ar1, yr1, obs_noise_sigma=sigma, dt=stepper.dt
            )
            record_mc = fit_moment_corrected(
                ap1, yp1, obs_noise_sigma=sigma, dt=stepper.dt
            )
            reader_iv = fit_replicate_iv(ar1, yr1, ar2, yr2)
            record_iv = fit_replicate_iv(ap1, yp1, ap2, yp2)

            joint_mc = combine_reader_record(reader_mc, record_mc)
            joint_iv = combine_reader_record(reader_iv, record_iv)
            selected = joint_iv if joint_iv["status"] == "CALIBRATED_READY" else joint_mc

            values["reader_ols"].append(float(reader_mc.M_ols))
            values["record_ols"].append(float(record_mc.M_ols))

            for name, report in (
                ("joint_moment_corrected", joint_mc),
                ("joint_replicate_iv", joint_iv),
                ("selected_joint", selected),
            ):
                if report["status"] == "CALIBRATED_READY":
                    ready_counts[name] += 1
                    values[name].append(float(report["M_joint"]))

        noise_report = {
            "sigma": sigma,
            "seed_pairs": N_SEED_PAIRS,
            "raw_reader_ols": summarize(values["reader_ols"], true_M),
            "raw_record_ols": summarize(values["record_ols"], true_M),
        }
        for name in (
            "joint_moment_corrected",
            "joint_replicate_iv",
            "selected_joint",
        ):
            noise_report[name] = {
                "ready_fraction": ready_counts[name] / N_SEED_PAIRS,
                "summary_on_ready_runs": (
                    summarize(values[name], true_M) if values[name] else None
                ),
            }
        results[f"{sigma:.0e}"] = noise_report

    return {
        "schema": "rtm-operational-exchange-benchmark-v0.1",
        "tier": "finite_diagnostic",
        "fixture": {
            "source": "existing Reader/Record stepper",
            "known_M": true_M,
            "n_steps": len(phi),
            "dt": float(stepper.dt),
            "initial_phi": [1.0, 1.01],
            "initial_psi": [-1.0, -1.01],
            "noise": "iid Gaussian observation noise",
            "base_seed": BASE_SEED,
            "seed_pairs_per_noise": N_SEED_PAIRS,
        },
        "results": results,
        "claim_boundary": [
            "actual repeated computation on the repository's existing scalar stepper",
            "not external laboratory validation",
            "error statistics are conditional on CALIBRATED_READY for fail-closed methods",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_benchmark(), indent=2, sort_keys=True))
