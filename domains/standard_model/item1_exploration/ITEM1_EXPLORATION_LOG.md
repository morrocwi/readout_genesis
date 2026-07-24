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
