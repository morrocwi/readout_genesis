#!/usr/bin/env python3
"""
Item 2 -- Attempt 3, 2026-08-08: CP-equivariant readout lower bound N >= 3,
as a LOCALLY-PROVEN conditional mechanism (not a borrowed count, not a fit).

WHAT THIS UPGRADES vs Attempt 2 (`item2_family_index_v2_fit.py`, DEV-SM-002):
  Attempt 2 borrowed the Cabibbo/Kobayashi-Maskawa phase-count theorem, fed in the observed
  CP violation, and POSTULATED minimality to select N=3. Its own honest fence disclosed a
  criterion-selection-hindsight caveat: "phase count >= 1" vs "angle count >= 1" both look
  legitimate, and only the target observation picks between them.
  This attempt closes part of that gap, in three ways, none of which feeds the number 3:
    (i)  The load-bearing vanishing theorem (N=2 unitarity ==> Jarlskog-type quartet
         invariant J == 0 identically) is PROVEN HERE, in-house, by a 3-step algebraic
         argument verified both symbolically-by-substitution and on exact Q(i) unitary
         families -- not cited from Kobayashi-Maskawa.
    (ii) The criterion itself ("why the CP-relevant count and not the angle count") is
         SELECTED BY STRUCTURE, not hindsight: the retained matter/antimatter difference is
         a SIGNED readout equivariant under a CP involution (J -> -J under elementwise
         conjugation, proven exactly below). Mixing-angle magnitudes are CP-EVEN (invariant
         under the same involution, checked exactly below) -- they cannot carry a signed
         equivariant readout at all, so they were never a candidate criterion for a
         CP-difference readout. This is the IDM equivariant-readout lens
         (information-discrete-math `formal/IDM_ReadoutMinimality.v` /
         `IDM_EquivariantReadout.v` -- proof PATTERN transferred, admissibility square
         REBUILT here for THIS group/object pair, per IDM_CROSS_POLLINATION_TODO.md #2/#10;
         the k_color=3 cyclic-closure argument is NOT used anywhere in this file).
    (iii) Everything numeric is exact Gaussian-rational Q(i) arithmetic (Fraction pairs):
         no floats, no trig, no continuum angles -- rotations come from Pythagorean triples,
         the CP phase from the unit-modulus Gaussian rational (3+4i)/5. IDM-clean: the
         contaminated-concept table's "angle" row is respected (overlap fractions /
         rational unit-circle points only).

THE CONDITIONAL RESULT (stated with its premise, never without):
  PREMISE (empirical, fed in, same status as Attempt 2's ingredient 2): the world retains a
    matter/antimatter difference of the CKM kind -- i.e. the CP-signed readout is
    NON-DEGENERATE (some configuration is read differently from its CP image).
  MECHANISM (proven here, exact):
    - For N=2, unitarity forces J == 0 on EVERY configuration: the signed readout is
      structurally DEGENERATE -- no 2-generation mixing structure can retain a CP-signed
      difference of this kind. (Section 2 below: algebraic proof + exact family check.)
    - For N=3, a single exact Q(i) witness shows J != 0 is retained. (Section 3.)
  CONCLUSION (conditional, forced): premise + mechanism ==> N >= 3. The lower bound is
    FORCED by the vanishing theorem GIVEN the premise; it is not a fit and contains no tuned knob
    (readout_universe B1 degrees-of-freedom criterion: the mechanism REDUCES freedom --
    an identical vanishing at N<=2 -- rather than reparametrizing a continuous knob).

NOVELTY CALIBRATION (explicit, per this domain's own Attempt-1 review precedent): the
  physics content here -- 2 generations admit no CKM-type CP violation, hence observed CP
  violation implies >= 3 -- is KNOWN TEXTBOOK PHYSICS (Kobayashi-Maskawa 1973). It is NOT a
  discovery of this file. The contribution is ONLY: the in-house exact/machine-checked
  re-derivation on this framework's own terms (no borrowed theorem in the load-bearing
  step), and the criterion-structure analysis in (ii) above.

WHAT THIS DOES NOT ESTABLISH (unchanged from Attempt 2, stated up front):
  - N == 3 exactly. Nothing here excludes N=4,5,... The step from ">=3" to "=3" remains
    either Attempt 2's declared minimality POSTULATE (DEV-SM-002) or an external empirical
    cap (e.g. Z-width light-neutrino counting), both openly non-derivations.
  - That the premise (retained CP difference) is itself root-derived. It is an observed
    fact about the world, fed in and labeled as such.
  - Why a mixing matrix / N-fold family replication exists at all (items 21-23; the C^N
    family slot remains the imported working ansatz Attempt 1's review flagged).
  - CRRC guard (Q3, identity-by-role): n_gen (this file) and k_color (SM master 2.2) are
    DIFFERENT quantities with different roles; their shared digit is not an identification.

Tier: mechanism = exact/in-house-proven (Coq witness attempted separately);
      conclusion = CONDITIONAL on the declared empirical premise; overall item 2 stays
      [Open] at the unconditional-derivation level.

Run: python3 item2_cp_equivariant_lower_bound_v3.py   (stdlib only; exact arithmetic)
"""

from fractions import Fraction as Fr

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------------------
# Exact Gaussian-rational complex numbers: z = re + im*i, re/im in Q (Fraction).
# ---------------------------------------------------------------------------
class QC:
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        return QC(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return QC(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return QC(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def __neg__(self):
        return QC(-self.re, -self.im)

    def conj(self):
        return QC(self.re, -self.im)

    def __eq__(self, o):
        return self.re == o.re and self.im == o.im

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else ''}{self.im}i)"


ZERO, ONE = QC(0), QC(1)


def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), ZERO) for j in range(p)]
            for i in range(n)]


def dagger(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def is_identity(A):
    return all(A[i][j] == (ONE if i == j else ZERO)
               for i in range(len(A)) for j in range(len(A)))


def is_unitary(A):
    return is_identity(mat_mul(dagger(A), A))


def conj_mat(A):
    return [[z.conj() for z in row] for row in A]


def jarlskog_quartet(V, a, b, i, j):
    """Im( V[a][i] * V[b][j] * conj(V[a][j]) * conj(V[b][i]) ) -- exact Fraction."""
    z = V[a][i] * V[b][j] * V[a][j].conj() * V[b][i].conj()
    return z.im


print("== 1. The readout and its involution: definitions, from scratch ==")
print("""  Object space X_N : N x N unitary matrices over Q(i) (mixing configurations).
  Involution  op    : elementwise complex conjugation V |-> conj(V)  (the CP action on the
                      mixing matrix; op(op V) = V trivially).
  Readout     r     : the quartet-sign readout FAMILY (one per N): sign of a quartet
                      invariant J(V) := Im(V_ai V_bj conj(V_aj) conj(V_bi)) into {+, -, 0}.
                      For N=3 we use indices (a,b;i,j)=(0,1;1,2); for N=2 the UNIQUE quartet
                      is (0,1;0,1) (Section 2). Per-N, r is total: the quartet that exists is
                      always exactly computable (IDM S4 minus bottom; bottom unused).
  This admissibility square is BUILT HERE for THIS pair (op, r); nothing is inherited from
  the cyclic-tape color argument (different group: Z2 vs cyclic; different object: unitary
  configurations vs tape channels; different readout: sign-of-J vs tape witness sign).""")

# --- involution property + equivariance J(conj V) = -J(V), proven pointwise-exact below
#     and algebraically: Im(conj(z)) = -Im(z) for every z, and the quartet of conj(V) is
#     the conjugate of the quartet of V.

print("== 2. N=2: unitarity forces J == 0 identically (the vanishing theorem, in-house) ==")
print("""  Algebraic proof (3 steps, no citation needed):
    (a) COLUMN orthogonality of a 2x2 unitary (the Hermitian inner product of columns
        (V00,V10) and (V01,V11)): V00*conj(V01) + V10*conj(V11) = 0
        ==> V00*conj(V01) = -V10*conj(V11).
    (b) Quartet: V00*V11*conj(V01)*conj(V10) = V11*conj(V10) * (V00*conj(V01))
                = V11*conj(V10) * (-V10*conj(V11)) = -(V10*conj(V10)) * (V11*conj(V11))
                = -|V10|^2 * |V11|^2   (a product of two z*conj(z) factors).
    (c) z*conj(z) is real for every z, so the quartet is real ==> Im = 0.  QED.
  The same argument with rows covers every index choice; below we CHECK it exactly on a
  3-parameter family of exact Q(i) unitaries (all three slots swept).""")


def u2(a, b, eta):
    """General-form 2x2 unitary [[a, b], [-conj(b)*eta, conj(a)*eta]], needs |a|^2+|b|^2=1,
    |eta|=1."""
    return [[a, b], [-(b.conj()) * eta, a.conj() * eta]]


# unit-modulus Gaussian rationals (Pythagorean): (3+4i)/5, (5+12i)/13, (8+15i)/17, 1, i, -1
UNITS = [QC(1), QC(0, 1), QC(-1), QC(Fr(3, 5), Fr(4, 5)), QC(Fr(5, 13), Fr(12, 13)),
         QC(Fr(8, 17), Fr(-15, 17))]
# (|a|,|b|) Pythagorean pairs with |a|^2+|b|^2=1
AB_PAIRS = [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(8, 17), Fr(15, 17))]

n2_checked = 0
all_zero = True
all_unitary = True
for (ma, mb) in AB_PAIRS:
    for ua in UNITS:
        for ub in UNITS:
            for eta in UNITS:
                a = QC(ma) * ua
                b = QC(mb) * ub
                U = u2(a, b, eta)
                if not is_unitary(U):
                    all_unitary = False
                # the only quartet for N=2: a=0,b=1,i=0,j=1
                z = U[0][0] * U[1][1] * U[0][1].conj() * U[1][0].conj()
                if z.im != 0:
                    all_zero = False
                n2_checked += 1
ck(f"all {n2_checked} exact Q(i) 2x2 family members are exactly unitary", all_unitary)
ck(f"J == 0 EXACTLY on all {n2_checked} of them (vanishing theorem instance check)", all_zero)
print("""  NOTE (honest scope): the family check is an exact INSTANCE sweep; the identity
  itself is the 3-step algebra above, and its machine-checked form is the separate Coq
  witness (formal/InfoCPEquivariantGenerationBound_attempt.v) -- the general statement is
  proven there for ARBITRARY entries satisfying the orthogonality relation, not only for
  this sweep.""")

print("== 3. N=3: one exact Q(i) witness retains J != 0 (lower bound achieved) ==")
c12, s12 = QC(Fr(3, 5)), QC(Fr(4, 5))       # Pythagorean 3-4-5
c23, s23 = QC(Fr(5, 13)), QC(Fr(12, 13))    # 5-12-13
c13, s13 = QC(Fr(8, 17)), QC(Fr(15, 17))    # 8-15-17
d = QC(Fr(3, 5), Fr(4, 5))                  # unit-modulus Gaussian rational "phase"

R12 = [[c12, s12, ZERO], [-s12, c12, ZERO], [ZERO, ZERO, ONE]]
R23 = [[ONE, ZERO, ZERO], [ZERO, c23, s23], [ZERO, -s23, c23]]
R13d = [[c13, ZERO, s13 * d.conj()], [ZERO, ONE, ZERO], [-s13 * d, ZERO, c13]]

V3 = mat_mul(R23, mat_mul(R13d, R12))
ck("witness V3 is EXACTLY unitary over Q(i)", is_unitary(V3))

J3 = jarlskog_quartet(V3, 0, 1, 1, 2)
print(f"  J(V3) = {J3}  (exact Fraction)")
ck("J(V3) != 0 exactly", J3 != 0, J3)

# closed-form cross-check: J = c12 s12 c23 s23 c13^2 s13 * Im(d)  (standard parametrization
# identity, recomputed here exactly rather than cited)
J_closed = (Fr(3, 5) * Fr(4, 5) * Fr(5, 13) * Fr(12, 13)
            * Fr(8, 17) ** 2 * Fr(15, 17) * Fr(4, 5))
ck("exact closed-form cross-check J = c12 s12 c23 s23 c13^2 s13 Im(d)", J3 == J_closed,
   (J3, J_closed))

print("== 4. CP equivariance and CP-evenness: the criterion is selected by structure ==")
V3cp = conj_mat(V3)
ck("CP involution: conj(conj(V3)) == V3", conj_mat(V3cp) == V3)
ck("CP is unitarity-preserving: conj(V3) is exactly unitary", is_unitary(V3cp))
J3cp = jarlskog_quartet(V3cp, 0, 1, 1, 2)
ck("signed readout is CP-EQUIVARIANT: J(conj V3) == -J(V3) exactly", J3cp == -J3,
   (J3cp, J3))
# angle-magnitude data |V_ij|^2 (the 'angle count' criterion's raw material) is CP-EVEN:
mag_even = all((V3[i][j] * V3[i][j].conj()) == (V3cp[i][j] * V3cp[i][j].conj())
               for i in range(3) for j in range(3))
ck("|V_ij|^2 is CP-EVEN (identical for V3 and conj V3), all 9 entries exact", mag_even)
print("""  ==> a CP-difference readout must be built from CP-ODD data. |V_ij|^2 (hence any
  mixing-ANGLE count) is CP-even: it cannot distinguish V from conj(V) even in principle.
  The 'phase/J' criterion is therefore not a hindsight pick among equals -- it is the only
  one of the two that can carry a signed CP-equivariant readout at all. (This addresses,
  without fully dissolving, Attempt 2's disclosed criterion-selection caveat: 'angles>=1'
  was never a candidate criterion FOR A CP-DIFFERENCE readout. What remains genuinely
  chosen is the premise that the CP difference is the retained difference in question.)""")

print("== 5. IDM necessary-condition checks NC1-NC3, run concretely (not cited) ==")
# NC1: a symmetry fixing an object fixes its readout. CP fixes every REAL orthogonal V
#      (conj V == V); its readout must then be a neg-fixed value (neutral).
V_real = mat_mul(R23, mat_mul(
    [[c13, ZERO, s13], [ZERO, ONE, ZERO], [-s13, ZERO, c13]], R12))  # d := 1 (real)
ck("V_real is exactly unitary (indeed real orthogonal over Q)", is_unitary(V_real))
ck("CP fixes V_real: conj(V_real) == V_real", conj_mat(V_real) == V_real)
J_real = jarlskog_quartet(V_real, 0, 1, 1, 2)
ck("NC1 instance: CP-fixed object has neg-fixed readout: J(V_real) == 0 exactly",
   J_real == 0, J_real)
# NC3: an object moved to a distinctly-read image cannot be read as a neg-fixed value.
ck("NC3 instance: V3 is read differently from conj(V3) (sign +/-), so r(V3) is NOT "
   "neg-fixed (nonzero)", J3 != 0 and J3cp == -J3 and J3 != J3cp)
# The three readout values {+, -, 0} are ALL REALIZED -- the 3-value minimality pattern's
# conclusion, instantiated concretely on THIS space (own square, not IDM_Harvest's k=3):
ck("three pairwise-distinct readout values realized: r(V3)=+, r(conj V3)=-, r(V_real)=0",
   J3 > 0 and J3cp < 0 and J_real == 0)

print("== 5b. Readout is well-defined on PHYSICAL states (rephasing invariance) ==")
# Master 1.2: physical state = equivalence class under unreadable renamings. For mixing,
# the renamings are diagonal rephasings V -> P1 V P2 (P1,P2 diagonal unit-modulus). The
# readout must be constant on each class -- checked exactly on the witness:
P1 = [[UNITS[3], ZERO, ZERO], [ZERO, UNITS[4], ZERO], [ZERO, ZERO, UNITS[1]]]
P2 = [[UNITS[5], ZERO, ZERO], [ZERO, UNITS[2], ZERO], [ZERO, ZERO, UNITS[3]]]
V3r = mat_mul(P1, mat_mul(V3, P2))
ck("rephased witness still exactly unitary", is_unitary(V3r))
ck("J is rephasing-INVARIANT exactly: J(P1 V3 P2) == J(V3)",
   jarlskog_quartet(V3r, 0, 1, 1, 2) == J3,
   jarlskog_quartet(V3r, 0, 1, 1, 2))
print("""  ==> r reads the equivalence CLASS, not a basis choice -- the readout is a
  physical readout in this framework's own 1.2 sense, not a coordinate artifact
  (readout_universe B1: no reparametrizable knob carries the conclusion).""")

print("== 6. N-dependence summary (the forced conditional bound) ==")
print("""  N=2: J == 0 identically (Section 2, proven)  -> signed readout DEGENERATE.
  N=3: J != 0 retained (Section 3, exact witness) -> signed readout NON-DEGENERATE.
  CONDITIONAL BOUND: if the world's mixing structure retains a non-degenerate CP-signed
  readout (empirical premise, fed in), then N >= 3 -- FORCED, no knob, no fit.
  N == 3 exactly: NOT established here (see header).  Item 2 remains [Open] at the
  unconditional level; this attempt moves the '>=3' half from borrowed-theorem+postulate
  (Attempt 2) to in-house-proven conditional mechanism.""")

print()
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS (exact arithmetic throughout; no floats anywhere)")
