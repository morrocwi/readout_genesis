<!-- The standard every domain leaf must meet to register into READOUT GENESIS. -->

# Domain Registration Standard — READOUT GENESIS

> **A domain is a translation, not a new root.** Registering a domain never adds an axiom to the
> master equation; it declares a *quotient* `q_D` of the one retained structure and proves — at an
> explicit, bounded tier — how much of that domain's structure the quotient exactly carries. The
> master file (`../READOUT_GENESIS_CORE.md`) stays the single root; a domain folder is a **readout**
> of it. Reference implementation: [`chem/`](chem/) (Information Chemistry v0.910).

This standard exists so that no domain can silently contaminate the master-equation lineage (the
founder rule: *if it does not connect to the master-equation stream, it does not enter the root*). It
turns that rule from prose into a **checkable release contract**.

---

## What a registered domain `<D>` MUST contain

A domain folder `domains/<D>/` is registrable only when it ships all of the following, and its own
checker returns `PASS`:

1. **`CLAIM_BOUNDARY_<D>.json`** — the tier and the two honest lists:
   - `tier` — the strongest thing the release is allowed to claim (e.g. `FORMAL_COMPOSITION_QUOTIENT_ONLY`).
   - `established[]` — what is proved, at that tier.
   - `not_established[]` — what is explicitly NOT claimed (the domain's real semantics, named laws,
     empirical generalization). This list is mandatory and adversarially audited.
   - `public_label` — the one-line label the release may present under (e.g.
     `[FiniteFormalWitnesses] root-native abstract composition layer`).

2. **`RULE_REGISTRY_<D>.json`** — every active rule, each carrying:
   - `rule_id`, `class` ∈ { `ROOT_THEOREM`, `PROTOCOL`, `EMPIRICAL_TAPE`, `DISCOVERED_DOMAIN_LAW`,
     `CALIBRATED_READOUT`, `NUMERICAL_PROCEDURE`, `UNRESOLVED`, `OBSTRUCTED` },
   - `assumptions[]`, `parents[]` (its edges in the DAG), `statement`,
   - **`forbidden_claims[]`** — what this specific rule does NOT license. Mandatory per rule.

3. **`ROOT_DAG_MASTER_<D>.md`** (+ `.json`) — a single acyclic graph, **rooted at `R0` = the master
   retained distinction `δ_R`**, that shows both directions the master core defines:
   - the **derivation** chain (`R0 → typed state/boundary → quotient sufficiency → ledger/…`), and
   - the **discovery** chain (`T0 empirical tape → D0 candidate-law discovery` under a frozen grammar
     `P0` and tie/complexity protocol `P1` → `D1 holdout/intervention/transport` → `O0 calibrated
     readout` + `N0 certified numerical` → `C0 bounded claim`).
   The DAG must be standalone (contain its own nodes, not a pointer) and every edge must be justified
   by a rule in the registry.

4. **`DRIFT_CONTRACT_<D>.json`** — the executable no-contamination contract. Its `hard_fail_conditions`
   MUST include at least:
   - any `ROOT_THEOREM` depends on an `EMPIRICAL_TAPE` / `DISCOVERED_DOMAIN_LAW` / `CALIBRATED_READOUT`
     / `NUMERICAL_PROCEDURE` node (tier purity — theorems never borrow empirical support),
   - **No-Free-`<D>`-Law**: the domain's source structure inferred *for free* from the carrier (e.g.
     source commutativity read off `ℕ^G`'s commutativity) — forbidden,
   - any **named domain law or named domain object activated** (a `prohibited_active_domain_tokens`
     list, e.g. for chemistry: `mass_action`, `henderson_hasselbalch`, `nernst_equation`, …),
   - a DAG cycle, a missing anchor / source snapshot / test / checksum,
   - a claim **stronger than the declared `tier`**.

5. **`source_root/READOUT_GENESIS_CORE_SNAPSHOT.md`** — an immutable snapshot of the master equation
   the domain is a readout of. This is the anchor that makes "domain = translation of the one root"
   auditable, not asserted.

6. **Verification bundle** — a proof kernel + unit tests + a **dual-implementation checker**
   (`checker_<D>.py`, an independent re-implementation of the proofs, not the same code) + a
   `PROOF_RECEIPT_<D>.json` + `CHECKSUMS_SHA256_<D>.txt` + immutable version **anchors** of every
   prior release embedded byte-complete. `run_all_tests_<D>.py` must return `PASS`.

7. **The encoding obstruction, stated honestly.** Every domain release must name what it does NOT yet
   have: the **calibrated encoding** from retained states to the domain's registry/observables that
   would license real-domain semantics. Until that encoding is supplied and independently checked, the
   release stays at its formal tier — never promoted to a claim about the real domain.

---

## The registration protocol (`R0 → registered`)

```
R0  Declare the quotient q_D and the tier ceiling in CLAIM_BOUNDARY.       (never a new axiom)
R1  Freeze the generator/profile registry and the discovery grammar        (PROTOCOL, before evidence)
      — no aliasing, identity-locked coordinates.
R2  Prove the structural layer over ℚ as FINITE_FORMAL_WITNESSES           (ROOT_THEOREMs)
      — each theorem lists its forbidden_claims.
R3  Run the DRIFT_CONTRACT audit + dual-implementation checker.            (must PASS, fail-closed)
R4  Adversarial peer review (imported-law · free-structure · alias ·        (PASS + open-obstruction
      refinement · lineage · claim audit).                                  stated)
R5  Register: add a row to domains/README.md and a linked DAG node in       (the master points back)
      READOUT_GENESIS_CORE.md that points to domains/<D>/.
```

A domain that fails any gate is recorded as `OBSTRUCTED` or `UNRESOLVED` with the exact failing gate —
it is **not** force-registered. "No evidence yet" (`⊥`) is a valid, recorded state, never a guess.

---

## How the master file references a registered domain

The master equation file carries, per registered domain, a short **domain section** that:
- shows the domain's DAG (or its head) as a leaf hanging off the spine's `domain = translation` node,
- states the domain's `tier` and its `not_established` list in one line,
- **points to `domains/<D>/`** for the full release — knowledge lives in the folder; the core keeps
  only the connective node and the honest tier.

This keeps the master file the single root and the domain folders the readouts, with one auditable
edge between them in each direction (core → folder pointer; folder → core `source_root` snapshot).
