# Biology domain — v0.1 Biology Root-Native (Partial)

> **Read this line first:** *TWO LINES THAT MUST NEVER BE MIXED* (founder, 2026-07-21).
> **LINE-1 ROOT-NATIVE** biology = grown from the retained-difference root; NO DNA / cell / enzyme /
> fitness / external biology equation as a premise. **LINE-2 TEXTBOOK** biology solver = a calculator
> for existing biology formulas, used ONLY as a checker/calibration reference, NEVER fed back as if
> root-derived. If mixed, the project would look like it "closed biology 100%" when it only "computes
> imported formulas." This folder is `BIOLOGY_ROOT_NATIVE_PARTIAL` — LINE-1 only.

## The discipline this domain exists to enforce

None of `{DNA, gene, cell, enzyme, protein-as-premise, fitness, Hodgkin-Huxley, Michaelis-Menten,
Lotka-Volterra, Hardy-Weinberg}` may ever be a **PREMISE** anywhere in the root-native chain — each is
licensed only as a **DESTINATION** that must grow from the retained root and pass its own gate. Every
gate that claims closure ships **BOTH** a passing and a failing machine-derived control (see
`RULE_REGISTRY.json` → `gates`). "Real biology" is licensed only when a **calibrated encoding** from
retained state to biological observables exists and is checked against **event-resolved** (not
synthetic) data — it does not, here, and this README does not pretend otherwise.

## What this domain is

`biology/` is a **readout** of the master retained-distinction root
(`source_root/READOUT_GENESIS_CORE_SNAPSHOT.md`), the *same* root that feeds `../relativity/` and
`../quantum/` — not a new axiom and not an import of any named biology law. Five structural bottlenecks
close root-native:

- **BIO-G1 Ordered Sequence Carrier.** The count carrier `N^G` FAILS (`nu(ab)=nu(ba)=(1,1)` but
  `nu(F(ab))=(2,0) != nu(F(ba))=(0,2)`); the **ordered quotient** `q_seq` CLOSES exact.
  `STRUCTURALLY_CLOSED`. "Sequence" is a carrier property, not yet an amino-acid or nucleotide chain.
- **BIO-G2 Functional Quotient.** `q_F` via intervention-response equivalence — order != function
  (swap-invariant readout passes; keep-first-letter quotient breaks output factorization and fails).
  `CLOSED` as function; the word "protein" stays `PARTIAL`/`UNCALIBRATED`.
- **BIO-G3 Living-Unit Closure.** A self-maintaining fixed point `V_A=Gamma(V_A)` under a no-free-repair
  ledger `x'+e'=x+e+j-d`; `(1,1)` stays in `V_A`, a sustained deficit contract drives integrity to 0
  (mortality = irreversible exit from `V_A`). `CONDITIONALLY_CLOSED`. Not a real cell until calibrated.
- **BIO-G4 Heredity + lineage.** `q_H` via descendant signatures; frequency `p_{j,n+1}` from lineage
  counts `B` (exact fixture `B=diag(2,1)`, `N0=(1,1)` -> `p1=(2/3,1/3)`) — **NO fitness as a root
  variable**. Heredity-count `STRUCTURALLY_CLOSED`; biological-selection semantics `UNCALIBRATED`.
- **T2 endogenous operator `L_R[Theta]`.** Operator-memory augmentation: the `I`-only quotient FAILS
  (identical before the step, diverges after), the augmented `(I,Theta)` quotient CLOSES exact.
  `CLOSED_BY_AUGMENTATION`.

## What's GREEN (structurally closed, 17/36 nodes)

Run the verifier — every check is exact-rational (`fractions.Fraction`, no floats, no network):

```bash
python3 biology_closure_v0_1.py
```

It witnesses all five bottlenecks above, each with a passing AND a failing control. Additional GREEN
backing comes from four re-compiled, axiom-clean health-Coq files (2026-07-21 biology-supplement
audit): `InfoBioHomeostasis_attempt.v` (decay/turnover/homeostasis-balance),
`InfoHealthCausalRelax_attempt.v` (setpoint one-/n-step error), `InfoHealthCuspFold_attempt.v`
(bistable window, critical slowing), `InfoCoupledCuspEP3_attempt.v` (coupling energy,
locked-iff-energy-zero, one-way-breaks-conservation). These back the living-unit/homeostasis substrate
**already counted** — they do not raise the 47.2%. Full trail: [`PROVENANCE.md`](./PROVENANCE.md).

## What's YELLOW (partial / uncalibrated, 11/36 nodes)

The protein-semantic bridge, the real-cell bridge, the reproduction-branch declaration, the
biological-selection bridge, the "evolution" readout, four clinical (`Dr`) readings of the substrate
theorems, the domain-discovery battery (real, but SYNTHETIC tapes only), and the bR lineage ledger
(architecture-only, no real run). None of these are claimed closed; see `CLOSURE_AUDIT.json`.

## What's RED — open, and stays open (8/36 nodes)

**Calibrated encoding, event-resolved real data, DNA/genome, cell/organelle, enzyme kinetics, fitness,
ecology, and the LINE-2 boundary are ALL still RED.** This is deliberate:

| node | what's open |
|---|---|
| `B-X1` | **calibrated encoding** retained-state -> biological observables — the CENTRAL open bottleneck |
| `B-X2` | end-to-end root -> real biology via event-resolved data — **0%** |
| `B-X3` | DNA/genome real semantics (destination only, never a premise) |
| `B-X4` | cell/organelle real semantics (destination only) |
| `B-X5` | enzyme/catalytic-kinetics real semantics (destination only, Michaelis-Menten never a premise) |
| `B-X6` | fitness / natural-selection as a root-derived quantity (explicitly forbidden as premise) |
| `B-X7` | ecology / population-level real dynamics (Lotka-Volterra never a premise) |
| `B-X8` | LINE-2 textbook 45/45 -> root-native promotion (permanent boundary marker, checker-only) |

**The remaining hard problems are the calibrated encoding and event-resolved data — not missing
structural equations.** All five root-native bottlenecks (BIO-G1..G4, T2) already close; what's missing
is the bridge from that abstract closure to any real, measured biological system.

## Closure numbers (36-node Minimal Root-Native Biology DAG)

| Tier | Count | % of this 36-node DAG |
|---|---|---|
| green | 17 | 47.2% |
| yellow | 11 | — |
| red (open) | 8 | — |
| **strict green** | **17/36** | **47.2%** |
| **weighted** (green + yellow/2) | **22.5/36** | **62.5%** |

This is **up from the founder's pre-closure baseline 13/11/12 = 36.1%/51.4%**, driven by five state
changes: ordered-sequence carrier (Open->Closed), functional quotient (Open->Partial), living-unit
closure (Partial->Closed), heredity (Open->Closed), endogenous operator (Open->Closed). **End-to-end
root -> real biology through event-resolved data stays 0%.** See `CLOSURE_AUDIT.json -> lift`.

## How to run the verifier

```bash
python3 biology_closure_v0_1.py   # the runnable exact-rational verifier (already present, do not modify)
python3 run_tests.py              # convenience runner, prints {"decision": "PASS"/"FAIL"} JSON
```

Stdlib only. Ends with `DECISION: PASS` when every check holds.

## The two-line honesty (mandatory to preserve)

1. **Structural closure ≠ real biology.** Every witness in `biology_closure_v0_1.py` is an
   exact-rational identity over the root's own finite structures, or a re-verified axiom-clean Coq
   theorem from the health-equation corpus. None of it licenses "this is a real sequence", "this is a
   real protein", "this is a real cell", "this is real heredity/fitness", or "biology is derived from
   one root." See `CLAIM_BOUNDARY.json -> not_established` and `DRIFT_CONTRACT.json ->
   hard_fail_conditions`.
2. **Tiers are not interchangeable.** `green` (`ROOT_THEOREM`/`Th_coqc`), `yellow`
   (`PARTIAL_UNCALIBRATED`/`YELLOW_BRIDGE_PARTIAL`), and `red` (`OPEN`) are distinct and must never be
   silently promoted. `gray` (measured/calibration adapter) is not used anywhere in this domain yet —
   that gap is exactly `B-X1`.
3. **LINE-1 and LINE-2 never mix.** The textbook curriculum solver's 45/45 checklist is a CHECKER only
   (tier `textbook_closure`/`finite_diagnostic`, no `Th_coqc`) and is **never** counted toward the
   47.2%/62.5% score — represented by exactly one permanently-red boundary node, `B-X8`.
4. **Three hollow gates are explicitly excluded**, not silently dropped: the EGFR C797S same-ligand
   Jaccard gate, the EGFR contact-residue-count "rescue" gate, and the PSII near-vs-far OEC gate — all
   retracted `Type-U` (Gate Typing Law, `readout_universe`) or matched by a zero-biology control. See
   `PROVENANCE.md`.

## Files

- `biology_closure_v0_1.py` — the runnable exact-rational verifier (already present; do not modify).
- `run_tests.py` — subprocess runner, prints PASS/FAIL decision JSON.
- `CLAIM_BOUNDARY.json` — tier, public label, `two_lines` split, established / not-established lists.
- `RULE_REGISTRY.json` — every active rule (30 total in the registry, 36 counted DAG nodes when
  including the finite-diagnostic and substrate entries) with class, assumptions, parents, forbidden
  claims, plus the `BG-1..BG-4`, `BG-T2`, `BG-CAL` gate registry (every gate names both a passing and a
  failing control, per the FAIL-ABLE gate law).
- `ROOT_DAG_MASTER.md` — the standalone 36-node DAG (mermaid), rooted at `B-R0` (`a≠b`), plus the
  founder's post-closure reading chain.
- `CLOSURE_AUDIT.json` — the full 36-node closure breakdown by layer, totals, lift note, excluded
  hollow gates, LINE-2 exclusion note.
- `DRIFT_CONTRACT.json` — the executable no-contamination / no-overclaim / no-premise / no-line-mixing
  contract.
- `PROVENANCE.md` — the two-line catalog: LINE-1 green Coq + verifier witnesses vs LINE-2 textbook
  checker (explicitly walled off), the excluded hollow gates, the bR-ledger/domain-discovery real-data
  status.
- `source_root/READOUT_GENESIS_CORE_SNAPSHOT.md` — immutable snapshot of the master root this domain
  reads out from (already present, do not modify).

Following the [Domain Registration Standard](../DOMAIN_REGISTRATION_STANDARD.md), mirroring the
exemplar releases [`relativity/`](../relativity/) and [`quantum/`](../quantum/).
