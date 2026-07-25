#!/usr/bin/env python3
"""
RTM v3 (synthesis) -- tape_generator.py: builds a MULTI-PATH, branch-tagged (Phi, Psi) transition
tape using the REUSED stepper (`stepper_reuse.py`, identical to v1/candidate PR #26's already-
reviewed shim -- no changes here). This is v1's single-path generator extended to emit v0.1's
(readout_genesis PR #67) richer schema shape (path_id, branch, per-sample records) so the same
synthetic-but-grounded tape can exercise v0.1's median-across-paths / branch-aggregation logic,
which v1's single-path demo never exercised.

Each path is a genuinely SEPARATE run of the real reused stepper with different, disclosed initial
conditions -- not the same trajectory re-labeled. Branch labels (U/D/E) are ARBITRARY assignments
for demonstration purposes only (this is a scalar toy apparatus, not a real fermion-branch
computation) -- disclosed explicitly, matching v1's own "Pi_0 toy, not a real branch claim" fence.

Tier: N/A (synthetic data generation). Fits performed on this tape are fit_calibrated -- see
rtm_fit.py.
"""
import numpy as np

from . import stepper_reuse as stepper

# Same noise model and reasoning as v1's tape_generator.py (kept, not re-litigated): a noiseless
# tape makes the scalar LS fit algebraically exact pointwise, which would make every validation
# test vacuously trivial. Disclosed i.i.d. observation noise on TOP of the clean simulated
# trajectory (physics source terms R_Phi/R_Psi/J stay zero) makes the tests genuinely falsifiable.
DEFAULT_OBS_NOISE_SIGMA = 2e-6  # matches v1/PR#26's actual orchestrator call (rtm_v1.py), NOT that
# file's own function-default docstring value (2e-3) -- self-caught bug: an earlier draft of this
# file copied the wrong number from v1's function signature default instead of its actual call
# site, which made the noise floor ~1000x too large (dt^4=1e-8 makes the noise-floor gate very
# sensitive to sigma) and marked every path underdetermined. Fixed before commit, not silently.
DEFAULT_RNG_SEED = 20260725


def _one_path(n_steps, phi0, phi1, psi0, psi1, rng, obs_noise_sigma):
    dt = stepper.dt
    phi = np.zeros(n_steps)
    psi = np.zeros(n_steps)
    phi[0], phi[1] = phi0, phi1
    psi[0], psi[1] = psi0, psi1
    for n in range(1, n_steps - 1):
        phi[n + 1] = stepper.step_reader(phi[n], phi[n - 1])
        psi[n + 1] = stepper.step_record(psi[n], psi[n - 1], phi[n])
    if obs_noise_sigma > 0:
        phi = phi + rng.normal(0.0, obs_noise_sigma, size=n_steps)
        psi = psi + rng.normal(0.0, obs_noise_sigma, size=n_steps)
    if not np.all(np.isfinite(phi)) or not np.all(np.isfinite(psi)):
        raise FloatingPointError("tape generation produced non-finite values -- refusing to hand "
                                  "back a broken tape silently")
    return phi, psi


# Disclosed, arbitrary per-path initial conditions -- NOT fit to reproduce any real PDG mass
# hierarchy or any other external target; chosen only to give the 3 demo paths genuinely different
# trajectories so branch-level median aggregation has something non-degenerate to aggregate over.
DEMO_PATHS = [
    {"path_id": "U-path-0", "branch": "U", "phi0": 1.0, "phi1": 1.01, "psi0": -1.0, "psi1": -1.01},
    {"path_id": "U-path-1", "branch": "U", "phi0": 0.9, "phi1": 0.92, "psi0": -0.9, "psi1": -0.92},
    {"path_id": "D-path-0", "branch": "D", "phi0": 0.6, "phi1": 0.605, "psi0": -0.6, "psi1": -0.605},
    {"path_id": "D-path-1", "branch": "D", "phi0": 0.55, "phi1": 0.56, "psi0": -0.55, "psi1": -0.56},
    {"path_id": "E-path-0", "branch": "E", "phi0": 0.2, "phi1": 0.202, "psi0": -0.2, "psi1": -0.202},
]


def build_multipath_tape(n_steps: int = 1500, paths=None,
                          obs_noise_sigma: float = DEFAULT_OBS_NOISE_SIGMA,
                          rng_seed: int = DEFAULT_RNG_SEED) -> dict:
    """Builds a multi-path tape: dict with 'paths' -> list of per-path dicts, each carrying
    (path_id, branch, t, Phi, Psi, meta). Each path is an independent run of the reused stepper."""
    paths = paths if paths is not None else DEMO_PATHS
    rng = np.random.default_rng(rng_seed)
    dt = stepper.dt
    t = np.arange(n_steps) * dt

    out_paths = []
    for spec in paths:
        phi, psi = _one_path(n_steps, spec["phi0"], spec["phi1"], spec["psi0"], spec["psi1"],
                              rng, obs_noise_sigma)
        out_paths.append({
            "path_id": spec["path_id"],
            "branch": spec["branch"],
            "t": t,
            "Phi": phi,
            "Psi": psi,
            "J": np.zeros(n_steps),
            "R_Phi": np.zeros(n_steps),
            "R_Psi": np.zeros(n_steps),
        })

    meta = {
        "D": stepper.D, "K": stepper.K, "M": stepper.M, "dt": dt,
        "n_steps": n_steps, "obs_noise_sigma": obs_noise_sigma, "rng_seed": rng_seed,
        "n_paths": len(out_paths),
        "branches": sorted({p["branch"] for p in out_paths}),
        "G_Theta": "identity (G[Theta_n]=1, same simplification attempt1/v1 already disclose)",
        "disclosure": (
            "NEW multi-path synthetic tape for RTM v3 synthesis, NOT a recovery of any previously-"
            "cited repo result (7.6e-4 QuTiP, v1's own single-path numbers, or v0.1/PR#67's "
            "fixture). Branch labels U/D/E are ARBITRARY demonstration assignments on a scalar toy "
            "apparatus -- explicitly NOT a real fermion-branch computation, no PDG masses used "
            "anywhere in this generator."
        ),
    }
    return {"paths": out_paths, "meta": meta}
