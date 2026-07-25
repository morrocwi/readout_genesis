#!/usr/bin/env python3
"""Executable operational-closure fixture for the RTM exchange coefficient."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path

import numpy as np

from operational_exchange_estimator_v0_1 import (
    combine_reader_record,
    exchange_path,
    fit_moment_corrected,
    fit_replicate_iv,
)


def load_stepper():
    here = Path(__file__).resolve()
    path = here.parents[2] / "matter_antimatter_exploration" / "attempt1_bateman_doubling_hypothesis_v1.py"
    if not path.exists():
        raise FileNotFoundError(path)
    spec = importlib.util.spec_from_file_location("attempt1_stepper_for_operational_closure", path)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


def simulate(stepper, n_steps=2000):
    phi = np.zeros(n_steps)
    psi = np.zeros(n_steps)
    phi[0], phi[1] = 1.0, 1.01
    psi[0], psi[1] = -1.0, -1.01
    for n in range(1, n_steps - 1):
        phi[n + 1] = stepper.step_reader(phi[n], phi[n - 1])
        psi[n + 1] = stepper.step_record(psi[n], psi[n - 1], phi[n])
    return phi, psi


def reader_ay(stepper, phi_obs):
    dt = stepper.dt
    d2 = (phi_obs[2:] - 2 * phi_obs[1:-1] + phi_obs[:-2]) / dt**2
    d1 = (phi_obs[2:] - phi_obs[:-2]) / (2 * dt)
    y = -stepper.D * d1 - stepper.K * phi_obs[1:-1] - stepper.gradV(phi_obs[1:-1])
    return d2, y


def record_ay(stepper, phi_obs, psi_obs):
    dt = stepper.dt
    d2 = (psi_obs[2:] - 2 * psi_obs[1:-1] + psi_obs[:-2]) / dt**2
    d1 = (psi_obs[2:] - psi_obs[:-2]) / (2 * dt)
    y = stepper.D * d1 - stepper.K * psi_obs[1:-1] - stepper.grad2V(phi_obs[1:-1]) * psi_obs[1:-1]
    return d2, y


def noisy_pair(phi, psi, sigma, seed):
    rng = np.random.default_rng(seed)
    return phi + rng.normal(0.0, sigma, len(phi)), psi + rng.normal(0.0, sigma, len(psi))


def run_fixture(sigma=1e-5, seed=20260725):
    stepper = load_stepper()
    phi, psi = simulate(stepper)
    phi1, psi1 = noisy_pair(phi, psi, sigma, seed)
    phi2, psi2 = noisy_pair(phi, psi, sigma, seed + 1)

    ar1, yr1 = reader_ay(stepper, phi1)
    ap1, yp1 = record_ay(stepper, phi1, psi1)
    ar2, yr2 = reader_ay(stepper, phi2)
    ap2, yp2 = record_ay(stepper, phi2, psi2)

    reader_mc = fit_moment_corrected(ar1, yr1, obs_noise_sigma=sigma, dt=stepper.dt)
    record_mc = fit_moment_corrected(ap1, yp1, obs_noise_sigma=sigma, dt=stepper.dt)
    reader_iv = fit_replicate_iv(ar1, yr1, ar2, yr2)
    record_iv = fit_replicate_iv(ap1, yp1, ap2, yp2)
    joint_mc = combine_reader_record(reader_mc, record_mc)
    joint_iv = combine_reader_record(reader_iv, record_iv)

    chosen = joint_iv if joint_iv["status"] == "CALIBRATED_READY" else joint_mc
    m_value = chosen["M_joint"]
    path = None
    if m_value is not None:
        path = exchange_path(
            phi, psi, np.arange(len(phi)) * stepper.dt,
            M_value=float(m_value),
            cost_unit_rd=1.0,
            path_semantics="observed_trajectory",
            delta_is_dimensionless=True,
        )
    return {
        "schema": "rtm-operational-closure-report-v0.1",
        "tier": "calibrated_readout / finite_diagnostic",
        "known_fixture_M": float(stepper.M),
        "noise_sigma": sigma,
        "moment_corrected": {
            "reader": reader_mc.__dict__,
            "record": record_mc.__dict__,
            "joint": joint_mc,
        },
        "replicate_iv": {
            "reader": reader_iv.__dict__,
            "record": record_iv.__dict__,
            "joint": joint_iv,
        },
        "selected_joint": chosen,
        "path_diagnostic": path,
        "claim_boundary": [
            "operational coefficient for declared tape/noise model only",
            "not unrestricted-root derivation",
            "not primitive-cost semantics unless path_semantics is independently closed",
            "Pi0 requires independent U/D/E primitive-closure branch tapes",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_fixture(), indent=2, sort_keys=True))
