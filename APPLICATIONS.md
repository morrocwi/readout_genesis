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

The EPSC proposal family now runs through `PROP-EPSC-33`.

- `PROP-EPSC-01..15` — nested refinement, target-indexed omitted-tail bounds, energy/relative-energy adapters, and exact finite RK4-path certification.
- `PROP-EPSC-16` — **OPEN** scalable/tight high-cutoff continuous-time outer enclosure.
- `PROP-EPSC-17` — observable-to-continuum orthogonal composition once both an inner `rho_N` and outer `beta_N` are independently certified.
- `PROP-EPSC-18` — retained finite-state inversion programme. Full `N=1` local inversion is quantitatively certified; measurement-ready and arbitrary-finite-`N` inversion remain open.
- `PROP-EPSC-19` — **OPEN** full noise-stable measurement-to-continuum certificate.
- `PROP-EPSC-20` — quantitative reduced three-mode inverse witness.
- `PROP-EPSC-21` — derivative-free finite-window shell-transfer uncertainty certificate.
- `PROP-EPSC-22` — explicit full-`N=1` 49-dimensional symmetry-slice local inverse existence.
- `PROP-EPSC-23` — exact rational interval/preconditioned inverse criterion.
- `PROP-EPSC-24` — **OPEN** practically informative `rho_1` for the full `N=1` inverse.
- `PROP-EPSC-25..29` — successive finite `N=1` quantitative tightening and observation-chart selection.
- `PROP-EPSC-30` — fixed-finite-`N` bridge from observability saturation modulo translation to an explicit square nonsingular local observation chart.
- `PROP-EPSC-31` — quantitative inner-certificate bridge: a certified branch, preconditioner and `q_N<1` convert measurement/forward residual uncertainty into `rho_N`.
- `PROP-EPSC-32` — **OPEN** arbitrary-finite-resolution constructive programme `N -> C_N=(S_N,H_N,A_N,B_N,q_N)`; this means a finite certificate schema for each finite input `N`, not an assumed completed `N=infinity` object.
- `PROP-EPSC-33` — fixed finite `N=1` exact centered entrywise local inverse box `||x-x_*||_inf <= 10^-17` with reproduced `q=0.08058674502845<1/2`.

These are Toledo **proposal identifiers**, not canonical verified theorem codes.

The NS energy-observability family is kept separate. `PROP-NSOBS-12` records exact `N=2` shell-energy earliest-order saturation at `R=30`, and `PROP-NSOBS-13` records the conjunction of exact shell saturation at the three consecutive finite cutoffs `N=1,2,3`. The key unresolved all-resolution statement remains `PROP-NSOBS-07`: earliest-order generic saturation at arbitrary finite resolution. Three finite cases and all-`N` triad connectivity strengthen the evidence but do not prove the arbitrary-finite-`N` minor-independence statement.

## Two completeness layers and the explicit bridge

The application separates three logically different questions.

**Inner structural observability:** does a declared finite observation process distinguish the represented finite state, modulo unavoidable symmetry?

**Inner quantitative certification:** once structural observability is available, can observation uncertainty be converted into a rigorous retained-state radius `rho_N` on a declared symmetry-fixed branch?

**Outer completeness:** how much information can remain outside the represented finite cutoff in the declared target norm/readout?

For a fixed finite Fourier cutoff, energy observability addresses the first question. EPSC-30 and EPSC-31 are the bridge to the second. EPSC tail and adapter results address the third. None substitutes for another.

For the retained finite state, total and shell-energy readers are invariant under spatial translation. The structural ceilings are

\[
\operatorname{rank}D\mathcal E_R\le\min(R+1,d_N-3),
\]

\[
\operatorname{rank}D\mathcal J_R\le\min(m_N+(m_N-1)R,d_N-3).
\]

Exact shell-energy reproduction now reaches the structural ceiling at its first admissible order for three consecutive fixed finite cutoffs:

\[
\boxed{(N,R_I^{min},d_N-3)=(1,23,49),(2,30,245),(3,39,681).}
\]

The `N=2` focused exact checker uses nine shells and gives rank `241` at `R=29` and rank `245` at `R=30`, so the middle case is both saturated and structurally earliest. This is finite evidence, not induction.

When a fixed finite reader reaches rank `d_N-3` at a state where the translation action is locally free, an explicit transverse three-symmetry gauge leaves a `(d_N-3)`-dimensional slice. Selecting a nonzero square minor on that slice gives a local finite chart `H_N`:

\[
\boxed{
\text{rank saturation modulo translation}
\to
\text{transverse finite slice}
\to
\det DH_N(x_*)\ne0.
}
\]

That is the structural-to-local-inverse bridge registered as `PROP-EPSC-30`. It is still not an error radius.

For a declared convex branch `B_N`, if a fixed preconditioner `A_N` satisfies

\[
q_N:=\sup_{x\in B_N}\|I-A_NDH_N(x)\|<1,
\]

then the quantitative inner certificate is

\[
\boxed{
\rho_N\le
\frac{\|A_N\|}{1-q_N}
(\sigma_{meas}+\sigma_{res}).
}
\]

This is `PROP-EPSC-31`. If the branch, symmetry slice, preconditioner enclosure or `q_N<1` proof is missing, the correct verdict remains `HOLD`.

## Full N=1 finite inverse: current certified chain

For `N=1`, the finite real Fourier-Galerkin state dimension is 52. Fixing a transverse gauge for the three spatial-translation directions leaves a 49-dimensional slice. An explicit selected `49x49` shell-energy Taylor-jet minor is nonzero, so a local real inverse exists on that slice.

Successive fail-closed quantitative certificates removed distinct sources of proof slack:

\[
10^{-7934}
\longrightarrow
10^{-3878}
\longrightarrow
10^{-59}
\longrightarrow
10^{-28}
\longrightarrow
\boxed{10^{-17}}.
\]

The latest exact centered entrywise enclosure propagates finite state, tangent and Jacobian radii with exact common-denominator integer arithmetic on

\[
\|x-x_*\|_\infty\le10^{-17},
\]

and uses the exact rational center preconditioner. The reproduced defect is

\[
\boxed{q=0.08058674502845<1/2},
\]

so the `10^-17` state-space local inverse box is certified and is registered in Toledo as `PROP-EPSC-33`. This is substantially stronger than the earlier coarse positive-radius certificates but is still not, by itself, a physical sensor tolerance or a branch-capture theorem.

The open `N=1` inner frontier is now **measurement readiness**: certify that noisy observations and the reconstructed state lie in the same inverse branch and map a physically interpreted observation uncertainty into a useful `rho_1`.

## Resolution evidence and the arbitrary-finite-N target

The exact structural record now includes `N=1` total energy, `N=1` shell energy, `N=2` total energy, `N=2` shell energy, and `N=3` shell energy. The new `N=2` shell result closes the missing structural middle case:

\[
\operatorname{rank}D\mathcal J_{2,29}=241<245,
\qquad
\operatorname{rank}D\mathcal J_{2,30}=245=d_2-3.
\]

Even with shell saturation certified at `N=1,2,3`, this remains three finite cases, not a proof of `PROP-NSOBS-07`. The finite-first target is constructive:

\[
\boxed{
N<\infty
\mapsto
\mathcal C_N=(S_N,H_N,A_N,B_N,q_N),
\qquad q_N<1.
}
\]

This is the `PROP-EPSC-32` programme. “All N” means an algorithm/schema that accepts any particular finite `N` and emits a finite proof object; it does not require postulating a completed infinite-resolution state.

The immediate next quantitative replication is therefore not another `N=2` rank computation. It is to take the already-saturated `N=2` shell jet at `R=30`, construct a 245-dimensional translation slice and square chart, and certify a preconditioned branch defect `q_2<1`, producing a fixed-finite `rho_2` certificate analogous to the `N=1` result.

## Transfer interpretation

For finite Fourier-Galerkin Navier--Stokes shell energy,

\[
\dot I_s=T_s-2\nu sI_s+F_s,
\qquad
\sum_sT_s=0
\]

in the unforced closed truncation. Internal transfer therefore preserves total retained energy while redistributing it among shells. For prescribed forcing,

\[
T=\dot I+2\nu SI-F,
\]

so `(I,T)` and `(I,dI/dt)` are an affine reparameterization at first order; transfer variables do not manufacture extra local rank. Their value is mechanism visibility and finite-window balance measurement. Time integration gives a derivative-free route to bounded transfer observations and is one input to the noise-aware EPSC-19 programme.

## Outer completeness and composition

Only after an inner finite certificate `rho_N` exists do we optionally attach a separate outer/continuum adapter. For an unforced Leray-Hopf trajectory on the `2*pi` periodic three-torus, one EPSC route supplies

\[
\|(I-P_N)u\|_{L^2(0,T;L^2_x)}
\le
\frac{\|u_0\|_2}{\sqrt{2\nu}(N+1)}.
\]

A terminal route uses a certified comparison path and the residual-based relative-energy adapter. These are external analytic adapters; they are not premises of the finite-native observability/inversion proof.

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

## Current fail-closed chain

The finite-native core is

\[
\boxed{
\text{finite measurements}
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

The optional downstream continuum interpretation is

\[
\boxed{
(\rho_N,\beta_N)
\to
\sqrt{\rho_N^2+\beta_N^2}
\to
\varepsilon\text{-verdict}.
}
\]

If either certificate required for the declared target is absent, the correct status is `HOLD`.

## What must NOT be imported into Genesis root

The following remain application-local and must not be promoted into `READOUT_GENESIS_CORE.md`: tested Taylor-Green cutoffs; finite numerical thresholds; claims that any finite cutoff is automatically continuum-complete; claims that local observability equals global reconstruction; claims that a raw Galerkin path equals the continuum projection; claims that continuum ontology has been disproved; claims that transfer connectivity or three fixed cutoffs prove all-resolution observability saturation; claims of turbulent DNS adequacy from finite tests; claims of global Navier--Stokes regularity or blow-up; or claims that the Clay Millennium problem has been solved.

The application-level lesson is now sharper:

> a finite readout can first be asked to certify what it determines **inside** a finite representation; only after that may a separately justified adapter certify what the declared target permits to remain **outside** it.

Genesis records this interpretation and the current boundary only. The mathematics remains owned and reproduced in the domain and finite-math repositories.
