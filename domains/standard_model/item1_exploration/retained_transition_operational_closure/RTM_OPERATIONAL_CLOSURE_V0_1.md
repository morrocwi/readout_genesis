# RTM Operational Exchange Closure v0.1 — candidate

## Decision

This candidate closes the exchange coefficient only at the **operational calibrated** tier.

It makes the following computation admissible on a declared tape:

```text
Reader/Record observations
  -> noise-aware M estimate
  -> reader/record agreement gate
  -> signed exchange diagnostic
  -> candidate nonnegative Delta
  -> lambda only when primitive-closure semantics and dimensionless Delta are independently declared
  -> Pi0 only when independent U, D, E branch lambdas exist
```

It does **not** claim that the unrestricted root derives `M`, that absolute exchange is the unique
primitive closure cost, or that one scalar tape supplies real Standard-Model U/D/E branches.

## Estimator A — known-noise moment correction

For uniform sampling and disclosed iid observation noise,

\[
a_{\rm obs}=a_{\rm true}+u,\qquad
\operatorname{Var}(u)=\frac{6\sigma^2}{\Delta t^4}.
\]

The ordinary least-squares denominator contains derivative-noise power. The operational correction is

\[
\widehat M_{\rm MC}
=
\frac{\sum_n a_{{\rm obs},n}y_{{\rm obs},n}}
{\sum_n a_{{\rm obs},n}^2-N\,6\sigma^2/\Delta t^4}.
\]

The estimator returns `UNRESOLVED` when the corrected denominator is non-positive or remains too close
to the expected noise floor.

## Estimator B — independent-replicate IV

When two independently noisy observations of the same latent trajectory exist,

\[
\widehat M_{\rm IV}
=
\frac{a_1^\top y_2+a_2^\top y_1}
{2a_1^\top a_2}.
\]

This is preferred because independent cross-products remove additive regressor-noise power in
expectation without subtracting a large nearly equal number.

## Required gates

1. explicit noise or replicate provenance;
2. positive corrected information;
3. corrected-to-noise ratio at least 3;
4. total-to-noise ratio at least 4;
5. positive finite Reader and Record estimates;
6. Reader/Record relative gap no greater than 5%;
7. no `lambda` unless `path_semantics=primitive_closure` and `Delta` is dimensionless;
8. no `Pi0` without independent U, D, and E branch lambdas in `(0,1]`.

## Deterministic fixture

The existing Reader/Record stepper has `M_true=1`.

At `sigma=1e-5`, the raw Reader OLS value is strongly attenuated, while moment correction and
independent-replicate IV recover an operational coefficient near 1. The exact values are produced by
`operational_exchange_closure_v0_1.py`.

At `sigma=1e-4`, the single-trace Reader moment correction fails closed rather than emitting a
plausible-looking coefficient.

## What is now usable

`M_joint` may be consumed by downstream calculations as:

```text
calibrated effective Reader/Record exchange coefficient
```

provided the report status is `CALIBRATED_READY`.

The signed exchange and `Delta_candidate` may be computed for diagnostics. `lambda` and `Pi0` remain
semantically locked until primitive closure paths, dimensionless normalization, and real branch
encoding are independently supplied.

## Status

- candidate only;
- no auto-merge;
- no shared canonical files modified;
- estimator assumptions remain visible in every result.
