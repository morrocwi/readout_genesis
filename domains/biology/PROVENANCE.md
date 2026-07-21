<!-- Two-line provenance catalog: LINE-1 root-native Coq/verifier witnesses vs LINE-2 textbook checker. -->

# Provenance — biology domain (2026-07-21)

**TWO LINES THAT MUST NEVER BE MIXED** (founder, verbatim intent): LINE-1 ROOT-NATIVE biology grows
only from the retained-difference root — no DNA, cell, enzyme, fitness, or external biology equation
as a premise. LINE-2 TEXTBOOK biology is a calculator for existing formulas, used only as a
checker/calibration reference, never fed back as if root-derived. This file catalogs the provenance of
every piece of evidence in this domain and walls the two lines apart, explicitly.

## LINE-1 — root-native (counted toward the 47.2% strict / 62.5% weighted score)

### Verifier witnesses (`biology_closure_v0_1.py`, exact rational, no floats)

| bottleneck | witness | passing control | failing control |
|---|---|---|---|
| BIO-G1 ordered sequence | count carrier vs ordered carrier on 2-letter words | ordered `ab != ba` -> `q_seq` closes | `nu(ab)=nu(ba)=(1,1)` but `nu(F(ab))!=nu(F(ba))` -> count carrier fails |
| BIO-G2 functional quotient | swap-invariant readout `O(w)` | `O(swap(w))==O(w)` all `w` | `q_first` breaks output factorization |
| BIO-G3 living-unit closure | no-free-repair ledger fixed point | `(1,1)` stays in `V_A` under contract `{(0,0),(1,1)}` | sustained `(d,j)=(1,0)` drives integrity to 0, exits `V_A` |
| BIO-G4 heredity | lineage-count matrix `B`, frequency `p1` | `N1=B*N0=(2,1)`, `p1=(2/3,1/3)` | coarse parent-quotient merges classes with different replication counts (2 != 1) |
| T2 endogenous operator | `(I,Theta)` augmentation | augmented quotient distinguishes `z1,z2` | `I`-only quotient identical before, diverges after |

All five run and PASS under `python3 biology_closure_v0_1.py` (already present, unmodified, exact
`fractions.Fraction` arithmetic).

### Green Coq substrate (re-compiled axiom-clean, root-native, 2026-07-21 biology-supplement audit)

Source: `research_universal_solver/formal/` (BIRCA health/bio equations -> discrete axiom-free Coq).

| file | theorems | backs | tier |
|---|---|---|---|
| `InfoBioHomeostasis_attempt.v` | `decay_geometric`, `homeostasis_balance`, `turnover_is_production` | B-SUB1, BIO-G3 substrate quality | green (Th_coqc) |
| `InfoHealthCausalRelax_attempt.v` | setpoint one-step error, n-step error | B-SUB2, BIO-G3 substrate quality | green (Th_coqc) |
| `InfoHealthCuspFold_attempt.v` | bistable window, critical slowing | B-SUB3, BIO-G3 substrate quality | green (Th_coqc) |
| `InfoCoupledCuspEP3_attempt.v` | coupling energy, locked-iff-energy-zero, one-way-breaks-conservation | B-SUB4, T2 substrate quality | green (Th_coqc) |

These four back the living-unit/homeostasis/relaxation SUBSTRATE nodes already counted in
`CLOSURE_AUDIT.json` (quality evidence for BIO-G3/T2) — they do **not** raise the 47.2%/62.5% score;
they are cited support, exactly parallel to how `quantum/PROVENANCE_CAUSAL_QG.md` folds in supporting
theorems without inflating the DAG node count. Their clinical readings (real physiological homeostasis,
recovery, disease bistability, hormonal/neural coupling) are declared, not derived — `Dr` bridges
(`B-Y6..B-Y9`), open pending calibration.

### REFUSED for LINE-1 (checker-only)

| file | why refused |
|---|---|
| `InfoEpidemicThreshold_attempt.v` | Imports the SIR (Susceptible-Infected-Recovered) model as a premise, not root-derived. This is a LINE-2 textbook item — kept as a checker-only reference (`B-X8` boundary marker), never cited as root-native evidence anywhere in `RULE_REGISTRY.json`. |

## LINE-2 — textbook checker (never counted toward the score)

The curriculum biology solver: 45/45 checklist items, tier `textbook_closure`/`finite_diagnostic`, NO
`Th_coqc` anywhere. Five items are declared `[Open]` by the solver itself: full Hodgkin-Huxley,
MD/protein-folding, Luria-Delbrück fluctuation test, Turing-pattern selection, ML-based phylogeny
inference. This solver exists ONLY as a calculator/checker for existing biology formulas — it is
reference material for calibration work, not evidence for the root-native DAG. `RULE_REGISTRY.json`
represents its existence with exactly one node, `B-X8`, permanently `red`, whose sole purpose is to
make the exclusion explicit and auditable. See `DRIFT_CONTRACT.json -> hard_fail_conditions` for the
executable version of this rule.

## Excluded hollow gates (retracted Type-U, Gate Typing Law — readout_universe)

None of the following are used as biology evidence anywhere in this domain; they are recorded here so
the exclusion is auditable, not silent:

- **EGFR C797S same-ligand Jaccard gate** — retracted Type-U.
- **EGFR contact-residue-count "rescue" gate** — retracted Type-U.
- **PSII near-vs-far OEC gate** — a zero-biology control matched the signal, i.e. the gate could not
  distinguish a biologically meaningful case from a null case; retracted.

## Real-data honesty (bR ledger + domain-discovery battery)

- **Domain-discovery battery** (`readout_genesis/scripts/domain_discovery_battery.py`) is real and
  runnable — `PASS` — but has been run only on **SYNTHETIC** tapes. No event-resolved real biological
  data has ever been passed through it. Recorded as `B-Y10`, yellow, bridge open.
- **bacteriorhodopsin (bR) lineage ledger** and its CLI are narrated and architected in the core
  snapshot, but are **architecture-only** — no real event-resolved run has ever been executed.
  Recorded as `B-Y11`, yellow, bridge open.

Neither of these constitutes the calibrated encoding (`B-X1`) or the end-to-end real-biology result
(`B-X2`) — both stay fully `OPEN`, `red`, 0%.
