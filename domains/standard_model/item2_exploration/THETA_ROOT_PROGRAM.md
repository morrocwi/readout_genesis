<!-- Program note, tier Dr except where tagged. Houses the founder ruling elevating Theta
     to a new root, the Theta-direction census (Th_coqc, n=3), and the Theta-law
     reconciliation. Housed in item2_exploration because item 2 motivated it; the content
     is ROOT-level, not SM-specific. -->

# Θ ROOT PROGRAM — founder ruling, direction census, law reconciliation (2026-08-08)

## 0. The founder ruling (recorded verbatim, 2026-08-08)

> "ไปอ่าน readout universe เพื่อเชื่อมตัวอ่าน บันทึก ความแตกต่าง และธีต้าซึ่งเป็นรากใหม่"

**Θ (the living-geometry state) is elevated to a NEW ROOT** alongside the reader `Φ`, the
record `Ψ`, and the retained difference `δ_R`. Basis in the existing corpus (2026-08-08
survey of `readout_universe` + `READOUT_GENESIS_CORE.md`, full citations in the session
log): Θ was already structurally peer-level — a slot in `Z_n` with role "โครงสร้างการแปล"
(the translation structure), its own action sector (`S_UF = S_DRL + S_Θ + …`), its own
stationarity law (Gate D, `FINITE_INTERNAL_CLOSURE`, exact fixture `Θ_{n+1}=3/8`, failing
control proving `Ψ` load-bearing), sourced bilinearly by reader×record
(`S_Θ^a = Φᵀ𝔾_aΨ`). No prior text called it a root; this ruling does. Mirrored as a row in
the central `DECISIONS.yaml` (`DEC-theta-new-root-2026-0808`).

**The connection the ruling names, in one line:**
`δ_R` (primitive) → forces `L_R = D_W − W` (Th_coqc) → `𝔾[Θ]` (operator read from Θ) →
governs `Φ`/`Ψ` (reader/record pair) → which write Θ back (`S_Θ^a = Φᵀ𝔾_aΨ`) — a closed
loop: geometry that is itself a retained readout of the reading process.

## 1. The Θ-direction census (GAP 1 closed for n=3; the index `a` now has an answer)

The affine law `𝔾[Θ] = 𝔾_0 + Σ_a Θ^a 𝔾_a` (`READOUT_GENESIS_CORE.md:1280`) never declared
what `a` ranges over — confirmed open by the 2026-08-08 survey (only a 1-component fixture
exists anywhere). Closed from the root's own forced characterization (the three properties
that force `L_R = D_W − W`: symmetric, zero-row-sum, off-diagonal ≤ 0 — reused as the
DEFINITION of admissibility, not re-proven):

> **Census theorem (`Th_coqc`, n=3: `formal/InfoThetaEdgeCensus_attempt.v`, all
> `Print Assumptions` Closed; exact sweep n=3,4: `theta_direction_census_v1.py`):**
> every admissible operator decomposes UNIQUELY as `Σ_e w_e L_e`, `w_e ≥ 0`, over the
> single-edge Laplacians, and the `L_e` are linearly independent — the admissible
> deformation directions are EXACTLY one per edge (`C(n,2)` at `n` vertices).

**Reading (Dr):** the natural realization is `𝔾_0 = 0`, `a = edges`, `𝔾_a = L_e`,
`Θ^e = W_ij` — Θ IS the retained edge-weight record; "living geometry" and "weighted
graph" are one object; `S_Θ^e = ΦᵀL_eΨ` is the reader×record difference read per edge.
**Θ's direction structure is discrete/countable BY CONSTRUCTION** — a finite edge set.
**Protection scope, stated precisely (per independent review):** the INDEX-CONTINUUM half
of the retracted EQ-069..071 mistake — an undeclared or continuous family of deformation
directions — is excluded at the index level (finite edge census). The KNOB half — sweeping
one weight as a free tunable parameter and reading a smooth bijection of it as an
observable — is NOT excluded by the census: each `Θ^e` remains a freely settable rational
value, and the standing discrete-only constraint (§3 below; `CONTINUUM_ARC_ERROR_NOTE.md`
lessons 1 and 5) must still be enforced separately.

**CRRC guard (binding):** nothing above identifies edges with fermion generations, sectors,
or any physics quantity. That identification would be a NEW admissibility square with its
own RDI count — not built here, not implied.

## 2. The Θ-law reconciliation (GAP 2 closed)

The corpus carried two Θ laws with no reconciliation statement:
- **(A)** `Θ_{n+1} = A_Θ Θ_n + B_ΘΦ Φ_n + B_ΘΨ Ψ_n + u_Θ` `[Dr]`
  (`READOUT_GENESIS_CORE.md:1278`; `A_Θ/B_ΘΦ/B_ΘΨ` never defined anywhere), and
- **(B)** `M_Θ δ_t²Θ + ∇U_Θ + K·Φᵀ(∂𝔾/∂Θ)Ψ = 0` (Gate D, `FINITE_INTERNAL_CLOSURE`).

**Resolved (exact algebra, `theta_direction_census_v1.py` §2):** (B) with quadratic `U_Θ`
IS affine — but on the doubled state `(Θ_n, Θ_{n−1})` and with a source BILINEAR in
`(Φ,Ψ)`; and no constant `B_ΘΦ/B_ΘΨ` can represent that bilinear source (exact scaling
contradiction: `(Φ,Ψ)→(2Φ,2Ψ)` scales the true source ×4, any linear form ×2). Premise of
the impossibility, explicit per review: `u_Θ,n` is read as an exogenous, field-independent
drive — the standard affine-recurrence reading matching the corpus's constant-matrix
notation; allowing `u_Θ,n` to depend on `(Φ,Ψ)` would make the impossibility vacuous by
absorption and the B-slots meaningless. Gate D's exact fixture (`Θ_{n+1}=3/8`) is
reproduced exactly by the doubled-state affine form.

**RECORDED DECISION (Dr, this program's working rule):** law (B) — the variational Gate-D
law — is CANONICAL (it has the action, the fixture, and the failing control). Law (A) is
its frozen-field linearization; `A_Θ/B_ΘΦ/B_ΘΨ` are derived objects of that linearization,
never free root-level dials.

## 3. Standing constraints inherited by every future step of this program

1. **Discrete-only** (`CONTINUUM_ARC_ERROR_NOTE.md`, `DISCRETE_MASS_ITEM1_PLAN.md`): read
   spectra of `L_R`/`𝕋_phys` directly, once, per sector; never a timestep-accumulated
   product; never a continuous knob; a smooth bijection of a free parameter is a
   coordinate, not an observable; refused endpoints are correct, not walls.
2. **Per-sector-distinct spectra required** (error note lesson 3): real cross-branch
   log-shapes differ (up 1.77 / down 2.27 / lepton 1.53 — down accelerates, up/lepton
   decelerate); a single shared graph with only a per-sector scale is empirically refuted.
3. **The CP gate** (item 2 Attempt 3, `InfoCPEquivariantGenerationBound_attempt.v`): any
   family structure this program produces must retain a CP-odd signed readout — a
   machine-checked conditional `N ≥ 3` consistency gate from an independent direction.
4. **Q3 identity-by-role**: `k_color`, `n_gen`, edge counts, spectrum-level counts stay
   distinct symbols until a role-equivalence square is built and checked.

## 4. On the qubit question (founder asked 2026-08-08; assessment, tier Dr)

The qubit is NOT the root and should not be made one. The framework's primitive is `δ_R`
(one retained distinction → 1 rbit under a lossless readout bridge — URR spec); a qubit's
continuum amplitude pair (Bloch sphere, ℂP¹) is I1-contaminated as ontology — precisely
the kind of object this framework treats as a non-readout. What IS usable, and was already
used in item 2 Attempt 3: the **exact ℚ(i) skeleton of qubit algebra** — unitary matrices
over Gaussian rationals, Born-rule overlap FRACTIONS (rational) instead of amplitudes/
angles — i.e. the readable, discrete part of quantum structure, honestly tiered. Quantum
mechanics remains a FACE/domain of the master equation (Born/unitarity is this domain's
imported prerequisite, backlog item 33), not a second root. If a future result needs
qubit machinery, translate it through the Lens Law into `δ_R`/overlap-fraction vocabulary
first; do not import the continuum state space as primitive.

## 5. Named next steps (5.1 DONE 2026-08-09; founder picks the next)

1. **Sector census over the gauge quotient — DONE (2026-08-09,
   `theta_sector_census_v1.py` + `formal/InfoThetaSectorSpectrum_attempt.v`, 9 theorems
   axiom-free).** Findings: (a) the gauge quotient cuts NO family-graph Θ-directions (𝒜
   acts as identity on the family slot — inherits Attempt 1's imported-ansatz caveat); the
   cutting group is the family graph's OWN symmetry, and the surviving-parameter count =
   **edge-orbit count** (invariance provably forces per-orbit uniform weights). (b) RDI
   count for the two 3-vertex candidates: K3/S3 and P3/Z2 each retain exactly ONE invariant
   direction — same parameter budget — yet **K3's invariant spectrum {0,3w,3w} is
   degenerate for every w (re-derives item1 Attempt 10 at the census level) while P3's
   {0,w,3w} has three distinct levels for every w>0: distinguishing power lives in
   TOPOLOGY, not parameters or symmetry-breaking**. Grounds the `DISCRETE_MASS_ITEM1_PLAN`
   reduction lever (P3→{0,1,3}) structurally. Four gates recorded for any future family
   candidate (≥3 distinct levels; per-sector-distinct shapes incl. both hierarchy shapes;
   the CP N≥3 gate; root-forcing of topology = step 5.2). CRRC guard binding: no
   level↔generation identification made.
2. **Topology-forced spectra — 5.2a DONE (2026-08-09, `theta_topology_readout_v1.py` +
   `formal/InfoThetaTopologyReadout_attempt.v`, 8 theorems axiom-free).** Root-native
   reframing established: **topology is a READOUT, not an input.** (R1) the per-edge
   Gate-D source is exactly the product of retained differences,
   `S_Θ^e = ΦᵀL_eΨ = (Φ_i−Φ_j)(Ψ_i−Ψ_j)`; (R2) at Gate-D stationarity on the census cone
   (quadratic edge cost, division-free doubled form, stationary point characterized by
   `μw* = −Ks`), an edge EXISTS iff its reader/record differences are ANTI-ALIGNED
   (discordant) — the family graph's support IS the reader↔record discordance pattern;
   (R3) honest negative: ALL 8 labeled 3-vertex supports are realizable (exhaustive over
   36 injective rank-pairs; complement closure Ψ→−Ψ proven generally), so kinematics does
   NOT restrict topology — **the selection must come from the DYNAMICS = step 5.2b
   (open):** which (Φ,Ψ) configuration the coupled Φ/Ψ/Θ system settles into. (R4,
   CORRECTED per review — the earlier "partial disorder ⟺ 3 distinct levels" reading was
   REFUTED and is WITHDRAWN: 5.1's spectra assume uniform weights while R2's stationary
   weights are the discordance values themselves, provably never uniform on an
   all-discordant K3 (a²+ab+b²=0 has no nonzero rational solution). Under R2 weights the
   K3 total-disorder witness gives {0,3,9}·(K/μ) — three distinct levels from TOTAL
   disorder — and every positive-weight P3-support separates too; what survives is that
   5.1's degenerate uniform-K3 spectrum is UNREACHABLE as an R2 readout — the mechanism
   generically avoids degeneracy. Tier Dr.) Scope: static/fixed-point case at frozen
   (Φ,Ψ) only; non-strict minimality machine-checked, uniqueness by strict convexity by
   inspection; quadratic cost declared, cost-independence open (needs coercivity). CRRC
   guard binding throughout.
3. **Census beyond n=4 / general-n Coq:** generalize `InfoThetaEdgeCensus_attempt.v` from
   the 3-vertex case to general n (the sweep here covers n=4 exactly; the general theorem
   is routine but unwritten).
