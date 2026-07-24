<!-- Curated, tier-honest subset of an externally-produced research bundle. This folder is NOT a
     registered domain under domains/DOMAIN_REGISTRATION_STANDARD.md (the source material itself
     states it has not closed the required root-forcing gate — see "not_established" below), and
     nothing here is added to READOUT_GENESIS_CORE.md's "THE FORCED SET" necessity-tier box. It is
     recorded here as a tier-honest external contribution, per the same convention used for
     domains/standard_model/mu4_exploration/. -->

# External research — π/φ retained-history fusion + Page-curve toy experiments (2026-07-24)

## Provenance

The user supplied three files on 2026-07-24:
- `READOUT_GENESIS_PI_PHI_STANDALONE_v3.pdf` + `READOUT_GENESIS_PI_PHI_STANDALONE_v3_BUNDLE.zip`
  (a self-contained release bundle produced in an earlier session, referencing this repo's own
  `SM_INFORMATION_PHILOSOPHY_MASTER.md`/`READOUT_GENESIS_STANDARD_MODEL_CANONICAL.md`-style content
  as its "canonical anchor" — i.e. it is downstream of this repo, not an independent source).
- `ROOT_NATIVE_PAGE_CURVE_COMPLETE_EXPERIMENT_PACKAGE_v1.0.0(1).zip` (a companion Kaggle-run
  experiment package covering the same retained-transfer / Page-curve / φ-schedule program).

Full original bundles (including PDFs, PNGs, `.ipynb` notebooks, and two legacy source zips —
several MB total) are **not duplicated into git**; they remain in `~/Downloads/` on this
workstation. This folder holds only the small text/code/data artifacts needed to independently
check every numerical claim referenced below.

## What this actually is

A finite-qubit simulation research program (not hardware, not a gravity derivation) that:
1. Proves a rank-two fusion-category closure (`τ⊗τ≅1⊕τ ⇒ FPdim(τ)=φ`) **conditional on seven
   declared gates H1–H7** (finite-dimensionality, splitting idempotents, simple unit, finitely many
   simples, duals+snake identities, faithful positive pairings) — a real, checkable algebraic
   result, but explicitly *not* a proof that the unrestricted root forces H1–H7 in any natural
   system.
2. Runs finite-qubit retained-transfer / Page-curve toy simulations, with a signed-readout
   discipline (negative values are retained as signed information, never silently clipped into a
   fake positive "entropy" — this is the same `readout-not-truth` discipline this repo already
   enforces elsewhere).
3. Tests a candidate golden-ratio (`φ`) measurement schedule under **two different protocols with
   opposite results**: the reduced 8-seed multiseed protocol shows φ beating random 8/8 seeds
   (mean RMSE reduction ≈31%); the independent simple paired-Pauli protocol shows φ *losing* to
   random by ≈30%. The bundle's own `CLAIM_BOUNDARY.yaml` correctly refuses to generalize from
   either result alone and states this as an open, protocol-dependent question — not a resolved
   claim in either direction.
4. Documents 11 concrete errors found and fixed in earlier drafts of this same program (see
   `ROOT_NATIVE_PAGE_CURVE_FINDINGS_LIMITS_ERRORS_v1.0.0.yaml`, `errors_found`), including a
   **retracted** earlier claim of a physical Rényi-2 entropy improvement (the underlying
   cross-purity values were outside the physical `[1/d,1]` interval and had been silently clipped
   before taking a log — exactly the kind of non-readout injection this repo's own discipline
   exists to catch).

## Independent verification performed here (not just trusting the bundle's own audit)

The bundle ships its own `audit/run_all_checks.py` and reports `overall_status: PASS`
(`CHECK_REPORT_original.json` in this folder is that original report, kept for comparison).
It was **independently re-run from scratch** in this environment on 2026-07-24 and reproduced the
same three script results and the same overall `PASS`:
- `verify_retained_history_phi.py` → spectral radius of the fusion matrix `[[0,1],[1,1]]` = φ =
  1.618033988749895 exactly, fusion-identity residual = 0.0.
- `analyze_multiseed.py` → recomputed from the raw CSV: golden beats random 8/8 seeds, mean RMSE
  golden=0.5247 vs random=0.7614 vs cyclic=0.8554.
- `analyze_counterexample.py` → recomputed from the raw log: golden loses to random by ≈30.2% in
  this protocol; `COUNTEREXAMPLE_PROTOCOL_GOLDEN_LOSES`.
- Manifest checksums: no mismatches.

This confirms the *arithmetic* in the bundle is honest and reproducible from its own raw data. It
does **not** independently re-verify the underlying quantum-circuit simulations themselves (that
would require re-running the original Kaggle notebooks, which are not fully recoverable — see
`SOURCE_LEDGER.md`'s "Important source limitation").

## Tier assignment (per this repo's own discipline)

| Result | Tier | Notes |
|---|---|---|
| `FPdim(τ)=φ` from rank-two fusion closure | `finite_diagnostic` (conditional, not `Th_coqc` — no `.v` witness exists for this; it is a cited external classification result, Ostrik's rank-two fusion category theorem, applied under H1–H7) | Closed *only* under declared gates; root-forcing of H1–H7 is explicitly `not_established`. |
| Golden-angle algebra `θ_G=2π/φ²` | `Dr` (algebraic identity, not a physical claim) | |
| Retained-transfer finite-qubit architecture (signed readout / positive Gram certificate `K_ret=M†GM` / physical-translation gate) | `finite_diagnostic` | Real, checkable simulation architecture; matches this repo's own signed-readout discipline. |
| φ-schedule reduces spectral-purity RMSE (v5.3 protocol) | `finite_diagnostic`, protocol-specific | Contradicted by the simple-protocol result below — do not generalize. |
| φ-schedule loses to random (simple protocol) | `finite_diagnostic`, protocol-specific | The negative control. Both numbers are kept; neither is allowed to stand alone. |
| Physical Page curve / black-hole unitarity / quantum advantage | **`[Open]` — explicitly `NOT_DERIVED` / `NOT_DEMONSTRATED`** | Named in the source's own `prohibited_claims` list. Do not cite this folder as evidence for any of these. |

## Explicit non-goals (do not use this folder to claim)

Copied directly from the source material's own `prohibited_claims` (both bundles independently
declare the same list) — this program does **not** claim to have solved the black-hole information
paradox, derived the gravitational Page curve from first principles, proven black-hole unitarity,
proven quantum gravity, demonstrated quantum computational advantage, shown φ-scheduling wins
"generally," or shown that any natural system is forced to select `φ`.

## Where this is referenced from

- `ROOT_INFO_LANGUAGE_INVENTORY.md` — new **Group D** entry.
- `READOUT_GENESIS_CORE.md` §V.15 (*Open and Untested Bridges — Recorded as TBD, Never Fabricated*)
  — one new bullet, pointing here. Nothing was added to §"THE FORCED SET" (the necessity-tier box).

## Files in this folder

- `CLAIM_BOUNDARY.yaml`, `SOURCE_LEDGER.md` — the source bundle's own honest-fence documents, kept
  verbatim.
- `CHECK_REPORT_original.json` — the source bundle's own audit report, kept verbatim for
  comparison against the independent re-run described above.
- `B0_RETAINED_HISTORY_FUSION_CLOSURE.md`, `retained_history_fusion_claim_boundary.json` — the H1–H7
  fusion-closure record.
- `verify_retained_history_phi.py`, `deterministic_metrics.csv` — the φ/fusion-matrix verifier.
- `analyze_multiseed.py`, `phi_schedule_v5_3_multiseed.csv`,
  `phi_schedule_pagecurve_v5_3_multiseed_report.json` — the positive-protocol recomputation.
- `analyze_counterexample.py`, `KAGGLE_SIMPLE_PHI_PAGECURVE.py`,
  `KAGGLE_SIMPLE_PHI_PAGECURVE_TEST.log`, `simple_phi_pagecurve_summary.csv` — the negative-control
  (counterexample) protocol, full runnable source included.
- `signed_retained_page_curve_v4_1_report_excerpt.json` — the signed-readout truth-audit excerpt.
- `ROOT_NATIVE_PAGE_CURVE_FINDINGS_LIMITS_ERRORS_v1.0.0.yaml` — the full consolidated findings /
  errors / prohibited-claims / next-experiments audit from the companion Kaggle package (in Thai;
  this is the single most complete tier-discipline document in the whole contribution and is worth
  reading in full before citing anything else here).
