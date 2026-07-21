<!-- Verified upgrades pulled from the causal-quantum-gravity Coq corpus (best-version audit), quantum domain. -->

# Provenance — causal-quantum-gravity Coq upgrades (2026-07-21), quantum domain

The founder's derivation gave this domain its *finite root witnesses* (exact-rational,
`quantum_closure_v0_1.py`). Several nodes have a **stronger, machine-checked** backing already in the
sibling repo `causal-quantum-gravity/` (public curated export, `make verify` CI-green — 81 formal
files). Those are folded in here as GREEN root theorems — but only after each cited `.v` was
**re-verified locally** (compiled with `coqc -q -R . DQG`, and grep-clean of `Admitted`/`admit`/
`Axiom`/`Parameter`) on 2026-07-21. Nothing is tagged `Th_coqc` on the strength of a filename or a
claimed tag.

**Status taxonomy** (per founder, 2026-07-21, same taxonomy as `relativity/PROVENANCE_CAUSAL_QG.md`):
`green` = Coq/formal closed · `yellow` = theorem closed but the *physical/semantic* bridge is partial
(FORMAL-CLOSED / BRIDGE-PARTIAL) · `red` = open · `gray` = measured/calibration adapter.

## Verified GREEN (compiled clean + axiom-grep clean here, 2026-07-21) — usable as `Th_coqc`

| quantum node | causal-quantum-gravity file | key theorem(s) | what it earns |
|---|---|---|---|
| forced-L_R (Q-R3) | `formal/InfoRetainedDistinctionForcesLaplacian_attempt.v` | retained-distinction axioms force the L_R (Laplacian-shaped) operator form | the retention operator's form is **forced**, not merely posited — closes the "why L_R and not some other operator" gap |
| seed trifurcation (Q-S1) | `formal/InfoAsymmetricSeedTrifurcation.v` | `R0 = DiagPart + SymOff + SkewOff`, exact and unique | the asymmetric seed decomposes uniquely; SkewOff is the torsion/circulation branch |
| seed torsion group/rank-N (Q-S2) | `formal/InfoSeedTorsionIsSkewOff.v`, `InfoSeedTorsionGroupAndRankN.v` | torsion branch = SkewOff; group structure; rank-N extension | the torsion branch is algebraically closed as a group, extends beyond the 3×3 witness |
| seed torsion genuine mixing (Q-S3) | `formal/InfoSeedTorsionGenuineMixing.v` | genuine (non-coboundary-reducible) mixing from the torsion branch | the torsion branch produces real (non-trivial) mixing, not a disguised diagonal case |
| memory-before-mass, formal (Q-M1, folded into Q-Y5) | `formal/InfoMemoryBeforeMass.v` | retained memory sequence forces a strictly positive mass-like readout | discrete-algebra formal claim only — see YELLOW section for the physical bridge |
| metric/curvature chain (Q-G1, folded from relativity/OB-03,OB-04) | `formal/InfoConnectionFromFrame_attempt.v`, `InfoDiscreteRiemannCurvature_attempt.v` (+ supporting chain) | `coboundary_telescopes`, `closed_loop_pure_gauge_flat`, `genuine_curvature_is_non_coboundary`, `riemann_is_second_difference`, `curvature_nonzero_witness` | same witnesses as `relativity/RULE_REGISTRY.json` OB-03/OB-04 — cited, not re-derived, because the underlying `L_R` operator is shared root structure |

## Verified GREEN but tagged YELLOW here (formal-closed, physical/semantic bridge partial)

| quantum node | causal-quantum-gravity file | key theorem(s) | why it stays yellow |
|---|---|---|---|
| telegraph crossover discriminant (Q-Y2) | `formal/InfoTelegraphHorizonUnification_attempt.v`, `InfoTelegraphCrossover_attempt.v` | `disc_is_spine_discr`, `lam_c_is_spine_lambda_c`, `quantum_iff_above_horizon` | compiles axiom-free and names a real threshold, but the BRIDGE from "above/below the discriminant" to "this regime IS quantum" is not established — a threshold is not a semantic identification. **Distinct object** from `relativity/`'s node-8 lapse/redshift (`OB-07`/`GC-01..05`) — do not conflate them. |
| memory-before-mass, physical bridge (Q-Y5) | `formal/InfoMemoryBeforeMass.v` (same file as Q-M1 above) | (as above) | the formal algebra (Q-M1) is green; whether the readout IS physical mass is a DECLARED correspondence, parallel to `relativity/`'s `OC-02` (mass-memory declared correspondence) |
| QM/SR bounded algebraic identity (Q-Y1) | `formal/InfoQuantumRelativityUnification.v`, `InfoSeedFeedsQuantumRelativity_attempt.v` | `box_quad_is_spine_residual`, `spine_dispersion_iff_box_quad_vanishes` | compiles axiom-free, BUT `box_quad` **inherits the imported Minkowski signature** from `InfoLorentzInvariance.box_quad` — see REFUSED section below and `relativity/PROVENANCE_CAUSAL_QG.md`. This is a bounded ALGEBRAIC IDENTITY between two independently-posited constructions, **never** "QM and SR derived from one root." |

**Tier footnote:** as in `relativity/`, `InfoLorentzContinuum.v` and `InfoQuantumGravityRootBridge.v`
are `+reals` (Coq's standard-library Reals axioms `sig_forall_dec` + `functional_extensionality_dep`,
disclosed by the repo, not a hidden import) — honestly weaker than axiom-free `Th_coqc`; neither is
pulled in here.

## REFUSED — checked and NOT pulled in (would repeat the hollow-card mistake)

| file | why refused |
|---|---|
| `formal/InfoLorentzInvariance.v` and `URCF_RD_All.v` module `InfoGR2.GW` | Compiles `Th_coqc`/axiom-free, **but** imports the Minkowski `interval` and the boost constraint `γ²(1−v²)=1` as `Definition`s/hypotheses — **NOT forced by the graph root**. The repo's own `supplement/completeness-and-claims.md` (L28-32) says "POSITED, not forced by the graph root." This is exactly why `Q-Y1` (which depends on `InfoQuantumRelativityUnification.v`, which in turn depends on this file) is capped at YELLOW_BRIDGE_PARTIAL and never promoted to `Th_coqc` as a root-native QM/SR derivation. |
| `formal/InfoQuantumRelativityUnification.v` and `InfoSeedFeedsQuantumRelativity_attempt.v`, cited as a ROOT-NATIVE derivation | These files themselves compile axiom-free and ARE cited (as `Q-Y1`, YELLOW) — but only as a bounded algebraic identity. Citing them as "QM derived from one root" or as a `Th_coqc` root theorem is REFUSED; that overclaim would repeat exactly the secret-import hollow-card mistake the founder's anti-hollow-card discipline exists to catch. |
| `formal/InfoAnalysisLift.v` | Imports the Schwarzschild metric as a `Definition`, not derived — consistent with Schwarzschild staying `[DeclaredFormula]` in `relativity/`. Not usable here either. |
| `formal/InfoQuantumGravityRootBridge_attempt.v` | Imports the GR field-equation conclusion (`[Dr]`/import), not root-derived. Not usable as a root-native upgrade for `Q-X12` (QFT, which stays fully OPEN). |

## Discipline note

Every GREEN upgrade above is the **algebraic/structural** claim, machine-checked and root-native. None
of them promotes the domain past `QUANTUM_ROOT_CLOSURE_PARTIAL`: Born-rule uniqueness, measurement,
subsystem composition, entanglement provenance, spin/statistics, and QFT stay `red` (open) exactly as
in `quantum_closure_v0_1.py`'s own closure audit (14 green / 6 yellow / 12 red of 32). Machine-checked
structure ≠ real quantum mechanics — and, per the founder's core discipline for this domain,
**oscillation (the Q-OS1 spine-dispersion split) is NOT itself quantum**: it is a green formal witness
about a real-coefficient second-order stepper, nothing more, until state + norm + composition +
channel + measurement close together.
