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
  or no `Σ`-obstruction ⇒ not weak. 🟥.
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
root-derived unified force = **0%** as a closed claim.
