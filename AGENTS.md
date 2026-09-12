# Mandatory AI Startup Protocol — Readout Genesis / Clay Program

`readout_genesis` is an interpretation/application map in the cross-repository Clay program. Treat it as architectural context, not as independent proof evidence.

## Read first for Clay-related work

1. `morrocwi/readout-problem-navier-stokes/CLAY_READ_FIRST.md`
2. `morrocwi/readout-problem-navier-stokes/CLAY_RESEARCH_TODO.md`
3. `morrocwi/readout-problem-navier-stokes/CLAY_MULTI_PROBLEM_FINITE_BRIDGE_PROGRAM.md`
4. `morrocwi/information-discrete-math/docs/UNIVERSAL_FINITE_OBSTRUCTION_UNIFORM_BRIDGE_KERNEL.md`
5. `morrocwi/toledo/docs/CLAY_BRIDGE_PROGRAM_2026-09-11.md`
6. `morrocwi/toledo/EQUATION_SOURCE_POLICY.md`, especially the central `TG-RFG-01` reuse-first gate.

## Central cross-repository derivation gate

Readout Genesis MUST participate in, but MUST NOT replace, the canonical Toledo provenance gate:

```text
Toledo lookup
    -> Genesis compatibility
    -> reuse existing object
    -> derive only the missing piece
    -> mark PROPOSAL
```

For mathematical work, Toledo lookup comes first because `morrocwi/toledo` is the authority for existing equation/theorem provenance and status. Genesis compatibility comes second and governs ontology, retention, sufficiency, quotient, translation, lineage and defect interpretation.

Rules:

- if Toledo already contains a usable object, reuse its code/status rather than inventing a Genesis-local equivalent;
- if an ontological/translation reading conflicts with Genesis, return `HOLD` or state a proposed Genesis revision explicitly;
- if Toledo has no matching object, derive only the smallest missing piece after the compatibility check and label it `PROPOSAL`;
- a Genesis sketch, analogy, domain interpretation, or architectural lemma MUST NOT be retroactively presented as an existing Toledo theorem;
- bypassing the order above is `DRIFT`, not evidence.

Passing this gate controls provenance only. It does not prove a domain theorem or close any Clay obligation.

## Role boundary

Use this repository to:

- map interpretations/applications;
- explain how readout ideas instantiate across domains;
- identify candidate adapters and conceptual transfers;
- point to the actual theorem/certificate source.

Do **not** use this repository alone to claim:

- Navier--Stokes regularity;
- `P != NP`;
- Yang--Mills existence/mass gap;
- RH, BSD, or Hodge;
- any theorem whose proof/certificate actually lives elsewhere.

For every strong statement, cite the upstream proof/certificate repo and its evidence tier.

## Anti-drift rule

A cross-domain analogy is not a theorem. Record a failed or unsupported analogy honestly and return to the shared core rather than inventing a bridge.

Core rule:

> **Genesis interprets; IDM proves generic finite kernels; domain repos instantiate; Toledo records status/provenance.**
