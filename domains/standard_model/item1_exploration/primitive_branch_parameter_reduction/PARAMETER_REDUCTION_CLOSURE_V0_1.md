# Native-RD U/D/E Parameter-Reduction Closure v0.1 — candidate

## Decision

This candidate removes five operational dials from the declared finite-architecture exchange-to-order subchain:

```text
before: M, C_RD, lambda_U, lambda_D, lambda_E  (5 possible fitted/tunable numbers)
after:  no free dial in this subchain          (0)
```

The reduction is not produced by setting arbitrary numerical values:

- `M` is supplied only by the merged operational calibration report with status `CALIBRATED_READY`;
- `C_RD=1` is a native-unit gauge fixing, not a physical coupling and not a user-adjustable number;
- `lambda_U`, `lambda_D`, and `lambda_E` are computed from three independent primitive branch tapes;
- `Pi0=3 lambda_U + 3 lambda_D + lambda_E` is consequently an output.

`alpha`, `beta`, physical gauge couplings, Yukawa data, and laboratory branch identification are not reduced by this candidate.

## Full operational chain

```text
Reader/Record calibration
  -> M_joint
  -> fixed native unit C_RD = 1
  -> independent primitive U/D/E branch tapes
  -> signed exchange_j
  -> Delta_j = sum |exchange step|
  -> lambda_j = exp(-Delta_j)
  -> Pi0 = 3 lambda_U + 3 lambda_D + lambda_E
```

Every branch must declare:

- `path_semantics=primitive_closure`;
- dimensionless `Delta`;
- no internal reset;
- orientation quotienting;
- unique path and initial-condition identifiers;
- matching `M` calibration provenance;
- stride-2 and stride-3 segmentation error no greater than 1%.

The code rejects a tunable `C_RD`, duplicate branch paths, observed trajectories mislabeled as primitive, unresolved `M`, and segmentation-unstable paths.

## Executed three-branch fixture

The fixture uses the repository's existing Reader/Record stepper, 200 samples per branch, and three distinct initial-condition paths:

| branch | initial `(phi0,phi1,psi0,psi1)` |
|---|---|
| U | `(0.2, 0.201, -0.2, -0.201)` |
| D | `(0.5, 0.502, -0.5, -0.502)` |
| E | `(0.8, 0.801, -0.8, -0.801)` |

The merged operational calibration supplies:

```text
M_joint = 1.0004294772
known fixture M_true = 1
relative error = 0.04294772%
```

### Computed outputs

| branch | signed exchange | Delta | lambda |
|---|---:|---:|---:|
| U | `-0.0100828831516` | `0.0100828831516` | `0.989967778699` |
| D | `-0.0641481484558` | `0.0688325371555` | `0.933482990707` |
| E | `-0.582721722762` | `0.583214890131` | `0.558101245154` |

Therefore:

```text
Pi0 = 3*lambda_U + 3*lambda_D + lambda_E
    = 6.328453553372
```

The same paths evaluated with `M_true=1` give:

```text
Pi0_true = 6.328688910510
Pi0 relative error = 0.00371889%
```

### Error propagation

| output | relative error |
|---|---:|
| `M_joint` | `0.04294772%` |
| each signed exchange | `0.04294772%` |
| each `Delta_j` | `0.04294772%` |
| `lambda_U` | `0.00043285%` |
| `lambda_D` | `0.00295489%` |
| `lambda_E` | `0.02503386%` |
| `Pi0` | `0.00371889%` |

The branch lambdas and Pi0 are more accurate than the raw M percentage in this fixture because their weighted nonlinear combination partially suppresses the common small calibration shift.

## Parameter-count statement

Within this operational subchain:

1. `M`: free/borrowed numerical dial -> calibrated output;
2. `C_RD`: scale degeneracy -> fixed native-unit convention;
3. `lambda_U`: free branch weight -> computed output;
4. `lambda_D`: free branch weight -> computed output;
5. `lambda_E`: free branch weight -> computed output.

Thus:

```text
operational free-dial count: 5 -> 0
```

This is a genuine reduction of fitted/redundant parameters in the framework's finite-architecture computation. It is not yet a claim that five independent experimentally measured Standard-Model constants have disappeared; the physical U/D/E adapter remains a separate empirical identification problem.

## Files

- `primitive_branch_parameter_reduction_v0_1.py` — fail-closed contract and calculation engine;
- `primitive_branch_fixture_v0_1.py` — executable three-branch fixture and known-truth comparison;
- `primitive_branch_tape_schema_v0_1.json` — fixed-native-unit tape schema;
- `test_primitive_branch_parameter_reduction_v0_1.py` — regression and adversarial gates.

## Run

```bash
cd domains/standard_model/item1_exploration/primitive_branch_parameter_reduction
python3 primitive_branch_fixture_v0_1.py
python3 test_primitive_branch_parameter_reduction_v0_1.py
```

## Tier and boundary

- `declared_finite_architecture / calibrated_readout / finite_diagnostic`;
- candidate until independently reviewed;
- no auto-merge requested;
- no unrestricted-root derivation of physical U/D/E histories;
- no claim that `Pi0 > alpha` is already established;
- no physical mass or coupling prediction from this fixture alone.
