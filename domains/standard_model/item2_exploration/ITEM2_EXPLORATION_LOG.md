<!-- Exploration log, tier Dr throughout. Item 2 (HANDOFF_NEXT_SESSION.md, generation
     multiplicity) is NOT closed by anything in this file. This is a scoping note: one
     confirmed structural fact about where the search for "why 3 generations" must actually
     start, adversarially reviewed before commit per the process this domain's item 1 log
     established. -->

# Item 2 exploration — 2026-07-24: scoping the actual starting point

## What this is and is not

This is not an attempt at deriving generation count. It is a single, deliberately small,
adversarially-reviewed first step: applying the checklist item1_exploration/ITEM1_EXPLORATION_LOG.md
left behind (Retained-Degree Insufficiency, RDI) to item 2 *before* proposing any construction,
per that log's own instruction: "before proposing any construction for 'why 3 generations,'
count how many genuine independent degrees of freedom that construction's own retained
structure carries." This entry counts that, for the one structure in this domain that already
performs a real search over matter content.

## Finding: the closed matter-search architecture carries zero generation-distinguishing
## degrees of freedom — a confirmed scoping fact, not a new discovery

`blind_matter_search_v1_6.py`'s blind search enumerates a multiplicity vector
`n=(nA,nAb,nB,nBb,nC,nD)` over **representation types**
(`A=(3,2), Ab=(3̄,2), B=(3,1), Bb=(3̄,1), C=(1,2), D=(1,1)`), and its gates (anomaly-freedom,
no-vectorlike, minimality) select the lexicographic-minimal anomaly-free chiral set — which
turns out to be exactly one full generation (`N_mult=5`, `D_total=15`). Reading the actual
enumeration/gate code (not just the docstring) confirms there is no second axis anywhere in
that search along which "family/generation copy" could vary — the search space has a
dimension for *what representation types appear*, not for *how many independent copies of a
full generation exist*. This was checked directly against the code by an independent
adversarial reviewer (2026-07-24, sonnet, instructed to refute), who confirmed the observation
holds and found no hidden family/flavor/generation index anywhere else in the domain (grepped
across every `.py`/`.md` in `domains/standard_model/`).

**Correction applied per that review** (do not overclaim past what survived): this is *not* a
new instance of Retained-Degree Insufficiency in the sense `ITEM1_EXPLORATION_LOG.md` defines
it (a readout collapsing, underdetermining, or tautologically returning a value because the
structure it reads HAS some but too few degrees of freedom). This is a stronger, simpler case —
**absence of the structure entirely** (M=0 DOF along the relevant axis, not "M<N DOF"). RDI is
the right checklist to have *run*, and its logic motivates why this check matters, but it should
not be cited as the diagnosis itself; the correct plain statement is a **scope-gap finding**:
`HANDOFF_NEXT_SESSION.md` and `hypercharge_global_quotient_v1_5.py` already flag generation
multiplicity as `OPEN` / "count NOT derived" at the *claim* level — this entry adds the
*code-level* reason why, confirmed by direct inspection rather than restated from the honest
fences: the existing search was never built with a family axis to search over in the first
place, so no refinement of `blind_matter_search_v1_6.py` itself can answer item 2 — a
structurally new construction is required, not a parameter sweep of the existing one.

## What this does NOT license

- Any claim, guess, or hint about the value 3, or any other number.
- Any claim that generation count is unconstrained/free — only that the CURRENT architecture
  does not yet contain a structure that could constrain it either way.
- Reuse of `SM_INFORMATION_PHILOSOPHY_MASTER.md` §2.1-2.2's cyclic-tape-closure argument
  (`k` odd, minimal `k>1 ⇒ k=3`) for this question — that argument is CRRC-forbidden here per
  `HANDOFF_NEXT_SESSION.md` §0.-1: it answered a different question (color-channel count) and
  its own admissibility square for "family index" has not been built and is not attempted here.

## The actual next construction task (named, not built)

Per the finding above, the first real task for item 2 is: construct **any** structure, built
independently from §2.2's cyclic-closure argument, that retains a genuine family-index degree
of freedom at all — invariant under every currently-established gauge automorphism `𝒜`
(`G0.1`–`G0.5`, closed `Th_coqc`), since real generations are not rotated into each other by
gauge transformations. Only once such a structure exists, with its own from-scratch
admissibility square, does "what caps its count at 3 (if anything)" become an answerable
question rather than premature.

## Attempt 1 — `item2_family_index_v1.py`, 2026-07-24: gauge anomaly cannot bound N (negative, scope-narrowing)

Formalizes the actual family-index slot the finding above says is missing: total matter space
`V_R ⊗ ℂ^N`, where every gauge automorphism `h∈𝒜` (`G0.1`–`G0.5`, closed) acts only on `V_R`
and as the identity on `ℂ^N`. Tests whether gauge-anomaly-freedom — the one per-generation
consistency condition this domain has already closed (`hypercharge_global_quotient_v1_5.py`) —
constrains `N`. Result, reusing v1.5's own closed hypercharge values exactly: local mixed
anomalies (`A_grav`, `A_111`) and the global Witten SU(2) doublet-parity condition are all
**linear in `N`**, hence identically satisfied (zero, or even) for every `N≥0` — verified by
direct computation for `N=0..7`. **Rules out gauge-anomaly-freedom as the closure condition
that could bound generation count**, before any further work is spent chasing that direction.

**Independent adversarial review (2026-07-24, verdict SURVIVES WITH CORRECTION)** required two
corrections, both applied to the script's own honest-fence text before this log entry:
1. The `ℂ^N`/trivial-gauge-action shape is **not merely "unverified in Coq"** — it borders on
   the practice `SM_INFORMATION_PHILOSOPHY_MASTER.md`'s own opening rule forbids (physical
   names/motivations fed as premises rather than earned): the shape's actual justification
   ("gauge can't rotate top into charm") is imported from known real-world SM phenomenology,
   not built from anything `G0.1`–`G0.5` actually closes (those close single-frame
   composition/inverse/localization/holonomy; nothing about multi-copy carriers). This must be
   treated as a physics-motivated **working ansatz**, not an established, earned structure.
2. The anomaly-blindness result is **not new physics** — it is well-known/textbook in real
   physics that anomaly-freedom is generation-blind. The genuine, modest contribution is
   re-deriving it exactly on this framework's own closed numbers, narrowing the in-repo search
   space — not a discovery. Overstated "CONCLUSION" language in the script was softened
   accordingly.

**What Attempt 1 does NOT establish**: any value of `N`; that the `ℂ^N` ansatz is earned rather
than imported; that no OTHER closure condition could bound `N`. The named-but-unbuilt next
candidate (an index-theorem-style "net chirality count as a topological invariant of the
closure map", by loose analogy to continuum QFT) remains explicitly unattempted and
CRRC-quarantined — it needs its own from-scratch admissibility square before any construction,
not resemblance-based borrowing.

## Attempt 2 — `item2_family_index_v2_fit.py`, 2026-07-24: `fit_calibrated`, `N=3`, per DEV-SM-002

Founder authorized a fitting track for item 2, same shape as item 1's DEV-SM-001: "ฟิตค่า ได้นะ
ไม่ต้อง ดีไรต์ จะเอาไงนายจัดการเลย ขอให้ตรงกับปรัชยาเรา และไสต์การทำงานเรา" (fitting is fine,
doesn't need to be a from-root derivation, handle it however, as long as it matches our
philosophy and working style). Declared as `DEV-SM-002` in `DRIFT_CONTRACT.json` (compensating
controls: tier tag on every occurrence, caveat in the same line, explicit non-weakening of
`hard_fail_conditions[4]`, borrowed theorem registered in `EQUATION_REGISTRY.md` before use).

**Construction, three explicit ingredients:**
1. **Borrowed, exact theorem** (Cabibbo 1963; Kobayashi–Maskawa 1973, registered in
   `EQUATION_REGISTRY.md`): an `N×N` unitary mixing matrix has `(N−1)(N−2)/2` physical CP-
   violating phases — zero for `N<3`, first nonzero (`=1`) at `N=3`. Verified exactly (plain
   integer arithmetic) for `N=0..6`.
2. **Externally observed fact, fed in as input, not derived**: CP violation of this kind is
   real (CMS `B⁰ₛ→J/ψK⁰`, 2026-07-24 — the same measurement `HANDOFF_NEXT_SESSION.md` §0.-1
   names as this item's motivating context).
3. **This framework's own minimality-selection style, explicitly flagged as a POSTULATE**: pick
   `N := min{N : phase_count(N)≥1} = 3`.

**Result**: `N_generations (fit_calibrated) = 3` — matches the real, observed count. Uses no
continuous fitted constant at all (only an integer selection over exact integer counts) —
genuinely minimal-parameter as the founder's instruction asked for.

**Independent adversarial review (2026-07-24, verdict SURVIVES WITH CORRECTION)** required
three corrections, all applied before this log entry:
1. **Bug found and fixed**: the script's two phase-count computations disagreed at the `N=0`
   boundary (one correctly gated to `N≥1`, the other an ungated raw formula giving a spurious
   `phase_counts[0]=1`). Fixed by gating both identically; does not affect the `N=3` result
   (`N=0` — no matrix, nothing to observe — was never the selected value).
2. **Criterion-selection hindsight, now disclosed in the fence**: the same parameter-counting
   family yields several countable quantities (angles, physical params, phases); "phase count"
   was selected because it is the CP-relevant one, which is only obvious given the target
   observation — a different, equally legitimate-looking choice ("angles≥1") would select
   `N=2`, not `3`. This is a declared fit doing exactly what a declared fit is allowed to do
   (matching a criterion to the target observation, per DEV-SM-002), but it must never be
   described as "the only natural choice" — now stated explicitly in the file.
3. **Minor cleanup**: dropped an unused `Fraction` import and corrected the registry's "exact
   over ℚ" phrasing to "exact over the integers" (no fractional values ever arise; the earlier
   phrasing overstated the machinery used).
Also confirmed by the same review: the postulate/forcing distinction (this construction's
minimality vs. `SM_INFORMATION_PHILOSOPHY_MASTER.md` §2.2/§3.1's forcing-style minimality) is
stated loudly and consistently, with no slippage into implying `N=3` is "the" answer;
`hard_fail_conditions[4]` compliance is clean (no unqualified "derived from root" language
anywhere); the Cabibbo/Kobayashi–Maskawa attributions are accurate.

**What Attempt 2 does NOT establish**: any derivation, forcing, or from-root necessity of `N=3`;
that `N=4,5,…` are excluded by anything but the fed-in CP-violation observation; that "nature
prefers minimal `N`" is anything but an unproven meta-postulate stated as such.

## Attempt 3 — `item2_cp_equivariant_lower_bound_v3.py` + `formal/InfoCPEquivariantGenerationBound_attempt.v`, 2026-08-08: conditional N≥3 forced, in-house, exact

Built per the founder's direction to learn from `information-discrete-math` (idm) and
`readout_universe` and extract tools for item 2 (this session first read
`IDM_CROSS_POLLINATION_TODO.md` #2/#4/#9/#10, `item1_exploration/ITEM1_EXPLORATION_LOG.md` in
full, and a thorough `readout_universe` survey confirming no prior generation-count derivation
exists anywhere and yielding two governing rules applied here: B1 — a mechanism must REDUCE
freedom, not reparametrize a knob; Q3 — identity by role, `k_color` and `n_gen` stay distinct
symbols regardless of shared digits).

**Construction (admissibility square built from scratch — nothing reused from the color
argument or `IDM_Harvest.v`):** object space = N×N unitary mixing configurations over exact
Gaussian rationals ℚ(i); involution = elementwise conjugation (the CP action); readout = sign
of a Jarlskog-type quartet invariant into {+,−,0}. IDM's equivariant-readout machinery is used
as proof PATTERN only (per TODO #2/#10); the per-instance content (equivariance, neutrality on
CP-fixed objects, non-degeneracy) is proven/exhibited locally, not cited.

**Machine-checked content** (Coq, 13 theorems, all `Print Assumptions` = Closed under the
global context; plus an exact-Fraction Python verifier, ALL PASS, no floats anywhere):
1. **Vanishing theorem (load-bearing, in-house):** for ANY 2×2 matrix over ℚ-pairs satisfying
   the column-orthogonality relation of unitarity, the quartet's imaginary part is exactly 0 —
   N=2 mixing structurally CANNOT retain a CP-signed difference. Proven generally
   (`two_gen_quartet_im_vanishes`), instance-swept on 648 exact ℚ(i) unitaries.
2. **CP equivariance, general:** conjugation flips the quartet sign (`quartet_conj_flips_sign`)
   — the signed readout is CP-equivariant for arbitrary entries; also rephasing-invariant
   (checked exactly), so it reads the physical equivalence class (master §1.2), not a basis.
3. **N=3 witness, exact:** V = R23·R13(d)·R12 from Pythagorean triples (3-4-5, 5-12-13,
   8-15-17) and unit-modulus Gaussian-rational phase d=(3+4i)/5 — exactly unitary, with
   J = 110592/4151485 ≠ 0 exactly (closed-form cross-checked). No trig, no continuum angles —
   IDM-floor clean.
4. **Three readout values realized** on {witness, CP(witness), CP-fixed real unitary}: {+,−,0}
   pairwise distinct — the 3-value minimality pattern instantiated locally on THIS square.

**The conditional result (premise always attached):** IF the world retains a CKM-type CP-signed
difference (empirical premise, fed in — same epistemic slot as Attempt 2's ingredient 2), THEN
N ≥ 3 is FORCED by the vanishing theorem given that premise — no fit, no tuned knob, no
minimality postulate needed for the ≥3 half. This upgrades Attempt 2's "≥3" ingredient from
borrowed-theorem+postulate to in-house-proven conditional mechanism. It also partially
addresses Attempt 2's disclosed criterion-selection-hindsight caveat: |V_ij|² is CP-EVEN
(proven trivially, checked exactly), so an angle count was never a candidate criterion FOR a
CP-difference readout — the criterion is selected by the equivariance structure; what remains
genuinely chosen is the premise that the CP difference is the retained difference in question.

**NOVELTY, calibrated (per Attempt 1's review precedent):** the physics content (2 generations
admit no CKM-type CP violation; observed CPV implies ≥3) is textbook (Kobayashi–Maskawa 1973),
NOT a discovery. The contribution is only the in-house exact/machine-checked re-derivation on
this framework's own terms and the criterion-structure analysis.

**NOT from the root — stated plainly (founder asked directly: "มาจากรากของเราจริงๆไหม"; answer:
no):** the supporting structure is imported, not grown from the root — the existence of an N×N
unitary mixing matrix (items 21–23 open), the ℂ^N family slot (Attempt 1's flagged ansatz),
unitarity itself (quantum-domain prerequisite, backlog item 33), and the CP↔matter/antimatter
semantics are all imported; the premise is empirical. What is native is the lens and the
discipline (IDM equivariant-readout pattern, exact-ℚ(i) floor, tier honesty). Epistemic rung:
"exact within a declared/imported architecture + empirical premise" — NOT the root-native rung
of the §2.1–2.2 color chain. If a future root-native family structure emerges (see below), this
attempt's N≥3 becomes a consistency check on it, not its derivation.

**Independent adversarial review (2026-08-08, verdict SURVIVES WITH REQUIRED CORRECTIONS, all
applied before commit):** (1) the orthogonality relation was mislabeled "row" — it is COLUMN
orthogonality (naming error, not soundness; fixed in both files); (2) the textbook-physics
novelty calibration had to be stated explicitly, not implied (added to both files); (3) the
Section-1 "r is total on X_N" wording was inaccurate at N=2 (the fixed 3×3 indices don't exist
there) — reworded as a per-N quartet-sign readout family. The reviewer independently re-derived
the decomposition identity symbolically, rebuilt the witness and the 648-family with different
constructions, retyped the Coq literals from source, re-ran `Print Assumptions` on all 13
theorems from its own scratch file, and confirmed CRRC-cleanliness (color-argument terms appear
only inside explicit guards) and DRIFT_CONTRACT `hard_fail_conditions[4]`/[8] compliance.

**Named next direction (founder, same session): Θ as the new root.** "ไปอ่าน readout universe
เพื่อเชื่อมตัวอ่าน บันทึก ความแตกต่าง และธีต้าซึ่งเป็นรากใหม่" — connect reader Φ, record Ψ,
retained difference, and Θ (the living-geometry state, `𝔾[Θ_n]=𝔾_0+Σ_a Θ_n^a 𝔾_a`,
`Θ_{n+1}=A_Θ Θ_n+B_ΘΦ Φ_n+B_ΘΨ Ψ_n`, source `S_Θ^a=Φᵀ𝔾_aΨ` per generator direction) as a
root-native carrier for the family index — under the hard constraint of
`item1_exploration/CONTINUUM_ARC_ERROR_NOTE.md`: discreteness must live in the OBJECT (the
discrete `L_R`/`𝕋_phys` spectrum per representation sector, MASS_GAP §25), never in a
continuous Θ knob (the retracted EQ-069–071 mistake). Scoping completed same session —
see [`THETA_ROOT_PROGRAM.md`](THETA_ROOT_PROGRAM.md) (founder ruling recorded; Θ-direction
census closed for n=3 at `Th_coqc` — `formal/InfoThetaEdgeCensus_attempt.v`; the two Θ laws
reconciled — `theta_direction_census_v1.py`; central row `DEC-theta-new-root-2026-0808`).
No family-index construction attempted; item 2 status unchanged.

## Attempt 5 — `theta_oriented_skew_v1.py` + `formal/InfoThetaOrientedSkewObstruction_attempt.v`, 2026-08-09: support-tied real oriented skew extension; `J_Theta≠0` FOUND at a living C4 fixed point, first root-native nonzero orientation-odd invariant in the program

Built per Attempt 3/`THETA_ROOT_PROGRAM.md` §5.4's own named next frontier: the corpus's
own `𝔾^(−)` G-adjoint split and `ω` pairing as candidates for making a retained `J≠0`
root-realizable. Item-2 side, this is **Theta 5.5** in the Theta-root-program line (see
[`THETA_ROOT_PROGRAM.md`](THETA_ROOT_PROGRAM.md) §5.5 for the full construction).

**Design provenance (multi-agent, disclosed):** a 3-route design workflow produced a
real-skew route (Route B), a Q(i)/`μ₄` route (Route A), and a hybrid (Route C);
adversarial judging FOUND a real support-untied bug in Route B's original construction
(its `a_e` was computed on every ordered pair regardless of support membership, silently
re-opening the census's "one direction per edge" closure) and a synthesis pass REPAIRED
it (support-tying: `a_e≡0` off the census-selected edge set `E`, by declaration). Orchestrator
ruling (binding): PRIMARY = the repaired support-tied real construction only; the
Q(i)/`μ₄` FALLBACK branch was NOT built (no `theta_oriented_gaussian_*.py` exists in the
repo); the untied enlarged-census reframing is deferred as a named **5.6 candidate**, not
pursued here. Implementation was checked by two independent adversarial reviews
(verdicts RELEASABLE and RELEASABLE-AFTER-FIXES) plus one repair pass that fixed a
print-precision overclaim at its root cause (a `%.6f` display format was silently
rounding a genuine ~2.6e-14 `J_Theta` cluster to `0.000000`, causing the implementer's
own natural-language summary to overstate uniform "9-11 orders of magnitude above
noise" — the on-disk file's raw output was always honest; only the summary text was
fixed, by switching to scientific notation plus an automatic magnitude-spread line).

**Construction:** for the SAME edge set `E` the existing census/Gate-D machinery
selects, add a real antisymmetric skew term tied to that support:
`𝔾[Θ]:=L[w]+A[a]`, `A[a]:=Σ_{e∈E}a_e A_e` (`A_e:=e_ie_j^T−e_je_i^T`), `a_e≡0` off
support by construction — concretely instantiating the corpus's own
`𝔾^(+)+𝔾^(-)` split for the first time. Extended living system (same declared regime
`a=−1,b=1,K=μ=1,J=0`): reader feels `+A`, record feels `−A` (literal transpose,
`𝔾[Θ]^T=L−A`, no complexification). `J_Theta(C)` := the ordered cyclic product of
`a_e*` around an independent cycle lying entirely within `E`.

**Th_coqc (7 lemmas/theorems, axiom-free, independently `Print Assumptions`-confirmed
by two reviewers):** `qsign_exists`; `cyclic_product_switching_invariant_triangle`/`_C4`
(Z2 vertex switching leaves the ordered cyclic product of `a_e` around K3/C4 exactly
invariant); `tree_gauge_fixable_P3`/`_star3`/`_P4`/`_star4` (the switching group gauges
every tree edge's `a_e≥0`). Scope honestly stated: concrete instances only — the general
finite-n-cycle statement and the general structural-induction tree lemma are both
declared `[Open]` in-file.

**finite_diagnostic (floats disclosed, fixed seeds 550/551/552, reviewer-confirmed
robust across 3 independent seed triples), the decisive re-check under the EXTENDED
`(L+A)`-coupled dynamics:**
- **K3 (n=3): 0/3000 living hits** — a strengthened bounded negative on top of
  5.2b-1's 0/3000 + review's 0/25000+homotopy (which were SYMMETRIC-ONLY dynamics,
  never before re-checked under the genuinely different extended system).
- **C4 (n=4): 101/3000 hits, 33 distinct living FPs, `J_Theta≠0`** — the FIRST
  root-native nonzero orientation-odd invariant found at a living fixed point in the
  program. Full magnitude spread, disclosed as mandatory (not just the largest
  values): `2.583e-14 (×8), 1.036e-05 (×6), 2.170e-05 (×7), 1.089e-03 (×8),
  4.544e-03 (×4)` — min 2.583e-14, max 4.544e-03. The near-zero cluster (8/33 FPs,
  ≈2.6e-14) sits within ~3 orders of magnitude of this support's worst Newton
  residual (8.7e-14), but a reviewer's post hoc 60-digit mpmath re-solve (residual
  ~3e-62) plus a Jacobian condition-number check (8.3, well-conditioned) confirmed it
  is a genuine, isolated, reproducible nonzero fixed point, not float noise — its
  rigorous exact-arithmetic distinction from a hypothetical exact-zero branch stays
  `[Open]`.
- **P3 control (n=3, tree): 577/3000 hits, 26 distinct FPs, `J_Theta` UNDEFINED**
  (no cycle in the support) — exactly as the tree-triviality lemma predicts.
- **Traversal-sign note:** `J_Theta`'s sign (not its nonzero-ness) flips under
  reversed traversal on the ODD cycle K3 but not on the EVEN cycle C4 — the general
  `(−1)^m` telescoping fact, matching the orchestrator ruling's own "orientation-odd" phrase.

**B1/B2 transfer to the extended system (orchestrator ruling's mandatory sub-task, exact
Fraction + paper derivation, `Dr`, numerically re-confirmed at all 59 found living FPs,
worst `|⟨Φ³,Ψ⟩|=5.42e-14`):** **B1** (`⟨Φ³,Ψ⟩=0`) transfers UNCONDITIONALLY — the
scalar-transpose identity `Ψ^T G Φ=Φ^T G^T Ψ` holds for ANY `G`, symmetric or not.
**B2** (symmetry is dead) also transfers, via a genuinely NEW mechanism: the skew
source vanishes identically at `Ψ=cΦ` for any `c`, forcing `A[a]=0` there and
collapsing to the symmetric case where the OLD proof applies verbatim — but the old
"graph term cancels" argument (which relied on `G=G^T` identically) does NOT survive
verbatim in the extended system, disclosed explicitly rather than silently inherited.

**The verdict, carefully fenced:** 5.4's missing ingredient IS root-realizable — a
living oriented fixed point CAN retain a nonzero orientation-odd real cyclic invariant
(YES at n=4/C4; n=3 stays NO within this bounded search, K3 dead). **Item 2 REMAINS
`[Open]`**: the identification square between this real `J_Theta` and 5.4's complex
`Cq` quartet-`J` is UNBUILT and is now the named next gate — Q3 identity-by-role
holds, CRRC guard binding throughout (grepped clean in both files; no
generation/CKM/color identification anywhere outside guard-disclaimer comments).

**What Attempt 5 does NOT establish:** any identification of `J_Theta` with 5.4's
complex CP-quartet invariant (the square is unbuilt); any value or bound on generation
count; that the near-zero C4 cluster is distinct from a possible exact-zero branch at
exact-arithmetic rigor; that `J_Theta`'s gauge invariance holds under anything beyond
Z2 sign-flips; stability of any C4 living FP (only static existence checked). Named
next steps: the quartetJ identification square (now the single most valuable named
open item of the whole Theta program); the 5.6 untied-reframing candidate (deferred,
not pursued); exact algebraic certification of the C4 living FPs; general finite-n-cycle
and general-tree-structural-induction Coq lemmas; full continuous gauge invariance.

## Attempt 6 — `theta_quartet_square_v1.py` + `formal/InfoThetaQuartetSquareObstruction_attempt.v`, 2026-08-09: the quartet-square identification is OBSTRUCTED for every embedding examined

Built per Attempt 5/`THETA_ROOT_PROGRAM.md` §5.5's own named next gate: the
identification square between 5.5's real `J_Theta` and 5.4's complex `Cq` quartet-`J`
(`real_quartet_no_cp_readout`'s obstruction). Item-2 side, this is **Theta 5.7** in the
Theta-root-program line (see [`THETA_ROOT_PROGRAM.md`](THETA_ROOT_PROGRAM.md) §5.7 for
the full construction; §5.6 stays reserved by 5.5's own text for the deferred untied
enlarged-census reframing candidate, not this square).

**Design provenance (multi-agent, disclosed):** a 3-route design workflow produced a
combinatorial/holonomy bridge (Route R2, primary), a spectral eigenbasis bridge (Route
R1), and a role-axiom square (Route R3); three independent adversarial judge lenses,
each doing its own from-scratch re-derivation, converged on ranking R2 > R1 > R3 and
verdict OBSTRUCTED for all three. One judge lens caught a genuine mechanism error in
R1's own gauge-bridge refutation (it tested the symmetric source `s_e` when the load-
bearing bilinear is the skew source `t_e`) — corrected and disclosed, per this
program's own house convention of naming caught mistakes rather than silently fixing
them. Orchestrator ruling: PRIMARY = Route R2 (Family A/B/C `Cq` embeddings), R1's
corrected diagnostics and R3's parity/rescaling content grafted in as supporting
material, not filed as separate artifacts; the triple-convergent rescaling lemma filed
ONCE. Implementation was checked by two independent adversarial reviews (verdicts
RELEASABLE-AFTER-FIXES and RELEASABLE) plus one repair pass that applied two
confirmed MINOR documentation-level findings (a cross-file C4 edge-quartet
pairing-convention disclosure; an eigen-ordering-convention-redundancy disclosure) —
no theorem or numeric result was changed by the repair.

**Construction:** three combinatorial embeddings into `Cq := Q×Q` tested against
`quartetJ(V) := Im(V_01·V_12·conj(V_02)·conj(V_11))` on the same `𝔾[Θ]=L[w]+A[a]`
architecture 5.5 builds: **Family A** (`z_e:=w_e*+i·a_e*`, both sectors), **Family B**
(`z_e:=i·a_e*`, skew-only, the unique gauge-clean embedding), **Family C**
(`N_ij:=conj(Z_i)·Z_j`, the vertex-phase Gram/rank-1 embedding — the `omega`/doubled-
real-space complex-structure lever the task named).

**Th_coqc (14 theorems, axiom-free, independently `Print Assumptions`-confirmed by two
reviewers plus a fresh post-repair recompile):** headline eight —
`quartet_rescale_invariant` (the ONE shared triple-convergent rescaling lemma, filed
once), `family_B_K3_exact`, `family_B_C4_vanishes`, `family_C_rank1_vanishes`,
`family_A_not_switching_invariant`, `skew_source_switching_covariant`,
`symmetric_source_not_switching_covariant`, `c4_reversal_is_gauge_witness` +
`k3_no_uniform_reversal_gauge`. Five supporting companion-witness/variant theorems
round out the 14. General-n cycle/tree statements stay `[Open]`.

**The corrected gauge mechanism (house-style disclosed correction):** `t_e :=
Phi_i·Psi_j−Phi_j·Psi_i` (sources `a_e*`) is EXACTLY `D_i·D_j`-covariant under vertex
switching for ANY `D` (`Th_coqc`, unconditional) — the skew sector is fully dynamically
gauge-compatible. `s_e := (Phi_i−Phi_j)(Psi_i−Psi_j)` (sources `w_e*`) is NOT (`Th_coqc`
witness: `s'=21` vs. the naive prediction `−1`) — the symmetric sector breaks gauge-
compatibility. Only Family B is dynamically gauge-clean.

**The verdict — OBSTRUCTED for every embedding family examined, by three
mutually-reinforcing mechanisms:**
1. **Gauge split** (Th_coqc): only the skew/`a_e` sector is dynamically
   gauge-compatible with the real-side `Z2^{|V|}` switching group.
2. **Parity** (Th_coqc): Family B reproduces `J_Theta` EXACTLY on K3
   (`Im(P)=a1·a2·a3`) but VANISHES IDENTICALLY on C4 (`i^4=1` parity fact). K3 is dead
   (THREE disclosed independent search efforts: 0/3000 + 0/25000+homotopy + 0/3000
   extended); C4 is the program's only living witness (33 distinct FPs, 5.5) — Family B
   is nonzero exactly where nothing lives, zero exactly at the living witness.
3. **Eigenbasis non-well-posedness** (finite_diagnostic + Dr): `V_cand:=V_A^{-1}·V_B`
   is not well-posed — a fresh sweep (seed 551, this run's own measurement) finds
   29/528 sector pairs flip `quartetJ`'s sign across four eigen-ordering conventions
   (robust across two extra reviewer seeds: 20/561, 23/561), magnitudes span `~1461x`,
   non-normality residual `≥0.416` and non-unitarity residual `≥0.807` at all 33 living
   FPs; plus a weakest-leg, explicitly-flagged `Dr` Galois-genericity argument that
   eigenvalues generically leave `Q(i)`.

**Positive byproducts, disclosed:** `quartet_rescale_invariant` — independently derived
by all three design routes, filed once, the one reusable general lemma this square
produces. Family C's general rank-1 vanishing CLOSES, negatively and permanently, the
`omega`/doubled-space complex-structure lever the task named — no future attempt should
believe it untried. The corrected `t_e`/`s_e` mechanism is recorded as this program's
house-style disclosed correction.

**Disclosures (mandatory):** the python file and the Coq file use DIFFERENT C4
edge-quartet pairing conventions for Family A/B (python: adjacent-edge split; Coq:
opposite-edge split) — TWO INDEPENDENT WITNESSES of the same qualitative
gauge-dependence conclusion, not cross-file numeric corroboration of one number.
Eigen-ordering convention #4 is analytically redundant with convention #1 (guaranteed
equal by `quartet_rescale_invariant`) — a live sanity check, not a 4th independent
test; effective independent conventions = 3, not 4. The 29/528 count is
this-run/this-platform; qualitative existence of conflict is the claim.

**What Attempt 6 does NOT establish:** any resolution of item 2's `[Open]` status
(stays an orchestrator/founder-level call outside this square's scope, per orchestrator
ruling 7); any generation/CKM identification anywhere (CRRC guard, grepped clean); that
the eigenbasis bridge is a validated `J` readout (it stays FORBIDDEN — used here purely
diagnostically to refute its own well-posedness, the compliant carve-out per orchestrator
ruling 1). Named next steps (unchanged, inherited): exact Groebner-basis/minimal-
polynomial certification of a C4 living FP's exact eigenvalue field; the nonlinear
(non-affine) embedding family; the qualitative/inequality-relation escape hatch; feeding
`G`'s actual eigenvalues into the R2 holonomy machinery; general finite-n-cycle and
general structural-induction tree Coq lemmas; the near-zero C4 cluster's rigorous
exact-arithmetic distinction from a possible exact-zero branch; stability of the C4
living FPs; full continuous gauge invariance beyond Z2 sign-flips.

## Honest status

- Item 2 (generation multiplicity): **`[Open]`, unchanged at `Th_coqc`/`Dr` tier.** No from-root
  derivation exists. What DOES now exist: a `fit_calibrated`, minimal-free-parameter, explicitly
  caveated construction (Attempt 2) that reproduces `N=3`, consistent-with (not forced-by) the
  observed value, per `DRIFT_CONTRACT.json` DEV-SM-002.
- Zeroth-order scope-gap finding: `Dr` tier (confirmed by independent adversarial review,
  verdict SURVIVES WITH CORRECTION, correction applied above), not a physics claim.
- Attempt 1 (`item2_family_index_v1.py`): `Dr` tier, negative/scope-narrowing result (confirmed
  by independent adversarial review, verdict SURVIVES WITH CORRECTION, both corrections applied
  above), not a physics claim. The `ℂ^N` family-slot ansatz it uses is explicitly flagged as
  imported motivation, not a derived/earned structure.
- Attempt 2 (`item2_family_index_v2_fit.py`): `fit_calibrated` tier per DEV-SM-002 (confirmed by
  independent adversarial review, verdict SURVIVES WITH CORRECTION, all three corrections
  applied above). `N=3`, consistent-with observation, NOT derived, NOT forced.
- Attempt 3 (`item2_cp_equivariant_lower_bound_v3.py` +
  `formal/InfoCPEquivariantGenerationBound_attempt.v`): CONDITIONAL mechanism tier — the
  mechanism itself is exact/machine-checked (axiom-free Coq), the conclusion `N≥3` is
  conditional on a declared empirical premise, and the whole construction sits on imported
  (non-root) structure, disclosed in-file. Does not change item 2's `[Open]` status at the
  unconditional/root level; does not establish `N=3` exactly.
- Nothing here touches `CLAIM_BOUNDARY.json` or any `run_tests.py` verifier — these are
  exploratory files, not wired into the domain's closed-claim registry.
