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

