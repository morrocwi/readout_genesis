<!-- Summary/synthesis document, tier Dr throughout (a narrative rollup of already-tiered results,
     not a new claim). Corrects an earlier, narrower framing from the same session (a "20%
     reduction" figure computed only over the 10-parameter quark-only subset, and a wrong claim
     that m_W=m_Z*cos(theta_W) represents NEW parameter savings beyond the standard SM count). -->

# Parameter economy — the honest, full-system count (2026-07-24)

## What this is

A single, accurate accounting of how many of the Standard Model's own ~19 free parameters this
session's work (items 1, 2, 12, 18, 21, 22, 24) actually reduces, replacing an earlier same-day
claim (`item24_exploration/cp_phase_jarlskog_v1.py` Part 4) that was correct on its own narrow
terms (quark sector only, 10-parameter subset) but got quoted informally in chat as if it applied
to the whole SM. It does not. This file gives the real, full-system number.

## The standard SM parameter count (19, canonical)

The Standard Model (excluding neutrino masses/PMNS, which need item 23, and excluding θ_QCD's own
open strong-CP-problem status) is conventionally counted as **19 independent free parameters**:
9 fermion masses, 3 gauge couplings, 4 CKM parameters (3 angles + 1 phase), 2 Higgs-sector
parameters (`v`, `λ`), 1 QCD θ-parameter.

## Corrected accounting, this session's actual work against each of the 19

| Category | SM count | This session | Genuinely saved? |
|---|---|---|---|
| 6 quark masses | 6 | 6, real PDG values, fed in (`item1_fit_calibrated_v1.py` / `fit_calibrated_registry.py`) | No — necessary input, not reducible by this session's work |
| 3 charged-lepton masses | 3 | 3, real PDG values, fed in (same registry) | No — necessary input |
| **3 CKM angles + 1 CP phase** | **4** | **2** (`D_up`, `phi` — `fritzsch_extended_texture_v1.py`, `cp_phase_jarlskog_v1.py`) | **YES — 2 of 4, `fit_calibrated` tier, via the Fritzsch texture-zero mechanism** |
| 3 gauge couplings (`g1,g2,g3`) | 3 | 3, untouched this session | No |
| Higgs sector (`v`, `λ`) | 2 | `v` fed in (already `fit_calibrated`, pre-existing); `λ` attempted (`item18_exploration/higgs_quartic_DOCUMENTED_NON_RESULT_v1.py`) and PROVEN fully circular — item 18 genuinely has **zero** tractable content, not a saving | No — 0 saved, and this is now a *proven*, not merely unattempted, non-result |
| θ_QCD | 1 | untouched | No |
| **Total** | **19** | **17 fed in + 2 reduced via mechanism** | **2 of 19 (~11%)**, not the 20% figure that circulated informally in this session's chat (that figure was computed only over the 10-parameter quark-only subset — `item24_exploration/cp_phase_jarlskog_v1.py` Part 4 — and is correct on ITS OWN narrower terms, but should never be quoted as a whole-SM figure) |

## The `m_W = m_Z·cos(θ_W)` correction (important, previously stated wrong in chat)

An earlier answer in this session's conversation (not committed to any file) claimed the
pre-existing, `Th_coqc`-tier result `m_W = m_Z·cos(θ_W)` (`ρ=1`, `order_higgs_closure_v1_12.py`,
`InfoOrderHiggsClosure.v`, `STANDARD_MODEL_CLOSURE.md` line 78) represented an ADDITIONAL
parameter saving beyond the standard 19-count. **This was checked and found wrong, corrected
here**: in the vanilla, unmodified Standard Model itself, `m_W` and `m_Z` are ALREADY both
computed from `g, g', v` via this exact tree-level relation (a standard consequence of the Higgs
being an `SU(2)` doublet) — the standard 19-parameter count never treats `m_W`/`m_Z` as
independent parameters to begin with, so there is no "extra" saving to claim here relative to
that count.

What `order_higgs_closure_v1_12.py` genuinely establishes, correctly stated: not a parameter
saving, but a **structural derivation of WHY** the vanilla SM's own assumed input (a single Higgs
doublet, hence custodial symmetry, hence `ρ=1`) holds — deriving the REPRESENTATION CHOICE
(`H=(1,2)_{1/2}`) from root order-carrier/stabilizer structure, rather than positing it as the
bare SM does. This is a genuine, `Th_coqc`-tier, pre-existing (not from this session) result about
explaining an SM INPUT, not a count reduction of the 19 free parameters themselves. Verified this
session: `order_higgs_closure_v1_12.py` line 76 uses `g,gp,v = Fr(3,2), Fr(1), Fr(2)` —
deliberately ARBITRARY symbolic values (explicitly commented "NOT predicted") — confirming
`m_W=m_Z cosθ` is proved as a structural IDENTITY (true for any `g,g',v`), not a numeric
coincidence, and not itself a reduction of the 19-count.

## Honest bottom line

- Real, `fit_calibrated`-tier saving this session actually earned: **2 of 19 parameters (~11%)**,
  specifically within the CKM/CP sector, via the Fritzsch texture-zero mechanism.
- Real, `Th_coqc`-tier structural explanation (pre-existing, not new this session, and NOT a
  parameter-count reduction): why the Higgs is a doublet (hence `ρ=1`).
- Real, disclosed non-result (also a form of honesty, not nothing): item 18 (Higgs quartic
  coupling) is PROVEN circular, zero tractable content until item 1 closes.
- Everything else (masses, gauge couplings, `v`, `θ_QCD`) remains necessary input, not reduced.
- This document supersedes the informal "20%" framing that circulated in chat this session for
  any whole-system claim; `cp_phase_jarlskog_v1.py`'s own 20% figure remains accurate for its own
  explicitly narrower scope (the 10-parameter quark-only subset) and does not need correction
  itself — only its generalization to "the SM" does.
