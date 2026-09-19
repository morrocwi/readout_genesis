---
name: git-essentials
description: Essential git workflow for readout_genesis — load before any commit, push, branch, or PR in this repo. Encodes attempt-file conventions for formal/, maker–checker separation in commits, claim-discipline (readout-not-truth) language for commit messages and PRs, and the standard branch/push/PR flow.
---

# Git essentials — readout_genesis

This repo's claim discipline is *readout-not-truth*: verified structure is not physical
truth. Git is where that discipline either holds or leaks — a commit message or PR body
that overstates a tier is a claim-discipline violation as real as one in a document.

## Formal files — attempt convention

- Coq work in `formal/` uses the `*_attempt.v` suffix (e.g.
  `InfoRetentionMetricSkewDecomposition_attempt.v`) — the same convention as the sibling
  solver repo. Keep the suffix until a file has actually passed verification; renaming
  (dropping `_attempt`) is a claim and belongs in its own commit with the verification
  evidence stated.
- Verifier scripts sit next to their targets (`formal/*_verify.py`); if a commit changes a
  formal file, run and cite its verifier in the same commit.

## Maker–checker in git terms

The repo's epistemic core separates maker from checker. Mirror that in commits: the change
(maker) and its gate/guard run (checker — the `scripts/*_check.py`, `*_guard.py`,
`*_gate.py` battery) are cited together, but a commit must never edit a guard **and** the
code it guards in a way that quietly weakens the guard. If a guard must change, say so
explicitly in the commit message and PR.

## Commit messages and PR bodies are claims

- Tag tiers honestly: `Th_coqc` for machine-checked structure, `finite_diagnostic` for an
  executed numeric run, `Dr` for narrative reading, `[Open]` for named unsolved items.
  The repo's own headline discipline ("M is posited, not derived"; "oscillation is NOT yet
  quantum") is the standard — never round a posited thing up to derived in a commit message.
- When touching a domain under `domains/`, check `domains/README.md` (the registry) and do
  not state a closure % other than the registry's strict/weighted numbers.
- The whitepaper (RG-UTW) is versioned **in its filename and internal `document.version`**;
  a content change to it must bump both, in the same commit, and update anything the canon
  defers to it for.

## Branch, push, PR mechanics

- Feature branch always; never push the default branch directly.
- `git fetch origin <branch>` for specific branches; `git push -u origin <branch>`; retry
  only network failures up to 4× with backoff (2s, 4s, 8s, 16s).
- After pushing, open a **draft PR** if none is open for the branch. PR body: what was run
  (scripts/gates and their exit status), tier of each claim, and any honest boundary the
  change touches.
- Never force-push a shared branch. If the branch's PR already merged, restart the branch
  from the latest default branch for follow-up work — never stack on merged history.
