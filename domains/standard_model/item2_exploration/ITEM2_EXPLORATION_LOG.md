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
- Nothing here touches `CLAIM_BOUNDARY.json` or any `run_tests.py` verifier — these are
  exploratory files, not wired into the domain's closed-claim registry.
