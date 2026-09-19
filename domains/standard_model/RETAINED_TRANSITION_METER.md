# Retained Transition Meter v0.1

> **Tier:** `calibrated_readout / finite_diagnostic`  
> **Claim boundary:** this tool measures an exchange rate and transition costs from the supplied tape. It does **not** derive a universal constant from the unrestricted root and does **not** turn a calibrated value into a root theorem.

## Purpose

The reader/record action already contains

\[
\mathcal L^n_{\rm exchange}=\frac{1}{\Delta t}\,\Delta\Phi_n^T M_n\Delta\Psi_n.
\]

The missing practical object was one meter that preserves a single encoding through the complete calculation:

```text
same tape events
  -> reader/record exchange rate M
  -> event retained load c_n
  -> primitive-path cost Delta_eff
  -> lambda = exp(-Delta_eff)
  -> Pi0 = 3 lambda_U + 3 lambda_D + lambda_E
```

This closes an **instrumentation gap**, not the unrestricted-root derivation gap. It avoids Cross-Role Readout Contamination by refusing to infer a cost from a sign, rank, copy licence, physical mass, or unrelated graph eigenvalue. A cost is computed only from transitions explicitly present and branch/path-tagged in the same tape.

## Operational meaning

For the rearranged reader and record equations, supply

\[
y_{\Phi,n}=M\,\delta_t^2\Phi_n,
\qquad
y_{\Psi,n}=M\,\delta_t^2\Psi_n.
\]

The meter estimates the scalar exchange rate independently and jointly:

\[
\widehat M_\Phi=\frac{\sum a_{\Phi,n}^Ty_{\Phi,n}}
{\sum a_{\Phi,n}^Ta_{\Phi,n}},
\quad
\widehat M_\Psi=\frac{\sum a_{\Psi,n}^Ty_{\Psi,n}}
{\sum a_{\Psi,n}^Ta_{\Psi,n}}.
\]

For every transition inside one declared primitive path,

\[
c_n=\frac{\left|\Delta\Phi_n^T\widehat M\Delta\Psi_n\right|}
{\Delta t\,C_{\rm RD}},
\]

where `cost_unit_rd = C_RD > 0` is the declared native-RD calibration unit. The magnitude is used as non-negative retained load; the sign remains an orientation readout, not a cost.

For repeated observed paths in branch `j`,

\[
\Delta_j^{\rm eff}=\operatorname{median}_{p\in j}
\sum_{n\in p}c_n,
\qquad
\lambda_j=e^{-\Delta_j^{\rm eff}}.
\]

`Pi0` is emitted only when `U`, `D`, and `E` are all present.

## Input

The machine schema is [`retained_transition_tape_schema_v0_1.json`](retained_transition_tape_schema_v0_1.json). Each sample contains:

- `path_id`: one primitive observed path;
- `branch`: branch label, such as `U`, `D`, or `E`;
- `phi`, `psi`: reader and record vectors;
- `reader_load`, `record_load`: calibrated non-inertial sides; endpoints may be `null`.

For the core equations an adapter should calculate

\[
y_{\Phi,n}=\mathcal R_{\Phi,n}+J_n-D\delta_t^c\Phi_n
-K\mathbb G_n\Phi_n-\nabla V(\Phi_n),
\]

\[
y_{\Psi,n}=\mathcal R_{\Psi,n}+D\delta_t^c\Psi_n
-K\mathbb G_n^T\Psi_n-\nabla^2V(\Phi_n)\Psi_n.
\]

The adapter, units, and every supplied term remain calibration provenance.

## Fail-closed gates

A report passes only when:

1. `M` is positive and identifiable;
2. reader and record estimates agree within 5%;
3. held-out normalized RMSE is at most 10% in each channel;
4. rotating loads away from their events performs at least three times worse;
5. costs are non-negative and every emitted `lambda` lies in `(0,1]`;
6. the built-in simulated fixture recovers hidden `M` within 1%.

Near-zero acceleration, missing path interiors, dimension mismatch, or a zero target scale produces a hard failure. No silent regularization is used.

## Run

```bash
# deterministic simulated fixture; run_tests.py uses this mode
python3 retained_transition_meter_v0_1.py --pretty

# write the fixture to inspect the format
python3 retained_transition_meter_v0_1.py --demo --write-demo /tmp/rtm_demo.json --pretty

# calibrated or experimental tape
python3 retained_transition_meter_v0_1.py --input my_tape.json --pretty
```

The deterministic `[SimulatedData]` fixture hides `M_true=1.75` and currently recovers about `M_joint=1.74942`, roughly `0.033%` relative error. These are software-recovery values, not physical constants.

## Domino output

A passing real tape provides:

- `M.reader`, `M.record`, and `M.joint`;
- branch-local exchange-rate diagnostics;
- per-path retained load in the declared RD calibration;
- `Delta_eff` and `lambda` for every observed branch;
- `Pi0` for a complete `U/D/E` tape.

One measured exchange encoding therefore feeds downstream calculations without changing the meaning of an existing readout.

## Still open

- transport of a measured `M` between different systems;
- correctness of a future laboratory or QuTiP adapter;
- whether a branch encoding is the physical Standard-Model encoding;
- whether any measured value is forced by the root;
- `alpha`, `beta`, generation multiplicity, and physical mass/coupling claims not supplied by a calibrated tape.
