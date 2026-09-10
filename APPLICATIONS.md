# Readout Genesis — External Application Map

This file maps **applications of the Readout/retention programme** without promoting their domain-specific mathematical or numerical results into the Genesis root canon.

Rule: an external application may cite Genesis concepts, but its mathematical/empirical claims remain owned by the repository where they are proved or tested. Application evidence does not flow backward into `READOUT_GENESIS_CORE.md` automatically.

## Navier–Stokes / Energy Observability / Discrete Epsilon-Completion

Status: **external research application; not a registered Genesis domain and not a root theorem**.

### Ownership map

| Layer | Repository | Role |
|---|---|---|
| General discrete mathematics | `morrocwi/information-discrete-math` | finite refinement, fail-closed certification, spectral/energy-budget certificates, relative-energy and exact-tape adapters, observable-to-continuum composition |
| Equation/proposal provenance | `morrocwi/toledo` | EPSC and NSOBS proposal IDs, lineage, tier/status, later canonical registration if reviewed |
| Navier–Stokes application | `morrocwi/readout-problem-navier-stokes` | NS-specific observability analysis, finite experiments, proof notes, reproduction, manuscripts and claim boundary |
| Interpretation | `morrocwi/readout_genesis` | records the readout interpretation only; does not own the NS mathematics |

### Toledo proposal families

The EPSC family now runs through `PROP-EPSC-19`:

- `PROP-EPSC-01..15` — nested-refinement, target-indexed tail, energy/relative-energy and exact-dyadic RK4 path certificate family;
- `PROP-EPSC-16` — **OPEN** scalable/tight high-cutoff certified enclosure;
- `PROP-EPSC-17` — observable-to-continuum orthogonal composition certificate;
- `PROP-EPSC-18` — **OPEN** certified energy-jet inversion radius;
- `PROP-EPSC-19` — **OPEN** noise-stable measurement-to-continuum certificate.

The NS energy-observability family is registered as `PROP-NSOBS-01..08`:

- `PROP-NSOBS-01` — finite real phase-space dimension;
- `PROP-NSOBS-02` — scalar total-energy Lie-jet ceiling and minimum structural depth;
- `PROP-NSOBS-03` — shell-energy Lie-jet ceiling and minimum structural depth;
- `PROP-NSOBS-04` — positive-viscosity rank universality;
- `PROP-NSOBS-05` — four exact finite saturation records;
- `PROP-NSOBS-06` — measurement-channel versus temporal-depth tradeoff;
- `PROP-NSOBS-07` — **OPEN** all-resolution earliest-order saturation conjecture;
- `PROP-NSOBS-08` — local finite-state completeness modulo spatial translations at certified saturation cases.

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

### Why rank alone is not a certificate

A saturated observation Jacobian establishes local differential identifiability modulo symmetry. It does **not** automatically give a constructive inverse, a certified branch, a condition-number bound, or a retained-state error radius `rho_N` under noisy measurements.

Therefore `PROP-EPSC-18` remains open. The practical noisy extension `PROP-EPSC-19` remains open as well. The all-resolution saturation conjecture `PROP-NSOBS-07` is another independent open problem.

These should not be confused with `PROP-EPSC-16`, which concerns the cost and tightness of the already-valid outer path certificate at larger cutoff and horizon.

### Genesis interpretation

This application sharpens the readout discipline without turning it into ontology:

> completeness has at least two separable components: completeness **inside the chosen representation for a declared reader**, and a proved bound on what the representation **leaves outside**.

The application-level chain is now

\[
\text{measurements}
\to
\rho_N\text{ for the retained quotient state}
\to
\beta_N\text{ for the omitted tail}
\to
\sqrt{\rho_N^2+\beta_N^2}
\to
\varepsilon\text{-verdict}.
\]

If either certificate is missing, the correct status is `HOLD`.

### What must NOT be imported into the Genesis root

The following remain application-local: Taylor-Green cutoff values and numerical thresholds; claims that any tested cutoff is automatically continuum-complete; claims that local observability rank equals global/stable reconstruction; claims that a raw Galerkin trajectory equals the continuum projection; claims that continuum ontology has been disproved; claims that the Clay Navier-Stokes problem has been solved; claims of turbulent DNS adequacy from a short finite run; or claims that the current conservative certificate remains tight at arbitrarily large `N` and `T`.

### Current application frontiers

The combined programme now has distinct frontiers rather than one undifferentiated gap:

- `PROP-NSOBS-07`: prove/refute earliest-order generic saturation for every finite Fourier resolution;
- `PROP-EPSC-18`: construct a quantitative certified inverse from energy jets to a retained-state quotient radius;
- `PROP-EPSC-19`: propagate measurement/noise/differentiation uncertainty through that inverse and the EPSC tail bound;
- `PROP-EPSC-16`: independently improve tightness and computational scaling of outer certification at larger cutoff/horizon.

Genesis records these boundaries and their interpretation only. It does not promote them into root ontology.
