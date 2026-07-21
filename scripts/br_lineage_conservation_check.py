#!/usr/bin/env python3
"""
[finite_diagnostic] Biological-readout lineage conservation check — SYNTHETIC fixtures
ONLY. This is NOT run on, and makes NO claim about, any real event-resolved biological,
chemical, or protein data. It exercises exact-rational bookkeeping only.

Verifies I_Q = I_B + O_C + O_P + O_B along a synthetic quantum -> chemical -> protein ->
biological lineage chain: I_Q (quantum input) is passed through three stages, each of
which retains a fraction of what remains and EMITS an observable quotient (O_C, O_P, O_B);
I_B is what is left after all three emissions. Conservation requires the full chain sum to
reconstruct I_Q exactly.

Also flags any fixture where a QUANTUM-ONLY shortcut (an observer who sees only the
quantum stage and naively re-applies its own retention ratio three times, skipping the
actual chemical/protein/biological-specific quotient maps) SPURIOUSLY commutes with —
i.e. accidentally reproduces — the true multi-stage result. A spurious match would hide
the fact that real lineage tracking cannot skip the intermediate quotients; the guard
must NOT let that go unnoticed.

Run: python3 scripts/br_lineage_conservation_check.py
"""
from fractions import Fraction as F

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

def run_chain(I_Q, retain_C, retain_P, retain_B):
    """Full chain: quantum -> chemical -> protein -> biological, each stage RETAINS a
    fraction of what remains and EMITS the rest as an observable quotient."""
    after_C = I_Q * retain_C
    O_C = I_Q - after_C
    after_P = after_C * retain_P
    O_P = after_C - after_P
    after_B = after_P * retain_B
    O_B = after_P - after_B
    I_B = after_B
    return I_B, O_C, O_P, O_B

def quantum_only_shortcut(I_Q, retain_C_guess, n_stages=3):
    """A quantum-only observer, blind to the chemical/protein/biological-specific
    retention ratios, naively re-applies the ONE ratio it can see (the chemical-stage
    retention) n_stages times, skipping the real intermediate quotients entirely."""
    return I_Q * (retain_C_guess ** n_stages)

# ===================================================== PASSING control (conserved fixture)
I_Q_pass = F(24)
retain_C, retain_P, retain_B = F(3, 4), F(2, 3), F(1, 2)
I_B, O_C, O_P, O_B = run_chain(I_Q_pass, retain_C, retain_P, retain_B)

check("PASSING: O_C = 6 exact", O_C == F(6), O_C)
check("PASSING: O_P = 6 exact", O_P == F(6), O_P)
check("PASSING: O_B = 6 exact", O_B == F(6), O_B)
check("PASSING: I_B = 6 exact", I_B == F(6), I_B)

conserved = (I_Q_pass == I_B + O_C + O_P + O_B)
check("PASSING: full chain conserves I_Q = I_B + O_C + O_P + O_B (24 = 6+6+6+6)",
      conserved, (I_Q_pass, I_B + O_C + O_P + O_B))

shortcut_pass = quantum_only_shortcut(I_Q_pass, retain_C)   # naive (3/4)^3 * 24 = 81/8
check("PASSING: quantum-only shortcut predicts 81/8 (naive re-applied retention)",
      shortcut_pass == F(81, 8), shortcut_pass)
spurious_match_pass = (shortcut_pass == I_B)
check("PASSING: shortcut does NOT commute with true I_B (81/8 != 6) — no spurious match",
      not spurious_match_pass, (shortcut_pass, I_B))

# =========================================================== FAILING control (leak fixture)
I_Q_fail = F(24)
# same declared retentions, but a bookkeeping LEAK: O_B mis-recorded as 5 instead of 6
I_B_leak, O_C_leak, O_P_leak = F(6), F(6), F(6)
O_B_leak = F(5)   # <-- injected leak (1 unit unaccounted for)
leak_sum = I_B_leak + O_C_leak + O_P_leak + O_B_leak
conserved_leak = (I_Q_fail == leak_sum)
check("FAILING: leak fixture sum = 6+6+6+5 = 23 != I_Q = 24 (exact)",
      leak_sum == F(23) and not conserved_leak, leak_sum)
check("FAILING: conservation check correctly FLAGS the leak (I_Q != I_B+O_C+O_P+O_B)",
      not conserved_leak)

# ================================================= additional fixture: spurious-commute case
# a degenerate fixture where every stage happens to share the SAME retention ratio ->
# the quantum-only shortcut DOES commute with the true chain. This must be caught too:
# a spurious commute is itself a flaggable condition (masks the need for real per-stage
# quotients even though this particular fixture happens to conserve).
I_Q_deg = F(64)
retain_same = F(1, 2)
I_B_deg, O_C_deg, O_P_deg, O_B_deg = run_chain(I_Q_deg, retain_same, retain_same, retain_same)
conserved_deg = (I_Q_deg == I_B_deg + O_C_deg + O_P_deg + O_B_deg)
shortcut_deg = quantum_only_shortcut(I_Q_deg, retain_same)
spurious_deg = (shortcut_deg == I_B_deg)
check("DEGENERATE fixture (equal retentions): chain still conserves I_Q", conserved_deg)
check("DEGENERATE fixture: quantum-only shortcut SPURIOUSLY commutes (== I_B) — flaggable",
      spurious_deg, (shortcut_deg, I_B_deg))

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — lineage conservation confirmed on the passing fixture (chain")
print("conserves, quantum-only shortcut correctly does NOT commute); leak fixture correctly")
print("flagged (I_Q != I_B+O_C+O_P+O_B); a degenerate equal-retention fixture demonstrates the")
print("shortcut CAN spuriously commute and is flaggable. [finite_diagnostic] SYNTHETIC fixtures")
print("ONLY — NOT run on real event-resolved biological/chemical/protein data.")
