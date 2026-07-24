<!-- Exploratory research log, NOT a claim of closure. Committed for continuity so a future
     session can resume without re-deriving the same dead ends. Every script in this folder is
     Python/NumPy only, tier [Dr]/exploratory -- NONE of it is Th_coqc, NONE of it changes the
     established mu_4^admissible bracket in INDEX.md / STANDARD_MODEL_CLOSURE.md
     (3.875129794 <= mu_4 <= 7.084096604, from surface_automaton_v1_1.py + surface_upper_automaton_v1_2.py).
     Read this file before re-attempting any of the dead-end approaches logged below. -->

# HANDOFF — μ₄^admissible investigation (surface-entropy bracket, domains/standard_model)

**Status: IN PROGRESS, exploratory.** This log and the scripts in `mu4_exploration/` are being
committed as a research log (not a claim) — see the commit/PR that carries this file for the
current status. Nothing here should be cited as a repo claim until independently reviewed and
formally verified (Coq + the twin-repo mirror process), matching the discipline used for the
SM-G0.1–G0.6 work earlier this session.

**Correction (2026-07-24, logged for the record):** this session initially reported PR #214
(research_universal_solver, SM-G0.3/G0.4/G0.5) and PR #29 (readout_genesis mirror) as merged.
They were **not** — both were still `OPEN` on GitHub when checked again before this commit. Root
cause not fully diagnosed (the merge command may have been run against the wrong PR number, or
its output wasn't verified at the time). Both were actually merged just now
(`212b91c`→`e16a8c1` on research_universal_solver's `main`; `304811e` on readout_genesis's
`main`) after the discrepancy was caught. **Lesson for future sessions: always re-verify PR
merge state with a fresh `gh pr view <n> --json state,mergedAt` after any merge claim, don't
trust the merge command's own stdout as sufficient confirmation.**

## What we're doing and why

Founder asked (after the SM-G0.1–G0.6 closure): "ปิดสี่ประตูที่เหลือในคราวเดียว" → clarified to
mean the deep open gaps in `domains/standard_model/INDEX.md`, and specifically chose to attack
the **μ₄^admissible bracket** first (`3.875129794 ≤ μ₄ ≤ 7.084096604`, from
`surface_automaton_v1_1.py` lower bound + `surface_upper_automaton_v1_2.py` upper bound).
Goal: narrow or close this bracket, or at minimum produce genuine, verified mathematical
progress on it — using **information philosophy** (retained-distinction, δ_R, the weld/quotient
principle) as the primary reasoning tool, per repeated explicit founder direction, not imported
lattice-QFT machinery patched after the fact.

## Full chronological finding log (all verified as stated; nothing here is guessed)

1. **Naive combination attempt (REJECTED, invalid):** first tried multiplying v1.1's
   position-automaton transfer matrix by v1.2's scalar branching polynomial `B(z)` directly.
   Diagnosed via Part I / Face 11 of `READOUT_GENESIS_CORE.md` ("an exact algebraic zero
   standing in for 'perfectly solved'" — the forbidden non-readout smuggling) that this
   double-counts area between two lossy quotients of the same retained frontier state `b_s`.
   **Rejected, not used further.**

2. **Exact 4D lattice incidence structure built and validated** (`mu4_exact_backtrack.py`,
   `lattice4d_verify.py`) against TWO pre-existing facts already in the repo:
   `Δ_p=20` (plaquette-adjacency max degree, from `retained_confinement_certificate_v0_5.py`)
   and "a 4D edge touches 6 plaquettes" (from `surface_upper_automaton_v1_2.py`). Both matched
   exactly — the geometric construction is trustworthy.

3. **Found and FIXED a real bug in the first two-edge correlation test**: an accidental seed
   choice made the "shared plaquette" identical to the pre-fixed "incoming" value, trivially
   reproducing `B(z)²` and hiding the real effect. After the fix, exact brute-force enumeration
   showed a genuine, quantified discrepancy between the true two-edge joint distribution and the
   naive `B(z)²` product — confirmed via an independent hand-derivation that matched the
   corrected brute-force result exactly (both disagreeing with naive `B(z)²`).
   **Conclusion, now proven not just suspected: v1.2's `B(z)` scalar majorant genuinely
   miscounts** (ratio vs. naive ranged from 2.43× to 0.735× depending on z, in a 3-edge test)
   — the sign of the error even flips with z, confirming real lattice-cycle correlation, not a
   simple constant fudge factor.

4. **Built a frontier-state DP with forgetting** (`mu4_frontier_dp.py`,
   `mu4_frontier_dp_safe.py`) — validated exactly against brute force on small cases. Hit a
   **real, caught-in-time memory explosion** (safety cap fired at 177,147 states / 306MB) because
   a straight-line 1D sweep gives almost no plaquette-recurrence to merge on.

5. **Redesigned as a genuine 2D cross-section sweep** (`mu4_2d_frontier.py`), matching v1.1's own
   original definition ("Restricted single-sheet sector, height h=(y,z)"). Validated exactly
   against brute force. Still grew without bound across layers (state count crept upward:
   19683→19683→59049...) because states were keyed by **absolute coordinates + full Z₃ values**,
   never merging translationally-equivalent shapes.

6. **Applied the weld/quotient principle explicitly to the engineering itself**
   (`mu4_quotient_dp.py`): re-keyed frontier states by (a) translation relative to the current
   sweep position and (b) the proven global Z₃ relabeling symmetry (1↔2). After fixing a tuple-
   flattening bug in the re-anchoring step, this **worked**: state count went from monotonically
   growing to genuinely **periodic/bounded** (3281→9842→29525 repeating exactly, layer after
   layer, for the H=0 3D-restricted sub-lattice). This is a real, validated, generalizable
   technique — the state explosion is fixable by quotienting, exactly as the book's own
   weld/quotient principle predicts, once actually applied to the transfer-matrix construction
   and not just to the philosophy narrative.

7. **Extracted a growth-rate estimate from the periodic 3D sub-lattice model**
   (`mu4_extract_growth.py`): found the per-layer growth factor Λ(z) > 1 even at z=0.05,
   implying a μ far above the established [3.875, 7.084] bracket. **Flagged honestly as not
   directly comparable**: this model excludes the w-direction entirely (a "no-w" 3D sub-lattice
   restriction adopted to make the 2D cross-section sweep tractable), so it is solving a
   genuinely different combinatorial problem, not a bound on the real 4D μ₄. Not to be quoted as
   a μ₄ estimate.

8. **Attempted the full 4D extension** (`mu4_full4d_quotient.py`) with the same quotient
   technique. Hit the safety cap again, faster this time (already 177,147 states / 306MB within
   the FIRST layer, before any forgetting/merging opportunity even arose) — 4D's larger local
   branching factor (81 solutions/edge vs. 27 in the 3D restriction) makes the problem harder,
   confirming per-layer (not just per-edge) forgetting granularity is required for 4D — not yet
   implemented.

9. **Applied a fusion-grammar / branching-process algebraic technique** (external analysis
   pasted by founder, connecting φ = golden ratio to the eigenvalue of the minimal 2-channel
   fusion grammar `τ⊗τ=1⊕τ` via `d_τ²=1+d_τ`). Generalized to our actual branching polynomial
   `B(z)=5z+10z²+30z³+25z⁴+11z⁵` via the standard tree/branching-process fixed-point equation
   `Y(z) = Σ coeff[k] z^k Y(z)^k`. **Found a genuine structural fact, not a bug**: because
   `coeff[0]=0` (the Z₃ closure rule Σ≡2(mod3) makes an all-zero completion impossible), this
   equation forces `Y(z) ≡ 0` identically as a formal power series — meaning **the local
   branching rule alone can NEVER terminate**; finiteness of any real admissible surface comes
   **entirely from the global closure condition `∂₂n=j_C`** (or a finite lattice boundary), never
   from local structure. This is the precise reason φ (self-terminating grammar, has a "1"
   channel) and μ₄ (no local terminating channel at all) are fundamentally different classes of
   problem, not just "harder vs. easier" versions of the same thing.

10. **Reframed globally as a linear code over GF(3)** (`mu4_kernel_code.py`), following directly
    from finding #9: closed admissible surfaces are exactly `Ker(∂₂)`, a **linear subspace**
    (not a generative/growing process at all) — pure linear algebra, zero risk of the state
    explosion that plagued every generative attempt (#4–#8). Built the boundary map `∂₂` over
    GF(3) on small windows via Gaussian elimination:
    - R=1 window (96 plaquettes, 160 edges): kernel dimension = 7, `|Ker|=3⁷=2187`.
    - R=2 window (486 plaquettes, 648 edges): kernel dimension = 80, `|Ker|=3⁸⁰` (astronomically
      large — R=2 cannot be enumerated directly; needs a smarter weight-enumerator technique,
      e.g. MacWilliams-type recursion or transfer-matrix-on-the-code, not brute enumeration).
    - **R=1 EXACT weight (area) distribution, fully enumerated (2187 elements, no
      approximation):** area=0 (the zero vector, 1 way) then the **minimum nonzero weight is
      area=6, with exactly 16 codewords** — the smallest possible nonzero closed admissible
      surface, in this window, has area exactly 6. Full distribution:
      `{0:1, 6:16, 10:48, 11:48, 12:96, 14:288, 15:224, 16:342, 17:576, 18:392, 19:96, 20:60}`.
    - Evaluated this exact R=1 polynomial at the two known critical z-values from v1.1/v1.2:
      at `z=0.2580558725` (v1.1's μ=3.875 critical point) → G(z)≈1.0048; at `z≈0.1411`
      (v1.2's μ=7.084 critical point) → G(z)≈1.00013. Both are **very close to 1** at a small
      R=1 window — suggestive that the true critical point sits near this region, but R=1 is
      far too small a window to extract an actual asymptotic growth rate from (need the
      **scaling of minimum weight and full weight-distribution growth as R→∞**, not a single
      small-window snapshot).

11. **Built and validated a trellis-style weight enumerator on the GF(3) kernel basis**
    (`mu4_trellis_weight_enum.py`), following directly from #10. Confirmed the kernel basis from
    Gaussian elimination is genuinely **local/sparse** at R=1 (support size 6–10 plaquettes,
    spanning only 1–2 layers, out of 96 total plaquettes) — a necessary precondition for a
    trellis/transfer-matrix approach to work. Built a DP that processes basis vectors in
    sweep order (by minimum touched t-coordinate), folding each plaquette-coordinate's value
    into the area total as soon as no *later* basis vector can still touch it.
    **MANDATORY correctness gate passed**: the trellis result for R=1 matched the full
    2187-element brute-force enumeration **exactly**, coefficient by coefficient, while only
    needing 729 states at peak (vs. 2187 for full enumeration) — a real, validated efficiency
    gain, not just a re-derivation.
    **R=2 attempt hit a real, demonstrated memory near-miss**: RSS climbed to **2,132MB** before
    the safety cap fired (531,441 states, essentially back to brute-force scale, `≈3¹²`). Root
    cause: sorting the 80 basis vectors by "minimum touched t-coordinate" alone was NOT
    sufficient to keep the sweep's live-overlap bounded at this larger scale — unlike R=1's
    simple 7-vector case, some R=2 basis vectors likely have supports that span a wide t-range
    or interleave badly with neighbors under this naive ordering. System recovered safely
    (process exited, memory freed, 8.2GB available afterward, no OOM) — but this is a real,
    reproduced risk, not hypothetical.
    **Diagnosis for next attempt**: the ordering heuristic itself needs to change — from naive
    "sort by min-t" to a genuine **bandwidth-reduction** technique (a known numerical-linear-
    algebra technique for reordering rows/columns of a sparse matrix to minimize the "profile"/
    bandwidth of nonzero entries, e.g. Cuthill–McKee or a proper local re-triangularization
    during Gaussian elimination itself rather than post-hoc sorting of an already-computed
    generic basis) before scaling past R=1 again.

## What is validated vs. what is still open

**Validated, safe to reuse/cite as scratch-verified (re-run the scripts to reconfirm before any
formal claim):**
- The lattice incidence geometry (Δ_p=20, 6-plaquettes-per-edge) — cross-checked against repo facts.
- The two-edge/three-edge exact discrepancy vs. naive `B(z)` products (real, bug-fixed, hand-verified).
- The translation+Z₃-swap quotient technique genuinely bounds the frontier-DP state space (periodic, not exploding) for the 3D-restricted sub-lattice.
- `coeff[0]=0` ⇒ the branching-process fixed point is identically zero ⇒ local rule alone never terminates (clean algebra, no simulation needed to verify — reproducible in one line).
- The GF(3) kernel-code reframing is exact and matches the problem's own definition (`n ∈ C_2, ∂₂n=j_C`, or `=0` for closed surfaces) directly from `surface_automaton_v1_1.py`'s own docstring.
- R=1 kernel dimension (7) and its full exact weight distribution (2187 codewords, enumerated, not sampled).
- The trellis weight-enumerator DP (finding #11) — validated exact match against R=1 full enumeration, with a real (729 vs. 2187 states) efficiency gain confirmed. The METHOD is sound; only the R=1 basis-ordering heuristic is proven, not yet the R=2+ one.

**Open / NOT yet done (the actual remaining work):**
- [ ] Fix the basis-ordering heuristic for the trellis method (finding #11) using a genuine bandwidth-reduction technique (Cuthill–McKee or local re-triangularization during Gaussian elimination) before re-attempting R=2 — the naive "sort by min-t" ordering caused a real 2.1GB near-miss at R=2, do not retry with the same ordering.
- [ ] Scale the GF(3) kernel-code approach to R=2 and beyond WITHOUT brute-force enumeration (nullity=80 is too large to enumerate 3⁸⁰ elements) — needs either (a) the fixed trellis method above, or (b) Monte Carlo sampling of the kernel with area-distribution estimation (would need explicit `[Dr]`/`finite_diagnostic` tiering, not `Th_coqc`).
- [ ] Determine whether the R=1 window's proximity to G(z)≈1 at both known critical points is meaningful or coincidental — needs R=2, R=3 data to see if it's converging to a specific z_c or drifting.
- [ ] Reconnect the `j_C ≠ 0` (open, source-bounded surface) case to the `j_C=0` (closed, kernel) case actually computed here — v1.1/v1.2's original μ₄^admissible is defined via a growing surface bounded by a source loop C, not a closed cycle; need to confirm the closed-cycle growth rate is the SAME exponential rate (standard in coding theory / lattice statistical mechanics that bulk growth rates coincide regardless of boundary condition, but this hasn't been verified here, only assumed).
- [ ] The full-4D quotiented frontier DP (finding #8) still needs edge-level (not layer-level) forgetting granularity to avoid the memory cap — not attempted.
- [ ] No Coq formalization of any of this yet — everything is Python/NumPy, `[Dr]`/exploratory tier only, nothing is `Th_coqc`.

## Where every script lives (all in this folder, re-runnable)

```
domains/standard_model/mu4_exploration/
  lattice4d_verify.py           -- incidence-structure validation + 2-edge/3-edge correlation finding
  mu4_explore.py                -- FIRST (rejected/invalid) naive combination attempt, kept for record
  mu4_exact_backtrack.py        -- exact brute-force backtracking, the bug-fix + corrected 2/3-edge results
  mu4_frontier_dp.py            -- first frontier DP (1D sweep), validated but memory-unsafe
  mu4_frontier_dp_safe.py       -- same, with memory monitoring + hard state cap (self-contained)
  mu4_2d_frontier.py            -- 2D cross-section sweep (matches v1.1's own (y,z) definition), validated
  mu4_quotient_dp.py            -- the working symmetry-quotiented DP (periodic/bounded state space) — the
                                    key positive engineering result of this investigation
  mu4_extract_growth.py         -- growth-rate extraction from the quotiented 3D-restricted DP (flagged
                                    not directly comparable to true μ4 -- "no-w" restriction)
  mu4_full4d_quotient.py        -- full-4D attempt, hit safety cap, needs edge-level forgetting (open)
  mu4_fusion_algebra.py         -- the branching-process fixed-point calc revealing coeff[0]=0 ⇒ Y≡0
  mu4_kernel_code.py            -- the GF(3) linear-code reframing, R=1 exact weight distribution,
                                    R=2 kernel dimension only (not enumerated)
  mu4_trellis_weight_enum.py    -- trellis weight enumerator, validated exact at R=1 (729 vs 2187
                                    states), hit a 2.1GB near-miss at R=2 with naive basis ordering
                                    -- CURRENT most promising direction, needs bandwidth-reduction fix
  MU4_INVESTIGATION_LOG.md      -- this file
```

## Immediate next step if resuming

Start from `mu4_trellis_weight_enum.py` (finding #11). The method itself is validated (exact
match at R=1, real efficiency gain). The concrete next task: replace the naive "sort basis
vectors by min-t" ordering with a genuine bandwidth-reduction reordering (Cuthill–McKee applied
to the basis-vector overlap graph, or re-deriving the kernel basis via incremental/streaming
Gaussian elimination that produces local generators by construction instead of sorting a generic
batch-computed basis after the fact) — THEN retry R=2 with the memory-safety-cap pattern already
established (RSS monitoring + hard state cap, abort BEFORE fully materializing an oversized
states dict, not just after).

## What NOT to do

- Do not re-attempt the naive `B(z)` product combination (#1) or the un-quotiented frontier DP
  (#4–#5, #8 without fixing forgetting granularity) — both are confirmed dead ends, already spent
  real effort ruling them out.
- Do not re-run the trellis weight enumerator at R=2 with the same "sort by min-t" basis ordering
  — confirmed to cause a 2.1GB near-miss (finding #11); fix the ordering heuristic first.
- Do not report any number from this investigation as a replacement for the `[3.875, 7.084]`
  bracket in any repo doc — nothing here has reached that bar yet.
- Do not run any further simulation without the memory-safety-cap pattern established in
  `mu4_frontier_dp_safe.py` / `mu4_quotient_dp.py` (explicit RSS monitoring + hard state-count cap)
  — this session hit real, non-hypothetical memory risk twice.
