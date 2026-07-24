#!/usr/bin/env python3
"""
T1 target (READOUT_GENESIS_CORE.md V.13a / II.8a): the metric-G / L_R^(pm) (here written G_op^(pm)
to avoid clashing with the retention metric G itself) antisymmetry algebra, currently tagged
[Dr]/[Open], "PROPOSED, pending T1. Do not assert it as proven."

Claim to check, EXACTLY as V.13a/II.8a state it (not the naive-transpose version):
  Split by the RETENTION METRIC G, not naive transpose:
    G_op^(+) = (G_op + G_op^adj_G) / 2      (G-self-adjoint part)
    G_op^(-) = (G_op - G_op^adj_G) / 2      (G-skew-adjoint part)
  where G_op^adj_G is the ADJOINT OF G_op WITH RESPECT TO <x,y>_G = x^T G y  (G_op^adj_G = G^-1 G_op^T G),
  NOT the plain transpose G_op^T.
  Target identity:  z^T G (G_op^(-) z) = 0   for all z   ("skew part carries oriented transfer/
  rotation, no self-diagonal contribution" under the RETENTION inner product <.,.>_G).

This script:
  1. Verifies the G-adjoint decomposition + skew-vanishing EXACTLY (Fraction arithmetic, no floats)
     on a concrete G != I fixture.
  2. NEGATIVE CONTROL: shows the naive-transpose split (using G_op^T instead of the G-adjoint)
     does NOT satisfy z^T G (G_op_skew_naive z) = 0 when G != I -- this is exactly why V.13a insists
     "not naive transpose" is load-bearing, not stylistic.
  3. Checks the abstract algebraic facts the Coq proof will need as explicit premises are actually
     true of concrete matrices (adjoint involution, bilinearity), so the Coq file isn't proving an
     abstraction that's vacuous or doesn't match the concrete construction.
"""
from fractions import Fraction as Fr

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def matadd(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matsub(A, B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scal(c, A):
    return [[c*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matvec(A, x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def vdot(x, y):
    return sum(a*b for a, b in zip(x, y))

def gauss_solve(A, b):
    """Exact Fraction Gauss-Jordan solve of A x = b for invertible A."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [v/pv for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [M[r][k] - f*M[col][k] for k in range(n+1)]
    return [M[i][n] for i in range(n)]

def matinv(A):
    n = len(A)
    cols = []
    for j in range(n):
        e = [Fr(1) if i == j else Fr(0) for i in range(n)]
        cols.append(gauss_solve(A, e))
    return transpose(cols)

F = lambda *vals: [Fr(v) for v in vals]

print("== fixture: n=3, retention metric G (symmetric, positive-definite, != I) ==")
G = [F(2, 1, 0), F(1, 3, 1), F(0, 1, 2)]
ck("G is symmetric (G = G^T)", G == transpose(G))
Ginv = matinv(G)
ck("G * G^-1 = I (G is invertible)", matmul(G, Ginv) == [F(1,0,0), F(0,1,0), F(0,0,1)])
# crude positive-definite spot check via leading principal minors (Sylvester's criterion, exact)
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
          - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
          + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
ck("leading principal minors of G all > 0 (Sylvester: G is positive-definite)",
   G[0][0] > 0 and (G[0][0]*G[1][1]-G[0][1]*G[1][0]) > 0 and det3(G) > 0)

print("\n== the operator G_op (an arbitrary linear map, NOT assumed symmetric) ==")
Gop = [F(1, 4, 0), F(0, 2, 3), F(5, 0, 1)]

print("\n== 1. G-adjoint construction: Gop_adjG = G^-1 Gop^T G ==")
Gop_adjG = matmul(matmul(Ginv, transpose(Gop)), G)
def check_adjoint(T, Tadj, G, label):
    # <Tx,y>_G = x^T G^T (Tx applied differently)... use direct: (T x)^T G y == x^T G (Tadj y)
    import random
    random.seed(0)
    ok = True
    for _ in range(6):
        x = F(random.randint(-3,3), random.randint(-3,3), random.randint(-3,3))
        y = F(random.randint(-3,3), random.randint(-3,3), random.randint(-3,3))
        lhs = vdot(matvec(T, x), matvec(G, [Fr(1) if i==j else Fr(0) for i in range(3)] and y or y))  # placeholder unused
    return ok
# direct symbolic-style check via explicit bilinear form ip(x,y) = x^T G y
def ip(x, y, G):
    return vdot(matvec(G, x), y) if False else vdot(x, matvec(G, y))
import random; random.seed(1)
def rand_vec():
    return F(random.randint(-4,4), random.randint(-4,4), random.randint(-4,4))
samples = [(rand_vec(), rand_vec()) for _ in range(8)]
ck("adjoint defining property: <Gop x,y>_G = <x, Gop_adjG y>_G for all sampled x,y",
   all(ip(matvec(Gop, x), y, G) == ip(x, matvec(Gop_adjG, y), G) for x, y in samples))
ck("involution: (Gop_adjG)_adjG = Gop  (adjoint of the adjoint returns the original)",
   matmul(matmul(Ginv, transpose(Gop_adjG)), G) == Gop)

print("\n== 2. G-symmetric/skew split of Gop (NOT naive transpose) ==")
half = Fr(1, 2)
Gop_symG  = scal(half, matadd(Gop, Gop_adjG))
Gop_skewG = scal(half, matsub(Gop, Gop_adjG))
ck("decomposition exact: Gop_symG + Gop_skewG = Gop", matadd(Gop_symG, Gop_skewG) == Gop)

Gop_symG_adjG  = matmul(matmul(Ginv, transpose(Gop_symG)), G)
Gop_skewG_adjG = matmul(matmul(Ginv, transpose(Gop_skewG)), G)
ck("Gop_symG is G-self-adjoint: (Gop_symG)_adjG = Gop_symG", Gop_symG_adjG == Gop_symG)
ck("Gop_skewG is G-skew-adjoint: (Gop_skewG)_adjG = -Gop_skewG", Gop_skewG_adjG == scal(Fr(-1), Gop_skewG))

print("\n== 3. TARGET THEOREM: <z, Gop_skewG z>_G = 0 for all z (skew part vanishes under G-IP) ==")
zs = [rand_vec() for _ in range(10)] + [F(1,0,0), F(0,1,0), F(0,0,1), F(1,1,1), F(2,-1,3)]
ck("<z, Gop_skewG z>_G = 0 for 15 sampled z (including basis vectors)",
   all(ip(z, matvec(Gop_skewG, z), G) == 0 for z in zs))

print("\n== 4. NEGATIVE CONTROL: naive transpose (ignoring G) does NOT have this property ==")
Gop_sym_naive  = scal(half, matadd(Gop, transpose(Gop)))
Gop_skew_naive = scal(half, matsub(Gop, transpose(Gop)))
ck("naive-transpose skew part IS antisymmetric in the ordinary sense (Gop_skew_naive = -Gop_skew_naive^T)",
   Gop_skew_naive == scal(Fr(-1), transpose(Gop_skew_naive)))
naive_vanishes = all(ip(z, matvec(Gop_skew_naive, z), G) == 0 for z in zs)
ck("naive-transpose skew part does NOT satisfy <z, skew_naive z>_G = 0 under G != I (should FAIL -- this is the whole point of V.13a's 'not naive transpose')",
   naive_vanishes == False)
nonzero_example = next((z, ip(z, matvec(Gop_skew_naive, z), G)) for z in zs if ip(z, matvec(Gop_skew_naive, z), G) != 0)
print(f"    concrete witness: z={nonzero_example[0]} gives <z,skew_naive z>_G = {nonzero_example[1]} (nonzero)")

print("\n== 5. sanity: with G = I (Euclidean), naive transpose and G-adjoint coincide ==")
I3 = [F(1,0,0), F(0,1,0), F(0,0,1)]
Gop_adjI = matmul(matmul(matinv(I3), transpose(Gop)), I3)
ck("when G=I, the G-adjoint reduces exactly to the plain transpose", Gop_adjI == transpose(Gop))

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS -- the G-adjoint (retention-metric) symmetric/skew split of an arbitrary")
print("operator satisfies Gop = Gop_symG + Gop_skewG, Gop_symG is G-self-adjoint, Gop_skewG is")
print("G-skew-adjoint, and <z,Gop_skewG z>_G = 0 for all z -- confirmed exact on a G!=I fixture,")
print("AND confirmed the naive-transpose version genuinely fails this property when G!=I (the")
print("negative control V.13a's own text warns about). Ready to state and prove the fully abstract")
print("(matrix-free) version in Coq.")
