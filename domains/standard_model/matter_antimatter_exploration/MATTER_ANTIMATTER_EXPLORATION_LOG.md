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
`InfoTelegraphHorizonUnification_attempt.v` (`domains/relativity/`), which proves the SAME
telegraph apparatus's own `(M,D,K)` triple forces the classical/quantum crossover discriminant
`λ_c=D²/4MK` — genuinely upstream of any graph `L_R` (it depends only on the temporal/damping
data, not the graph-coupling term). Its own honest fence explicitly states this is a *distinct*
object from node-8's horizon lapse `N=√detB`/redshift, NOT node-8 itself. Separately, this repo's
curated external Page-curve research (`external_research/pi_phi_retained_history_page_curve_v3/`)
is explicitly `[Open]`/"NOT_DERIVED" for anything about the physical Page curve or black-hole
unitarity, with those exact claims on its own `prohibited_claims` list. Neither file was written
to make an antimatter connection, and citing either one now for "Ψ lives in the black hole
equation" without a real derivation would repeat the CRRC pattern this session has caught and
corrected multiple times already. Flagged here as a candidate direction for a NEXT attempt (the
`λ_c` discriminant, and whether Ψ's own instability found in Attempt 1 has a `λ_c`-shaped
under/over-damped reading), not yet built or claimed.
