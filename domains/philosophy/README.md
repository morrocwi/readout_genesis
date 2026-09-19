# Information Philosophy / MEMK Domain v0.2.0

**Status:** `ARCHITECTURE_CONDITIONAL_UNRESOLVED_DOMAIN`  
**Repository role:** bounded Readout Genesis domain candidate  
**Root policy:** one root only — `delta_R -> L_R -> F`; philosophy/MEMK is a quotient/readout, never a new root.

This domain formalizes the connected readout cycle:

```text
retained distinction
  -> domain quotient
  -> event trace
  -> meaning
  -> experience
  -> memory
  -> belief
  -> externalized claim
  -> independently checked bounded knowledge status
  -> view / identity / conventional truth
  -> next meaning and action
```

The optional informational-LoRA lane adds a frozen base, low-rank meaning adapters, semantic potential, informational work, barrier crossing, unbinding/rebinding, reconsolidation, and consolidation tests.

## Current normative companion

`Information Epistemic Foundation v1.6.0` is registered as the current normative companion artifact through `FOUNDATION_RELEASE_REGISTRY_PHILOSOPHY_MEMK.yaml`. It adds the explicit belief layer, the normative knowledge-status proposal, conditioned agency, identity-binding and release, complete epistemic control gates, and Agency Meta-Readout Governance.

It is downstream of `PHILOSOPHY_MEMK_DOMAIN_v0_2_0.yaml`; it does not replace the root or promote the domain to empirical closure. The exact Markdown is stored losslessly under `artifacts/` and rebuilt with a deterministic verifier.

## Honest boundary

This release registers the **architecture and executable anti-drift bundle**. It does **not** establish:

- an exact empirical human-cognition or machine-cognition quotient;
- literal biological LoRA;
- informational work as physical energy;
- shock, conviction, authority, consensus, or subjective certainty as truth;
- spiritual experience as an independently validated metaphysical claim;
- universal transport outside declared domains and contexts;
- external independent review or held-out real-domain calibration.

## Run

From this folder:

```bash
python -B run_all_tests_philosophy_memk.py
```

Requirements: Python 3 standard library only. No network.

Expected result:

```text
PASS: PHILOSOPHY_MEMK_STRUCTURAL_REGISTRATION
DOMAIN_CLOSURE: UNRESOLVED
EMPIRICAL_CALIBRATION: UNRESOLVED
```

## Files

- `PHILOSOPHY_MEMK_DOMAIN_v0_2_0.yaml` — canonical registered domain specification.
- `FOUNDATION_RELEASE_REGISTRY_PHILOSOPHY_MEMK.yaml` — current and retained standalone foundation releases.
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.validation.yaml` — v1.6.0 canonicalization, identity, and validation receipt.
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.2.0.validation.yaml` — retained v1.2.0 receipt.
- `artifacts/` — lossless split archives and deterministic rebuild verifiers for standalone companions.
- `CLAIM_BOUNDARY_PHILOSOPHY_MEMK.json` — strongest permitted claim and explicit non-claims.
- `RULE_REGISTRY_PHILOSOPHY_MEMK.json` — active root, protocol, domain, and unresolved rules.
- `ROOT_DAG_MASTER_PHILOSOPHY_MEMK.md/.json` — one-root derivation and discovery DAG.
- `DRIFT_CONTRACT_PHILOSOPHY_MEMK.json` — fail-closed anti-contamination rules.
- `source_root/READOUT_GENESIS_CORE_SNAPSHOT.md` — immutable source lock and root excerpts.
- `philosophy_memk_closure_v0_2_0.py` — primary structural verifier.
- `checker_philosophy_memk.py` — independent reimplementation.
- `run_all_tests_philosophy_memk.py` — combined runner.
- `PROOF_RECEIPT_PHILOSOPHY_MEMK.json` — bounded receipt.
- `CLOSURE_AUDIT_PHILOSOPHY_MEMK.json` — closure matrix and open obstructions.
- `CHECKSUMS_SHA256_PHILOSOPHY_MEMK.txt` — immutable file hashes.

## Registration interpretation

`PASS` means the release bundle is internally consistent, rooted, recoverable, fail-able, lineage-preserving, and claim-bounded. It does not mean empirical philosophy, psychology, neuroscience, religion, or metaphysics has been closed.
