# Quantum domain — v0.1 Quantum Root Closure (Partial)

> **Read this line first:** `oscillation is NOT yet quantum.` Everything in this folder is
> `QUANTUM_ROOT_CLOSURE_PARTIAL` — exact-rational finite witnesses (plus a small, re-verified set of
> Coq-green causal-quantum-gravity theorems) over the root's own retained-distinction structure. It is
> **NOT** real quantum mechanics, **NOT** Born-rule-derived, **NOT** a Hilbert-space construction, and
> **NOT** an empirical claim about the universe.

## The discipline this domain exists to enforce

The founder's own words (2026-07-21), verbatim intent: *do NOT repeat the hollow quantum-card mistake
of taking an "equation that looks quantum" and calling it closed. "oscillation is NOT yet quantum."*

None of the following may ever be a **PREMISE** anywhere in this domain — each is licensed only as a
**DESTINATION** that must grow from the retained root and pass its own gate:

```
i · psi · Hilbert space H · Born rule p=|psi|^2 · tensor product ⊗ · [A,B]=i*hbar
spin · particles · creation/annihilation operators · vacuum · coupling constants
```

Every gate that claims closure ships **BOTH** a passing and a failing machine-derived control — a gate
without both is a `Type-U` convention and must never be claimed closed (see `RULE_REGISTRY.json` →
`gates`, `QG-1..QG-14`). The word **"quantum"** is licensed only when **state + norm + composition +
channel + measurement close TOGETHER** — they do not, here, and this README does not pretend otherwise.

## What this domain is

`quantum/` is a **readout** of the master retained-distinction root
(`source_root/READOUT_GENESIS_CORE_SNAPSHOT.md`), the *same* root that feeds `../relativity/` — not a
new axiom and not an import of any named quantum-mechanical law. The chain runs *from the root*:

```
a≠b → distinguishability → asymmetry → ordered transitions → retention τ_c>0
   → discrete ticks → retained-distinction axioms FORCE the L_R operator form
   → telegraph coarse-grain / spine PDE (M∂²+D∂+K) → characteristic equation
   → oscillatory-regime split λ_c=D²/4MK
```

From that shared spine, two more branches close formally:

- **Asymmetric-seed / torsion branch.** `R0 = DiagPart + SymOff + SkewOff`, exact and unique
  (`Th_coqc`), with `SkewOff` — the torsion/circulation branch — forming a group with genuine
  (non-degenerate) mixing at rank `N`. **`SkewOff` is NOT spin** — no rotation-group representation or
  half-integer quantization has been built; `spin/spin-statistics` (`Q-X11`) stays fully `RED`.
- **Complexification / norm / evolution branch.** A closed real oriented mode-pair with an orientation
  `J` (`J²=-I`, `G`-skew: `J^{†_G}=-J`) **EARNS** the complex coordinate `psi=u+Jv` as a **readout**,
  never a premise — with a machine-verified **failing control** (`J_bad=I`, `J_bad²=+I`, correctly
  refused). On that same closed pair: a positive quantum norm `N_Q(psi)≥0` (`=0` iff `psi=0`), and
  reversible `G`-orthogonal evolution that provably preserves it.

## What's GREEN (formal-closed, 14/32 nodes)

Run the verifier — every check below is exact-rational (`fractions.Fraction`, no floats, no network):

```bash
python3 quantum_closure_v0_1.py
```

It witnesses: the oscillatory split (§A), the complexification gate with its failing control (§B),
positive norm + reversible evolution (§C), the seed trifurcation (§D), and the Born-candidate
refinement-consistency finite diagnostic (§E — evidence, not a uniqueness proof). Additional GREEN
backing comes from the causal-quantum-gravity Coq corpus, **re-compiled axiom-clean today**
(`coqc -q -R . DQG`): `InfoRetainedDistinctionForcesLaplacian_attempt.v` (forces the `L_R` form),
`InfoAsymmetricSeedTrifurcation.v`, `InfoSeedTorsionIsSkewOff.v` / `InfoSeedTorsionGroupAndRankN.v` /
`InfoSeedTorsionGenuineMixing.v`, `InfoMemoryBeforeMass.v`, and the discrete metric/curvature chain
folded in from `../relativity/` (`OB-03`/`OB-04`). Full audit trail:
[`PROVENANCE_CAUSAL_QG.md`](./PROVENANCE_CAUSAL_QG.md).

## What's YELLOW (formal-closed, bridge-partial, 6/32 nodes)

- **QM/SR bounded algebraic identity** (`Q-Y1`) — `InfoQuantumRelativityUnification.v` compiles
  axiom-free, but its `box_quad` **inherits an imported Minkowski signature** from `relativity/`'s
  refused `InfoLorentzInvariance.v`. This is a bounded algebraic identity between two independently
  posited constructions — **never** "QM and SR derived from one root." **CRITICAL CAVEAT, do not
  overclaim this.**
- **Telegraph crossover discriminant** (`Q-Y2`) — a real, green threshold theorem
  (`quantum_iff_above_horizon`), but the bridge from "above the threshold" to "this regime IS quantum"
  is not established; distinct from `relativity/`'s node-8 lapse/redshift.
- **`v²=K/M` conditional oscillator-parameter identification** (`Q-Y3`) — declared, not derived.
- **Metric/curvature-to-quantum-regime bridge** (`Q-Y4`) — the geometry (`Q-G1`) is green; its bridge
  into a quantum-regime reading is not established.
- **Memory-before-mass physical bridge** (`Q-Y5`) — the algebra (`Q-M1`) is green; the "this is real
  mass" identification is declared, not derived.
- **Channel/CPTP formal card** (`Q-Y6`) — the target definition exists; the bridge from the root's
  reversible evolution to a general CPTP (open-system) map is open, both controls `NOT YET
  CONSTRUCTED`.

## What's RED — open, and stays open (12/32 nodes)

**Born/measurement, spin, subsystem composition, and QFT are ALL still RED.** This is deliberate and
must not be blurred:

| node | what's open |
|---|---|
| `Q-X1` | general root-derived complex `psi` (only the single closed-pair witness exists) |
| `Q-X2` | **quantum quotient `q_Q`** — architecture sketched, commuting-square NOT proven; central bottleneck |
| `Q-X3` | mixed-state from hidden lineage |
| `Q-X4` | subsystem composition `⊗_κ` |
| `Q-X6` | **measurement / Born-rule uniqueness** — TARGET only; §E's refinement-consistency check is evidence FOR the quadratic form on one refinement, not a uniqueness proof |
| `Q-X7` | conditional update / collapse |
| `Q-X8` | uncertainty relation — a formal guard survived the hollow-card audit but is a boundary check, not a root derivation |
| `Q-X9` | correlation / CHSH / Tsirelson bound — same: boundary guard, not root derivation |
| `Q-X10` | mass / particle layer (beyond the formal memory-mass algebra) |
| `Q-X11` | **spin / spin-statistics** — fully open; the torsion branch is NOT spin |
| `Q-X12` | **QFT** — needs `q_Q` + relativity's `q_g` + a geometry `q_geometry` jointly, none complete |
| `Q-X13` | superposition gate — only a narrow fixed-operator case exists, not a general principle |

## Closure numbers (32-node Quantum DAG)

| Tier | Count | % of this 32-node DAG |
|---|---|---|
| green | 14 | 43.75% |
| yellow | 6 | — |
| red (open) | 12 | — |
| **strict green** | **14/32** | **43.75%** |
| **weighted** (green + yellow/2) | **17/32** | **53.1%** |

This is **up from the founder's first-pass 10/32=31.25%** baseline, because the causal-quantum-gravity
green nodes (forced-`L_R`, seed trifurcation/torsion, metric/curvature chain) were undercounted in the
first pass — folding them in raised the count. **Born/measurement/spin/composition/QFT stay RED
throughout this rescore; none of them were used to inflate the percentage.** See
`CLOSURE_AUDIT.json` → `rescore_note` and `remaining_red`.

## How to run the verifier

```bash
python3 quantum_closure_v0_1.py   # the runnable exact-rational verifier
python3 run_tests.py              # convenience runner, prints {"decision": "PASS"/"FAIL"} JSON
```

Stdlib only (uses `fractions.Fraction` for exact rational arithmetic — no floats, no network). Ends
with `DECISION: PASS` when every check holds.

## The closing order (roadmap, not a claim of progress made)

The founder's closing order for this domain, Q1→Q10 — **none of Q2 onward are closed by this
release**; only Q1 (and only in the narrow, gated senses described above) has any green content:

1. **Q1 — complexification** (`Q-C1`): closed, narrow (single closed-pair witness); general case (`Q-X1`) open.
2. **Q2 — norm/positivity, general**: closed on one witness (`Q-N1`); general case open.
3. **Q3 — reversible evolution, general**: closed on one witness (`Q-N2`); general case open.
4. **Q4 — quantum quotient `q_Q`**: open (`Q-X2`), central bottleneck.
5. **Q5 — mixed states**: open (`Q-X3`).
6. **Q6 — composition / `⊗_κ`**: open (`Q-X4`).
7. **Q7 — channel / CPTP**: yellow bridge card only (`Q-Y6`); root-native construction open.
8. **Q8 — measurement / Born uniqueness**: open (`Q-X6`), one finite-diagnostic data point only.
9. **Q9 — spin / statistics**: fully open (`Q-X11`).
10. **Q10 — QFT**: fully open (`Q-X12`), needs `q_Q` + relativity's `q_g` + geometry jointly.

## The two-level honesty (mandatory to preserve)

1. **Formal/structural closure ≠ real quantum mechanics.** Every witness in `quantum_closure_v0_1.py`
   is an exact-rational identity over the root's own finite structures, or a re-verified axiom-free
   Coq theorem from the causal-quantum-gravity corpus. None of it licenses "this is `i`", "this is
   the wavefunction", "this is the Born rule", "this is a Hilbert space", "this is spin", or "QM is
   derived from one root." See `CLAIM_BOUNDARY.json` → `not_established` and `DRIFT_CONTRACT.json` →
   `hard_fail_conditions`.
2. **Tiers are not interchangeable.** `green` (`Th_coqc` or exact-rational finite witness with both
   controls), `yellow` (`YELLOW_BRIDGE_PARTIAL`, formal-closed / semantic-bridge-partial), and `red`
   (`OPEN`) are distinct and must never be silently promoted. `gray` (measured/calibration adapter) is
   not used anywhere in this domain yet.

## Files

- `quantum_closure_v0_1.py` — the runnable exact-rational verifier (already present; do not modify).
- `run_tests.py` — subprocess runner, prints PASS/FAIL decision JSON.
- `CLAIM_BOUNDARY.json` — tier, public label, established / not-established lists.
- `RULE_REGISTRY.json` — every active rule (33 total: 32 counted DAG nodes + 1 cited support rule)
  with class, assumptions, parents, forbidden claims, plus the `QG-1..QG-14` gate registry (every
  gate names both a passing and a failing control, per the FAIL-ABLE gate law).
- `ROOT_DAG_MASTER.md` — the standalone 32-node DAG (mermaid), rooted at `Q-R0` (`a≠b`), plus the
  corrected unified causal-QG DAG view.
- `CLOSURE_AUDIT.json` — the full 32-node closure breakdown, totals, rescore note, remaining red list.
- `DRIFT_CONTRACT.json` — the executable no-contamination / no-overclaim / no-premise contract.
- `PROVENANCE_CAUSAL_QG.md` — the authoritative record of the causal-quantum-gravity Coq upgrades
  (verified green, verified-green-but-yellow, and refused).
- `source_root/READOUT_GENESIS_CORE_SNAPSHOT.md` — immutable snapshot of the master root this domain
  reads out from (already present, do not modify).

Following the [Domain Registration Standard](../DOMAIN_REGISTRATION_STANDARD.md), mirroring the
exemplar releases [`chem/`](../chem/) and [`relativity/`](../relativity/).
