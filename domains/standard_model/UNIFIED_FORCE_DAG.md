<!-- Unified-force design: ONE retained dynamics -> many interaction readouts. Founder design
     merged with the 2026-07-21 survey. NOT F_total = F_grav+F_strong+F_weak+F_EM. Mostly open. -->

# Unified Force — one action, four projections (roadmap · merged with verified assets)

> **The wrong form** is `F_total = F_gravity + F_strong + F_weak + F_EM` — that adds four
> already-separated forces afterward, and forces gravity (a *geometry* readout) to be the same kind
> of object as the gauge forces. **The right form for this architecture:**
> `one retained dynamics ⟶ many interaction readouts` — the four forces are different **projections**
> of one action/obstruction. The force names live at the **END** of the DAG, never the start.

## The unified action (candidate) and its stationary equation

```
   S_UF = S_DRL + S_Θ + S_U + S_Σ + S_cut/tape
   δS_UF / δZ_n = 𝒥_{C,n}[Z_n]        Z_n = (X_n, Θ_n, U_n, Σ_n, 𝒯_n)
```
block form (typed, from ONE action — not four scalar theories added):
```
   [ 𝓔_X  𝓔_Θ  𝓔_U  𝓔_Σ  𝓔_𝒯 ]ᵀ_n = [ 𝒥_X  𝒥_Θ  𝒥_U  𝒥_Σ  𝒥_𝒯 ]ᵀ_n
```
force = a projection of the same right-hand side:
```
   𝓕_D = P_D ( −∇_Z 𝒰_UF + 𝒥_C )
   P_geo → gravity   P_center → EM   P_chiral,broken → weak   P_simple,unbroken → strong
```

## Sector-by-sector, with CURRENT tiers (survey 2026-07-21)

| sector | what it is | tier now | asset |
|---|---|---|---|
| `S_DRL` reader–record | the forced two-field `(Φ,Ψ)` variational system | 🟩 | core II.8a; `InfoCompanionSkew` (Th_coqc) |
| **action stationarity** `δS/δZ` | the very backbone of "one action → equations" | 🟩 **Th_coqc** | `InfoActionStationarity` (CI-verified, axiom-clean) |
| `S_Θ` geometry → **gravity** | `M_Θ Δ²Θ + ∇𝒰_Θ`, curvature defect, backreaction | 🟩 metric/curvature; 🟨 full law | `RDL_MetricReadout`, `InfoDiscreteRiemannCurvature`, **`InfoBackReaction`** (Th_coqc) |
| `S_U` internal transport | edge transport `U`, holonomy `H_C`, curvature `K_U=H_C−I` | 🟩 **Th_coqc** | `InfoConnectionFromFrame`, `InfoRationalSO3Curvature`, group seed `InfoSeedTorsionGroupAndRankN` |
| `C_int` matter↔transport↔geometry feedback | the cross-coupling term | 🟩 **Th_coqc** | `InfoCrossTermDominance` |
| `∇V` / cubic | the potential / nonlinear restoring | 🟩 **Th_coqc** | `InfoCubicLinearization`; coercivity `InfoCoercivityBoundedClosure` |
| `S_Σ` selected state | `Σ_* ∈ argmin V_Σ`, obstruction `(M²_obs)_{ab}=⟨T_aΣ_*,T_bΣ_*⟩` | 🟨 attempt | `InfoSeedArgminActionCost_attempt` (grep-clean, not CI-confirmed here) |
| `S_cut/tape` | the cut current / lineage record | 🟩 growth; 🟥 from-one-action | `InfoCutGrowth` (Th_coqc), `InfoMaxFlowMinCut_attempt`; a *unified* DRL–cut–tape action is Open |
| **unified master readout** | seed → velocity + coupling + damping in one readout | 🟨 attempt | `InfoSeedUnifiedMasterEquation_attempt`, `InfoSpineUnification_attempt` (grep-clean) |

So most **sectors** of the unified action already have formal support (Th_coqc for the causal-QG
sector pieces; grep-clean attempts for the unified-readout and selected-state). **What is genuinely
Open** is: (a) the SINGLE assembled `S_UF` as one stationary action (the pieces exist, the one-action
weld does not), (b) `UF-0` gauge-automorphism-from-root, (c) the four-force **projection decoder**, and
(d) everything downstream.

## Where the four forces grow from (END of the DAG, not the start)
- **gravity** = `P_geo 𝓕_all`: retained operator → principal symbol → metric → transport → curvature →
  backreaction. Gravity is the **geometry response**, NOT another gauge sector. (metric/curvature 🟩;
  full nonlinear GR / Einstein equations 🟥.)
- **EM** = the **center** sector `𝔷` (`[𝔷,𝔤]=0`), an unbroken abelian direction with a long-range loop
  phase — *label* only after charge calibration. 🟥 (needs UF-0 + calibration).
- **weak** = a **chiral** simple sector with **selected-state obstruction** (short range) — no chirality
  or no `Σ`-obstruction ⇒ not weak. 🟥 from the unrestricted root. **Architecture-level update
  (v1.7–v1.13, `Th_coqc` within a declared minimal architecture, see `STANDARD_MODEL_CLOSURE.md`
  §4/§6):** the chirality grading `Γ_𝒯` IS exact and comes with an exact no-go (grading alone gives
  no weak asymmetry — needs an orientation order `Ξ`, `CONDITIONAL` on `⟨Ξ⟩≠0`, v1.7); the order
  carrier `H=(1,2)_{1/2}` bridging weak-active/inactive sectors is **forced** by the matter skeleton
  and gives one massless + three massive vector directions when nonzero, `m_W=m_Z cosθ`, `ρ=1`
  (v1.12); *why* the order condenses reduces to one primitive-cost inequality `Π₀>α`, not yet forced
  (v1.13). None of this closes the unrestricted-root 🟥 above — it closes the analogous question
  within the declared architecture.
- **strong** = an **unbroken non-abelian** sector with **self-carrier closure** → composite-only
  readout. AP20 gives, conditionally, `c_self/c_geo = 1` — but its commutator + self-carrier are still
  **borrowed premises**. 🟨.

## The gates that stop the DAG from cheating
`UF-G1` common-root (every sector traces to `R0→L_R/D→S_UF`) · `UF-G2` geometry/internal are two
readouts of one state, not one variable · `UF-G3` automorphism `O(hz)=O(z), hF=Fh` · `UF-G4` derive
`U_{ji}↦h_j U_{ji} h_i⁻¹` · `UF-G5` discover center/simple sectors from the real algebra (do NOT force
the count to 3) · `UF-G6` massless/obstructed from `Σ_*` · `UF-G7` close quantum norm/composition/
measurement/spin-statistics before naming matter · `UF-G8` both `geometry→matter` and `matter→geometry`
(**`InfoBackReaction` closes one joint, Th_coqc**) · `UF-G9` the names gravity/EM/weak/strong need
held-out empirical encoding · `UF-G10` macroscopic forces must commute with micro-dynamics under a
declared coarse-graining.

## Emergent / macroscopic forces are NOT new roots
`strong → composite → residual nuclear`; `EM+quantum → atomic/molecular/chemical/elasticity/normal/
friction/surface-tension`; `weak → decay/channel-conversion`; `gravity → weight/orbit/tidal/large-scale`;
`all + coarse-grain → pressure/viscosity/buoyancy/thermodynamic/biomechanical`. Friction is not a fifth
fundamental force; the residual nuclear force is not a fifth — each is a quotient of composite dynamics.

## WHERE TO START — `UF-0` = build readout-preserving automorphism + local transport from the root
This is the SAME kernel as **SM-G0** ([`ROOT_TO_SM_DAG.md`](ROOT_TO_SM_DAG.md)) — closing it yields, from
one mechanism: internal gauge structure, connection, holonomy, curvature, self-interaction, and the
abelian/non-abelian fork — and it plugs straight into the geometry branch to give the real unified
force equation **without adding four ready-made theories together**. The connection, curvature,
action-stationarity, cross-term, cubic, coercivity and backreaction pieces are already `Th_coqc`; what
`UF-0` still owes is deriving the *automorphism = gauge* step and assembling the *single* `S_UF`.

**Honest status:** the unified-action *sectors* are mostly forced/attempted; the *single assembled
action*, the *gauge-from-root* step, the *four projections*, and all downstream physics (chirality,
anomaly, spin-statistics, generations, constants, full nonlinear GR) are **Open**. End-to-end
root-derived *physical* unified force = **0%** as a closed claim.

## Unified Force Closure v0.1 — INTERNALLY CLOSED (finite), physical OPEN
[`unified_force_closure_v0_1.py`](unified_force_closure_v0_1.py) (PASS) witnesses the architecture at the
finite/typed level: **ONE action, ONE block master equation, and the four forces as orthogonal
projection readouts** `F_all = F_G + F_EM + F_W + F_S + F_res`, with a **falsifiable completeness score
χ4** (`χ4 = 1` on a strong⊕weak `so(3)` fixture with `Σ*=e_3`; `χ4 < 1` the moment a hidden fifth
interaction leaks outside the four sectors). Witnessed exactly (`Fraction`, each with a failing control):
the automorphism group `A = {h : O h = O, hF = Fh, hᵀGh = G}`; the connection law `U' = h_j U h_i⁻¹`
*derived* from transport-commutation; holonomy `tr/det` class-invariants; the order defect `[X,Y]` with
Jacobi from associativity; covariant retained-Laplacian covariance `L_{U',Θ}Φ' = h(L_{U,Θ}Φ)`; and the
selected-state `h/m` split (unbroken `W_z Σ* = 0` vs broken `W_x,W_y Σ* ≠ 0`).

This is **not** physical four-force unification. Still **Open** and *must not be faked*: the
gauge-from-root step (`UF-0`/`SM-G0`), whether the emergent algebra is really `SU(3)×SU(2)×U(1)`,
chirality/anomaly/spin-statistics, three generations, every coupling constant (`α` rejected-not-faked),
confinement, full nonlinear GR, and experimental matching. The four are **not added together** — they
are made *orthogonal readouts of one generalized force* with a residual `F_res` that can refute the
"exactly four" claim. Root-derived **physical** unification = **0%** as a closed claim; the finite
architecture is **INTERNALLY CLOSED**.

## SM-G0 / G0.6 — order-defect from ordered composition (Th_coqc: AP20 borrow #2 discharged)
[`InfoOrderDefectFromComposition.v`](InfoOrderDefectFromComposition.v) (`Print Assumptions` **Closed over
ℚ**) closes the one piece the whole corpus left borrowed. AP20 gets `c_self/c_geo=1` on three borrowed
premises; its premise #2 states verbatim that *"the noncommutative/Lie-algebraic input remains borrowed;
AP20 does not derive it from RD4"*, and `InfoDiscreteRiemannCommutator` only **posits** a Heisenberg
product with the non-commuting term written in by hand. Here the ordered composition is **plain 2×2
rational matrix product** — the concrete form of "compose transport X then transport Y" for linear
readout-transports, with **no non-commuting term written in**. Then: composition is **associative** (a
theorem), the order defect `K(X,Y)=XY−YX` is bilinear + antisymmetric, **Jacobi is DERIVED from
associativity** (the gap that previously existed only as a numeric check in AP20), non-commutativity is
**emergent** (a witness pair fails to commute — not put in by hand), and **commuting transports ⇒ zero
defect** (AP20's own failing control, now derived). This **REDUCES AP20 borrow #2 in status** — its
*form* is now theorem-level (Jacobi/antisymmetry **derived**, not an imported Lie-algebra axiom) — **but
does not remove it**: the self-force needs a *non-commuting* pair, here **hand-exhibited (X0,Y0), not
root-forced** (`diagonal_commute_zero_defect` proves K=0 for every commuting pair), so the non-abelian
*input* is relocated to "the root emits a non-commuting pair", not eliminated — consistent with AP20's own
note that it *"does not remove the Lie-algebra/commutator borrow."* **Still fully OPEN:** self-carrier
closure (#3), the common quadratic load A4 (#4), whether the transports are *forced* by the root, and
everything downstream. `SM-G0/G0.6 (commutator FORM): 🟩 Th_coqc` (was 🟥); the non-abelian input: still 🟥.

## Four-Force Circulation v0.2 (fixture scheme) — [SimulatedData / FiniteFormalWitness]
[`four_force_circulation_v0_2.py`](four_force_circulation_v0_2.py) (PASS) and
[`InfoFourForceCirculationRecovery.v`](InfoFourForceCirculationRecovery.v) (**Closed over ℚ**) go past
"one force → another": they compute the **full four-sector response and split it**. On a four-sector
ring fixture `A = H + Ω` (`H` symmetric reciprocal load, `Ω` antisymmetric circulation load), with
`χ = A⁻¹`:
- **stability gate** (not instability-driven): `spec(H)={6,4,4,2}>0`, `spec(A)={6,2,4±i}`, `Re λ(A)>0`;
- **exact directed-response identity** `χ − χᵀ = −2 χᵀ Ω χ` (proven, not approximated) — this is the
  non-trivial content: the *measurable nonreciprocity* of the response equals the planted circulation
  conjugated by the full susceptibility;
- **circulation read-back** `Ω_recovered = Ω_planted` as the unique **antisymmetric part** of `χ⁻¹`
  (`Ω = ½(χ⁻¹−χ⁻ᵀ)`) — exact **by construction** (the unique symmetric/antisymmetric split), a scheme on
  a **known** fixture, *not* tomography of an unknown system;
- **failing controls:** reciprocal (`Ω=0 ⇒ χ=χᵀ ⇒ Ω_rec=0`, no directed cycle manufactured) and
  missing-edge (cut `S–G` ⇒ recovered `|Ω_SG|≈0` while real edges survive — no hallucinated structure);
- scalar readout `C_F = ½‖χ−χᵀ‖_F` (`C_F²=2/289` exact; `=0` when `Ω=0`).

**Honest fence.** `(G,EM,W,S)` are **decoder labels in a fixture**, NOT forces calibrated to nature.
Closed = a finite tomography *scheme* (response identity + exact recovery + controls). OPEN = that the
labels are the real forces, a physical separable per-force source, the true susceptibility, the quantum
measurement layer, unit calibration, the gauge group, and empirical novelty. Baseline lineage: `Ω=0`
recovers **Onsager reciprocity** (symmetric χ); `Ω≠0` is the nonreciprocal/non-equilibrium response.

## Unified Force v0.3 — CALIBRATED ELECTROWEAK DECODER (EM↔Weak), the first real-observable bridge
[`electroweak_decoder_v0_3.py`](electroweak_decoder_v0_3.py) (PASS) +
[`InfoElectroweakNullDirection.v`](InfoElectroweakNullDirection.v) (**Closed over ℚ**) take the EM and
weak sectors from *decoder labels* to a decoder **bound to real observables that can fail**. Two halves,
kept strictly apart:
- **Structural core (exact, ours).** The neutral selected-state obstruction
  `M²_neutral = (v²/4)·outer((g,−g'),(g,−g'))` is a **rank-1 outer product**, so `det M²=0` **identically
  (all g,g',v)** ⇒ **exactly one massless + one massive** neutral direction, and **the photon's
  masslessness EMERGES** — it is never imported as a premise. Massless (photon) `~ (g',g) =
  sinθ_W W³ + cosθ_W B`, eigenvalue `0`; massive (Z) `~ (g,−g')`, eigenvalue `m_Z²=(v²/4)(g²+g'²)`;
  charged `m_W²=g²v²/4`. **Failing control** `FAIL_NO_MASSLESS_ABELIAN_DIRECTION`: a generic rank-2
  obstruction has `det≠0` ⇒ no massless direction. Gates EW-P1..P5 (rank / null-vector / orthogonal
  massive / charge-universality / held-out mass) each carry a control.
- **Calibration (float, real constants — CONSISTENCY, not prediction).** With CODATA 2022 + PDG 2025:
  `v=246.21965 GeV`, `g'/g=tanθ_W=0.535802`, `g=0.652824`, `g'=0.349784`, `α₂=0.033914`, `α_Y=0.009736`.
  On-shell `sin²θ_W` is *defined* via the mass ratio, so this is a **calibration-consistency** check, not
  an independent prediction. The one honest **held-out** check (EW-P5): fit `{G_F→v, θ_W, M_W}` and
  predict `M_Z=M_W/cosθ_W = 91.178 GeV` vs PDG `91.188` (**0.011%** at tree level; the **radiative layer
  is OPEN** before any "precision prediction").

**Honest label:** `CALIBRATED ELECTROWEAK DECODER`, **not** "Standard Model derived from the root." The
gauge algebra `SU(2)×U(1)`, chirality, matter representations, the *value* of `θ_W`, three generations,
and radiative corrections are **OPEN and must not be imported as premises**. What is genuinely ours is
the **rank-1 ⇒ (massless photon + massive W/Z) structure** — a real, fail-able target.
