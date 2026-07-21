# Relativity domain — v0.3 Finite Internal Closure

> **Read this line first:** an *internal algebraic closure* is not a proof of real physics.
> Everything in this folder is `FINITE_INTERNAL_CLOSURE` — exact-rational finite witnesses over the
> root's own causal-cone and operator structure. It is **NOT** real spacetime physics, **NOT**
> Coq-checked (with one named exception below), and **NOT** an empirical claim about the universe.

## What this domain is

`relativity/` is a **readout** of the master retained-distinction root
(`source_root/READOUT_GENESIS_CORE_SNAPSHOT.md`), not a new axiom and not an import of any external
relativity or geometry law. The whole chain runs *from the root*:

```
a≠b → distinguishability → asymmetry → ordered transitions → retention τ_c>0
   → discrete ticks t=nΔθ → finite causal graph / retention operator L_R
   → MQ.08 stepper → telegraph coarse-grain → finite front speed v=√(D/τ_c)
   → causal cone |x|≤vt
```

`v` here is the front speed of the root's own telegraph coarse-grain — it is **derived from finite
retention**, never the physical speed of light `c` inserted by hand.

From that shared cone/operator, the closure work builds two arms:

- **Observer-Cone Closure (group A, 12/12 nodes closed).** Null coordinates on the cone
  `n_± = vt ± x`, cone product `Q_v = n_+n_-`, and an observer map `B` gated by four conditions
  (path-additivity, cone-preservation, orientation, and the **one new gate**: RD-neutrality — a pure
  observer change must preserve the RD causal-cell count `n_+n_-`). That RD-neutrality gate is
  `[Proposed internal gate]`, not proved from the root; it forces a Lorentz-shaped map
  (`Γ_R`, boosts, time dilation, length contraction, relative simultaneity, velocity composition)
  that is exact and internally consistent but conditional on the gate. **This entire SR sector is
  `[Proposed internal bridge]` — never `[Th_coqc]`, never "real physics".**

- **Living-Geometry Closure (group B, 5/7 nodes closed).** The retention operator's metric readout
  `g^ij ≈ ½ Hess σ_LR` is the one node with a machine-checked base in the master core (Face 8,
  `[Th_coqc]`, operator→metric direction only — spectrum-alone→metric is explicitly forbidden).
  Everything else here — the discrete connection, the curvature certificate (two finite transports
  that fail to commute), the free-path obstruction minimizer, and the geometry↔field feedback
  commuting square — are `[finite_diagnostic]` finite-matrix witnesses, all machine-verified below.

A third arm — boundary/black-hole/quantum-gravity (group C) — is at 1/5 strict closure: graph
front-speed↔measured-speed, mass-memory, Schwarzschild `r_s=2GE/c⁴`, and Unruh `τ_c=πc/a` remain
`[DeclaredFormula]` calculator identities (same tier as the core gateway, not theorems); the horizon
bridge (`OC-05`) is now `closed` (v0.2, see below).

## v0.2 — two new internal gates close both v0.1 bottlenecks

v0.1 left two nodes `OPEN`: `OB-07` (observer-normalization/redshift) and `OC-05` (horizon bridge /
dynamic metric-source closure). v0.2 closes both — via FINITE INTERNAL CLOSURE only (algebraic, not
real physics, not Coq) — with two new internal gates, added in `relativity_closure_v0_2.py` §C/§D:

- **Gate C — Null-Transport Factorization Gate `[Proposed internal gate]`.** A diagonal observer map
  `B=diag(a,b)` factors uniquely as `B=N·diag(χ⁻¹,χ)`, with `N=√(det B)` the internal **lapse** and
  `χ=√(b/a)` the relative-observer factor. Pure observer change (`det B=1`) forces `N=1`. Redshift is
  read as the *relative retained-step rate*: `ν_o=Nν_i`. Composition is multiplicative in `N`
  (`N_j|o=N_j|i·N_i|o`, loop holonomy `H_N(C)`). The horizon is `N=0 ⟺ det B=0` — a **finite**
  rank-loss boundary, not infinity — where the observer map has no inverse. An Unruh-fix readout
  `κ_R=Normalize_N(a_local)` repairs the internal bridge to the Schwarzschild/Unruh sector without
  claiming `κ_R` is physical surface gravity. Closes `OB-07`; closes the horizon half of `OC-05`.
- **Gate D — Geometry Stationarity Gate `[Finite diagnostic]`.** The living-geometry state `Θ` obeys
  the *same* DRL retained-action grammar as the rest of the root: `S_closed = S_DRL +` a
  retained-difference cost of `Θ`. The geometry source `S_Θ = Φᵀ G_a Ψ` (reader × record changing the
  operator geometry reads — never posited as energy/mass/stress). Stationarity gives an explicit
  stepper for `Θ_{n+1}`. An exact fixture (`Θ_n=1/2, Θ_{n-1}=0, M_Θ=2, K=1, Δt=1, U_Θ=Θ²/4,
  𝔾_1=[[0,1],[1,0]], Φ_n=[1,0], Ψ_n=[0,1]`) gives `S_Θ=1`, `Θ_{n+1}=3/8`, action residual `0`. A
  **failing control** (drop the `Ψ` source, `S_Θ=0`) gives `Θ_wrong=7/8` and, checked against the
  *true* equation, residual `R_Θ=1 ≠ 0` — proving the record field `Ψ` is load-bearing, not a
  hand-picked recurrence that always succeeds. Closes the metric-source half of `OC-05`.

Both gates are exact-rational, verified in `relativity_closure_v0_2.py`, registered in
`RULE_REGISTRY.json` (`GC-01..GC-05`, `GD-01..GD-04`), and carry their own `forbidden_claims` —
neither is tagged `[Th_coqc]`; the sole `[Th_coqc]` node in the whole domain remains `OB-01`'s
operator→metric forward direction.

## v0.3 — causal-quantum-gravity Coq upgrades (quality, not quantity)

v0.3 folds in **verified, machine-checked** tier upgrades from the sibling repo
`causal-quantum-gravity/` (public curated export, 81 formal files). Full audit trail, the
green/yellow/red/gray status taxonomy, and the exact refusal reasoning are in
[`PROVENANCE_CAUSAL_QG.md`](./PROVENANCE_CAUSAL_QG.md) — read that file for the authoritative record.
Every cited `.v` file was re-verified locally (`coqc -q -R . DQG`, grep-clean of
`Admitted`/`admit`/`Axiom`/`Parameter`) before being pulled in; nothing is tagged `Th_coqc` on the
strength of a filename or a claimed tag.

**What upgraded (green):**

- **Discrete connection (`OB-03`)** and **curvature certificate (`OB-04`)**: `[finite_diagnostic]` →
  `Th_coqc`, backed by `InfoConnectionFromFrame_attempt.v` and `InfoDiscreteRiemannCurvature_attempt.v`
  (plus a supporting discrete-geometry curvature chain: metric-compatible curvature, 2nd Bianchi,
  Gauss–Bonnet, Riemann pair symmetry, rational SO(3) curvature). No continuum/manifold import.
- **Operator→metric (`OB-01`)**: stays `Th_coqc` (unchanged tier), **broadened** by
  `InfoMetricIsEnergyReadout.v`, which closes the previously-named "isolated islands" gap
  (metric-Hessian readout = mother-equation energy form).
- **Lorentzian signature foundation (under `OA-06`)**: green via `InfoLorentz.v`
  (signature-from-causal-order `≺`). This upgrades the *signature foundation only* — `OA-06` itself
  stays `[Proposed internal gate]`.
- **Geometry back-reaction joint (`GD-01`/`GD-03`)**: a green PARTIAL joint via `InfoBackReaction.v`
  (edge-strain/budget exactness); tier stays `[finite_diagnostic]`, full `GD-04` source law stays open.

**What did NOT upgrade, on purpose:**

- **`Γ_R` and the whole observer-transform sector (`OA-07`…`OA-12`)** remain
  `[Proposed internal bridge]`. Nothing in the causal-quantum-gravity corpus derives `Γ_R`
  root-natively.
- **`InfoLorentzInvariance.v` and `InfoQuantumRelativityUnification.v` were CHECKED AND REFUSED.**
  Both compile axiom-free, but `InfoLorentzInvariance.v` imports the Minkowski interval and the boost
  constraint as premises — the repo's own `completeness-and-claims.md` says "POSITED, not forced by
  the graph root." `InfoQuantumRelativityUnification.v`'s result inherits that same imported signature,
  so it is a bounded *algebraic identity* between two independently-posited constructions, never "QM
  and SR derived from one root." Pulling either in as a root-native derivation would repeat exactly the
  secret-import hollow-card mistake the founder's anti-hollow-card discipline exists to catch — so
  neither is tagged `Th_coqc` here. See `PROVENANCE_CAUSAL_QG.md` → "REFUSED" for the full list
  (also `InfoAnalysisLift.v`, `InfoQuantumGravityRootBridge_attempt.v`).
- **Node-8 (observer-normalization / redshift / lapse, `OB-07`/`GC-01`..`GC-05`)** got no new
  `coq_backing`. `InfoTelegraphHorizonUnification_attempt.v` is verified green but proves a
  *distinct* object — the spine's own classical/quantum crossover discriminant `λ_c=D²/4MK` — not
  node-8's lapse `N=√detB` / redshift `ν_o=Nν_i`.

**Percentage is unchanged.** These are `[finite_diagnostic]` → `Th_coqc` **quality** upgrades on nodes
that were already counted `closed` in the v0.2 audit — not `open` → `closed` moves. The 24-node
Minimal Relativity DAG closure stays exactly `19/24=79.2%` strict, `21.5/24=89.6%` weighted; see
`CLOSURE_AUDIT.json` → `percentage_unchanged_note`.

## How to run the verifiers

```bash
python3 relativity_closure_v0_1.py   # immutable v0.1 anchor, unmodified
python3 relativity_closure_v0_2.py   # current release: v0.1 witnesses + Gate C + Gate D
```

Stdlib only (uses `fractions.Fraction` for exact rational arithmetic — no floats, no network). Each
prints every witness check and ends with `DECISION: PASS` when all checks hold. A convenience runner
is also provided:

```bash
python3 run_tests.py
```

which subprocess-invokes both verifiers and prints a `{"decision": "PASS"}` / `{"decision": "FAIL"}`
JSON per script plus an overall decision, based on their exit codes.

## The closure audit (24-node Minimal Relativity DAG)

| Group | Nodes | Closed | Partial | Open |
|---|---|---|---|---|
| A — observer/kinematics | 12 | 12 | 0 | 0 |
| B — geometry/GR | 7 | 6 | 1 | 0 |
| C — boundary/BH/QG | 5 | 1 | 4 | 0 |
| **Total** | **24** | **19** | **5** | **0** |

Strict closure: `19/24 = 79.2%`. Weighted (partial counted as ½): `21.5/24 = 89.6%`. This percentage
is **of this 24-node Minimal Relativity DAG only** — not of "all of relativity" or "all textbook
formulas". Lift chain on this same DAG: `16.7% → 70.8% (v0.1) → 79.2% (v0.2)` strict, `→ 81.25% (v0.1)
→ 89.6% (v0.2)` weighted. See `CLOSURE_AUDIT.json` for the full per-node breakdown.

## The two-level honesty (mandatory to preserve)

1. **Internal algebraic closure ≠ proof of real physics.** Every witness in
   `relativity_closure_v0_1.py` and `relativity_closure_v0_2.py` is an exact-rational identity over
   the root's own finite structures. None of it is checked against a real measurement, none of it is
   Coq-proved except the one named Face 8 direction, and none of it licenses "this is the physical
   Lorentz transform", "`c` is derived here", "`N` is a real physical lapse", "`κ_R` is real surface
   gravity", or "`S_Θ` is real stress-energy". See `CLAIM_BOUNDARY.json` → `not_established` and
   `DRIFT_CONTRACT.json` → `hard_fail_conditions` for the enforced boundary.
2. **Tiers are not interchangeable.** `[Th_coqc]` (one node only: operator→metric, Face 8),
   `[Proposed internal bridge]` / `[Proposed internal gate]` (the whole SR sector, plus Gate C's core),
   `[finite_diagnostic]` (living-geometry finite-matrix witnesses, plus Gate C's readouts and Gate D),
   `[DeclaredFormula]` (Schwarzschild, Unruh — calculator identities, not theorems), and `OPEN`
   (unresolved bottlenecks — none remain in v0.2) are distinct and must never be silently promoted.

## What closed, and what's still open

Both v0.1 bottlenecks (`OB-07` observer-normalization/redshift, `OC-05` horizon bridge / dynamic
metric-source closure) are **closed in v0.2** — see Gate C and Gate D above. Nothing remains `OPEN` on
this DAG.

What remains `partial` — and this is exactly what still blocks promotion beyond
`FINITE_INTERNAL_CLOSURE` to any real-physics tier — is five real-physics **calibration gaps**, not
missing internal algebra:

1. **`v` = measured speed of light `c`** (`OC-01`) — still only declared, not derived or calibrated.
2. **Mass-memory correspondence** (`OC-02`) — still only declared.
3. **Schwarzschild-as-derived** (`OC-03`) — remains a `[DeclaredFormula]` calculator identity.
4. **Unruh-as-derived** (`OC-04`) — remains `[DeclaredFormula]`; the v0.2 Unruh-fix repairs only the
   *internal* bridge (`κ_R=Normalize_N(a_local)`), not the physical identification.
5. **Full basis covariance / minimal closed state** (`OB-02`) — unchanged from v0.1, still partial.

Until those five close — and none may close by importing a named external law as a premise, per
`DRIFT_CONTRACT.json` — the domain stays at `FINITE_INTERNAL_CLOSURE`.

## Files

- `relativity_closure_v0_1.py` — the immutable v0.1 verifier anchor (do not modify).
- `relativity_closure_v0_2.py` — the current runnable exact-rational verifier (v0.1 witnesses +
  Gate C + Gate D).
- `run_tests.py` — subprocess runner around both verifiers, prints PASS/FAIL decision JSON.
- `CLAIM_BOUNDARY.json` — tier, public label, established / not-established lists.
- `RULE_REGISTRY.json` — every active rule with its class, assumptions, parents, and forbidden claims.
- `ROOT_DAG_MASTER.md` — the standalone DAG (mermaid), rooted at `P0` (`a≠b`).
- `CLOSURE_AUDIT.json` — the full 24-node closure breakdown, the v0.2 gates, and the five remaining
  real-physics-calibration bottlenecks.
- `DRIFT_CONTRACT.json` — the executable no-contamination / no-overclaim contract.
- `PROVENANCE_CAUSAL_QG.md` — the authoritative record of the v0.3 causal-quantum-gravity Coq upgrades
  (verified green, refused, and status taxonomy).
- `source_root/READOUT_GENESIS_CORE_SNAPSHOT.md` — immutable snapshot of the master root this domain
  reads out from (already present, do not modify).

Following the [Domain Registration Standard](../DOMAIN_REGISTRATION_STANDARD.md), mirroring the
exemplar release [`chem/`](../chem/).
