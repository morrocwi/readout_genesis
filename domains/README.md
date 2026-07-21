<!-- Registry of domain leaves. Each is a readout of the one root, at a bounded tier. -->

# 🧬 Registered Domains — READOUT GENESIS

> A **domain is a translation** `q_D` of the one retained structure — never a new root. Each folder
> here is a **readout** of `../READOUT_GENESIS_CORE.md`, registered under a fixed contract so it can
> never contaminate the master-equation lineage. The contract: [`DOMAIN_REGISTRATION_STANDARD.md`](DOMAIN_REGISTRATION_STANDARD.md).

```
                 [ READOUT_GENESIS_CORE.md ]          the one root  (δ_R → L_R → spine)
                            │  domain = translation  q_D
                            ▼
   ┌────────────────────────────────────────────────────────────────┐
   │  registered domain leaves — each a bounded-tier readout          │
   │                                                                  │
   │   chem/   Information Chemistry v0.910   FORMAL_COMPOSITION_      │
   │           (free ℕ^G carrier + quotient    QUOTIENT_ONLY   ✅ PASS │
   │            gates + lineage sidecar)                               │
   └────────────────────────────────────────────────────────────────┘
```

## Registered

| domain | release | tier | status | not established (headline) |
|---|---|---|---|---|
| [`chem/`](chem/) | Information Chemistry v0.910 | `FORMAL_COMPOSITION_QUOTIENT_ONLY` | ✅ `PASS` (dual-checker + peer review) | chemical semantics · periodic-table identity · formula/molecular identity · reaction occurrence |
| [`relativity/`](relativity/) | Relativity finite-internal-closure v0.3 | `FINITE_INTERNAL_CLOSURE` | ⏳ `79.2%` strict / `89.6%` weighted (exact-rational verifier PASS; connection/curvature Th_coqc via causal-quantum-gravity) | real physics · v=c · surface gravity · stress-energy · full GR/QFT · root-native Γ_R (still Proposed) |
| [`quantum/`](quantum/) | Quantum root-closure-partial v0.1 | `QUANTUM_ROOT_CLOSURE_PARTIAL` | ⏳ `43.75%` strict green / `53.1%` weighted (verifier PASS; oscillation≠quantum) | real QM · i/ψ/Hilbert/Born/tensor/spin as fundamental · Born uniqueness · measurement · composition · entanglement · spin · QFT (all RED) |
| [`biology/`](biology/) | Biology root-native-partial v0.1 | `BIOLOGY_ROOT_NATIVE_PARTIAL` | ⏳ `47.2%` strict / `62.5%` weighted root-native (verifier PASS); real end-to-end `0%` | real biology · DNA/cell/enzyme/fitness as premise · protein/cell semantics · biological selection · calibrated encoding · (textbook 45/45 is LINE-2 checker, NOT counted) |

## Frontier (roadmaps — NOT closed domains, no verifier by design)

| domain | kind | root-derived | what it is |
|---|---|---|---|
| [`standard_model/`](standard_model/) | `FRONTIER_ROADMAP` | **0%** | root-native Standard Model DAG + the survey of verified gauge *substrate* (connection/holonomy/curvature Th_coqc, Heisenberg group, SO(3), Noether, a proven gauge invariance) + **SM-G0** = where to start. Imports of `SU(3)×SU(2)×U(1)`/particles/Higgs as premises are drift-contract hard-fails. See [`standard_model/ROOT_TO_SM_DAG.md`](standard_model/ROOT_TO_SM_DAG.md). |

## How to read a domain folder

Each `<D>/` ships its own `CLAIM_BOUNDARY`, `RULE_REGISTRY`, `ROOT_DAG_MASTER`, `DRIFT_CONTRACT`,
verification bundle (proof kernel + dual-implementation checker + tests + checksums + immutable
anchors), and a `source_root/READOUT_GENESIS_CORE_SNAPSHOT.md` anchoring it back to the master. Run
`python run_all_tests_<D>.py` inside the folder to re-verify from a clean extraction (standard library
only, no network).

## The one honest boundary every domain keeps

A registered domain proves its **structural / formal** layer. It does **not** claim the real domain's
semantics until a **calibrated encoding** from retained states to the domain's registry is supplied
and independently checked. That open obstruction is stated in each release — discoverability of the
form is not truth of the content.
