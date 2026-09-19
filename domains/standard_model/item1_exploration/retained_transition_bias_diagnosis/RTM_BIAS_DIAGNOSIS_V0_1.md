# RTM OLS Bias Diagnosis v0.1

> **Tier:** `finite_diagnostic / candidate`  
> **Purpose:** diagnose the mechanism behind the OLS bias observed in PR #68 before selecting an EIV or state-space estimator.  
> **Integration status:** candidate only; no shared registry, README, canonical test runner, or prior candidate is modified.

## Question

The scalar fit uses

\[
\widehat M=\frac{\sum_n a_n y_n}{\sum_n a_n^2},
\qquad a_n=\delta_t^2 X_n.
\]

Observation noise is added to the recorded field before both `a_n` and `y_n` are constructed. The diagnosis separates:

1. **EIV-only:** noisy acceleration, clean target;
2. **target-only:** clean acceleration, fully noisy target;
3. **linearized target propagation:** first-order Taylor propagation through the Reader/Record terms;
4. **full nonlinear observation fit**;
5. **analytic attenuation prediction** from the known second-difference noise variance.

No corrected estimator is proposed in this candidate.

## Analytic mechanism

For iid observation noise \(\epsilon_n\sim(0,\sigma^2)\),

\[
 u_n=\delta_t^2\epsilon_n
 =\frac{\epsilon_{n+1}-2\epsilon_n+\epsilon_{n-1}}{\Delta t^2},
\]

so

\[
\operatorname{Var}(u_n)=\frac{6\sigma^2}{\Delta t^4}.
\]

Ignoring the much smaller target-noise covariance for a moment, the expected scalar attenuation is

\[
\mathbb E[\widehat M]
\approx
M\frac{S_a}{S_a+N\,6\sigma^2/\Delta t^4},
\qquad
S_a=\sum_n a_{\rm true,n}^2.
\]

The same noise power acts on Reader and Record. Their bias differs because the disclosed fixture has very different acceleration energies:

- Reader: \(S_{a,\Phi}\approx432.07\);
- Record: \(S_{a,\Psi}\approx182830.03\);
- ratio: about \(423\times\).

The anti-damped Record trajectory therefore carries far more acceleration signal than the settled Reader trajectory. The asymmetry does not require a different estimator-bias mechanism.

## Deterministic reproduction

Using the existing stepper, its long disclosed trajectory (`N=2000`, `Phi=(1,1.01)`, `Psi=(-1,-1.01)`), iid noise, and seed `20260725`:

| sigma | Reader full | Reader EIV-only | Reader target-only | Record full | Record EIV-only | Record target-only |
|---:|---:|---:|---:|---:|---:|---:|
| `2e-6` | `0.98972377` | `0.98972371` | `0.99999981` | `0.99996924` | `0.99996964` | `0.99999960` |
| `1e-5` | `0.79471369` | `0.79470963` | `0.99999907` | `0.99932452` | `0.99932650` | `0.99999801` |
| `1e-4` | `0.03742446` | `0.03740232` | `0.99999077` | `0.93853696` | `0.93855449` | `0.99998021` |

The user's independently reported sweep is reproduced. At `sigma=1e-4`, the Reader should still be treated as **underdetermined** by the existing noise-floor gate; the raw number is displayed only to diagnose the attenuation.

## Finding

For this fixture and tested noise range:

- the full noisy estimate is almost identical to the EIV-only estimate;
- target-only fits stay approximately at the true `M=1`;
- full nonlinear and first-order-linearized fits are nearly identical;
- the analytic attenuation formula tracks Monte Carlo means.

Therefore the dominant mechanism is:

\[
\boxed{\text{second-difference EIV attenuation + Reader/Record acceleration-SNR asymmetry}}
\]

The nonlinear Reader/Record target terms are not absent, but they are a secondary contribution here. This does **not** establish that they remain secondary for other potentials, dimensions, trajectories, correlated noise, or laboratory data.

## Consequence for the next estimator

Do not patch OLS merely because the nonlinear terms look different. A next candidate must first handle the latent-state/derivative-noise problem. Eligible comparison tracks include:

- state-space latent trajectory estimation;
- errors-in-variables or total least squares with disclosed noise covariance;
- smoothing followed by derivative estimation, with held-out simulation calibration;
- moment correction only as a diagnostic, because it becomes unstable near the identifiability threshold.

The estimator must be compared on multiple trajectories and must fail closed when the corrected denominator approaches its noise floor.

## Run

```bash
python3 domains/standard_model/item1_exploration/retained_transition_bias_diagnosis/rtm_bias_diagnosis_v0_1.py --pretty
python3 domains/standard_model/item1_exploration/retained_transition_bias_diagnosis/test_rtm_bias_diagnosis_v0_1.py
```

## Claim boundary

This candidate diagnoses one disclosed finite fixture. It does not derive `M`, validate a physical primitive-transition cost, select a final estimator, or close any Standard-Model item.
