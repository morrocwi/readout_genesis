<!-- Exploratory scoping log, NOT a claim of closure for items 25/26. Committed for continuity,
     same pattern as mu4_exploration/MU4_INVESTIGATION_LOG.md. Items 25 and 26 in
     HANDOFF_NEXT_SESSION.md remain FULLY OPEN after this session -- nothing here closes them.
     The one artifact this session produced (beta_function_coefficients_v1.py, item 34's
     separable group-theory sub-piece) is a genuinely narrower, adjacent, honestly-scoped result
     -- see that file's own HONEST FENCE for exactly what it does and does not establish. -->

# Scoping log — items 25 & 26 (real one-loop β-functions, continuum limit), 2026-07-24

## What was asked

`HANDOFF_NEXT_SESSION.md` §2 P2:
- item 25: "Gauge-orbit fluctuation Hessian (ghost/orbit-volume subtraction, polarization
  counting) for real one-loop β-functions — §9; v0.4's radiative engine is explicitly NOT this"
- item 26: "Regulator-independence / genuine continuum limit — §9"
- item 34 (adjacent, checked as a possible easier target): "AP10 one-loop β-slope kinematic
  weights (11/3, 2/3, 1/3) derived from root — representation content is currently SM input; the
  three weights themselves are not derived"

## 1. Status read of the existing "v0.4 radiative engine" (why it is explicitly NOT items 25/26)

`sm_discovery_pipeline_v0_4.py` §§7-8 computes three numbers it calls `(r1,r2,r3) =
(-153/20, -243/20, -216/5)`. Read the file's own header and in-line disclaimers (this session
verified by running it, `All checks PASS`, output unchanged):

> "HONEST VERDICT (founder): ... the radiative-correction engine only to a FINITE SPECTRAL
> DIAGNOSTIC level. This is NOT a full end-to-end derivation ... Radiative engine (finite
> log-det) : FINITE DIAGNOSTIC PASS ... The three remaining bottlenecks (not four): (i)
> root-derived orientation/spin-statistics, (ii) the gauge-orbit fluctuation Hessian, (iii)
> continuum / held-out radiative validation."

and, immediately at the computation itself (line 213):

> `ck("HONEST FENCE: (r1,r2,r3) are RAW finite log-det curvatures, NOT one-loop SM beta
> coefficients", True)`

Mechanically: `r_a = Tr(K0^-1) * (-Σ_matter C2_a(R)·dim(R) + C2_a(H)·dim(H))`, where `K0 = L + I`
is built from the spectrum of a **6-cycle graph Laplacian** (`specL = [0,1,1,3,3,4]`), an
arbitrary finite fixture with no connection to an actual gauge-fixed path integral, no ghost
fields, no orbit-volume subtraction, and no momentum-space loop integral of any kind. It reuses
the same Casimir/hypercharge data as the beta-function group-theory formula (coincidentally,
`C2_2`, `C2_3` in that file are literally the same SU(2)/SU(3) Casimirs used here) but combines
them with a graph-spectral trace, not a loop-diagram computation — a structurally different
object that happens to share some inputs. `STANDARD_MODEL_CLOSURE.md` §9 independently confirms
this reading: `Radiative engine (v0.4) | finite log-det curvatures ... | FINITE_FIXTURE (**NOT**
physical β-functions — no ghost/orbit-volume subtraction)`.

**Confirmed: this is genuinely not items 25/26**, and this session did not reuse, lightly modify,
or re-claim it.

## 2. Item 34 investigated as the adjacent target — what's tractable, what isn't

The real-physics formula (`beta_function_coefficients_v1.py`'s docstring, EQUATION_REGISTRY.md
entry added this session) splits cleanly into two structurally different pieces:

- **(A) Group-theory data** — `C2(G_a)` (Casimir of the adjoint) and `T_a(R)` (Dynkin index of
  each matter representation). This depends ONLY on which representations exist — exactly the
  matter content this repo already fixed in `hypercharge_global_quotient_v1_5.py` /
  `sm_discovery_pipeline_v0_4.py`.
- **(B) Loop-kinematic weights** — the numbers `11/3, 2/3, 1/3` themselves, plus the `3/5` GUT
  hypercharge normalization. These come from an actual perturbative loop calculation: the
  one-loop vacuum-polarization diagram in a gauge-fixed theory, including the Faddeev-Popov
  ghost contribution. They are the SAME three numbers for any gauge theory with the SM's field
  content PATTERN (1 vector multiplet + Weyl fermions + complex scalars) regardless of which
  representations or which gauge group — i.e. they carry NO representation-theoretic content at
  all, so no amount of Casimir/Dynkin-index bookkeeping can produce them.

**Tried and confirmed tractable:** (A) alone. `beta_function_coefficients_v1.py` recomputes
`C2(G_a)` and `Σ T_a(R)` from this repo's own already-fixed matter content (exact `Fraction`
arithmetic, `ck()` harness, run and confirmed `DECISION: PASS`), and — combined with (B) taken as
an EXPLICITLY LABELED EXTERNAL input, never computed — reproduces the real, independently-known
SM one-loop coefficients `b3=7`, `b2=19/6`, `b1=-41/10` exactly. This is a genuine, if narrow,
piece of new honest progress: AP10 previously existed ONLY as a prose/table reference
(`ROOT_TO_SM_DAG.md`, `STANDARD_MODEL_CLOSURE.md`, `CLAIM_BOUNDARY.json` all cite it; grep
confirms **no file anywhere in this repo previously computed it** — `grep -rl "AP10"
--include="*.py" .` returns nothing before this session). It is now a checked artifact, not just
a claim.

**Confirmed NOT tractable (searched, did not find any shortcut):** deriving (B) — the three
weights themselves — from anything currently in this repo. `grep -rli` across `domains/quantum/`,
`domains/relativity/`, and all of `domains/standard_model/` for `propagator`, `path integral`,
`Feynman`, `momentum space`, `loop integral`, `ghost determinant`, `Faddeev-Popov`, `BRST`, `vacuum
polarization` returns essentially nothing usable (one incidental hit in
`domains/quantum/DRIFT_CONTRACT.json`, not a construction). There is no gauge-fixed measure, no
propagator, no loop-momentum integral, no ghost sector anywhere in this codebase. Deriving `11/3,
2/3, 1/3` from root would require building that machinery from scratch — which is precisely what
item 25 ("gauge-orbit fluctuation Hessian, ghost/orbit-volume subtraction, polarization
counting") names as missing, and what item 26 (regulator-independence / continuum limit) would
then need to make sense of at all (a loop integral is only well-defined once a regulator and its
removal are specified).

## Conclusion — items 25/26 are NOT closed, NOT partially closed, by this session

- **Item 25**: fully OPEN. No gauge-orbit fluctuation Hessian, ghost sector, or polarization
  counting exists anywhere in this repo, before or after this session.
- **Item 26**: fully OPEN, and untouched — it presupposes item 25's machinery exists first (you
  cannot ask "is the continuum limit regulator-independent" of a loop calculation that does not
  exist).
- **Item 34**: re-scoped, not closed. It splits into a group-theory half (now closed as a checked
  `finite_diagnostic` artifact, `beta_function_coefficients_v1.py`) and a loop-kinematic-weight
  half that is **confirmed identical in kind** to item 25's blocker — not a separate, easier
  problem, and not reachable by any representation-theory technique, however extended.

## What would actually need to exist before items 25/26 become attemptable at all

A genuine path-integral measure / gauge-fixing + ghost-determinant construction built from this
repo's own root primitives (the graph-Laplacian retained-distinction operator `L_R`, the
discrete connection `U=V_j⁻¹V_i`, curvature `K_C`, etc. — see `ROOT_TO_SM_DAG.md`). Concretely,
at minimum:
1. A discrete analogue of the gauge orbit (the space of connections modulo gauge transformations
   `h_i`) with an actual volume/measure on it — nothing in this repo currently defines "the set
   of all connections" as an object with a measure; only single connections/holonomies are built.
2. A Faddeev-Popov-style ghost sector or an equivalent orbit-volume-subtraction device, derived
   from — not imported into — this framework's own retained-distinction vocabulary (the `readout-
   not-truth` discipline explicitly forbids importing the continuum path integral wholesale; a
   finite, discrete analogue would need to be built and shown to reduce to the standard
   Faddeev-Popov result in an appropriate limit, itself a nontrivial research question).
3. A genuine one-loop fluctuation determinant (Hessian of the action around a background
   connection) computed on this repo's own finite graph/lattice objects, analogous to how
   `sm_discovery_pipeline_v0_4.py`'s `Tr K0^-1` is a log-det trace — but of the ACTUAL gauge
   action's second variation, not an arbitrary 6-cycle fixture.
4. Only once (1)-(3) exist does "regulator-independence / continuum limit" (item 26) become a
   well-posed question at all — currently there is no regulator-dependent object to take a limit
   of.

None of (1)-(4) exist in any form in this repo as of this session. This is the precise, named
blocker — turning "vague backlog item" into "four concretely missing pieces" is the actual
deliverable of this half of the investigation.

## Files touched this session (all new, nothing pre-existing modified)

- `domains/standard_model/item25_exploration/beta_function_coefficients_v1.py` — the tractable
  group-theory sub-piece of item 34 (finite_diagnostic tier, run and confirmed `DECISION: PASS`).
- `domains/standard_model/item25_exploration/ITEM25_26_SCOPING_LOG.md` — this file.
- `docs/root/EQUATION_REGISTRY.md` — two new rows (one-loop non-abelian gauge β-function
  group-theory formula; GUT hypercharge normalization 3/5), registered at first use per this
  repo's standing rule.
