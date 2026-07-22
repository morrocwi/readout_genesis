# Biology Translation Compiler v0.2

This extension fills the **architecture gap** between the existing root-native Biology v0.1 equations and explicit biological language.

It does **not** claim that real biology has been derived from the retained root. Instead, it provides the missing typed bridges, observables, gates, controls, and calibration debts needed to translate the existing equations into biological semantics without contaminating the root-native line.

## Why this extension exists

Biology Root-Native v0.1 already closes several abstract structures:

- ordered sequence carrier,
- functional quotient,
- bounded self-maintaining unit,
- heredity quotient and lineage counts,
- endogenous operator-memory augmentation,
- formal homeostasis, relaxation, cusp-fold, and coupled substrates.

However, the existing domain correctly leaves the following unresolved:

- real molecular identity,
- real sequence and macromolecular semantics,
- binding and catalysis,
- membrane and compartment semantics,
- resource and metabolic ledgers,
- cellular regulation and identity,
- reproduction and lineage in measured biology,
- multicellular tissue organization,
- matrix, vascular, immune, and repair contexts,
- pathology and cancer semantics.

This extension declares all of those missing bridges and makes each one fail-able.

## Dependency order

```text
Retained root
  -> Standard Model frontier
  -> Information Chemistry composition layer
  -> biomolecular semantic encoders
  -> bounded cellular semantic encoders
  -> multicellular and tissue semantic encoders
  -> pathology semantic encoders
  -> bounded report
```

The order is mandatory. A downstream domain label may never be inserted upstream as a premise.

## Files

- `BIOLOGICAL_TRANSLATION_STACK_v0_2.yaml` — JSON-compatible YAML containing the full compiler stack, equations, dependencies, nineteen biological modules, required observables, controls, and statuses.
- `ROOT_TO_BIOLOGICAL_SEMANTICS_DAG_v0_2.md` — standalone DAG from the retained root through Standard Model and chemistry dependencies to explicit biological semantics.
- `CLAIM_BOUNDARY.json` — what this extension establishes and explicitly does not establish.
- `DRIFT_CONTRACT.json` — hard-fail conditions against premise smuggling, tier inflation, calibration leakage, and clinical overreach.
- `verify_translation_stack_v0_2.py` — standard-library fail-closed architecture verifier with negative controls.
- `run_tests.py` — convenience runner.

## Run

```bash
cd domains/biology/translation_v0_2
python3 run_tests.py
```

Expected result:

```json
{"decision": "PASS", "runner": "translation_v0_2/run_tests.py"}
```

A PASS verifies only:

- JSON-compatible YAML parsing,
- English-only standalone metadata,
- stage and module dependency closure,
- DAG acyclicity,
- required observables and dual controls,
- declared Standard Model and chemistry debts,
- root semantic-preload protection,
- key molecular-to-cell-to-tissue-to-pathology path presence,
- claim-boundary and drift-contract consistency.

It does not verify real molecules, cells, tissues, cancer, or any other biological system.

## Biological compiler path

The compiler contains nineteen modules:

1. molecular identity,
2. ordered polymer sequence,
3. conformation,
4. binding and complex identity,
5. catalysis,
6. membrane and compartment,
7. resource and metabolic ledger,
8. regulatory memory,
9. signal decoder,
10. cell identity and viability,
11. reproduction and lineage,
12. spatial tissue organization,
13. matrix, niche, and vascular transport,
14. immune audit,
15. tissue repair and corrigibility,
16. unreported decoder drift,
17. cross-scale corrigibility rupture,
18. hierarchy inversion and operator capture,
19. cancer-like persistent pathological regime.

Every module declares:

```text
parents
root-native inputs
biological output
required measured observables
gate
passing control
failing control
status
```

## Standard Model relation

The extension uses Standard Model outputs only at their declared tiers:

- connection, holonomy, and curvature substrate,
- readout-preserving automorphism concept,
- orientation and chirality grading inside declared architectures,
- order-carrier and vector-mass rank patterns inside declared architectures,
- calibrated electroweak decoder slots.

It preserves the open debts:

- unrestricted-root gauge kernel,
- unrestricted gauge-algebra uniqueness,
- physical couplings and masses derived from root,
- interacting chiral gauge measure,
- generations and mixing,
- spin-statistics,
- end-to-end Standard Model derivation.

Therefore Standard Model structure is a dependency and calibration layer, not a completed root-derived premise.

## Chemistry relation

The extension uses Information Chemistry v0.910 as a formal composition-quotient dependency. It does not treat composition closure as proof of real atomic or molecular chemistry.

Before a real molecular label is admitted, the compiler requires measured identity readers such as composition, structure-sensitive signatures, context, event-resolved association or reaction records, and independent controls.

## The biological onset equation

The cross-scale onset candidate is:

```text
n_star = earliest n such that
  connection remains present,
  cellular decoder state differs from the tissue model,
  tissue orchestration no longer predicts cellular transition,
  the measured repair set is empty,
  and cellular viability remains present.
```

Biologically, this means the tissue still communicates with the cell, but the cell interprets the signal through a changed regulatory state that is not correctly represented in the tissue-level model. The problem is not simple channel loss. It is connection without shared corrigibility.

## Current honest decision

```text
Architecture for biological translation: available
Root-native Biology v0.1 closure score: unchanged
End-to-end Standard Model: open
Real chemistry: open
Calibrated biological encoders: open
Event-resolved biological validation: open
Clinical use: prohibited
```
