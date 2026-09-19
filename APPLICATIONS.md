# Readout Genesis — External Application Map

This file maps **applications of the Readout/retention programme** without promoting domain-specific mathematics into the Genesis root canon.

Rule: application evidence remains owned by the repository where it is proved or tested.  Nothing below is automatically a theorem of `READOUT_GENESIS_CORE.md`.

## Navier–Stokes / Energy Observability / Discrete Epsilon-Completion

Status: **external research application**.

| Layer | Repository | Role |
|---|---|---|
| General finite-first mathematics | `morrocwi/information-discrete-math` | finite records, fail-closed gates, exact finite linear/interval tools |
| Provenance / theorem map | `morrocwi/toledo` | EPSC/NSOBS proposal identifiers and claim boundaries |
| Navier–Stokes specialization | `morrocwi/readout-problem-navier-stokes` | finite Fourier-Galerkin checkers, observability, EPSC certificates |
| Interpretation | `morrocwi/readout_genesis` | application map only |

All Toledo `weld/P.??.v1` identifiers remain proposal placeholders until canonical audit.

## Genesis interpretation: difference, transfer, restoration

The step-by-step Genesis vocabulary describes energy as transmitted difference and force as recovery from disequilibrium.  In the Navier–Stokes application this is an interpretive bridge only, not an assertion that generic informational quantities equal SI energy.

For the declared finite Fourier-Galerkin system,

\[
\dot I_s=T_s-2\nu sI_s+F_s.
\]

The nonlinear triads redistribute retained kinetic energy among shells, while viscosity contributes dissipation.  For prescribed forcing,

\[
T=\dot I+2\nu SI-F.
\]

Thus transfer is a mechanism/measurement coordinate; it does not manufacture additional first-order observability rank.  The finite-window identity

\[
\int_{t_0}^{t_1}T_sdt
=I_s(t_1)-I_s(t_0)+2\nu s\int_{t_0}^{t_1}I_sdt-\int_{t_0}^{t_1}F_sdt
\]

remains useful because it removes numerical differentiation from that substep.

## Current finite evidence ladder

For shell-energy observability,

\[
\operatorname{rank}D\mathcal J_R
\le\min(m_N+(m_N-1)R,d_N-3).
\]

Exact finite reproduction reaches the continuous translation ceiling at the first structurally admissible order for three consecutive cutoffs:

\[
\boxed{(N,R_I^{min},d_N-3)=(1,23,49),(2,30,245),(3,39,681).}
\]

This is finite evidence, not an arbitrary-finite-`N` induction theorem. `PROP-NSOBS-07` remains OPEN.

At `N=1`, an explicit translation slice and exact entrywise inverse enclosure give

\[
\|x-x_*\|_\infty\le10^{-17},
\qquad q_1\le0.08058674502845<1/2.
\]

At `N=2`, a deliberately conservative positive quantitative witness gives

\[
10^{-79490}<r_2\le10^{-79489},
\qquad q_2\le1/2.
\]

The N=2 scale is mathematical, not sensor-ready.

## Measurement route: from Taylor chart to actual finite-time samples

`PROP-EPSC-35` gives the branch-conditioned N=1 scaled-chart error law

\[
\|x-z\|_\infty<2.58(\sigma+\tau)
\]

once both states are already in the certified branch.

`PROP-EPSC-37` then shows that high-order numerical differentiation is not structurally necessary: 49 actual shell-energy values at finitely many times form a local N=1 sample chart for sufficiently small nonzero spacing.  `PROP-EPSC-38` quantifies why reconstructing the high-order Taylor jet from noisy closely spaced samples is badly conditioned.

The preferred route is therefore direct:

\[
\boxed{
\text{raw finite samples}
\to\mathcal S_h
\to\text{direct sample-map gate}
\to\rho_N.
}
\]

## Finite-first correction: the gate is not real-root existence

The fixed-N=1 direct construction now separates two tiers.

`PROP-EPSC-39` is the native finite inequality gate.  With a square preconditioner `A`, a declared radius `r`, data/model budget `delta`, and a separately certified defect bound `q`,

\[
q<1,
\qquad
\|A\|_\infty\delta+qr\le r
\]

imply the exact finite budgets

\[
\boxed{
\delta\le\frac{(1-q)r}{\|A\|_\infty},
\qquad
\rho_{cond}=\frac{\|A\|_\infty}{1-q}\delta\le r.
}
\]

This does **not** silently create an exact real root or an attained infinite contraction limit.

`PROP-EPSC-40` stores the ordinary Banach fixed-point implication separately as an **Open real-analysis adapter**.  It becomes available only if completeness and the relevant real existence assumptions are explicitly granted.

This separation follows the Genesis/IDM discipline:

\[
\boxed{
\text{finite retained certificate}
\neq
\text{silent completed-infinity or real-completeness premise}.
}
\]

## New global symmetry obstruction

The earlier observability calculations removed the three continuous translation directions, but discrete global aliases must also be respected.

`PROP-NSOBS-14` gives an explicit N=1 witness: one-mode states supported at

\[
(1,0,0)
\quad\text{and}\quad
(0,1,0)
\]

are related by an axis permutation but **not** by spatial translation, because translations change Fourier phases and do not change wavevector support.  Nevertheless the two states have the same shell energy, zero quadratic self-interaction, the same viscous rate, and hence the same shell-energy derivative record at every arbitrary finite order in the one-mode construction.

Therefore `PROP-EPSC-41` records

\[
\boxed{
\text{shell-energy-only data}
\not\Longrightarrow
\text{globally unique state modulo translations alone}.
}
\]

This does not contradict local rank saturation: a discrete symmetry need not lower local differential rank.

## Corrected EPSC-36 target

The measurement problem must no longer demand impossible global orientation recovery from a reader that discards that orientation.

`PROP-EPSC-42` therefore reframes the target as either

\[
\boxed{
\text{raw shell samples}\to[x]_G\pm\rho_N
}
\]

for a declared symmetry group `G`, or

\[
\boxed{
\text{raw shell samples}+\text{orientation-breaking readout/prior}\to x\pm\rho_N.
}
\]

This is the Genesis-relevant conceptual point: **the answer must preserve the distinctions the readout can actually support.**  If the reader is invariant under a transformation, demanding that it recover which member of that orbit was “really” present adds information not contained in the readout.

The repaired target remains OPEN until the complete declared symmetry group is accounted for or a sufficient augmented reader/prior is certified, and until practical sample spacing/noise tolerances exist.

## Optional outer completion

Only after an inner retained-state/orbit radius is valid for the declared target may a separately proved outer certificate `beta_N` be attached.  If the retained/tail split is orthogonal and the declared symmetry preserves the cutoff,

\[
\boxed{
\inf_{g\in G}\|u(T)-g\widehat x_N\|_2
\le\sqrt{\rho_N^2+\beta_N^2}.
}
\]

This is the application meaning of `PROP-EPSC-17`.  The continuum adapter is downstream, not a foundational premise of the finite proof.

## Current proposal landmarks

- `PROP-EPSC-16` — OPEN scalable/tight outer certificate.
- `PROP-EPSC-17` — conditional inner/outer orthogonal composition.
- `PROP-EPSC-18` — retained-state inversion programme; fixed N=1/N=2 progress, arbitrary finite N still open.
- `PROP-EPSC-19` — OPEN full noisy measurement-to-continuum chain.
- `PROP-EPSC-21` — derivative-free finite-window transfer identity.
- `PROP-EPSC-24` — OPEN practical N=1 measurement radius.
- `PROP-EPSC-30/31` — structural observability -> square chart -> quantitative local error bridge.
- `PROP-EPSC-32` — OPEN arbitrary-finite-resolution constructive certificate schema.
- `PROP-EPSC-35` — fixed-N=1 branch-conditioned scaled-chart noise law.
- `PROP-EPSC-36` — raw finite-window measurement interface, now refined by symmetry accounting.
- `PROP-EPSC-37` — derivative-free finite-time N=1 sample-chart existence.
- `PROP-EPSC-38` — exact sample-to-Taylor interpolation conditioning law.
- `PROP-EPSC-39` — finite direct-sample q/data-budget gate.
- `PROP-EPSC-40` — separate Open real-analysis/Banach adapter.
- `PROP-EPSC-41` — translation-only global shell branch-capture obstruction.
- `PROP-EPSC-42` — OPEN symmetry-aware/orientation-augmented repair target.
- `PROP-NSOBS-14` — explicit non-translation cubic shell-energy alias at N=1.

## What must not be imported into Genesis root

Do not promote any of the following into `READOUT_GENESIS_CORE.md`: a claim that local observability equals global injectivity; a claim that shell energy uniquely fixes orientation; a claim that finite q/data-budget inequalities establish real completeness or an attained Banach limit; a claim that `h=10^-200` is practical; a claim that three finite cutoffs prove arbitrary `N`; a claim that a finite Galerkin path automatically equals the continuum projection; or any claim of Navier–Stokes global regularity, blow-up, DNS adequacy, or a Clay solution.

Genesis records the interpretation and boundary.  The mathematics remains owned by IDM, Toledo and the Navier–Stokes repository.
