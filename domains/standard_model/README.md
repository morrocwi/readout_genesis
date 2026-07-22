<!-- Standard Model: a FRONTIER with node-level closures, not one closed domain. -->

# ⚛️ Standard Model — FRONTIER (node-level closures, no single end-to-end verifier)

> **This folder is different from `chem/`, `relativity/`, `quantum/`, `biology/`.** Those are
> *registered* domains with one closure percentage. This is a **DAG of nodes**: each node has its own
> Python verifier + Coq witness (`run_tests.py` — 24 verifiers + 24 Coq witnesses as of v1.13, all
> PASS/Closed). There is **no single end-to-end Standard Model verifier by design** — do not read
> node-level PASS as end-to-end closure, and do not deny the nodes exist either.
> **End-to-end root-derived Standard Model (unrestricted root) = 0%.**

## The one rule
The Standard Model must be a **domain — a translation of the retained structure — not a new root**,
and must **not** import `SU(3)×SU(2)×U(1)`, quarks, leptons, the Higgs, or the gauge equations as
*premises*. The same names ARE allowed as discovered/labelled endpoints, comparisons, or semantic
labels attached AFTER a derivation (see `DRIFT_CONTRACT.json` for the exact premise-vs-endpoint
scope). Gauge is, first, **the non-uniqueness of the internal description under the same checkable
readout**: `Aut(F,O) = { h : O∘h = O, h∘F = F∘h }` — the weld of core §V.20.

## Where to look
- **[`INDEX.md`](INDEX.md)** — the version timeline (v0.1→v1.13): every verifier + Coq witness + tier
  + one-line honest status. **Read this first**, kept in lock-step with `run_tests.py`.
- **[`STANDARD_MODEL_CLOSURE.md`](STANDARD_MODEL_CLOSURE.md)** — the node-level closure matrix (ten
  categories, each node individually tiered: `EXACT` / `EXACT_WITHIN_DECLARED_ARCHITECTURE` /
  `CONDITIONAL` / `FINITE_FIXTURE` / `CALIBRATION_ONLY` / `OPEN` / `SUPERSEDED`). Read this before
  citing any specific claim's scope.
- **[`SM_INFORMATION_PHILOSOPHY_MASTER.md`](SM_INFORMATION_PHILOSOPHY_MASTER.md)** — the canonical
  narrative synthesis (root → color → confinement → hypercharge → matter → chirality → kinetic →
  spacetime → order/Higgs), same tier discipline, prose form.
- **[`MASS_GAP_INFORMATION_PHILOSOPHY.md`](MASS_GAP_INFORMATION_PHILOSOPHY.md)** — the root-native
  mass-gap program + the universal reflection-positive mass slab. **NOT** the Clay Yang–Mills mass
  gap (OPEN); a finite-scale theorem + a universal mass reader.
- **[`ROOT_TO_SM_DAG.md`](ROOT_TO_SM_DAG.md)** / **[`UNIFIED_FORCE_DAG.md`](UNIFIED_FORCE_DAG.md)** —
  the DAG maps, each node carrying **two axes**: root/formal status (a Coq witness from an
  unrestricted root?) and architecture/discovery status (closed within a declared finite
  architecture — a minimal alphabet, a carrier, a coarse-reader map?). Never collapse the two.
- `CLAIM_BOUNDARY.json` — machine-readable per-claim tier fence (`established` / `not_established`,
  one entry per registered version).
- `DRIFT_CONTRACT.json` — the hard-fail conditions that keep this a domain-translation, never a root;
  scoped as premise-position rules, not blanket word bans.
- `source_root/READOUT_GENESIS_CORE_SNAPSHOT.md` — the return anchor to the master equation.

## Latest registered version
**v1.13** (`intertwiner_order_vacuum_v1_13.py` + `InfoIntertwinerOrderVacuum.v`) — see `INDEX.md` for
the full chain v0.1→v1.13. Two distinct order-type records are in play and must never be conflated:
`Ξ∈{+1,−1}` (orientation order, selects weak chirality, v1.7) and `H=(1,2)_{1/2}` (the electroweak
order carrier, `⟨H†H⟩` sets the vector-mass scale, v1.12–v1.13).

## What is already ours (verified `Th_coqc`, root-native substrate) vs open
- 🟩 **substrate**: discrete connection (`InfoConnectionFromFrame`), SO(3) holonomy + curvature
  (`InfoRationalSO3Curvature`), a non-abelian **Heisenberg group** from the seed
  (`InfoSeedTorsionGroupAndRankN`), a proven gauge invariance (`InfoScaleGaugeNonReadout`), Noether
  (`InfoGraphNoether`).
- 🟨 **exact within a declared finite architecture** (see `INDEX.md` v1.5–v1.13): hypercharge + Z₆
  quotient, a **blind** matter-skeleton search, an ordered-tape chirality grading + no-go, a
  Ginsparg–Wilson kinetic operator + no-doubling fixture, a **derived** `d=4`, an isotropic fixed
  point with weights derived from a reflection-positive slab, a **forced** minimal order carrier
  with its vector mass-rank pattern, and a corrected intertwiner-rank order criterion.
- 🟥 **open (must not be faked)**: SM-G0.1–G0.5 (the automorphism-as-gauge kernel proper, as a Coq
  witness), gauge-algebra uniqueness over the *unrestricted* root (**`SU(3)` is still the wall** at
  that level), `⟨Ξ⟩≠0` and `Π₀>α` FORCED (not merely possible) from an action, interacting chiral
  gauge measure, three generations/mixing, every physical coupling constant and mass (`α` is
  *rejected-not-faked*). The Quantum domain (§V.18) is a prerequisite for spin-statistics.

## Progress on SM-G0 (the kernel) + v0.2 circulation + v0.3 electroweak decoder
- 🟩 **SM-G0 / G0.6 order-defect from ordered composition** — `Th_coqc`
  ([`InfoOrderDefectFromComposition.v`](InfoOrderDefectFromComposition.v), Closed over ℚ). The
  commutator is derived from **plain 2×2 rational matrix composition** (no non-commuting term written
  in); associativity + **Jacobi** are theorems; commuting ⇒ zero defect. This **reduces AP20's borrow #2**
  (the commutator): its *form* is now theorem-level (Jacobi/antisymmetry derived), **but does not remove
  it** — the non-abelian input still rests on an un-forced non-commuting pair. Self-carrier closure (#3)
  and the common load A4 (#4) are **still fully borrowed/OPEN**; `c_self/c_geo=1` is **not** root-derived.
- 🟦 **Four-Force Circulation v0.2 (fixture scheme)** — `[SimulatedData/FiniteFormalWitness]`
  ([`four_force_circulation_v0_2.py`](four_force_circulation_v0_2.py) PASS +
  [`InfoFourForceCirculationRecovery.v`](InfoFourForceCirculationRecovery.v) Closed). On a **known**
  four-sector ring fixture `A=H+Ω`: the non-trivial exact identity `χ−χᵀ=−2χᵀΩχ` (measurable
  nonreciprocity = circulation conjugated by χ), and `Ω_recovered=Ω_planted` as the unique **antisymmetric
  part** of `χ⁻¹` — exact **by construction** (sym/antisym split), *not* tomography of an unknown — with
  reciprocal + missing-edge controls. Labels `(G,EM,W,S)` are decoder names, not calibrated forces.
- 🟩/🟦 **v0.3 CALIBRATED ELECTROWEAK DECODER (EM↔Weak)** — `Th_coqc` structural core + calibration
  ([`electroweak_decoder_v0_3.py`](electroweak_decoder_v0_3.py) PASS +
  [`InfoElectroweakNullDirection.v`](InfoElectroweakNullDirection.v) Closed). The neutral obstruction is
  **rank-1** ⇒ `det=0` identically ⇒ **the photon's masslessness EMERGES** (photon `~(g',g)`, `Z~(g,−g')`
  with `m_Z²=(v²/4)(g²+g'²)`), failing control = generic rank-2 ⇒ no massless direction. Calibrated to
  CODATA2022/PDG2025 (`v=246.21965 GeV`, `g=0.652824`, `g'=0.349784`); held-out tree-level
  `M_Z=91.178` vs PDG `91.188` (0.011%). **Label: CALIBRATED ELECTROWEAK DECODER, not SM-from-root** —
  gauge algebra, chirality, `θ_W` value, radiative corrections OPEN.

## Next step — two parallel tracks
1. **Root-debt track:** close the rest of **SM-G0**: gauge redundancy + the connection transform +
   curvature from retained readout-equivalence as one Coq kernel (G0.1–G0.5), and discharge AP20's
   remaining borrows (#3 self-carrier, #4 the common quadratic load).
2. **Downstream closure track** (v1.14+): derive the primitive intertwiner costs
   `Δ_j,ε₃,ε_±,α,β` from the tape/closure grammar to test whether `Π₀>α` (v1.13) is FORCED, not
   merely possible; then the physical order-spectrum audit and generation multiplicity.
Neither track substitutes for the other — the root-debt track grounds the *architecture* declared by
the downstream track; closing SM-G0 alone does not re-derive v1.5–v1.13, and closing v1.14+ alone
does not remove the unrestricted-root debt.
