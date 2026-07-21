# Information Chemistry v0.901 — Standalone Root Proof Layer

## Run

```bash
python run_all_tests_v0_901.py
```

No network and no third-party Python package are required.

## Why this ZIP is standalone

The package includes:

- the root source snapshot used for interpretation;
- the v0.1 foundational anchor;
- the v0.900 peer-review charter;
- the full frozen root DAG and delta;
- every active rule and its claim restrictions;
- proof and drift code;
- an internal dual-implementation Checker;
- tests, source locks, manifests, and checksums.

## Permanent descendant rule

Every later version must include the whole DAG and all anti-drift control files again. Referencing an earlier release without embedding the required material fails the standalone gate.
