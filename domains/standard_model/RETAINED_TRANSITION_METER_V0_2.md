# Retained Transition Meter v0.2 — isolated candidate

> **Tier:** `calibrated_readout / finite_diagnostic / candidate`  
> **Integration status:** standalone Draft-PR candidate; no `main` README, registry, claim boundary, or shared test runner is changed.  
> **Claim boundary:** values are measured from the supplied tape under its declared adapter and calibration. They are not derived from the unrestricted root and are not automatically physical Standard-Model parameters.

## What this candidate tests

The reader/record action contains an exchange term

\[
\mathcal L_{\mathrm{exchange}}^n
=\frac{1}{\Delta t}\Delta\Phi_n^T M_n\Delta\Psi_n.
\]

v0.2 asks an operational question: can one preserved event encoding carry a calculation continuously through

```text
sampled reader/record tape
  -> exchange-rate estimate M
  -> signed and absolute path exchange
  -> declared Delta_eff statistic
  -> lambda = exp(-Delta_eff)
  -> optional Pi0
```

It does not claim that the final semantic identification has been established. It supplies gates that can reject a proposed encoding before downstream numbers are used.

## What changed from candidate v0.1

### 1. Irregular sampling is first-class

Every sample carries an explicit `time`. The acceleration estimate uses the unequal-step three-point formula

\[
a_n\approx \frac{2}{h_0+h_1}
\left(\frac{x_{n+1}-x_n}{h_1}-\frac{x_n-x_{n-1}}{h_0}\right).
\]

The fixture deliberately gives different paths 31, 38, 47, and 56 samples over the same duration.

### 2. Adapter provenance is mandatory

Every tape declares:

- `source_id`
- `adapter_id`
- `calibration_id`

Interior loads may be supplied directly or as explicit core-term components:

\[
y_{\Phi}=\mathcal R_\Phi+J-D\delta_t^c\Phi-K\mathbb G\Phi-\nabla V,
\]

\[
y_{\Psi}=\mathcal R_\Psi+D\delta_t^c\Psi-K\mathbb G^T\Psi-\nabla^2V\,\Psi.
\]

The implementation uses a fixed sign contract and hard-fails if direct and component forms are both supplied for the same channel.

### 3. Transport is tested, not inferred from an in-path tail

The candidate reports:

- leave-one-path-out prediction;
- leave-one-branch-out prediction;
- path-local and branch-local estimates of `M` and their dispersion.

A global scalar `M` candidate fails if it cannot travel to an unseen path or branch within the declared error gates.

### 4. Segmentation sensitivity is measured

For each path,

\[
C_p=\sum_{n\in p}
\frac{|\Delta\Phi_n^T\widehat M\Delta\Psi_n|}
{\Delta t_n C_{\mathrm{RD}}}.
\]

The same path is re-evaluated at native resolution, stride 2, and stride 3. The worst relative change must be at most 10%. This is a finite diagnostic, not a continuum proof.

### 5. Meaning is locked before downstream output

The tape must explicitly declare one of:

- `path_semantics = primitive_closure`
- `path_semantics = observed_trajectory`

An observed trajectory may pass all instrument tests, but `lambda` and `Pi0` remain suppressed. They are emitted only when all gates pass **and** the source declares primitive-closure semantics.

The selected branch statistic is also explicit:

- `delta_mode = path_total`
- `delta_mode = rate_per_time`

The tape must also set `delta_is_dimensionless = true`, explicitly asserting that the declared calibration makes the selected statistic admissible inside `exp(-Delta)`. This prevents the tool from silently deciding whether path duration belongs to the meaning of `Delta_eff`.

### 6. Stronger controls

The candidate fits contaminated tapes and then scores them against genuine events:

1. one-step load shift inside each path;
2. complete load reversal inside each path;
3. load transfer from another path in the same branch.

It also applies a fixed signed coordinate permutation to every state and load. Scalar `M` and path costs must remain invariant to machine precision.

## Fail-closed gates

A candidate report passes only if:

- `M > 0`;
- reader and record estimates agree within 5%;
- full-fit joint NRMSE is at most 10%;
- worst leave-one-path-out joint NRMSE is at most 15%;
- worst leave-one-branch-out joint NRMSE is at most 20%;
- all three negative controls degrade sufficiently;
- signed orthogonal coordinate relabeling preserves `M` and cost;
- stride-2/3 path-cost discrepancy is at most 10%;
- all candidate lambdas lie in `(0,1]`;
- the deterministic software fixture recovers hidden `M` within 1%.

Missing provenance, duplicate times, non-positive intervals, inconsistent dimensions, insufficient independent paths, or zero acceleration rank are hard failures. No silent regularization is used.

## Current deterministic fixture result

The fixture uses `M_true = 1.75` and mixed direct/component adapters.

- recovered `M_joint ≈ 1.7500184`;
- relative recovery error ≈ `0.0011%`;
- full-fit joint NRMSE ≈ `0.274%`;
- worst leave-one-path-out NRMSE ≈ `0.351%`;
- worst leave-one-branch-out NRMSE ≈ `0.347%`;
- worst stride-2/3 cost discrepancy ≈ `3.76%`;
- one-step, reverse, and cross-path controls all degrade;
- coordinate relabeling gaps are at floating-point zero.

These results validate the software and the stated finite gates on the fixture. They do not validate a laboratory adapter or physical branch encoding.

## Files and commands

```bash
python3 retained_transition_meter_v0_2.py --pretty
python3 retained_transition_meter_v0_2.py --demo --write-demo /tmp/rtm_v02_demo.json --pretty
python3 retained_transition_meter_v0_2.py --input my_tape_v02.json --pretty
python3 test_retained_transition_meter_v0_2.py
```

Input contract: `retained_transition_tape_schema_v0_2.json`.

## Candidate comparison criteria

Parallel candidates should be compared on:

1. whether raw terms are transformed into loads with auditable signs and units;
2. leave-one-path and leave-one-branch transport;
3. segmentation and coordinate invariance;
4. whether path semantics are declared before `Delta_eff` is interpreted;
5. whether any held-out observable is predicted without being used in calibration;
6. whether a real QuTiP or laboratory adapter passes the same gates.

## Still open

- a real QuTiP or laboratory adapter;
- transport between genuinely different systems, not fixture branches;
- whether absolute exchange is the correct primitive closure load;
- whether a declared primitive-closure path matches the SM branch object;
- any root derivation of `M`, `cost_unit_rd`, `Delta`, `alpha`, or `beta`;
- any physical mass, coupling, generation, or end-to-end SM claim.

The test bundle also injects a branch-specific exchange rate into branch `E`; the global-scalar candidate must fail and the leave-one-branch gate must identify the incompatibility.
