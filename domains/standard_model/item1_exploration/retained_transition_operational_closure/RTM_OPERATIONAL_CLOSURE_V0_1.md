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

## Scope boundary (required correction, independent review 2026-07-25)

This candidate's directory/title echo item 1's own open branch-closure quantity (also called `M_n`,
also feeding a `Pi0`/`Delta_j` chain) named in `HANDOFF_NEXT_SESSION.md` as POSITED not derived
after 8 failed root-native attempts. **They are not the same closure.** This PR calibrates only the
toy scalar Reader/Record apparatus's own `M` against a synthetic tape with a KNOWN injected
`M_true=1` -- it does not touch, and is not evidence toward, item 1's still-open root-derivation
question. `ITEM1_EXPLORATION_LOG.md` already names this exact risk as Cross-Role Readout
Contamination (CRRC): reusing a readout across two different questions without an established
admissibility bridge between them. No such bridge is built or claimed here.

Estimator B (replicate-IV) additionally requires two genuinely independent noisy re-measurements
of the *same* latent trajectory (assumption disclosed in code, `operational_exchange_estimator_v0_1.py`).
This is a real, nontrivial data requirement: a single real/external dataset (e.g. one QuTiP run,
one lab record) will typically NOT satisfy it without a deliberately designed replicate-measurement
protocol. This sits on top of, and does not relax, closure criterion 3 (real external adapter) from
the prior bias-diagnosis final synthesis -- still open.

## Status

- candidate only;
- no auto-merge;
- no shared canonical files modified;
- estimator assumptions remain visible in every result.
