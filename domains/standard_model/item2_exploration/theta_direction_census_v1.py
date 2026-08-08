#!/usr/bin/env python3
"""
Theta-direction census + Theta-law reconciliation, 2026-08-08 (founder ruling: Theta is
elevated to a NEW ROOT alongside reader Phi / record Psi / retained difference delta_R —
"ไปอ่าน readout universe เพื่อเชื่อมตัวอ่าน บันทึก ความแตกต่าง และธีต้าซึ่งเป็นรากใหม่").

TWO deliverables, both exact-Fraction arithmetic (no floats anywhere), both answering gaps
the 2026-08-08 readout_universe survey found explicitly OPEN in the corpus:

GAP 1 (census): the affine living-geometry law G[Theta] = G_0 + Sum_a Theta^a G_a is written
  in READOUT_GENESIS_CORE.md:1280, but the index set of `a` is never declared anywhere.
  ANSWER (proven for n=3 in formal/InfoThetaEdgeCensus_attempt.v, verified for n=3 and n=4
  here): the root's own forced characterization of admissible retained-difference operators
  (symmetric, zero-row-sum, off-diagonal <= 0 — the same three properties that force
  L_R = D_W - W, Th_coqc in readout_universe logic.md R-L-uniq) makes the admissible
  deformation directions EXACTLY one per EDGE: every admissible L decomposes uniquely as
  Sum_e w_e L_e with w_e >= 0 (single-edge Laplacians), and the L_e are linearly
  independent — so a = edges, Theta^e = retained edge weight W_ij, and the DIRECTION census
  is discrete/countable BY CONSTRUCTION (C(n,2) directions at n vertices). Scope of the
  protection, stated precisely (per independent review): the INDEX-CONTINUUM half of the
  retracted EQ-069..071 mistake — an undeclared or continuous family of deformation
  directions — is excluded at the index level (finite edge census). The KNOB half — sweeping
  one weight as a free tunable parameter and reading a smooth bijection of it as an
  observable — is NOT excluded by the census: each Theta^e remains a freely settable
  rational value, and the standing discrete-only constraint (CONTINUUM_ARC_ERROR_NOTE.md
  lessons 1 and 5) must still be enforced separately. CRRC guard: nothing here identifies
  edges with generations or any physics — that square is NOT built here.

GAP 2 (reconciliation): the corpus carries TWO Theta laws with no reconciliation statement:
  (A) affine recurrence  Theta_{n+1} = A_T Theta_n + B_TP Phi_n + B_TS Psi_n + u  [Dr]
      (READOUT_GENESIS_CORE.md:1278; A_T/B_TP/B_TS never defined anywhere), and
  (B) variational law    M_T d2_t Theta + grad U_T + K * Phi^T (dG/dTheta) Psi = 0
      (relativity closure Gate D, FINITE_INTERNAL_CLOSURE, exact fixture Theta_{n+1}=3/8,
      failing control proving Psi load-bearing).
  ANSWER (proven exactly below): (B) with quadratic U_T IS an affine recurrence — but on the
  DOUBLED state (Theta_n, Theta_{n-1}) and with a source BILINEAR in (Phi,Psi); and NO
  constant matrices B_TP/B_TS can represent that bilinear source (exact counterexample:
  scaling both fields by 2 scales the true source by 4 but any linear form by 2). So law (A)
  as literally written (linear in Phi and Psi separately) is NOT the realized law — it is at
  most a frozen-field linearization of (B). (Premise of the impossibility, made explicit per
  independent review: u_{T,n} is read as an exogenous, FIELD-INDEPENDENT drive — the
  standard affine-recurrence reading, matching the corpus's constant-matrix notation; if
  u_{T,n} were allowed to depend on (Phi,Psi), the impossibility becomes vacuous by
  absorption and the named B-slots become meaningless notation.) RESOLUTION RECORDED: (B) is canonical (it is the
  one with an action, a fixture, and a failing control); (A) should be read as (B)'s
  linearization and its undefined A_T/B_TP/B_TS as derived, not free, objects.

Tier: census = Th_coqc (n=3, Coq witness) + finite_diagnostic (n=4 exact sweep here);
      reconciliation = exact algebra on declared forms (finite_diagnostic), with the
      canonical-law choice a RECORDED DECISION, not a theorem.

Run: python3 theta_direction_census_v1.py   (stdlib only; exact arithmetic)
"""

from fractions import Fraction as Fr
from itertools import combinations
import random

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


def edge_laplacian(n, i, j):
    """Single-edge Laplacian L_e for edge (i,j) on n vertices: exact Fractions."""
    L = [[Fr(0)] * n for _ in range(n)]
    L[i][i] = Fr(1)
    L[j][j] = Fr(1)
    L[i][j] = Fr(-1)
    L[j][i] = Fr(-1)
    return L


def mat_add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mat_scale(c, A):
    return [[c * x for x in row] for row in A]


def zeros(n):
    return [[Fr(0)] * n for _ in range(n)]


def exact_rank(M):
    """Rank over Q by exact Gaussian elimination (Fractions)."""
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0])
    rank, r = 0, 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        M[r] = [x / M[r][c] for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                M[i] = [a - M[i][c] * b for a, b in zip(M[i], M[r])]
        r += 1
        rank += 1
        if r == rows:
            break
    return rank


print("== 1. GAP 1 — the Theta-direction census: a = EDGES, exactly ==")
random.seed(20260808)
for n in (3, 4):
    edges = list(combinations(range(n), 2))
    gens = [edge_laplacian(n, i, j) for (i, j) in edges]

    # (a) linear independence of the edge generators: rank of the flattened set = #edges
    flat = [[g[i][j] for i in range(n) for j in range(n)] for g in gens]
    ck(f"n={n}: {len(edges)} edge generators are linearly independent (exact rank"
       f" = C({n},2) = {len(edges)})", exact_rank(flat) == len(edges), exact_rank(flat))

    # (b) round-trip: random nonneg rational weights -> admissible L -> recover weights
    all_ok = True
    for trial in range(50):
        w = {e: Fr(random.randint(0, 12), random.randint(1, 7)) for e in edges}
        L = zeros(n)
        for e, g in zip(edges, gens):
            L = mat_add(L, mat_scale(w[e], g))
        # admissibility of the built L (symmetric, zero-row-sum, offdiag <= 0)
        sym = all(L[i][j] == L[j][i] for i in range(n) for j in range(n))
        rowsum = all(sum(L[i]) == 0 for i in range(n))
        offd = all(L[i][j] <= 0 for i in range(n) for j in range(n) if i != j)
        # census recovery: w_e := -L[i][j] — unique by the Coq uniqueness theorem (n=3)
        rec = {(i, j): -L[i][j] for (i, j) in edges}
        if not (sym and rowsum and offd and rec == w):
            all_ok = False
            break
    ck(f"n={n}: 50 exact round-trips weight->admissible L->unique recovery", all_ok)

print("""  ==> the admissible deformation directions of the retained-difference operator are
  ONE PER EDGE (one per retained pairwise distinction): G_0 = 0, a = edges, G_a = L_e,
  Theta^e = W_ij.  The DIRECTION census is discrete/countable by construction — a finite
  edge set.  Protection scope (per review): the INDEX-CONTINUUM half of the retracted
  EQ-069..071 mistake is excluded (finite direction set); the KNOB half is NOT — each
  Theta^e is still a freely settable rational, so the standing discrete-only constraint
  must still be enforced separately.  n=3 case is Th_coqc:
  formal/InfoThetaEdgeCensus_attempt.v (exists/unique/independent, Print Assumptions
  Closed).  CRRC guard: edges are NOT identified with generations or any physics here.""")

print("== 2. GAP 2 — reconciling the two Theta laws ==")
# The realized law (B), Gate D exact fixture (relativity_closure_v0_2.py), reproduced:
# M_T d2_t Theta + grad U_T + K * Phi^T G_1 Psi = 0, explicit stepper
# Theta_{n+1} = 2 Theta_n - Theta_{n-1} - dt^2/M_T * (grad U(Theta_n) + K * S_Theta)
M_T, K, dt = Fr(2), Fr(1), Fr(1)
Theta_n, Theta_nm1 = Fr(1, 2), Fr(0)
# U_T = Theta^2/4  =>  grad U = Theta/2 ;  G_1 = [[0,1],[1,0]] ; Phi=[1,0], Psi=[0,1]
Phi, Psi = [Fr(1), Fr(0)], [Fr(0), Fr(1)]
G1 = [[Fr(0), Fr(1)], [Fr(1), Fr(0)]]
S_Theta = sum(Phi[i] * G1[i][j] * Psi[j] for i in range(2) for j in range(2))
ck("Gate D fixture source S_Theta = Phi^T G_1 Psi = 1 exactly", S_Theta == 1, S_Theta)
Theta_np1 = 2 * Theta_n - Theta_nm1 - dt * dt / M_T * (Theta_n / 2 + K * S_Theta)
ck("Gate D exact fixture reproduced: Theta_{n+1} = 3/8", Theta_np1 == Fr(3, 8), Theta_np1)

# (i) law (B) IS affine — on the DOUBLED state (Theta_n, Theta_{n-1}), source bilinear:
# [Theta_{n+1}]   [2 - dt^2 mu/(2 M_T)   -1] [Theta_n  ]   [-dt^2 K/M_T * Phi^T G_a Psi]
# [Theta_n    ] = [1                      0] [Theta_nm1] + [0                          ]
mu = Fr(1, 2)  # grad U = mu*Theta with U = Theta^2/4
A_doubled = [[2 - dt * dt * mu / M_T, Fr(-1)], [Fr(1), Fr(0)]]
src = [-dt * dt * K / M_T * S_Theta, Fr(0)]
state = [Theta_n, Theta_nm1]
stepped = [sum(A_doubled[i][j] * state[j] for j in range(2)) + src[i] for i in range(2)]
ck("doubled-state affine form reproduces the variational stepper exactly",
   stepped[0] == Theta_np1 and stepped[1] == Theta_n, stepped)

# (ii) NO constant linear maps B_TP, B_TS can represent the bilinear source:
# scaling BOTH fields by 2 scales Phi^T G_a Psi by 4, but B_TP(2Phi)+B_TS(2Psi) by 2.
S_scaled = sum((2 * Phi[i]) * G1[i][j] * (2 * Psi[j]) for i in range(2) for j in range(2))
ck("bilinear source scales x4 under (Phi,Psi) -> (2Phi,2Psi)", S_scaled == 4 * S_Theta,
   S_scaled)
# if S = B_TP Phi + B_TS Psi held at both (Phi,Psi) and (2Phi,2Psi), then
# S_scaled = 2*(B_TP Phi + B_TS Psi) = 2*S_Theta — contradiction whenever S_Theta != 0:
ck("linear-in-each-field law (A) contradicted: 4*S != 2*S given S != 0 (exact)",
   S_scaled != 2 * S_Theta and S_Theta != 0)

print("""  ==> RECONCILIATION RECORDED: the variational Gate-D law (B) is CANONICAL (it has
  the action, the exact fixture 3/8, and the failing control proving Psi load-bearing).
  The affine recurrence (A) as literally written — linear in Phi and Psi separately with
  undefined constant B_TP/B_TS — CANNOT represent (B)'s bilinear reader x record source
  (exact scaling contradiction above); (A) is at most a frozen-field linearization of (B),
  affine only on the doubled state (Theta_n, Theta_{n-1}).  A_T/B_TP/B_TS are therefore
  DERIVED objects of (B)'s linearization, not free root-level dials.""")

print()
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS (exact arithmetic throughout; no floats anywhere)")
