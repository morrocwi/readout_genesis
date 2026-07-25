#!/usr/bin/env python3
"""
RTM operational closure -- pipeline-completeness fixture, 2026-07-25.

*** TIER: DIAGNOSTIC_ONLY. This file makes NO physics claim. ***

WHAT THIS IS: a software/pipeline test. It runs the merged RTM operational-closure chain
(tape -> M_joint -> exchange_path -> branch lambdas -> Pi0) END TO END on THREE FICTIONAL
"branch" tapes, to confirm the pipeline itself computes without error and that the
`primitive_closure`/`Pi0` semantic gates in `operational_exchange_estimator_v0_1.py` behave as
designed when their declared preconditions ARE met.

WHAT THIS IS NOT, EXPLICITLY (read before using any number below for anything):
  - This does NOT build real "U/D/E branch" tapes in the physics sense. The toy scalar
    Reader/Record stepper (`attempt1_bateman_doubling_hypothesis_v1.py`) has no SU(3) color, no
    SU(2) weak-isospin structure, and no representation content whatsoever -- there is no root-
    native construction connecting it to up-type quarks, down-type quarks, or charged leptons.
    The three "branches" below are DISTINGUISHED ONLY by an arbitrary different initial condition
    (phi0) fed into the SAME undifferentiated stepper -- a convenient way to get three DIFFERENT
    numbers out of the pipeline, nothing more.
  - This is NOT item 1's own, already-established, fit_calibrated Pi0. That quantity
    (Pi0 ~= 6.9888, from `item1_fit_calibrated_v1.py`, Attempt 5, independently reviewed, PASSED)
    comes from REAL PDG fermion masses via `lambda_j = exp(-m_j/v_EW)` -- an entirely different,
    already-sourced computation that this file does not touch, extend, or supersede.
  - Item 1's actual root-derivation question for Delta_j (what FORCES a branch's primitive cost)
    remains fully Open (Attempts 10-17, ITEM1_EXPLORATION_LOG.md) -- nothing here bears on it.
  - This file exists because the founder asked to "continue" toward building U/D/E branch tapes
    after the RTM operational-closure merge (2026-07-25); independent triage (this same session)
    identified a real Cross-Role Readout Contamination risk in doing that literally (fabricating
    physics-labelled tapes from an apparatus with no representation content) and the founder chose
    the PIPELINE-TEST-ONLY framing instead -- this file is exactly that, and only that.

Run: python3 pipeline_completeness_fixture_v1.py
"""
from operational_exchange_closure_v0_1 import load_stepper, noisy_pair, reader_ay, record_ay
from operational_exchange_estimator_v0_1 import (
    combine_reader_record,
    exchange_path,
    fit_moment_corrected,
    fit_replicate_iv,
    pi0_from_branch_lambdas,
)

import numpy as np

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


# fictional fixture labels ONLY -- explicitly NOT physical branches, see docstring
FIXTURE_LABELS = ("U_fixture", "D_fixture", "E_fixture")
FIXTURE_PHI0 = {"U_fixture": 1.0, "D_fixture": 0.8, "E_fixture": 1.2}
SIGMA = 1e-5
BASE_SEED = 20260725


def simulate_from(stp, phi0, n_steps=2000):
    phi = np.zeros(n_steps)
    psi = np.zeros(n_steps)
    phi[0], phi[1] = phi0, phi0 * 1.01
    psi[0], psi[1] = -1.0, -1.01
    for n in range(1, n_steps - 1):
        phi[n + 1] = stp.step_reader(phi[n], phi[n - 1])
        psi[n + 1] = stp.step_record(psi[n], psi[n - 1], phi[n])
    return phi, psi


def run_one_fixture_branch(stp, phi0, seed):
    phi, psi = simulate_from(stp, phi0)
    phi1, psi1 = noisy_pair(phi, psi, SIGMA, seed)
    phi2, psi2 = noisy_pair(phi, psi, SIGMA, seed + 1)

    ar1, yr1 = reader_ay(stp, phi1)
    ap1, yp1 = record_ay(stp, phi1, psi1)
    ar2, yr2 = reader_ay(stp, phi2)
    ap2, yp2 = record_ay(stp, phi2, psi2)

    reader_iv = fit_replicate_iv(ar1, yr1, ar2, yr2)
    record_iv = fit_replicate_iv(ap1, yp1, ap2, yp2)
    reader_mc = fit_moment_corrected(ar1, yr1, obs_noise_sigma=SIGMA, dt=stp.dt)
    record_mc = fit_moment_corrected(ap1, yp1, obs_noise_sigma=SIGMA, dt=stp.dt)
    joint_iv = combine_reader_record(reader_iv, record_iv)
    joint = joint_iv if joint_iv["status"] == "CALIBRATED_READY" else combine_reader_record(reader_mc, record_mc)

    if joint["status"] != "CALIBRATED_READY":
        return {"label": None, "M_joint": None, "path": None, "status": joint["status"]}

    m_value = joint["M_joint"]
    path = exchange_path(
        phi, psi, np.arange(len(phi)) * stp.dt,
        M_value=float(m_value),
        cost_unit_rd=1.0,
        # deliberately declared to exercise the gate's TRUE branch -- see honest fence below for
        # why this declaration is a PIPELINE-TEST fiction, not a real primitive-closure claim
        path_semantics="primitive_closure",
        delta_is_dimensionless=True,
    )
    return {"M_joint": m_value, "path": path, "status": joint["status"]}


print("== 0. TIER TAG (mandatory) ==")
print("  DIAGNOSTIC_ONLY -- pipeline plumbing test, zero physical U/D/E content. See module")
print("  docstring for the full disclosure before using any number below.")

print("\n== 1. run the full closure chain on 3 fixture branches (fictional labels only) ==")
stp = load_stepper()
results = {}
for i, label in enumerate(FIXTURE_LABELS):
    r = run_one_fixture_branch(stp, FIXTURE_PHI0[label], BASE_SEED + 100 * i)
    results[label] = r
    if r["status"] == "CALIBRATED_READY":
        print(f"   {label}: M_joint={r['M_joint']:.6f}  path_status={r['path']['status']}  "
              f"Delta_candidate={r['path']['Delta_candidate']:.4f}  lambda={r['path']['lambda']:.6e}")
    else:
        print(f"   {label}: UNRESOLVED ({r['status']})")

ck("all 3 fixture branches reach CALIBRATED_READY at this disclosed noise level (pipeline runs "
   "end to end without a gate refusal at this sigma, confirming the chain is wired correctly)",
   all(r["status"] == "CALIBRATED_READY" for r in results.values()),
   {k: v["status"] for k, v in results.items()})

print("\n== 2. lambda_j values land in the required (0,1] domain the Pi0 API enforces ==")
lambdas = {}
if all(r["status"] == "CALIBRATED_READY" for r in results.values()):
    for label in FIXTURE_LABELS:
        lambdas[label] = results[label]["path"]["lambda"]
    ck("every fixture lambda_j is in (0,1]",
       all(0 < v <= 1 for v in lambdas.values()), lambdas)

print("\n== 3. pi0_from_branch_lambdas() accepts the fixture and computes without error ==")
Pi0_fixture = None
if len(lambdas) == 3:
    branch_map = {"U": lambdas["U_fixture"], "D": lambdas["D_fixture"], "E": lambdas["E_fixture"]}
    Pi0_fixture = pi0_from_branch_lambdas(branch_map)
    print(f"   Pi0_fixture = {Pi0_fixture:.6e}  (pipeline-test number, NOT a physics result)")
    ck("Pi0_fixture computed without raising (API accepted 3 in-range lambdas)",
       Pi0_fixture is not None)
    ck("Pi0_fixture respects the no-go ceiling Pi0<=7 the same way the real formula does "
       "(same arithmetic form, sanity check only)", Pi0_fixture <= 7.0 + 1e-9, Pi0_fixture)

print("\n== 4. REQUIRED negative check: this fixture Pi0 must NOT collide with item 1's real, "
      "already-established fit_calibrated Pi0 (guards against exactly the confusion this file "
      "exists to prevent) ==")
# item1_fit_calibrated_v1.py's actual reported value, hardcoded here ONLY as a disclosed
# cross-check target (not recomputed -- recomputing PDG masses is out of scope for a pipeline test)
ITEM1_REAL_PI0_REPORTED = 6.9888
if Pi0_fixture is not None:
    ck("Pi0_fixture is numerically far from item 1's real fit_calibrated Pi0 (~6.9888) -- "
       "if these ever collided it would be a coincidence worth investigating, not evidence of a "
       "shared root, since the two are computed by unrelated formulas from unrelated data",
       abs(Pi0_fixture - ITEM1_REAL_PI0_REPORTED) > 0.5, (Pi0_fixture, ITEM1_REAL_PI0_REPORTED))

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print(f"""
HONEST FENCE (DIAGNOSTIC_ONLY -- no physics tier applies to any number in this file):

- WHAT THIS ESTABLISHES: the merged RTM operational-closure chain (tape -> M_joint ->
  exchange_path -> branch lambdas -> Pi0) is WIRED CORRECTLY and runs end to end without error on
  a 3-branch fixture, including the `primitive_closure`/dimensionless-Delta declaration gate and
  the `pi0_from_branch_lambdas` (0,1]-domain and no-go-ceiling checks. This is a software-pipeline
  completeness result, nothing more.
- WHAT THIS DOES NOT ESTABLISH: any physical content for "U/D/E branches" from this apparatus.
  The three fixture tapes differ ONLY by an arbitrary phi0 initial condition on the SAME toy
  scalar stepper -- there is no SU(3)/SU(2) representation structure anywhere in this
  construction, so `Pi0_fixture` above is NOT a candidate value for the real order-vacuum
  criterion (Pi0>alpha) and must never be cited as one. Item 1's real Pi0 (~6.9888,
  `item1_fit_calibrated_v1.py`) is unrelated and unaffected by this file.
- Item 1's root-derivation question for Delta_j (what a branch's primitive cost actually IS,
  from root primitives) remains fully Open -- Attempts 10-17 already searched exhaustively and
  found no root-native source; this pipeline test does not reopen or touch that search.
- If real primitive U/D/E branch tapes are ever wanted (i.e. tapes with an actual root-native
  connection to color/weak representation content), that requires solving item 1's still-open
  derivation problem first -- not running the existing toy stepper three more times.
""")
