<!-- Durable handoff for the Standard-Model arc. Committed to git so it survives a closed
     terminal / a fresh Claude session — read this FIRST before touching domains/standard_model. -->

# HANDOFF — Standard Model arc, resume point (as of v1.13, 2026-07-22; session log 2026-07-24)

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
  question, met again here. Still fully `[Open]`.
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
