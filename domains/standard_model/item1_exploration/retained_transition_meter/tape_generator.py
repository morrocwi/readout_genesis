#!/usr/bin/env python3
"""
RTM v1 -- tape_generator.py: builds a NEW synthetic (Phi, Psi) transition tape using the REUSED
stepper (`stepper_reuse.py`) with disclosed initial conditions/length that are DIFFERENT from
attempt1_bateman_doubling_hypothesis_v1.py's own run, so this tape is never confused with, and
never claimed to reproduce, attempt1's own numbers or the repo's previously-cited 7.6e-4 QuTiP
result. This is a fresh synthetic tape, honestly labeled as such.

Scalar case only (d=1): Phi_n, Psi_n are scalars, matching attempt1's own stepper (which is scalar).
Theta_n / G[Theta_n] is the identity (G=1, "no graph"), same simplification attempt1 already
discloses taking -- not a new, unstated simplification introduced here.

Tier: N/A (synthetic data generation, not a physics claim). The RTM fit performed on this tape is
`fit_calibrated` tier -- see rtm_fit.py.
"""
import numpy as np

from . import stepper_reuse as stepper


def build_tape(n_steps: int, phi0: float, phi1: float, psi0: float, psi1: float, seed_note: str,
               obs_noise_sigma: float = 2e-3, rng_seed: int = 20260725) -> dict:
    """
    Builds a tape dict-of-arrays (Design's Tape contract) using the reused Reader/Record stepper.

    DISCLOSED NOISE MODEL (required, not decorative): the underlying physics remains noiseless
    (R_Phi=R_Psi=J=0, matching attempt1's own simplification exactly) -- but the exact simulated
    trajectory is a noiseless deterministic recurrence, so a raw noiseless tape makes the RTM
    scalar least-squares fit ALGEBRAICALLY EXACT pointwise (M*a_n = y_n holds to machine precision
    for every single n independently of order), which would make every one of the 5 required
    validation tests vacuously trivial (zero residual regardless of holdout/shuffle/transport --
    not because the fit is doing anything real, but because there is no misspecification for it to
    fail on). To make the 5 tests genuinely falsifiable (as required), i.i.d. Gaussian MEASUREMENT
    noise (NOT a physics source term -- disclosed as purely an observation/recording-noise model on
    what the tape stores, applied AFTER the clean simulation) is added to the recorded Phi/Psi
    values with std `obs_noise_sigma`, fixed `rng_seed` (both reported in tape meta for exact
    reproducibility). This is a standard, disclosed synthetic-benchmark choice, not a hidden
    assumption.

    Fields (all length N=n_steps, scalar d=1 case -> shape (N,) not (N,1), documented here):
      t:      (N,) timestamps, dt fixed = stepper.dt (reused, not re-chosen)
      Phi:    (N,) reader field, clean simulation + measurement noise (see above)
      Psi:    (N,) record field, clean simulation + measurement noise (see above)
      Theta:  None (G[Theta_n] = 1 identity, same simplification attempt1 already discloses)
      J:      (N,) source term, zero (matches attempt1's own R_Phi=R_Psi=J=0 simplification)
      R_Phi:  (N,) zero (the PHYSICS source term, not the observation noise -- kept separate)
      R_Psi:  (N,) zero
      meta:   dict recording D, K, dt, gradV/grad2V identity, and this tape's own disclosed params
    """
    dt = stepper.dt
    phi = np.zeros(n_steps)
    psi = np.zeros(n_steps)
    phi[0], phi[1] = phi0, phi1
    psi[0], psi[1] = psi0, psi1

    for n in range(1, n_steps - 1):
        phi[n + 1] = stepper.step_reader(phi[n], phi[n - 1])
        psi[n + 1] = stepper.step_record(psi[n], psi[n - 1], phi[n])

    rng = np.random.default_rng(rng_seed)
    if obs_noise_sigma > 0:
        phi = phi + rng.normal(0.0, obs_noise_sigma, size=n_steps)
        psi = psi + rng.normal(0.0, obs_noise_sigma, size=n_steps)

    t = np.arange(n_steps) * dt
    J = np.zeros(n_steps)
    R_Phi = np.zeros(n_steps)
    R_Psi = np.zeros(n_steps)

    meta = {
        "D": stepper.D,
        "K": stepper.K,
        "M": stepper.M,
        "dt": dt,
        "delta_t_c_order": 1,  # d_t^c in the Reader/Record eqns == first-order damping term, reused as-is
        "gradV_fn_id": "attempt1_bateman_doubling_hypothesis_v1.gradV (cubic double-well, reused unmodified)",
        "source": "synthetic_v1",
        "n_steps": n_steps,
        "phi0": phi0, "phi1": phi1, "psi0": psi0, "psi1": psi1,
        "seed_note": seed_note,
        "obs_noise_sigma": obs_noise_sigma, "rng_seed": rng_seed,
        "G_Theta": "identity (G[Theta_n]=1, same simplification attempt1 already discloses, not new here)",
        "disclosure": (
            "NEW synthetic tape built for RTM v1, NOT a recovery of any previously-cited repo result "
            "(e.g. the 7.6e-4 QuTiP number) and NOT attempt1's own run (different n_steps/init "
            "conditions, disclosed below) -- reuses attempt1's exact stepper functions unmodified."
        ),
    }

    if not np.all(np.isfinite(phi)) or not np.all(np.isfinite(psi)):
        raise FloatingPointError(
            "tape generation produced non-finite values -- refusing to hand back a broken tape silently"
        )

    return {
        "t": t, "Phi": phi, "Psi": psi, "Theta": None,
        "J": J, "R_Phi": R_Phi, "R_Psi": R_Psi, "meta": meta,
    }
