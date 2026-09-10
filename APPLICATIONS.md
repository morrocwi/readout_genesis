# Readout Genesis — External Application Map

This file maps **applications of the Readout/retention programme** without promoting their domain-specific mathematical or numerical results into the Genesis root canon.

Rule: an external application may cite Genesis concepts, but its mathematical/empirical claims remain owned by the repository where they are proved or tested. Application evidence does not flow backward into `READOUT_GENESIS_CORE.md` automatically.

## Navier–Stokes / Discrete Epsilon-Completion

Status: **external research application; not a registered Genesis domain and not a root theorem**.

### Ownership map

| Layer | Repository | Role |
|---|---|---|
| General discrete mathematics | `morrocwi/information-discrete-math` | finite refinement, nested consistency, fail-closed certification, reusable spectral-tail certificate machinery |
| Equation/proposal provenance | `morrocwi/toledo` | proposal IDs, lineage, tier/status, later canonical registration if reviewed |
| Navier–Stokes application | `morrocwi/readout-problem-navier-stokes` | NS-specific Fourier-Galerkin experiment, analytic tail note, reproduction, frozen results, claim boundary |
| Interpretation | `morrocwi/readout_genesis` | explains how the application relates to retained/readout language; does not own the NS theorem |

### Registered proposal family

Toledo proposal file: `registry/proposals/discrete_epsilon_completion.json`.

The original core remains:

- `PROP-EPSC-01`: Nested Readout Consistency Defect
  \[
  \delta_K=\|R_Kx_{K+1}-x_K\|.
  \]
- `PROP-EPSC-02`: Navier-Stokes Fourier boundary-energy diagnostic.
- `PROP-EPSC-03`: fail-closed epsilon-completion acceptance protocol.
- `PROP-EPSC-04`: computable omitted-information/tail certificate target.

The 2026-09-10 analytic refinement adds:

- `PROP-EPSC-05`: terminal finite-Fourier-readout non-identifiability obstruction;
- `PROP-EPSC-06`: spectral `H^s -> L2` tail inequality;
- `PROP-EPSC-07`: Leray-Hopf spacetime Fourier-tail certificate;
- `PROP-EPSC-08`: Lipschitz readout lift;
- `PROP-EPSC-09`: conditional terminal `H^s` certificate.

These remain Toledo **proposal identifiers**, not canonical verified Toledo theorem codes.

### What changed conceptually

The earlier EPSC formulation asked for one undifferentiated object

\[
\|(I-P_K)x\|\le\beta_K.
\]

The Navier-Stokes analysis shows that this question is not well posed until the **target norm/readout and admissible class are declared**.

For an unrestricted terminal Fourier state, finite retained coefficients cannot identify the omitted tail: one may add a divergence-free conjugate pair entirely outside the cutoff without changing the retained record. Thus a terminal finite record is not automatically a complete description of the richer target.

For an unforced Leray-Hopf Navier-Stokes trajectory on the periodic three-torus, however, the standard energy inequality plus the spectral tail inequality gives

\[
\|(I-P_K)u\|_{L^2(0,T;L^2_x)}
\le
\frac{\|u_0\|_2}{\sqrt{2\nu}(K+1)}.
\]

The right-hand side tends to zero. This is therefore a genuine omitted-information certificate **for that declared spacetime norm**, not for arbitrary terminal reconstruction.

A Lipschitz readout `Q` inherits the bound:

\[
\|Q(u)-Q(P_Ku)\|\le L_Q\beta_K.
\]

In particular, the time-averaged field has an `L2` tail bounded by `beta_K/sqrt(T)`.

### Genesis interpretation

This application sharpens a central readout discipline without turning the application into ontology:

> completeness is always completeness **for a declared reader/norm under declared assumptions**.

The mathematical lesson is therefore not "the continuum is unnecessary in every sense." It is narrower:

\[
\text{finite retained record}
+\text{proved omitted-distinction bound in target }Y
\Longrightarrow
\text{epsilon-completeness in }Y.
\]

Without the second term, the verdict is `HOLD`.

This is consistent with the Genesis claim boundary that `[finite_diagnostic]` evidence must not be promoted into a stronger statement merely because it fits the narrative. The positive spacetime certificate is owned by the NS/IDM mathematical layer; Genesis only records the interpretation.

### What must NOT be imported into the Genesis root

The following remain application-local and must not be written into the root canon as universal facts:

- the recorded Taylor-Green values at K=1..5;
- the specific `1e-6` and `1e-8` numerical diagnostic thresholds;
- the statement that K=5 is continuum-complete;
- the claim that every terminal Navier-Stokes state has a finite-record-only `beta_K`;
- claims that continuum ontology has been disproved;
- claims that the Clay Navier-Stokes problem has been solved;
- claims of physical/DNS turbulence adequacy from the short finite run.

### What remains open

The spacetime result does **not** supply an unconditional pointwise terminal `H^s` bound for arbitrary 3-D Navier-Stokes data. If such a bound `M_s(T)` is separately certified, then

\[
\|(I-P_K)u(T)\|_2\le\frac{M_s(T)}{(K+1)^s}.
\]

Producing that globally valid terminal regularity control is precisely where the classical 3-D difficulty can re-enter. Genesis should preserve this boundary rather than convert the partial closure into a universal claim.
