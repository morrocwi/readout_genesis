# RD-to-GeV Fit-Calibrated Bridge v0.1 — candidate

## Decision

Per the founder's own explicit direction (2026-07-25), following this project's standing
DEV-SM-001 precedent ("fit is fine, real SM fits ~19 values too" — see Attempt 17's `r_U,r_D,r_E`
fit): fits ONE physical-unit conversion factor `Lambda_RD_to_GeV` against ONE known physical
observable (`v=246 GeV`), then uses that SAME `Lambda` to compute an INDEPENDENT, non-circular
prediction of the Higgs mass from a quantity that was never used in the fit.

```text
Lambda_RD_to_GeV = v_physical_gev / v_native = 246.0 / 2.7652689218262565 = 88.96060634765863
```

**This is a calibration (`fit_calibrated`), not a derivation** — exactly the same epistemic move
as Attempt 17, applied here to close a physical-unit scale instead of a branch-cost ratio.

## Circularity — read this before citing anything from this candidate

Fitting `Lambda` from `v=246 GeV` and then "predicting" `v=246 GeV` back would be entirely
circular: `Lambda` is *defined* so that `Lambda * v_native == 246.0` exactly. This file never does
that. The only thing `Lambda` is used for afterward is converting the merged order-vacuum
closure's `radial_curvature_proxy` (already tagged there, before this candidate existed, as "not a
physical Higgs pole mass") into a predicted Higgs mass, in GeV, and comparing it to the real,
independently measured value. `radial_curvature_proxy` was never touched during the `Lambda` fit —
this comparison is the actual, falsifiable test.

## The independent test — and its real, disclosed result

```text
radial_curvature_proxy (native) = 6.005340238045337
m_higgs_native = sqrt(radial_curvature_proxy) = 2.450579571865671
m_higgs_predicted_gev = Lambda * m_higgs_native = 218.00504461635578 GeV

m_higgs_physical (PDG 2024) = 125.20 GeV
relative error = 74.13%
```

**`FAILS` a 5% band around the real Higgs mass.** This is reported exactly as computed — not
softened, not reframed as a partial success, not excluded from the file. A real, disclosed
negative result: this construction's native-unit radial-curvature proxy, once put on the real
physical scale via the one fitted conversion factor, does NOT reproduce the real Higgs mass.

This does not mean `Lambda`, `v_native`, `Pi0`, or any upstream number is computed wrong — every
one of them has been independently re-verified earlier in this chain. It means the *specific
physical content* being tested here (does this architecture's radial-curvature mode correspond to
the real Higgs boson, once the scale is fixed) is not supported by this result.

## What this does and does not establish

- `Lambda_RD_to_GeV` itself: a real, disclosed, `fit_calibrated` number — usable for further
  diagnostic conversions, never for re-deriving `v=246 GeV`.
- The Higgs-mass test: a real, non-circular, `finite_diagnostic` comparison that came out
  negative. This is evidence *against* treating the radial-curvature proxy as a physical Higgs
  mass candidate under this specific scale-fixing choice — not proof the whole construction is
  wrong, but a genuine falsification signal that should not be ignored or re-fit away.
- Does NOT establish that `v=246 GeV` itself is derived (it is the external calibration input).
- Does NOT touch item 1's root-derivation question, the branch initial-conditions gap, or the
  structural-guarantee finding on `ORDERED_READY` — all remain exactly as previously disclosed.

## Files

- `rd_to_gev_fit_calibrated_bridge_v0_1.py` — the fit and the independent test;
- `test_rd_to_gev_fit_calibrated_bridge_v0_1.py` — regression, adversarial, and non-circularity
  gates, including a test that locks in today's real (failing) result so a future change cannot
  silently flip it without the test noticing.

## Run

```bash
cd domains/standard_model/item1_exploration/rd_to_gev_fit_calibrated_bridge
python3 rd_to_gev_fit_calibrated_bridge_v0_1.py
python3 test_rd_to_gev_fit_calibrated_bridge_v0_1.py
```

## Tier and boundary

- `fit_calibrated` for `Lambda_RD_to_GeV`; `finite_diagnostic` for the Higgs-mass comparison;
- candidate until independently reviewed;
- no auto-merge requested;
- reports a real negative result honestly — this is not a "some day fix the number" placeholder,
  it is the actual outcome of the test as specified;
- inherits every upstream claim_boundary unchanged.
