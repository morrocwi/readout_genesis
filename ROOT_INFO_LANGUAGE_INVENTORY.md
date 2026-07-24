# Root Info-Language Inventory — everything Coq-verified 100% from the root, translated out of domain vocabulary

**Status:** companion inventory, linked from [`READOUT_GENESIS_CORE.md`](READOUT_GENESIS_CORE.md#the-one-line-master-equation),
**not part of the master-equation box itself.**

**Why a separate file, not folded into the box:** the master-equation box's own discipline
(§V.20 THE WELD, §V.22 label-inflation rule) forbids treating every `[Th_coqc]` result across every
domain as if it were a new term of the master equation `F`. Only results that are genuinely the
**same `F` read at a different face** belong in the box (Group A below — these *are* already folded
into the box, 2026-07-23). Results that are theorems *about a specific domain instantiation* of `F`
(Standard Model, biology) are downstream consequences, not the equation itself, and are catalogued
here instead so they stay reachable without inflating the box.

**Method:** every row below was **compiled or coqchk'd fresh** (not just read off an existing
`[Th_coqc]` tag) in a verification session on 2026-07-23. Passing bar: `coqc` returns `Closed under
the global context` for every embedded `Print Assumptions` call, or `coqchk` returns `Modules were
successfully checked` with no `Axioms:` section and no `Admitted` anywhere in the source.

**Info-language rule:** the "equation (root language)" column uses only root vocabulary (δ, edges/graph,
retained-distinction, order-parameter, τ_c, M/D, Γ, K, Q_v, ...) — no domain words (no "photon", "color",
"gene", "disease", ...). Domain vocabulary is parenthesized at the end of the row for cross-reference only.

---

## Group A — Faces of the one master equation `F` (same information, different face)

Source: `causal-quantum-gravity/formal/*.v` (module root `DQG.formal`, compiled from that repo's root with
`-R . DQG`) + `research_universal_solver/formal/InfoAnalysisLift.v` (module root `RDL`). **These files are
not mirrored into this repo** — they live in sibling repos on the same machine
(`~/ANSE.ASIA/causal-quantum-gravity`, `~/ANSE.ASIA/research_universal_solver`). All 14 are already folded
into the master-equation box's 2026-07-23 verification addendum.

| Theorem | Equation (root language) | Verified |
|---|---|---|
| `InfoActionStationarity.retention_balance_rem` | δS/δZ_n is unchanged (no free growth) when a retained node is removed — the difference equals exactly the boundary term | ✅ coqchk clean |
| `InfoBackReaction.strain_nonneg` / `strain_zero_iff` | strain(x,e) ≥ 0 always; strain(x,e)=0 ⟺ x_u = x_v (no distinction across the edge) | ✅ coqchk clean |
| `InfoConeInheritance.step_path_local_stencil` | one operator step inherits the same local stencil ⇒ the finite causal cone survives composition | ✅ coqchk clean |
| `InfoCrossTermDominance.cell_diag` / `cell_cross_polarization` | the cross term in a 2×2 local cell separates cleanly from the diagonal term | ✅ coqchk clean |
| `InfoCubicLinearization.qshift_nonneg` / `qshift_pos` | the residual linearized from the cubic potential is ≥ 0 (and > 0 off the fixed point) | ✅ coqchk clean |
| `InfoCutGrowth.screen_strain_nonneg` | cut is monotone under edge growth; screened strain ≥ 0 | ✅ coqchk clean |
| `InfoGraphNoether.noether_c6` | symmetry under a graph permutation (C6 rotation) ⇒ a conserved quantity (Noether on a graph) | ✅ coqchk clean |
| `InfoLorentz.causal_form_frame_covariant` | Q_v = n₊·n₋ (from the cone's edges) is covariant under frame change — signature comes from the causal order `≺` | ✅ coqchk clean |
| `InfoLorentzInvariance.box_quad_boost_invariant` | the box quadratic form is invariant under a boost (g²(1−v²)=1) — narrow claim only, not the broader "unification" claim this book refuses elsewhere | ✅ coqchk clean |
| `InfoMemoryBeforeMass.memory_before_mass` | rate·τ_c = 1; equal τ_c ⇒ identical dynamics regardless of how (M,D) split — **memory (τ_c) precedes mass (M)** | ✅ coqchk clean |
| `InfoMetricIsEnergyReadout.metric_form_is_energy_readout` | qform(L(edges), x) ≡ energy(edges, x) — the metric's Hessian and the energy functional are the same object | ✅ coqchk clean |
| `InfoQuantumRelativityUnification.spine_dispersion_iff_box_quad_vanishes` | M·ω² = K·λ ⟺ box_quad(...) = 0, and this null-condition survives a boost — narrow dispersion-identity claim only | ✅ coqchk clean |
| `InfoSeedTorsionGroupAndRankN.rankn_seed_torsion_is_lam_ord` | nonzero torsion witness ⇒ the commutator generates a non-abelian group of rank N (the gauge-algebra seed) | ✅ coqchk clean |
| `InfoCoercivityBoundedClosure` | wshare/wdeg closure is bounded (coercivity of the potential) | ✅ coqchk clean |
| `InfoAnalysisLift.clairaut_xy` / `clairaut_yx` (`research_universal_solver/formal`, root `RDL` — **not** the same-named file in `causal-quantum-gravity`, which imports Schwarzschild and is refused elsewhere in the core doc) | ∂²(metric)/∂x∂y = ∂²(metric)/∂y∂x — mixed-partial symmetry of the metric lift | ✅ coqchk clean |
| `InfoRetainedDistinctionForcesLaplacian.only_LR_passes_all_three` (`research_universal_solver/formal`, root `RDL`, still tagged `_attempt` in that repo's own convention) | among candidate retained-difference operators, **only** `L_R` passes all required structural tests — the exact citation already backing the `L_R` row in the master box, now independently reconfirmed | ✅ coqchk clean |
| `InfoSeedUnifiedMasterEquation.seed_master_readout_zero_iff_homogeneous` (same source, `_attempt`) | velocity+coupling+damping combine into one seed readout that vanishes iff the field configuration is homogeneous | ✅ coqchk clean |
| `InfoScaleGaugeNonReadout.dispersion_gauge_invariant` (same source, `_attempt`) | the dispersion relation's sign/structure is invariant under a scale-gauge transform | ✅ coqchk clean |
| `InfoSeedArgminActionCost.action_argmin` (same source, `_attempt`) | the selected state minimizes the action (general variational principle) | ✅ coqchk clean |
| `InfoConnectionFromFrame.closed_loop_pure_gauge_flat` / `genuine_curvature_is_non_coboundary` (same source, `_attempt`) | a connection built from any frame difference; a closed loop is pure gauge iff flat, and genuine curvature is exactly the non-coboundary part | ✅ coqchk clean |
| `InfoDiscreteRiemannCurvature.flat_iff_second_diff_zero` (same source, `_attempt`) | discrete curvature from second differences: flat ⟺ the second difference vanishes | ✅ coqchk clean |
| `InfoDiscreteRiemannCommutator.nonvacuous_witness` (same source, `_attempt`) | curvature recovered from the transport commutator; the nonvacuous witness shows it's not a vacuous statement | ✅ coqchk clean |
| `InfoTelegraphHorizonUnification.lam_c_is_spine_lambda_c` (same source, `_attempt`) | the spine's own classical/quantum crossover `λ_c` (Face 3/4 content) — a *distinct* object from GR redshift, not a claim of unifying the two | ✅ coqchk clean |
| `InfoOrderDefectFromComposition` (`domains/standard_model/`, **promoted from Group B 2026-07-23 round 2**, caveat: the algebraic identity — bilinear+antisymmetric commutator, Jacobi from associativity — is genuinely general; the specific noncommuting pair used to witness it is hand-exhibited, not itself root-forced) | K(X,Y)=XY−YX bilinear+antisymmetric; Jacobi follows from associativity of ordered composition alone — no Lie algebra imported | ✅ coqchk clean |

**This is the set that legitimately folds into "the master equation"** — these 24 *are* the stepper `F`
read at a different regime/face, not separate theorems. (15 confirmed round 1, 2026-07-23; 9 more —
8 new + 1 promoted from Group B — confirmed round 2, same day, after applying the founder's stricter
necessity bar: only admit a result if its premises are root-generic, not conditional on a declared
domain alphabet/architecture.)

**Round-2 correction (independent adversarial review, second Claude session, 2026-07-23):** two
candidates initially proposed for promotion — `InfoRationalSO3Curvature` and `InfoOrderedTapeClosure`
— were caught and reverted before merge. Both files **self-tag as conditional in their own headers**:
`InfoOrderedTapeClosure.v` states *"HONEST FENCE. CONDITIONAL ALGEBRAIC PASS... Kinematic neutrality
is NOT yet dynamical confinement"* and hardcodes its dimension-3 carrier (`Mat3`) as a record rather
than deriving it; `InfoRationalSO3Curvature_attempt.v` states *"this is a specific pair, not a
parametrized theorem for all rational rotations"* — one hand-picked Pythagorean-triple witness, not a
general SO(3)/dimension-3 derivation. Both remain correctly classified as conditional, in Group B below.

---

## Group B — Theorems that follow from applying `F` to a specific question (Standard-Model chain, v0.2–v1.13)

Source: `domains/standard_model/*.v` in **this repo** — compiled standalone fresh 2026-07-23 (no custom
imports beyond the Coq standard library).

| Theorem | Equation (root language) | Domain vocabulary (reference only) |
|---|---|---|
| `InfoOrderedTapeClosure` (initially misclassified as necessity in a round-2 draft, reverted after independent review — see the round-2 correction note above) | closed ordered tape: nonzero witness ⇒ (−1)^(k−1)=1 ⇒ k odd; minimal odd k>1 ⇒ k=3; **but** the k=3 carrier is realized via a hardcoded 3×3 matrix type, not derived from the closure argument itself — "Kinematic neutrality is NOT yet dynamical confinement" (the file's own fence) | (color=3, SU(3), Z₃ center) |
| `InfoBlindMatterSearch` | blind enumeration over a minimal representation alphabet under closure/anomaly/parity/no-vectorlike/minimality gates ⇒ minimum total dimension = 15, forced (not fed in) | (matter skeleton, 1 generation) |
| `InfoRootChirality` | a grading Γ from the ordered triple (Γ²=I, Γ†=Γ, RΓR=−Γ); an order-odd Ξ is required to get an asymmetric projector P=(I−ΞΓ)/2 | (chirality, one-sided weak coupling) |
| `InfoTapeKineticGW` | an exact Ginsparg-Wilson relation Γ(I−V)+(I−V)Γ=(I−V)Γ(I−V); no-doubling when 0<m₀<2r | (kinetic operator, fermion doubling) |
| `InfoDimensionFourClosure` | d≤4, d even, d≠2 ⇒ d=4 forced from a dim-4 carrier + isotropy + kinetic-closure gate | (why d=4, 3+1) |
| `InfoIsotropicFixedPoint` | the twirl Π₄(X)=(TrX/4)I is an exact projector; the contraction Δ_(n+1)=(1−α)Δ_n is an irrelevant direction; spectral radius ρ<1 (root of a degree-6 polynomial over ℚ) | (isotropic fixed point, Lorentz shadow) |
| `InfoFrameMixingAction` | the mixing weights p(h) come from a Gram operator K=B†B (reflection-positive); the only fixed metric is the scalar line ℝI | (frame-mixing from the action) |
| `InfoOrderHiggsClosure` | the order carrier is forced: a singlet w.r.t. one closed sector + a doublet w.r.t. a paired sector; the neutral mass-matrix has rank 1 ⇒ one null direction + one non-null direction | (Higgs rep, massless photon, m_W/m_Z) |
| `InfoIntertwinerOrderVacuum` | invariant multiplicity ≠ rank of the closure map; Z_j(r)=(1+λ_j r)^{d_j}; order condition Π₀>α | (⟨H†H⟩>0, order-vacuum criterion) |
| `InfoHyperchargeGlobalQuotient` | a global quotient structure on the charge lattice | (hypercharge Z₆ quotient) |
| `InfoHyperchargeAnomalyClosure` | Σ(charge³)=0 exactly ⇒ forces the charge assignment | (cubic anomaly=0, hypercharges) |
| `InfoElectroweakNullDirection` | obstruction matrix M²=(v²/4)·outer((g,−g'),(g,−g')) is rank 1, det=0 ⇒ exactly one null direction | (massless-photon emergence) |
| `InfoFourForceCirculationRecovery` | χ=A⁻¹, the exact identity χ−χᵀ=−2χᵀΩχ; Ω is recovered as the antisymmetric part of χ⁻¹ | (four-force circulation decoder) |
| ~~`InfoOrderDefectFromComposition`~~ | **promoted to Group A, 2026-07-23 round 2** — see above | (order-defect, non-abelian seed) |
| `InfoConfinementCertificate` / `InfoCenterConfinement` / `InfoBlockCorrelation` / `InfoAllOrderCharacter` / `InfoSurfaceAutomaton` / `InfoSurfaceUpperAutomaton` | a family of surface-entropy bounds + automaton brackets that close as a computable certificate | (confinement) |
| `InfoTrialitySpectralFlow` / `InfoUniversalRPSlab` / `InfoFiniteTransferGap` / `InfoRetainedIntertwiner` | a universal reflection-positive slab reads the finite-transfer spectral gap in every sector | (mass gap, universal RP slab) |
| `InfoRationalSO3Curvature` (`research_universal_solver/formal`, `_attempt`; reverted from a round-2 necessity-promotion attempt — see correction note above) | one concrete rational-rotation pair with nonzero holonomy — proves curvature *exists* for this witness, not a general SO(3)/dimension-3 derivation (file's own words: "a specific pair, not a parametrized theorem") | (SO(3) holonomy witness) |

**Important**: Group B is **not** a new master equation — these are theorems that *follow* when `F` is
squeezed against the Standard-Model alphabet/gates. Do not lift these into `F` as new additive terms —
that would be exactly the label-inflation this book warns against (§V.20, §V.22).

---

## Group C — Biology / Health / Epidemic (compiled fresh 2026-07-23 — clean, but still tagged `_attempt` in the source repo)

Source: `research_universal_solver/formal/Info*_attempt.v` (sibling repo, not mirrored into this repo).

⚠️ **Honesty note:** these files have **not been promoted** to a canonical (non-`_attempt`) name in their
home repo's own convention — meaning they have not gone through a final review pass or been wired into
that repo's index yet. They did, however, **compile clean, fresh, today, with no `Admitted`/`Axiom`.**

| Theorem | Equation (root language) | Domain vocabulary |
|---|---|---|
| `InfoBioHomeostasis.homeostasis_balance` / `turnover_is_production` | geometric decay; the balance point is where production equals turnover | (homeostasis) |
| `InfoHealthCuspFold.rest_iff_critical` | the system is at rest (a fixed point) ⟺ it sits exactly at the critical threshold (cusp) | (cusp/fold, health) |
| `InfoHealthCausalRelax.n_step_error` | the error after n steps is the n-th power of the single-step error (geometric decay of the relaxation error) | (causal relax) |
| `InfoCoupledCuspEP3.sync_solves_single_cusp` | two cusps that synchronize satisfy the same equation as a single cusp (composition adds no new term) | (EP-3 coupling) |
| `InfoEpidemicThreshold.endemic_positive_iff_R0_gt_1` | a nonzero fixed point exists ⟺ the reproduction ratio > 1 | (SIR/SIS threshold) |

---

## Group D — External-contributed, declared-gate-conditional (π/φ retained-history fusion + Page-curve toy experiments, 2026-07-24)

Source: `external_research/pi_phi_retained_history_page_curve_v3/` (this repo). A user-supplied,
externally-produced research bundle, downstream of this repo's own canonical Standard-Model doc
(used as its declared anchor), independently re-verified here (arithmetic reproduced from raw
data, `PASS`). **Nothing in this group is `Th_coqc`** — no `.v` witness exists for any of it — and
none of it enters "THE FORCED SET" box in `READOUT_GENESIS_CORE.md`. See the folder's own `README.md`
for the full tier table; summary:

| Result | Tier | Status |
|---|---|---|
| `τ⊗τ≅1⊕τ ⇒ FPdim(τ)=φ` | `finite_diagnostic`, conditional | Closed only under 7 declared gates H1–H7 (finite-dim history morphisms, splitting idempotents, simple unit, finitely many simples, duals+snake, faithful positive pairings). Root-forcing H1–H7 in any natural domain is explicitly `not_established`. Uses Ostrik's external rank-two fusion-category classification, cited not re-derived. |
| Golden-angle identity `θ_G=2π/φ²` | `Dr` | Algebraic identity, not a physical claim. |
| Finite-qubit signed-readout / retained-transfer architecture | `finite_diagnostic` | Matches this repo's own `readout-not-truth` discipline: negative readouts are kept as signed information, never silently clipped into a fake entropy. |
| φ-schedule vs random measurement scheduling | `finite_diagnostic`, protocol-dependent — **both directions kept** | 8-seed reduced protocol: φ beats random 8/8 (mean RMSE −31%). Independent simple-protocol counterexample: φ *loses* to random by −30%. Neither is allowed to generalize; both scripts + raw data are in the folder. |
| Physical Page curve / black-hole unitarity / quantum advantage | **`[Open]`** | Explicitly `NOT_DERIVED` / `NOT_DEMONSTRATED` in the source's own claim boundary. Do not cite this group for any of these. |

⚠️ **Retraction on record inside the source material itself:** an earlier draft of this same
program claimed a physical Rényi-2 entropy improvement; the underlying cross-purity values were
outside the physical `[1/d,1]` interval and had been silently clipped before `-log`. That claim is
marked `RETRACTED_AS_PHYSICAL_ENTROPY_ENDPOINT` in the source's own audit — kept here as an example
of the exact non-readout injection this repo's discipline exists to catch, not as a live claim.

---

## Not yet verifiable this round (stated honestly, not hidden)

Round 1 flagged 11 names as unverified; round 2 (2026-07-23) tracked down and independently
coqchk'd 9 of them clean. 8 are genuinely necessity-tier and are now in Group A above
(`InfoConnectionFromFrame`, `InfoDiscreteRiemannCommutator`, `InfoDiscreteRiemannCurvature`,
`InfoScaleGaugeNonReadout`, `InfoSeedArgminActionCost`, `InfoSeedUnifiedMasterEquation`,
`InfoTelegraphHorizonUnification`, `InfoRetainedDistinctionForcesLaplacian`). The 9th,
`InfoRationalSO3Curvature`, compiles clean but is a **single hand-picked witness pair**, not a general
theorem (see the round-2 correction note above) — it stays conditional, listed in Group B. Still
outstanding:

`InfoAllOrderCharacter` (file found, not yet re-tested independently of Group B's compile),
`InfoQuotientCompressionExactness` (not located this round either)

→ these do not enter this inventory until independently compiled and coqchk'd clean — per this
inventory's own rule ("Coq-verified 100% from the root, or it doesn't count").

## Already refused in the core doc itself (do not re-admit even though the tag looks fine)

The broad "`InfoLorentzInvariance`" / "`InfoQuantumRelativityUnification`" **unification** claims — the
core doc's §V.13a states these secretly import the Minkowski interval and boost as premises (not root-derived).
Only the narrow theorem content verified in Group A above (boost-invariance of the box quadratic form) is
kept; the broader "unification" reading that the book itself refuses is not reinstated here.
