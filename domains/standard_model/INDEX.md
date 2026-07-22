<!-- Index only. The CANONICAL synthesis is SM_INFORMATION_PHILOSOPHY_MASTER.md; the ledger of
     record is STANDARD_MODEL_CLOSURE.md; the machine tier fence is CLAIM_BOUNDARY.json. This file
     adds no new claims — it points at those three. -->

# Standard Model — Version Index

> **Read first:** [`SM_INFORMATION_PHILOSOPHY_MASTER.md`](SM_INFORMATION_PHILOSOPHY_MASTER.md) — the
> canonical synthesis (root → SU(3) → Z₃ → confinement), with the honest split closed (§21) /
> conditional·numerical (§22) / not-yet-derived (§23). Use it as the primary reference to prevent
> drift back to importing external physics as a premise.
> **Mass program:** [`MASS_GAP_INFORMATION_PHILOSOPHY.md`](MASS_GAP_INFORMATION_PHILOSOPHY.md) — the
> root-native mass-gap analysis + proof DAG + the **universal reflection-positive mass slab** (§25).
> **NOT** a proof of the Clay Yang–Mills mass gap (OPEN); a finite-scale theorem + a universal mass reader.
>
> **Status: FRONTIER ROADMAP, not a closed domain.** End-to-end physical Standard Model from the root
> = **0%, OPEN**. Every row below is honestly fenced — see [`CLAIM_BOUNDARY.json`](CLAIM_BOUNDARY.json)
> and [`STANDARD_MODEL_CLOSURE.md`](STANDARD_MODEL_CLOSURE.md) before quoting any result out of context.

## At a glance

| what | value |
|---|---|
| End-to-end root-derived SM | **0% — OPEN** (chirality/spin-statistics · gauge-orbit Hessian · continuum/radiative) |
| Color / SU(3) / Z₃ center | conditionally derived (oddness of the minimal closed tape is a theorem) |
| Hypercharges + cubic anomaly | forced exactly, `Th_coqc` (given SM rep content as a fixture) |
| All-order character `u(κ), v(κ)` | closed to all orders, high-precision numerical (not an interval proof) |
| Link intertwiner | `‖P‖≤1` (contraction), `Th_coqc` — representation tail closed |
| Surface entropy bracket | **3.875 ≤ μ₄^admissible ≤ 7.084** |
| Confinement window | **κ < 0.321687** |

## Version timeline

| version | file (`.py`) | Coq witness (`.v`) | what it closes | tier | honest status |
|---|---|---|---|---|---|
| v0.1 unified_force_closure | `unified_force_closure_v0_1.py` | *(core `InfoConnectionFromFrame`/`InfoRationalSO3Curvature`)* | one action → four ORTHOGONAL projection readouts `F_all=F_G+F_EM+F_W+F_S+F_res` + `χ4` | finite/internal, PASS | `INTERNALLY_CLOSED_FINITE`; physical four-force unification OPEN |
| SM-G0/G0.6 order_defect | *(v0.1/v0.2 harnesses)* | `InfoOrderDefectFromComposition.v` | commutator + Jacobi **derived** from ordered composition; commuting ⇒ zero defect | `Th_coqc` | **reduces** AP20 borrow #2 (form), not removed; #3/#4 OPEN |
| v0.2 four_force_circulation | `four_force_circulation_v0_2.py` | `InfoFourForceCirculationRecovery.v` | exact `χ−χᵀ=−2χᵀΩχ`; `Ω` = unique antisym split of `χ⁻¹` | `[SimulatedData/FiniteFormalWitness]` | exact on a KNOWN fixture, not tomography; labels are decoder names |
| v0.3 electroweak_decoder | `electroweak_decoder_v0_3.py` | `InfoElectroweakNullDirection.v` | rank-1 obstruction ⇒ photon massless (emergent) + massive W/Z | `Th_coqc` + calibration | `CALIBRATED_ELECTROWEAK_DECODER`; tree `M_Z` 0.011% from PDG; algebra/chirality/θ_W OPEN |
| v0.4 sm_discovery_pipeline | `sm_discovery_pipeline_v0_4.py` | `InfoHyperchargeAnomalyClosure.v` | blind algebra `u(1)⊕su(3)⊕su(2)` + reps + **hypercharges forced + cubic anomaly =0** | `FINITE_BLIND` (+`Th_coqc` on hypercharge/anomaly) | chirality conditional; radiative finite-diagnostic only; 3 bottlenecks |
| ordered_tape_closure | `ordered_tape_closure_v0_2.py` | `InfoOrderedTapeClosure.v` | color **3**, SU(3), Z₃, dim 8 from closed-tape oddness `(−1)^{k−1}=1⇒k` odd `⇒k=3` | `CONDITIONAL_ALGEBRAIC_PASS` | oddness **derived**, not "3 colors" input |
| center_confinement | `center_confinement_v0_3.py` | `InfoCenterConfinement.v` | area law `⟨W⟩=q^{Area}⇒V(R)=σR`, `σ=−log q>0` | `EXACT_PASS`, **Z₃/2D** | not full SU(3) 3+1D; standard lattice criterion, not new |
| v0.5 retained_confinement_certificate | `retained_confinement_certificate_v0_5.py` | `InfoConfinementCertificate.v` | computable `𝔠_t=μ₄·ρ_t<1`; rigorous `0<κ<0.0020252`; candidate `κ≲0.053` | rigorous small-κ + `[SeriesEstimate]` | RG flow, sup over all reps, exact `μ₄`, continuum OPEN |
| v0.6 triality_spectral_flow | `triality_spectral_flow_v0_6.py` | `InfoTrialitySpectralFlow.v` | serial `ρ_t(b)=ρ_t^{b²}`; **block-scale existence** `∃b_*: 𝔠_t<1` | exact (serial) + conditional (4D) | full `K_b`, real-action `ε_t(b)`, calibration OPEN |
| v0.7 full_block_closure | `full_block_closure_v0_7.py` | `InfoBlockCorrelation.v` | first-shell bumps; minimal-surface amplitude `ρ_geom=u⁴(1+16u⁴)` | `FIRST_SHELL_DIAGNOSTIC` **[CORRECTED by v0.9]** | its `u<0.34915` was **not** a valid criterion (self-caught bug) |
| v0.9 retained_metric_intertwiner | `retained_metric_intertwiner_v0_9.py` | `InfoRetainedIntertwiner.v` | intertwiner `P=∫ρ(h)dh` projector `‖P‖≤1`; **corrected criterion** `μ₄·û<1`; `κ≲0.05358` | `CORRECTED_CERTIFICATE` (`Th_coqc`) | fixes the v0.7 power-4 bug; superseded by v1.0 for exact `u,v` |
| v1.0 all_order_character | `all_order_character_v1_0.py` | `InfoAllOrderCharacter.v` | `u(κ),v(κ)` **all orders** from exact SU(3) Weyl integrals; `0<κ<0.053583974745` | `ALL_ORDER_NUMERICAL` (not interval proof) | matches v0.9 series to ~4e-6 (not a fit) |
| v1.1 surface_automaton | `surface_automaton_v1_1.py` | `InfoSurfaceAutomaton.v` | `μ₄^admissible` = Perron growth of a Z₃ frontier automaton; `μ_short=3.8751297942` | `EXACT_CONSTRUCTION` + **lower bound only** | single-sheet; bracket `[3.875, 54.366]` |
| v1.2 surface_upper_automaton | `surface_upper_automaton_v1_2.py` | `InfoSurfaceUpperAutomaton.v` | upper automaton `B(z)=5z+10z²+30z³+25z⁴+11z⁵`; `μ^+≤7.084097`; `κ<0.321687` (~6×) | `CONDITIONAL_UPPER_BOUND` (first-discovery) | exact `μ₄` still open between the two automata |
| v1.3 finite_transfer_gap | `finite_transfer_gap_v1_3.py` | `InfoFiniteTransferGap.v` | finite-transfer mass-gap theorem: `q=‖𝕋P_⊥‖<1 ⇒ Δ=−(1/a)log q>0` + exp clustering | `EXACT_CONDITIONAL` | NOT Clay mass gap; uniform `L→∞`,`a→0` + OS axioms OPEN; controls: diffusion gap closes, degeneracy `Δ=0` |
| v1.4 universal_rp_slab | `universal_rp_slab_v1_4.py` | `InfoUniversalRPSlab.v` | universal reflection-positive slab (all sectors): gauge/scalar/Fock Gram-positive ⇒ `T_UF⪰0`; mass reader `m=−(1/a)log λ` | `FORMAL_INTERNAL_PASS` + reader unit-test | PDG unit-test reads masses **back** (NOT prediction); chiral `A_f`/Yukawa/continuum OPEN; ratios `a`-independent |
| v1.5 hypercharge_global_quotient | `hypercharge_global_quotient_v1_5.py` | `InfoHyperchargeGlobalQuotient.v` | anomaly cancellation forces SM hypercharges `Y=(1/6,−2/3,1/3,−1/2,1,1/2)`; cubic `A₁₁₁=(A_grav)³=(h−3q)³` ⇒ grav+cubic are ONE condition `h=3q`; center-lock `2t+3s+y≡0 (mod 6)` ⇒ `G_phys=[SU(3)×SU(2)×U(1)]/Z₆` | `FORMAL_INTERNAL_PASS` (`Th_coqc`, 7 thm) + known-result rebuilt | exact **conditional on the one-generation skeleton**; ν^c ⇒ Y–(B−L) degenerate (negative control); blind skeleton derivation OPEN |
| v1.6 blind_matter_search | `blind_matter_search_v1_6.py` | `InfoBlindMatterSearch.v` | **blind** enumeration over `{1,3,3̄}×{1,2}` ⇒ unique minimal chiral set `(3,2)+2(3̄,1)+(1,2)+(1,1)`, `N=5,D=15`; the 2 colored singlets + colorless doublet are **forced** (color/Witten/closure); labels attached AFTER | `BLIND_SEARCH_EXACT_IN_ALPHABET` (`Th_coqc`, 10 thm; unbounded `D≥15` via lia) | uniqueness over ALL reps OPEN; ν^c ⇒ Y–(B−L) degenerate (control) |
| v1.7 root_native_chirality | `root_native_chirality_v1_7.py` | `InfoRootChirality.v` | Γ_T from ordered triple: `Γ²=I`, `Γ†=Γ`, `RΓR=−Γ`; **no-go**: unbroken reversal ⇒ two orientations carry equal weak reps ⇒ need order `Ξ`; weak-active `P_w=(I−ΞΓ)/2` | `ORIENTATION_EXACT`+`WEAK_ASYMMETRY_CONDITIONAL` (`Th_coqc`, 12 thm) | weak chirality needs ⟨Ξ⟩≠0 (OPEN); no γ⁵ imported; K_Ξ⪰0 via minors |
| v1.8 tape_kinetic_operator | `tape_kinetic_operator_v1_8.py` | `InfoTapeKineticGW.v` | root-native `D_T` with **exact Ginsparg–Wilson** `Γ(I−V)+(I−V)Γ=(I−V)Γ(I−V)`; free **no-doubling** (0<m₀<2r ⇒ one zero); 16→1+15 at d=4 | `KINETIC_GW_EXACT`+`NO_DOUBLING_FREE` (`Th_coqc`, 11 thm) | Clifford `{A_μ,A_ν}=2δ` forced by isotropy; continuum/Lorentz Dr/+reals; masses OPEN |
| v1.9 relation_channel_dimension | `relation_channel_dimension_v1_9.py` | `InfoDimensionFourClosure.v` | **derive d=4** from minimal carrier (orientation⊗incidence, dim 4): `d≤4` (≤3 ⟂ in ℝ³), `d` even (parity), `d≠2` (spectator), explicit `A₀=τ₁⊗I,Aᵢ=τ₂⊗σᵢ`, `Γ=−A₀A₁A₂A₃` | `DIMENSION_FOUR_EXACT_IN_ARCHITECTURE` (`Th_coqc`, 8 thm) | **closes v1.8's why-d=4**; 3+1 reflection-conditional; isotropic fixed point OPEN |
| v1.10 isotropic_fixed_point | `isotropic_fixed_point_v1_10.py` | `InfoIsotropicFixedPoint.v` | coarse-graining **attracts** to isotropy: twirl `Π₄(X)=(Tr X/4)I`; contraction `Δ_{n+1}=(1−α)Δ_n`; five-move mixer `ρ_frame=0.858010754588<1` (largest root of a sextic, rational bracket in Coq); doubly-stochastic sectors ⇒ one `c_*` | `ISOTROPIC_FIXED_POINT_EXACT_FOR_DECLARED_MAP` (`Th_coqc`, 11 thm) | **closes v1.9's isotropic fixed point**; `c_*` not predicted; derive `p(R)` from `S_UF` OPEN |
| v1.11 frame_mixing_from_action | `frame_mixing_from_action_v1_11.py` | `InfoFrameMixingAction.v` | **derive** the mixing weights `p(h)` from a slab of `S_UF`: `b_m=e^{−ε(m)/2}`, Gram `K_fr=B†B` (reflection-positive), `p(h)=Σ_{m⁻¹n=h}b_mb_n/(Σb)²` (≥0, Σ=1, `p(h)=p(h⁻¹)`); Fix=`ℝI₄`; equal-cost `ρ_aniso=0.7361824549886<v1.10's 0.8580` (root of a `25⁶`-sextic) | `FRAME_WEIGHTS_DERIVED_FROM_SLAB` (`Th_coqc`, 10 thm) | **closes v1.10's derive-p(R)-from-S_UF**; uniform gap/cost ratios/boosts OPEN |

## How to run

```bash
python3 run_tests.py     # runs all 22 verifiers + 22 Coq witnesses; prints a JSON decision
```
Each version's status is honestly fenced against [`CLAIM_BOUNDARY.json`](CLAIM_BOUNDARY.json) and
[`STANDARD_MODEL_CLOSURE.md`](STANDARD_MODEL_CLOSURE.md) — read those (and the master synthesis), not
this index, before citing a number.

## Current state (2026-07 snapshot)
**Closed / conditionally closed:** color **3** · **SU(3)** · **Z₃** center (conditionally derived);
**hypercharges** `Y=(1/6,−2/3,1/3,−1/2,1,1/2)` from anomaly cancellation with the **grav≡cubic** factorization `A₁₁₁=(A_grav)³` and the **Z₆** center-lock ⇒ `[SU(3)×SU(2)×U(1)]/Z₆` (`Th_coqc`, conditional on the one-generation skeleton);
**all-order** `u(κ),v(κ)` (exact Weyl integrals, numerical); the link **intertwiner** is a contraction
`‖P‖≤1` (`Th_coqc`) — the representation tail is closed.
**Numeric brackets:** surface entropy **`3.875 ≤ μ₄^admissible ≤ 7.084`**; confinement window **`κ<0.321687`**.
**Matter + chirality + spacetime arc (v1.6–v1.9):** the one-generation skeleton is **found blind** (v1.6, unique up to conjugation, `D=15`); chirality **grows** from the ordered triple with an exact no-go (v1.7, needs order `Ξ`); a root-native kinetic `D_T` has **exact Ginsparg–Wilson** chirality and **no doubling** (v1.8); and **`d=4`** is **derived** from the minimal carrier (v1.9); and coarse-graining **attracts** to isotropy with an exact contraction rate (v1.10), driving all sectors to one limiting speed `c_*`; and the frame-mixing weights themselves are **derived from a reflection-positive slab of `S_UF`** (v1.11), with the stronger rate `ρ_aniso=0.7361824549886<1` — the Euclidean 4-channel isotropy behind a 3+1 Lorentz shadow, now sourced by the action rather than posited. All `Th_coqc`. **Still fenced:** ⟨Ξ⟩≠0 from an action, continuum/Lorentz isotropic fixed point, Yukawa/masses/generations — none claimed.
**Still open:** physical Standard Model from root = **0%, OPEN** — chirality/spin-statistics, the
gauge-orbit Hessian, continuum/radiative validation, and the exact `μ₄` between the lower (v1.1) and
upper (v1.2) automata.

---
See also: [`SM_INFORMATION_PHILOSOPHY_MASTER.md`](SM_INFORMATION_PHILOSOPHY_MASTER.md) (canonical synthesis) ·
[`STANDARD_MODEL_CLOSURE.md`](STANDARD_MODEL_CLOSURE.md) (ledger of record) ·
[`CLAIM_BOUNDARY.json`](CLAIM_BOUNDARY.json) (machine tier fence) · [`README.md`](README.md) (folder overview).
