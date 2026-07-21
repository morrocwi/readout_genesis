# Readout Genesis — Core Canon

> **Reality is retained before it is divided into domains.**
> The base is not matter, not a continuum, not physics/chemistry/biology/mind. The base is
> *information* — difference, history, and retained change. Everything named is a *readout* of it.
>
> **Native unit:** `1 RD` = one retained distinction. SI units (kg, eV, s, m) appear only through a
> declared decoder, never at the root.

## 0. Claim discipline — *readout-not-truth*

Verified structure is not physical truth. Machine-checkable structure and laboratory measurement are
two different things, and this document never conflates them. Every claim carries a tier:

| tier | meaning |
|---|---|
| `Th_coqc` | machine-checked, axiom-free over ℚ (`Print Assumptions` closed) |
| `finite_diagnostic` | measured or computed, finite and exact |
| `Dr` | a declared bridge / human narrative reading |
| `Open` | not established |

**There is no hidden ℝ behind the odometer.** A "quantity" is not a Platonic magnitude waiting to be
measured; it is a projection on the bounded, discrete, finite-resolution readout space a system can
return. Two projections with identical arithmetic and equal numeric value can still be *different
quantities* — a quantity's identity is its causal/inferential role in the finite readout graph, not
the number it shows.

---

## 1. The one root

The primitive is a **retained distinction**:

```
δ_R = (a ♯ b)
```

— a difference between `a` and `b` that leaves a trace. If a difference occurs and leaves no retained
effect, the system has no internal evidence to separate it from what never happened. So the primitive
is not "information an observer already knows" but *a difference whose effect the system still keeps*.

Retention axiom (histories that differ must remain separable in the residue):

```
Γ_n ≠ Γ_n'  ⟹  ℜ_n(Γ_n) ≠ ℜ_n(Γ_n')
```

An observer may *read* two histories the same while the residue still separates them:

```
O_α(Γ_n) = O_α(Γ_n')     yet     Q_α(Γ_n) ≠ Q_α(Γ_n')
```

giving the load-bearing principle used everywhere below:

> **reads-the-same ≠ is-the-same.**

The retained structure is realized on a **finite causal graph** `Γ`, whose Laplacian is the one
genuinely derived operator of the whole framework:

```
L_R := D_W − W            (D_W = weighted degree, W = weight matrix)
⟨x, L_R x⟩ = ½ Σ_ij W_ij (x_i − x_j)²  ≥ 0        [Th_coqc]  (PSD; kernel = connected components)
```

Everything downstream of `L_R` is `POSITED` or a `DEFINITIONAL-RELABEL`, not derived — this is stated
plainly and not smoothed over.

---

## 2. From the root to the trunk

The **foundational dynamical object is the discrete stepper** (schematically):

```
γ = 1/τ_c ;  V[n+1] = V[n] + Δθ(−γV[n] − D_s·L_R X[n]) ;  X[n+1] = X[n] + Δθ·V[n+1]
```

Its coarse-grain readout (the continuum `Δθ→0` limit) is the **universal spine PDE** — *the trunk, a
readout of the stepper, not the reverse*:

```
M ∂²_t Φ + D ∂_t Φ + K·L_R Φ + ∇V(Φ) = J − η          (legacy label: Eq.49)
```

Its memoryless (`M→0`), linear (`V→0`) limit is the **relaxation / turbulence-structure equation**:

```
τ_R dI_R/dt + L_R I_R = S_R + η_R                       (legacy label: Eq.60)
```

**Three layers stack here and must not be merged:** the second-order DRL–telegraph root, the
first-order relaxation limit, and an external Littlewood–Paley / Navier–Stokes *audit* (a checker, never
a generator of the native RD update).

---

## 3. The master equation, term by term — honest tiers

```
M ∂²_t Φ + D ∂_t Φ + K·L_R Φ + ∇V(Φ) = J − η
```

| term | reading | tier |
|---|---|---|
| `M` (inertia / memory) | `τ_c = M/D` is the memory time; **mass is a readout of τ_c**, `m = ħ/(2c²τ_c)` | **`POSITED`** — forcing `M` from the root failed 8× |
| `D ∂_t Φ` (damping) | the arrow of time (odd under time reversal) | `Dr` (narrow, from an action) |
| `K·L_R Φ` (restoration/geometry) | `L_R` is a **full operator**, not a scalar `λ` | `Th_coqc` for `L_R` itself only |
| `∇V(Φ)` (potential / nonlinear cascade) | fitness landscape; turbulence `∇V = g Φ³` | `POSITED` |
| `J` (source / flux) | open-system in/out-flow | `POSITED` (weakest slot) |
| `η` (noise / residual) | drift + mutation | `POSITED` — **must not be a catch-all error bucket** |

**Regime split** (per mode `k`, from `M s² + D s + K λ_k = 0`): `λ_c = D²/(4MK)`.
`D² < 4MKλ` → complex roots → oscillatory / quantum-like / turbulent-like; else overdamped / classical.

> **τ_c is DISCRETE and PRIOR TO MASS.** Mass is nowhere in the foundational stream; it enters only as an
> input example at the decoder. This is founder-locked. `τ_c` here is **not** the textbook quantum speed
> limit (QSL) — they share only the algebraic shadow `ħ/2E`. The falsifiable part is the discrete-step
> floor `τ_c ≥ τ_Planck`: a physical `τ_c` measured below it (non-back-defined) would falsify the
> discrete framework.

**Turbulence correction (important):** turbulence does *not* live in the linear `M·a` term; it lives in
the nonlinear `∇V / (u·∇)u` (paraproduct) term, and the relevant inertia is `τ_R` (first-order
relaxation-memory), not `M`.

---

## 4. The three layers

The canon is organized into exactly three layers. Collapsing them is the mistake to avoid.

### 4.1 Ontological — retention, state, lineage, tape
`δ_R → state 𝔖_n = (G_n, Λ_n, 𝒯_n) → spine → gateway`. Truth is retained first; a record is provably,
strictly lossy (`R_O ≠ D_O`, `Th_coqc`). Tape is append-only; sharing a computational node is allowed
but **lineage and residue are never erased** (`γ ≡_S γ' ⇏ γ =_R γ'`).

### 4.2 Translational — domain = translation

A **domain** is not the name of a science and not a kind of object. It is:

```
Domain 𝒟_α = 𝔃_α / ∼_α  = the minimal, sufficient, dynamically-closed translation
                            of the retained state for a question 𝒬_α.
```

Different questions give different domains: `𝒬_α ≠ 𝒬_β ⟹ 𝒟_α ≠ 𝒟_β` is allowed — there is no absolute
domain independent of readout. But domains are **not arbitrary**: a partition must pass the

**Exact Domain Gate:**
```
q_{α,n+1} ∘ F_n = F♯_{α,n} ∘ q_{α,n}          (dynamics is preserved)
O_{α,n} = O♯_{α,n} ∘ q_{α,n}                   (readout is preserved)
```
(this square is the machine-checked lumpability / `InfoQuotientCompressionExactness` theorem.)
If a collapsed distinction can come back to change the readout, the quotient is wrong and must refine.

**Sufficiency before discovery:** `Retention → State Proposal → Sufficiency Audit → Partition Discovery
→ Exact Quotient`. **Refinement cannot recover distinctions absent from its input** — *compress only
after equivalence is audited*, never compress-then-hope-discovery-recovers-it. If the state is
insufficient, *expand the state* (`𝔃^(k+1) = 𝔃^(k) ⊞ Δ𝔃_missing`); do **not** patch insufficiency by
changing the meaning of the output or importing a domain law.

**Field-count ≠ domain-count** (resolves the "how many fields?" question): a many-field system may be
*one* domain if its coupling is needed for one readout (`𝒟_α = (Φ,Ψ,χ,…)/∼_α`); a single retained field
may read out as *many* domains. The number of fields is a sufficiency/closure result, discovered — not
assumed, and not forced down to one to match a reduced equation.

**A cross-domain bridge is real only if it commutes and preserves readout:**
```
K_{β←α} F♯_α = F♯_β K_{β←α}          and          O♯_β K_{β←α} = D_{β←α} O♯_α
```
Anything else is mistranslation / lost information / insufficient resolution / a target that lacks the
needed variables / no closure. **`translatable ≠ exactly equivalent`.** Equivalence levels: `L0` surface
analogy · `L1` shared variables · `L2` shared transition signature · `L3` readout-preserving map ·
`L4` dynamically commuting quotient · `L5` recoverable bidirectional equivalence. A look-alike equation
is only `L0/L1`.

### 4.3 Epistemic — the Maker–Checker firewall

Maker–Checker is not a testing technique; it is an **epistemic firewall** that keeps answers from
leaking back into inference. *A solver cannot certify its own unrestricted interpretation.*

```
Registrar  fixes the question, allowed vs forbidden inputs, metrics, thresholds, failure rules; hashes it.
Maker      proposes state / partition / normal form / operator / prediction. Sees NO held-out outcome,
           NO checker-only label, NO answer-derived threshold.  Info(Maker ; Y_checker) = 0.
Freeze     Hash(prediction, code, config, params, score-orientation, deps) before any answer is opened.
Checker    verifies hash, coverage, invariants, exact-quotient claims, controls, error; scores by the
           frozen rule. Never changes the model or flips a sign after seeing the answer.
Auditor    Result → Scope Audit → Bounded Claim.   computed ≠ checked ≠ interpreted ≠ claimed.
Deviation  append-only; never overwrite a registered protocol.
```

Its complement is the **FAIL-ABLE gate law**: a claim counts as evidence (Type P) only if it ships
**both** a control the criterion derives as *failing* and one it derives as *passing* — otherwise it is
Type U convention, not evidence. FAIL-ABLE gates each claim; Maker–Checker separates the claimant from
the answer.

### 4.4 The general gates (the architecture around the recurrence)

Seven general principles govern *any* domain reading. They upgrade the architecture around the DRL
recurrence; the recurrence core itself does not change.

1. **No-Free-Domain-Law.** Retention alone does not hand you a domain-specific law:
   `δ_R + Retention ⇏ (F, 𝒞, V, θ)_domain`. If more than one model is retention-compatible
   (`|{ℳ : ℳ ⊨ δ_R, Retention, 𝒦}| > 1`), you may **not** declare a domain law — you owe extra
   interaction tape, observation, or a postulate. (This is the general form of the two-field / field-count
   result: a law is not free, it is *earned* with sufficiency.)

2. **Three-valued admissibility.** `𝒞(ξ | c, 𝒯) ∈ {1, 0, ⊥}` — admitted / obstructed / **unresolved**.
   `⊥` (no information) is **not** `0` (blocked): on `⊥`, *record unresolved and do not guess*. Admitted →
   expand; obstructed → record the obstruction certificate; unresolved → record and wait.

3. **Context-indexed law.** Operators are not context-free: `F_n = F_n(𝔖_n, c_n, 𝒯_n)`,
   `𝔾_n = 𝔾_n(G_n, c_n, 𝒯_n)`, `Adm_n = Adm_n(ξ; c_n, 𝒯_n)`. **valid in context `c` ⇏ valid in `c'`.**
   (The general form of state-dependent coupling `L_R[I_R]`.)

4. **State-sufficiency gate** (three-valued): `Suff_{α,L}(𝔃^cand; c, 𝒯) ∈ {1,0,⊥}`, checked *before*
   discovery/quotient. Insufficient → **expand the state** `𝔃^(k+1) = 𝔃^(k) ⊞ Δ𝔃_missing`, never patch a
   lost distinction with a threshold or decoder.

5. **Invariant-completion gate.** One invariant set may be insufficient: two states can share a
   distance-matrix `D²(g) = D²(g')` yet be separated by the readout through an orientation invariant
   `χ(g) ≠ χ(g')`. An exact quotient must therefore *also* preserve the question's invariants:
   `Inv_α = Inv♯_α ∘ q_α`. If `q(z) = q(z')` but `Inv_α(z) ≠ Inv_α(z')`, refine `C_a → C_{a,1} ⊔ C_{a,2}`.
   **apparent symmetry ≠ valid quotient symmetry.** (The general form of a readout that looked sufficient
   but was missing an invariant — e.g. the structural-camera failure.)

6. **Query-relative symmetry group.** Do not quotient by every visible symmetry — only by
   transformations that preserve the *question's* readout:
   `ℋ_α = { h : O_α(hz) = O_α(z), hF = Fh }`, and `𝒟_α = 𝔃 / ℋ_α`. (Reflection is a symmetry only if the
   readout ignores orientation; permutation only among units with truly equal interaction profiles.)

7. **Calibration firewall.** A native informational functional is **not** a physical observable until an
   independently-checked decoder says so: `y_α^known = U_α(r_RD; θ_α, c, 𝒞_α^cal)`, frozen by
   `H_cal = Hash(U_α, θ_α, training, units, protocol)` and checked against held-out data
   (`Checker → ε_cal`). **native informational functional ≠ physical observable** before calibration.

**Defect vector** (replace a single scalar error): `ε_α = (ε_suff, ε_dyn, ε_read, ε_inv, ε_bridge, ε_cal)`.
An `exact` claim requires `ε_α = 0`; otherwise it is `approximate` and must name the non-zero component.

**Must NOT enter the root** (these live in the domain tape / interpretation / empirical layer, never as a
universal axiom): a specific atom's valence, a specific molecular formula, a sample's oriented volume, a
demo calibration coefficient, "RD-cost = energy", a domain-specific geometry class, or any result derived
from synthetic data.

> **The single most general lesson:** *Retention forces the preservation of difference, but it does not
> hand out domain-specific laws for free.* And: `unknown ≠ impossible`; `an invariant that looks
> sufficient ≠ an invariant that actually preserves the readout`; `an informational value ≠ a physical
> value before calibration`.

---

## 5. The honest state (what is settled, posited, and open)

- **`M` is posited, not derived.** Eight attempts to force it from the root failed; the framework records
  this as an honest patch, not a derivation. Mass is a readout of `τ_c`.
- **Physics interpretation cards:** only the quantum sub-domain (Schrödinger dispersion, decoherence,
  uncertainty, CPTP) carries real `Th_coqc` content; the relativity "QM=SR weld" is a
  `DEFINITIONAL-RELABEL`; several other cards were audited as **hollow** (`vm_compute` of their own
  textbook formula, disconnected from `L_R`) and must not be cited as machine-checked. A label-inflation
  guard exists to catch exactly this.
- **The two-field wall, reframed:** judging `L_R I_R` by its scalar `λφ` reduction discards the
  off-diagonal/skew coupling (the *Scalar-Eigenmode Reduction Error*). Skew/rotational coupling fits in
  `L_R = L_R^(+) + L_R^(-)` under the retention metric — this repair is **`PROPOSED`, pending test T1**,
  not proven. The remaining gap is endogenous state-dependent `L_R[I_R]` (test T2).
- **Imagination** = reversible skew-transport `L_R^(-)` across still-living modes (`λ≠0`); it is *not*
  infinite — a potential-breadth inside finite meaning. At `λ=0` the mode collapses: readout is zero and
  all meanings become indistinguishable (the kernel of `L_R`).
- **Ethics** (for an AI) is not an intrinsic morality; it is a readout-selection structure. The aim is a
  system that discloses the frame it reads through, preserves every party's ability to correct and
  object (corrigibility, the `J − η` feedback), and adapts to culture without erasing the dignity and
  voice of the affected. `Dr`.
- **Blank / TBD domain bridges are recorded, never fabricated.** A *failing* bridge (a single
  quantum-only quotient that does not commute to biology) is documented as a feature, not hidden.

---

## 6. Non-claims

This document does **not** claim to: derive `G, ħ, c, k_B, α` or particle masses from first principles;
solve the Navier–Stokes Millennium problem or replace DNS/CFD; prove quantum gravity (the `α_QG =
G E²/(ħc⁵) = (E/E_Planck)²` diagnostic is a calculator, not a proof); solve GUT/quantum-gravity; be
production-ready; or replace laboratory measurement. `unit conversion ≠ derivation`;
`same equation form ≠ same retained mechanism`; `cross-domain analogy ≠ cross-domain equivalence`;
`successful report ≠ complete recovery of reality`.

---

## 7. Editing rule for the next version

Extend, never overwrite the prior anchor. Declare a tier for every new statement. Require an executable
or formal guard for any retained claim. Keep the non-claims honest. Move empirical results (benchmark
numbers, dataset runs) to a separate empirical ledger; this core holds general principles.
**Update knowledge here, in one file.**
