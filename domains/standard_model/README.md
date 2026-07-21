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

## Next step
Close **SM-G0**: prove gauge redundancy, the connection transform, and curvature grow from retained
readout-equivalence, and lift AP20's borrowed commutator to a root-derived order defect. Only then
does the rest of the DAG have a real root to stand on.
