# Native Vacuum-Amplitude Closure v0.1 — candidate

## Decision

Stacked on the order-vacuum threshold closure candidate. Converts the ordered minimum `r_star`
into a native-unit vacuum amplitude via the standard normalization convention `r = v^2/2`:

```text
v_native = sqrt(2 * r_star)
```

`v_native` is a COMPUTED OUTPUT of the closure chain, not a new free dial:

```text
M -> Delta_{U,D,E} -> lambda_{U,D,E} -> Pi0 -> alpha_order,beta_order -> r_star -> v_native
```

## Executed fixture result

```text
r_star     = 3.823356105009073
v_native   = 2.7652689218262565
```

Compared against the order-vacuum candidate's own known-`M_true=1` reconstruction:

```text
r_star_true   = 3.823379983152252
v_native_true = 2.7652775568294232
v_native relative error = 0.00031227%
```

## What this explicitly does NOT do — read before citing `v_native` anywhere else

**`v_native` is not in GeV, and no attempt is made here to put it in GeV.** The RD-to-GeV
conversion factor (`Lambda_RD_to_GeV`) is not derived, not approximated, and not set equal to any
physical constant — in particular it is never set so that `Lambda * v_native` lands near the real
246 GeV Higgs vacuum expectation value. Doing that would be a reverse-fit dressed up as a
prediction, which this project's own tier discipline forbids. Finding a real, independently
justified `Lambda_RD_to_GeV` (from an actual observable or bridge, not from matching the answer)
remains a fully open frontier — not attempted, not scoped further, in this candidate.

## Parameter-count statement

Cumulative operational/native subchain, none of these are free fitting dials anymore:

```text
M, C_RD, lambda_U, lambda_D, lambda_E, alpha_order, beta_order, v_native
8 -> 0 new/fitted dials in this native subchain
```

Still NOT reduced/eliminated by this or any prior candidate in this chain: the mother-potential
coefficients `a, b`; the RD-to-GeV conversion factor; the U/D/E branch initial conditions
(disclosed as arbitrary/uncalibrated in the primitive-branch candidate this stacks on); real SM
gauge couplings, Yukawa data, and any physical mass or coupling in SI/GeV units.

## Fail-closed conditions

`derive_native_vev` refuses (raises) when the upstream phase is not `ORDERED_READY`, or when
`r_star` is non-finite or non-positive — an amplitude has no meaning for an unordered/degenerate
vacuum. It never attaches a physical unit to its output.

## Files

- `native_vacuum_amplitude_v0_1.py` — bridge and fail-closed contract;
- `test_native_vacuum_amplitude_v0_1.py` — regression and adversarial gates.

## Run

```bash
cd domains/standard_model/item1_exploration/native_vacuum_amplitude_closure
python3 native_vacuum_amplitude_v0_1.py
python3 test_native_vacuum_amplitude_v0_1.py
```

## Tier and boundary

- `declared_finite_architecture / exact_bridge / calibrated_readout / finite_diagnostic`;
- candidate until independently reviewed;
- no auto-merge requested;
- inherits every upstream claim_boundary from `order_vacuum_threshold_closure_v0_1.py` unchanged,
  including the structural-guarantee disclosure on `ORDERED_READY` (see that candidate's own
  docs — `v_native` existing at all is downstream of an outcome that was already shown to be
  guaranteed by this stepper's potential sign, not by the branch-tape data);
- not a physical vacuum expectation value in GeV;
- not a prediction of the observed Higgs mass, gauge couplings, or vacuum scale in SI units.
