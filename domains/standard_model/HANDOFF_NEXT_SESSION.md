<!-- Durable handoff for the Standard-Model arc. Committed to git so it survives a closed
     terminal / a fresh Claude session — read this FIRST before touching domains/standard_model. -->

# HANDOFF — Standard Model arc, resume point (as of v1.13, 2026-07-22; session log 2026-07-24)

## 0.-3 CURRENT RESUME POINT (2026-08-09 — supersedes §0.-1 below for item 2)

**§0.-1's "item 2 is virgin territory" is STALE.** Item 2 now has 4 attempts and a whole
root-native program behind it. Read, in order:
1. [`item2_exploration/THETA_ROOT_PROGRAM.md`](item2_exploration/THETA_ROOT_PROGRAM.md) —
   the Θ root program (founder ruling `DEC-theta-new-root-2026-0808` + erratum row):
   steps 5.1 → 5.4 ALL DONE (2026-08-08/09), each independently adversarially reviewed
   before commit, mirrored byte-identically to `research_universal_solver`.
2. [`item2_exploration/ITEM2_EXPLORATION_LOG.md`](item2_exploration/ITEM2_EXPLORATION_LOG.md)
   — Attempts 1–4 (Attempt 3 = CP-conditional N≥3 machine-checked; Attempt 4 = the 5.4
   admissibility square, half-closed with a proven real-mixing obstruction).

**State in one paragraph:** Θ (living geometry) is a root by founder ruling. Proven
(`Th_coqc`, all axiom-free): Θ's deformation directions = edges (5.1); family topology =
reader↔record discordance readout (5.2a); at closed static fixed points the balance
`⟨Φ³,Ψ⟩=0` is forced and both `Ψ=±Φ` are dead (5.2b-1); **n=2 admits NO living fixed
point — root-native N≥3** (5.2b-2, 7 theorems, confirmed by reviewer's Gröbner even over
ℂ); a real mixing matrix retains no CP-signed readout (5.4 obstruction). Measured
(`finite_diagnostic`): n=3 lives on path supports only (≥2 orbits); n=4 lives more
broadly (disclosed); living-sector eigenbasis mismatch gives real mixing angles
(|V₁₁|=½) but the phase slot is structurally empty. Item 2 remains `[Open]` — but is now
reduced to ONE sharp question (todo #1 below).

**TODO LIST (handed off, priority order):**
1. ~~**Step 5.5 — Oriented Θ (THE gate)**~~ — **DONE 2026-08-09** (see
   `item2_exploration/THETA_ROOT_PROGRAM.md` §5.5 + `ITEM2_EXPLORATION_LOG.md` Attempt 5;
   files `theta_oriented_skew_v1.py` + `formal/InfoThetaOrientedSkewObstruction_attempt.v`,
   7 lemmas axiom-free). Outcome: YES at n=4 — C4 admits living fixed points with
   `J_Θ ≠ 0` (`finite_diagnostic`, first root-native nonzero orientation-odd invariant
   at a living configuration); K3 (n=3) stays dead under the extended dynamics
   (strengthened bounded negative). Item 2 remains `[Open]`: the real-`J_Θ` ↔
   Cq-`quartetJ` identification square is UNBUILT and is now THE gate (new todo #0).
0. ~~**Build the `J_Θ` ↔ `quartetJ` identification square**~~ — **DONE 2026-08-09,
   verdict OBSTRUCTED** (§5.7 in `item2_exploration/THETA_ROOT_PROGRAM.md` + Attempt 6
   in the log; files `theta_quartet_square_v1.py` +
   `formal/InfoThetaQuartetSquareObstruction_attempt.v`, 14 theorems axiom-free).
   Three converging mechanisms: only the skew/`a_e` sector is switching-covariant
   (`t_e` yes / `s_e` no, both machine-checked); the unique gauge-clean embedding
   `z_e = i·a_e` vanishes identically on C4 (the living witness) and is nonzero only on
   dead K3; the eigenbasis bridge is not well-posed (ordering flips sign; eigenvalues
   generically leave ℚ(i) — Dr). Positive byproducts: `quartet_rescale_invariant`
   (shared lemma), Family-C rank-1 vanishing closes the ω/doubled-space lever
   NEGATIVELY (permanently — do not re-try it). Item 2 stays `[Open]` — the status
   call is a founder/orchestrator decision outside the square. **Named escape hatches
   (the new top candidates):** Gröbner/minimal-polynomial certification of a C4 living
   FP's exact eigenvalue field; nonlinear (non-affine) embedding family; qualitative/
   inequality-relation route; feeding `𝔾`'s eigenvalues into the holonomy machinery;
   5.6 untied-reframing candidate (still reserved); exact certification of C4 FPs;
   near-zero-cluster exact distinction; general-n Coq lemmas; stability analysis.
   **Downstream work (2026-08-09):** the field-certification, transient-selection, and
   orientation-sign theorem steps (5.8–5.10) that followed this square are recorded in
   `item2_exploration/THETA_ROOT_PROGRAM.md` §5.8–§5.10 and cross-referenced (not given
   a new Attempt number) in `ITEM2_EXPLORATION_LOG.md`; item 2 remains `[Open]`.
2. ~~**Stability of the living fixed points**~~ — **CLOSED NEGATIVELY at the declared
   regimes, 2026-08-09** (`item2_exploration/THETA_ROOT_PROGRAM.md` §5.9;
   `theta_transient_selection_v1.py`, 8/8 checks PASS, independently reproduced by both
   reviewers incl. extra seeds). The corpus's own Gauss-Jordan reader(`+D`)/record(`−D`)
   stepper, regime `a=−1,b=1,K=μ=1,M=1`, `D` in `{0.5,1.0,2.0}` plus a `D=0` control plus
   extra seeds: **100% DIVERGED** — every C4 living FP is dynamically UNSTABLE at this
   regime (DT-independent physical divergence time, ~11–15 time units, not a stepper
   artifact). "Exactly 3 is stable" does **not** hold at these regimes; the Bateman
   anti-damped-record concern flagged above was the right thing to worry about. Scope
   caveat (binding): this closes stability ONLY at the declared parameter regime, not
   for all possible `(a,b,K,μ,D)`; other regimes remain untested. A NEW static fact
   surfaced by the same file: all 33/33 living C4 FPs have `sign(J_Θ)=+`, which seeded
   step 5.10 (see `THETA_ROOT_PROGRAM.md` §5.10 — the "living ⇒ J_Θ > 0" theorem
   program). Named next targets:
   - **Lemma 2/Lemma 3 closure routes** (5.10, `THETA_ROOT_PROGRAM.md` §5.10): a
     dedicated 60-minute round-3 compute campaign (idm Buchberger, sympy grevlex,
     resultant cascade, GF(p) probes) left both `[Open]` at declared budgets
     (120s/300s/600s/900s/1200s/1500s tried). Next attempt should try
     resultant+gcd-splitting on the now-derived exact `T(x,p,q)` relation, msolve-class
     (Groebner-over-finite-field-with-lifting) tooling if available, or a materially
     larger declared budget.
   - The hand-checked-only `Phi0=0` (resp. `Phi2=0`) sub-case from the round-3
     factorization needs an exhaustive computer check, not just a hand substitution.
   - **IDM backlog pointer:** no dedicated multivariate-resultant/variable-elimination
     `kind` exists in `idm`'s 269-kind catalogue (checked this round, per §5.10) — a
     real product gap surfaced by this campaign, named here for whoever next extends
     `idm`.
3. **Step 5.3 — Coq hygiene:** matrix-level objects (replace entrywise transliteration),
   general-n census theorem, `Coq.Reals` (+ℝ flag) restatement of the n=2 theorem.
4. **Exact algebraic certification of the living FPs** (symbolic solve timed out twice —
   minimal polynomials open; the uniform-star orbit looks most tractable).
5. **K3 nonexistence proof** (currently a bounded negative: 3000+25000 trials +
   failed homotopy continuation, not a theorem).
6. **Push both repos to remotes** — every commit in this arc passed the adversarial
   gate; push itself awaits founder go (commits: readout_genesis `9c921d4`→`710b09b`,
   research_universal_solver `bc1e91c`→`7cfb64b`).
7. **Fix `cpg` DECISIONS.yaml strict-YAML breakage** (pre-existing, line ~1875; the
   anse_sync loader returns `[]` for decisions — the theta rows are appended in current
   convention but nothing materializes).
8. **Fix twin-repo `make verify-attempts` PRE-EXISTING failures** (discovered 2026-08-09
   during 5.5's one-time full-arc audit): `InfoThetaEdgeCensus_attempt.v` and
   `InfoThetaFixedPointBalance_attempt.v` fail the audit's `Hypothesis` source scan —
   both files byte-identical to HEAD, so the failure pre-dates 5.5 (the scanner was
   evidently extended after those commits); either discharge/restate the section
   hypotheses or scope the scanner, then re-run the audit once. NOT caused by 5.5
   (`InfoThetaOrientedSkewObstruction_attempt.v` scans clean and passes).

**DO NOT (binding, unchanged):** reuse the color `k=3` cyclic argument for generations
(CRRC); identify spectral levels / slots / edge counts with generations without building
the admissibility square (Q3 identity-by-role); inject continuum knobs (discrete-only,
`CONTINUUM_ARC_ERROR_NOTE.md` lessons 1+5 — the census excludes only the index-continuum
half); commit anything without an independent adversarial review pass; edit
`domains/standard_model/` in one repo only (always mirror both, verify `diff -q`).

## 0.-2 READ FIRST, EVEN BEFORE 0.-1: check for a broader "closing the SM" framework before citing status

This session's canonical (private) twin repo caught and fixed a real gap: this domain's whole
item1-35 exploration ran for a full session without checking whether a broader, pre-existing
"express the SM in minimal master equations + empirical residue" framework already existed
elsewhere in the private canonical repo. This public repo does not carry that broader framework
(it is private), but the LESSON generalizes: before citing "the SM is open/closed" from this
domain alone, check whether a fresh session already reconciled the two views in the canonical
repo, and prefer that reconciliation's framing. One concrete, self-caught error from that
reconciliation, already fixed here: `item25_exploration/beta_function_coefficients_v1.py`
originally overclaimed being "the first runnable artifact" for its beta-function coefficients;
corrected in that file to a narrower, accurate claim (see its own honest fence).

## 0.-1 START HERE if you are the fresh session after 2026-07-24's marathon

**The single next task, decided at the end of a very long 2026-07-24 session: attempt item 2,
generation multiplicity (why exactly 3).** Confirmed that session, by direct grep across every
`.md` file in this domain and `docs/engineering/GENESIS_STEP_BY_STEP_V3_1.md`: item 2 is
**genuine virgin territory** — `ROOT_TO_SM_DAG.md` line 77 says plainly `generations (repeated
classes) + mixing ... 🟥 (count NOT derived)`, and `blind_matter_search_v1_6.py`'s own honest
fence lists "generation count" as explicitly out of its scope. There is no partial work, no
buried hint, no existing construction to extend — this needs a genuinely new, from-scratch
argument, built with the same rigor as everything below (read §0.0 next), not a re-reading of
existing text.

**Why this is the highest-leverage starting point right now (not item 1):** a real, external
event on 2026-07-24 (CMS's most-precise-to-date CP-violation measurement in `B⁰ₛ→J/ψK⁰`, matches
the Standard Model exactly) sits at item 24 on this backlog, chaining back through items 21-23 to
items 1, 2, 18. The Kobayashi-Maskawa mechanism requires **≥3 generations** for a CKM matrix to
carry a physical complex phase AT ALL — below 3, this class of CP violation is mathematically
impossible, not merely unmeasured. So item 2 is the deepest root prerequisite for that entire
downstream chain, more foundational than previously scoped. See the 2026-07-24 entries under
item 2 (§2, P0) and item 1 (§2, P0) below for the full chain of reasoning.

**Before attempting anything on item 2, read `item1_exploration/ITEM1_EXPLORATION_LOG.md` in
full.** It documents 9 real attempts at item 1 that same day (4 derivation attempts adversarially
REFUTED, 1 openly-declared fit that passed, 3 further probes mixed/negative, 1 infrastructure
fix) and names TWO reusable diagnostic tools that will very likely bite again on item 2:
- **Cross-Role Readout Contamination**: re-using a readout established for one question as if it
  answers a different one (a sign formula read as a cost formula, etc.) — the #1 way today's item
  1 attempts failed. Item 2 will be tempting to attack by analogy to `SM_INFORMATION_PHILOSOPHY_
  MASTER.md` §2.2's `k=3` color argument (same numeral, "3") — **do not** reuse that argument for
  generations without independently building and checking the admissibility square; that specific
  temptation is exactly what CRRC is named after.
- **Retained-Degree Insufficiency**: asking a readout to resolve more independently-distinguishable
  answers than the structure it's read from actually retains (collapses, is underdetermined, or is
  circular). Before proposing any construction for "why 3 generations," count how many genuine
  independent degrees of freedom that construction's own retained structure carries, and check it
  is actually ≥3-valued, not just "3" by assertion.

**Also useful, not required:** `DRIFT_CONTRACT.json`'s `DEV-SM-001` (declared, tagged FIT is
allowed as a parallel, secondary, OPTIONAL track — never a substitute for derivation) and
`fit_calibrated_registry.py` (shared PDG/EW constants, reusable, avoid re-typing literals) are
both available if a fit-tier probe on item 2 becomes useful — but derivation is still the primary
goal for item 2, exactly as it was for item 1.

**Process reminder** (this is what caught 2 near-misses on 2026-07-24, including one inside the
CRRC finding itself while it was being written): independently adversarially review anything
before committing to git, even Dr-tier documentation — a "sounds right when I write it" pass is
not sufficient, spawn a separate reviewer with instructions to actively try to refute the claim.

## 0. How to resume in one paragraph
Read `INDEX.md` (version timeline) and `STANDARD_MODEL_CLOSURE.md` (current node-level status
matrix) first — they are the source of truth, not this file's prose. This file's job is the
**priority-ordered open-items backlog** (§2 below, 34 items reviewed 2026-07-22, +1 exploratory item added 2026-07-24) and the **exact
next step** (§1). Everything here was reviewed for continued relevance on 2026-07-22 — nothing was
found obsolete; the discipline (`Th_coqc` / tier-honest / no overclaim) still applies to every new
result. Read `[[readout-not-truth]]` skill and `SM_INFORMATION_PHILOSOPHY_MASTER.md` before writing
any new claim.

## 1. The single next step (founder-locked, highest leverage)
The founder's own roadmap after v1.13 (the letter that shipped the intertwiner-counting correction)
named two next versions explicitly:
- **v1.14 — Physical Order-Spectrum Audit**: compute the microscopic intertwiner-cost parameters
  `g_j, Δ_j, κ_j, α, β` (equivalently, in v1.13's cleaner form: `λ_j = e^{−Δ_j^eff}`) from the actual
  tape/closure grammar — NOT fit to any physical mass — to test whether `Π₀ = 3λ_U+3λ_D+λ_E > α` is
  **FORCED** by the root, or merely one possible regime. This is the same underlying task as closing
  item §2.13 (`⟨Ξ⟩≠0` from an action) and §2.15 (the primitive cost ratios behind v1.11's isotropy) —
  **all three reduce to "derive the primitive rewrite-cost functional from `S_UF`"**. Solving one
  well may substantially inform the other two; consider them as one research thread, not three.
  **2026-07-24 exploration (`item1_exploration/ITEM1_EXPLORATION_LOG.md`):** four independent
  attempts at `Δ_j`/`α` this session were all adversarially REFUTED (read the log before
  re-attempting — it names the exact flaw in each). The exploration converged on one useful
  diagnostic (a named failure mode, "Cross-Role Readout Contamination" — reusing a readout
  established for one question as if it answered a different one) and one honest re-identification:
  the "price per elementary retained-distinction transition" this item is chasing is `M_n`, the
  `Φ↔Ψ` exchange rate in II.8a's own DRL action — the SAME quantity `READOUT_GENESIS_CORE.md`
  §II.6 already flags as "POSITED, not derived" after 8 independent failed attempts. Item 1 is
  therefore not a smaller, SM-local problem — it is the master equation's own oldest open
  question, met again here. Still fully `[Open]` in the DERIVATION sense.

  **2026-07-25 exploration (`item1_exploration/retained_transition_operational_closure/`,
  `primitive_branch_parameter_reduction/`, `order_vacuum_threshold_closure/`,
  `native_vacuum_amplitude_closure/`, `rd_to_gev_fit_calibrated_bridge/`,
  `mass_ratio_test_no_fit/`, `native_causal_memory_consistency/` — full narrative in
  `ITEM1_EXPLORATION_LOG.md`, read that file for the complete story, this is only the pointer):**
  `M_n` was CALIBRATED (not derived) via a noise-aware operational estimator (moment-correction +
  replicate-IV), independently reviewed, merged to `main` in both this repo and
  `research_universal_solver`. The chain was then extended, each step independently reviewed and
  merged: declared U/D/E branch tapes → `Pi0=6.328453553357985` → order-vacuum criterion
  `Pi0>alpha_order` (inherited from the mother potential, not a new dial) → `ORDERED_READY`,
  `r_star=3.823356105009073` → native vacuum amplitude
  `v_native=sqrt(2*r_star)=2.7652689218262565`. **All of this is MERGED to `main`, usable,
  tier-tagged `fit_calibrated`/`declared_finite_architecture`/`finite_diagnostic`.**

  **Two required disclosures on the merged chain, both already applied, read before citing
  `Pi0`/`ORDERED_READY` anywhere:** (1) the U/D/E branch initial conditions are explicitly
  arbitrary/uncalibrated (checked — no PR in either repo derives them); (2) `ORDERED_READY` on
  this specific stepper is STRUCTURALLY GUARANTEED regardless of branch data (`alpha_order=-0.5`
  sits below `Pi0`'s unconditional lower bound of 0) — this was found by an independent
  scientific-methodology review and is disclosed in the merged code's own `claim_boundary`.

  **Three further candidates, all DRAFT/UNMERGED, testing whether any of this matches real
  physics** (this repo's PR #79, #80, #81; mirrored, unmerged, in `research_universal_solver`):
  fitting a RD-to-GeV scale from `v=246 GeV` and independently predicting the Higgs mass —
  **FAILS**, 74% error; the same test with ZERO fitted parameters via a mass ratio — **FAILS**,
  identical 74% (an algebraic consequence, not new evidence); an internal (zero-external-input)
  consistency check between two independently-derived native "mass" readouts (`tau_c=M/D`-based
  vs curvature-based) — **NOT CONSISTENT**, 94% deviation. All three honestly disclosed, not
  hidden, not merged. A founder-initiated side-investigation into a discrete-vs-apparent-continuum
  bridge found a real, pre-existing, Th_coqc, `tau_c`-parametrized bridge
  (`docs/root/PERSISTENT_WALK_TELEGRAPH_DERIVATION.md` in `research_universal_solver`) —
  structural only (same equation form), no numeric GeV conversion, partially discharged — and an
  unresolved internal tension between two of this project's own philosophy docs
  (`ZERO_INFINITY_DUAL_DIAGNOSIS.md`'s readout-vs-readout STANDING GUARD vs. this project's own
  routine use of PDG masses as `fit_calibrated` inputs elsewhere) that this session explicitly did
  NOT resolve — flagged, not papered over. **Paused here by explicit founder instruction.** Item 1
  remains fully `[Open]` in the root-DERIVATION sense; the OPERATIONAL-CALCULATION question for
  `M_n` itself is closed (merged, usable); matching real Higgs-sector physics from this
  construction is, so far, a disclosed failure on every route tried.
- **v1.15 — Generation Multiplicity**: derive why there are (if there are) exactly 3 generations,
  without feeding the count.
Root-debt track (parallel, independent): **SM-G0.1–G0.5** (§2 items 1–5) — closing these is
architecturally prerequisite to ever calling ANY of v1.5–v1.13's results root-derived rather than
"exact within a declared architecture." Neither track blocks the other; pick based on what the
founder wants to see next.

## 2. Full open-items backlog (34 items reviewed 2026-07-22 + item 35 added 2026-07-24 — all still necessary)
Grouped by priority. "Still necessary?" was checked against the current merged state of both repos
(`main`, both at the same commit as of this handoff) — none were found stale or already closed.

### P0 — founder-named next steps (do these first)
1. **Derive `g_j, Δ_j, κ_j` (or `λ_j`) from the tape/intertwiner grammar** — the v1.14 Physical
   Order-Spectrum Audit. Tests whether `Π₀>α` (v1.13) is forced. *Still necessary: YES — this is the
   sharpest, most recently-opened frontier; v1.13's own honest fence names it explicitly.*
2. **Generation multiplicity** — why 3 (or is it derived at all)? v1.15. *Still necessary: YES —
   completely untouched; §8 of the closure ledger is 100% open.* **External context (2026-07-24):**
   CMS's most-precise-to-date CP-violation measurement in `B⁰ₛ→J/ψK⁰` (real experiment, matches SM
   exactly, no new physics found — [home.cern, 2026-07-24]) is item 24 (CP violation) on this same
   backlog, which needs items 21-23 → 1, 2, 18. The mathematical reason this item is the true root
   prerequisite for that whole downstream chain: the Kobayashi-Maskawa mechanism requires **≥3
   generations** for a CKM matrix to carry a physical, non-rotatable-away complex phase at all — with
   2 generations CP violation of this kind is impossible outright, not just unmeasured. So item 2 is
   not only "why 3" in the abstract; it is the specific root-level fact that must close before this
   entire class of real, currently-being-measured phenomena is even reachable from the root. Logged,
   not attempted — item 2 remains exactly as open as before this note.

### P1 — root-debt track (SM-G0, architecturally foundational)
3-7. ~~G0.1–G0.5 (path composition, `Aut(F,O)` closure, localization, connection transformation,
   holonomy invariant)~~ — **RESOLVED, items 3-7 STALE as of 2026-07-24 (audited this session).**
   All 6 structural sub-gates (G0.1–G0.6) are closed as unconditional `Th_coqc` Coq witnesses:
   `InfoGaugeAutomorphismGroup.v` (G0.1/G0.2, closed 2026-07-23 commit `92eb769`) and
   `InfoGaugeLocalizationConnectionHolonomy.v` (G0.3/G0.4/G0.5, closed 2026-07-24 commit
   `90cefb6`) — see `CLAIM_BOUNDARY.json` keys `sm_g0_1_g0_2_automorphism_group` and
   `sm_g0_3_g0_4_g0_5_localization_connection_holonomy`, and `SM_INFORMATION_PHILOSOPHY_MASTER.md`
   §21. Re-verified this session by a fresh, independent `coqc -q` compile of both current `.v`
   files (clean, exit 0, every `Print Assumptions` call reports "Closed under the global
   context" — axiom-free). These items were left un-updated across four later same-day edits to
   this file (`997484d`, `5aeb94c`, `e69c778`, `af81167`, all 2026-07-24) — staleness by omission,
   not active re-affirmation; this line's own prior "`CLAIM_BOUNDARY.json` still says 'SM-G0 not
   yet built'" claim was already false against current file content (that string no longer exists
   anywhere in `CLAIM_BOUNDARY.json`) and is corrected here. **Scope caveat, unchanged from both
   source-of-truth files' own hedge**: this is a STRUCTURAL closure only ("for arbitrary
   `(S,R,F,O)`" / "for ANY group `(G,id,mul,inv)`") — it does NOT show `Aut(F,O)`, the frame
   connection, or holonomy are non-trivial for this project's actual root dynamics; that remains
   open. (Numbering note, also pre-existing: §1 above calls this "items 1–5"; the actual §2
   numbering is items 3–7, corrected here, not renumbered to avoid breaking other cross-refs.)
8. AP20 borrow #3 — self-carrier closure (still fully borrowed)
9. AP20 borrow #4 — the common quadratic load A4 (still fully borrowed)
   *Still necessary: YES — `c_self/c_geo=1` is still not root-derived. (Confirmed still accurate
   in the same 2026-07-24 audit that resolved items 3-7 — `CLAIM_BOUNDARY.json`'s
   `not_established` list still carries these as "still fully borrowed".)*

### P1 — structural prerequisites (each blocks a cluster of P2 items below)
10. 4D correlation defect `ε_t(b)` — the full block kernel `K_b`, `ρ_t^full(b)` for `b=2` from the
    real action (confinement §2's "sharpened wall" — a finite integral, not a debate)
11. Nonzero continuum string tension `σ_phys` (confinement, §2)
12. Uniqueness of the matter skeleton over ALL representations, not just the declared minimal
    alphabet `{1,3,3̄}×{1,2}` (§3; v1.6 only closed the minimal-alphabet case)
13. `⟨Ξ⟩≠0` derived from the unified action (§4; v1.7's chirality grading is exact, but weak
    *selection* is conditional on this)
14. Interacting chiral gauge measure / anomaly coefficients from the actual oriented
    determinant/Jacobian (§4)
15. The primitive cost ratios `κ_ord, κ_inc, κ_rel, κ_cut` behind v1.10–v1.11's isotropic fixed
    point — derive from `S_UF` (§5; note the overlap with item 1 — same underlying task)
16. Uniform spectral gap as volume/block-scale → ∞ (§5, "does the gap survive thermodynamic limit")
17. Full interacting Lorentz continuum: boosts, scattering covariance, microcausality — beyond the
    Euclidean 4-channel isotropy + dispersion shadow v1.9–v1.11 actually closed (§5)
18. Physical scalar (Higgs) mass from real microscopic parameters, once item 1 is closed (§6)

### P2 — downstream (blocked on P0/P1 above; do not start early)
19. Physical pole masses from a REAL spectral transfer (not a local Hessian) — §7; needs item 16–17
20. Root-native chiral `A_f` (mass-gap program's RP-G4: locality/chirality/anomaly/doubling) — needs
    item 14
21. Yukawa coefficients — needs items 1, 18
22. CKM/PMNS mixing angles — needs item 2 (generations) + item 21
23. Neutrino architecture (Dirac vs Majorana, whether `ν^c` must exist) — v1.5's own negative
    control flagged this as `OPEN_EXTRA_ABELIAN` when `ν^c` is added
24. CP violation — needs items 21–23
25. Gauge-orbit fluctuation Hessian (ghost/orbit-volume subtraction, polarization counting) for real
    one-loop β-functions — §9; v0.4's radiative engine is explicitly NOT this
26. Regulator-independence / genuine continuum limit — §9

### P3 — deferred by design (do not pursue without a specific reason to revisit)
27. **Continuum Yang–Mills mass gap (the Clay Millennium Problem)** — explicitly NOT pursued per the
    `readout-not-truth` discipline: this is a question about the non-readout continuum arbiter;
    diagnose it as an injected-infinity artifact, don't chase it. *Still necessary to track as
    explicitly OPEN and explicitly not-attempted, so nobody accidentally claims it.*
28. Scattering amplitudes (§10) — needs essentially everything above
29. Decay rates (§10) — same
30. Cross sections (§10) — same
31. Physical coupling values `g, g', v` derived (not calibrated) from the root — needs item 1/15/18
32. Radiative corrections / one-loop matching to real QCD/EW data — needs item 25–26
33. Spin-statistics / Born-measurement — flagged as a **prerequisite from the QUANTUM domain**
    (`domains/quantum/`), not this domain's job; track here only as a known blocking dependency
34. AP10 one-loop β-slope kinematic weights (`11/3, 2/3, 1/3`) derived from root — representation
    content is currently SM input; the three weights themselves are not derived
35. **Exact `μ₄^admissible`** (narrow/close `[3.875129794, 7.084096604]`) — an exploratory
    2026-07-24 attempt is logged in [`mu4_exploration/MU4_INVESTIGATION_LOG.md`](mu4_exploration/MU4_INVESTIGATION_LOG.md)
    (11 findings, several dead ends ruled out, current most-promising direction: reframe closed
    admissible surfaces as `Ker(∂₂)` over GF(3) — a linear code — and compute its weight
    enumerator via a trellis/transfer-matrix method; validated exact at a small window (R=1),
    hit a real memory near-miss at R=2 that needs a bandwidth-reduction fix before retrying).
    **Read that log before re-attempting — it names four confirmed dead ends.** Nothing in it
    is `Th_coqc`; does not change this domain's established bracket.

## 3. Explicit non-goals (do not attempt without founder direction)
- Predicting any physical number not already used for calibration-consistency.
- Claiming uniqueness of the gauge group/matter content over unrestricted representations — only
  "exact within the declared minimal architecture" is earned so far.
- Reviving the superseded exponential order-closure ansatz (`1+ζe^{κr}`) — see v1.13's fence.
- Conflating `Ξ` (chirality orientation order, v1.7) with `H` (electroweak order carrier, v1.12–13).

## 4. Where everything lives (so a fresh session orients in one read)
- `INDEX.md` — version timeline v0.1→v1.13, one row each.
- `STANDARD_MODEL_CLOSURE.md` — the authoritative node-level status matrix (§1–§11).
- `SM_INFORMATION_PHILOSOPHY_MASTER.md` — canonical narrative synthesis, same discipline.
- `CLAIM_BOUNDARY.json` / `DRIFT_CONTRACT.json` — machine-readable fences (v0.2, scoped).
- `ROOT_TO_SM_DAG.md` / `UNIFIED_FORCE_DAG.md` — DAG maps, two-axis (root vs. declared-architecture).
- `run_tests.py` — 24 Python verifiers + 26 Coq witnesses, all PASS/Closed; run before any new claim.
- Both repos (`research_universal_solver` canonical + `readout_genesis` public twin) mirror
  `domains/standard_model/` byte-identically — always edit both, verify with `diff -rq`.
- `mu4_exploration/MU4_INVESTIGATION_LOG.md` — exploratory research log (item 35 above), not a claim.
- The build pattern for a new version: exact-Fraction Python verifier (independent recompute of
  every founder-given number) → `formal/Info*_attempt.v` Coq witness (`Print Assumptions` Closed) →
  domain copy (scrub `_attempt`) → wire into `run_tests.py` → `CLAIM_BOUNDARY.json` entry → `INDEX.md`
  row → core `§V.22` note in BOTH twin core docs → `EQUATION_REGISTRY.md` if an external result is
  used → branch+PR+merge both repos, full-arc `make verify-attempts` audit before merging.

## 5. Central tracking
The 4 P0/root-debt-track headline items (§2 rows 1, 2, 3-9-as-one-line) are also registered in the
ANSE.ASIA central todo system (`cpg/tools/agent_office/todo.py list`) for visibility outside this
repo. This file is the authoritative detail; the central todo entries are pointers back here.
