#!/usr/bin/env python3
"""
Item 1 -- fit_calibrated extension, 2026-07-24: generation-resolved lambda_{j,gen} grid.
Pi0 itself is LEFT UNTOUCHED (still item1_fit_calibrated_v1.py's own branch-level ~6.9888).

*** TAG: fit_calibrated. NOT derived from the root. FITTED, not derived; consistent-with, not
    forced-by (DEV-SM-001, same caveat as item1_fit_calibrated_v1.py, every occurrence). ***

Founder direction (2026-07-24, chat): "ต้นทุนเท่าไหร่ใช้วิธีการฟิตเอาเลย" (for the cost values,
just go ahead and fit them) -- do not attempt another from-root derivation of Delta_j/alpha/kappa_j
(4 independent attempts already failed this session, item1_exploration/ITEM1_EXPLORATION_LOG.md
Attempts 1-4). Instead extend the existing PASSED fit (Attempt 5,
item1_fit_calibrated_v1.py, Pi0=3*lambda_U+3*lambda_D+lambda_E~=6.9888).

WHAT THIS DOES: item1_fit_calibrated_v1.py collapses each branch's 3 real PDG masses into ONE
branch-level number via a geometric mean BEFORE applying lambda_j := exp(-m_j/v_EW) -- its own
honest fence already names the resulting gap: "lambda_j is a single BRANCH-level number ... not
generation-resolved." This file applies the SAME ALREADY-DECLARED fit_calibrated formula,
UNMODIFIED, to the 9 individual PDG masses instead of their 3 branch-level geometric means --
i.e. it stops averaging before applying the transform. ZERO new free parameters: no new constant,
no new functional form, no new external input -- same v_EW=246 GeV, same exp(-m/v_EW) form, same
9 PDG masses already in fit_calibrated_registry.py.

(2026-07-24: this construction went through independent adversarial review before being written
up this way -- verdict SURVIVES_WITH_CORRECTION. Two corrections applied to this docstring/code
vs. the first draft: (1) an earlier claim that this construction and item 2's N=3 fit
(item2_family_index_v2_fit.py) "draw on the identical external fact" was WRONG and has been
struck -- item 2's N=3 never touches the PDG mass table at all, it comes purely from unitary-
matrix phase-count combinatorics + the externally-observed CP-violation fact; the two are
independent constructions with DIFFERENT inputs that happen to numerically coincide on "3" (one
via mass-table row count, one via CP-violation-forced minimality) -- NOT a shared input echoed
twice, and neither should ever be cited as confirming the other. (2) an earlier draft called this
"the same READOUT operation" -- "readout" is this domain's loaded technical term for a root-
native operator r=O(X) (tape order, cyclic closure, Aut(F,O), retained metric, holonomy); exp(-m/
v_EW) is an admittedly non-root, fit_calibrated heuristic and was never such an operator, which is
exactly why it carries the fit_calibrated tag instead of Th_coqc/Dr. Corrected to plain language:
"the same already-declared fit_calibrated formula, applied to different already-available raw
inputs" -- no CRRC-style admissibility claim is made or needed.)

Run: python3 item1_generation_resolved_lambda_v1.py
"""
import math

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory, DEV-SM-001) ==")
print("  fit_calibrated -- FITTED, not derived from the root; consistent-with, not forced-by.")

print("\n== 1. same PDG masses item1_fit_calibrated_v1.py already reads, unaveraged ==")
PDG_MASSES_GEV = {
    "u": 0.00216, "c": 1.27, "t": 172.5,
    "d": 0.00467, "s": 0.0934, "b": 4.18,
    "e": 0.000511, "mu": 0.1057, "tau": 1.777,
}
v_EW = 246.0
BRANCHES = {"U": ("u", "c", "t"), "D": ("d", "s", "b"), "E": ("e", "mu", "tau")}

grid = {j: [math.exp(-PDG_MASSES_GEV[gen] / v_EW) for gen in gens] for j, gens in BRANCHES.items()}
for j, vals in grid.items():
    print(f"   lambda_{{{j},gen}} = {['%.8f' % v for v in vals]}")
    ck(f"branch {j}: monotone decreasing across generations (matches real mass ordering m1<m2<m3)",
       vals[0] > vals[1] > vals[2])

print("\n== 2. branch-level lambda_j (item1_fit_calibrated_v1.py's own value, UNCHANGED) ==")
def geomean(vals): return math.exp(sum(math.log(v) for v in vals) / len(vals))
lam_branch = {j: geomean([PDG_MASSES_GEV[g] for g in gens]) for j, gens in BRANCHES.items()}
lam_branch = {j: math.exp(-m / v_EW) for j, m in lam_branch.items()}
for j, v in lam_branch.items():
    print(f"   lambda_{j} (branch, geomean) = {v:.8f}")
Pi0 = 3 * lam_branch["U"] + 3 * lam_branch["D"] + lam_branch["E"]
ck("Pi0 (branch-level, UNCHANGED from item1_fit_calibrated_v1.py) ~= 6.98883632",
   abs(Pi0 - 6.98883632) < 1e-6, Pi0)

print("\n== 3. illustrative-only check: naive per-generation SUM is NOT proposed as a Pi0-analog ==")
naive_sum_Pi0 = 3 * sum(grid["U"]) + 3 * sum(grid["D"]) + sum(grid["E"])
print(f"   naive sum-of-9 analog = {naive_sum_Pi0:.8f} (>7, breaks v1.13's own Pi0<=7 no-go ceiling)")
ck("naive sum breaks the Pi0<=7 no-go ceiling -- confirms recombination needs its own",
   naive_sum_Pi0 > 7, naive_sum_Pi0)
print("   (no recombination rule is proposed here -- any such rule is an undeclared NEW free")
print("   parameter; this is reported only to show why none is smuggled in.)")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier fit_calibrated, per DRIFT_CONTRACT.json DEV-SM-001):
- WHAT THIS ESTABLISHES: a genuinely zero-new-free-parameter extension of item1_fit_calibrated_v1.py
  -- same functional form, same v_EW, same PDG masses already in the shared registry, applied
  unaveraged instead of pre-averaged. Restores per-generation information the branch-level
  geometric mean was discarding.
- WHAT THIS DOES NOT ESTABLISH: (a) any explanation of WHY fermion masses differ across
  generations -- the mass-hierarchy problem stays [Open] at Th_coqc/Dr tier; the grid only
  re-expresses already-known PDG masses through an already-declared fit transform, it derives or
  predicts nothing. (b) any new Pi0 value -- Pi0 remains item1_fit_calibrated_v1.py's own
  branch-level ~6.9888, untouched; no recombination of the 9-value grid into one number is
  proposed. (c) any relationship to item 2's N=3 fit (item2_family_index_v2_fit.py) -- these are
  two INDEPENDENT constructions with DIFFERENT external inputs (a mass-table row count vs. a
  CP-violation-forced minimality selection) that happen to numerically coincide at 3; citing one
  as confirming the other would be a fresh instance of Cross-Role Readout Contamination.
- Does not weaken DRIFT_CONTRACT.json hard_fail_conditions[12] (Pi0>alpha root-derivation ban);
  nothing here claims Pi0>alpha is forced or proven.
""")
