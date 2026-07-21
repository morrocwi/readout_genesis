<!-- Standard Model: a FRONTIER ROADMAP, not a closed domain. Read ROOT_TO_SM_DAG.md. -->

# ⚛️ Standard Model — FRONTIER (roadmap, not a closed domain)

> **This folder is different from `chem/`, `relativity/`, `quantum/`, `biology/`.** Those are
> *registered* domains with a passing verifier and a measured closure %. This one is a **roadmap**:
> a DAG of where to start and an honest ledger of what is still open. **End-to-end root-derived
> Standard Model = 0%.** Do not read anything here as a Standard Model derivation.

## The one rule
The Standard Model must be a **domain — a translation of the retained structure — not a new root**,
and it must **not** import `SU(3)×SU(2)×U(1)`, quarks, leptons, the Higgs, or the gauge equations as
premises. Gauge is, first, **the non-uniqueness of the internal description under the same checkable
readout**: `Aut(F,O) = { h : O∘h = O, h∘F = F∘h }` — the weld of core §V.20.

## Contents
- **[`UNIFIED_FORCE_DAG.md`](UNIFIED_FORCE_DAG.md)** — one action → four force projections (gravity/EM/weak/strong as readouts of one `S_UF`, not four theories added); core §V.22.
- **[`ROOT_TO_SM_DAG.md`](ROOT_TO_SM_DAG.md)** — the full root-native DAG, the survey of existing
  verified assets, the honest per-node tiers, and **SM-G0 (the Gauge Emergence Kernel)** = where to
  start (six proofs + failing controls).
- `CLAIM_BOUNDARY.json` — tier `FRONTIER_ROADMAP`, what is established (the gauge *substrate*) vs the
  large not-established list.
- `DRIFT_CONTRACT.json` — the hard-fail conditions that keep this a domain-translation, never a root.
- `source_root/READOUT_GENESIS_CORE_SNAPSHOT.md` — the return anchor to the master equation.

## What is already ours (verified `Th_coqc`, root-native) vs open
- 🟩 **substrate**: discrete connection (`InfoConnectionFromFrame`), SO(3) holonomy + curvature
  (`InfoRationalSO3Curvature`), a non-abelian **Heisenberg group** from the seed
  (`InfoSeedTorsionGroupAndRankN`), a proven gauge invariance (`InfoScaleGaugeNonReadout`), Noether
  (`InfoGraphNoether`).
- 🟥 **open (must not be faked)**: the automorphism-as-gauge derivation, the gauge group (**`SU(3)`
  is the wall**), matter representations, chirality/anomaly, three generations, mixing, the full
  Higgs mechanism, and every coupling constant (`α` is *rejected-not-faked*). The Quantum domain
  (§V.18) is a prerequisite.

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

## Next step
Close the rest of **SM-G0**: gauge redundancy + the connection transform + curvature from retained
readout-equivalence as one Coq kernel (G0.1–G0.5), and discharge AP20's remaining borrows (#3
self-carrier, #4 the common quadratic load). Only then does the rest of the DAG have a real root to
stand on.
