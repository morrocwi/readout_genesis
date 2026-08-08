#!/usr/bin/env python3
"""
Theta DYNAMICAL SELECTION v1 — step 5.2b-1 of THETA_ROOT_PROGRAM.md, 2026-08-09.
Founder's guiding directive, recorded verbatim: "เผื่อใจไว้ด้วยว่า แท้จริงแล้วทั้งหมดอาจเป็น
สิ่งเดียวกันมาจากรากกลับสู่ราก ไม่สมมาตร แต่สมดุล" (everything may be one thing, from the
root back to the root — NOT SYMMETRIC, BUT BALANCED).

THE QUESTION (left open by 5.2a): kinematics allows every topology; which support does
the coupled Phi/Psi/Theta system actually SETTLE INTO at a full self-consistent fixed
point of the loop  delta_R -> L_R -> G[Theta] -> (Phi,Psi) -> Theta -> ... ?

SETUP (all declared): n=3 family slots (imported ansatz, Attempt 1 caveat inherited);
J=0 AND R_Phi = R_Psi = 0 (no external drive AND the closed/no-cut-exchange case — the
core's reader/record equations carry boundary currents R on the RHS; setting them to
zero is the closed-system reading, DECLARED here per review, not silently assumed);
mother-potential coefficients a=-1, b=1 (the corpus's own declared values); K=mu=1.
Full static fixed point:
    reader:  K G[w] Phi + a Phi + b Phi^3           = 0   (componentwise cubic)
    record:  K G[w] Psi + (a + 3 b Phi^2) Psi       = 0
    theta :  w_e = max(0, -(K/mu)(Phi_i-Phi_j)(Psi_i-Psi_j))   (5.2a, per edge)
"Living" fixed point := Psi != 0 (the record retains something; Psi is load-bearing per
Gate D's own failing control).

RESULTS (three layers, tiers separated):

  B1 (BALANCE LAW — exact, general; Coq: formal/InfoThetaFixedPointBalance_attempt.v):
     at ANY J=0 static fixed point with symmetric G and b != 0:
         << Phi^3 , Psi >>  :=  Sum_i Phi_i^3 Psi_i  =  0   -- FORCED.
     The reader-cubed/record overlap must vanish. This is the founder's "balanced",
     derived: not a symmetry of the configuration but a forced bilinear balance.

  B2 (SYMMETRY IS DEAD — exact, general, Coq same file): perfect agreement Psi = Phi
     forces Phi = 0 (via 2a*Phi_i = 0), and perfect mirror Psi = -Phi forces Phi = 0
     (via 2b*Phi_i^3 = 0): BOTH the symmetric and the anti-symmetric reader/record
     configurations admit only the dead state. Any living fixed point is NECESSARILY
     not-symmetric (Psi not proportional to +/-Phi) yet obeys B1's balance — the
     founder's "ไม่สมมาตร แต่สมดุล", now a pair of theorems.

  B3 (SELECTION EXPERIMENT — numeric, finite_diagnostic, floats DISCLOSED, multistart
     Newton, fixed seeds): searching all 8 supports for living fixed points:
       - path supports (P3-shape, all 3 labelings): living fixed points FOUND, residual
         ~1e-15. At least TWO distinct orbits exist across searches: a uniform-weight
         star solution (w1=w2~0.1351, spectrum {0,w,3w}, ratio exactly ~3.0 — the one
         this file's seeded run reports) and a non-uniform one (w~(0.2271,0.1421),
         spectrum ratio ~3.33) found in the exploratory prototype. Both show THREE
         DISTINCT LEVELS; balance B1 holds to ~1e-15; Psi not proportional to Phi (B2
         respected). No uniqueness claim is made. Disclosure (per review): at the
         UNIFORM orbit the non-support edge is an exact TIE (s_12 = 0, with P1=P2 and
         S1=S2 exactly — a residual leaf-swap symmetry of the profile); w=0 there is
         still forced by 5.2a's rule at s>=0. The non-uniform orbit is strictly
         concordant on its non-support edge. B2's theorems exclude only Psi = +/-Phi,
         not profile symmetries like the leaf swap.
       - K3 (all-discordant): NO living fixed point in 3000 trials including
         structured anti-aligned starts. NOT a nonexistence proof — disclosed as a
         bounded search negative.
       - single-edge and empty supports: none found with Psi != 0 (record equation
         forces Psi into the dead diagonal there).
     READING (Dr): the dynamics appears to SELECT the path topology — the same
     topology 5.1 proved is the 3-vertex one whose spectrum separates — and rejects
     both full symmetry and full disorder. The loop closes root -> configuration ->
     root: the graph the system retains is the readout of its own balanced,
     non-symmetric settlement. No generation identification is made (CRRC guard).

WHAT THIS DOES NOT ESTABLISH (binding):
  - Nonexistence of K3/other living fixed points (numeric absence only; exact
    algebraic certification attempted via Groebner/solve and TIMED OUT — recorded as
    open; the found path solution is certified only by residual ~1e-15, its exact
    minimal polynomials are open).
  - Anything beyond n=3, beyond a=-1,b=1,K=mu=1, beyond the static case, or beyond
    the quadratic edge cost — all declared, none root-forced yet.
  - Any identification of vertices/levels with generations (CRRC guard; the family
    slot itself is still the imported ansatz).

Run: python3 theta_dynamics_selection_v1.py   (stdlib only for exact parts; float
Newton for B3; a few seconds)
"""

from fractions import Fraction as Fr
from itertools import combinations
import math
import random

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


EDGES = [(0, 1), (0, 2), (1, 2)]

print("== B1. The forced balance law (exact identity sweep; general proof in Coq) ==")
# identity: Sum_i Psi_i*READER_i - Sum_i Phi_i*RECORD_i == -2 b Sum_i Phi_i^3 Psi_i
# for ANY symmetric G, any a,b,K, any profiles — so at a fixed point (both sides'
# equation-vectors zero) the balance Sum Phi_i^3 Psi_i = 0 is forced when b != 0.
random.seed(20260809)
ok = True
for _ in range(200):
    a = Fr(random.randint(-4, 4), random.randint(1, 5))
    b = Fr(random.randint(-4, 4), random.randint(1, 5))
    Kq = Fr(random.randint(1, 5), random.randint(1, 5))
    P = [Fr(random.randint(-6, 6), random.randint(1, 5)) for _ in range(3)]
    S = [Fr(random.randint(-6, 6), random.randint(1, 5)) for _ in range(3)]
    g = {(i, j): Fr(random.randint(-6, 6), random.randint(1, 5))
         for i in range(3) for j in range(i, 3)}
    G = [[g[(min(i, j), max(i, j))] for j in range(3)] for i in range(3)]
    GP = [sum(G[i][j] * P[j] for j in range(3)) for i in range(3)]
    GS = [sum(G[i][j] * S[j] for j in range(3)) for i in range(3)]
    reader = [Kq * GP[i] + a * P[i] + b * P[i] ** 3 for i in range(3)]
    record = [Kq * GS[i] + (a + 3 * b * P[i] ** 2) * S[i] for i in range(3)]
    combo = sum(S[i] * reader[i] for i in range(3)) - sum(P[i] * record[i] for i in range(3))
    if combo != -2 * b * sum(P[i] ** 3 * S[i] for i in range(3)):
        ok = False
ck("combo identity == -2b<Phi^3,Psi> exactly, 200 random (a,b,K,G,Phi,Psi)", ok)
print("  ==> at any J=0 fixed point (reader=record=0), b != 0 forces <Phi^3,Psi> = 0.")

print("== B2. Symmetry is dead (exact component algebra; general proof in Coq) ==")
# agree case Psi=Phi: concordance -> w=0 -> G=0 -> equations decouple; combining
# 3*(a p + b p^3) - (a + 3 b p^2) p = 2 a p  == 0  -> p = 0 (a != 0).
a, b = Fr(-1), Fr(1)
ok = all(3 * (a * p + b * p ** 3) - (a + 3 * b * p ** 2) * p == 2 * a * p
         for p in [Fr(0), Fr(1), Fr(-1), Fr(2, 3), Fr(-7, 5)])
ck("agree-combo identity 3*reader - record == 2a*p exactly (5 instances)", ok)
# mirror case Psi=-Phi: reader_i + record_i(-Phi) == -2 b p^3 -> p = 0 (b != 0),
# for ANY graph term gp (it cancels):
ok = True
for p in [Fr(0), Fr(1), Fr(-2, 3), Fr(5, 4)]:
    for gp in [Fr(0), Fr(3, 7), Fr(-9, 2)]:
        if (gp + a * p + b * p ** 3) + (-gp + (a + 3 * b * p ** 2) * (-p)) != -2 * b * p ** 3:
            ok = False
ck("mirror-combo identity reader + record == -2b*p^3 exactly (graph term cancels)", ok)
print("""  ==> Psi = Phi forces Phi = 0; Psi = -Phi forces Phi = 0. A LIVING fixed point
  must be NOT-SYMMETRIC (Psi not +/- Phi) yet BALANCED (B1) — "ไม่สมมาตร แต่สมดุล".""")

print("== B3. Selection experiment (numeric, finite_diagnostic, floats disclosed) ==")
af, bf, Kf, muf = -1.0, 1.0, 1.0, 1.0


def system(x, support):
    P, S = x[:3], x[3:]
    s = {e: (P[e[0]] - P[e[1]]) * (S[e[0]] - S[e[1]]) for e in EDGES}
    w = {e: (-Kf / muf * s[e] if e in support else 0.0) for e in EDGES}
    G = [[0.0] * 3 for _ in range(3)]
    for (i, j), we in w.items():
        G[i][i] += we
        G[j][j] += we
        G[i][j] -= we
        G[j][i] -= we
    F = [0.0] * 6
    for i in range(3):
        F[i] = Kf * sum(G[i][j] * P[j] for j in range(3)) + af * P[i] + bf * P[i] ** 3
        F[3 + i] = Kf * sum(G[i][j] * S[j] for j in range(3)) + (af + 3 * bf * P[i] ** 2) * S[i]
    return F, s, w, G


def newton(x0, support, iters=80):
    x = x0[:]
    for _ in range(iters):
        F, _, _, _ = system(x, support)
        if math.sqrt(sum(f * f for f in F)) < 1e-13:
            break
        J = [[0.0] * 6 for _ in range(6)]
        h = 1e-7
        for k in range(6):
            xp = x[:]
            xp[k] += h
            Fp, _, _, _ = system(xp, support)
            for i in range(6):
                J[i][k] = (Fp[i] - F[i]) / h
        Aug = [J[i][:] + [-F[i]] for i in range(6)]
        for c in range(6):
            piv = max(range(c, 6), key=lambda r2: abs(Aug[r2][c]))
            if abs(Aug[piv][c]) < 1e-14:
                return None
            Aug[c], Aug[piv] = Aug[piv], Aug[c]
            Aug[c] = [v / Aug[c][c] for v in Aug[c]]
            for r2 in range(6):
                if r2 != c and Aug[r2][c] != 0:
                    Aug[r2] = [v - Aug[r2][c] * u for v, u in zip(Aug[r2], Aug[c])]
        x = [xi + Aug[i][6] for i, xi in enumerate(x)]
    F, _, _, _ = system(x, support)
    return (x, math.sqrt(sum(f * f for f in F)))


def living_fp(x, support):
    """residual small + Psi nonzero + support sign conditions satisfied."""
    res = newton(x, support)
    if not res:
        return None
    xs, r = res
    if r > 1e-10 or math.sqrt(sum(v * v for v in xs[3:])) < 1e-2:
        return None
    _, s, w, G = system(xs, support)
    if any(s[e] >= -1e-9 for e in support):
        return None
    if any(s[e] < -1e-9 for e in EDGES if e not in support):
        return None
    return xs, r, w, G


random.seed(42)
found = {}
for k in range(4):
    for support in combinations(EDGES, k):
        sup = frozenset(support)
        for _ in range(300):
            x0 = [random.uniform(-2, 2) for _ in range(6)]
            hit = living_fp(x0, sup)
            if hit:
                found[tuple(sorted(sup))] = hit
                break
path_supports = [((0, 1), (0, 2)), ((0, 1), (1, 2)), ((0, 2), (1, 2))]
ck("living fixed points FOUND on all 3 path-shape supports",
   all(tuple(s) in found for s in path_supports), sorted(found))
ck("NO living fixed point found on K3/single-edge/empty supports (300 trials each)",
   all(tuple(s) in [tuple(p) for p in path_supports] for s in found), sorted(found))

# K3-focused deeper negative: 3000 trials incl. structured anti-aligned starts
random.seed(7)
supK = frozenset(EDGES)
k3_found = 0
for t in range(3000):
    if t < 1000:
        x0 = [random.uniform(-2, 2) for _ in range(6)]
    elif t < 2000:
        x0 = ([random.uniform(-1, 1) for _ in range(3)]
              + [random.uniform(-0.5, 0.5) for _ in range(3)])
    else:
        base = [random.uniform(-1.5, 1.5) for _ in range(3)]
        x0 = base + [-v * random.uniform(0.1, 2) for v in base]
    if living_fp(x0, supK):
        k3_found += 1
        break
ck("K3-focused search: 0 living fixed points in 3000 trials (bounded negative, "
   "NOT a nonexistence proof)", k3_found == 0, k3_found)

# properties AT the found path living fixed point
xs, r, w, G = found[((0, 1), (0, 2))]
P, S = xs[:3], xs[3:]
bal = sum(P[i] ** 3 * S[i] for i in range(3))
ck("balance B1 holds at the living FP: |<Phi^3,Psi>| < 1e-12", abs(bal) < 1e-12, bal)
crossp = abs(P[0] * S[1] - P[1] * S[0]) + abs(P[0] * S[2] - P[2] * S[0])
ck("B2 respected: Psi NOT proportional to Phi at the living FP", crossp > 1e-6)
# spectrum of symmetric G via characteristic cubic (no numpy): eigenvalues of 3x3
tr = G[0][0] + G[1][1] + G[2][2]
# G is a weighted-path Laplacian -> one eigenvalue is 0 (constants); the other two
# solve x^2 - tr*x + q = 0 with q = sum of 2x2 principal minors:
q = (G[0][0] * G[1][1] - G[0][1] * G[1][0]) + (G[0][0] * G[2][2] - G[0][2] * G[2][0]) \
    + (G[1][1] * G[2][2] - G[1][2] * G[2][1])
disc = tr * tr - 4 * q
lam1 = (tr - math.sqrt(disc)) / 2
lam2 = (tr + math.sqrt(disc)) / 2
ck("spectrum of G at the living FP has THREE DISTINCT levels {0, lam1, lam2}",
   disc > 1e-12 and lam1 > 1e-9,
   (0.0, lam1, lam2))
print(f"  living FP: weights {{(0,1): {w[(0,1)]:.6f}, (0,2): {w[(0,2)]:.6f}}}, "
      f"spectrum {{0, {lam1:.6f}, {lam2:.6f}}}, ratio {lam2/lam1:.4f} "
      f"(uniform path would give 3.0), residual {r:.1e}")
print("""  ==> READING (Dr): at self-consistent settlement the dynamics rejected both the
  dead symmetric states (B2) and — within this bounded search — the full-disorder K3;
  what lives is a PATH configuration, not symmetric, balanced (B1), whose retained
  spectrum separates into three distinct levels. From the root, back to the root.""")

print()
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS (exact parts in Fractions; B3 floats disclosed)")
