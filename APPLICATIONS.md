# Readout Genesis — External Application Map

This file maps **applications of the Readout/retention programme** without promoting their domain-specific mathematical or numerical results into the Genesis root canon.

Rule: an external application may cite Genesis concepts, but its mathematical/empirical claims remain owned by the repository where they are proved or tested. Application evidence does not flow backward into `READOUT_GENESIS_CORE.md` automatically.

## Navier–Stokes / Discrete Epsilon-Completion

Status: **external research application; not a registered Genesis domain and not a root theorem**.

### Ownership map

| Layer | Repository | Role |
|---|---|---|
| General discrete mathematics | `morrocwi/information-discrete-math` | finite refinement, nested consistency, fail-closed certification, spectral and terminal energy-budget certificate machinery |
| Equation/proposal provenance | `morrocwi/toledo` | proposal IDs, lineage, tier/status, later canonical registration if reviewed |
| Navier–Stokes application | `morrocwi/readout-problem-navier-stokes` | NS-specific Fourier-Galerkin experiment, analytic certificate notes, reproduction, frozen results, claim boundary |
| Interpretation | `morrocwi/readout_genesis` | explains how the application relates to retained/readout language; does not own the NS mathematics |

### Registered proposal family

Toledo registration is split across:

- `registry/proposals/discrete_epsilon_completion.json` — `PROP-EPSC-01..09`;
- `registry/proposals/discrete_epsilon_completion_terminal_energy.json` — `PROP-EPSC-10..12`.

The core chain is:

- `PROP-EPSC-01`: Nested Readout Consistency Defect
  \[
  \delta_K=\|R_Kx_{K+1}-x_K\|.
  \]
- `PROP-EPSC-02`: Navier-Stokes Fourier boundary-energy diagnostic.
- `PROP-EPSC-03`: fail-closed epsilon-completion acceptance protocol.
- `PROP-EPSC-04`: target-indexed computable omitted-information certificate.
- `PROP-EPSC-05`: terminal finite-Fourier-readout non-identifiability obstruction.
- `PROP-EPSC-06`: spectral `H^s -> L2` tail inequality.
- `PROP-EPSC-07`: Leray-Hopf spacetime Fourier-tail certificate.
- `PROP-EPSC-08`: Lipschitz readout lift.
- `PROP-EPSC-09`: conditional terminal `H^s` certificate.
- `PROP-EPSC-10`: terminal Leray-Hopf energy-budget tail certificate.
- `PROP-EPSC-11`: energy-defect floor / energy-equality closure.
- `PROP-EPSC-12`: **Open** finite-Galerkin to continuum retained-record adapter certificate.

These remain Toledo **proposal identifiers**, not canonical verified Toledo theorem codes.

### What changed conceptually

The earlier EPSC formulation asked for one undifferentiated object

\[
\|(I-P_K)x\|\le\beta_K.
\]

The Navier-Stokes analysis shows that this question is not well posed until the **target norm/readout and admissible class are declared**.

For an unrestricted terminal Fourier state, finite retained coefficients cannot identify the omitted tail: one may add a divergence-free conjugate pair entirely outside the cutoff without changing the retained record. Thus a terminal finite record is not automatically a complete description of the richer target.

For an unforced Leray-Hopf trajectory on the periodic three-torus, however,

\[
\|(I-P_K)u\|_{L^2(0,T;L^2_x)}
\le
\frac{\|u_0\|_2}{\sqrt{2\nu}(K+1)}.
\]

The right-hand side tends to zero. This is a genuine omitted-information certificate **for that declared spacetime norm**, not for arbitrary terminal reconstruction.

A Lipschitz readout `Q` inherits the bound

\[
\|Q(u)-Q(P_Ku)\|\le L_Q\beta_K,
\]

and the time-averaged field has an `L2` tail bounded by `beta_K/sqrt(T)`.

### Richer retained state: the energy tape

The terminal no-go applies to terminal low-mode coefficients **alone**. It does not say no richer finite record can certify a terminal tail.

The Navier-Stokes energy inequality identifies a useful retained tape:

\[
\mathcal R_K^{EB}
=
\left(
U_0,
L_K(T),
\underline D_K(T)
\right),
\]

where

- `U_0` is a certified upper bound on the initial `L2` norm;
- `L_K(T)` is a certified lower bound on the actual retained terminal norm `||P_Ku(T)||_2`;
- `D_K(T)` is a certified lower bound on retained viscous dissipation `nu int ||grad P_Ku||_2^2 dt`.

Then the NS application proves at analytic (`Dr`) tier

\[
\boxed{
\|(I-P_K)u(T)\|_2
\le
\left[U_0^2-L_K(T)^2-2\underline D_K(T)\right]^{1/2}
}
\]

when the directional certificates are consistent. If the bracket is materially negative, the proper verdict is `HOLD`, not zero tail.

For exact projections, the squared certificate decomposes as

\[
(\beta_K^{EB})^2
=
\|(I-P_K)u(T)\|_2^2
+2\nu\int_0^T\|\nabla(I-P_K)u\|_2^2dt
+\mathcal D_E(T),
\]

where `D_E(T)` is the energy-inequality slack. Consequently the asymptotic floor of this certificate is exactly that slack. If energy equality is independently justified, the floor is zero and the terminal certificate closes as `K -> infinity`.

### Genesis interpretation

This application sharpens a central readout discipline without turning the application into ontology:

> completeness is completeness **for a declared reader/norm under declared assumptions and a sufficient retained record**.

The retained record is therefore itself part of the mathematical problem. Terminal low modes are insufficient, while low-mode energy plus accumulated dissipation and an initial budget can be sufficient for a rigorous upper bound once linked to the actual continuum projection.

The pattern is

\[
\text{finite retained record}
+\text{proved adapter}
+\text{proved omitted-distinction bound in target }Y
\Longrightarrow
\text{epsilon-completeness in }Y.
\]

Without the required bridge, the verdict remains `HOLD`.

This preserves the Genesis claim-boundary rule: `[finite_diagnostic]` evidence must not be promoted merely because it fits the narrative. The positive certificates are owned by the NS/IDM mathematical layers; Genesis records only their interpretation.

### Current frontier

The sharp next problem is `PROP-EPSC-12`:

```text
finite Galerkin output
    -> certified directional adapter error
actual continuum projected terminal energy + dissipation tape
    -> terminal energy-budget certificate
rigorous terminal beta_K
```

The project's finite Galerkin values cannot be silently substituted for the actual `P_Ku` quantities. A certified Galerkin-to-continuum adapter is required.

### What must NOT be imported into the Genesis root

The following remain application-local and must not be written into the root canon as universal facts:

- the recorded Taylor-Green values at K=1..5;
- the specific numerical diagnostic thresholds;
- the statement that K=5 is continuum-complete;
- the claim that every terminal Navier-Stokes state has a finite-record-only `beta_K`;
- the claim that the project's current finite Galerkin output is already a certified continuum projection;
- claims that continuum ontology has been disproved;
- claims that the Clay Navier-Stokes problem has been solved;
- claims of physical/DNS turbulence adequacy from the short finite run.

### What remains open

Two routes to terminal certification are now explicit rather than conflated:

1. a separately certified pointwise `H^s` bound gives
   \[
   \|(I-P_K)u(T)\|_2\le\frac{M_s(T)}{(K+1)^s};
   \]
2. a certified retained energy/dissipation tape gives the a-posteriori energy-budget bound above.

What is still missing for the existing solver is the certified adapter from its finite recurrence to the actual continuum projected tape. Genesis should preserve this boundary rather than convert partial mathematical closure into a universal claim.
