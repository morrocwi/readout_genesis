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

## 5.2b-1 — dynamical selection: "ไม่สมมาตร แต่สมดุล" (2026-08-09)

Founder's guiding directive, recorded verbatim: *"เผื่อใจไว้ด้วยว่า แท้จริงแล้วทั้งหมดอาจเป็น
สิ่งเดียวกันมาจากรากกลับสู่ราก ไม่สมมาตร แต่สมดุล."* Files:
`theta_dynamics_selection_v1.py` + `formal/InfoThetaFixedPointBalance_attempt.v`
(3 theorems, general coefficients, axiom-free).

- **B1 — forced balance law (`Th_coqc`):** at ANY J=0 static fixed point of the
  reader/record pair over a symmetric operator (mother potential `aΦ+bΦ³`, b≠0):
  **`⟨Φ³,Ψ⟩ = ΣᵢΦᵢ³Ψᵢ = 0` is FORCED.** "สมดุล" is not a symmetry of the configuration —
  it is a forced bilinear balance.
- **B2 — symmetry is dead (`Th_coqc`):** perfect agreement `Ψ=Φ` forces `Φ=0` (via
  `2aΦᵢ=0`, decoupled case justified by 5.2a's support rule), and perfect mirror `Ψ=−Φ`
  forces `Φ=0` (via `2bΦᵢ³=0`, ANY graph term — it cancels). Both the symmetric and the
  anti-symmetric configurations retain nothing. **A living fixed point (Ψ≠0) is
  necessarily NOT-symmetric yet balanced — the founder's phrase as a theorem pair.**
- **B3 — selection experiment (`finite_diagnostic`, floats disclosed, fixed seeds):**
  multistart Newton over all 8 supports (n=3, a=−1, b=1, K=μ=1, J=0 and ℛ_Φ=ℛ_Ψ=0 —
  closed case, declared): living fixed points found ONLY on the three path-shape
  supports (≥2 distinct orbits: a uniform-weight star, spectrum `{0,w,3w}` ratio 3.0
  — its non-support edge is an exact TIE s=0 with a residual leaf-swap profile
  symmetry, disclosed; and a non-uniform one, ratio ~3.33, strictly concordant off
  support — both with THREE DISTINCT levels, balance ≈0 at ~1e-15, Ψ∦Φ). K3: **0
  living fixed points in 3000 trials** incl. structured anti-aligned starts — a
  bounded negative, NOT a nonexistence proof (independent review additionally failed
  to refute it with 25,000 trials + homotopy continuation). Single-edge/empty: none
  living.
- **Reading (Dr):** within this bounded search the dynamics rejects both dead symmetric
  states and full disorder; what lives is a path configuration — the very topology whose
  spectrum separates (5.1) — closing the loop root → configuration → root.
- **Open, named:** exact algebraic certification of the living fixed points (symbolic
  solve timed out twice — recorded); K3 nonexistence proof; n>3; dynamic (non-static)
  selection; parameter-dependence beyond the declared `a=−1,b=1,K=μ=1`. CRRC guard
  binding: no generation identification.

## 5.2b-2 — the minimal living count: N ≥ 3, root-native (2026-08-09)

Files: `theta_minimal_living_v1.py` + `formal/InfoThetaMinimalLiving_attempt.v`
(6 theorems/lemmas, all axiom-free).

- **PROVEN (`Th_coqc`): n=2 admits NO living fixed point.** Empty-support branch: the
  record dies componentwise (`n2_empty_support_dead`). Edge-present branch (both
  retained differences nonzero): the four fixed-point equations are **contradictory**
  (`n2_edge_present_dead`) — complete case tree, endgame factor `(3D²−4)(D²−1)=0` with
  every root killing a living hypothesis; the reduction to sum/difference variables is
  itself machine-checked (4 ring identities); and the top-level assembly under the
  5.2a support rule is now ONE Coq theorem (`n2_no_living_fixed_point`, added per
  review — its case split uses the order comparison; M2's core stays order-free).
  Every M2 step is characteristic-0 field algebra — **valid over ℝ, not only ℚ**
  (formal `Coq.Reals` restatement open, noted); independent review confirmed
  nonexistence by Gröbner saturation — **even over ℂ**.
- **MEASURED (`finite_diagnostic`):** n=3 lives (paths only, per 5.2b-1); n=4 also
  lives, and more broadly — with structure (per review): the isolated-vertex class is
  the n=3 living path embedded in n=4 (the isolated slot is EXACTLY dead, its
  decoupled equations being M1's); the star, P4-path, and 4-cycle classes are
  genuinely 4-slot living. So existence alone does NOT single out 3.
- **VERDICT:** **a living reader/record/geometry loop needs ≥ 3 slots — a root-native
  lower bound**, with 3 as the MINIMAL living count. "Exactly 3" invokes the
  framework's own declared minimality-selection discipline (`Dr` — the same "minimum
  value that still supports a nontrivial retained closure" semantics the EQ-stream
  already uses), not existence alone.
- **Convergence, carefully stated (Q3 identity-by-role):** root-native minimal-living
  `N ≥ 3` (here) and CP-conditional `N ≥ 3` (Attempt 3, imported physics) are two
  INDEPENDENT arrows hitting the same value from different premises. Identifying their
  two N's is an unbuilt admissibility square — the CRRC guard holds; that square is now
  the single most valuable named open item of the program.

## 5.4 — the admissibility square between the two N≥3 arrows: HALF-CLOSED (2026-08-09)

Files: `theta_cp_square_v1.py` + `formal/InfoThetaCPSquareObstruction_attempt.v`
(1 theorem, axiom-free). Item-2 side: this is **Attempt 4** in the item-2 line.

- **Part 1 — legitimate intersection (exact within declared architecture):** both
  arrows constrain the dimension of the SAME declared family-slot space (the ℂ^N
  ansatz): Θ-graph vertices = slot indices (5.1–5.2b setup) and mixing-matrix indices
  = slot indices (Attempt 3 setup). Two different questions about one declared index
  set — combining necessary conditions is an intersection, not CRRC. **N ≥ 3 stands
  with two supports of UNEQUAL TIER** (per review): the root arrow is unconditional
  within the declared architecture; the CP arrow is conditional on the empirical
  retained-CP premise (fed in, not derived — and per Part 3 not yet root-realizable).
  Root-native + empirical-conditional, NOT two root-native proofs.
- **Part 2 — bridge candidate (declared, Dr):** mixing = eigenbasis mismatch of two
  living sector graphs' Laplacians. On two living path sectors (different centers):
  V = U_AᵀU_B is a genuine nontrivial rotation (|V₁₁| = ½ — reads 60° under the
  declared ascending-eigenvalue/sign convention, 120° under a sign flip; the
  convention-invariant content is |V₁₁| = ½ and non-permutation mixing) — **real
  mixing angles exist natively.**
- **Part 3 — proven obstruction (`real_quartet_no_cp_readout`, Th_coqc):** a REAL
  mixing matrix's Jarlskog quartet has Im ≡ 0 — the CP-signed readout reads NEUTRAL on
  every real configuration. The current real-weighted Θ architecture **cannot satisfy
  A_CP's premise**; the two N's cannot yet be identified as one derived quantity.
- **Named next step (root-available, not built):** oriented/skew edge structure — the
  corpus's own `𝔾^(−)` G-adjoint split (storage vs oriented transfer) and `ω` pairing
  are the precise candidates for making a retained `J ≠ 0` root-realizable. That is
  the program's next frontier.
