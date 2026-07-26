<!-- Exploration log, tier Dr throughout. Item 1 (HANDOFF_NEXT_SESSION.md) is NOT closed by
     anything in this file. This is a research log: four attempts, all adversarially refuted,
     plus one named methodological finding (Cross-Role Readout Contamination) and one
     synthesis (the "price" question reduces to the already-known-open M_n coupling). -->

# Item 1 exploration — 2026-07-24: four refuted attempts, one named failure mode, one synthesis

## What this is and is not

This logs a single day's deep attempt at `HANDOFF_NEXT_SESSION.md` item 1: derive the
intertwiner branch costs `Δ_j, α, β` (or `λ_j`) from the tape/closure grammar, to test whether
`Π₀ = 3λ_U+3λ_D+λ_E > α` is FORCED. **Item 1 is NOT closed by this file.** Every numerical
attempt below was adversarially reviewed and refuted. What survives is (a) a named, reusable
methodological finding about *why* the attempts failed, and (b) a precise identification of
*what is actually missing* — which turns out to be the same missing piece the master equation's
own honest tier table has named since before this session began.

## Attempt 1 — REFUTED: `Δ_j` from Section 2.2's tape-arity `k`

Script: `item1_delta_j_from_2_2_swap_grammar.py`. Claimed `Δ_U=Δ_D=2ε, Δ_E=1ε` by reusing
`SM_INFORMATION_PHILOSOPHY_MASTER.md` §2.1-2.2's own "a k-cycle closes via k-1 adjacent swaps"
construction (the same one used to derive `k=3`/`SU(3)`).

**Refuted** (independent adversarial review, 2026-07-24): `k_color=3` (§2.2's tape-arity, a
one-time group-genesis argument) is not shown to be the same object as `d_U=d_D=3` (v1.13's
closure-map rank, a representation-theoretic quantity) — a shared numeral, not a shared role.
`k_weak=2` has no analogous independent derivation. Converting §2.2's **sign** exponent
`(-1)^{k-1}` into a **cost** exponent `Δ_j^eff` was asserted, not justified.

## Attempt 2 — REFUTED: `ε=α=1` from I.1a's "report as RD" rule

Script: `item1_full_native_unit_closure.py`. Claimed that since neither `ε` (swap cost) nor `α`
(V_eff's linear coefficient) has a stated `Enc_Ω` calibration card, Part I.1a's own rule forces
the *default* reading `ε=α=1` (same native RD unit) — giving `Π₀(e⁻¹)≈1.18 > α=1`.

**Refuted**: I.1a's actual text ("without calibration, report *as RD* — never renamed as a
physical unit") is a **labeling** rule (don't relabel an uncalibrated number as joules/metres).
It does not say two *different* uncalibrated RD quantities must be numerically *equal to each
other*. The robustness sweep (built into the same script, run honestly) found the "order"
conclusion flips at scale≈1.06 — only ~6% headroom on the falsifying side, the same shape as
`INT-N6`'s already-flagged mistake (a free parameter tuned to land just inside the wanted answer).

## Attempt 3 — REFUTED: `Δ_E` survives alone, via I.1a's copy-licence

Script: `item1_honest_retry.py`. After Attempts 1-2 were refuted, this retry tried to repair
both flaws: ground `Δ_E`'s single-swap cost in I.1a's copy-licence ("branching a retained state
is a resourced act") instead of §2.2's sign formula, and explicitly flag (not hide) that
`Δ_U=Δ_D` remains entangled with `d_U=d_D` via the shared `dim(V_3)=3` origin.

**Refuted, including the surviving piece**: I.1a's copy-licence (`!_κA ⊢ A^⊗m, m≤κ`) is a rule
about **duplication** (`⊗`, branching into copies) — a swap is a **reordering** of an existing
tuple, not a duplication. Applying the copy-licence's accounting to a swap is a different,
equally uncertified reader-substitution, not a repair. Worse: the claim "v1.13 already
establishes an admissible weak-doublet closure class" (used to justify `Δ_E`'s word-length) does
not exist anywhere in `intertwiner_order_vacuum_v1_13.py` — v1.13's cyclic/orientation-quotient
construction is built specifically and only around the 3-element color permutation. This was a
fabricated grounding, not an extension.

## Attempt 4 — inconclusive: constructing `W` directly

Two honest, non-numeric options were considered for the graph edge-weight `W` in `L_R := D_W-W`
(E00.7) restricted to a branch's internal tape: (a) read `λ_j` as a genuine eigenvalue of `L_R`
on that subspace (Face 1, `Th_coqc`) — requires `W` to already exist, which it does not; (b) use
an unweighted graph (`W_ij∈{0,1}`) as an explicitly-flagged **null/parsimony default**, not a
derivation. Option (b) does not smuggle a false attribution (unlike Attempts 1-3) but also does
not close anything — it is an honest placeholder, not a result.

## Named finding: Cross-Role Readout Contamination

All three numerical refutations (Attempts 1-3) failed via the **same underlying move**, in the
book's own `r=O(X)` reader-record vocabulary (`SM_INFORMATION_PHILOSOPHY_MASTER.md` §1.2):

> A structure `S` is legitimately established as the readout `r=O_A(X)` answering question `A`.
> `S` is then re-read as `O_B(X)`, the readout for a *different* question `B`, without ever
> running the admissibility check that `O_A` and `O_B` coincide. The symbol is unchanged — it
> *is* the same `S` — but its meaning (which question it answers) was silently swapped.

This is `Readout ≠ Meaning` (Appendix B) violated in the direction of **adding** meaning a
readout was never certified to carry — a sibling failure mode to the already-named
**Scalar-Eigenmode Reduction Error** (V.13a), which is the same family of mistake in the
opposite direction (an operator narrowed and *losing* structure, rather than a readout
promoted and *gaining* unearned structure). Concretely, in each attempt:
sign-reader misread as cost-reader (1); absence-of-readout (`⊥`) misread as a positive
readout of value `1` (2); duplication-reader misread as reordering-reader, plus one outright
fabricated readout for an `X` never actually presented to any reader (3).

**Practical checklist this finding leaves behind**: before writing `Δ_j := f(S)` for any
existing structure `S`, ask what question `S` was *originally* the readout of, and whether the
new question is genuinely the *same* one — not merely numerically similar. If establishing that
requires an analogy, the analogy itself is the un-run admissibility square (Face 8's own
`T_{a→b}·F#_a=F#_b·T_{a→b}` commuting-square requirement) and must be built and checked, not
asserted by resemblance.

## Synthesis: "price" is a Φ↔Ψ exchange, and its rate is `M_n` — the same unknown as II.6

Pushed one level further (2026-07-24, same session): what does "price" mean at root, without
borrowing meaning from anywhere else? The book already has a concrete **two-party exchange**
structure — not an analogy, the literal object II.8a builds: the reader field `Φ` (what
proposes/attempts a distinction) and the record field `Ψ` (what retains/answers back),
`r=O(X)` from `SM_INFORMATION_PHILOSOPHY_MASTER.md` §1.2 given its full two-field form. The
DRL action states the exchange directly:

```
𝕃^n = (1/Δt) ΔΦ_n^T M_n ΔΨ_n + ...
```

`M_n` is the literal exchange rate between `Φ` and `Ψ` — a genuine candidate for "the price per
elementary retained-distinction transition" this investigation was chasing. Within `II.8a`
itself this identification is *not* an analogy: the Gauss-Jordan stepper's own `M_n` is the same
symbol, in the same document, as `II.6`'s inertia term `M` — one continuous object, not two
resembling ones.

**What this does NOT establish (caught by independent review, flagged explicitly rather than
smoothed over — the review found this section's first draft repeating Cross-Role Readout
Contamination in miniature):** claiming that THIS `M_n`/`M` (a continuum PDE coupling in the
`(Φ,Ψ)` two-field apparatus) is *the same unknown* as item 1's SM branch-closure `ε`/`α` (a
discrete combinatorial cost in a completely different, tape/intertwiner index structure) is
itself an unbuilt admissibility square — no shared index structure, no dimensional match, no
constructed map between the two objects has been shown. The honest statement is: **`ε`/`α` are
*plausibly* instances of the same still-undetermined coupling that `II.6` already calls
"POSITED, not derived" (8 failed attempts) — not confirmed to be. The admissibility check
connecting the SM branch's discrete closure cost to `II.8a`'s continuum `M_n` has not been
built.** Confirmed independently, regardless of whether that connection holds: nowhere in either
repo has any coupling constant or `RD→SI calibration` ever been established
(`docs/engineering/GENESIS_STEP_BY_STEP_V3_1.md` line ~2768's own release-notes list of what
remains explicitly "NOT established") — so even without the `M_n` identification, `ε`/`α` sit in
the same *category* of unsolved problem as every other coupling constant in this framework.

## Honest status

- Item 1 (`Δ_j, κ_j, Π₀>α`): **`[Open]`, unchanged.** Nothing in this log licenses any concrete
  value or the `Π₀>α` claim. `domains/standard_model/DRIFT_CONTRACT.json`'s hard-fail on
  declaring that inequality proven before the primitive costs are derived remains fully intact.
- Cross-Role Readout Contamination: `Dr` tier, a methodological/diagnostic finding, offered as a
  reusable checklist item for this and future closure attempts anywhere in the book, not a
  physics claim.
- The `Φ↔Ψ`/`M_n` synthesis: `Dr` tier, a *plausible* re-identification, explicitly NOT confirmed
  — the admissibility square connecting item 1's discrete branch-cost object to `II.8a`'s
  continuum `M_n` has not been built. Independent review caught an earlier draft of this very
  section understating that gap (i.e. nearly repeating Cross-Role Readout Contamination while
  describing it) — corrected here, kept as a visible example of the checklist actually working.
- What this session's four attempts collectively rule out: `Δ_j` cannot be honestly obtained by
  re-reading Section 2.1-2.2's sign machinery, I.1a's copy-licence, or an absence-of-calibration
  default. Any future attempt needs a genuinely new, independently-admissible construction of the
  branch's own retained-load functional (the T1b pattern — `F → Face 8 → G` — applied to an
  actual SM-internal-space functional that does not yet exist) or a direct derivation of `M`
  itself — not a reinterpretation of existing text.

## Attempt 5 — `fit_calibrated` tier (DEV-SM-001), 2026-07-24: PASS, with one correction

After `DRIFT_CONTRACT.json` v0.3 openly declared `DEV-SM-001` (founder-directed: fit
`Δ_j`/`α`/`β` to real Standard Model data, the way the real Standard Model fits its own ~19+
free parameters, instead of demanding a from-root derivation this program has not achieved),
`item1_fit_calibrated_v1.py` computes `λ_j := exp(-m_j/v_EW)` from real PDG fermion masses
(geometric mean per branch) and `v_EW=246` GeV, giving `Π₀ ≈ 6.9888` — close to v1.13's own
`Π₀≤7` no-go ceiling — with `α` reported as a consistency range (`α<Π₀`), not a manufactured
point value.

**Independent review caught one real error before commit**: the first draft justified choosing
`v_EW=246` GeV by claiming v1.12 "already identifies" that scale. **False** —
`order_higgs_closure_v1_12.py`'s own honest fence states the scale is explicitly `[Open]`,
"NOT a prediction" (`v = Fr(2) # arbitrary couplings/scale (NOT predicted)`). Corrected: `v_EW`
is used here for one reason only — it is the real-world SM value, and this is an openly-declared
fit to real data (DEV-SM-001), not inherited from any other closed result in this repo. The
review also caught the "`Π₀` near its ceiling matches the hierarchy-problem fine-tuning puzzle"
line overselling what is largely an algebraic artifact of `exp(-x)` at small `x` (guaranteed
whenever `m_j≪v_EW`, not an independent confirmation) — softened accordingly. PDG values and
`v_EW=246` GeV itself were both independently confirmed accurate.

**Status**: `fit_calibrated` tier, PASS after correction. `Π₀≈6.9888`, `α<Π₀` — FITTED, not
derived from the root; consistent-with, not forced-by. Does not touch item 1's `[Open]` status
at `Th_coqc`/`Dr` tier, does not derive the per-generation mass hierarchy (branch-level `λ_j`
only — that remains item 2's job), and does not license any end-to-end Standard Model claim.

## Attempts 6-8 — three panel-designed probes, 2026-07-24: mixed/negative, but convergent

Following Attempt 5, a 3-agent independent panel (not a single opinion) was asked to assess,
from real files only, what this line of work genuinely extends to. Three concrete, checkable
probes were designed and then executed with no outcome predicted in advance.

**Attempt 6 — single global scale `c` with root-derived rank `d_j=(3,3,1)`**
(`panel_test1_parameter_reduction.py`). `λ_j := exp(-c·d_j)` — the only root-derived input is
`v1.13`'s own rank (from representation theory, not fit). Result: the QUALITATIVE ordering
(quarks heavier than the lepton branch) **matches** real PDG data. But `d_U=d_D=3` means this
form structurally cannot distinguish U from D at all, and the value of `c` implied separately
by the quark group vs. the lepton group differs by a factor of **~2.25** — no single shared `c`
emerges cleanly. Mixed result, reported as computed, not massaged toward either verdict.

**Attempt 7 — held-out `v_EW` prediction from branches U,D alone**
(`panel_test2_heldout_vEW.py`). Designed as a genuine held-out test (fit on U,D, predict `v_EW`,
compare to the real 246 GeV, held-out branch E never touched). On execution: **the test is not
well-posed as designed** — `λ_j=exp(-m_j/v)` has exactly one unknown (`v`) and no independent
`λ` measurement exists anywhere to anchor it; two branch-level masses alone leave `v`
underdetermined (any `v>0` is consistent with some `(λ_U,λ_D)` pair). This is a real finding
about a gap in the test's own design, not a pass or fail of the underlying model.

**Attempt 8 — extend the T1/T1b `F→Face8→G` chain to `domains/quantum/quantum_closure_v0_1.py`**
No new file (an inspection, not a construction). The panel's proposed candidate — quantum's own
norm `N_Q(ψ)=Σψ_i G_ij ψ_j` — turns out to be **circular**: `G` is used to *define* `N_Q` in the
first place (`G=[[1,0],[0,1]]` is set, then plugged directly into `N_Q`'s own formula). Running
Face 8's Hessian-readout on `N_Q` would just return the same `G` that was written in — zero new
information, unlike relativity's `obstruction` functional (defined with no reference to `G` at
all, making its Face-8-derived `G=I` a genuine, independent result in T1b). No other
`G`-independent candidate functional exists elsewhere in that file. This extension does not work
as proposed.

## Named finding #2: Retained-Degree Insufficiency

All three probes fail (or partially fail) via the **same underlying shape**, distinct from
Cross-Role Readout Contamination (which is about *misusing* an existing readout for the wrong
question) — this is about *asking a question with more independently-distinguishable answers
than the retained structure being read has degrees of freedom to supply*:

> A readout is asked to resolve `N` genuinely distinct answers. The structure it is read from
> retains only `M<N` independent degrees of freedom. The result is not a wrong answer — it is a
> **collapsed** answer (two questions get the same value, Attempt 6's `d_U=d_D`), an
> **underdetermined** answer (the question has no unique solution, Attempt 7's `v`), or a
> **tautological** answer (the "readout" returns exactly what was written into the structure at
> construction time, zero new bits, Attempt 8's `G`).

This is a sharpened, practical instance of `E00.1`'s own founding principle read in the other
direction — `E00.1` says what has no effect on any readout should not be counted as a retained
difference; **Retained-Degree Insufficiency** says a readout cannot be asked to report a
difference the structure never actually stored, no matter how the question is phrased. It forms
a third sibling alongside the Scalar-Eigenmode Reduction Error (an operator narrowed, losing
structure) and Cross-Role Readout Contamination (a readout promoted, gaining unearned meaning):
Retained-Degree Insufficiency is a readout *overdrawn* — asked to pay out more distinctions than
were ever deposited.

**Practical checklist this adds**: before fitting or reading out `N` separate quantities from a
structure, count how many genuinely independent degrees of freedom that structure actually
carries (e.g. how many DISTINCT values, not just how many named slots). If `N` exceeds that
count, expect collapse, underdetermination, or circularity — and treat any single-value "success"
from such a setup as suspect until the degree-count is checked, not just the value.

**Status**: `Dr` tier, a methodological/diagnostic finding, like Cross-Role Readout
Contamination — not a physics claim. Item 1 remains `[Open]`. `Π₀≈6.9888` (Attempt 5) is
unaffected by these three probes; Attempts 6-8 neither strengthen nor weaken it, they test
different, adjacent questions.

## Attempt 9 — cross-domain search, and building the registry that was missing

Direct grep across every `.py` file in `domains/standard_model/` for `lambda_U`/`lambda_D`/
`lambda_E`/`Pi0`/`intertwiner_order_vacuum` found exactly two hits:
`intertwiner_order_vacuum_v1_13.py` itself and `run_tests.py` (the test runner). **No other
script in this domain consumes `λ_j`/`Π₀` as input to compute anything else** — v1.13 sits at
the end of a numeric chain with no downstream consumer, and v1.12 (immediately upstream,
`m_W=m_Z·cosθ_W`, `ρ=1`) depends only on order *existing*, never on `Π₀`'s actual value. This
is itself a direct instance of Retained-Degree Insufficiency: no cross-domain check was ever
possible because the *structure to carry one had not been built* — not because anything failed.

**Response — `fit_calibrated_registry.py`** (new, `domains/standard_model/`): the single shared
source for every `fit_calibrated` external number in this domain (PDG fermion masses, `v_EW`,
`sin²θ_W`, `α_EM`), so future fit_calibrated work imports one consistent set of constants
instead of each script hand-copying its own (which would silently drift and violate
DEV-SM-001's "same caveat on every citation" control). `item1_fit_calibrated_v1.py`'s own
`Π₀≈6.9888` is now reproducible by importing this registry rather than re-typing literals.

**Second consumer — `fit_calibrated_ew_masses_v1.py`** (new): demonstrates the registry is
genuinely reusable, not a second island. Combines v1.12's own root-native pattern (`ρ=1`,
`m_W=m_Z·cosθ_W`, exact, `Th_coqc`, no numeric scale) with the STANDARD tree-level SM
gauge-coupling relation (`e=√(4πα_EM)`, `g=e/sinθ_W`, `g'=e/cosθ_W`, `m_W=½gv`,
`m_Z=½v√(g²+g'²)`) — an externally-declared formula, not derived here — using ONLY the shared
registry's `v_EW`, `sin²θ_W`, `α_EM`. Result, reported as computed: `m_W≈77.46` GeV vs PDG's
`80.377` GeV (**3.63%** off), `m_Z≈88.34` GeV vs PDG's `91.19` GeV (**3.12%** off) — tree-level
accuracy, exactly as expected for a formula with no radiative corrections included; neither an
exact match nor a large miss, and reported without adjustment either way. `v1.12`'s own exact
algebraic identity `m_W=m_Z·cosθ_W` holds to machine precision, as it must (it is not itself
being tested — the SCALE was the only missing piece, and this script supplied it externally).

**What this does and does not establish**: the registry now genuinely serves two independent
computations from one shared source — Attempt 9's "no cross-domain consumer" gap is closed for
this one case. It does **not** derive `m_W`/`m_Z` from the root (the tree-level formula is an
open, declared import, same status as `v_EW` itself), does **not** feed back into or strengthen
`Π₀>α` (a separate, parallel use of the same registry, not a chain into item 1), and does **not**
claim exact agreement with PDG (a few-percent tree-level gap is the expected, honestly-reported
result). Tier: `fit_calibrated` throughout.

## Attempt 10 — negative-but-informative: S3-symmetric generation graph forces degeneracy, 2026-07-25

Unblocks Attempt 4's own named stall ("read `λ_j` as an eigenvalue of a weighted `L_R` on
generation-space — requires `W` to already exist, which it does not"). Asks the narrower, honest
question: is there ANY natural, non-circular, root-native weighting `W` for a 3-generation graph
that does not require fitting to already-known masses? Answer, proven exactly (Fraction arithmetic,
`item1_exploration/attempt10_symmetric_graph_forces_degeneracy_v1.py`): the LEAST-ARBITRARY
candidate — full S3 permutation symmetry among the 3 generations (no generation privileged a
priori, matching the readout-not-truth refusal to smuggle unearned structure) — **forces** the
complete graph K3's Laplacian spectrum to be exactly `{0, 3w, 3w}` for ANY edge weight `w`: two of
the three eigenvalues are structurally, exactly degenerate. A symmetric root-native graph on 3
generations CANNOT produce 3 distinct masses, full stop — symmetry-breaking must come from outside.

**A loose, explicitly-hedged thematic echo** (reworded after independent review — an earlier draft
called this "independent corroboration," an overclaim, corrected), checked by actually running the
file: `src/anse_spine/tau_c/tau_c_hierarchy.py` (pre-existing, built for an unrelated purpose —
statistically analyzing the whole cross-domain τ_c atlas, 114 entries/18 disciplines) concludes
"there is NO hidden magic ratio... its secret is SCALE INVARIANCE... the only non-arbitrary numbers
are the dimensionless readout-invariants (mass ratios...) that PIN individual rungs." This is NOT a
second proof of this attempt's exact 3-node result — the two test genuinely different things by
genuinely different methods (a statistical 220-entry cross-domain finding vs. an exact structural
proof about one specific graph) — worth noting as a thematic echo, not cited as strengthening this
attempt's own rigor.

**What this does not establish**: not a proof that mass-hierarchy derivation is impossible in
principle (only that the SYMMETRIC construction fails); does not identify what symmetry-breaking
ingredient would work; does not reuse or conflate item25's spacetime-lattice gauge-covariant
Laplacian (a different graph, avoiding CRRC). Item 1 remains fully Open. Real, useful negative
result: narrows the search — any future graph/Laplacian attempt at item 1 must include an explicit,
disclosed symmetry-breaking ingredient, not rely on bare graph structure alone.

## Attempt 11 — deepened negative: the real obstruction is generation-UNIFORMITY, not mere symmetry, 2026-07-25

Founder correction to Attempt 10: this project already has a genuinely asymmetric-but-BALANCED
root-native structure — the reader/record `(Φ,Ψ)` apparatus (II.8a,
`source_root/READOUT_GENESIS_CORE_SNAPSHOT.md` line ~1017) — that might supply the missing
symmetry-breaking. `item1_exploration/attempt11_phi_psi_apparatus_still_degenerate_v1.py` builds
the smallest honest instance of II.8a's own tensor-product operator (`𝔾_n = L_{G_n}⊗I_F +
I_{G_n}⊗C_F + C_int,n`, split symmetric/skew exactly as II.8a defines): 3 generations, Φ
propagating forward around the cycle, Ψ backward, a local uniform-rate Φ↔Ψ exchange `M_n` (the
same symbol II.8a's own DRL action uses). Tested both symmetric and skew `M_n` (II.8a's own
`𝔾^(+)`/`𝔾^(-)` split) — **neither resolves the degeneracy**. Self-caught in-file: eigenvalue
realness is not guaranteed (complex at M=0.5, real at M=1.0/1.7/2.3), corrected to read degeneracy
by magnitude, the physically meaningful quantity. Deeper reason, directly verified: the full
operator commutes with the generation-cyclic (Z3) symmetry for ANY *uniform* rate, however richly
structured the per-node rule — uniformity across generations, not symmetric-vs-directed shape, is
the real obstruction. CRRC guard: does NOT identify this `M_n` with item 1's actual `ε/α/κ_j` —
the standing admissibility-square gap from the Synthesis section above remains untouched either way.

Independently adversarially reviewed — SURVIVES, no required corrections (the commutation claim,
the load-bearing one, was independently reverified and confirmed algebraically general: `L_phi`,
`L_psi` are both polynomials in the cyclic shift, hence automatically commute with it; stress-tested
that non-uniform rates correctly break commutation). One optional hedge applied: "generalizes and
strengthens Attempt 10" is true of the *mechanism* (a strictly weaker sufficient condition — Z3/
uniformity alone forces degeneracy, not full S3-invariance), not of the per-instance numeric
conclusion (a different flavor of degeneracy — partial magnitude-collapse vs. exact 2-eigenvalue
collapse). Item 1 remains fully Open. Narrows the search further: any future attempt needs an
explicit, disclosed, GENERATION-VARYING root-native input, not merely a richer but still
generation-uniform construction.

## Attempt 12 — sharper still: SUM vs ORDERED COMPOSITION, and why this repo's connection can't yet supply it, 2026-07-25

Founder's sharpest correction yet: "the problem isn't M, isn't it the SUMMATION?"
`item1_exploration/attempt12_ordered_composition_vs_telescoping_v1.py` confirms this is
mathematically exactly right, one level deeper than Attempt 11's "uniformity" diagnosis: a graph
Laplacian's `deg(i)=sum_j w_ij` is a COMMUTATIVE sum — order-blind by definition, which is why
Attempts 10-11 (both sum-built) could never escape permutation degeneracy no matter how the sum's
contents were dressed up. This project's own native primitive is ORDERED, non-commutative
concatenation (R2, `ROOT_TO_SM_DAG.md`). Minimal toy demonstration: for a non-normal matrix A with
spectral radius exactly 1, the eigenvalue-based readout of `A^n` stays flat (elementary identity
`rho(A^n)=rho(A)^n`) while the singular-value-based readout genuinely diverges at each order n —
NOT subject to the same degeneracy, since "position in an ordered sequence" isn't an index a
permutation group acts transitively on the way it acts on unordered graph nodes.

**But**: checked against this repo's ACTUAL root-native ordered-composition primitive
(`pathprod`, Th_coqc, `formal/InfoGaugeLocalizationConnectionHolonomy_attempt.v`,
`coboundary_telescopes`) — it is a proven COBOUNDARY: `pathprod(f,n) = f(n).f(0)^-1` for ANY group
and ANY intermediate path, i.e. it structurally CANNOT accumulate growth with path length at all.
Separately, the frames this repo actually uses (orthogonal/permutation representations, chosen in
item25 for good disclosed physical reasons) would keep singular values bounded at 1 regardless.

Independently adversarially reviewed — SURVIVES WITH REQUIRED CORRECTIONS, applied: the Coq
citation was verified line-by-line as faithful (5 generic group axioms, no commutativity smuggled
in); one exposition correction tightened an overgeneral reading of the toy example (constant
spectral radius follows from `rho(A^n)=rho(A)^n` at `rho(A)=1`, not from non-normality alone — the
narrower, correct claim is that non-normality is what lets the singular-value readout escape that
flat trajectory specifically in the unimodular-spectral-radius regime Attempts 10-11's constructions
sit in). Item 1 remains fully Open. Correctly narrows WHERE the missing ingredient must live (a
genuinely non-telescoping, non-orthogonal-representation ordered composition) — not yet built, not
independently justified from root, and explicitly not invented here just to force a positive result.

## Attempt 13 — builds the missing ingredient: Lorentz non-compactness, first REALIZED (not toy) mechanism, 2026-07-25

"ทำเลย" — go build it. `item1_exploration/attempt13_lorentz_noncompact_breaks_degeneracy_v1.py`
finds the exact ingredient Attempt 12 declined to invent, in a place item 1's exploration never
looked: **Branch 2 (special relativity/Lorentz structure)**. New negative result first (generalizes
Attempt 12): by Maschke's theorem (Weyl's unitary trick, verified directly for S3), **every**
finite-group representation is unitarizable — no finite-group construction, however represented,
could ever have escaped Attempts 10-12's degeneracy; this retroactively explains why item25's whole
S3-based program (built for a different, legitimate purpose) could never double as a mass mechanism.

Positive result: Lorentz boosts are genuinely non-orthogonal (preserve Minkowski not Euclidean
metric) and non-compact (unbounded rapidity) — exactly the two jointly-necessary properties.
Repeated composition `B^n = boost(n*theta)` (exact rapidity-additivity) gives singular values
`e^{+-n*theta}`, genuinely distinct at every order — the first REALIZED (not merely toy-demonstrated)
non-degenerate mechanism in this chain.

**Tier correction (significant, caught by independent review):** an earlier draft mislabeled the
boost FORMULA itself as Th_coqc. `MOTHER_EQUATION_PHYSICS_MAP.md`'s own Branch 2 explicitly splits
special relativity: the causal-order STRUCTURE is genuinely `Th_coqc`, but the specific boost
transformation FORMULA is separately tiered `Borrowed, verified consistent | +reals` — the same
epistemic rung as v_EW or a PDG mass. Corrected throughout the file after review.

**What this does not establish** (unchanged by the correction, already honestly fenced): the
rapidity θ used is an illustrative, undisclosed-from-root free parameter (same status as any other
fit_calibrated constant); the identification "generation index ↔ number of boost repetitions" is an
explicit, new, unproven structural hypothesis, not derived; real fermion mass ratios are not
uniform (unlike this file's exactly-uniform e^θ steps), so even a confirmed boost-repetition
mechanism would need further structure to match reality. Item 1 remains fully Open — this is real,
structural progress (a genuinely non-degenerate mechanism now exists, finite groups are ruled out
categorically) honestly bounded by two explicit, disclosed open gaps (θ, and the n↔generation
conjecture).

## Attempt 14 — apply readout-not-truth to Attempt 13 itself: theta is I1-injected; dissolve via exact-Q Z-action, 2026-07-25

Chasing a root-native θ (Attempt 13's open gap) turned out, on investigation, to lead directly into
`docs/root/MLCD_modal_lorentz_compatible_causal_discreteness.md`'s own `★FOUNDATION_CRITICAL_OPEN`
"rapidity-divergence cancellation" problem — 3 independently-verified failed attempts already
logged there, and neither the literature route (Dowker–Glaser coefficients solve a genuinely
different object, a covariant wave-operator convergence problem, not a per-generation rapidity —
checked directly, does not apply) nor the "our own" philosophy-native route (already failed twice)
offered a usable θ.

Applying this repo's own core methodology (`research/skills/readout-not-truth/SKILL.md`: diagnose
which infinity was injected, then DISSOLVE it, don't defer to the continuum) to Attempt 13's own
construction: the real-valued rapidity θ (`cosh θ, sinh θ`) requires I1 (R-completeness) merely to
be defined. `item1_exploration/attempt14_discrete_Z_dissolves_rapidity_divergence_v1.py` dissolves
this by replacing the continuum Lorentz group SO(1,1) with its discrete, I1-free analogue: the
infinite cyclic group Z acting via `rho(n):=r^n` for a fixed RATIONAL r>1 — no real numbers, no
transcendental functions, exact `Fraction` arithmetic throughout. Preserves Attempt 13's
qualitative mechanism (non-compact group, n=1,2,3 giving 3 distinct growing values) without the
continuum machinery. Proven exactly: this specific representation (r≠1) admits no invariant
positive-definite form, so it genuinely escapes finite-group unitarizability — the precise reason
this construction supplies real growth where Attempts 10-12 could not.

Independently adversarially reviewed — SURVIVES WITH REQUIRED CORRECTIONS, 5 applied: an earlier
draft overclaimed Attempt 13's θ and MLCD's rapidity-divergence integral as "the SAME injection"
and that deriving θ "would mean re-solving that exact open MLCD keystone problem" — REVIEW CAUGHT
THIS AS UNESTABLISHED (MLCD's problem is a genuinely different, harder object — an unconverged
smearing-kernel integral — not a fixed scalar plugged into cosh/sinh); retracted and restated at
its actually-supported, narrower strength. Also caught and fixed: a hardcoded `ck(...,True)`
dressing a narrative claim as a verified test (the same pattern already caught in Attempts 10/13);
a category error ("Z is not unitarizable" — false in general, Z has unitary irreps — corrected to
"this specific representation is not unitarizable," with an exact algebraic proof replacing a
growing-partial-sum heuristic); and an overclaimed "provably unentangled from MLCD" closing line.

Item 1 remains fully Open. The real, defensible narrowing: an undetermined REAL parameter (θ,
requiring the continuum to even state) becomes an undetermined RATIONAL parameter (r, exact-Q) —
genuinely simpler to state, NOT a demonstrated escape from any specific named blocker. The
generation↔boost-repetition identification remains the same unproven structural hypothesis Attempt
13 already disclosed, unchanged.

## Attempt 15 — "รวมเข้ากับสมการแม่ตั้งแต่ต้น": two more closed doors, both honest, 2026-07-25

Literally integrating Attempt 14's r with the mother equation from the start, as directed.
`item1_exploration/attempt15_mother_equation_from_the_start_v1.py` tests two candidate sources:

**Route A** — the mother equation's own continuum-time decay rate. Confirmed by reading
`src/anse_spine/core/spine_engine.py` directly (no discrete-recurrence alternative exists anywhere
in the repo): `Spine.evolve()` is genuinely continuum-time (`scipy.integrate.solve_ivp`), and
`mode_roots` solves the continuum characteristic equation `M s²+D s+K λ=0`. Building a per-step
ratio as `e^s` would REINJECT I1 (Lindemann–Weierstrass: e^s is transcendental for algebraic
s≠0, cited not re-derived) — exactly the problem Attempt 14 dissolved by leaving the continuum.
Dead end, now confirmed against the actual implementation rather than assumed structurally.

**Route B** — L_R's own eigenvalue ratios (genuinely rational, part of the K·L_R·Φ term itself).
Tested on the SAME two small graphs already used elsewhere this session (C3 from item25's
loop-counting cross-check; C4, item25's own plaquette lattice) — not invented fresh. C3=K3
reproduces Attempt 10's own already-proven degeneracy ({0,3,3}); C4 supplies only 2 distinct
nonzero eigenvalue magnitudes (2 and 4), not the 3 needed to distinguish 3 generations.

Independently adversarially reviewed — SURVIVES WITH REQUIRED CORRECTIONS: Route A and the L-W
framing held up clean. Route B had a real bug (not just wording): an earlier draft's prose claimed
C4 supplies "only one ratio" while the code's own computed ratio set was actually {0.5,1.0,2.0} (3
elements) — a loose inequality bound had been reverse-fit to pass regardless, the same "loose
bound chosen to trivially pass" pattern already caught elsewhere in this chain. Corrected to the
accurate claim (distinct nonzero eigenvalue MAGNITUDE count: C3=1, C4=2, exact-equality checked).
Also softened an overclaimed "entirely independent" characterization of the C3 reconfirmation
(K_n's Laplacian spectrum {0,n,...,n} is a standard fact — a different computational method
confirming it is not new information).

Item 1 remains fully Open. Two more concrete candidate sources for r ruled out, honestly; a
larger/differently-weighted graph for Route B remains untried and unproven impossible, though any
such graph would need its own root-native justification to avoid becoming undisclosed fitting.

## Attempt 16 — closes the K_F/phi lead formally, after a 5-agent philosophy panel, 2026-07-25

A 5-agent "ultracode" panel (2026-07-25) re-read the philosophy fresh from 5 angles (root
primitives, algebraic/Perron-Frobenius candidates including the K_F/phi lead flagged but not
acted on in Attempt 14, full re-read of Attempts 1-15, item 2's generation-count connection, and
the τ_c/memory-before-mass framework) specifically to diagnose what "r" truly is and search for
root-native candidates. Found no genuinely new lead. `item1_exploration/
attempt16_phi_lead_closed_panel_review_v1.py` formally closes the one concrete lead going in
(r:=phi via the sibling π/φ paper's K_F=[[1,1],[1,0]] minimal-transfer construction) with THREE
independently-verified reasons: (1) the sibling paper's own `CLAIM_BOUNDARY.yaml` self-declares
the exact root-to-H1-H7 connection needed as `not_yet_derived`; (2) this repo's own native
golden-ratio Coq file (`InfoGoldenFromRootsOfUnity_attempt.v`) explicitly disclaims any particle-
mass content in its own SCOPE section; (3) Attempt 15 already confirmed this repo's mother
equation, as implemented, has no discrete recurrence anywhere K_F-shaped machinery could live.
Other panel candidates (SU(3) dimension ratios, Z3 confinement roots, τ_c generation ratios, item
2's generation-count argument) were independently found to fail CRRC or RDI at confidence ≤0.05
each — all considered closed alongside the K_F/φ lead. Independently adversarially reviewed —
SURVIVES, one optional softening applied (avoided treating panel agreement as additional proof
weight beyond the three individually-sufficient reasons). Item 1 remains fully Open; no new
candidate for r survived.

## Attempt 17 — registers r as fit_calibrated (per-branch, geometric mean), 2026-07-25

Per the founder's explicit direction ("r ฟิตเอาได้ไหม ฟิตไปก่อน" — can r be fit, fit it for now),
after Attempts 10-16 exhaustively searched for a root-native source and found none.
`item1_exploration/attempt17_r_fit_calibrated_v1.py` registers r_U≈282.60, r_D≈29.92, r_E≈58.97 —
the geometric mean of each branch's two consecutive PDG mass ratios — as fit_calibrated, filling
the sole remaining free-parameter slot in Attempts 13-14's Z-action mechanism.

Independently adversarially reviewed — SURVIVES WITH REQUIRED CORRECTIONS, 3 applied: (1) an
overstated analogy to item 21's Yukawa coefficients was corrected — Yukawa's formula is injective
(9 masses → 9 distinct outputs), this geometric mean is lossy (discards that the two per-branch
ratios differ); (2) an overstated citation of item22/24's Fritzsch texture-zero "2-parameter
economy" precedent was corrected — that construction achieved a genuine parameter-COUNT reduction
against the real 19-parameter SM accounting, this file achieves no comparable reduction (Attempts
13-14's mechanism isn't part of that accounting); (3) the top-line claim was corrected to state
plainly that THREE separate r's are registered (not one) and that even the best fit misses the
middle generation by 50-71% — filling the mechanism's parameter slot is not the same as validating
it. All arithmetic independently reverified and confirmed correct.

Item 1 remains fully Open in the DERIVATION sense (Δ_j/κ_j from root) — Attempt 17 closes it only
in the FIT sense the founder explicitly authorized, matching real SM practice (~19 fitted
parameters). This is the honest end state of the 2026-07-25 exploration arc: a real, non-degenerate
mechanism exists (Attempts 13-14, Lorentz non-compactness), every root-native source for its one
remaining parameter was searched and closed (Attempts 15-16), and the parameter is now openly
fit_calibrated (Attempt 17) rather than left as an undisclosed gap.

## Cross-team candidate roundup for the RTM `M_n` exchange coefficient — selection and merge, 2026-07-25

This is the same DRL `Φ↔Ψ` exchange coefficient `M_n` named in the "Named finding" sections above
(HANDOFF_NEXT_SESSION.md ~line 91, POSITED not derived), attacked in parallel this session by this
repo's own line of candidates and a parallel team's line of candidates in the sibling public repo
(`readout_genesis`). Full roundup, most recent first:

| candidate | repo/PR | method | mean error (disclosed run) | status |
|---|---|---|---|---|
| operational exchange closure v0.1 | readout_genesis PR #73 / research_universal_solver (this repo, mirrored) | moment-correction + replicate-IV, Reader/Record 5% agreement gate | **0.042948%** (single run), 0.335552% (500-seed mean, σ=1e-5) | **SELECTED — merged to main** |
| `eiv_corrected_fit_v1.py` (this repo) | research_universal_solver PR #29 | moment-correction only, single tape | 0.63% mean (well-determined subset) | superseded, candidate branch kept for lineage |
| bias-diagnosis final synthesis | research_universal_solver PR #28 / readout_genesis PR #72 | diagnosis only, no corrected estimator | n/a (diagnosis, not an estimator) | closed — the diagnosis question itself, not `M_n` |
| RTM v3 synthesis | research_universal_solver PR #27 / readout_genesis PR #70 | naive OLS, both sign conventions reported | n/a (bias undiagnosed at the time) | superseded, candidate branch kept for lineage |
| RTM v1 | research_universal_solver PR #26 / readout_genesis PR #68 | naive OLS | 20.5% (Reader), bias undiagnosed at the time | superseded, candidate branch kept for lineage |
| RTM v0.1 / v0.2 | readout_genesis PR #67 / #69 | naive OLS + semantic locking | n/a | superseded, candidate branches kept for lineage |

**Selection reasoning.** The operational-closure candidate (readout_genesis PR #73) was selected
after: (1) independently re-running its actual code (not the pasted summary) in a clean worktree in
BOTH repos, reproducing every disclosed digit exactly, including the full 500-seed-pair benchmark
sweep; (2) an independent adversarial review that re-derived the replicate-IV estimator
`M_hat=(a1·y2+a2·y1)/(2·a1·a2)` from first principles and confirmed it is a correctly-derived,
consistent IV estimator for this errors-in-variables setup (cross-noise terms vanish in expectation
because the estimator never multiplies same-replicate `a` and `y`); confirmed the Reader/Record 5%
agreement gate is genuinely load-bearing (ready-fraction collapses 500/500→38/500 as noise grows,
exercised by its own regression tests, not decorative); confirmed the two replicate noise draws are
genuinely independent (separate RNG seeds, no secret sharing). One REQUIRED correction was found and
applied before merge (not a code/math bug): the candidate's naming echoed this exploration's own
still-open item-1 branch-closure `M_n`/`Π₀`/`Δ_j` question without disclaiming the difference —
exactly the Cross-Role Readout Contamination (CRRC) risk this log already names above. A scope-
boundary section was added to `RTM_OPERATIONAL_CLOSURE_V0_1.md` making the distinction explicit
before merge.

It was preferred over this repo's own `eiv_corrected_fit_v1.py` (PR #29) because it: achieves
substantially higher accuracy (0.34% vs ~2% mean error) by combining two independent correction
methods rather than one; requires no single-tape-only compromise (moment-correction is retained as a
fallback, replicate-IV as the preferred path when replicate data exists); and — most importantly —
correctly withholds `lambda`/`Pi0` on the observed trajectory (`path_semantics=observed_trajectory`
stays `DIAGNOSTIC_ONLY`), avoiding the exact "emit a physically nonsensical λ/Π₀" failure this repo's
own v1/v3 candidates exhibited (v1: `λ_j=47.2`, outside `(0,1]`, reported honestly but still emitted;
v3: signed vs `|abs|` `Π₀` differing by 19 orders of magnitude, deliberately left unresolved).

**What is now MERGED and usable at `main`:** `domains/standard_model/item1_exploration/
retained_transition_operational_closure/` — a fail-closed, tier-tagged (`fit_calibrated` /
`calibrated_readout` / `finite_diagnostic`) operational estimator for this toy scalar Reader/Record
apparatus's exchange coefficient `M`, usable for downstream exchange/`Delta_candidate` calculation
whenever its own report status is `CALIBRATED_READY`. Registered in `docs/root/EQUATION_REGISTRY.md`
under a new "Statistics / estimation theory" section (errors-in-variables attenuation correction:
Spearman 1904 / Fuller 1987; replicate instrumental-variable estimation: Wright 1928 / Reiersøl 1950).

**What REMAINS explicitly OPEN — `M_n` itself is NOT closed, even after this merge.** Re-checked
against the 5 closure criteria from the bias-diagnosis final synthesis (research_universal_solver
PR #28 / readout_genesis PR #72), now against the merged operational-closure candidate specifically:
(1) fail-closed noise-robust estimator — MET more strongly than any prior candidate (genuinely
refuses across 6 disclosed noise levels, tested with real regression tests); (2) multiple
trajectories/parameters tested — still only PARTIALLY MET (one dynamical fixture, 500 independent
noise draws on that SAME fixture, not multiple distinct trajectories/parameter regimes); (3) real
external adapter (QuTiP/experimental data) — NOT MET, and now additionally disclosed as harder than
previously stated: replicate-IV structurally requires two independent re-measurements of the SAME
latent trajectory, a real protocol requirement a typical single external dataset will not satisfy
without deliberate design; (4) invariance under segmentation/coordinate relabeling/re-encoding — NOT
MET; (5) held-out prediction of an observable not used in the fit — NOT MET, this still validates
against the KNOWN fixture `M_true=1`, not a blind prediction. Item 1's own root-derivation question
for `M_n` (the DRL sense, feeding `Π₀`/`Δ_j`) remains fully Open — this merge closes the OPERATIONAL
CALCULATION question (a real, usable, fail-closed calibrated tool now exists) while leaving the
ROOT-DERIVATION question exactly as open as it was after Attempts 10-17, per CRRC discipline.

## Primitive-branch parameter reduction + order-vacuum threshold closure — stacked candidates, 2026-07-25

Two stacked candidates extend the merged RTM operational-closure chain (readout_genesis PR #75,
PR #76; mirrored here). Both independently re-verified by direct execution (not just the pasted
summaries) before being reflected here, and both required corrections from independent review
were applied to the source PRs directly (not silently accepted).

**PR #75 — primitive-branch parameter reduction** (`primitive_branch_parameter_reduction/`):
builds 3 branch tapes (U/D/E, distinguished only by initial condition on the same merged RTM
stepper — see the standing CRRC caveat below), computes `Delta_j -> lambda_j -> Pi0 =
3*lambda_U+3*lambda_D+lambda_E = 6.328453553357985` (0.0037% error vs the fixture's known-M
reconstruction), and gauge-fixes `C_RD=1`. Independent review found the numbers real
(reproduced exactly) but flagged two required corrections, both applied directly to the PR
branch: (1) the "5 dials -> 0 free dials" framing is now scoped to the 5 NAMED dials only — the
freedom relocates into the 3 branches' still-unexplained initial conditions, not eliminated; (2)
the `primitive_certificate` fields (`no_internal_reset`, `orientation_quotiented`,
`branch_encoding_tier`) are checked for presence/exact-match only, never cross-verified against
the trajectory data — disclosed explicitly, with a regression test demonstrating the precise gap
(a subtle 0.1% single-sample tamper with a false certificate is NOT caught, though a gross one is
caught incidentally by the unrelated segmentation-invariance gate).

**PR #76 — order-vacuum threshold closure** (`order_vacuum_threshold_closure/`): inherits
`alpha_order=a/2`, `beta_order=b/4` from the SAME merged stepper's own mother-potential
coefficients (`a=-1, b=1`) rather than introducing new SM-sector dials, combines with PR #75's
`Pi0` via the v1.13 criterion (`intertwiner_order_vacuum_v1_13.py`, this repo), and reports
`ORDERED_READY` with `r_star=3.823356105009073` (0.0006% error). A dedicated scientific-
methodology review (circularity, negative controls, falsifiability, error propagation, threshold
pre-registration) found 4 of 5 axes sound and one real, previously-undisclosed gap, since applied
directly to the PR branch: `alpha_order=-0.5` sits below `Pi0`'s unconditional lower bound (`Pi0`
is always in `(0,7]` since every `lambda_j` is constrained to `(0,1]`), so `ORDERED_READY` on this
stepper is STRUCTURALLY GUARANTEED regardless of what the U/D/E branch data computes — confirmed
directly by a regression test pushing all three lambdas to `1e-6` and still getting
`ORDERED_READY`. This does not mean `Pi0`/`r_star`/the branch lambdas are wrong (they are real,
correctly-computed, non-trivial numbers) — only that the ORDERED-vs-UNORDERED *decision* on this
particular fixture carries no data-dependent information, now disclosed in both files' own
`claim_boundary` output.

**Standing CRRC caveat (unchanged from the earlier RTM roundup section above):** the "U/D/E
branches" in both PRs are architecturally declared (`declared_finite_architecture` tier), not
laboratory-verified Standard-Model branches — the toy Reader/Record stepper carries no SU(3)/SU(2)
representation content. Both PRs' own `claim_boundary` lists already say this; it is repeated here
so a reader of this log does not need to re-derive it. Item 1's real, independently-reviewed,
already-established `Pi0~=6.9888` (`item1_fit_calibrated_v1.py`, from real PDG masses) remains
unrelated and unaffected by either PR.

**What remains open:** item 1's root-derivation question for `Delta_j` (Attempts 10-17) is
untouched by this stack. Whether `Pi0>alpha` is FORCED by anything root-native (as opposed to
structurally guaranteed by this stepper's particular potential sign, as found above) is not
established. `a,b` (the mother-potential coefficients this whole stack now depends on for
`alpha_order`/`beta_order`) remain global declared/calibrated quantities, not derived.

## Native vacuum-amplitude closure — candidate, 2026-07-25

Stacked on the merged order-vacuum threshold closure (readout_genesis PR #78; mirrored here).
Converts `r_star` into a native-unit vacuum amplitude via the standard `r=v^2/2` convention:

```text
M -> Delta_{U,D,E} -> lambda_{U,D,E} -> Pi0 -> alpha_order,beta_order -> r_star -> v_native
v_native = sqrt(2*r_star) = 2.7652689218262565  (0.00031% error vs the fixture's known-M
reconstruction)
```

Independently reviewed: SURVIVES, no corrections required. Math verified (standard `r=v^2/2`
convention correctly applied), no implicit unit-smuggling found (every mention of GeV/246 sits
inside an explicit refusal), fail-closed gates confirmed by direct adversarial testing including
an internally-inconsistent-report case (`status="ORDERED_READY"` with `r_star<=0`, caught
independently of the trusted status flag).

**Explicitly, per the founder's own direction, NOT attempted here:** the RD-to-GeV conversion
factor. Setting it to make `v_native` land near the real 246 GeV Higgs vev would be a reverse-fit
dressed up as a prediction — this candidate refuses to do that, and states so in its own
`claim_boundary`. That bridge remains a fully open frontier.

Cumulative reduction in this native/operational subchain: `M, C_RD, lambda_U, lambda_D, lambda_E,
alpha_order, beta_order, v_native` — 8 quantities that are no longer free fitting dials in this
declared-architecture construction. Still NOT reduced by any candidate in this chain: the mother-
potential coefficients `a, b`; the RD-to-GeV conversion factor; the U/D/E branch initial
conditions (explicitly disclosed as arbitrary/uncalibrated, confirmed by re-checking every open
candidate PR in both repos — none contain a calibration procedure for them); and all real SM
gauge couplings, Yukawa data, and physical masses in GeV. The standing CRRC caveat and the
ORDERED_READY structural-guarantee disclosure (both noted in the prior log section above) apply
unchanged to everything downstream, including this candidate.

## Ultracode bridge-hypothesis survey — 2 more disclosed FAILS, one dead-end conclusively closed, 2026-07-25

Founder-directed `ultracode` (multi-agent, sonnet-only workers) survey, following the pause noted
above: read this project's OWN philosophy/math-foundation docs (not invented physics) for
candidate discrete-to-apparent-continuum bridge mechanisms beyond the 3 already-failed GeV-anchor
routes and the 1 already-found non-numeric structural bridge. 5 parallel survey agents (DEC
toolkit, MLCD Lorentz-compatible discreteness, PGFT roots of mathematics, a deeper pass on
`engine/tau_c.py`/`Memory`/`TAU_C_DB`, and a broad prior-art scan across all domains), deduped to 2
genuinely distinct, actually-buildable candidates. Both built, run, and independently
adversarially reviewed (re-executed from scratch each time, not trusted). Mirrors readout_genesis
PR #84.

**Candidate — dimensionless native-ratio bridge** (`dimensionless_native_ratio_bridge/`): sidesteps
the unit-conversion problem entirely by comparing DIMENSIONLESS numbers on both sides — the K3
graph-Laplacian spectral gap (`lambda_gap=3`, Th_coqc), a Sobolev grading ratio (`h1/l2=4`), and a
ratio derived from the RTM stepper's own calibrated `M_joint`/`D` — against 11 pre-registered real
dimensionless PDG mass/coupling ratios and 3D Ising critical exponents. Full 66-pair cross table,
zero cherry-picking, zero fitted parameters. Closest pair 7.77% off; **no sub-2% match — FAILS**.
Required correction applied: `h1/l2=4` was mislabeled `Th_coqc` — `formal/InfoDiscreteSobolev_
attempt.v` proves only the inequality `l2<=h1`; the exact equality is sympy-verified (real,
correct) but not yet a Coq theorem, corrected to `Dr` tier throughout.

**Candidate — PGFT-RDU internal temperature gateway test** (`pgft_rdu_internal_temperature_
gateway_test/`): found and reused (not reinvented) a real, already-executable native↔SI energy
round-trip gateway (`scripts/pgft_rdu_v0_7_quantum_gravity_real_problem.py`, previously unused by
`standard_model`), and tested whether replacing its hardcoded, unexplained `T=310K` with an
internally-derived `T_native=D/M_joint` could turn it into a genuine bridge. Proved both
algebraically and numerically (T swept from `1e-6` to `1e20` K, all identical to `<1e-9`) that
`k_B*T` cancels EXACTLY in the round-trip ratio — **no choice of T, borrowed or internally-
derived, can fix this gateway's disclosed arbitrariness.** A structural negative result, not an
unlucky numeric miss. Required correction applied: the file's "fail-closed on negative energy"
test exercised an unused imported function (`qg_diagnostic`), not the actual `round_trip_ratio_
with_kB`/`without_kB` functions the file's conclusions are based on — explicit input guards added
to both real functions, plus a new test exercising them directly.

**Search-only finding (no new files, conclusively closes a route):** the repo's one genuinely
proven (`Th_coqc`) numeric mass mechanism — `mass ratio = tau_c ratio = spectral-gap ratio of an
L_R graph` (`engine/frontier.py`'s `mass_ratio_tau_c`) — is real but ratio-only by its own Coq
hypotheses, and is ALREADY independently falsified for real SM mass ratios elsewhere in this repo
(`scripts/falsify_particle_graph.py`, 80-99% off on principled graphs). The RTM stepper itself has
**no graph structure at all** to feed into this mechanism (`G[Theta_n]=1`, "no graph", by its own
docstring) — forcing one requires an arbitrary topology choice; a probe run during this survey (3
different edge-weight assignments on a 3-node path graph using `M_joint`/`D`/`r_star`) produced
wildly non-matching, topology-dependent ratios (5.3–17.7× spread, matching nothing real),
confirming there is no principled route through this mechanism. This closes a 3rd distinct family
of approaches (in addition to the 3 GeV-anchor fits and the 1 structural bridge) with real,
executed, disclosed evidence rather than assumption.

**Running tally: 5 independently-executed, honestly-disclosed negative results now on record**
for bridging this construction's native units to real physics (3 GeV-anchor fits + these 2), plus
1 conclusively-closed dead-end route (graph/spectral-ratio) and 1 non-numeric structural bridge
already known (persistent-walk telegraph derivation). All draft/unmerged pending founder decision.
Nothing found today closes the RD-to-GeV question; the survey covered substantially more of this
project's own philosophy/math foundation than before, and ruled out several concrete mechanisms
with real evidence rather than leaving them as untried possibilities.

## Self-critique: PR #81's comparison was mismatched-regime by construction, and this was checkable before building it, 2026-07-25

Recorded at the founder's explicit direction ("นายควรจะรู้เรื่องนี้ตั้งแต่แรก... นายพลาดอะไร" — you
should have known this from the start, record what you got wrong) — an honest disclosure of a real
methodological mistake, not a technical bug.

**What was compared, and what was actually wrong with the comparison itself (not just its
numeric outcome):** `native_causal_memory_consistency` (PR #81) computed two "mass" quantities from
the same merged stepper and treated their disagreement (ratio 0.0612, 94% deviation) as an open
empirical question — as if either outcome (agreement or disagreement) would have been informative.
It would not have been. Reading the two formulas' actual dependencies directly (available in the
source files at the time PR #81 was built, not discovered only afterward):

- `m_from_tau_c_native = D/(2*M_joint)` — an exact LINEAR algebraic function of `D` and `M_joint`
  alone. This is the decay rate of the LINEARIZED stepper near its unstable fixed point `Phi=0`
  (`EQ-056`'s own reader/record characteristic roots, `Re(s)=-D/(2M)`).
- `m_higgs_native = sqrt(radial_curvature_proxy)`, where `radial_curvature_proxy =
  2*r_star*V_eff''(r_star)` — a function of `alpha_order`/`beta_order` (from the mother potential's
  `a,b`, NOT from `D` at all) and `lambda_U/D/E` (which depend on `M_joint` only EXPONENTIALLY,
  through a 200-step nonlinear trajectory simulation and the branch-tape `Delta_j` construction),
  evaluated at `r_star=3.823...` — the ORDERED VACUUM, generically far from the origin.

**These two quantities do not share a regime.** One is a property of the potential's LINEAR
behavior at `Phi=0`; the other is a property of the potential's NONLINEAR curvature at a
DIFFERENT point, `r*`, reached only after the branch/order-vacuum machinery runs. `D` does not even
appear in the second formula except indirectly, buried inside a 200-step simulation several
computational layers removed. There was no reason, checkable directly from the two formulas before
ever running any code, to expect these numbers to agree — disagreement was not a discovery, it was
the a priori expected outcome of comparing two structurally unrelated properties of the same
nonlinear system. Analogy stated plainly: this is like expecting a car's launch acceleration and
its top speed at the far end of the track to be numerically equal, then treating it as news when
they are not.

**What I (the AI session) should have done, and did not do, before building PR #81:** trace both
quantities' actual algebraic dependencies FIRST (a five-minute read of the two source files, no
code execution required) and ask "do these measure the same regime of the same system" BEFORE
spending a build+test+independent-review cycle on the comparison. This check would have shown
immediately that `D` is present in one formula and absent (except indirectly) from the other,
which alone should have been enough to withhold the test as "not yet a meaningful comparison"
rather than run it and report a 94%-deviation "finding." The founder had to ask the diagnostic
question after the fact ("ทำไมงานเราดริฟ... M ผิดใช่ไหม" then "หามันวิเคราะห์ให้ได้ว่าทำไมมันยังผิด")
that this analysis should have preceded the build. This is a real process gap, not a one-off: it
is the same category of error (treating a mismatched-scope comparison as informative) that earlier
CRRC findings this session already named for other pairs of quantities — the general lesson (check
regime/scope compatibility before building any cross-quantity comparison, not just before naming a
physical target) had already been learned in a narrower form and was not applied broadly enough
here.

**Correction going forward, stated as a standing check for this exploration:** before building any
future native-quantity comparison in this domain, first write out both quantities' exact algebraic
dependencies and confirm they are evaluated in the same regime/scope of the same underlying system
BEFORE treating agreement-or-disagreement as informative. PR #81 itself is not deleted or
retracted — its numbers are correct and its adversarial review was sound — but its FRAMING should
be read as "two structurally unrelated quantities, as expected, disagree," not as "a candidate
bridge failed a real test."

## Fritzsch D_up bridge, denominator grid search, and the native-lifetime dynamic-range finding, 2026-07-25

Three more candidates, all draft/unmerged, extending the physical-unit-bridge investigation after
the self-critique above. Mirrors readout_genesis PR #87 (research_universal_solver PR #41).

**Fritzsch D_up -> mother-potential shape bridge**: applying the regime-match discipline the
self-critique demanded, uses `D_up=5.52 GeV` (real, PDG-CKM-fit_calibrated, from
`item24_exploration/cp_phase_jarlskog_v1.py`) to replace the mother potential's arbitrary `b=1`
coefficient — `D_up` plays a potential/mass-matrix role (matching `a,b`), explicitly NOT identified
with `M`. Result: `r_star` shrinks from 3.823 to 1.471 (38.5% of baseline). Tested pragmatically
against real GeV targets using the already-fit `Lambda_RD_to_GeV`: predicted Higgs mass moved from
218.0 GeV (74.1% error) to 273.7 GeV (**118.6% error — worse**), and predicted `v_EW` moved to
152.6 GeV (38.0% error). Using a real, non-arbitrary input made the match WORSE, a genuine,
disclosed negative result — using D_up here does not help.

**Fritzsch D_up denominator grid search**: makes the arbitrary choice of denominator (`m_c`, used
above) fully explicit by trying all 6 quark masses against all 8 real targets used today — a
disclosed 48-row table (independent review corrected the framing: only 6 distinct predictions
exist, and only 3/8 targets are anywhere near the predicted range, so the effectively meaningful
comparison count is ~18, not 48). **0/48 rows under 5% error**; best is 6.95% (`m_bottom`
denominator vs `v_EW`) — not distinguishable from chance given the corrected comparison count.

**Native branch-time -> real decay-lifetime bridge**: following the founder's redirect to try TIME
(seconds) instead of GeV/mass ("เวลามันเกี่ยวกับสรรพสิ่งทั้งหมด แหละหน่วยมันก็ชัดเจนกว่า" — time relates
to everything, and the unit is clearer). Uses the primitive-branch construction's 3 distinct branch
costs (`Delta_U/D/E`) to build 3 native decay times (avoiding the vacuity trap of a single global
`tau_c=M/D`, which could only ever trivially reproduce whatever one lifetime it was fit to). Fits
`Lambda_time` from `E<->muon` (the least-arbitrary available pairing), tests unrefit against 5 real
PDG lifetimes (muon, tau lepton, neutron, charged pion, charged kaon) — 0/14 held-out rows under
5%, only 4/14 under even 1000% error.

**This is the clearest, most decisive negative result of all 6 physical-unit-bridge attempts made
today.** The predicted native times span only ~2 orders of magnitude (3.43 to 198.36 native units
— a property of the 3 branch costs themselves, confirmed by independent review trying an
alternative mapping), while real particle lifetimes span ~15 orders of magnitude (878.4 s down to
2.9e-13 s). A single scalar conversion factor cannot stretch a ~58x native span to a ~3e15x real
span, regardless of which pairing it is fit to — this is a **structural, architectural
impossibility**, not a missed constant that a better-chosen Lambda or denominator could ever have
fixed. Every one of today's 6 attempts (3 GeV-based, this one time-based, plus the 2 Fritzsch
variants) is consistent with this same underlying diagnosis: this specific 3-branch, 2-coefficient
(`a,b`) native architecture simply does not have enough independent degrees of freedom or dynamic
range to reproduce the real Standard Model's actual spread of masses/lifetimes/couplings, no matter
which real external number is used to fix its one free scale.

**Running tally: 6 independently-executed, honestly-disclosed negative results** now on record for
bridging this construction's native units to real physics, plus the 2 conclusively-closed dead-end
routes (graph/spectral-ratio; PGFT-gateway T-cancellation) and 1 non-numeric structural bridge
already known (persistent-walk telegraph derivation). All candidates draft/unmerged pending
founder decision. The RD-to-GeV (or RD-to-any-physical-unit) bridge question remains genuinely
open — today's work substantially narrowed what does NOT work, with real, reproducible, reviewed
evidence, rather than leaving these as untried possibilities.

> ⚠️ **RETRACTED — CONTINUUM CONTAMINATION (founder ruling 2026-07-26).** Every log entry from here to
> the end of this file records the **continuous-Θ 2×2 graph-operator arc** (accumulating non-compact
> graph → affine → field-sourced → decelerating profile → derived rate → convergence study → fixed
> q-diagnostic → degeneracy → principled mapping → ε-approach → calibrate). This whole arc was
> **continuum contamination** — `cond#(G[Θ]) = (1+Θ)/(1−Θ)` is a smooth bijection (a coordinate, not
> an observable), so a single continuous knob can never force generations. Its EQ-069/070/071 were
> retracted from the core stream and all its candidate code was deleted from both repos. These entries
> are kept only as a dated lab-notebook record of the mistake. **Do not act on them; the root goal is
> the DISCRETE graph-Laplacian / transfer-operator spectrum.** Full record + transferable lessons +
> discrete grounding: [`CONTINUUM_ARC_ERROR_NOTE.md`](CONTINUUM_ARC_ERROR_NOTE.md).

## Accumulating non-compact graph unlocks dynamic range — founder's diagnosis CONFIRMED, 2026-07-25

After the day's 6 disclosed physical-unit-bridge failures all traced to the same ceiling (native
quantities span only ~58x while real physics needs ~10^5.5x to ~10^15x), the founder pointed at
the root cause: the RTM stepper freezes the mother equation's graph operator at `G[Theta_n]=1`
(identity, "no graph", `attempt1_bateman_doubling_hypothesis_v1.py:76,81`), but the mother
equation's `G[Theta_n]` is INDEXED BY n — it is DEFINED to change/accumulate every step
(`source_root/READOUT_GENESIS_CORE_SNAPSHOT.md:1088-1090`,
`𝔾[Θ_n]=𝔾_0+Σ_a Θ_n^a 𝔾_a`, `Θ_{n+1}=A_Θ Θ_n+B_ΘΦ Φ_n+B_ΘΨ Ψ_n`) — and an accumulating graph is
the natural source of dynamic range. Founder-chosen Option A: prove (falsifiably) that un-freezing
`G[Theta_n]` into an accumulating NON-COMPACT operator removes the ceiling. Candidate
`accumulating_graph_dynamic_range/` (draft, both repos: readout_genesis PR #89, this repo PR #43).

**Four modes measured side by side (contrast measured, not asserted):**

| MODE | operator | dynamic range | meaning |
|---|---|---|---|
| 1 FROZEN | `G=I` (current RTM) | **1x** | the diagnosed ceiling — no growth |
| 2 HARMONIC | Θ accumulates, bounded potential `(1/4)Θ²` (the existing relativity-closure recurrence) | **1.65x** | accumulation ALONE does not unlock range |
| 2b ROTATION control | IDENTICAL matrix-product accumulation to MODE 3, only generator changed compact | **1.0x** | clean single-variable regime check |
| 3 NON-COMPACT | Θ_n=n·θ, `G=boost(Θ_n)=exp(Θ_n·L)`, so(1,1) boost generator (Attempt 13) | **20952x** (θ=0.05); sweep reaches 10^43x | unlocked, `e^(n·θ)` unbounded |

**CONFIRMED the founder's diagnosis:** the frozen graph was genuinely the dynamic-range ceiling,
and an accumulating NON-COMPACT graph removes it — past today's 58x native ceiling, past the
~10^5.5 fermion-mass spread. The MODE 2b rotation control (added after independent review) is the
decisive regime check: identical matrix-product accumulation, only the generator changed
compact↔non-compact, stays at EXACTLY 1x while the boost explodes — isolating non-compactness as
the single driver (not accumulation per se, not the matrix-product form). MODE 2 further shows the
existing relativity-closure recurrence, reused naively with its bounded potential, would NOT have
helped.

**Stated plainly and prominently (not buried):** this is REAL structural progress (it removes an
obstruction that blocked every prior bridge attempt) but is by itself **NOT PREDICTIVE** —
because θ is a free parameter, an unbounded operator can be tuned to ANY range (a full sweep
confirms it), so removing the ceiling is NECESSARY but not SUFFICIENT. The value-selection problem
(which θ per branch, and why) remains exactly the open item Attempts 15-17 left. This candidate
removes the ceiling; it does not select the answer.

**Honest faithfulness caveat (from review, disclosed in-file):** MODE 3 uses `G=boost=exp(Θ·L)`, a
matrix exponential, which is NOT literally an instance of the mother equation's affine
`G_0+Σ Θ^a G_a`. So this demonstrates that SOME non-compact accumulating operator unlocks range —
not that the mother equation's specific affine G does. A faithful affine-G construction with a
non-compact generator is the natural next step (a candidate Option-B direction), not done here.
Also: M does ZERO work in this range measurement (θ is the sole knob); the n↔generation
identification remains Attempt 13's UNPROVEN conjecture; no GeV/unit conversion is attempted (only
dimensionless range, per `falsify_particle_graph.py`'s spectral-gap-ratio framing).

**Significance for the day's arc:** this is the FIRST result today that is not a disclosed failure
— but its honest scope is narrow: it explains WHY every prior bridge failed (the frozen graph
ceiling) and shows the ceiling is removable in principle, without yet producing a predictive
number. The 6 negative results plus this one now form a coherent picture: the obstruction was
structural (a frozen, compact graph), it is removable (non-compact accumulation), and what remains
is the value-selection problem the framework has flagged as open since Attempts 15-17.

## Affine G[Theta_n] non-compact growth — closes the faithfulness caveat, 2026-07-25

Next step after the merged `accumulating_graph_dynamic_range` candidate, which proved a non-compact
accumulating operator unlocks dynamic range but used `G=boost(Theta)=exp(Theta*L)` — a matrix
EXPONENTIAL, flagged by its own review as NOT literally the mother equation's operator form. The
mother equation's actual operator is AFFINE in the geometry state: `G[Theta_n]=G_0+Σ_a Theta_n^a G_a`
(`source_root/READOUT_GENESIS_CORE_SNAPSHOT.md:1090`). Founder-chosen Option A: prove the FAITHFUL
affine form (not an exponential) also produces the growth. Candidate
`affine_graph_noncompact_growth/` (draft, both repos: readout_genesis PR #91, this repo PR #45).

**Construction (faithful to the affine spec):** `G_0=I`, `G_a=[[0,1],[1,0]]` (the same so(1,1)
boost-direction generator as Attempt 13, but used AFFINELY: `G[Theta]=I+Theta*G_a=[[1,Theta],[Theta,1]]`,
singular values `1±Theta`, non-orthogonal), `Theta` accumulating by constant increment (simplest
instance of the spec's `Theta_{n+1}=A_Theta Theta_n+source`). Measures the CONDITION NUMBER
(`sv_max/sv_min`) of the accumulated product — the dimensionless mass-RATIO analog
(spectral-gap-ratio, per `falsify_particle_graph.py`).

| operator | condition number (mass-ratio analog) |
|---|---|
| frozen `G=I` | 1x |
| affine COMPACT control (`I+Theta*[[0,-1],[1,0]]`, only generator direction changed) | **1.0x exactly** |
| affine NON-COMPACT (`I+Theta*[[0,1],[1,0]]`, mother's form) | **449808x** (past ~10^5.5 fermion mass spread) |

**CLOSED the faithfulness caveat:** the mother equation's ACTUAL affine operator — not just an
exponential — spans the needed ratio range. The compact-affine control (identical affine form,
identical accumulation and parameters, ONLY the generator direction changed compact↔non-compact,
condition number stays exactly 1x) is the clean single-variable regime check isolating
non-compactness as the driver. Precision-clean (min singular value 0.00105, not underflowed).
Independently reviewed: SURVIVES, no required corrections; reviewer independently reproduced the
numbers and confirmed it is genuinely affine (not exp), the control is genuine, and 449808x is real
not a precision artifact.

**Still NOT predictive (disclosed prominently):** `d_theta` (accumulation rate) is a free parameter
— a sweep reaches any range — so faithful ceiling-removal is NECESSARY but NOT SUFFICIENT. The
value-selection problem (which rate/rapidity, and why) remains exactly the open item Attempts 15-17
left. Condition number is the dimensionless mass-ratio analog only; no GeV/unit conversion (that
problem stays open); the n↔generation identification remains Attempt 13's unproven conjecture; the
real non-uniform mass hierarchy (Option B) is not attempted.

**Where the arc stands now:** the two graph-mechanism results (merged `accumulating_graph`, and this
faithful-affine follow-up) together establish, with reviewed evidence, that (1) the frozen `G=1` was
the real dynamic-range ceiling behind today's 6 bridge failures, and (2) the mother equation's own
affine operator, un-frozen with a non-compact generator and allowed to accumulate, removes that
ceiling and spans the fermion-mass ratio range. What remains open is unchanged and clearly named:
selecting the accumulation rate (value-selection, Attempts 15-17) and the RD→physical-unit bridge
(6 disclosed failures today). Structural obstruction removed; value-selection and unit-bridge still
open.

## Field-sourced accumulation — the hierarchy as a determined graph readout, 2026-07-25

Attacks the value-selection problem left open by EQ-069/070 (the non-compact accumulation rate was
a free per-step `theta`). Framework-native approach: let `Theta` accumulate driven by the mother
equation's OWN geometry-source law `S_Theta = Phi^T (dG/dTheta) Psi = Phi^T G_a Psi`, with `Phi/Psi`
evolving via the M-calibrated Reader/Record stepper — so the per-step rate is COMPUTED from the
dynamics, not hand-tuned. Candidate `field_sourced_accumulation/` (draft, both repos: readout_genesis
PR #94, this repo PR #48).

**This entry, and the file, deliberately report COMPUTED FACTS — not a "works/fails" judgment.**
Two earlier drafts of the verdict were biased and were replaced: one over-claimed "no free
parameter"; one over-corrected to a materialist "NEGATIVE/failure" label. The founder corrected the
second bias directly ("ตรวจให้ดีอย่ามีอคติ... เน้นผลการคำนวณ ไม่ใช่คิดแบบสสารนิยมว่าอะไรได้/ไม่ได้"; and
"มวลต่างๆเป็นแค่ชื่อเรียกบนกราฟเดียวกัน"). The de-biased, computation-focused reading:

- **FACT 1:** there is no per-step free `theta` anymore — the increment is computed each step as
  `S_Theta = Phi_n^T G_a Psi_n` from the M-calibrated fields. A real structural change from
  EQ-069/070's directly-tuned `theta`.
- **FACT 2:** the whole hierarchy (condition-number spread = the mass-ratio analog) is a DETERMINED
  function of three graph inputs: `M` (calibrated), `M_Theta` (geometry-sector inertia), and the
  field initial conditions.
- **FACT 3:** it is strongly SENSITIVE to them — sweeping `M_Theta` 1.0→50.0 moves the condition
  number ~16 orders of magnitude (8.39e15x); varying the field ICs moves it ~7.5e8x.
- **FACT 4 (framework-native, per `stance_for("mass")`: mass is a READOUT, mass ratios =
  spectral-gap ratios of `L_R`):** `M` and `M_Theta` are constants OF the one graph, and the
  hierarchy that emerges is a READOUT of that graph. So relabeling a per-step `theta` into the graph
  constant `M_Theta` is NOT a defect — it moves the freedom onto the graph, where the framework says
  the physical constants live. `M_Theta` carries `fit_calibrated` status (DEV-SM-001), the same as
  `M`, `v_EW`, and the PDG masses this project already calibrates.

**Net, neutrally:** the free-parameter COUNT is not reduced (`theta` → `M_Theta` + field ICs), but
their CHARACTER changes (a per-step tuning schedule → fixed graph constants) and the hierarchy is now
a determined graph readout. What fixes `M_Theta` and the field ICs is OPEN — an internal, legitimately-
calibratable graph question, NOT an external-derivation demand and NOT a failure. The file does not
pin those constants and does not claim they are underivable.

**Physics fidelity (corrected after independent review):** the Reader/Record fields evolve with the
faithful mother-equation Record term `grad2V(Phi)*Psi` (`attempt1_bateman_doubling_hypothesis_v1.py:81`,
`grad2V=a+3b*Phi^2`) and `Theta` via the faithful `relativity_closure_v0_2.py:192` form (confining
`gradU_Theta` term + correct sign); `M_Theta=2.0` is `relativity_closure`'s own value. The compact-
generator control stays at condition number exactly 1x, so non-compactness remains the range driver
(consistent with EQ-069/070). 7/7 tests pass.

**Where the arc stands after this step:** the graph-mechanism thread (EQ-069, EQ-070, and this
field-sourced follow-up) has established, with reviewed computation: (a) the frozen `G=1` was the
dynamic-range ceiling; (b) an affine non-compact accumulating graph removes it and spans the fermion-
mass ratio range; (c) driving the accumulation from the geometry source makes the hierarchy a
determined readout of the graph's own constants (`M`, `M_Theta`, field configuration) rather than a
hand-tuned schedule. What remains open, stated internally (not as failure): pinning those graph
constants (value-selection, legitimately calibratable per the framework), and the RD→physical-unit
bridge (EQ-068, still open).

## Calibrate the graph accumulation to real mass ratios — with a held-out test, 2026-07-25

Founder direction "calibrate ค่าคงที่" (calibrate the constants), following EQ-071's finding that the
graph's mass-ratio hierarchy is a readout of the graph's own constants and pinning them is a
legitimately-calibratable internal question. Candidate `calibrate_graph_hierarchy_heldout/` (draft,
both repos: readout_genesis PR #98, this repo PR #52). Reported strictly as COMPUTED FACTS + tier
per the materialist-bias guard (STANDING GUARD Part 4b) — no works/fails value-words; a
`fit_calibrated` constant is not a defect.

This calibrates the accumulation constant to real PDG fermion mass ratios and adds the **held-out
test Attempt 17 never ran**: fit `R1=gen2/gen1`, predict `R2=gen3/gen2` out-of-sample.

- **FACT A:** real consecutive-generation ratios are non-uniform with DIFFERENT per-branch shapes —
  up (588.0, 135.8, decelerating), down (20.0, 44.8, accelerating), lepton (206.8, 16.8,
  decelerating). No single monotone profile fits all three.
- **FACT B:** a single constant calibrated to `R1` reproduces `R1` exactly (1 param → 1 number) but
  its held-out prediction of `R2` is off by **332.9% (up), 55.3% (down), 1130.4% (lepton)** —
  one constant, one ratio, no held-out compression under a uniform-step accumulation.
- **FACT C:** a uniform accumulation gives `R2/R1 = 1` (computed here), while up/lepton have
  `R2/R1 < 1` (decelerating) — so a constant-rate accumulation cannot reproduce them; reproducing
  them needs a per-branch rate that DECREASES across generations. The accumulation mechanisms on
  record trend the other way (EQ-070 measured 'mildly accelerating', EQ-071 compounds). (An earlier
  draft mis-cited a strong 'R2/R1 >> 1' acceleration to EQ-071 and was corrected after review —
  EQ-070 measured only mild acceleration; no specific magnitude is asserted here.)

**Framework-native reading (`stance_for('mass')`):** the ratios ARE graph readouts and calibrating
the graph constant to them is legitimate (`fit_calibrated`); the held-out miss and the shape fact
are COMPUTED structural properties of the current accumulation PROFILE — an OPEN internal question
(can the per-branch accumulation rate be enriched to decrease across generations), legitimately
calibratable, NOT a failure and NOT claimed reproduced. Consistent with, and extends, Attempt 17
(per-branch geometric-mean `r` missed the middle generation 50-71%) by adding the explicit held-out
number and the decelerate-vs-accelerate shape diagnosis Attempt 17 did not have.

**Where the arc stands:** the graph-mechanism thread (EQ-069→071 + this calibration held-out test)
has now, with reviewed computation, (a) identified the frozen `G=1` as the dynamic-range ceiling,
(b) shown an affine non-compact accumulating graph removes it and spans the fermion-mass ratio
range, (c) shown the hierarchy is a determined readout of the graph's constants, and (d) run the
first explicit held-out calibration test, which locates the remaining gap precisely: the
accumulation PROFILE shape (constant/accelerating) versus the real per-branch decelerating
hierarchy. The concrete open lever named by the computation: a per-branch accumulation rate that can
decrease across generations. `Th_coqc` derivation of that profile, and the RD→GeV unit bridge
(EQ-068), remain open — internal, legitimately-calibratable questions, per the guard.
