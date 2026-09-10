# Readout Genesis — External Application Map

This file maps **applications of the Readout/retention programme** without promoting their domain-specific numerical results into the Genesis root canon.

Rule: an external application may cite Genesis concepts, but its mathematical/empirical claims remain owned by the repository where they are proved or tested. Application evidence does not flow backward into `READOUT_GENESIS_CORE.md` automatically.

## Navier–Stokes / Discrete Epsilon-Completion

Status: **external finite-diagnostic research application; not a registered Genesis domain and not a root theorem**.

### Ownership map

| Layer | Repository | Role |
|---|---|---|
| General discrete mathematics | `morrocwi/information-discrete-math` | finite refinement, nested consistency diagnostics, fail-closed certification interface |
| Equation/proposal provenance | `morrocwi/toledo` | proposal IDs, lineage, tier/status, later canonical registration if reviewed |
| Navier–Stokes application | `morrocwi/readout-problem-navier-stokes` | NS-specific Fourier-Galerkin experiment, reproduction, frozen results, claim boundary |
| Interpretation | `morrocwi/readout_genesis` | explains how the application relates to retained/readout language; does not own the NS result |

### Current registered proposal family

Toledo proposal file: `registry/proposals/discrete_epsilon_completion.json`.

- `PROP-EPSC-01`: Nested Readout Consistency Defect
  \[
  \delta_K=\|R_Kx_{K+1}-x_K\|.
  \]
- `PROP-EPSC-02`: Navier-Stokes Fourier boundary-energy diagnostic
  \[
  E_{\partial K}=\frac12\sum_{\|k\|_\infty=K}|\widehat u_k|^2.
  \]
- `PROP-EPSC-03`: fail-closed epsilon-completion acceptance protocol.
- `PROP-EPSC-04`: **Open** computable omitted-information/tail certificate target.

These are proposal identifiers, not verified canonical Toledo theorem codes.

### Genesis interpretation

The application is consistent with the programme's distinction between a retained record and the richer target from which it is read. In computational terms, the finite solver works with declared finite records; an additional theorem is required before those records may be called complete for an infinite target.

The epistemic discipline is therefore:

\[
\text{finite diagnostic PASS}
\not\Rightarrow
\text{infinite/continuum certificate}.
\]

The general epsilon-completion gate makes that discipline executable: if no proved omitted-information bound `beta_K` exists, the infinite-object verdict remains `HOLD`.

### What must NOT be imported into the Genesis root

The following are application-local and must not be written into the root canon as universal facts:

- the recorded Taylor-Green values at K=1..5;
- the specific `1e-6` and `1e-8` diagnostic thresholds;
- the statement that K=5 is continuum-complete;
- claims that continuum ontology has been disproved;
- claims that the Clay Navier-Stokes problem has been solved;
- claims of physical/DNS turbulence adequacy from the short finite run.

If a later `PROP-EPSC-04` theorem is proved with clearly declared hypotheses, Genesis may cite that theorem at its actual tier. It still should not replace the theorem's source repository as the mathematical source of truth.
