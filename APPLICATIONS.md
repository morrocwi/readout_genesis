# Readout Genesis — External Application Map

This file maps **applications of the Readout/retention programme** without promoting domain-specific mathematical or numerical results into the Genesis root canon.

Rule: an external application may cite Genesis concepts, but its mathematical and empirical claims remain owned by the repository where they are proved or tested. Application evidence does not flow backward into `READOUT_GENESIS_CORE.md` automatically.

## Navier–Stokes / Energy Observability / Discrete Epsilon-Completion

Status: **external research application; not a registered Genesis domain and not a root theorem**.

### Ownership map

| Layer | Repository | Role |
|---|---|---|
| General finite-first mathematics | `morrocwi/information-discrete-math` | refinement, fail-closed certification, target-indexed tail bounds, relative-energy and interval-inverse primitives |
| Equation/proposal provenance | `morrocwi/toledo` | EPSC/NSOBS proposal identifiers, lineage, tier/status, later canonical review |
| Navier–Stokes specialization | `morrocwi/readout-problem-navier-stokes` | finite Fourier-Galerkin analysis, reproduction, observability, EPSC certificates, manuscripts |
| Interpretation | `morrocwi/readout_genesis` | application map only; does not own the NS mathematics |

### Current EPSC proposal map

The EPSC proposal family now runs through `PROP-EPSC-26`.

- `PROP-EPSC-01..15` — nested refinement, target-indexed omitted-tail bounds, energy/relative-energy adapters, and exact finite RK4-path certification.
- `PROP-EPSC-16` — **OPEN** scalable/tight high-cutoff continuous-time enclosure.
- `PROP-EPSC-17` — observable-to-continuum orthogonal composition.
- `PROP-EPSC-18` — finite retained-state inversion programme. Full `N=1` local inverse existence and a strictly positive quantitative radius are now closed in a conservative sense; a useful measurement-scale radius remains open.
- `PROP-EPSC-19` — **OPEN** full noise-stable measurement-to-continuum certificate.
- `PROP-EPSC-20` — quantitative reduced three-mode inverse witness.
- `PROP-EPSC-21` — derivative-free finite-window shell-transfer uncertainty certificate.
- `PROP-EPSC-22` — full `N=1` 49-dimensional symmetry-slice local inverse existence.
- `PROP-EPSC-23` — exact rational interval/preconditioned inverse criterion.
- `PROP-EPSC-24` — **OPEN** practically informative `rho_1` for the full `N=1` inverse.
- `PROP-EPSC-25` — conservative explicit positive full-`N=1` radius from uniform Cramer/Hadamard bounds.
- `PROP-EPSC-26` — row-aware Hadamard tightening of that radius.

These are Toledo **proposal identifiers**, not canonical verified theorem codes.

### Two completeness layers

The application separates two logically different questions.

**Inner completeness:** does a declared observation process determine the represented finite state, modulo unavoidable symmetry?

**Outer completeness:** how much information can remain outside the represented finite cutoff in the declared target norm/readout?

For Fourier cutoff `P_N`, energy observability addresses the first layer and EPSC tail/adaptor results address the second. Neither substitutes for the other.

For the retained finite state, total and shell-energy readers are invariant under spatial translation. The structural ceilings are

\[
\operatorname{rank}D\mathcal E_R\le\min(R+1,d_N-3),
\]

\[
\operatorname{rank}D\mathcal J_R\le\min(m_N+(m_N-1)R,d_N-3).
\]

Exact modular witnesses reach the translation ceiling at the earliest structurally allowed order in the recorded cases `N=1` total energy, `N=1` shell energy, `N=2` total energy, and `N=3` shell energy. This establishes local finite identifiability modulo translation in those cases, not global injectivity.

### Full N=1 inverse: what is now closed

For `N=1`, the finite real Fourier-Galerkin state has dimension 52. Removing the three translation directions gives a 49-dimensional symmetry slice. An explicit 49-by-49 shell-energy Taylor-jet minor is nonzero, so a local real inverse exists on that slice.

A later finite certificate turns local existence into an explicit positive radius. The first conservative construction used a single worst-row Jacobian/Hessian majorant and gave

\[
10^{-7934}<r_1\le10^{-7933},
\qquad
\|J_0^{-1}(J(x)-J_0)\|_\infty\le\tfrac12.
\]

`PROP-EPSC-26` keeps one majorant for each selected observation row. If

\[
R_j\ge\|J_{0,j*}\|_1,
\qquad
H_j\ge\sup_{x\in B}\|D J_{j*}(x)\|_{\infty\to1},
\]

then integer nonzero determinant plus row-wise Hadamard cofactors give

\[
\|J_0^{-1}(J(x)-J_0)\|_\infty
\le
r\sum_j\left(\prod_{k\ne j}R_k\right)H_j.
\]

Choosing

\[
\boxed{
 r=\frac{1}{2\sum_j(\prod_{k\ne j}R_k)H_j}
}
\]

again gives `q<=1/2`, but removes thousands of decimal orders of avoidable slack from the uniform-row proof. This is a genuine tightening of a rigorous lower bound; it is **not** yet a practical estimate of the actual inverse conditioning.

The remaining `PROP-EPSC-24` frontier is therefore narrower: construct an actual entrywise interval Jacobian and effective rational preconditioner, certify branch containment, and obtain a measurement-informative `rho_1`.

### Outer omitted-information certificates

For an unforced Leray-Hopf trajectory on the normalized periodic setting used by the NS application,

\[
\|(I-P_N)u\|_{L^2(0,T;L^2_x)}
\le
\frac{\|u_0\|_2}{\sqrt{2\nu}(N+1)}.
\]

A terminal route uses a certified comparison path `v`, residual

\[
r=\partial_t v+P[(v\cdot\nabla)v]-\nu\Delta v-Pf,
\]

and relative energy. With

\[
A_T=2\int_0^T\|\nabla v\|_\infty dt,
\qquad
B_T=\int_0^T\|r\|_{H^{-1}}^2dt,
\]

one obtains the conditional terminal adapter

\[
\sup_{0\le t\le T}\|u(t)-v(t)\|_2^2
\le
e^{A_T}\left(e_0^2+\frac{B_T}{\nu}\right).
\]

The repository contains an exact finite construction from stored binary64 RK4 nodes to a rational piecewise-linear comparison path with certified continuous-time summaries. This does not imply turbulent DNS adequacy or global regularity.

### Observable-to-continuum composition

If the retained inversion supplies

\[
\inf_{g\in G}\|P_Nu(T)-g\widehat x_N\|_2\le\rho_N
\]

and an independent EPSC certificate supplies

\[
\|(I-P_N)u(T)\|_2\le\beta_N,
\]

orthogonality gives

\[
\boxed{
\inf_{g\in G}\|u(T)-g\widehat x_N\|_2
\le
\sqrt{\rho_N^2+\beta_N^2}.
}
\]

For the NS energy-reader application, `G=T^3` is spatial translation. Retained uncertainty and omitted-tail uncertainty are separate budgets; a final epsilon verdict requires both.

### Transfer bridge

For finite Fourier-Galerkin NS shell energy,

\[
\dot I_s=T_s-2\nu sI_s+F_s,
\qquad
\sum_sT_s=0
\]

for the unforced closed truncation. Hence total energy collapses internal redistribution while shell-energy readers retain it. For prescribed forcing,

\[
T=\dot I+2\nu SI-F,
\]

so `(I,T)` and `(I,dI/dt)` carry the same local rank information; transfer variables expose mechanism but do not manufacture new information.

Integrated over a window,

\[
\int_{t_0}^{t_1}T_sdt
=I_s(t_1)-I_s(t_0)+2\nu s\int_{t_0}^{t_1}I_sdt-\int_{t_0}^{t_1}F_sdt,
\]

which supports certified transfer summaries without high-order numerical differentiation.

A constructive all-cutoff triad-connectivity lemma removes one kinematic obstruction to the all-`N` saturation problem, but it does not prove the required nonvanishing/algebraic independence of enough observation minors.

### Current fail-closed chain

The intended application chain is

\[
\text{measurements/windows}
\to\text{finite observation certificate}
\to\rho_N
\to\beta_N
\to\sqrt{\rho_N^2+\beta_N^2}
\to\varepsilon\text{-verdict}.
\]

If a required quantitative retained-state certificate or omitted-tail certificate is missing, the correct end-to-end status is `HOLD`.

### What must NOT be imported into the Genesis root

The following remain application-local and must not be promoted into root ontology: specific Taylor-Green cutoffs or thresholds; claims that any tested cutoff is automatically continuum-complete; claims that local rank implies global/stable reconstruction; claims that a raw Galerkin trajectory equals the continuum projection; claims that continuum mathematics or ontology has been disproved; claims that the Clay Navier-Stokes problem is solved; claims of turbulent DNS adequacy from short finite runs; claims that triad connectivity proves all-`N` saturation; or claims that the present conservative inverse radius is a realistic sensor tolerance.

### Current frontiers

- `PROP-EPSC-24`: replace conservative determinant/derivative majorants by an effective entrywise interval/Krawczyk certificate and obtain a useful `rho_1`.
- `PROP-EPSC-19`: propagate measurement/window uncertainty through that inverse and combine it with an EPSC tail certificate.
- `PROP-NSOBS-07`: prove or refute all-resolution earliest-order observability saturation after the connectivity obstruction has been removed.
- `PROP-EPSC-16`: improve outer comparison-path certificate tightness and scaling at larger cutoff/horizon.

Genesis records these boundaries and their interpretation only. It does not promote them into root ontology.
