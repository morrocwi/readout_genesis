#!/usr/bin/env python3
"""
Theta MINIMAL LIVING COUNT v1 — step 5.2b-2 of THETA_ROOT_PROGRAM.md, 2026-08-09.

THE RDI QUESTION THIS ANSWERS: the whole Theta program so far ran on n=3 family slots —
but 3 was FED as the slot count. Does the mechanism itself prefer any n? This file runs
the n-scan the RDI checklist demands before any identification square is even proposed.

HEADLINE RESULT (machine-checked): **THE MINIMAL LIVING SYSTEM HAS >= 3 SLOTS.**
  At n=2, the closed static reader/record/Theta system (declared setting: J=0,
  R_Phi=R_Psi=0, a=-1, b=1, K=mu=1, 5.2a support rule) admits NO living fixed point:
  - empty-support branch: the record dies componentwise (s=0) — Coq theorem
    n2_empty_support_dead (formal/InfoThetaMinimalLiving_attempt.v, axiom-free);
  - edge-present branch (both retained differences nonzero): the four fixed-point
    equations are CONTRADICTORY — Coq theorem n2_edge_present_dead (axiom-free), via a
    complete case tree (U=0 vs U^2=4-3D^2, T=0 vs 3D^2=4, endgame factor
    (3D^2-4)(D^2-1)=0 with every root killing D<>0 or E<>0 or U<>0);
  - TOP-LEVEL: n2_no_living_fixed_point (added per review) assembles both branches
    under the 5.2a support rule into ONE Coq theorem: the record vanishes, s0=s1=0
    (the support-rule case split is an ordered-field step; M2's core stays order-free).
  Every M2 proof step is field algebra in characteristic 0 — no order axioms, no square
  roots — so that derivation is valid over R, not only Q (formal Coq.Reals restatement
  open, noted not claimed). This file re-verifies the four reduction identities and the
  case-B endgame factorization symbolically (sympy, exact); the full case tree lives in
  the Coq file; numerics find no living FP (multistart).

  Combined with 5.2b-1 (living fixed points EXIST at n=3, finite_diagnostic):

      n=2: dead (PROVEN)      n=3: alive (numeric)      ==>  N >= 3, ROOT-NATIVE.

  This converges with item 2 Attempt 3's CP-conditional N >= 3 from a completely
  independent, imported-physics direction. Two arrows, one target, different premises —
  neither cites the other's evidence (Q3 identity-by-role respected: root-native
  minimal-living N and CP-mixing N are DIFFERENT quantities until an admissibility
  square identifies them; none is built here). Independent review additionally
  confirmed the nonexistence by Groebner saturation: no living n=2 fixed point exists
  even over the COMPLEX numbers.

THE HONEST OTHER HALF (n-scan up, finite_diagnostic): n=4 ALSO lives — and less
  selectively (living supports found in several shapes: paths/trees, a star, and the
  4-cycle; see the scan below). So this mechanism FORCES >= 3 but does NOT force
  exactly 3 by existence alone. "Exactly 3" currently requires the MINIMAL-LIVING
  selection reading (Dr): the framework's own minimality discipline (minimal
  non-spectator carrier, EQ-stream minimality semantics: minimum value that still
  supports a NONTRIVIAL retained closure) selects n=3 as the first living count.
  That is a declared selection principle, not a theorem — stated plainly.
  Structure of the n=4 living classes (per review): the (0,1,1,2) class has an
  ISOLATED vertex whose slot is EXACTLY dead (its decoupled equations are M1's
  hypotheses, forcing its record component to 0) — that class is the n=3 living path
  embedded in n=4, with living-ness concentrated on 3 slots; the star (1,1,1,3), the
  P4 path (1,1,2,2), and the 4-cycle (2,2,2,2) classes are genuinely 4-slot living.

WHAT THIS DOES NOT ESTABLISH (binding):
  - n=3 uniqueness by dynamics (n=4 lives); any level<->generation identification
    (CRRC guard — unbuilt square); stability analysis of living FPs (open); the
    dynamic (non-static) case; parameter families beyond the declared a=-1,b=1,K=mu=1.

Run: python3 theta_minimal_living_v1.py   (sympy for exact identity checks; float
Newton for the n-scan; ~1-2 min)
"""

import math
import random
from itertools import combinations

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


print("== 1. The n=2 case tree, every identity re-verified exactly (sympy) ==")
import sympy as sp

p0, p1, s0, s1 = sp.symbols('p0 p1 s0 s1')
U = p0 + p1
D = p0 - p1
T = s0 + s1
E = s0 - s1
# edge-present branch: w = -DE substituted into the four componentwise equations
E1 = sp.expand(-D * D * E - p0 + p0 ** 3)
E2 = sp.expand(D * D * E - p1 + p1 ** 3)
R0 = sp.expand(-D * E * E + (-1 + 3 * p0 ** 2) * s0)
R1 = sp.expand(D * E * E + (-1 + 3 * p1 ** 2) * s1)


def ident(name, lhs, rhs):
    ck(name, sp.simplify(sp.expand(lhs - rhs)) == 0)


ident("reduction rsum : 4(E1+E2) == U(U^2+3D^2-4)",
      4 * (E1 + E2), U * (U * U + 3 * D * D - 4))
ident("reduction rdiff: 4(E1-E2) == D(-8DE-4+3U^2+D^2)",
      4 * (E1 - E2), D * (-8 * D * E - 4 + 3 * U * U + D * D))
ident("reduction csum : 4(R0+R1) == -4T+3T(U^2+D^2)+6UDE",
      4 * (R0 + R1), -4 * T + 3 * T * (U * U + D * D) + 6 * U * D * E)
ident("reduction cdiff: 4(R0-R1) == -8DE^2-4E+6UDT+3E(U^2+D^2)",
      4 * (R0 - R1), -8 * D * E * E - 4 * E + 6 * U * D * T + 3 * E * (U * U + D * D))
# endgame of case B (U^2=4-3D^2, DE=1-D^2, T eliminated): the final constraint factors
u, d, t = sp.symbols('u d t')
e_sub = (1 - d * d) / d
csum_B = 4 * t - 3 * t * d * d + 3 * u * d * e_sub
cdiff_B = sp.expand(-8 * d * e_sub ** 2 + 8 * e_sub - 6 * d * d * e_sub + 6 * u * d * t)
t_sol = sp.solve(sp.Eq(sp.simplify(cdiff_B), 0), t)[0]
final = sp.factor(sp.expand(sp.simplify(csum_B.subs(t, t_sol) * 3 * u * d)).subs(u ** 2, 4 - 3 * d * d))
ck("case-B endgame factors as 8 d (d-1)(d+1)(3d^2-4) (every root contradicts a "
   "living hypothesis)", final == sp.factor(8 * d * (d - 1) * (d + 1) * (3 * d * d - 4)), final)
print("""  ==> the complete case tree is machine-checked in Coq
  (formal/InfoThetaMinimalLiving_attempt.v: n2_empty_support_dead +
  n2_edge_present_dead + 4 reduction identities, all Print Assumptions Closed).
  All steps are characteristic-0 field algebra: valid over R, not only Q.""")

print("== 2. Numeric confirmation: n=2 finds nothing; n=3 lives; n=4 lives broadly ==")


def run_n(n, trials, seed):
    random.seed(seed)
    EDG = [(i, j) for i in range(n) for j in range(i + 1, n)]
    a, b, K, mu = -1.0, 1.0, 1.0, 1.0

    def system(x, support):
        P, S = x[:n], x[n:]
        s = {e: (P[e[0]] - P[e[1]]) * (S[e[0]] - S[e[1]]) for e in EDG}
        w = {e: (-K / mu * s[e] if e in support else 0.0) for e in EDG}
        G = [[0.0] * n for _ in range(n)]
        for (i, j), we in w.items():
            G[i][i] += we
            G[j][j] += we
            G[i][j] -= we
            G[j][i] -= we
        F = [0.0] * (2 * n)
        for i in range(n):
            F[i] = K * sum(G[i][j] * P[j] for j in range(n)) + a * P[i] + b * P[i] ** 3
            F[n + i] = K * sum(G[i][j] * S[j] for j in range(n)) \
                + (a + 3 * b * P[i] ** 2) * S[i]
        return F, s, w, G

    def newton(x0, support, iters=100):
        x = x0[:]
        m = 2 * n
        for _ in range(iters):
            F, _, _, _ = system(x, support)
            if math.sqrt(sum(f * f for f in F)) < 1e-13:
                break
            J = [[0.0] * m for _ in range(m)]
            h = 1e-7
            for k in range(m):
                xp = x[:]
                xp[k] += h
                Fp, _, _, _ = system(xp, support)
                for i in range(m):
                    J[i][k] = (Fp[i] - F[i]) / h
            Aug = [J[i][:] + [-F[i]] for i in range(m)]
            for c in range(m):
                piv = max(range(c, m), key=lambda r2: abs(Aug[r2][c]))
                if abs(Aug[piv][c]) < 1e-14:
                    return None
                Aug[c], Aug[piv] = Aug[piv], Aug[c]
                Aug[c] = [v / Aug[c][c] for v in Aug[c]]
                for r2 in range(m):
                    if r2 != c and Aug[r2][c] != 0:
                        Aug[r2] = [v - Aug[r2][c] * u2 for v, u2 in zip(Aug[r2], Aug[c])]
            x = [xi + Aug[i][m] for i, xi in enumerate(x)]
        F, _, _, _ = system(x, support)
        return (x, math.sqrt(sum(f * f for f in F)))

    living = {}
    for k in range(len(EDG) + 1):
        for support in combinations(EDG, k):
            sup = frozenset(support)
            for _ in range(trials):
                x0 = [random.uniform(-2, 2) for _ in range(2 * n)]
                res = newton(x0, sup)
                if not res:
                    continue
                x, r = res
                if r > 1e-10:
                    continue
                if math.sqrt(sum(v * v for v in x[n:])) < 1e-2:
                    continue
                _, s, w, G = system(x, sup)
                if any(s[e] >= -1e-9 for e in sup):
                    continue
                if any(s[e] < -1e-9 for e in EDG if e not in sup):
                    continue
                living[tuple(sorted(sup))] = r
                break
    return living


liv2 = run_n(2, trials=400, seed=2)
ck("n=2: NO living support found (400 trials/support — matching the Coq proof)",
   len(liv2) == 0, sorted(liv2))
liv3 = run_n(3, trials=120, seed=3)
ck("n=3: living supports found, and they are EXACTLY the 3 path shapes",
   sorted(liv3) == [((0, 1), (0, 2)), ((0, 1), (1, 2)), ((0, 2), (1, 2))], sorted(liv3))
liv4 = run_n(4, trials=60, seed=4)
ck("n=4: living supports exist too (>= 10 found) — existence does NOT single out n=3",
   len(liv4) >= 10, len(liv4))


def shape(sup, n):
    deg = [0] * n
    for (i, j) in sup:
        deg[i] += 1
        deg[j] += 1
    return tuple(sorted(deg))


shapes4 = sorted({shape(s, 4) for s in liv4})
print(f"  n=4 living degree-sequences: {shapes4}")
ck("n=4 selection is BROADER than paths (more than one degree-sequence class lives)",
   len(shapes4) > 1, shapes4)

print("""== 3. Verdict (tiers separated) ==
  PROVEN (Th_coqc, char-0 field algebra, R-valid): n=2 admits NO living fixed point.
  MEASURED (finite_diagnostic): n=3 lives (paths only); n=4 lives (several shapes).
  ==> ROOT-NATIVE LOWER BOUND: a living reader/record/geometry loop needs >= 3 slots.
      The count 3 is the MINIMAL living count — 'exactly 3' via the framework's own
      declared minimality-selection discipline (Dr), not by existence alone (n=4 lives).
  Convergence, stated carefully (Q3): root-native minimal-living N >= 3 (here) and
  CP-conditional N >= 3 (Attempt 3, imported physics) are INDEPENDENT arrows at the
  same value; identifying their N's is an unbuilt admissibility square (CRRC guard).""")

print()
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS")
