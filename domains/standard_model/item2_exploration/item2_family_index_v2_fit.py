#!/usr/bin/env python3
"""
Item 2 (generation multiplicity), Attempt 2 — fit_calibrated tier, per DRIFT_CONTRACT.json
DEV-SM-002 (founder-authorized 2026-07-24, same shape as DEV-SM-001 for item 1: fitting is
permitted, does not need to be a from-root derivation, tagged and caveated instead).

CONSTRUCTION (three explicit ingredients, none hidden):
  (1) BORROWED, exactly computed: a general N×N unitary quark-mixing matrix has N² real
      parameters; 2N−1 are removable by phase redefinition of the N up-type and N down-type
      fields modulo one overall common phase; the remaining (N−1)² physical parameters split
      into N(N−1)/2 real mixing angles and (N−1)(N−2)/2 CP-violating complex phases
      (Cabibbo 1963; Kobayashi–Maskawa 1973 — registered in docs/root/EQUATION_REGISTRY.md).
      This is exact integer combinatorics, verified over the integers below for N=0..6 — not a
      fit itself, a theorem, cited not re-derived.
  (2) EXTERNALLY OBSERVED (declared input, not derived from anything in this repo): CP
      violation is a real, measured phenomenon (most recently CMS's B⁰ₛ→J/ψK⁰ measurement,
      2026-07-24, matching the Standard Model — see HANDOFF_NEXT_SESSION.md §0.-1 item 2 note).
      Feeding this in as a fact-to-match, not deriving it, is the FIT part of fit_calibrated —
      same declared-input methodology as item 1's Attempt 5 (fit_calibrated_registry.py).
  (3) THIS FRAMEWORK'S OWN STYLE, explicitly flagged as a POSTULATE not a forcing argument:
      select the smallest N consistent with (1)+(2) — i.e. the smallest N whose phase count is
      ≥1. This is stylistically the same MOVE as SM_INFORMATION_PHILOSOPHY_MASTER.md's §2.2
      ("k>1 minimal ⇒ k=3") and §3.1 ("dim<3 makes the closure form identically zero ⇒ dim=3
      minimal admissible"), but is NOT the same STRENGTH of argument — see HONEST FENCE below,
      this is the exact distinction DRIFT_CONTRACT.json DEV-SM-002 names as the risk to not
      smuggle past a reader.

Run: python3 item2_family_index_v2_fit.py
"""

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 1. unitary N×N mixing-matrix parameter counting (Cabibbo 1963 / Kobayashi-Maskawa 1973, exact) ==")
def counts(N):
    total = N*N
    removable = 2*N - 1 if N >= 1 else 0
    physical = total - removable if N >= 1 else 0
    angles = N*(N-1)//2
    phases = physical - angles
    return total, removable, physical, angles, phases

for N in range(0, 7):
    total, removable, physical, angles, phases = counts(N)
    if N >= 1:
        ck(f"N={N}: total={total}, removable={removable}, physical=(N-1)^2={ (N-1)**2 }",
           physical == (N-1)**2 and total - removable == physical)
        ck(f"N={N}: angles=N(N-1)/2={N*(N-1)//2}, phases=(N-1)(N-2)/2={ (N-1)*(N-2)//2 }",
           angles == N*(N-1)//2 and phases == (N-1)*(N-2)//2)
    ck(f"N={N}: CP-phase count = {phases}", True)  # report, not a pass/fail condition itself

print("== 2. minimal N with a nonzero physical CP phase (exact, over the integers) ==")
# N=0 is a boundary case (no mixing matrix exists at all -- 0 flavors, nothing to mix or
# violate CP with); the raw formula (N-1)(N-2)/2 is only valid for N>=1 and must be gated
# explicitly here (an earlier draft left it ungated, giving a spurious phase_counts[0]=1 that
# disagreed with counts(0)'s correctly-gated phases=0 -- caught by independent adversarial
# review before commit; fixed by gating both the same way).
phase_counts = {0: 0} | {N: (N-1)*(N-2)//2 for N in range(1, 7)}
for N in range(0, 7):
    print(f"   N={N}: phase_count = {phase_counts[N]}" + ("  (boundary: no matrix exists)" if N == 0 else ""))
ck("N=1: phase_count = 0 (KM mechanism structurally impossible)", phase_counts[1] == 0)
ck("N=2: phase_count = 0 (Cabibbo's own 2-generation case: real, no CP phase)", phase_counts[2] == 0)
ck("N=3: phase_count = 1 (first N with a nonzero physical phase)", phase_counts[3] == 1)
N_min = min(N for N in range(1, 7) if phase_counts[N] >= 1)
ck("min{N : phase_count(N) >= 1} = 3", N_min == 3, N_min)

print("== 3. fit_calibrated combination (declared, not derived) ==")
print("   Input (2), externally observed: CP violation of this type is real (CMS 2026-07-24).")
print("   Input (1), borrowed theorem: phase_count(N)=0 for N<3, >=1 for N>=3 (exact, verified).")
print("   Selection (3), this framework's minimality STYLE, explicitly a POSTULATE here (see")
print("   honest fence): N := min{N : phase_count(N) >= 1} = 3.")
print(f"   RESULT: N_generations (fit_calibrated) = {N_min}")
print("   Matches the real, observed Standard Model generation count (3). CONSISTENT-WITH,")
print("   not FORCED-BY -- see honest fence, this is not a claim of derivation.")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier fit_calibrated, per DRIFT_CONTRACT.json DEV-SM-002 — read that entry's
"risk" field before citing this result anywhere):
- Ingredient (1) is exact, borrowed, cited-not-derived combinatorics (Cabibbo/Kobayashi-Maskawa,
  registered in docs/root/EQUATION_REGISTRY.md). Not in question here.
- Ingredient (2) is an EXTERNAL OBSERVATION fed in as a fact-to-match, exactly like item 1's
  Attempt 5 fit_calibrated_registry.py (fit_calibrated_ew_masses_v1.py etc.) — declared FIT
  input, not derived from anything in this repo.
- Ingredient (3), the minimality SELECTION, is the part most likely to be mis-cited later, so it
  is stated as plainly as possible: THIS IS A POSTULATE, NOT A FORCING ARGUMENT. In
  SM_INFORMATION_PHILOSOPHY_MASTER.md §2.2/§3.1, "minimal" means smaller values are
  MATHEMATICALLY IMPOSSIBLE (a closed cyclic tape below length 3 cannot exist at all under
  those axioms; an alternating trilinear form on dim<3 is identically zero, so no closure
  object exists at all). HERE, N=1 or N=2 generations are NOT mathematically impossible or
  even inconsistent with anything else already closed in this domain (item2_family_index_v1.py,
  Attempt 1: gauge-anomaly-freedom holds for every N≥0) — they are merely inconsistent with
  the OBSERVED fact of CP violation, which is ingredient (2), a fed-in fact, not a theorem of
  this framework. Calling this "the same minimality argument as §2.2/§3.1" would itself be a
  Cross-Role Readout Contamination applied to the WORD "minimal" rather than to a specific
  formula (the exact failure mode DEV-SM-002 was written to flag in advance) — DO NOT make
  that equivalence in any downstream citation of this file.
- What this attempt DOES establish, honestly: a genuinely minimal-free-parameter, entirely
  root-tool-independent construction (uses no continuous fitted constant at all — only an
  integer selection rule over exact integer counts) that lands on N=3, tagged fit_calibrated,
  consistent with observation.
- What it does NOT establish: any derivation, forcing, or from-root necessity of N=3; any
  claim that N=4,5,... are excluded by anything but the fed-in CP-violation observation; any
  claim about WHY nature would select the minimal N rather than some larger one (that "nature
  prefers minimal N" is itself an unproven, underived meta-postulate, stated as such, not
  smuggled in as if it were a theorem).
- CRITERION-SELECTION HINDSIGHT (flagged after independent adversarial review, 2026-07-24):
  the parameter-counting family in ingredient (1) produces SEVERAL countable quantities at
  once -- angles=N(N-1)/2, physical=(N-1)^2, phases=(N-1)(N-2)/2. This attempt selects "phase
  count >= 1" as the ONE that matters, not because it is the only countable quantity available,
  but because it is the CP-relevant one -- and that relevance judgment is only obvious given
  that CP violation (not, say, "at least one mixing angle") is the fact being matched. A
  different, equally legitimate-looking choice ("angles >= 1") would select N=2, not N=3. This
  is disclosed, not hidden: the criterion was picked to match the specific observation in
  ingredient (2), which is exactly what a DECLARED fit is allowed to do (per DEV-SM-002) -- but
  it means this construction should never be described as "the only natural choice" or as
  ruling out N=2 on its own terms; it rules out N=2 only RELATIVE TO the CP-violation fact
  chosen as the target.
""")
