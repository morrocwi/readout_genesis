#!/usr/bin/env python3
"""
Item 2 -- Attempt 4 / Theta program step 5.4, 2026-08-09: building the admissibility
square between the two N >= 3 arrows -- result: HALF-CLOSES, with a proven obstruction
naming the exact missing ingredient.

THE TWO ARROWS (both machine-checked, independent premises):
  A_root: minimal-living N >= 3 (5.2b-2, InfoThetaMinimalLiving_attempt.v) -- a living
          reader/record/Theta loop needs >= 3 family slots.
  A_CP  : CP-conditional N >= 3 (Attempt 3, InfoCPEquivariantGenerationBound_attempt.v)
          -- retaining a CP-signed difference needs an N >= 3 mixing structure.
The CRRC question: are the two N's the same quantity? This file BUILDS the square
instead of asserting it.

SQUARE PART 1 -- same-object check: LEGITIMATE INTERSECTION (within the declared
  architecture). Both arrows constrain the dimension of the SAME declared family-slot
  space (the C^N working ansatz of Attempt 1, on which gauge acts trivially): the
  Theta-graph's vertices ARE the slot indices (5.1-5.2b setup), and the mixing
  matrix's indices ARE the slot indices (Attempt 3 setup). Two different QUESTIONS
  about one declared index set -- combining them as necessary conditions on one N is
  an intersection of constraints, NOT a readout contamination. Tier: exact within the
  declared architecture; the slot space itself remains the imported ansatz. The two
  supports are of UNEQUAL tier: the root arrow is unconditional within the declared
  architecture; the CP arrow is conditional on the empirical retained-CP premise (fed
  in, not derived — and per Part 3 not yet root-realizable). The double support is
  root-native + empirical-conditional, NOT two root-native proofs.

SQUARE PART 2 -- bridge candidate (DECLARED, Dr): in real physics the mixing matrix is
  the eigenbasis mismatch between two sectors' mass operators. The root-native analog:
  V := U_sectorA^T U_sectorB, the orthonormal-eigenbasis mismatch of two LIVING
  sector graphs' Laplacians (per-sector-distinct graphs are required anyway by the
  error-note shape constraint). Checked below on two living path-shape sectors
  (star-centered-0 vs path-centered-1, uniform weights for exactness): V is a genuine
  NONTRIVIAL real rotation (a 60-degree block!) -- real mixing ANGLES exist natively.

SQUARE PART 3 -- THE OBSTRUCTION (proven; Coq companion
  InfoThetaCPSquareObstruction_attempt.v): a REAL mixing matrix retains NO CP-signed
  readout: the Jarlskog-type quartet of real entries has imaginary part IDENTICALLY
  ZERO (trivial and load-bearing, like the neutral third value). The current Theta
  architecture -- real symmetric weighted-graph Laplacians with real orthonormal
  eigenbases -- therefore CANNOT satisfy arrow A_CP's premise. The square half-closes:
    - the two N's constrain the same declared slot count (Part 1) -- N >= 3 stands
      doubly supported;
    - but the root-native structure does NOT yet provide the CP-odd retained
      difference that A_CP's premise requires -- identifying the two N's as one
      DERIVED quantity remains open.

THE NAMED MISSING INGREDIENT (pointer, not built): an ORIENTED/complex edge structure.
  The corpus already carries exactly this shape: the G-adjoint split G = G^(+) + G^(-)
  (symmetric part = storage, SKEW part = oriented transfer, READOUT_GENESIS_CORE.md
  ~line 1259) and the antisymmetric pairing omega = [[0,1],[-1,0]] (line ~1323). A
  Theta program step that lets edges carry orientation (skew/phase) is the precise,
  root-available candidate for making J != 0 retainable -- NOT built here, named as
  the program's next step. (In real physics language: real orthogonal mixing has
  angles but no phase; the phase needs complex structure -- same statement.)

WHAT THIS DOES NOT ESTABLISH (binding): that the two N's are one derived quantity
  (open until the oriented extension exists and retains J != 0); any level<->
  generation identification (CRRC guard); that the eigenbasis-mismatch bridge is
  forced (it is a declared Dr candidate, natural but chosen).

Run: python3 theta_cp_square_v1.py   (exact Fractions + floats disclosed for
normalized eigenbases)
"""

import math
from fractions import Fraction as Fr

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


print("== 1. The obstruction, exact (unnormalized -- no floats needed) ==")
# Jarlskog-type quartet of ANY real matrix has Im == 0: verified exactly via the SAME
# Cq complex arithmetic as the Coq companion (corrected per review -- the earlier
# isinstance check could never fail and verified nothing).
import random


def cmul(x, y):  # (re, im) pairs of Fractions -- mirrors Coq Cmul
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cconj(x):
    return (x[0], -x[1])


random.seed(20260809)
ok = True
for _ in range(100):
    V = [[Fr(random.randint(-9, 9), random.randint(1, 7)) for _ in range(3)]
         for _ in range(3)]
    q = cmul(cmul((V[0][1], Fr(0)), (V[1][2], Fr(0))),
             cmul(cconj((V[0][2], Fr(0))), cconj((V[1][1], Fr(0)))))
    if q[1] != Fr(0):
        ok = False
ck("Cq quartet of real entries has Im == 0 EXACTLY, 100 matrices, quartetJ's own "
   "indices (general proof: Coq companion)", ok)

print("== 2. The bridge candidate on real living-sector data (floats disclosed) ==")


def normalize(v):
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v]


# two living path-shape sectors, uniform weight (5.2b-1's uniform orbit), different
# centers -- eigenvectors known exactly up to normalization:
U_A = [normalize(v) for v in [[1, 1, 1], [0, 1, -1], [2, -1, -1]]]   # star center 0
U_B = [normalize(v) for v in [[1, 1, 1], [1, 0, -1], [1, -2, 1]]]    # path center 1
V = [[sum(U_A[i][k] * U_B[j][k] for k in range(3)) for j in range(3)]
     for i in range(3)]
VtV = [[sum(V[k][i] * V[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
ck("mismatch V = U_A^T U_B is orthogonal (real unitary), 1e-12",
   all(abs(VtV[i][j] - (1 if i == j else 0)) < 1e-12
       for i in range(3) for j in range(3)))
ck("V is a NONTRIVIAL rotation (|V11| = 1/2 to 1e-12; reads 60 deg under the "
   "declared convention)", abs(abs(V[1][1]) - 0.5) < 1e-12, V[1][1])
qc = complex(V[0][1]) * complex(V[1][2]) * complex(V[0][2]).conjugate() \
    * complex(V[1][1]).conjugate()
ck("its quartet's imaginary part is EXACTLY 0.0 (real inputs; the obstruction, live)",
   qc.imag == 0.0, qc.imag)
print("""  Convention disclosed (per review): eigenvectors ordered by ascending eigenvalue
  (0 < w < 3w) with the listed sign representatives; V is defined only up to
  per-vector sign choices (eigenvalues simple) -- under a sign flip the block reads
  120 deg instead of 60 deg. Convention-INVARIANT content: |V11| = 1/2 and V is not a
  signed permutation (nontrivial mixing); nontriviality and the Part-3 obstruction
  are sign/order-independent.
  ==> real mixing ANGLES exist natively between living sectors, but the PHASE slot is
  structurally empty: J = Im(real) = 0 always.""")

print("""== 3. Verdict of the square ==
  PART 1 (legitimate intersection): both arrows constrain the same declared slot
    count -> N >= 3 stands with two supports OF UNEQUAL TIER (root-native
    unconditional + empirical-conditional; see docstring). Combining necessary
    conditions on one declared N is not CRRC.
  PART 3 (proven obstruction): the current real Theta architecture retains NO CP-odd
    difference -- A_CP's premise is not yet root-realizable. The two N's therefore
    CANNOT yet be identified as one derived quantity.
  NAMED NEXT STEP (root-available): oriented/skew edge structure (G^(-) split, omega
    pairing -- both already in the corpus) as the candidate carrier of a retainable
    J != 0. Not built here.""")

print()
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS")
