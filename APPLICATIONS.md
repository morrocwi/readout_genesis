# Readout Genesis — External Application Map

This file maps **applications of the Readout/retention programme** without promoting their domain-specific mathematical or numerical results into the Genesis root canon.

Rule: an external application may cite Genesis concepts, but its mathematical/empirical claims remain owned by the repository where they are proved or tested. Application evidence does not flow backward into `READOUT_GENESIS_CORE.md` automatically.

## Navier–Stokes / Discrete Epsilon-Completion

Status: **external research application; not a registered Genesis domain and not a root theorem**.

### Ownership map

| Layer | Repository | Role |
|---|---|---|
| General discrete mathematics | `morrocwi/information-discrete-math` | finite refinement, fail-closed certification, spectral/energy-budget certificates, relative-energy and exact-tape adapter machinery |
| Equation/proposal provenance | `morrocwi/toledo` | EPSC proposal IDs, lineage, tier/status, later canonical registration if reviewed |
| Navier–Stokes application | `morrocwi/readout-problem-navier-stokes` | NS-specific analysis, finite experiments, proof notes, reproduction, manuscript and claim boundary |
| Interpretation | `morrocwi/readout_genesis` | records the readout interpretation only; does not own the NS mathematics |

### Toledo proposal family

The live EPSC proposal family currently runs through `PROP-EPSC-16`:

- `PROP-EPSC-01` — nested readout consistency defect `delta_K`;
- `PROP-EPSC-02` — NS Fourier boundary-energy diagnostic;
- `PROP-EPSC-03` — fail-closed epsilon-completion gate;
- `PROP-EPSC-04` — target-indexed omitted-information certificate target;
- `PROP-EPSC-05` — terminal finite-Fourier non-identifiability obstruction;
- `PROP-EPSC-06` — spectral `H^s -> L2` tail inequality;
- `PROP-EPSC-07` — Leray-Hopf spacetime Fourier-tail certificate;
- `PROP-EPSC-08` — Lipschitz readout lift;
- `PROP-EPSC-09` — conditional terminal `H^s` certificate;
- `PROP-EPSC-10` — terminal Leray-Hopf energy-budget certificate;
- `PROP-EPSC-11` — energy-defect floor / energy-equality closure;
- `PROP-EPSC-12` — Galerkin-to-continuum retained-record adapter obligation;
- `PROP-EPSC-13` — residual-based Leray relative-energy adapter;
- `PROP-EPSC-14` — finite Fourier residual tape;
- `PROP-EPSC-15` — exact-dyadic piecewise-linear continuous-time enclosure of a recorded RK4 tape;
- `PROP-EPSC-16` — **OPEN** scalable/tight high-cutoff certified enclosure.

These are Toledo **proposal identifiers**, not canonical verified theorem codes.

### What the application established

The original EPSC question

\[
\|(I-P_K)x\|\le\beta_K
\]

is too coarse unless the target norm/readout and admissible assumptions are declared. For unrestricted terminal Fourier data, retained low modes alone do not identify the omitted tail. For an unforced Leray-Hopf trajectory on the periodic three-torus, however,

\[
\|(I-P_K)u\|_{L^2(0,T;L^2_x)}
\le
\frac{\|u_0\|_2}{\sqrt{2\nu}(K+1)},
\]

so a genuine computable omitted-information certificate exists in that spacetime norm and tends to zero. Lipschitz readouts inherit the corresponding bound.

A richer terminal retained record can also certify a terminal tail. If `U_0` is a certified upper bound for `||u_0||_2`, `L_K(T)` a certified lower bound for `||P_Ku(T)||_2`, and `D_K(T)` a certified lower bound for `nu int ||grad P_Ku||_2^2 dt`, then

\[
\|(I-P_K)u(T)\|_2
\le
\left[U_0^2-L_K(T)^2-2D_K(T)\right]^{1/2}
\]

when the directional certificates are consistent. The asymptotic floor of this energy-budget certificate is the energy-inequality slack; under energy equality that floor is zero.

### Relative-energy bridge and exact tape enclosure

Let `v(t)` be a divergence-free finite Fourier comparison path, let

\[
r=\partial_t v+P[(v\cdot\nabla)v]-\nu\Delta v-Pf,
\]

and define

\[
A_T=2\int_0^T\|\nabla v\|_\infty dt,
\qquad
B_T=\int_0^T\|r\|_{H^{-1}}^2dt.
\]

The NS application records the standard relative-energy/Gronwall estimate in EPSC form:

\[
\sup_{0\le t\le T}\|u(t)-v(t)\|_2^2
\le
e^{A_T}\left(e_0^2+\frac{B_T}{\nu}\right).
\]

If `v(T)` is supported in the retained cutoff, the same right-hand side bounds the terminal omitted tail of the actual Leray-Hopf solution.

`PROP-EPSC-15` supplies the previously missing numerical construction for a recorded finite RK4 tape. Each stored binary64 component is interpreted as its **exact dyadic rational**, each node is Leray-projected exactly, and consecutive nodes are joined by a continuous piecewise-linear finite Fourier path `v_h`. Because the Fourier coefficients are affine on each time cell, the quadratic Navier-Stokes residual is a degree-at-most-two polynomial in normalized cell time. Consequently its homogeneous `H^{-1}` norm squared is degree at most four and can be integrated exactly with rational arithmetic. A coefficientwise Fourier `l1` majorant gives a rigorous upper bound for the gradient integral, and the exponential is enclosed from above by an exact rational Taylor/geometric-remainder bound.

The finite path therefore supplies

\[
A_T\le\overline A_T,
\qquad
B_T\le\overline B_T
\]

without identifying the RK4 recurrence with the exact PDE flow. The path's PDE defect is explicitly paid for in `B_bar`.

### Genesis interpretation

This application sharpens a readout discipline without turning it into ontology:

> completeness is completeness **for a declared reader/norm, under declared assumptions, from a sufficient retained record plus a proved/certified adapter**.

The implemented chain is now

\[
\text{stored finite RK4 tape}
\xrightarrow{\text{exact dyadic capture + piecewise-linear path}}
(\overline A_T,\overline B_T)
\xrightarrow{\text{relative energy (Dr)}}
\beta_K^{RE}
\xrightarrow{\text{reader/gate}}
\varepsilon\text{-certificate}.
\]

This is a closure for the **declared finite comparison-path problem**, not a claim that every finite truncation is accurate or that continuum dynamics are ontologically discrete.

### What must NOT be imported into the Genesis root

The following remain application-local: Taylor-Green cutoff values and numerical thresholds; claims that K=5 (or any tested cutoff) is automatically continuum-complete; claims that a raw Galerkin trajectory equals the continuum projection; claims that continuum ontology has been disproved; claims that the Clay Navier-Stokes problem has been solved; claims of turbulent DNS adequacy from a short finite run; or claims that the present conservative certificate will remain tight at arbitrarily large `K` and `T`.

### Current frontier

The logical enclosure gap formerly labelled `PROP-EPSC-15` now has a concrete finite construction. The next application-local frontier is `PROP-EPSC-16`: make certified `A_bar/B_bar` evaluation scalable and sufficiently tight at larger Fourier cutoffs and longer horizons. Genesis records this boundary but does not promote either the EPSC-15 construction or its future optimisations into root ontology.
