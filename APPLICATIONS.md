# Readout Genesis — External Application Map

This file maps **applications of the Readout/retention programme** without promoting their domain-specific mathematical or numerical results into the Genesis root canon.

Rule: an external application may cite Genesis concepts, but its mathematical/empirical claims remain owned by the repository where they are proved or tested. Application evidence does not flow backward into `READOUT_GENESIS_CORE.md` automatically.

## Navier–Stokes / Energy Observability / Discrete Epsilon-Completion

Status: **external research application; not a registered Genesis domain and not a root theorem**.

### Ownership map

| Layer | Repository | Role |
|---|---|---|
| General discrete mathematics | `morrocwi/information-discrete-math` | finite refinement, fail-closed certification, spectral/energy-budget certificates, relative-energy and exact-tape adapters, observable-to-continuum composition, energy-transfer helper algebra |
| Equation/proposal provenance | `morrocwi/toledo` | EPSC and NSOBS proposal IDs, lineage, tier/status, later canonical registration if reviewed |
| Navier–Stokes application | `morrocwi/readout-problem-navier-stokes` | NS-specific observability analysis, finite experiments, proof notes, reproduction, manuscripts and claim boundary |
| Interpretation | `morrocwi/readout_genesis` | records the readout interpretation only; does not own the NS mathematics |

### Toledo proposal families

The EPSC family now runs through `PROP-EPSC-21`:

- `PROP-EPSC-01..15` — nested-refinement, target-indexed tail, energy/relative-energy and exact-dyadic RK4 path certificate family;
- `PROP-EPSC-16` — **OPEN** scalable/tight high-cutoff certified enclosure;
- `PROP-EPSC-17` — observable-to-continuum orthogonal composition certificate;
- `PROP-EPSC-18` — **OPEN** certified energy-jet inversion radius for the full finite Fourier quotient;
- `PROP-EPSC-19` — **OPEN** full noise-stable measurement-to-continuum certificate;
- `PROP-EPSC-20` — quantitative inverse-radius witness for the existing analytic three-mode reduced NS subcase;
- `PROP-EPSC-21` — derivative-free finite-window shell-transfer uncertainty certificate.

The NS energy-observability family now runs through `PROP-NSOBS-11`:

- `PROP-NSOBS-01` — finite real phase-space dimension;
- `PROP-NSOBS-02` — scalar total-energy Lie-jet ceiling and minimum structural depth;
- `PROP-NSOBS-03` — shell-energy Lie-jet ceiling and minimum structural depth;
- `PROP-NSOBS-04` — positive-viscosity rank universality;
- `PROP-NSOBS-05` — four exact finite saturation records;
- `PROP-NSOBS-06` — measurement-channel versus temporal-depth tradeoff;
- `PROP-NSOBS-07` — **OPEN** all-resolution earliest-order saturation conjecture;
- `PROP-NSOBS-08` — local finite-state completeness modulo spatial translations at certified saturation cases;
- `PROP-NSOBS-09` — finite shell-energy transfer balance and total-transfer conservation;
- `PROP-NSOBS-10` — affine equivalence of `(I,T)` and `(I,dI/dt)` for the declared forcing scope;
- `PROP-NSOBS-11` — all-cutoff kinematic triad-transfer connectivity lemma.

These are Toledo **proposal identifiers**, not canonical verified theorem codes.

### Two completeness layers

The synthesis distinguishes two different questions.

**Inner completeness:** does the declared observation process determine the represented finite state, modulo unavoidable symmetry?

**Outer completeness:** how much unrepresented continuum information can remain above the cutoff?

For a Fourier cutoff `P_N`, the energy-observability work addresses the first layer. EPSC addresses the second. Neither substitutes for the other.

At the finite observability layer, total and shell energy readers are translation-invariant. Structural rank ceilings are

\[
\operatorname{rank}D\mathcal E_R\le\min(R+1,d_N-3),
\]

\[
\operatorname{rank}D\mathcal J_R\le\min(m_N+(m_N-1)R,d_N-3).
\]

Exact modular certificates reach the translation ceiling at the earliest structurally allowed order in four recorded reader-resolution cases: `N=1` total and shell energy, `N=2` total energy, and `N=3` shell energy. This yields local quotient-state identifiability in those cases, not a global or noise-stable inverse.

At the outer layer, EPSC provides target-specific omitted-tail bounds. For an unforced Leray-Hopf trajectory,

\[
\|(I-P_N)u\|_{L^2(0,T;L^2_x)}
\le
\frac{\|u_0\|_2}{\sqrt{2\nu}(N+1)}.
\]

A terminal residual-based route uses a certified comparison path and the relative-energy adapter. `PROP-EPSC-15` supplies one exact finite construction from stored binary64 RK4 nodes to a rational piecewise-linear path with certified residual summaries.

### Observable-to-continuum composition

The two layers connect only after the finite observation side supplies a **quantitative** retained-state radius.

If a certified inversion gives

\[
\inf_{g\in G}\|P_Nu(T)-g\widehat x_N\|_2\le\rho_N
\]

and EPSC independently gives

\[
\|(I-P_N)u(T)\|_2\le\beta_N,
\]

then orthogonality of the retained and omitted Fourier subspaces gives

\[
\boxed{
\inf_{g\in G}\|u(T)-g\widehat x_N\|_2
\le
\sqrt{\rho_N^2+\beta_N^2}.
}
\]

For the NS energy-reader application, `G=T^3` is spatial translation. This is the application-level result registered as `PROP-EPSC-17`.

The square-root composition matters conceptually: uncertainty inside the retained representation and uncertainty outside it are separate orthogonal budgets. A final tolerance verdict requires both.

### Restoration / transfer interpretation and the NS shell balance

The current Genesis core contains the interpretive split in which a restoring part responds to imbalance while oriented/skew structure carries transfer. The older step-by-step formulation also uses the phrase "force = recovery from disequilibrium; energy = transmitted difference." This application **does not treat that language as a derivation of physical Navier-Stokes energy**. It uses it only as an interpretive map after the NS equations have supplied their own standard energy identity.

For the finite Fourier-Galerkin NS application,

\[
\dot I_s=T_s-2\nu s I_s+F_s,
\qquad
\sum_sT_s=0
\]

in the unforced closed truncation. Here the viscous term is dissipative, while the quadratic nonlinearity redistributes retained energy among shells.

This makes a previously implicit point explicit: the total-energy reader collapses internal transfer because `sum_s T_s=0`, whereas the shell reader keeps the redistribution pattern visible.

For prescribed forcing,

\[
T=\dot I+2\nu SI-F.
\]

Therefore `(I,T)` and `(I,dI/dt)` are related by an invertible affine block transform and have the same local observation rank. Transfer variables do **not** manufacture new information beyond the first shell-energy jet. Their benefit is that they expose the mechanism and support finite-window balance measurements.

Integrating over a window gives

\[
\int_{t_0}^{t_1}T_sdt
=I_s(t_1)-I_s(t_0)+2\nu s\int_{t_0}^{t_1}I_sdt-\int_{t_0}^{t_1}F_sdt,
\]

so a transfer summary can be certified without high-order numerical differentiation. This is registered as the partial `PROP-EPSC-21` result and narrows, but does not close, `PROP-EPSC-19`.

### What the new transfer bridge closes

A constructive lemma now removes one possible obstruction to `PROP-NSOBS-07`: for every `N>=2`, every newly introduced boundary mode `k` with `||k||_infinity=N` has a non-collinear triad `p+q=k` with `p` already in `K_{N-1}`. Thus every new boundary mode is kinematically attached to the previous cutoff, and every new shell has a transfer-hypergraph connection to an old shell.

This does **not** prove all-`N` saturation. The remaining problem is algebraic independence/nonvanishing of enough observation minors after the translation symmetry directions are removed.

The existing analytic three-mode NS subcase has also been upgraded from qualitative observability to a quantitative reduced inverse. For `c_a=3/10`, `|a|^2=1`,

\[
J_{1,a}=2c_a r-2\nu x,
\qquad
r=\frac{J_{1,a}+2\nu x}{2c_a},
\]

and certified input radii give

\[
|r-\widehat r|
\le
\frac{\sigma_J+2\nu\sigma_x}{2|c_a|}.
\]

This is `PROP-EPSC-20`: a real quantitative witness for the **reduced triad subcase**. It must not be cited as closure of `PROP-EPSC-18` for the 52-dimensional `N=1` cube or arbitrary `N`.

### Why rank alone is not a certificate

A saturated observation Jacobian establishes local differential identifiability modulo symmetry. It does **not** automatically give a constructive inverse, a certified branch, a condition-number bound, or a retained-state error radius `rho_N` under noisy measurements.

Therefore `PROP-EPSC-18` remains open for the full finite Fourier quotient. The practical full noisy extension `PROP-EPSC-19` remains open as well, although `PROP-EPSC-21` removes numerical differentiation from one transfer-observation substep. The all-resolution saturation conjecture `PROP-NSOBS-07` is also still open, now narrowed past the connectivity issue.

These should not be confused with `PROP-EPSC-16`, which concerns the cost and tightness of the already-valid outer path certificate at larger cutoff and horizon.

### Genesis interpretation

This application sharpens the readout discipline without turning it into ontology:

> completeness has at least two separable components: completeness **inside the chosen representation for a declared reader**, and a proved bound on what the representation **leaves outside**.

The transfer bridge adds another non-collapse:

> total retained energy is not the same readout as the internal redistribution pattern that preserves that total.

The application-level chain is now

\[
\text{shell-energy measurements/windows}
\to\text{certified transfer summaries}
\to\rho_N\text{ for the retained quotient state}
\to\beta_N\text{ for the omitted tail}
\to\sqrt{\rho_N^2+\beta_N^2}
\to\varepsilon\text{-verdict}.
\]

If either the full retained-state certificate or the tail certificate is missing, the correct end-to-end status is `HOLD`.

### What must NOT be imported into the Genesis root

The following remain application-local: Taylor-Green cutoff values and numerical thresholds; claims that any tested cutoff is automatically continuum-complete; claims that local observability rank equals global/stable reconstruction; claims that a raw Galerkin trajectory equals the continuum projection; claims that continuum ontology has been disproved; claims that the Clay Navier-Stokes problem has been solved; claims of turbulent DNS adequacy from a short finite run; claims that the Genesis phrase "transmitted difference" is numerically identical to SI Joules without a domain translation; claims that triad connectivity implies observability-rank saturation; or claims that the current conservative certificate remains tight at arbitrarily large `N` and `T`.

### Current application frontiers

The combined programme now has distinct, narrower frontiers:

- `PROP-NSOBS-07`: after all-`N` kinematic connectivity, prove/refute nonvanishing/algebraic independence sufficient for earliest-order generic saturation at every finite resolution;
- `PROP-EPSC-18`: extend the quantitative inverse from the triad witness to a gauge-fixed, branch-certified full finite Fourier quotient radius;
- `PROP-EPSC-19`: propagate measured window uncertainty through that full inverse and the EPSC tail bound; `PROP-EPSC-21` closes only the derivative-free transfer-observation substep;
- `PROP-EPSC-16`: independently improve tightness and computational scaling of outer certification at larger cutoff/horizon.

Genesis records these boundaries and their interpretation only. It does not promote them into root ontology.
