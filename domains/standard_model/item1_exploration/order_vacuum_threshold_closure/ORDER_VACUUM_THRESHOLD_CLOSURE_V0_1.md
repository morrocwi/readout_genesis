# Order-Vacuum Threshold Closure v0.1

## Decision

Within the declared scalar finite architecture, the order-vacuum threshold is now executable from the
same chain that produced the calibrated exchange coefficient and the U/D/E primitive branch weights.
No independent `alpha_order` or `beta_order` is introduced.

The inherited scalar mother potential is

\[
V(x)=\frac{a}{2}x^2+\frac{b}{4}x^4.
\]

Under the declared order-amplitude coordinate

\[
r=x^2,
\]

this is exactly

\[
V_{\rm bare}(r)=\alpha_{\rm ord}r+\beta_{\rm ord}r^2,
\qquad
\alpha_{\rm ord}=\frac a2,
\qquad
\beta_{\rm ord}=\frac b4.
\]

For the existing Reader/Record stepper, `a=-1` and `b=1`, hence

\[
\alpha_{\rm ord}=-0.5,
\qquad
\beta_{\rm ord}=0.25.
\]

These are inherited coefficients, not two new Standard-Model-sector fitting dials.

## Full calculated chain

The stacked calculation is

```text
noise-aware Reader/Record tape
  -> M_joint
  -> native C_RD=1
  -> independent primitive U/D/E tapes
  -> Delta_U, Delta_D, Delta_E
  -> lambda_U, lambda_D, lambda_E
  -> Pi0
  -> inherit alpha_order=a/2 and beta_order=b/4
  -> test Pi0 > alpha_order
  -> solve unique convex r_star
```

The branch candidate produces

\[
\lambda_U=0.989967778698984,
\quad
\lambda_D=0.933482990705046,
\quad
\lambda_E=0.558101245145896,
\]

so

\[
\Pi_0=3\lambda_U+3\lambda_D+\lambda_E
=6.328453553357985.
\]

The order margin is therefore

\[
\Pi_0-\alpha_{\rm ord}
=6.828453553357985>0.
\]

The v1.13 criterion is satisfied decisively:

\[
\boxed{\Pi_0>\alpha_{\rm ord}}.
\]

The effective potential

\[
V_{\rm eff}(r)
=\alpha_{\rm ord}r+\beta_{\rm ord}r^2
-3\log(1+\lambda_Ur)
-3\log(1+\lambda_Dr)
-\log(1+\lambda_Er)
\]

is strictly convex because `beta_order>0`. Its unique minimum is

\[
\boxed{r_*=3.823356105009073}.
\]

The local curvature outputs are

\[
V_{\rm eff}''(r_*)=0.785349320480192,
\]

and

\[
2r_*V_{\rm eff}''(r_*)=6.005340238045337.
\]

The latter remains a local architecture curvature proxy, not a physical Higgs pole mass.

## Error audit

Using the known fixture `M_true=1` as the comparison baseline:

| output | estimated | truth-fixture | relative error |
|---|---:|---:|---:|
| `Pi0` | 6.328453553357985 | 6.328688910509923 | 0.003718892732% |
| `r_star` | 3.823356105009073 | 3.823379983152252 | 0.000624529691% |
| radial-curvature proxy | 6.005340238045337 | 6.005409549512299 | 0.001154150544% |

The phase verdict is stable because the order margin is about `6.82845`, vastly larger than the
numerical uncertainty induced by the calibrated `M` error.

**REQUIRED CORRECTION (independent scientific-methodology review, 2026-07-25):** this stability
is not itself evidence that the branch-tape data is predictive. Because `lambda_j` is constrained
to `(0,1]`, `Pi0` is unconditionally in `(0,7]` for ANY legitimate branch-tape input. Since
`alpha_order=a/2=-0.5` on this stepper sits below `Pi0`'s unconditional lower bound of `0`,
`Pi0>alpha_order` holds no matter what the U/D/E branches compute — `ORDERED_READY` on this
stepper is guaranteed by the mother potential's sign alone, not by anything the branch
construction discovered. See `falsifiability_note` in the executable's own output and
`test_alpha_order_is_below_pi0_unconditional_lower_bound`, which demonstrates `ORDERED_READY`
still holds even when all three lambdas are pushed to `1e-6` (near the extreme low end of their
legal domain). This does not mean the numbers above are wrong — `Pi0`, `r_star`, and the branch
lambdas are still real, correctly computed outputs — only that the specific ORDERED-vs-UNORDERED
*decision* on this fixture carries no data-dependent information.

## Parameter reduction

This stage removes two additional independent SM-sector dials:

```text
alpha_order, beta_order -> inherited from mother potential a,b
```

Cumulative declared operational subchain:

```text
M, C_RD, lambda_U, lambda_D, lambda_E, alpha_order, beta_order
7 candidate/fitted dials -> 0 new/fitted SM-subchain dials
```

This does **not** erase the global mother-potential coefficients `a,b`. It proves only that the order
sector does not need separate duplicate coefficients after the bridge `r=x^2` is declared.

## Fail-closed conditions

The executable rejects nonfinite mother-potential coefficients, `beta_order<=0`, invalid branch
weights, a mismatch between disclosed `Pi0` and the branch lambdas, failure to bracket a convex
minimum, or violation of the exact v1.13 bounds. A valid case with `Pi0<=alpha_order` returns
`UNORDERED_READY` and `r_star=0` rather than manufacturing order.

## Claim boundary

- exact algebraic bridge inside the declared scalar architecture;
- calibrated finite-diagnostic branch pressure;
- ordered vacuum established for this executable fixture;
- **REQUIRED (2026-07-25 review): on this stepper, `alpha_order=-0.5` is below `Pi0`'s
  unconditional lower bound (0), so `ORDERED_READY` is structurally guaranteed regardless of the
  branch-tape data — do not cite this fixture's `ORDERED_READY` status as evidence the
  primitive-branch construction is predictive; see the Error audit section above and
  `falsifiability_note` in the executable output;**
- not an unrestricted-root proof that the physical universe must use this scalar bridge;
- not a prediction of the observed Higgs mass, gauge couplings, or vacuum scale in SI units.
