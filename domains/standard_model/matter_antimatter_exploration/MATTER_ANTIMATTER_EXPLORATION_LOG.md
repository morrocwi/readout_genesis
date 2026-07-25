<!-- Exploration log, tier Dr throughout. This is a new (2026-07-25) thread, opened per
     SM_INFORMATION_PHILOSOPHY_MASTER.md section 23's own "particle-antiparticle from root" entry
     in its not-yet-derived list. Nothing in this file closes that entry. -->

# Matter/antimatter exploration — 2026-07-25: Attempt 1, a refuted-direction, informative negative

## What this is and is not

Opened fresh, deliberately NOT forced onto item 1's `r` search (Attempts 10-17,
`../item1_exploration/ITEM1_EXPLORATION_LOG.md`), after the founder asked whether matter/
antimatter might, informationally, be the reader/record (Φ/Ψ) pair — "asymmetric but balanced."
The founder explicitly asked to explore this fresh first, reading with information philosophy
throughout, and only afterward check for any real (not forced) connection to item 1.

## Attempt 1 — REFUTED (in its naive form): Bateman-doubling hypothesis, Reader settles / Record diverges

Script: `attempt1_bateman_doubling_hypothesis_v1.py`. Uses the repo's own already-existing,
`[finite_diagnostic]` "(executable)" Reader/Record telegraph stepper (II.8a,
`domains/standard_model/source_root/READOUT_GENESIS_CORE_SNAPSHOT.md`) verbatim, simplified only
by taking `G[Theta_n]=1` (no graph) and zero forcing/interaction terms, run on a scalar
double-well potential.

**Hypothesis tested** (Dr, new): Ψ (record, anti-damped `-D`) ~ matter (persists), Φ (reader,
damped `+D`) ~ antimatter (transient/resolves) — motivated by the source document's own
"Bateman-doubled structure" commentary, which genuinely connects this apparatus's sign-flipped
damping to real antiparticle physics (Feynman-Stueckelberg, CTP/Keldysh).

**Result: the opposite of the hypothesis, and NOT bounded.** Under this nonlinear (cubic) double-
well potential, Φ (reader, `+D`) SETTLES to a stable fixed point (persists), while Ψ (record,
`-D`) diverges — its envelope grows from ~1.0 to ~323 (291.9x) over the run, still increasing at
the end, not settling. The η-pairing bilinear Φ·Ψ (the source's own natural paired quantity) also
grows ~50x, not bounded/conserved.

Two loose-threshold checks in an earlier draft (`ratio>=0.5` for "Psi doesn't decrease";
`<1e6` for "Phi*Psi is bounded") were self-caught before review — both would have trivially
PASSED despite the real ~50-300x growth, masking the actual finding. Rewritten to test and report
the real magnitudes directly.

**Independently adversarially reviewed, 2026-07-25** — verdict SURVIVES WITH ONE REQUIRED
CORRECTION (minor, cosmetic): reviewer independently recomputed the simulation from scratch,
reproduced this file's numbers exactly (bit-identical), confirmed the stepper matches the
source's quoted Reader/Record formulas sign-by-sign, and confirmed the self-correction is real.
One fix required: a Part-1 comment mislabeled the simplification as `G[Theta_n]=K` when the code
has always computed `G[Theta_n]=1` (numerically inert here since K=1.0, but the prose was wrong
about which simplification was taken) — fixed in-file. No overreach found: no connection claimed
to item 1's `r`, no conflation with item 12's unrelated SU(3) color-conjugation result, no claim
about real quantum numbers or cosmological baryon asymmetry.

**What this establishes**: a real, disclosed negative result — the naive Bateman-doubled
construction, under this potential/parameters/initial condition, is genuinely unstable, not
balanced, and inverts (not confirms) the specific reader=antimatter/record=matter direction
proposed. This is informative, not merely "failed": it rules out the naive form and narrows the
next step (linear/carefully-damped regime, proper contour/regularization for the anti-damped
partner as real CTP/Keldysh constructions require, or a different pairing).

**What this does not establish**: whether ANY version of the Φ/Ψ-as-matter/antimatter hypothesis
could be made to work; any connection to item 1's `r`; any connection to the real cosmological
baryon asymmetry or to real particle quantum numbers.

## Founder redirect (2026-07-25, not yet acted on beyond this log entry)

"ถ้าเจอจุดเชื่อมน่าจะอยู่ก่อน lr. อยู่ตั้งแต่จุด อ่านเขียนในสมการแม่" — if there is a connection
point, look for it BEFORE/upstream of `L_R`, at the more primitive read/write (Φ/Ψ) point in the
mother equation itself, rather than in the fuller II.8a apparatus (which already contains
`L_{G_n}⊗I_ℱ`, i.e. `L_R`, inside `𝔾_n`). Attempt 1 above lives entirely downstream of that split
(its `G[Theta_n]` slot is exactly where `L_R` would enter, just set to identity here). Not yet
investigated: `SM_INFORMATION_PHILOSOPHY_MASTER.md` §1.1's primordial `Z_n=(Φ_n,Ψ_n,Θ_n,U_n,
Σ_n,𝒯_n,Λ_n)` retained-state tuple and §1.2's reader-record relation `r=O(X)`, which are stated
prior to any L_R/graph machinery entering the framework — a genuinely more primitive layer than
II.8a's fuller elaboration, not yet checked for this question.

Separately, the founder also asked (2026-07-25) whether Ψ (record) might belong "in the black
hole equation." Checked: this repo does carry a real telegraph-equation-to-relativity bridge,
`InfoTelegraphHorizonUnification_attempt.v` (`formal/`, cited from `domains/relativity/README.md`),
which proves the SAME telegraph apparatus's own `(M,D,K)` triple forces the classical/quantum
crossover discriminant `λ_c=D²/4MK` — genuinely upstream of any graph `L_R` (it depends only on
the temporal/damping data, not the graph-coupling term). Its own honest fence explicitly states
this is a *distinct* object from node-8's horizon lapse `N=√detB`/redshift, NOT node-8 itself.
Separately, this repo's curated external Page-curve research
(`external_research/pi_phi_retained_history_page_curve_v3/`) is explicitly
`[Open]`/"NOT_DERIVED" for anything about the physical Page curve or black-hole unitarity, with
those exact claims on its own `prohibited_claims` list. Neither file was written to make an
antimatter connection, and citing either one now for "Ψ lives in the black hole equation" without
a real derivation would repeat the CRRC pattern this session has caught and corrected multiple
times already. Flagged (at the time) as a candidate direction for a next attempt — acted on
immediately below, as Attempt 2.

## Attempt 2 — REFUTED (both sub-claims as literally stated), two exact facts survive

Script: `attempt2_universe_as_cache_of_record_v1.py`. Directly tests the founder's follow-up
hypothesis: "จักรวาลสรรพสิ่งเป็นเพียงการ CASH ของ RECORD แท้ที่อยู่ในสมการคล้ายหลุมดำ" (the
observable universe is merely a CACHE of the true Record, which lives in a black-hole-like
equation). Split into two separately-checked sub-claims, using Attempt 1's own already-reviewed
stepper and the source's own quoted equations — no new machinery.

**(A) Directional claim — Ψ is "the true record," Φ (hence the universe) is a cache of it:
REFUTED.** Re-read the source's own quoted Reader/Record equations directly
(`READOUT_GENESIS_CORE_SNAPSHOT.md` II.8a): the Reader equation has zero Ψ-dependence anywhere
(Φ evolves autonomously); the Record equation depends on Φ via `∇²V(Φ_n)Ψ_n`. The structural
direction is `Φ→Ψ` (Φ drives, Ψ records/responds), the OPPOSITE of the hypothesis. If a
cache/original relationship exists here at all, the field names read more naturally the other
way — but Ψ's own recording is unstable (Attempt 1), a poor "ground truth" candidate regardless.

**(B) Location claim — Ψ lives in a black-hole-like equation, candidate `λ_c=D²/4MK`: REFUTED as
literally stated, but a real, exact, narrower fact survives.** `λ_c` is NOT a stability boundary —
Record is unstable (positive real-part characteristic root) for any `D>0`, independent of `λ_c`;
the real instability onset is `D=0`. What `λ_c=1` genuinely marks (verified both analytically via
the quadratic formula and numerically, matched to 1e-3, with an independent re-run at a different
`K` to rule out coincidence) is a change in the FUNCTIONAL FORM of the growth/decay rate:
underdamped (`λ_c<1`) gives an exact, K-INDEPENDENT rate `∓D/(2M)` for Reader/Record respectively;
overdamped (`λ_c>1`) gives a larger, K-DEPENDENT rate. Calling this "a black-hole equation" is at
best a Dr-tier analogy about where the growth-rate formula changes character — not an
identification of a horizon, consistent with (not contradicting) the source `.v` file's own fence
that `λ_c` is a distinct object from the real horizon lapse `N`.

**Independently adversarially reviewed, 2026-07-25** — verdict SURVIVES WITH REQUIRED CORRECTIONS,
applied: the file cited its own source file's path incorrectly (`domains/relativity/
InfoTelegraphHorizonUnification_attempt.v` when the real file lives under `formal/`, only cited
FROM `domains/relativity/README.md`) — fixed at every occurrence, in this file and in this log
entry. All substantive claims were independently reverified from scratch (source equations
re-read directly and confirmed to match; the `∓D/(2M)` algebra independently re-derived
symbolically, confirmed general not coincidental; growth/decay rates independently reproduced
with a different integrator; the `λ_c` honest-fence quote confirmed accurate, not out of context).

**What this establishes**: two real, disclosed negative results on the specific hypotheses as
literally stated, alongside two genuine positive facts (the `Φ→Ψ` structural direction; `λ_c`'s
exact role as a growth-rate-regime marker, not a stability gate) that a future attempt could build
on more carefully. **What this does not establish**: any resolution of what "the observable
universe" corresponds to in this toy system; any connection to item 1's `r`, item 12's SU(3)
result, real quantum numbers, or the real cosmological baryon asymmetry — none attempted. Also
does not establish that the founder's broader "universe is a readout, not the truth" intuition is
wrong in general — that IS this repo's own existing root stance (`Z_n` retained state vs. any
`O(X)` readout of it, §1.2); only the specific Ψ=truth/Φ=cache and λ_c=black-hole identifications
tested here are refuted.

## Findings report — primordial (pre-L_R) layer, read per the founder's redirect

Per the founder's redirect after Attempt 2 ("ถ้าเจอจุดเชื่อมน่าจะอยู่ก่อน lr. อยู่ตั้งแต่จุด
อ่านเขียนในสมการแม่"), read `READOUT_GENESIS_CORE_SNAPSHOT.md`'s ROOT-0 (§I.1, `E00.1`-`E00.7`) and
Face 10 (Record/Readout/Epistemic) fresh, with information philosophy throughout, before building
anything further. Three findings:

1. **Confirmed: `L_R` genuinely sits downstream of the primordial read/write pair.** `E00.7`
   (`L_R := D_W − W`) is the LAST line of ROOT-0. The primordial "read" act is `E00.2` (`A`, the
   discriminator that registers `a≠b` — the first appearance of any reader/translator role,
   generalized later into `q_α`). The primordial "write/retain" act is `E00.5` (`τ_c>0`,
   persistence between distinguishable events). Both are stated before `E00.7` introduces `L_R`
   at all — matching the founder's intuition exactly.

2. **Face 10 (`R_O = Γ_{RAR,O}(D_O) = Ω_A∘A∘Π∘T_Σ(D_O)`, strict gap `M_A[n]≠θ(E) ∀n`,
   `ε_tot>0 ∀n`) states that EVERY observer's record is lossy, unconditionally.** This is a
   general, book-wide theorem, not specific to Ψ. It initially reads as undercutting "there is a
   true record" entirely (no record anywhere in this framework is ever the truth) — but the
   founder's follow-up refined the claim precisely: the TRUE thing (`D_O`, the underlying event
   being recorded) still exists; what Face 10 rules out is any record `R_O` ever EQUALING it, not
   its existence. "It exists but we cannot read it" turns out to be exactly what Face 10 already
   says, read correctly — not a new claim in tension with it.

3. **A new, unexplored, more-primordial-than-`L_R` lead: `I.1a`'s Copy Licence
   (`A ⇏ A⊗A`, `!_κA ⊢ A^⊗m, m≤κ`)** — a resource-logic no-free-duplication axiom, stated even
   before `E00.7`. Structurally resembles a no-cloning-theorem-shaped constraint (real physics'
   no-cloning connects to unitarity/CPT/pair creation) and matches Attempt 1's own "pair creation"
   initial-condition language. No executable machinery exists anywhere in the repo for this axiom
   yet (only cited in two `item1_exploration` files, never built or tested) — flagged as a
   candidate for a future attempt, not pursued here; testing it honestly would need new,
   deliberately-scoped work, not a quick add-on to this attempt.

## Attempt 3 — CONFIRMED (Th_coqc): the refined claim, proven in its precise general form

Script: `attempt3_true_record_unreadable_v1.py`. Coq: `formal/InfoTrueRecordUnreadable_attempt.v`
(axiom-free, `Print Assumptions` reports "Closed under the global context" for all three lemmas,
verified both standalone `coqc` and under the repo's `-R . RDL` namespace).

Tests the founder's refined claim directly: "มี RECORD แท้ แต่เราอ่านไม่ได้หนะ" (there IS a true
Record, we just cannot read it) — NOT the same claim Attempt 2 refuted (that Ψ specifically plays
that role). Proves, fully generally and axiom-free: whenever a readout `O` collapses two distinct
true states `x1≠x2` to the same readout value (exactly §1.2's own `O(hX)=O(X)` gauge-redundancy
condition), both states continue to exist as ordinary values, but NO decoder function can recover
both of them correctly from the shared readout alone (`no_decoder_recovers_state`,
`gauge_redundancy_forces_undecodability`, `true_state_exists_but_no_total_decoder` — the last
lemma keeps "x exists" and "a correct total decoder exists" as the two separate claims the
founder's refined phrasing distinguishes). Cross-checked numerically on a concrete 4-state
instance (`X={0,1,2,3}`, `O(x)=x mod 2`, gauge map `h(x)=(x+2) mod 4`), exhaustively over every
possible decoder.

**What this establishes**: the founder's refined claim is TRUE and PROVABLE, in this precise
general sense — grounding, with an exact Coq proof, Face 10's informal "every record is lossy"
claim and §1.2's gauge-redundancy definition, both pre-existing in this repo. **What this does not
establish**: that Ψ, Φ, or any other specific field is the "true state" or "readout" role-player —
this is a general, Type-polymorphic, physics-free conditional (IF a readout is non-injective, THEN
undecodability follows), not a new claim about which concrete object occupies either role. Attempt
2's refutation of the specific Φ/Ψ identification stands, unrevisited. No connection to item 1's
`r`, item 12's SU(3) result, real quantum numbers, or the real cosmological baryon asymmetry.

Independently adversarially reviewed, 2026-07-25 — verdict SURVIVES WITH REQUIRED CORRECTIONS,
applied: a cosmetic decoder-count mislabel ("2^2=4" instead of the correct 4×4=16 the code always
actually built and checked) in the Python file's Part 2 print statement, fixed. Reviewer
independently compiled the Coq file both standalone and under `-R . RDL`, hand-traced all three
proofs and confirmed none is vacuous (no unused hypothesis, no `Admitted`, no smuggled classical
axiom), and independently confirmed both source-document citations (§1.2, Face 10) are accurate,
not stretched. No other issues found.
