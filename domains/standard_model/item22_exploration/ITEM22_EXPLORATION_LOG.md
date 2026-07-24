<!-- Exploration log, tier Dr throughout. Item 22 (CKM/PMNS mixing angles) is NOT closed by
     anything in this file. Mirrors the item1/item2 exploration logs' discipline: log every
     attempt including refuted ones, name reusable failure modes, never smooth over a mistake. -->

# Item 22 exploration — 2026-07-24: mixing-angle interpretation, one refutation, one named
# methodological finding (Continuum-Readout Injection via Analytic Functions)

## What this is and is not

This logs a single session's attempts to give "mixing angle" a meaning in this framework's own
vocabulary, separate from item 22's earlier value-level work (`mixing_angle_from_L_R_v1.py`'s
predecessor context: the Gatto-Sartori-Tonin `theta_12` fit already logged elsewhere in this
domain's item-22 history). **Item 22 is NOT closed by anything in this file.** One attempt was
outright REFUTED (a category error); the survivor needed a real conceptual correction the founder
caught, not a Coq-reviewer or a script bug.

## Attempt 1 — REFUTED: mixing angle as T (weak charge) vs tau_c (mass) basis mismatch

File: `mixing_angle_as_basis_mismatch_v1.py` (not further corrected, left as the refuted record).
Proposed "mixing angle" as the basis-mismatch between the traceless su(2) Cartan generator `T`
(this session's own weak-charge-from-root construction,
`item_weakcharge_exploration/weakcharge_from_root_v1.py`) and the `tau_c` (mass) operator.

**Refuted** (independent adversarial review, 2026-07-24): `T` acts on the 2-dimensional ISOSPIN
DOUBLET (distinguishes up-type from down-type WITHIN one generation); `tau_c`/mass varies across
the 3-dimensional GENERATION index (item 2's own `N=3`). These are different indices entirely —
`T`'s eigenbasis (up vs down) is identical in both the weak-interaction basis and the mass basis
and plays no role in why generation-1's down quark mixes with generation-2's. The review named
this the same *shape* of error as Cross-Role Readout Contamination (item1_exploration's named
finding): borrowing "eigenbasis mismatch" vocabulary established for one question (the doublet)
and silently reapplying it to a structurally different index (generation) without establishing
they share a domain. **Correct reframing, per the reviewer**: real CKM/PMNS mixing is a mismatch
between the mass-diagonal basis and the gauge-flat basis, IN GENERATION SPACE — not isospin space.

## Attempt 2 — SURVIVES_WITH_CORRECTION (after 3 review rounds), then a founder-caught conceptual
## error the reviewers did not name: `mixing_angle_from_L_R_v1.py`

Rebuilt in generation space per Attempt 1's correction. Founder also gave a stricter standing rule
for this specific construction: fitting NUMBERS is fine, but the EQUATION must be root-native (no
borrowed QM perturbation-theory formula, unlike item 22's earlier openly-borrowed Gatto-Sartori-
Tonin work, which is fine for its own declared scope). A prior deep-search across both repos
(`research_universal_solver` and `readout_genesis`) found no existing generation-space mixing
formalism, but identified `L_R := D_W - W` (docs/root/BORROWED_VS_DERIVED_LEDGER.md row 4,
genuinely **DERIVED**, `Th_coqc`, not posited) as reusable root-native machinery.

**Construction**: a 3-node graph (nodes = the 3 generations), edge weights
`w_ij := lambda_i * lambda_j` from today's already-`fit_calibrated` per-generation lambda grid
(`item1_exploration/item1_generation_resolved_lambda_v1.py`), `L_R := D_W - W` on this graph
(root-native), exact diagonalization (no perturbation theory), "mixing angle" read off as the
angle (via the retained metric `G=I`, Section 1.3) between `L_R`'s nontrivial eigenvectors and the
standard (mass) basis.

**Review round 1** (`SURVIVES_WITH_CORRECTION`): confirmed `L_R`'s generic reuse is clean (no
CRRC — the operator is defined over an abstract weighted graph, no baked-in semantic tie to any
specific prior graph). Found a real, undisclosed problem: because all three down-type `lambda`
values are close to 1, the edge weights are all close to equal, putting the graph very near a
constant-weight complete graph — whose nontrivial eigenvalue pair is EXACTLY degenerate. The
actually-computed eigenvalues (2.949 vs 2.982, ~1% apart) meant the specific eigenvector split —
and the resulting `~45.9deg` figure — was likely driven by fourth-decimal-place input differences,
not robust structure. Required: disclose this explicitly (not just a "precision" caveat), and test
an alternative edge-weight rule as a stability check.

**Round 1 fix + round 2 review**: added a `w_ij := |lambda_i - lambda_j|` alternative-rule test.
The actual result contradicted the prediction — the two rules gave CLOSE angles (`delta~0.6deg`),
not a large divergence. Rewrote the honest fence to report this HONESTLY as inconclusive (not
proof of robustness — only 2 of infinitely many rules tested — but also not the strong instability
predicted). Round 2 review (`SURVIVES_WITH_CORRECTION`) found the reported numbers correct and the
"inconclusive" framing honest, but caught a further, subtler concern: both angle computations used
`atan2(abs(v[1]), abs(v[0]))` — taking absolute values BEFORE computing the angle mechanically
compresses results toward a narrower range, so "close agreement" between the two rules could be an
artifact of the `abs()+atan2` construction itself clustering outputs, not evidence the underlying
eigenstructure is genuinely similar. Flagged as needing disclosure, not yet fixed when the founder
asked the next question.

## Named methodological finding: Continuum-Readout Injection via Analytic Functions

The founder's own catch, independent of and orthogonal to both review rounds above: **"องศาคืออะไร
ในสารสนเทศ เราน่าจะยังวางรากฐานบางอย่างผิดโดยแอบใส่ความเข้าใจแบบโลกเดิมเข้าไป"** (what is a "degree"
informationally — we're probably still smuggling old-world understanding into the foundation).

This project's own `readout-not-truth` skill (`research/skills/readout-not-truth/SKILL.md`) states
plainly that the continuum, `ℝ`, and infinity are *non-readouts*, and names **I1 (`ℝ`-completeness
/ LUB / Dedekind)** as the first of four forbidden injections — the discipline that makes `√2, π`
"numbers," and the thing the entire axiom-free Coq arc is built specifically to refuse. `acos` and
`atan2` are **analytic functions whose very definition depends on the completeness of `ℝ`** — they
are not finite computations, they are limits/inverse-function constructions that only make sense
once `ℝ` is assumed complete. `mixing_angle_from_L_R_v1.py` computed a "mixing angle in degrees"
via exactly these functions while explicitly, repeatedly claiming the whole construction was
"root-native" — **silently injecting I1 while asserting the opposite**, the precise failure mode
this project's own foundational discipline exists to catch, and neither of the two independent
adversarial review rounds on that file caught it — both reviewed the file's *arithmetic* and
*modeling choices* rigorously, but neither checked the file's *readout vocabulary itself* against
the project's own I1 refusal. This is a genuinely NEW class of failure mode for this domain's
checklist, alongside Cross-Role Readout Contamination and Retained-Degree Insufficiency:

> **Continuum-Readout Injection via Analytic Functions (CRIAF)**: a construction that computes a
> genuinely discrete/root-native intermediate result (e.g. eigenvectors of a rational-weighted
> graph Laplacian) but then reports it through an ANALYTIC FUNCTION (inverse trig, log, exp used
> as an inverse, any operation whose definition presupposes `ℝ`'s completeness) as the final
> readout — smuggling a non-readout (I1) into the *output stage* of an otherwise root-native
> pipeline, while the construction's own prose claims "root-native throughout."

**Practical checklist this adds**: before reporting any final numeric readout from a construction
claimed to be root-native, check whether the LAST step is a genuine ratio/algebraic operation
(`+,-,*,/`, or an exact/finite construction) or an analytic function (`acos`, `atan2`, `log`,
`exp` used analytically, any transcendental). If the latter, the construction has NOT stayed
root-native, regardless of how root-native its earlier steps were — the failure can hide in the
*last* step, not just the premises, and neither an adversarial reviewer focused on arithmetic
correctness nor one focused on CRRC/RDI will necessarily catch it, since it is a different axis
of honesty (readout-vocabulary discipline, not arithmetic or admissibility-square discipline).

**CRIAF corollary, SIMPLIFIED TO A STANDING POLICY per founder direction (2026-07-24)** — following
the founder's own question "sin/tan/cos ต่างกันอย่างไรในปรัชญาสารสนเทศ" (how do sin/tan/cos differ
in information-philosophy terms) and the explicit follow-up instruction: **do not build a graded
hierarchy — compute and connect every future formula from ONE thing only, the Born-rule-shaped
squared ratio, and record this as a finding.**

An earlier draft of this entry proposed a 4-level graded hierarchy (`sin²/cos²` best, then
`sin/cos`, then `tan`, then `θ` itself worst) and reached first for `I4` (actual infinity) to
explain why `tan` (unbounded near 90°) was worse than `sin/cos` (bounded). **That graded framing
is RETIRED here, replaced by a single, sharper, easier-to-defend rule** — not because the ranking
was necessarily wrong in every particular, but because ranking four functions of the SAME
underlying continuum angle against each other invites exactly the kind of "how much I1 is too
much I1" hair-splitting this project's own tier discipline exists to avoid (`Th_coqc`/
`finite_diagnostic`/`Dr`/`Open` are supposed to be a small number of clean, defensible steps, not
a sliding scale). The simpler, stronger rule:

> **POLICY (standing, this domain): the ONLY admissible root-native form for a mixing/overlap-type
> readout is the Born-rule-shaped SQUARED RATIO** — `sin²θ := m_light/(m_light+m_heavy)` (or the
> equivalent `τ_c`-ratio form), i.e. exactly the shape already established, machine-tiered
> `Th_coqc`, in `engine/lexicon.py`'s GLOSSARY entry for probability: `p_i = |amp_i|²/Σ|amp_j|²`.
> `sinθ`, `cosθ`, `tanθ`, and `θ` itself (degrees or radians) are NEVER the target readout going
> forward in this domain — they may appear only as (a) an explicit, separately-tiered cross-check
> against textbook/PDG conventions (exactly how `gst_mechanism_texture_zero_v1.py`'s Part 3 uses
> `math.sin`/`math.atan` — clearly labeled "cross-check ONLY, not part of the proposed readout"),
> never as the thing actually claimed to be root-native, or (b) inside an openly-declared,
> `fit_calibrated`/borrowed-formula construction (per `DRIFT_CONTRACT.json`'s DEV-SM-00x pattern)
> where the whole point is citing an external formula, not claiming root-native purity.

**Why this connects "from the root," concretely, though still a structural parallel, not a proven
identity** (softened after independent adversarial review, 2026-07-24, verdict
SURVIVES_WITH_CORRECTION): every quantity on the right-hand side of
`sin²θ:=m_light/(m_light+m_heavy)` already has an independent, `Th_coqc`-tier root-native
pedigree in THIS project — `m = ℏ/(2τ_c c²)` (`engine/lexicon.py`, mass is a readout of
causal-memory time) and the Born rule's own `p_i=|amp_i|²/Σ|amp_j|²` shape (same GLOSSARY, same
tier). A "mixing overlap" built this way REUSES that already-accepted Born-rule FORM applied to a
new pair of `τ_c` values — but this is a **structural parallel, motivated by and identical in
shape to the Born rule, NOT an independently proven identity**: the GLOSSARY's own Born-rule entry
is specifically about complex QM amplitudes (tied to Gleason's theorem, the R0 energy quadratic
form), and applying that exact formula shape to mass/`τ_c` ratios has not been shown to be the
SAME underlying R0 concept, only the same arithmetic pattern — the same caution
`mixing_angle_from_L_R_v2_overlap_fraction.py`'s own docstring already applied ("Th_coqc-
**precedented shape**," not identical). This is still why the squared-ratio form is preferred
over `sin/cos/tan/θ` in this domain — it reuses a real, already-tiered root-native PATTERN rather
than importing external geometry — but that preference should be stated as "structurally
identical to, and motivated by, an established root-native pattern," not overstated as literal
identity with it.

**Practical rule this adds to the CRIAF checklist, going forward, replacing the earlier graded
version**: when a construction's natural readout is trig-shaped, the ONLY form to report as
root-native is the squared-ratio/Born-rule form. Do not report `sinθ`, `cosθ`, `tanθ`, or `θ`
itself as if they were comparably native — they are not merely "less pure," under this policy they
are simply NOT the claimed readout at all, full stop, regardless of boundedness or which specific
non-readout each one injects. This removes the need to litigate exactly how bad `tan`'s
unboundedness is relative to `sin/cos`'s irrationality — a distinction this entry no longer makes.
This is `Dr` tier — a domain policy/practice convention extending the already-validated CRIAF
finding (see above, the `mixing_angle_from_L_R_v2_overlap_fraction.py` review), not itself an
independently reviewed numeric claim, but a standing rule for how future work in this domain
should be written, per explicit founder direction.

## Attempt 2, continued — `mixing_angle_from_L_R_v2_overlap_fraction.py`

Fix proposed (same `L_R`/graph construction, unchanged): replace "mixing angle in degrees" with a
**mixing OVERLAP FRACTION** `|<v,e_i>_G|^2 / (<v,v>_G · <e_i,e_i>_G)`, `G=I` — the same shape as
this project's own already-`Th_coqc`-tier Born-rule GLOSSARY entry
(`engine/lexicon.py`: `p_i = |amp_i|^2/Σ|amp_j|^2`), a plain ratio of squared magnitudes, no
inverse trig, no `π`, no explicit `ℝ`-completeness invocation. All checks PASS; overlaps
per-mode sum to exactly 1 (a genuine Born-rule-style normalization, not asserted, verified).

**Status at time of writing**: sent for independent adversarial review with an explicitly
skeptical framing (is this a substantive fix, or a cosmetic rename of the same `cos²(θ)` value
under a new label — since `cos²(45.9°)≈0.485` numerically matches the overlap fraction found,
`0.484`?) and whether floating-point eigendecomposition itself (`np.linalg.eigh`, computing roots
of a characteristic polynomial) secretly re-injects `ℝ`-completeness one step earlier than the
final `acos`/`atan2` call, regardless of the fix. Review pending — **do not cite v2 as a resolved
fix until that review returns and is recorded here.**

## Honest status

- Item 22 (CKM/PMNS mixing angles) at the interpretation/definition level: **`[Open]`, unchanged.**
  Nothing in this file establishes a validated meaning or value for "mixing angle" in this
  framework's own vocabulary — only a REFUTED attempt (Attempt 1), an unstable/inconclusive
  numeric template (Attempt 2 v1, `~45.9deg`, explicitly not to be cited as a prediction), and a
  pending-review attempt to at least fix the vocabulary (Attempt 2 v2).
- Continuum-Readout Injection via Analytic Functions: `Dr` tier, a methodological/diagnostic
  finding (like CRRC and RDI before it), reusable checklist item, not a physics claim. Confirmed
  by direct comparison against `research/skills/readout-not-truth/SKILL.md`'s own I1 definition —
  not yet independently adversarially reviewed as a NAMED finding in its own right (only the code
  fix it motivated has been sent for review); should get the same "review the finding itself"
  treatment CRRC and RDI received in `item1_exploration/ITEM1_EXPLORATION_LOG.md` before being
  treated as fully validated methodology, not just an accepted-on-the-spot observation.
- `mixing_angle_from_L_R_v1.py` is KEPT (not deleted) as the honest record of both the near-
  degeneracy issue and the I1 mistake — matches this project's own practice of logging refuted/
  superseded attempts rather than silently erasing them (item1's Attempts 1-4, item2's Attempt 1).
- Item 22's earlier value-level work (Cabibbo angle via Gatto-Sartori-Tonin, openly borrowed
  formula, different declared scope than this file's root-native-formula requirement) is
  unaffected by anything in this log.
