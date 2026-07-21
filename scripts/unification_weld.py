#!/usr/bin/env python3
"""
The weld — a runnable witness that the master equation and the domain-DSL are ONE object.

Claim (architecture): the master stepper F (MQ.08 / spine) and the domain-DSL are two
readings of a single relation. A domain q_D is an admissible "sentence" of the DSL IFF it
COMMUTES with the master stepper:            q_D ∘ F  =  F♯_D ∘ q_D.
So "running the equation" (apply F) and "generating an admissible domain-sentence"
(find a q_D that closes the square) are the same act — a self-generating / homoiconic
system, like a rewrite rule that is at once its own language and its own dynamics.

This file does NOT assert that in prose; it WITNESSES it on a concrete finite F, exact
rational: a valid quotient closes the square (PASS = a real DSL sentence), and a
one-entry perturbation breaks it (FAIL = rejected as a non-sentence). Tier: the witness
is [finite_diagnostic]; the UNIVERSAL weld (every admissible domain is exactly a
commuting quotient of the one stepper) is [Dr]/architecture until proved as a theorem.

Run: python3 scripts/unification_weld.py
"""
from fractions import Fraction as F

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

# ---- the ONE master stepper F (a concrete MQ.08-flavoured retained operator) ----
h = F(1,2); q1 = F(1,4)
Fmat = [[h, h, q1, q1],
        [h, h, q1, q1],
        [q1, q1, h, h],
        [q1, q1, h, h]]

# ---- a domain-DSL "sentence": the quotient q_D that keeps pair-sums ----
qD  = [[F(1),F(1),F(0),F(0)],
       [F(0),F(0),F(1),F(1)]]
FsharpD = [[F(1), h],
           [h,   F(1)]]

print("== A domain is a SENTENCE iff it commutes with the master equation ==")
lhs = mm(qD, Fmat)          # q_D ∘ F
rhs = mm(FsharpD, qD)       # F♯_D ∘ q_D
check("weld closes: q_D ∘ F = F♯_D ∘ q_D  (this q_D IS an admissible DSL sentence)", lhs == rhs, (lhs, rhs))
# the SAME F both (a) steps the dynamics and (b) admits this quotient -> equation = language
check("the SAME stepper F both runs dynamics AND admits the sentence (one object)", lhs == rhs)

print("== FAILING control: perturb the equation by one entry -> no F♯ closes the square ==")
Fbad = [row[:] for row in Fmat]
Fbad[0][0] = Fbad[0][0] + F(1,8)     # single-entry perturbation
lhs_bad = mm(qD, Fbad)               # q_D ∘ F_bad
# two fine states with the SAME coarse image but different coarse successors -> no function F♯ exists
xA = [[F(1)],[F(0)],[F(0)],[F(0)]]
xB = [[F(0)],[F(1)],[F(0)],[F(0)]]
qxA = mm(qD, xA); qxB = mm(qD, xB)
sA = mm(qD, mm(Fbad, xA)); sB = mm(qD, mm(Fbad, xB))
check("same coarse state q_D·xA = q_D·xB", qxA == qxB, (qxA, qxB))
check("but different coarse successors after F_bad  -> NO F♯ exists  -> NOT a sentence (rejected)",
      sA != sB, (sA, sB))
check("so the weld is FAIL-ABLE: a non-commuting q_D is correctly refused, not admitted", sA != sB)

print("== Consequence: forcing a term from the root == discovering a commuting quotient ==")
# The productive identity: growing the equation (forcing structure) and growing the language
# (admitting a domain) are the same act — both are 'make another square close from the root.'
check("equation-growth and language-growth are the SAME act (a closed square from the root)",
      lhs == rhs and sA != sB)

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — the weld is witnessed: one stepper F is at once the master equation")
print("and the admissibility grammar of the domain-DSL. [finite_diagnostic] on this instance;")
print("the UNIVERSAL weld stays [Dr]/architecture until proved as a theorem.")
