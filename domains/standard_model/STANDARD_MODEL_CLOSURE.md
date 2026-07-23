<!-- The honest "close the Standard Model" ledger. Read this before claiming anything about
     the SM in this project. It is a CLOSURE LEDGER, not a derivation of the SM. -->

# Standard Model — Closure Ledger (v1.13, node-level)

> **What "closed" means here.** We close what is provable and mark the wall precisely. This is
> **not** a derivation of the Standard Model from the unrestricted retained root. The honest
> headline: **many nodes close, each at its own tier — some `Th_coqc` from the substrate, most
> `EXACT WITHIN A DECLARED FINITE ARCHITECTURE` (a minimal alphabet, a carrier, a coarse-reader
> map) — and the end-to-end physical Standard Model from the unrestricted root is STILL OPEN.**
> Do not compress this into "three remaining bottlenecks" — the open surface has grown *more*
> precise, not smaller; see §3.

Every row points at a runnable verifier (`… .py`, PASS) and/or a machine-checked Coq witness
(`… .v`, `Print Assumptions` **Closed over ℚ**). Run them all: `python3 run_tests.py` (24
verifiers + 24 Coq witnesses as of v1.13, all PASS/Closed).

**Status vocabulary** used below (never blur these):
- `EXACT` — a genuine root-native `Th_coqc` result, no declared finite architecture needed.
- `EXACT_WITHIN_DECLARED_ARCHITECTURE` — `Th_coqc`, but conditional on a stated minimal alphabet /
  carrier / gate set (e.g. the blind matter search's `{1,3,3̄}×{1,2}` alphabet, or v1.9's binary
  orientation+incidence carrier). Uniqueness/derivation claims are scoped to that architecture only.
- `CONDITIONAL` — exact given an unproven premise from elsewhere in the arc (e.g. weak chirality
  given `⟨Ξ⟩≠0`; order condensation given `Π₀>α`).
- `FINITE_FIXTURE` — a blind/finite-blind discriminator result, not yet a root Coq witness.
- `NUMERICAL_NOT_INTERVAL` — high-precision numerical, not a rigorous interval/exact-rational proof.
- `CALIBRATION_ONLY` — fit to CODATA/PDG for consistency-checking, not a prediction.
- `OPEN` — not established here.
- `SUPERSEDED` — a prior result in this ledger that is now known WRONG and must not be cited.

---

## §1. Gauge substrate
| node | result | status | witness |
|---|---|---|---|
| Discrete connection | `U=V_j⁻¹V_i` | `EXACT` | `InfoConnectionFromFrame` |
| SO(3) holonomy, curvature≠0 | one hand-picked rational rotation pair | `CORRECTED 2026-07-23: WITNESS_ONLY` (its own header: "a specific pair, not a parametrized theorem for all rational rotations" — not a general SO(3) result; do not cite as closing G0.5) | `InfoRationalSO3Curvature` |
| SM-G0.1/G0.2 automorphism-as-gauge kernel | path composition is a monoid; `Aut(F,O)` closed under composition+identity+inverse, for **arbitrary** `(S,R,F,O)` | `EXACT` (fully general, no domain alphabet) | `InfoGaugeAutomorphismGroup.v` (2026-07-23) |
| SM-G0/G0.6 order defect | commutator from plain 2×2 rational composition; Jacobi derived | `EXACT` (borrow #2 *reduced*, not removed — non-commuting pair still hand-exhibited) | `InfoOrderDefectFromComposition.v` |
| SM-G0.3–G0.5 (localization, connection-law-as-theorem, general holonomy invariance) | — | `OPEN` (no Coq witness yet) | — |

## §2. Color and confinement
| node | result | status | witness |
|---|---|---|---|
| Color number 3 / SU(3) / Z₃ | ordered closed tape ⇒ oddness `(−1)^{k−1}=1` ⇒ k odd ⇒ k=3 ⇒ SU(3)+Z₃+dim 8 | `EXACT_WITHIN_DECLARED_ARCHITECTURE` (oddness derived, not "3 colors" posited) | `ordered_tape_closure_v0_2.py`, `InfoOrderedTapeClosure.v` |
| Center-sector confinement | `⟨W(C)⟩=q(κ)^{A(C)}` ⇒ area law `σ=−log q>0` | `EXACT`, **Z₃/2D only** | `center_confinement_v0_3.py`, `InfoCenterConfinement.v` |
| Confinement certificate (SU(3)) | `𝔠_t=μ_4·ρ_t<1`: rigorous `0<κ<0.0020252`, candidate `κ≲0.053` | `EXACT` (rigorous small-κ) + `NUMERICAL_NOT_INTERVAL` (candidate) | `retained_confinement_certificate_v0_5.py`, `InfoConfinementCertificate.v` |
| Triality spectral flow (RG of ρ_t) | `ρ_t(b)=ρ_t^{b²}`; block-scale existence theorem | `EXACT` (serial) + `CONDITIONAL` (4D correlation defect open) | `triality_spectral_flow_v0_6.py`, `InfoTrialitySpectralFlow.v` |
| Corrected certificate + all-order u,v | `‖P‖≤1`; criterion `μ_4·û<1` (linear, corrects a v0.7 bug); Weyl integrals to all orders | `EXACT` (projector/criterion) + `NUMERICAL_NOT_INTERVAL` (u,v) | `retained_metric_intertwiner_v0_9.py`, `all_order_character_v1_0.py` |
| Surface automata (lower + upper) | bracket `μ_4^admissible∈[3.875,7.084]`, window `κ<0.321687` | `EXACT_WITHIN_DECLARED_ARCHITECTURE` | `surface_automaton_v1_1.py`, `surface_upper_automaton_v1_2.py` |

## §3. Matter and hypercharge
| node | result | status | witness |
|---|---|---|---|
| Algebra + representation discovery (blind, v0.4) | center=1, ideals 8⊕3 → `u(1)⊕su(3)⊕su(2)`; 5 blocks `(3,2)+(1,2)+(3,1)×2+(1,1)` | `FINITE_FIXTURE` (blind, negative controls pass) | `sm_discovery_pipeline_v0_4.py` |
| Hypercharge + cubic anomaly (v0.4/v1.5) | `q=1/6,ℓ=−1/2,u=2/3,d=−1/3,e=−1`; `[U(1)]³=0` exact; `A₁₁₁=(A_grav)³` factorization; Z₆ global quotient | `EXACT_WITHIN_DECLARED_ARCHITECTURE` (conditional on the one-generation skeleton) | `InfoHyperchargeAnomalyClosure.v`, `InfoHyperchargeGlobalQuotient.v` |
| **Blind matter-skeleton search (v1.6)** | `(3,2)+2(3̄,1)+(1,2)+(1,1)`, `D=15`, unique up to conjugation, unbounded via `lia` — **found, not fed** | `EXACT_WITHIN_DECLARED_ARCHITECTURE` (minimal alphabet `{1,3,3̄}×{1,2}`; uniqueness over ALL reps OPEN) | `blind_matter_search_v1_6.py`, `InfoBlindMatterSearch.v` |

## §4. Chirality and kinetic structure
| node | result | status | witness |
|---|---|---|---|
| Chirality (v0.4 pipeline) | orientation op → `η_χ=1` chiral vs `0` vectorlike | `CONDITIONAL` (needs a *given* `J_ord`) | `sm_discovery_pipeline_v0_4.py` §2 |
| Root-native chirality grading + no-go (v1.7) | `Γ_T` exact involution; no-go: unbroken reversal ⇒ equal weak reps | `EXACT` (grading) + `CONDITIONAL` (weak selection needs `⟨Ξ⟩≠0`) | `root_native_chirality_v1_7.py`, `InfoRootChirality.v` |
| Ginsparg–Wilson kinetic operator + no-doubling (v1.8) | `Γ(I−V)+(I−V)Γ=(I−V)Γ(I−V)`; free fixture 16→1+15 lifted | `EXACT` (finite fixture; free case only) | `tape_kinetic_operator_v1_8.py`, `InfoTapeKineticGW.v` |
| Interacting chiral gauge measure | — | `OPEN` | — |

## §5. Spacetime shadow
| node | result | status | witness |
|---|---|---|---|
| d=4 relation channels (v1.9) | `d≤4`, `d` even, `d≠2` (spectator), explicit 4-channel realization | `EXACT_WITHIN_DECLARED_ARCHITECTURE` (binary orientation+incidence carrier) | `relation_channel_dimension_v1_9.py`, `InfoDimensionFourClosure.v` |
| Isotropic fixed point (v1.10) | twirl `Π₄=(Tr/4)I`; contraction `ρ_frame=0.858010754588<1` | `EXACT_WITHIN_DECLARED_ARCHITECTURE` (a declared coarse-reader map) | `isotropic_fixed_point_v1_10.py`, `InfoIsotropicFixedPoint.v` |
| Frame weights from the action (v1.11) | `p(h)` derived from a reflection-positive Gram slab; `ρ_aniso=0.7361824549886<0.858` | `EXACT_WITHIN_DECLARED_ARCHITECTURE` (weights derived; the underlying cost ratios still input) | `frame_mixing_from_action_v1_11.py`, `InfoFrameMixingAction.v` |
| Full interacting Lorentz continuum | — | `OPEN` | — |

## §6. Order/Higgs
| node | result | status | witness |
|---|---|---|---|
| Minimal order carrier + stabilizer (v1.12) | `H=(1,2)_{1/2}` forced; `Q_res=T₃+Y`; neutral matrix `det=0` rank1; `m_W=m_Z cosθ`, `ρ=1`; DOF `8+4=2+9+1` | `EXACT_WITHIN_DECLARED_ARCHITECTURE` (given nonzero order) | `order_higgs_closure_v1_12.py`, `InfoOrderHiggsClosure.v` |
| Order-vacuum criterion (v1.13, **corrects a superseded draft**) | `ν=(1,1,1)` ≠ rank `(3,3,1)`; Fock factor `(1+λ_jr)^{d_j}`, `Z_j(0)=1`; `Π₀=3λ_U+3λ_D+λ_E>α ⇒` order; automatic convexity; no-go `Π₀≤7` | `EXACT` (counting/Fock factor) + `CONDITIONAL` (whether `Π₀>α` is FORCED, not just possible) | `intertwiner_order_vacuum_v1_13.py`, `InfoIntertwinerOrderVacuum.v` |
| ~~Exponential closure ansatz `1+ζe^{κr}`~~ | wrongly kept nonzero weight at `H=0` (violates linearity-in-`H`) | `SUPERSEDED` — do not cite | *(removed from canonical files; see v1.13 for the correction)* |

## §7. Mass reader and spectrum
| node | result | status | witness |
|---|---|---|---|
| Electroweak decoder (v0.3) | rank-1 obstruction ⇒ photon massless emergent; held-out tree `M_Z` 0.011% | `EXACT` (structural core) + `CALIBRATION_ONLY` (v, g, g') | `electroweak_decoder_v0_3.py`, `InfoElectroweakNullDirection.v` |
| Finite-transfer gap theorem (v1.3) | `q=‖𝕋P_⊥‖<1 ⇒ Δ=−(1/a)log q>0` | `EXACT` (finite-transfer half only) | `finite_transfer_gap_v1_3.py`, `InfoFiniteTransferGap.v` |
| Universal reflection-positive slab (v1.4) | `T_UF⪰0` across all sectors; one reader `m=−(1/a)log λ` | `EXACT` (formal internal pass) + reader unit-test (reads masses **back**, not a prediction) | `universal_rp_slab_v1_4.py`, `InfoUniversalRPSlab.v` |
| Physical pole masses from a real spectral transfer | — | `OPEN` | — |

## §8. Generations and mixing
All `OPEN`: generation count, CKM/PMNS, Yukawa coefficients, mass hierarchy, neutrino architecture.

## §9. Continuum and radiative physics
| node | result | status | witness |
|---|---|---|---|
| Radiative engine (v0.4) | finite log-det curvatures `(r1,r2,r3)=(−153/20,−243/20,−216/5)` | `FINITE_FIXTURE` (**NOT** physical β-functions — no ghost/orbit-volume subtraction) | `sm_discovery_pipeline_v0_4.py` §7–8 |
| Continuum Yang–Mills mass gap | — | `OPEN` (this is the Clay Millennium Problem; not claimed) | — |
| Gauge-orbit fluctuation Hessian, regulator-independence | — | `OPEN` | — |

## §10. Empirical predictions
All `OPEN`: scattering amplitudes, decay rates, cross sections. Nothing in this ledger predicts a
number that was not first put in for calibration-consistency (`CALIBRATION_ONLY` rows only).

---

## What is genuinely closed (do not undersell)
- The **gauge substrate** (connection/holonomy/curvature) and the **order defect** are `EXACT`
  (root-native `Th_coqc`, no declared architecture needed).
- Within their declared architectures: hypercharges + Z₆ quotient, a **blind** one-generation
  matter skeleton (found, not fed), an ordered-tape chirality grading + exact no-go, a
  Ginsparg–Wilson kinetic operator with no doubling in the free fixture, a **derived** `d=4`, an
  isotropic fixed point whose mixing weights are themselves derived from a reflection-positive
  slab of the action, a **forced** minimal order carrier with its vector mass-rank pattern, and a
  corrected order-vacuum criterion from actual intertwiner-rank counting — all `Th_coqc`.
- The photon's masslessness **emerges** from a rank-1 obstruction (not imported); the electroweak
  decoder calibrates to CODATA/PDG with a held-out tree-level `M_Z` at 0.011%.
- Every discriminator/search this session is **blind**: the skeleton, the reps, the charges, the
  order carrier are never fed; every stage carries a failing/negative control.

## §11. The wall — what must NOT be claimed
End-to-end **physical Standard Model from the unrestricted root = 0%**. The open surface is now
tracked **per node** (§1–§10 above), not as a fixed bottleneck count — collapsing it back into
"three bottlenecks" would hide real progress on some fronts and real gaps on others. The load-
bearing open items, by category: SM-G0.3–G0.5 as Coq witnesses (§1; G0.1/G0.2 closed 2026-07-23); the 4D correlation defect and
continuum `σ_phys` (§2); uniqueness of the matter skeleton over ALL representations, not just the
declared minimal alphabet (§3); `⟨Ξ⟩≠0` and interacting chiral gauge measure (§4); the primitive
cost ratios behind isotropy and full interacting Lorentz covariance (§5); whether `Π₀>α` is FORCED
(§6); real spectral-transfer pole masses (§7); everything in §8–§10.

Also never conflate: `Ξ∈{+1,−1}` (orientation order, chirality selector, v1.7) with
`H=(1,2)_{1/2}` (electroweak order carrier, v1.12–v1.13) — distinct records, distinct roles.
Never cite the superseded exponential order-closure ansatz (§6) as canonical.

## One-line verdict
> **Root-Native Standard-Model Architecture: substantial conditional and node-level closure —
> not a complete Standard Model derived from the unrestricted root.** Saying exactly this is the
> closure.
