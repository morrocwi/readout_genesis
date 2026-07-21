<!-- The honest "close the Standard Model" ledger. Read this before claiming anything about
     the SM in this project. It is a CLOSURE LEDGER, not a derivation of the SM. -->

# Standard Model — Closure Ledger (v0.4, honest)

> **What "closed" means here.** We close what is provable and mark the wall precisely. This is
> **not** a derivation of the Standard Model from the retained root. The honest headline:
> **three layers close in FINITE BLIND FIXTURES, the radiative engine closes only to a FINITE
> SPECTRAL DIAGNOSTIC, and the physical Standard Model from the root is STILL OPEN** — with
> exactly **three** remaining bottlenecks (down from four).

Every row points at a runnable verifier (`… .py`, PASS) and/or a machine-checked Coq witness
(`… .v`, `Print Assumptions` **Closed over ℚ**). Run them all: `python3 run_tests.py`.

## The pipeline (what each stage does and its honest tier)

| stage | result | tier | witness |
|---|---|---|---|
| **SM-G0 substrate** (connection, holonomy, curvature) | `U=V_j⁻¹V_i`, SO(3) holonomy, curvature≠0 | 🟩 `Th_coqc` | `InfoConnectionFromFrame`, `InfoRationalSO3Curvature` |
| **SM-G0/G0.6 order defect** | commutator from ordered composition; Jacobi derived | 🟩 `Th_coqc` | `InfoOrderDefectFromComposition.v` (borrow #2 *reduced*, not removed) |
| **Algebra discovery** (blind) | center=1, ideals 8⊕3 → `u(1)⊕su(3)⊕su(2)`; neg-control `1⊕3⊕3`→FAIL | 🟦 finite blind PASS | `sm_discovery_pipeline_v0_4.py` §1 |
| **Chirality** | orientation op → `η_χ=1` chiral vs `0` vectorlike | 🟡 conditional PASS | pipeline §2 (needs a `J_ord`; root→`J_ord` OPEN) |
| **Representation discovery** | 5 blocks `(3,2)+(1,2)+(3,1)×2+(1,1)` from Casimirs | 🟦 finite blind PASS | pipeline §3–4 |
| **Hypercharge** (derived) | `q=1/6,ℓ=−1/2,u=2/3,d=−1/3,e=−1` forced by anomaly+coupling | 🟩 `Th_coqc` | `InfoHyperchargeAnomalyClosure.v`; pipeline §5–6 |
| **Cubic anomaly** | `6q³−3u³−3d³+2ℓ³−e³ = 0` exact | 🟩 `Th_coqc` | `InfoHyperchargeAnomalyClosure.v` |
| **Electroweak masses** | rank-1 obstruction ⇒ photon massless (emergent) + massive `W/Z` | 🟩 `Th_coqc` + calib | `InfoElectroweakNullDirection.v`, `electroweak_decoder_v0_3.py` |
| **Radiative engine** | finite log-det curvatures `(r1,r2,r3)=(−153/20,−243/20,−216/5)` | 🟡 finite **diagnostic** | pipeline §7–8 (**NOT** physical β-functions) |
| **Color number = 3 / SU(3) / Z₃** | ordered closed tape ⇒ `(−1)^{k−1}=1` ⇒ k **odd** ⇒ k=3 ⇒ SU(3) + Z₃ center + dim 8 | 🟦 conditional `Th_coqc` | `ordered_tape_closure_v0_2.py`, `InfoOrderedTapeClosure.v` (oddness **derived**, not posited; not "3 colors" input) |
| **Center-sector confinement** | `⟨W(C)⟩=q(κ)^{A(C)}` ⇒ area law `σ=−log q>0` ⇒ `V(R)=σR` | 🟦 exact, **Z₃/2D only** | `center_confinement_v0_3.py`, `InfoCenterConfinement.v` (root curvature action, no QCD potential; controls κ→∞⇒σ→0) |
| **Physical SM end-to-end** | — | 🟥 **OPEN** | — |

## What is genuinely closed (do not undersell)
- The **gauge substrate** (connection/holonomy/curvature) and the **order defect** are `Th_coqc`.
- Given the SM one-generation **rep content as a finite fixture**, the **hypercharges are forced**
  by anomaly + coupling closure, the **cubic anomaly cancels exactly**, and these are the real SM
  values — all machine-checked over ℚ, with **no charge fed in**.
- The **photon's masslessness emerges** from a rank-1 obstruction (not imported), and the
  electroweak decoder calibrates to CODATA/PDG with a held-out tree-level `M_Z` at 0.011%.
- The discriminators are **blind**: the group, the reps, the charges, and L/R are never inputs;
  every stage carries a **failing/negative control**.
- **The color number 3 and SU(3) are conditionally derived** from the ordered closed tape — the
  *oddness* of the minimal closure is a theorem (`(−1)^{k−1}=1`), not "nature has three colors" — and
  a **first dynamical-confinement result** (area law `V(R)=σR`) is exact in the Z₃/2D center sector.

## The wall — what must NOT be claimed (three bottlenecks, honestly)
End-to-end **physical Standard Model from the root = 0%**. The remaining bottlenecks are **three**:
1. **Root-derived orientation / spin-statistics** — the pipeline uses a *given* `J_ord`; deriving a
   physical chirality operator from the retained root is open (so chirality is *conditional*).
2. **Gauge-orbit fluctuation Hessian** — the radiative `(r1,r2,r3)` are raw finite log-det
   curvatures; without the exact orbit-volume (ghost) subtraction, polarization counting, and a
   single-action gauge-carrier Hessian they are **not** one-loop SM β-coefficients.
3. **Continuum / held-out radiative validation** — no large-graph limit, no regulator-independence,
   no held-out coupling-flow comparison has been run.

Also not derived from the root (finite BLIND fixtures supply them): the **rep content itself**, the
**count** (why exactly `u(1)×su(2)×su(3)`), and any **physical coupling value**. `α`, masses, and
`θ_W` remain **rejected-not-faked / calibration inputs**.

**On color/confinement specifically** (v0.2/v0.3): SU(3) and its Z₃ center are *conditionally* derived,
and confinement is closed **only** in the Z₃ center sector on a **2D** graph. Still open there: the full
**SU(3)** (all 8 directions, not just the center), **3+1D** coupled plaquettes, a nonzero **continuum**
`σ_phys` under a root-derived scale flow, and — the sharpened wall — proving the **full SU(3) action
flows into the center-confined sector** without projecting Z₃ by hand. (The Wilson-loop area-law
criterion and the center's role are standard lattice-gauge results, not new here.)

## One-line verdict
> **Algebra + representations + hypercharges + anomaly cancellation: FINITE BLIND / Th_coqc closed.
> Chirality: conditional. Radiative engine: finite diagnostic. Physical Standard Model from the
> root: OPEN — three bottlenecks.** Saying exactly this is the closure.
