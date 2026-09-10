# Readout Genesis — External Application Map

This file maps **applications of the Readout/retention programme** without promoting domain-specific mathematical or numerical results into the Genesis root canon.

Rule: an external application may cite Genesis concepts, but its mathematical and empirical claims remain owned by the repository where they are proved or tested. Application evidence does not flow backward into `READOUT_GENESIS_CORE.md` automatically.

## Navier–Stokes / Energy Observability / Discrete Epsilon-Completion

Status: **external research application; not a registered Genesis domain and not a root theorem**.

### Ownership map

| Layer | Repository | Role |
|---|---|---|
| General finite-first mathematics | `morrocwi/information-discrete-math` | refinement, fail-closed certification, target-indexed tail bounds, relative-energy and exact interval/inverse primitives |
| Equation/proposal provenance | `morrocwi/toledo` | EPSC/NSOBS proposal identifiers, lineage, tier/status, later canonical review |
| Navier–Stokes specialization | `morrocwi/readout-problem-navier-stokes` | finite Fourier-Galerkin analysis, reproduction, observability, EPSC certificates, manuscripts |
| Interpretation | `morrocwi/readout_genesis` | application map only; does not own the NS mathematics |

### Current proposal map

The EPSC proposal family now runs through `PROP-EPSC-28`.

- `PROP-EPSC-01..15` — nested refinement, target-indexed omitted-tail bounds, energy/relative-energy adapters, and exact finite RK4-path certification.
- `PROP-EPSC-16` — **OPEN** scalable/tight high-cutoff continuous-time enclosure.
- `PROP-EPSC-17` — observable-to-continuum orthogonal composition.
- `PROP-EPSC-18` — retained finite-state inversion programme. A strictly positive quantitative full-`N=1` radius is now certified; practical measurement-scale and arbitrary-`N` inversion remain open.
- `PROP-EPSC-19` — **OPEN** full noise-stable measurement-to-continuum certificate.
- `PROP-EPSC-20` — quantitative reduced three-mode inverse witness.
- `PROP-EPSC-21` — derivative-free finite-window shell-transfer uncertainty certificate.
- `PROP-EPSC-22` — explicit full-`N=1` 49-dimensional symmetry-slice local inverse existence.
- `PROP-EPSC-23` — exact rational interval/preconditioned inverse criterion.
- `PROP-EPSC-24` — **OPEN** practically informative `rho_1` for the full `N=1` inverse.
- `PROP-EPSC-25` — conservative explicit full-`N=1` positive radius from uniform Cramer/Hadamard bounds.
- `PROP-EPSC-26` — row-aware Hadamard tightening.
- `PROP-EPSC-27` — exact characteristic-zero `49x49` Jacobian and rational preconditioner `A=J_0^{-1}`; reproduced radius between `10^-59` and `10^-58`.
- `PROP-EPSC-28` — componentwise exact coefficient-tensor/Hessian tightening; reproduced radius between `10^-28` and `10^-27`.

These are Toledo **proposal identifiers**, not canonical verified theorem codes.

The NS energy-observability proposal family remains separate. Its key unresolved all-resolution statement is `PROP-NSOBS-07`: earliest-order generic saturation at every finite resolution. The constructive triad-connectivity obstruction is closed, but sufficient all-`N` minor nonvanishing/algebraic independence remains open.

## Two completeness layers

The application separates two logically different questions.

**Inner completeness:** does a declared observation process determine the represented finite state, modulo unavoidable symmetry?

**Outer completeness:** how much information can remain outside the represented finite cutoff in the declared target norm/readout?

For Fourier cutoff `P_N`, energy observability addresses the first layer; EPSC tail and adapter results address the second. Neither substitutes for the other.

For the retained finite state, total and shell-energy readers are invariant under spatial translation. The structural ceilings are

\[
\operatorname{rank}D\mathcal E_R\le\min(R+1,d_N-3),
\]

\[
\operatorname{rank}D\mathcal J_R\le\min(m_N+(m_N-1)R,d_N-3).
\]

Exact modular witnesses reach the translation ceiling at the earliest structurally allowed order in the recorded cases `N=1` total energy, `N=1` shell energy, `N=2` total energy, and `N=3` shell energy. These are finite local quotient-state results, not global injectivity claims.

## Full N=1 finite inverse: current certified chain

For `N=1`, the finite real Fourier-Galerkin state dimension is 52. Fixing a transverse gauge for the three spatial-translation directions leaves a 49-dimensional slice. An explicit selected `49x49` shell-energy Taylor-jet minor is nonzero, so a local real inverse exists on that slice.

Successive fail-closed quantitative certificates then remove distinct sources of proof slack:

\[
10^{-7934}
\longrightarrow
10^{-3878}
\longrightarrow
10^{-59}
\longrightarrow
10^{-28}.
\]

More precisely:

- the uniform Cramer/Hadamard certificate gives `10^-7934 < r <= 10^-7933`;
- retaining one cofactor/Hessian majorant per selected row gives `10^-3878 < r <= 10^-3877`;
- reconstructing the actual characteristic-zero selected matrix and inverting it exactly gives `1.28 < ||J_0^{-1}||_inf < 1.29` and `10^-59 < r <= 10^-58` with the previous scalar derivative envelope;
- constructing the exact scaled `52x52x52` quadratic coefficient tensor and propagating componentwise rational derivative majorants gives `10^-28 < r <= 10^-27`, still with `q<=1/2` and with the radius certified to remain inside the declared local box.

The exact tensor reproduction records 2096 nonzero coefficients and an exact induced infinity bilinear row-sum bound of 36000.

The interpretation is important: the very small first radii were largely consequences of deliberately coarse proof envelopes. The later finite certificates remove determinant and scalar-majorant slack without weakening the local inverse criterion.

However, `10^-28` is still not a practical measurement tolerance. The open inner frontier is a branch-stable, noise-aware, entrywise/local interval certificate that yields a measurement-informative retained-state radius.

## Outer completeness and composition

For an unforced Leray-Hopf trajectory on the `2*pi` periodic three-torus, the EPSC lane supplies

\[
\|(I-P_N)u\|_{L^2(0,T;L^2_x)}
\le
\frac{\|u_0\|_2}{\sqrt{2\nu}(N+1)}.
\]

A terminal route uses a certified comparison path and the residual-based relative-energy adapter. Stored binary64 RK4 nodes can be captured exactly as dyadic rationals and converted into a continuous piecewise-linear comparison path with rigorous finite residual summaries in the declared setting.

If the finite observation side supplies

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

For invariant energy readers, `G=T^3` is spatial translation. This is the application-level composition registered as `PROP-EPSC-17`.

## Transfer interpretation

For finite Fourier-Galerkin Navier-Stokes shell energy,

\[
\dot I_s=T_s-2\nu sI_s+F_s,
\qquad
\sum_sT_s=0
\]

in the unforced closed truncation. Internal transfer therefore preserves total retained energy while redistributing it among shells. For prescribed forcing,

\[
T=\dot I+2\nu SI-F,
\]

so `(I,T)` and `(I,dI/dt)` are an affine reparameterization at first order; transfer variables do not manufacture extra local rank. Their practical value is mechanism visibility and finite-window balance measurement.

## Current fail-closed measurement-to-continuum chain

\[
\text{energy/window measurements}
\to
\rho_N\text{ on a certified retained quotient branch}
\to
\beta_N\text{ on omitted information}
\to
\sqrt{\rho_N^2+\beta_N^2}
\to
\varepsilon\text{-verdict}.
\]

At `N=1`, a mathematically positive retained-state radius is no longer open. A **measurement-ready** `rho_1` is still open because robust branch/noise containment has not been certified. Arbitrary-`N` retained inversion is also open. If either the retained-state certificate or the omitted-tail certificate required by a declared target is absent, the correct status remains `HOLD`.

## What must NOT be imported into Genesis root

The following remain application-local and must not be promoted into `READOUT_GENESIS_CORE.md`: tested Taylor-Green cutoffs; finite numerical thresholds; claims that any finite cutoff is automatically continuum-complete; claims that local observability equals global reconstruction; claims that a raw Galerkin path equals the continuum projection; claims that continuum ontology has been disproved; claims that transfer connectivity proves all-resolution observability saturation; claims of turbulent DNS adequacy from the finite tests; claims of global Navier-Stokes regularity or blow-up; or claims that the Clay Millennium problem has been solved.

The application-level lesson remains:

> completeness has at least two separable budgets: what the declared reader determines **inside** the chosen finite representation, and what a proved certificate permits to remain **outside** it.

Genesis records this interpretation and the current boundary only. The mathematics remains owned and reproduced in the domain and finite-math repositories.
