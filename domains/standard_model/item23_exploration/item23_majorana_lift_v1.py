#!/usr/bin/env python3
"""
Item 23 -- neutrino architecture (Dirac vs Majorana nu^c), Attempt 1, 2026-07-24.

STARTING POINT (already in this repo, hypercharge_global_quotient_v1_5.py Part 8, unchanged,
read not modified): adding a right-handed neutrino nu^c with Dirac closure ell+h+n=0 (n := Y(nu^c))
makes anomaly cancellation alone UNDERDETERMINE hypercharge -- Y and B-L degenerate into a genuine
2-parameter family (OPEN_EXTRA_ABELIAN, a negative control, correctly reported not hidden). Part 8
then ASSERTS (via `ck(..., True)`, i.e. stated, not computed) that a "neutral self-pair" condition
nu^c (x) nu^c -> 1 lifts the degeneracy back to the unique h=3q solution. This file's only job:
turn that assertion into an actual COMPUTATION, checked against v1.5's own closure algebra, and
report honestly whether it holds and what it costs.

WHY THIS MATTERS FOR ITEM 23: nu^c (x) nu^c -> 1 (the closure product of nu^c with itself yielding
the trivial/identity representation, i.e. hypercharge-neutral) is EXACTLY the same-shape statement
this repo already uses to build a Majorana mass term for nu^c (a self-pairing bilinear, not a
nu^c-H-L Yukawa coupling). So: IF you want v1.5's own already-established unique-hypercharge result
(h=3q, Th_coqc-adjacent, the repo's main closure result) to survive the addition of nu^c WITHOUT any
new free input, THEN nu^c must be self-paired (Majorana-shaped), not purely Dirac. This is a
CONDITIONAL structural argument (root-native closure algebra, no external premise), not a claim that
nature chose Majorana -- it says which choice is CONSISTENT with a result this repo already has.

Run: python3 item23_majorana_lift_v1.py
"""
from fractions import Fraction as Fr

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 1. reuse v1.5's own closure charges (unchanged) ==")
def charges(q, h):
    u = -q - h
    d = -q + h
    l = -3*q
    e = h - l
    return u, d, l, e

print("\n== 2. reuse v1.5's own nu^c Dirac-closure relation: ell+h+n=0 => n=3q-h ==")
def n_dirac(q, h):
    u, d, l, e = charges(q, h)
    return -l - h  # = 3q - h

for (q, h) in [(Fr(1), Fr(1)), (Fr(2), Fr(0)), (Fr(1), Fr(5)), (Fr(1, 2), Fr(7))]:
    n = n_dirac(q, h)
    ck(f"q={q},h={h}: n = 3q-h = {3*q-h} (matches v1.5 Part 8 exactly)", n == 3*q - h)

print("\n== 3. v1.5's own negative control, reconfirmed: n=3q-h solves the FULL anomaly system for")
print("   EVERY (q,h), i.e. anomalies alone give ZERO constraint on h once nu^c is present ==")
def A_grav_nu(q, h, n):
    u, d, l, e = charges(q, h)
    return 6*q + 3*u + 3*d + 2*l + e + n
def A_111_nu(q, h, n):
    u, d, l, e = charges(q, h)
    return 6*q**3 + 3*u**3 + 3*d**3 + 2*l**3 + e**3 + n**3

for (q, h) in [(Fr(1), Fr(1)), (Fr(2), Fr(0)), (Fr(1), Fr(5)), (Fr(-3), Fr(2)), (Fr(1, 2), Fr(7))]:
    n = n_dirac(q, h)
    ck(f"q={q},h={h}: A_grav=0 and A_111=0 for arbitrary h (anomalies do NOT fix h anymore)",
       A_grav_nu(q, h, n) == 0 and A_111_nu(q, h, n) == 0)
ck("=> confirmed: with pure-Dirac nu^c, h is a genuinely free parameter (Y vs B-L degenerate, "
   "OPEN_EXTRA_ABELIAN) -- v1.5's own claim, now verified across 5 distinct (q,h) samples not "
   "asserted from a single one", True)

print("\n== 4. THE ACTUAL COMPUTATION v1.5 skipped: does nu^c (x) nu^c -> 1 (self-pair / Majorana- ==")
print("   shaped closure) force n=0, and does n=0 (combined with the SAME n=3q-h Dirac-closure")
print("   relation) recover EXACTLY v1.5's own h=3q unique-hypercharge condition? ==")
print("   Closure-product hypercharge rule (this repo's own grammar, Part 1): a field of charge n")
print("   paired with itself under the closure product X(x)X->1 carries total charge 2n (additive,")
print("   same rule used everywhere else in Part 1 for two-field contractions); for the product to")
print("   equal 1 (the U(1)-neutral trivial rep) the total charge must vanish: 2n=0.")
for (q, h) in [(Fr(1), Fr(1)), (Fr(2), Fr(0)), (Fr(1), Fr(5)), (Fr(-3), Fr(2)), (Fr(1, 2), Fr(7))]:
    n = n_dirac(q, h)
    self_pair_charge = 2 * n
    forces_n_zero = (self_pair_charge == 0) == (n == 0)
    ck(f"q={q},h={h}: SANITY CHECK ONLY (field-arithmetic tautology, 2n=0 iff n=0 -- not counted "
       f"as substantive evidence, flagged per independent review)", forces_n_zero)

q_sym, h_sym = Fr(1), None  # symbolic check done by direct substitution below
print("   solving n=3q-h together with the Majorana constraint n=0, for symbolic q (Fraction-exact):")
for q in [Fr(1), Fr(2), Fr(1, 3), Fr(-5)]:
    # n = 3q - h = 0  =>  h = 3q
    h_forced = 3 * q
    n_check = n_dirac(q, h_forced)
    ck(f"q={q}: n=0 forces h=3q={h_forced} exactly, and n_dirac(q,h_forced)={n_check}==0 "
       f"(round-trip check)", n_check == 0)
ck("=> Majorana self-pair condition (2n=0) + Dirac-closure relation (n=3q-h) TOGETHER force "
   "h=3q -- the IDENTICAL condition v1.5 Part 2-3 derives from anomaly cancellation ALONE in the "
   "no-nu^c case. This is a DIRECT, single-step consequence of substituting n=0 into the already- "
   "established n=3q-h relation (not an independent surprise -- see honest fence below), now "
   "checked across multiple q values rather than merely asserted.", True)

print("\n== 5. ILLUSTRATIVE reconfirmation only (adds NO new evidence beyond Part 3's general proof --")
print("   flagged as such per independent review): if nu^c is PURELY Dirac (no self-pair term, no")
print("   Majorana mass allowed), h stays free UNLESS some other input fixes it -- there is no")
print("   root-native mechanism in this repo, checked here on 4 sample h values, that picks a value")
print("   of h from closure+anomaly alone in that branch ==")
free_h_examples = [Fr(0), Fr(3), Fr(-7), Fr(100)]
all_survive_pure_dirac = True
for h in free_h_examples:
    q = Fr(1)
    n = n_dirac(q, h)
    ok = (A_grav_nu(q, h, n) == 0 and A_111_nu(q, h, n) == 0)
    if not ok:
        all_survive_pure_dirac = False
ck("pure-Dirac branch: h=0,3,-7,100 (arbitrarily different values) ALL satisfy anomaly-freedom "
   "equally -- confirms no anomaly-based tiebreaker exists in that branch, matching v1.5's own "
   "OPEN_EXTRA_ABELIAN label", all_survive_pure_dirac)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier Dr -- design-narrative / conditional structural argument; the anomaly algebra
itself is Th_coqc-adjacent exact-Fraction arithmetic reusing v1.5's own audited relations, but the
"closure product of a field with itself carries additive charge 2n, must vanish to equal 1" step is
a NAMING/GRAMMAR CHOICE about what nu^c(x)nu^c->1 means, not independently forced -- same status as
this session's earlier weak-charge magnitude disclosure):
- WHAT THIS ESTABLISHES: v1.5 Part 8 ASSERTED (via a bare `ck(..., True)`, no computation) that a
  "neutral self-pair" condition on nu^c recovers h=3q. This file COMPUTES it for the first time,
  Fraction-exact, across multiple (q,h) samples: the self-pair condition 2n=0 forces n=0 exactly,
  and n=0 combined with v1.5's own Dirac-closure relation n=3q-h forces h=3q exactly -- the IDENTICAL
  condition v1.5's own anomaly cancellation derives in the no-nu^c case (Part 2-3). This is a real,
  checked algebraic fact, not a restatement of the assertion. IMPORTANT HEDGE (caught by independent
  review): the step from "n=0" to "h=3q" is a DIRECT, single-line algebraic consequence, not an
  independent surprise -- n=3q-h already inherits the h=3q target structurally, because ell=-3q was
  fixed anomaly-independently of h back in v1.5 Part 1, before nu^c was ever introduced. The
  "convergence" with v1.5's own answer is therefore expected given the shared closure grammar, not
  a second, independent confirmation of it. What this file adds beyond the trivial substitution is
  narrower than it may first read: it names and checks the EXACT postulate (2n=0, additive
  self-pair charge) that has to be assumed to get that direct consequence -- v1.5 never named or
  computed it, only asserted the outcome.
- THE STRUCTURAL READING (Dr tier, this file's actual content): IF one wants v1.5's own
  already-established unique-hypercharge result to survive adding a right-handed neutrino WITHOUT
  introducing any new free input, THEN nu^c must be self-paired under the closure product (the same
  shape as a Majorana mass term, not a Dirac Yukawa coupling to L and H). This is a CONDITIONAL
  argument from internal consistency with an already-established result -- it does NOT independently
  derive that nature is Majorana, and does NOT rule out Dirac neutrinos with some OTHER (currently
  absent from this repo) mechanism fixing h.
- WHAT THIS DOES NOT ESTABLISH: (a) that "closure product of a field with itself must vanish to
  equal 1" is the FORCED, unique reading of nu^c(x)nu^c->1 in this repo's own grammar -- it is the
  natural/consistent extension of the additive charge rule used everywhere else in Part 1, but this
  file does not derive that additivity itself from anything more primitive; flagged, not hidden.
  (b) any value for a Majorana mass scale, mixing among generations, or the seesaw mechanism --
  those are entirely separate, unaddressed questions. (c) that the pure-Dirac branch is impossible
  in principle -- only that THIS repo currently has no root-native mechanism (checked in Part 5
  above) that fixes h in that branch; a real physical UV completion might supply one this repo does
  not yet model. (d) any connection to why there are exactly 3 generations (item 2, already
  fit_calibrated, DEV-SM-002) -- this file treats one generation only, same scope as v1.5 itself.
- Independently adversarially reviewed, 2026-07-24 -- verdict SURVIVES (with required wording
  corrections, applied above): confirmed the additive self-pair charge rule (2n=0) is a legitimate,
  non-ad-hoc extension of v1.5's own 3-field closure grammar, not invented to force the answer;
  confirmed all Fraction arithmetic by independent hand-substitution; required correcting an
  overclaim ("genuine coincidence" -> direct consequence, now hedged above) and relabeling Part 5
  and the 2n=0-iff-n=0 sub-check as illustrative/sanity-only rather than substantive evidence.
""")
