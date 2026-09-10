# Readout Genesis — External Application Map

This file maps **applications of the Readout/retention programme** without promoting domain-specific mathematical or numerical results into the Genesis root canon.

Rule: an external application may cite Genesis concepts, but its mathematical and empirical claims remain owned by the repository where they are proved or tested. Application evidence does not flow backward into `READOUT_GENESIS_CORE.md` automatically.

## Navier–Stokes / Energy Observability / Discrete Epsilon-Completion

Status: **external research application; not a registered Genesis root theorem**.

### Ownership map

| Layer | Repository | Role |
|---|---|---|
| General finite-first mathematics | `morrocwi/information-discrete-math` | finite refinement, fail-closed certification, exact interval/inverse primitives |
| Equation/proposal provenance | `morrocwi/toledo` | EPSC/NSOBS proposal identifiers, lineage, tier/status, later canonical review |
| Navier–Stokes specialization | `morrocwi/readout-problem-navier-stokes` | finite Fourier-Galerkin analysis, reproduction, observability, EPSC certificates, manuscripts |
| Interpretation | `morrocwi/readout_genesis` | application map only; does not own the NS mathematics |

### Current proposal map

The Toledo EPSC lineage now runs through `PROP-EPSC-36`; the newer bridge proposals are proposal/provenance records with placeholder `weld/P.??.v1` codes, not canonical verified theorem codes.

- `PROP-EPSC-16` — **OPEN** scalable/tight high-cutoff outer comparison-path certification.
- `PROP-EPSC-17` — inner/outer orthogonal composition once `rho_N` and `beta_N` are independently certified.
- `PROP-EPSC-18` — retained finite-state inversion programme; fixed `N=1` and conservative fixed `N=2` quantitative branches now exist, but arbitrary-finite-`N` and practical measurement readiness remain open.
- `PROP-EPSC-19` — **OPEN** full noise-stable measurement-to-continuum certificate.
- `PROP-EPSC-20` — reduced three-mode quantitative inverse witness.
- `PROP-EPSC-21` — derivative-free finite-window shell-transfer uncertainty certificate.
- `PROP-EPSC-22..29` — explicit full-`N=1` symmetry slice and successive quantitative tightening through an exact centered entrywise `10^-17` branch box.
- `PROP-EPSC-30` — structural bridge from saturated quotient observability to an explicit square nonsingular finite chart.
- `PROP-EPSC-31` — certified branch plus `q_N<1` converts chart uncertainty and forward residual into `rho_N`.
- `PROP-EPSC-32` — **OPEN** arbitrary-finite-resolution certificate schema `N -> C_N=(S_N,H_N,A_N,B_N,q_N)`.
- `PROP-EPSC-33` — fixed `N=1` bridge instance: `||x-x_*||_inf<=10^-17`, reproduced `q_1<=0.08058674502845<1/2`.
- `PROP-EPSC-34` — fixed `N=2` positive bridge instance: `10^-79490<r_2<=10^-79489`, `q_2<=1/2`; mathematically positive but deliberately very conservative.
- `PROP-EPSC-35` — fixed `N=1`, branch-conditioned **scaled-chart** noise propagation.
- `PROP-EPSC-36` — **OPEN** raw finite-window/sample -> selected chart uncertainty plus branch capture.

The NS energy-observability lineage remains distinct. `PROP-NSOBS-12` records exact `N=2` shell-energy earliest-order saturation at `R=30`; `PROP-NSOBS-13` records the three consecutive fixed-finite shell witnesses `N=1,2,3`. `PROP-NSOBS-07` remains OPEN: triad connectivity and three finite witnesses do not prove arbitrary-finite-`N` observable-minor independence.

## Genesis interpretation: difference, transfer, restoration

The older step-by-step Genesis vocabulary describes energy as transmitted difference and force as recovery from disequilibrium. In the Navier–Stokes application this is used only as an **interpretive bridge**, not as an identity between generic informational quantities and SI energy.

For the declared finite Fourier-Galerkin system, shell energy obeys

\[
\dot I_s=T_s-2\nu sI_s+F_s.
\]

The nonlinear triads redistribute retained kinetic energy among shells (`T_s`), while viscosity contributes dissipation. In the unforced closed finite system,

\[
\sum_s T_s=0.
\]

For prescribed forcing,

\[
T=\dot I+2\nu SI-F,
\]

so `(I,T)` is an affine reparameterization of `(I,dI/dt)` at first order. Transfer therefore exposes mechanism and supports finite-window balances, but does not manufacture extra local observability rank.

This preserves the Genesis distinction:

\[
\boxed{
\text{difference/retained state}
\to
\text{transfer + restoration/dissipation response}
\to
\text{observable finite dynamics}
}
\]

without claiming that every Genesis information quantity is physical energy.

## Four layers of the current NS application

The programme now separates four logically different questions.

**1. Structural inner observability.** Does a finite observation process distinguish the represented finite state modulo unavoidable symmetry?

**2. Quantitative inner certification.** On an explicit symmetry-fixed branch, can observation uncertainty be converted into a rigorous retained-state radius `rho_N`?

**3. Measurement interface.** Can raw finite samples/windows be converted into uncertainty for the selected inverse chart and can the correct local branch be certified?

**4. Outer completion.** If a continuum target is requested, how much can remain outside the finite retained cutoff, quantified separately by `beta_N`?

The finite-native chain is therefore

\[
\boxed{
\text{finite observations}
\to
\text{finite observability}
\to
\text{finite local chart}
\to
q_N<1
\to
\rho_N.
}
\]

The measurement-ready version inserts the still-partly-open upstream interface:

\[
\boxed{
\text{raw finite samples/windows}
\to
(H_N\text{ uncertainty},\text{branch certificate})
\to
\rho_N.
}
\]

Only after this, and only when a continuum interpretation is actually requested, may a separately proved outer adapter be attached:

\[
\boxed{
(\rho_N,\beta_N)
\to
\sqrt{\rho_N^2+\beta_N^2}
\to
\varepsilon\text{-verdict}.
}
\]

If a required link is absent, the application-level verdict is `HOLD`.

## Structural finite evidence

For shell-energy observability,

\[
\operatorname{rank}D\mathcal J_R
\le
\min(m_N+(m_N-1)R,d_N-3).
\]

Exact reproduction reaches the translation ceiling at the first structurally admissible order for three consecutive finite cutoffs:

\[
\boxed{(N,R_I^{min},d_N-3)=(1,23,49),(2,30,245),(3,39,681).}
\]

At `N=2`, the focused exact checker gives

\[
\operatorname{rank}D\mathcal J_{2,29}=241<245,
\qquad
\operatorname{rank}D\mathcal J_{2,30}=245=d_2-3.
\]

This fills the finite middle case but is not an induction theorem.

## Quantitative fixed-resolution bridge

For `N=1`, an explicit translation gauge leaves a 49-dimensional slice. The selected shell-energy Taylor chart has an exact nonsingular characteristic-zero Jacobian. Successive fail-closed bounds tighten the state-space branch from the first extremely conservative positive radius to the current exact centered entrywise box

\[
\boxed{\|x-x_*\|_\infty\le10^{-17}},
\qquad
\boxed{q_1\le0.08058674502845<1/2}.
\]

For `N=2`, the nine-shell reader at `R=30` supports an explicit 245-dimensional translation slice and 245-observation square chart. A conservative finite Cramer--Hadamard/Hessian construction gives

\[
\boxed{10^{-79490}<r_2\le10^{-79489}},
\qquad
\boxed{q_2\le1/2<1}.
\]

The tiny `N=2` radius is an existence-scale mathematical certificate, not a practical measurement tolerance. Its significance is that the structural -> square-chart -> positive-quantitative bridge has crossed **two distinct finite resolutions**.

## New partial EPSC-19 closure at N=1

The exact `N=1` center inverse also satisfies

\[
\|A_1\|_\infty<1.29.
\]

Using the already-certified conservative branch defect `q_1<=1/2`, if the true state `x` and candidate `z` are both certified to lie in the same `10^-17` local branch and the selected scaled chart satisfies

\[
\|y-H_1(x)\|_\infty\le\sigma,
\qquad
\|H_1(z)-y\|_\infty\le\tau,
\]

then

\[
\boxed{
\|x-z\|_\infty<\frac{129}{50}(\sigma+\tau)=2.58(\sigma+\tau).
}
\]

This is the application meaning of `PROP-EPSC-35`: **once the correct branch and chart uncertainty are supplied, noise-to-state propagation is no longer open at fixed N=1.**

What remains open is upstream and physically important: raw sensor/time-window data are not yet the selected high-order scaled chart. `PROP-EPSC-36` must provide a derivative-free finite sample/window map, a validated flow/Taylor remainder, and branch capture. Therefore `PROP-EPSC-19` and practical `PROP-EPSC-24` remain OPEN.

The finite-window transfer identity from `PROP-EPSC-21`,

\[
\int_{t_0}^{t_1}T_sdt
=
I_s(t_1)-I_s(t_0)
+2\nu s\int_{t_0}^{t_1}I_sdt
-\int_{t_0}^{t_1}F_sdt,
\]

is one useful derivative-free input to that open measurement-interface problem; it is not itself the selected inverse chart.

## Finite-first meaning of “all N”

The general target remains constructive:

\[
\boxed{
N<\infty
\mapsto
\mathcal C_N=(S_N,H_N,A_N,B_N,q_N),
\qquad q_N<1.
}
\]

“All N” means an algorithm/schema that accepts any particular finite cutoff and emits a finite proof object. It does **not** mean that the application begins from a completed infinite Fourier state. Continuum spaces may enter later as external analytic adapters when a continuum target is explicitly requested.

Current ladder:

\[
N=1:\;\text{structural + tight local quantitative + branch-conditioned chart-noise},
\]

\[
N=2:\;\text{structural + conservative positive quantitative},
\]

\[
N=3:\;\text{structural saturation only}.
\]

The next high-value tasks are therefore raw-window/sample -> chart plus branch certification at `N=1`, improving `N=2` conditioning, building an explicit quantitative `N=3` branch, and separately proving or refuting the arbitrary-finite-`N` structural minor-independence statement.

## Outer completeness and composition

Only after an inner `rho_N` is available do we optionally attach an external continuum adapter. If the finite observation side supplies

\[
\inf_{g\in G}\|P_Nu(T)-g\widehat x_N\|_2\le\rho_N
\]

and the omitted-tail side independently supplies

\[
\|(I-P_N)u(T)\|_2\le\beta_N,
\]

then orthogonality gives

\[
\boxed{
\inf_{g\in G}\|u(T)-g\widehat x_N\|_2
\le
\sqrt{\rho_N^2+\beta_N^2}.
}
\]

For invariant energy readers, `G=T^3` is spatial translation. This is `PROP-EPSC-17`. The continuum adapter is downstream; it is not an ontological premise of the finite proof.

## What must NOT be imported into Genesis root

The following remain application-local and must not be promoted into `READOUT_GENESIS_CORE.md`: finite Taylor-Green thresholds; claims that any finite cutoff is automatically continuum-complete; claims that local observability equals global reconstruction; claims that a raw Galerkin path equals the continuum projection; claims that continuum ontology has been disproved; claims that transfer connectivity or three fixed cutoffs prove all-resolution saturation; claims that the `10^-17` or `10^-79490` scales are practical physical sensor tolerances; claims of turbulent DNS adequacy from finite tests; claims of global Navier--Stokes regularity or blow-up; or claims that the Clay Millennium problem has been solved.

Genesis records the interpretation and the boundary. The mathematics remains owned and reproduced in the domain and finite-math repositories.
