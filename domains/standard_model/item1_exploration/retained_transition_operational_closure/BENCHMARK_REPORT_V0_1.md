# RTM Operational Exchange Benchmark v0.1

## Decision

The operational closure was executed on the repository's existing scalar Reader/Record stepper,
not merely inspected from formulas. The benchmark uses the known fixture value `M_true=1`, 2000
steps, `dt=0.01`, and 500 independent replicate-noise pairs at each disclosed iid Gaussian noise
level.

At the main tested level `sigma=1e-5`, the selected independent-replicate IV estimator is
`CALIBRATED_READY` in 500/500 runs and achieves:

- mean absolute percentage error: **0.335552%**;
- median absolute percentage error: **0.275900%**;
- RMSE: **0.426199%**;
- 95th-percentile absolute error: **0.835736%**;
- worst observed absolute error: **1.504460%**.

For comparison, raw Reader OLS at the same noise level has mean absolute error **21.659056%**.
The operational correction therefore reduces the average Reader-side error by roughly a factor of
64 on this benchmark, while the joint Reader/Record agreement gate remains active.

## 500-pair-seed sweep

Errors below are computed only when the fail-closed selected report is `CALIBRATED_READY`.

| observation noise sigma | ready runs | mean M | mean abs. error | median abs. error | P95 abs. error | worst abs. error |
|---:|---:|---:|---:|---:|---:|---:|
| `2e-6` | 500/500 | 1.000012 | 0.013485% | 0.011303% | 0.033786% | 0.056399% |
| `5e-6` | 500/500 | 1.000078 | 0.083722% | 0.070832% | 0.207854% | 0.364536% |
| `1e-5` | 500/500 | 1.000337 | 0.335552% | 0.275900% | 0.835736% | 1.504460% |
| `2e-5` | 434/500 | 1.000433 | 1.037221% | 0.958386% | 2.373178% | 2.630195% |
| `5e-5` | 100/500 | 0.997695 | 1.085545% | 1.141622% | 2.260879% | 2.485807% |
| `1e-4` | 38/500 | 0.997937 | 1.073009% | 0.922872% | 2.141210% | 2.371280% |

The decreasing ready fraction at high noise is intentional. The system abstains when independent
Reader/Record estimates disagree by more than 5%, rather than reporting an attractive but unstable
number.

## Exact disclosed run

For the PR fixture seed pair `20260725/20260726` at `sigma=1e-5`:

- raw Reader OLS: `0.7947136899` — error `20.528631%`;
- moment-corrected Reader: `1.0194259427` — error `1.942594%`;
- replicate-IV Reader: `1.0009133055` — error `0.091331%`;
- replicate-IV Record: `0.9999456490` — error `0.005435%`;
- selected joint IV: `1.0004294772` — error **`0.042948%`**.

## Actual downstream calculation

Using the clean underlying trajectory, `cost_unit_rd=1`, and the selected joint value above:

| output | true M=1 calculation | selected M calculation | relative error |
|---|---:|---:|---:|
| signed exchange total | -31.8594388282 | -31.8731217316 | 0.042948% |
| Delta candidate | 34.0403957258 | 34.0550153005 | 0.042948% |
| exp(-Delta candidate) | 1.6460536059e-15 | 1.6221640553e-15 | 1.451323% |
| orientation cancellation fraction | 0.0640696693 | 0.0640696693 | effectively zero |

The exchange and Delta errors equal the M error because they are linear in M. The exponential
lambda transformation amplifies a small Delta error when Delta is large; this is a property of the
exponential, not a failure of the M estimator.

## Reproduction

Run:

```bash
python3 domains/standard_model/item1_exploration/retained_transition_operational_closure/benchmark_operational_exchange_v0_1.py
```

## Status

This is an actual numerical benchmark on the project's existing Reader/Record dynamics. It supports
using `M_joint` for operational calculations whenever status is `CALIBRATED_READY`. It is not a
claim of external laboratory validation or an unrestricted-root derivation.
