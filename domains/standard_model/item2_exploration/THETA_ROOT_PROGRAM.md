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

## 5.5 — support-tied real oriented skew extension: `J_Theta ≠ 0` FOUND ROOT-NATIVE at a living C4 fixed point (2026-08-09)

Files: `theta_oriented_skew_v1.py` + `formal/InfoThetaOrientedSkewObstruction_attempt.v`
(7 lemmas/theorems, all axiom-free, `Print Assumptions` confirmed independently by two
reviewers). Item-2 side: this is **Attempt 5** in the item-2 line — 5.4's named next
frontier, taken up.

**Provenance (multi-agent design + build, disclosed):** a 3-route design workflow
proposed real-skew (Route B), Q(i)/mu_4 (Route A), and a Route-C hybrid; adversarial
judging FOUND a real support-untied bug in Route B (its `a_e` was computed on every
ordered pair in `V×V` regardless of whether the edge was in the census-selected
support `E`, silently re-opening the "one admissible direction per edge" closure
5.1/5.2a already proved shut) and the synthesis pass REPAIRED it by tying `A`'s
support identically to `L`'s support (`a_e≡0` off `E` by declaration). **Orchestrator ruling
(binding, Step 0):** PRIMARY = the repaired support-tied real construction only;
FALLBACK Q(i)/`μ₄` branch NOT built (no `theta_oriented_gaussian_*.py` exists); the
untied enlarged-census reframing is deferred, named as a **5.6 candidate**, not
pursued here. Implementation passed two independent adversarial reviews (verdicts
RELEASABLE and RELEASABLE-AFTER-FIXES) plus one repair pass (the repair fixed a
print-precision overclaim at its root cause — see below — not a mathematical error).

**Construction:** for the SAME edge set `E` the census/Gate-D machinery already
selects (5.1/5.2a), add a real antisymmetric skew term tied to that support:
`𝔾[Θ] := L[w] + A[a]`, `A[a] := Σ_{e∈E} a_e A_e`, `A_e := e_ie_j^T − e_je_i^T` for
`e=(i,j)∈E` ONLY, `a_e ≡ 0` off support by construction (not a separate
optimization). This concretely instantiates the corpus's own `𝔾^(+)+𝔾^(-)` split
(closing V.13a's flagged "[Open] concrete instantiation") with `𝔾^(+):=L`,
`𝔾^(-):=A`. The extended living reader/record system (same declared regime
`a=−1,b=1,K=μ=1,J=0`): `K(L[w]+A[a])Φ + aΦ + bΦ³ = 0`, `K(L[w]−A[a])Ψ +
(a+3bΦ²)·Ψ = 0` — the record couples to `𝔾[Θ]^T = L−A` (literal transpose,
verified against `READOUT_GENESIS_CORE.md:1332-1337`, not a dagger — no
complexification needed). `J_Theta(C)` := the ordered cyclic product of `a_e*`
around an independent cycle `C` lying entirely within `E` (only possible when `L`'s
own support is non-tree).

**Th_coqc (`InfoThetaOrientedSkewObstruction_attempt.v`, 7 lemmas/theorems,
axiom-free):** `qsign_exists` (shared Z2 sign-witness helper);
`cyclic_product_switching_invariant_triangle`/`_C4` (Z2 vertex switching
`a_e→ε_iε_ja_e` leaves the ordered cyclic product of `a_e` around K3/C4 EXACTLY
invariant, telescoping — the two concrete cycles the program's living-FP inventory
can reach); `tree_gauge_fixable_P3`/`_star3`/`_P4`/`_star4` (the Z2 switching group
gauges every `a_e≥0` on the four concrete tree supports 5.2b-1's search actually
visits). Scope stated honestly: these are concrete-instance transliterations, not
the general theorems — the general finite-n-cycle statement and the general
structural-induction tree lemma are both declared `[Open]` in-file (concrete-and-
closed over general-and-stuck, per playbook risk ranking).

**finite_diagnostic (floats disclosed, fixed seeds 550/551/552, reviewer-verified
robust across 3 independent seed triples), the decisive re-check under the
EXTENDED `(L+A)`-coupled dynamics:**
- **K3 (n=3, 5.4's re-verification target): 0/3000 living hits.** A strengthened
  bounded negative — the OLD symmetric-only dynamics already found 0/3000
  (5.2b-1) plus 0/25000+homotopy (independent review), but those were never
  re-checked under the genuinely different `(L+A)`-coupled system until now; K3
  stays dead under the extension too. Bounded-search negative, not a nonexistence
  proof.
- **C4 (n=4): 101/3000 living hits, 33 distinct FPs, `J_Theta ≠ 0` — the FIRST
  root-native nonzero orientation-odd invariant found at a living fixed point
  anywhere in this program.** The full magnitude spread MUST be disclosed, not
  just the largest values: `J_Theta ∈` `{2.583e-14 (×8 FPs), 1.036e-05 (×6),
  2.170e-05 (×7), 1.089e-03 (×8), 4.544e-03 (×4)}` (33 total), i.e.
  **min|J_Theta|=2.583e-14,
  max|J_Theta|=4.544e-03** — nearly 9 orders of magnitude of internal spread on
  the identical support/parameter regime. The near-zero cluster (8/33 FPs,
  ≈2.6e-14) sits within ~3 orders of magnitude of this support's worst Newton
  residual (8.7e-14) — genuinely close to the noise floor by eye — but was
  independently confirmed by a reviewer's 60-digit mpmath re-solve (residual
  ~3e-62, `a_e` stable to 60+ digits) plus a Jacobian condition-number check
  (8.3, well-conditioned, not a degenerate manifold) to be a real, isolated,
  reproducible nonzero fixed point, not floating-point noise. Its rigorous
  exact-arithmetic distinction from a hypothetical exact-zero branch remains
  `[Open]` — the mpmath/condition-number check is a strong post hoc finite_diagnostic
  indicator, not a Coq-level or exact-arithmetic proof.
- **P3 control (n=3, {(0,1),(0,2)}, tree): 577/3000 living hits, 26 distinct FPs,
  `J_Theta` UNDEFINED (no cycle in the support) — exactly as the tree-triviality
  lemma predicts.**
- **Odd/even traversal-sign note:** `J_Theta`'s SIGN (not its nonzero-ness) flips
  under reversed cycle traversal for the ODD cycle K3 (`m=3`) but is invariant
  under reversal for the EVEN cycle C4 (`m=4`) — the general `(−1)^m` telescoping
  fact, exactly what the orchestrator ruling's own phrase "orientation-odd cyclic
  product" already names; nonzero-ness itself is traversal-invariant either way.

**B1/B2 transfer to the extended `(L+A)`-coupled system (orchestrator ruling 3c's
mandatory sub-task — exact Fraction checks + paper derivation, tier `Dr` as
general claims, numerically re-confirmed at all 59 living FPs found, worst
`|⟨Φ³,Ψ⟩|=5.42e-14`):**
- **B1 (`⟨Φ³,Ψ⟩=0`) transfers UNCONDITIONALLY**, for a MORE GENERAL reason than
  5.2b-1 needed: the scalar-transpose identity `Ψ^T G Φ = Φ^T G^T Ψ` holds for ANY
  matrix `G` (not only symmetric ones — nothing but "a 1×1 matrix equals its own
  transpose"), so the combo identity `⟨Ψ,Reader⟩−⟨Φ,Record⟩ = −2b⟨Φ³,Ψ⟩` holds
  exactly REGARDLESS of `A[a]`.
- **B2 (symmetry is dead) ALSO transfers, but via a genuinely NEW mechanism —
  disclose that the old "graph term cancels" argument does NOT survive
  verbatim:** the skew source `S^{e,skew}=Φ_iΨ_j−Φ_jΨ_i` vanishes identically at
  `Ψ=cΦ` for ANY scalar `c`, forcing Gate-D-stationary `A[a]=0` exactly there —
  collapsing `𝔾[Θ]` back to plain symmetric `L[w]`, at which point the OLD
  (pre-5.5) B2 proof applies verbatim. The old proof relied on `G=G^T` identically
  (`G−G^T=2A≠0` in general under the extension), so it genuinely does not survive
  as stated — B2's conclusion transfers, its old mechanism does not.

**The verdict, carefully fenced:** 5.4's missing ingredient IS root-realizable — a
living oriented fixed point CAN retain a nonzero orientation-odd real cyclic
invariant (**YES at n=4/C4; n=3 stays NO within this bounded search, K3 dead**).
**Item 2 REMAINS `[Open]`**: the identification square between this real
`J_Theta` and 5.4's complex `Cq` quartet-`J` (`real_quartet_no_cp_readout`'s own
obstruction: a real mixing matrix's quartet has `Im≡0`) is UNBUILT and is now
**the named next gate** — Q3 identity-by-role holds (`w_e`, `a_e`, `k_color`,
`n_gen`, edge/level counts stay distinct symbols), CRRC guard binding throughout
(no generation/CKM identification made anywhere in either file, grepped clean).

**Named open items:** the quartetJ identification square (the single most
valuable named open item now, per 5.2b-2's precedent framing); the 5.6
untied-reframing candidate (deferred by orchestrator ruling, not pursued); exact
algebraic/minimal-polynomial certification of the C4 living FPs (currently
residual-certified only, ~1e-14 to 1e-16, symbolic solve not attempted); the
near-zero-cluster's rigorous exact-arithmetic distinction from a possible
exact-zero branch; general finite-n-cycle and general structural-induction tree
Coq lemmas (both declared `[Open]` in-file); full continuous diagonal-rescaling
gauge invariance (only Z2 sign-flip verified, per Route B's own unresolved
risk #2); stability of the C4 living FPs (only static existence checked, not
stability); the `V=U_A^†U_B` eigenbasis bridge stays FORBIDDEN as a `J` readout
(gauge-artifact trap, two independent design routes converged on this
independently — never used in either new file).

## 5.7 — the quartet-square identification: OBSTRUCTED for every embedding examined (2026-08-09)

(§5.6 stays RESERVED, per 5.5's own text, for the deferred untied enlarged-census
reframing candidate — not pursued here; this is a different, later number.)

Files: `theta_quartet_square_v1.py` + `formal/InfoThetaQuartetSquareObstruction_attempt.v`
(14 theorems, axiom-free, `Print Assumptions` confirmed independently by two reviewers
plus a post-repair fresh recompile). Item-2 side: this is **Attempt 6** in the item-2
line — 5.5's own named next gate, taken up: the identification square between 5.5's
real `J_Theta` and 5.4's complex `Cq` quartet-`J` (`real_quartet_no_cp_readout`'s
obstruction).

**Provenance (multi-agent design + build, disclosed):** a 3-route design workflow
produced a combinatorial/holonomy bridge (Route R2 — Family A/B/C `Cq` embeddings, no
eigenproblem), a spectral bridge (Route R1 — the eigenbasis-mismatch object), and a
role-axiom square (Route R3 — bipartite/parity connective observations). Three
independent adversarial judge lenses (gauge/convention-invariance; discrete-floor+CRRC;
provability/decisiveness), each doing its own from-scratch symbolic/numeric
re-derivation, converged on the same ranking (R2 > R1 > R3) and the same top-line
verdict (OBSTRUCTED for all three routes' natural constructions). One judge lens
independently caught a genuine mechanism error in R1's own gauge-bridge refutation — it
had tested the wrong bilinear (see the corrected mechanism below) — and the repair is
disclosed as this program's house-style caught-and-fixed correction, matching the
5.2a/5.4 precedent of naming a caught mistake rather than silently overwriting it. The
orchestrator ruled: PRIMARY = Route R2 (holonomy/Family A/B/C), with R1's corrected
diagnostic content and R3's parity/rescaling content grafted in as supporting material,
not filed as three separate near-duplicate artifacts; the triple-convergent rescaling
lemma is filed ONCE. Implementation passed two independent adversarial reviews
(verdicts RELEASABLE-AFTER-FIXES and RELEASABLE) plus one repair pass — both findings
applied were documentation-level MINORs (a cross-file C4 edge-quartet pairing-convention
disclosure and an eigen-ordering-convention-redundancy disclosure), no theorem or
numeric result was changed.

**Construction:** on the SAME `𝔾[Θ]=L[w]+A[a]` architecture 5.5 builds, three
combinatorial embeddings into `Cq := Q×Q` (Gaussian rationals) are tested against
`quartetJ(V) := Im(V_01·V_12·conj(V_02)·conj(V_11))`: **Family A** (`z_e := w_e*+i·a_e*`,
uses both sectors), **Family B** (`z_e := i·a_e*`, skew-only, the unique gauge-clean
embedding), **Family C** (`N_ij := conj(Z_i)·Z_j` for `Z_i := Phi_i+i·Psi_i`, the
vertex-phase Gram/rank-1 embedding — this is the `omega`/doubled-real-space complex
structure lever the task named). The real-side gauge group tested is `Z2^{|V|}` vertex
switching, split by which bilinear source is probed: the skew source
`t_e := Phi_i·Psi_j − Phi_j·Psi_i` (sources `a_e*`) vs. the symmetric discordance
`s_e := (Phi_i−Phi_j)(Psi_i−Psi_j)` (sources `w_e*`).

**Th_coqc (`InfoThetaQuartetSquareObstruction_attempt.v`, 14 theorems, axiom-free,
independently `Print Assumptions`-confirmed by both reviewers and a fresh post-repair
recompile):** headline eight — `quartet_rescale_invariant` (the ONE shared
triple-convergent rescaling/rephasing lemma, filed once per orchestrator ruling, subsuming
all three routes' independently-derived versions), `family_B_K3_exact`,
`family_B_C4_vanishes`, `family_C_rank1_vanishes`, `family_A_not_switching_invariant`,
`skew_source_switching_covariant`, `symmetric_source_not_switching_covariant`,
`c4_reversal_is_gauge_witness` + `k3_no_uniform_reversal_gauge` (existence + general
impossibility, the bipartite-parity pair). Five supporting theorems (companion witness
values and the real-scalar-rescale variant) round out the 14. General-n cycle/tree
statements stay `[Open]`, matching 5.5's own precedent.

**The corrected gauge mechanism (the single most consequential finding, house-style
disclosed correction — a judge refuted a design route's own wrong-bilinear test):**
`t_e` is EXACTLY `D_i·D_j`-covariant under vertex switching `(Phi,Psi)→(D.Phi,D.Psi)` for
ANY `D` (`Th_coqc` `skew_source_switching_covariant`, unconditional ring identity) —
the skew/`a_e` sector is fully, dynamically gauge-compatible. `s_e` is NOT
`D_i·D_j`-covariant for non-uniform `D` (`Th_coqc` `symmetric_source_not_switching_covariant`,
concrete witness: `s'=21` vs. the naive covariant prediction `−1`) — the symmetric/`w_e`
sector breaks gauge-compatibility. Only the `a_e` sector — Family B — is dynamically
gauge-clean; any embedding touching `w_e` (Family A) is not.

**The verdict — OBSTRUCTED, by three mutually-reinforcing mechanisms, for every
embedding family examined:**
1. **Gauge split** (Th_coqc, above): only the skew/`a_e` sector is dynamically
   gauge-compatible with the real-side `Z2^{|V|}` switching group; the symmetric/`w_e`
   sector is not.
2. **Parity** (Th_coqc `family_B_K3_exact` + `family_B_C4_vanishes`): the unique
   gauge-clean embedding (Family B) reproduces `J_Theta` EXACTLY on K3
   (`Im(P)=a1·a2·a3`) but VANISHES IDENTICALLY on C4 (`i²·(−i)²=1`, real — the
   unconditional `i^4=1` parity fact). K3 is the program's dead topology — THREE
   disclosed independent search efforts, 0/3000 (5.2b-1) + 0/25000+homotopy
   (independent review) + 0/3000 extended (5.5) — and C4 is the program's only living,
   nonzero-`J_Theta` witness (33 distinct FPs, 5.5). Family B is nonzero exactly where
   nothing lives and zero exactly at the program's one living witness.
3. **Eigenbasis non-well-posedness** (finite_diagnostic + Dr): the eigenbasis bridge
   `V_cand := V_A^{-1}·V_B` is not well-posed. A fresh sweep (seed 551, this run's own
   disclosed measurement, not transcribed from any design paper): 29/528 sector pairs
   flip `quartetJ`'s sign across four eigen-ordering conventions (robust across two extra
   reviewer seeds: 20/561, 23/561 — qualitative existence of conflict is the load-bearing
   claim, not the precise 29 count), magnitudes span `~1461x`, non-normality residual
   `≥0.416` and non-unitarity residual `≥0.807` at all 33 living FPs (`G` genuinely has
   no canonical orthonormal eigenbasis). Plus a weakest-leg, explicitly-flagged `Dr`
   Galois-genericity argument: the eigenvalues generically generate a field extension
   with no structural reason to sit in `Q(i)`.

**Positive byproducts (disclosed, not buried):** `quartet_rescale_invariant` was
independently derived by all three design routes and is filed once — the one
unambiguously reusable, general, Coq-cheap positive lemma this square produces. Family
C's general rank-1 vanishing (`family_C_rank1_vanishes`, no case split, the single most
general lemma in the file) CLOSES, negatively and permanently, the `omega`/doubled-space
complex-structure lever the task named and 5.4/5.5 left open — no future attempt should
believe this lever is untried. The corrected `t_e`/`s_e` mechanism itself (found by a
judge refuting a design route's own wrong-bilinear test on `theta_oriented_skew_v1.py`'s
`S^{e,skew}` definition) is recorded as this program's house-style disclosed correction,
matching the caught-mistake conventions already visible in 5.2a/5.4's text.

**Disclosures (mandatory):** the python file (`theta_quartet_square_v1.py`) and the Coq
file use DIFFERENT C4 edge-quartet pairing conventions for Family A/B's construction
(python: adjacent-edge split; Coq: opposite-edge split) — both independently confirmed
correct under their own convention, but these are TWO INDEPENDENT WITNESSES of the same
qualitative gauge-dependence conclusion for Family A, NOT cross-file numeric
corroboration of one number; do not read the two files' witness values as verifying each
other. Eigen-ordering convention #4 in the Part-4 sweep is analytically redundant with
convention #1 (a unit-modulus column rephasing of it, so `quartet_rescale_invariant`
GUARANTEES the two agree) — it functions as a live sanity check of that lemma, not a 4th
independent ordering test; effective independent conventions in the magnitude-spread
statistic = 3, not 4. The 29/528 sign-conflict count is this-run/this-platform
(numpy 2.4.6, Python 3.13.13); the qualitative existence of eigen-ordering conflict, not
the precise count, is the claim this square rests on.

**Framing guards (binding, unchanged from 5.5):** this square does **not** resolve item
2's `[Open]` status — that determination stays an orchestrator/founder-level call
outside this square's scope (orchestrator ruling 7). No generation/CKM identification is
made anywhere (CRRC guard, grepped clean in both files). The eigenbasis bridge
(`V=U_A^†U_B`-style construction) stays FORBIDDEN as a `J` readout — its numeric
evaluation here is used purely diagnostically, to refute its own well-posedness
(orchestrator ruling 1's compliant refutation-purpose carve-out), never as a validated
readout. Named `[Open]` escape hatches, unchanged from the synthesis: exact
Groebner-basis/minimal-polynomial certification of a C4 living FP's exact eigenvalue
field; the nonlinear (non-affine) embedding family; the qualitative/inequality-relation
escape hatch; feeding `G`'s actual eigenvalues into the R2 holonomy machinery; general
finite-n-cycle and general structural-induction tree Coq lemmas (both inherited
`[Open]` from 5.5's own file).

**Named open items:** all four escape hatches above; the near-zero C4 cluster's
rigorous exact-arithmetic distinction from a possible exact-zero branch (inherited from
5.5, unaddressed here); stability of the C4 living FPs (inherited, unaddressed); full
continuous diagonal-rescaling gauge invariance beyond the Z2 sign-flip case (inherited).
