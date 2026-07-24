<!-- Root-native Standard Model DAG. A FRONTIER MAP, not a closure. Founder design v0.1
     merged with the 2026-07-21 survey of existing verified assets. Most of it is RED. -->

# Standard Model — Root-Native DAG (v0.1, roadmap · merged with existing verified assets)

> **Status: MAP, not result.** The Standard Model must be a **domain — a translation of the retained
> structure — not a new root**, and it carries **two separate chains** (derivation vs empirical
> discovery) per the Domain Registration Standard. We must NOT start by importing `SU(3)×SU(2)×U(1)`,
> quarks, leptons, the Higgs, or the gauge equations as premises — that would put the Standard Model
> in the premise. End-to-end root-derived Standard Model = **0%**.

Tiers: 🟩 forced-from-root / formal support · 🟨 conditional / partial premise borrowed · 🟦 discovery
or calibration from data · 🟥 open.

## The founder rule — where gauge structure comes from

Gauge is **not** "a kind of force" first. It is, first, **the non-uniqueness of the internal
description under the same checkable readout**:

```
  first question (NOT "which gauge group?") :
      which change of internal description leaves the checkable readout unchanged?
  Aut(F,O) = { h : O∘h = O ,  h∘F = F∘h }        ← the internal symmetry, grown from the
                                                    exact-quotient discipline, not posited
```

This is the same commuting-square the domains already require (`q∘F = F♯∘q`, `O = O♯∘q`); an
automorphism is a relabelling inside the equivalence class that does not change what the quotient may
read. **The weld (V.20) is exactly this**: an admissible symmetry is one that commutes with `F`.

## The DAG (with current tiers)

```
R0  δ_R retained distinction                                             🟩
 ▼
R1  typed retained state (G, Λ, T) + tape                               🟩
 ▼
R2  ordered transition paths / concatenation (identity + associativity) 🟨  candidate-from-root
 ▼
R3  readout-preserving automorphism group  Aut(F,O)      ◄ FIRST GATE   🟥  (SM-G0 below)
 ▼
R4  localized automorphism at each node  h_i                            🟥
 ▼
R5  edge transport / connection  U_{j←i}=V_j⁻¹V_i                        🟩  Th_coqc: InfoConnectionFromFrame
 ▼
R6  loop transport / holonomy  H_C = U_C                                🟩  Th_coqc: InfoRationalSO3Curvature (SO(3), R^TR=I)
 ▼
R7  order defect / curvature  K_C = H_C − I                             🟩  Th_coqc: curvature_nonzero
 ├───────────────────────┬────────────────────────┐
 ▼                       ▼                         ▼
G0 gauge-algebra         Q0 quantum completion     scale refinement
   discovery                (norm/channel/           (kinematic weights)
 │                          measurement/spin)       │
 ▼                       │                          ▼
center 𝔷 ⊕ simple 𝔤_i    │                     three weights 11/3, 2/3, 1/3   🟥 not derived
 │  🟨 group seed:        ▼                          ▼
 │  Heisenberg Hb        spin / statistics /    representation counting        🟨 (SM content = input)
 │  (InfoSeedTorsion-    occupation  🟥              ▼
 │   GroupAndRankN,      │                     coupling-flow coefficients      🟦 benchmark match (AP10)
 │   Th_coqc)            │
 ▼                       │
representations =        │
response classes  🟥 ◄───┘
 ▼
chirality (orientation V=V_+⊕V_-)  🟥   ──►  anomaly = classical-commutes / quantum-record-does-not  🟥
 ▼
minimal consistent representation set  🟥
 ▼
order-parameter potential  V(Φ)   🟨   (∇V substrate exists; coercivity forced — force_potential.py)
 ▼
selected state  v ∈ argmin V ;  stabilizer  H = {g : gv=v}  →  G→H  🟥
 ▼
gauge-direction obstruction  (M_G²)_{ab} = ⟨T_a v, T_b v⟩_G  🟥   (massless = ker; obstructed = mass)
 ▼
invariant matter couplings  Y ∈ Hom_G(V_L⊗S, V_R)  →  M_f = Y(·,v)  🟨-form / 🟦-value
 ▼
generations (repeated classes) + mixing  U_mix = V_int⁻¹ V_mass  🟥  (count NOT derived)
 ▼
scale flow / coupling running  🟦  · empirical encoding + group identification  🟦
 ▼
SU(3)×SU(2)×U(1) semantic label — ONLY IF DISCOVERED  🟥
 ▼
bounded Standard Model claim
```

> **This DAG tracks the UNRESTRICTED root chain only.** The 🟥 nodes above (representations,
> chirality, minimal rep set, selected state, gauge obstruction) are genuinely open **from an
> unrestricted root** — no Coq witness derives them without a declared finite architecture. But a
> separate v1.5–v1.13 arc (`domains/standard_model/*_v1_[5-9,1*].py` + matching `Info*.v`) DOES
> close the *architecture-level* analogue of several of these nodes, exact within a stated minimal
> alphabet / carrier. **Never collapse the two axes into one 🟥/🟩** — read them side by side:

| DAG node (unrestricted root) | Root/formal status | Finite-architecture status (v1.5–v1.13) |
|---|---|---|
| representations = response classes | 🟥 open | `EXACT_WITHIN_DECLARED_ARCHITECTURE` — blind search over `{1,3,3̄}×{1,2}` finds `(3,2)+2(3̄,1)+(1,2)+(1,1)` uniquely (v1.6, `InfoBlindMatterSearch.v`) |
| chirality (orientation `V=V_+⊕V_-`) | 🟥 open | `EXACT` grading `Γ_𝒯` + exact no-go (v1.7, `InfoRootChirality.v`); weak *selection* stays `CONDITIONAL` on `⟨Ξ⟩≠0` |
| minimal consistent representation set | 🟥 open | same as representations row — minimal within the declared alphabet only, not over all reps |
| order-parameter potential `V(Φ)` / selected state `v∈argmin V` | 🟥 open (substrate exists, coercivity forced) | `H=(1,2)_{1/2}` forced by matter closure (v1.12); `⟨H†H⟩>0` from closure-pressure/intertwiner-rank counting, `CONDITIONAL` on `Π₀>α` being forced (v1.13, `InfoOrderHiggsClosure.v` + `InfoIntertwinerOrderVacuum.v`) |
| gauge-direction obstruction `(M_G²)_{ab}` | 🟥 open | `EXACT` rank pattern given nonzero order: `det=0` photon, `m_W=m_Z cosθ`, `ρ=1` (v1.12) |
| hypercharge normalization (not shown above, folds into "representations") | 🟥 open (unrestricted) | `EXACT_WITHIN_DECLARED_ARCHITECTURE` — `Y=(1/6,−2/3,1/3,−1/2,1,1/2)` + Z₆ quotient forced by anomaly cancellation on the skeleton (v1.5) |
| `d=4` / spacetime shadow (not on this DAG; see `UNIFIED_FORCE_DAG.md`) | 🟥 open (unrestricted, why 3+1 at all) | `EXACT_WITHIN_DECLARED_ARCHITECTURE` — derived from the minimal orientation⊗incidence carrier (v1.9); Lorentz shadow conditional on a declared coarse-reader map with weights derived from the action (v1.10–v1.11) |

The finite-architecture column is real progress and is machine-checked (`run_tests.py`), but it is
**not** a substitute for closing R3/SM-G0 on the unrestricted root — the architecture itself (the
declared alphabet, the carrier, the coarse-reader map) is still an *input*, not yet derived from R0–R7.

## What we ALREADY have (2026-07-21 survey — verified, axiom-clean, root-native)

| asset | file (Th_coqc unless noted) | role in the SM DAG |
|---|---|---|
| **discrete connection** `U=V_j⁻¹V_i` | `InfoConnectionFromFrame` | R5 gauge-field seed (forced) |
| **SO(3) rotation group** (R^TR=I, holonomy, curvature≠0) | `InfoRationalSO3Curvature` | R6/R7; SO(3)↔SU(2) = spin/weak-isospin seed |
| **non-abelian group from the seed** = **Heisenberg `Hb`**, group-torsion-free = group-inverse | `InfoSeedTorsionGroupAndRankN` | the gauge **algebra** seed — non-abelian, canonical-commutation flavour |
| **a proven gauge invariance** (dispersion invariant under scale `s`) | `InfoScaleGaugeNonReadout` | R3 template: a genuine readout-preserving redundancy already exists |
| **Noether** (symmetry → conserved current) | `InfoGraphNoether`, `InfoCurvatureNoether` | the conserved-current backbone gauge theory needs |
| **self-interaction relative weight** `c_self/c_geo = 1`, total `= 2` | AP20 | gauge self-coupling ratio — 🟨 (commutator + self-carrier still **borrowed** premises) |
| **one-loop β slopes** `b_a = 11/3·C₂(G_a) − 2/3·ΣT_a(R) − 1/3·ΣT_a(S)` | AP10 | 🟦 benchmark match; representation content is **SM input**, the three kinematic weights NOT derived |
| **mass = internal-mode energy** `m = ħω_int/2c²`; mass-loading does double duty (mass + gravity sign) | `mass_note.tex` | Higgs/mass substrate — 🟨/[Dr] |

So R5–R7 (connection, holonomy, curvature) are **stronger than a first pass suggests — they are `Th_coqc`**, and a genuine **non-abelian group (Heisenberg) + a proven gauge invariance + Noether** already exist. The gauge *substrate* is real. What is **not** yet done is R3/SM-G0 (deriving gauge redundancy from readout-equivalence itself) and everything from representations onward.

## WHERE TO START — SM-G0: the Gauge Emergence Kernel (NOT Higgs, not particles, not β)

Prove six things, closing the borrowed premises that currently prop up AP20:

- **G0.1 Path composition** — ordered path carrier with identity + associativity `(P₃∘P₂)∘P₁ = P₃∘(P₂∘P₁)`. **🟩 Th_coqc (done, 2026-07-23):** [`InfoGaugeAutomorphismGroup.v`](InfoGaugeAutomorphismGroup.v) (Closed) — proved fully abstractly for *any* carrier `(M, one, op)` that is a monoid: `pathcomp` (fold `op` over a list of steps) satisfies `pathcomp(xs++ys) = op(pathcomp xs)(pathcomp ys)`, single-step and app-associativity corollaries. No domain alphabet, no Section/Hypothesis.
- **G0.2 Automorphism group** — `Aut(F,O)` closed under composition + inverse. **🟩 Th_coqc (done, 2026-07-23):** same file — `Aut(F,O) := {h : O∘h=O, h∘F=F∘h}` proved to contain the identity, be closed under composition, and be closed under inverse (whenever a two-sided inverse exists), for **arbitrary** state type `S`, readout type `R`, dynamics `F : S→S`, readout `O : S→R`. This satisfies every group axiom Aut(F,O) needs — it does *not* yet show Aut(F,O) is nontrivial for the actual root dynamics, which is a separate question.
- **G0.3 Localization** — each node may change internal representative while observable transport still factors through the quotient. **🟩 Th_coqc (done, 2026-07-24):** [`InfoGaugeLocalizationConnectionHolonomy.v`](InfoGaugeLocalizationConnectionHolonomy.v) (Closed) — proved for *any* group `(G, id, mul, inv)`: a frame field `f : nat → G` assigns an arbitrary per-node representative; the frame-difference connection's ordered product (`pathprod`) telescopes to depend only on the endpoint frames `f(n)`, `f(0)`, for any intermediate choice; a closed loop (`f n = f 0`) is provably pure gauge (trivial holonomy). Generalizes `InfoConnectionFromFrame`'s single-group (Heisenberg) result to any group.
- **G0.4 Connection transformation** — DERIVE `U_{ji} ↦ h_j U_{ji} h_i⁻¹` from transport-commutation (not posit it). *(the connection itself is already `Th_coqc`.)* **🟩 Th_coqc (done, 2026-07-24):** same file — proved both **existence** (defining `U' := h_j·U·h_i⁻¹` makes transport commute with local relabeling) and **uniqueness** (any transport satisfying the same commutation requirement for every state *must equal* `h_j·U·h_i⁻¹`) — for any group. The law is forced by requiring the diagram to commute, not chosen freely.
- **G0.5 Holonomy invariant** — loop readout independent of internal representative (conjugacy-invariants of `H_C`). *(CORRECTED 2026-07-23: `InfoRationalSO3Curvature` is a single hand-picked rational witness pair, not a general theorem — its own header says so.)* **🟩 Th_coqc (done, 2026-07-24, supersedes the single-witness result):** same file — proved for any group that holonomy triviality (flat vs curved) is a **conjugation-invariant**, representative-independent fact (`conj_trivial_iff`), and that composing two representative changes acts correctly as a genuine group action (`conj_composes`), consistent with G0.2's automorphism-group closure.
- **G0.6 Order-defect / self-carrier gate** — build the commutator FROM the ordered product (ordered composition → exchange defect → commutator algebra, with Jacobi following algebraically), then wire it to AP20 so `c_self/c_geo=1` is lifted from **borrowed commutator** to **root-derived order defect**. **🟩 Th_coqc (done, for the commutator):** [`InfoOrderDefectFromComposition.v`](InfoOrderDefectFromComposition.v) (Closed over ℚ) — plain 2×2 rational matrix composition (no non-commuting term written in), associativity a theorem, `K(X,Y)=XY−YX` bilinear+antisymmetric, **Jacobi derived from associativity**, non-commutativity emergent, commuting ⇒ zero defect. This **reduces AP20 borrow #2** (grounds the commutator *form* — Jacobi/antisymmetry become theorems) **but does not remove it**: the self-force still needs a *non-commuting* pair, here hand-exhibited (not root-forced), so the non-abelian *input* is relocated, not eliminated. Self-carrier closure (#3) and the common load A4 (#4) are **still fully borrowed/OPEN**; `c_self/c_geo=1` is **not** root-derived.

### First failing controls (the gate must be able to fail)
- **F1** a transformation with `O(hz) ≠ O(z)` → rejected, NOT a gauge transformation.
- **F2** a commutative path carrier `XY=YX` → `[X,Y]=0` → no non-abelian curvature, no self-interaction branch (must be excludable).
- **F3** an external payload not in the same carrier algebra → no quadratic self-term (AP20's own failing control, but currently AP20 borrows the non-commutative algebra as a premise — G0.6 removes that).

## Honest status (unrestricted root — see the two-axis table above for finite-architecture status)

| part | tier |
|---|---|
| retained root / operator / geometry | 🟩/🟨 strong |
| connection · holonomy · curvature (R5–R7) | 🟩 **Th_coqc** |
| non-abelian group seed (Heisenberg) · SO(3) · Noether · a proven gauge invariance | 🟩/🟨 present |
| **gauge = readout-preserving automorphism (R3 / SM-G0)** | 🟩 **all 6 structural sub-gates closed: G0.1/G0.2 (2026-07-23), G0.3/G0.4/G0.5 (2026-07-24), G0.6 (earlier) — all `Th_coqc`; does NOT show the structure is nontrivial for the real root dynamics, nor derive anything downstream** |
| localized-connection-from-root | 🟥 |
| order-defect-from-root (G0.6, the commutator) | 🟩 Th_coqc — `InfoOrderDefectFromComposition.v` (AP20 borrow #2 *form* grounded — Jacobi/antisym now theorems — but non-abelian input still un-forced; self-carrier #3 + load A4 #4 still borrowed) |
| gauge self-interaction relative weight (AP20) | 🟨 conditional (premises borrowed) |
| representation counting (unrestricted) | 🟥 (only closed as SM input here; **but see v1.6: exact within a declared minimal alphabet, not unrestricted**) |
| gauge-group discovery · matter reps · chirality/anomaly (unrestricted root) | 🟥 (**architecture-level**: hypercharge+Z₆ v1.5, blind skeleton v1.6, chirality grading+no-go v1.7 all `Th_coqc` — see two-axis table) |
| generations/mixing | 🟥 |
| SU(3) (unrestricted) | 🟥 (conditionally derived within the ordered-tape architecture — §2 of `STANDARD_MODEL_CLOSURE.md`) |
| constants (couplings/masses) | 🟥 |
| Higgs-like mechanism | 🟨 substrate (unrestricted root); **architecture-level: forced minimal order carrier + vector mass-rank pattern, v1.12; order-vacuum criterion corrected, v1.13** |
| full quantum measurement / spin-statistics (prerequisite) | 🟥 |
| **Standard Model end-to-end, root-derived (unrestricted)** | **0%** |

**Direction (honest):** not "write the Standard Model," but **prove that gauge redundancy, the
connection, and curvature grow from retained readout-equivalence** (SM-G0). When SM-G0 closes, the
borrowed premises under AP20 come off, and only then do gauge group, matter representations,
Higgs-like breaking, and the rest of the DAG have a real root to stand on. The Quantum domain (§V.18)
is a hard prerequisite: without spin-statistics we may not call a response class a fermion/boson, and
without Born/measurement closure we may not claim cross-sections or decay rates from the root.
