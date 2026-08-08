#!/usr/bin/env python3
"""
Theta TOPOLOGY-IS-A-READOUT v1 — step 5.2a of THETA_ROOT_PROGRAM.md, 2026-08-09.

THE QUESTION (step 5.2): which family-graph topology does the ROOT force — so that no
graph is ever hand-picked?

THE ROOT-NATIVE ANSWER ESTABLISHED HERE (exact arithmetic, no floats; Coq companion
formal/InfoThetaTopologyReadout_attempt.v):

  R1 (bilinear edge identity, exact/ring): for every edge e=(i,j),
        S_Theta^e = Phi^T L_e Psi = (Phi_i - Phi_j)(Psi_i - Psi_j)
     — the per-edge geometry source of Gate D is EXACTLY the product of the reader's
     retained difference and the record's retained difference across that pair.

  R2 (clipped stationarity, exact — STATIC/FIXED-POINT CASE ONLY: at a fixed point of
     Gate D's dynamic law the M_Theta d2_t Theta term vanishes, reducing the law to
     grad U(w) = -K s per edge at FROZEN (Phi,Psi); the dynamic transient and the
     co-evolution of (Phi,Psi) are untouched here — that is 5.2b): with quadratic edge cost
     U(w) = mu w^2/2 (mu > 0, K > 0) under the census admissibility cone w >= 0,
     the stationary weight of every edge is
        w_e* = max(0, -(K/mu) * (Phi_i-Phi_j)(Psi_i-Psi_j))
     — an edge EXISTS (w_e* > 0) iff the reader difference and record difference across
     that pair are ANTI-ALIGNED (discordant); aligned or tied pairs get w_e* = 0.

  ==> TOPOLOGY IS A READOUT, NOT AN INPUT: the family graph's support is the discordance
      pattern between the reader profile and the record profile. No graph is chosen by
      hand; the graph is what the reader/record configuration retains. This is the
      root-native reframing of step 5.2 — the mother equation's own Gate-D law, the
      Theta census (a = edges), and nothing imported.

  R3 (support census, exact, exhaustive over rank patterns + tie witnesses): on 3
     vertices with INJECTIVE profiles, ALL 8 labeled supports are realizable (witnesses
     exhibited, each verified exactly; complement-closure Phi -> Phi, Psi -> -Psi flips
     every discordance, pairing the 8 into 4 complement pairs). HONEST NEGATIVE:
     kinematics alone does NOT restrict the topology — the root's restriction, if any,
     must come from the DYNAMICS (which (Phi,Psi) configuration the coupled system
     settles into) — that is step 5.2b, named and untouched here.

  R4 (CORRECTED after independent review — an earlier draft's reading "3 distinct levels
     appear exactly when disorder is PARTIAL" was REFUTED and is WITHDRAWN): 5.1's spectra
     assume per-orbit UNIFORM weights, but R2's stationary weights are the discordance
     values themselves and are provably NEVER uniform on an all-discordant K3
     (uniformity forces a^2+ab+b^2=0 for the Phi-gaps, which has no nonzero rational
     solution — verified exactly below). So the two layers do not compose directly.
     Under R2 weights: the file's own K3 total-disorder witness gives spectrum
     {0, 3, 9}*(K/mu) — THREE distinct levels from TOTAL disorder (verified exactly
     below); P3-supports give 3 distinct levels for any positive weights. What survives:
     the degenerate uniform-K3 spectrum of 5.1 is UNREACHABLE as an R2 readout — the R2
     mechanism generically avoids the degenerate configuration. Tier Dr.

WHAT THIS DOES NOT ESTABLISH (binding):
  - Which support the dynamics selects (5.2b, open). Nothing here forces P3.
  - Any identification of vertices/edges/levels with generations or physics (CRRC
    guard; unbuilt square). The 3-vertex family space itself is still the imported
    C^N working ansatz (Attempt 1 caveat, inherited).
  - The quadratic edge cost U(w) = mu w^2/2 is the SIMPLEST admissible choice, declared
    (Gate D's own fixture uses quadratic U_Theta); other convex costs shift the value of
    w_e*. The SUPPORT rule is EXPECTED to be cost-independent for COERCIVE strictly
    convex U with U'(0)=0 — checked here for ONE non-quadratic instance (w^4/4, grid)
    only; the general statement is OPEN and needs the coercivity hypothesis (a
    bounded-slope convex U admits no minimizer at all for s<0, per review).

Tier: R1/R2 exact algebra (Coq companion, entrywise convention); R3 exact enumeration +
      witnesses (finite_diagnostic); R4 Dr. Item 2 stays [Open].

Run: python3 theta_topology_readout_v1.py   (stdlib only; exact Fractions)
"""

from fractions import Fraction as Fr
from itertools import permutations
import random

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


EDGES = [(0, 1), (0, 2), (1, 2)]


def edge_L(n, i, j):
    L = [[Fr(0)] * n for _ in range(n)]
    L[i][i] = L[j][j] = Fr(1)
    L[i][j] = L[j][i] = Fr(-1)
    return L


def bilinear(P, L, S):
    n = len(P)
    return sum(P[a] * L[a][b] * S[b] for a in range(n) for b in range(n))


print("== R1. The bilinear edge identity (exact, random rational sweep) ==")
random.seed(20260809)
ok = True
for _ in range(300):
    P = [Fr(random.randint(-9, 9), random.randint(1, 7)) for _ in range(3)]
    S = [Fr(random.randint(-9, 9), random.randint(1, 7)) for _ in range(3)]
    for (i, j) in EDGES:
        if bilinear(P, edge_L(3, i, j), S) != (P[i] - P[j]) * (S[i] - S[j]):
            ok = False
print("  S_Theta^e = Phi^T L_e Psi = (Phi_i-Phi_j)(Psi_i-Psi_j)")
ck("identity holds exactly, 300 random profiles x 3 edges (general proof: Coq R1)", ok)

print("== R2. Clipped stationarity: edge exists iff reader/record discordant ==")
mu, K = Fr(3), Fr(2)


def w_star(s):
    """argmin over w>=0 of mu w^2/2 + K s w (exact)."""
    unc = -K * s / mu
    return unc if unc > 0 else Fr(0)


# verify minimality exactly on a rational grid around the claimed minimizer:
ok = True
for s in [Fr(-5, 3), Fr(-1), Fr(0), Fr(1, 4), Fr(2)]:
    wst = w_star(s)
    f = lambda w: mu * w * w / 2 + K * s * w
    for dw in [Fr(-7, 5), Fr(-1, 3), Fr(1, 8), Fr(1), Fr(9, 4)]:
        w = wst + dw
        if w >= 0 and f(w) < f(wst):
            ok = False
ck("w* = max(0, -(K/mu) s) minimizes the edge cost on the cone (exact grid, 5 s-values)",
   ok)
ck("edge PRESENT iff discordant: w*(s<0)>0, w*(0)=0, w*(s>0)=0",
   w_star(Fr(-1)) > 0 and w_star(Fr(0)) == 0 and w_star(Fr(1)) == 0)
# support rule is cost-independent for convex U with U'(0)=0: one non-quadratic check
# U(w) = w^4/4 (U'(w)=w^3): stationary w^3 = -K s => same sign rule on the cone.
ok = True
for s in [Fr(-2), Fr(0), Fr(3)]:
    # minimize g(w)=w^4/4 + K s w over w>=0 on an exact grid vs claimed support
    claimed_present = s < 0
    g = lambda w: w ** 4 / 4 + K * s * w
    best_w = min([Fr(k, 6) for k in range(0, 25)], key=g)
    if (best_w > 0) != claimed_present:
        ok = False
ck("support rule survives a non-quadratic convex cost (w^4/4, grid instance)", ok)
print("""  ==> TOPOLOGY IS A READOUT: the stationary family graph's edge set = the
  DISCORDANCE pattern between reader profile Phi and record profile Psi. The graph is
  never chosen; it is what the reader/record configuration retains (Gate D + census,
  nothing imported).""")

print("== R3. Support census: all 8 labeled supports realizable (witnesses, exact) ==")
# systematic: over all pairs of rank permutations (injective profiles), the discordance
# pattern takes all 8 values — verified exhaustively:
pats = set()
for a in permutations([Fr(1), Fr(2), Fr(3)]):
    for b in permutations([Fr(1), Fr(2), Fr(3)]):
        pat = tuple(1 if (a[i] - a[j]) * (b[i] - b[j]) < 0 else 0 for (i, j) in EDGES)
        pats.add(pat)
ck("exhaustive over 36 injective rank-pairs: all 8 supports appear", len(pats) == 8,
   sorted(pats))
# named witnesses for the two structurally-interesting supports:
Phi_K3, Psi_K3 = [Fr(1), Fr(2), Fr(3)], [Fr(3), Fr(2), Fr(1)]     # total reversal
patK = [(Phi_K3[i] - Phi_K3[j]) * (Psi_K3[i] - Psi_K3[j]) < 0 for (i, j) in EDGES]
ck("K3 support = TOTAL disorder witness (full reversal): all 3 discordant", all(patK))
Phi_P3, Psi_P3 = [Fr(3), Fr(1), Fr(2)], [Fr(-2), Fr(-1), Fr(-5)]  # partial disorder
patP = [(Phi_P3[i] - Phi_P3[j]) * (Psi_P3[i] - Psi_P3[j]) < 0 for (i, j) in EDGES]
ck("P3-shape support = PARTIAL disorder witness: exactly 2 discordant (edges 01,12)",
   patP == [True, False, True], patP)
# complement closure: Psi -> -Psi flips every discordance (exact, on the P3 witness):
Psi_neg = [-x for x in Psi_P3]
patN = [(Phi_P3[i] - Phi_P3[j]) * (Psi_neg[i] - Psi_neg[j]) < 0 for (i, j) in EDGES]
ck("complement closure: Psi -> -Psi flips the pattern exactly",
   patN == [not x for x in patP], patN)
print("""  ==> HONEST NEGATIVE, stated plainly: kinematics does NOT restrict the topology —
  every 3-vertex support is the readout of SOME reader/record configuration. The root's
  selection, if any, must come from DYNAMICS (which configuration the coupled
  Phi/Psi/Theta system settles into) — step 5.2b, named, untouched.""")

print("== R4 (corrected). R2 weights are non-uniform: total disorder ALSO separates ==")


def is_eigen(L, v, lam):
    n = len(v)
    return [sum(L[i][j] * v[j] for j in range(n)) for i in range(n)] == [lam * x for x in v]



# the file's own K3 total-disorder witness, now with R2's ACTUAL stationary weights
# (proportional to the discordance magnitudes, K/mu scaled out): s = (-1,-4,-1)
w01c, w02c, w12c = Fr(1), Fr(4), Fr(1)
LC = [[w01c + w02c, -w01c, -w02c],
      [-w01c, w01c + w12c, -w12c],
      [-w02c, -w12c, w02c + w12c]]
ck("counterexample (review): (1,1,1) eigenvector for 0", is_eigen(LC, [Fr(1)] * 3, Fr(0)))
ck("counterexample: (1,0,-1) eigenvector for 9", is_eigen(LC, [Fr(1), Fr(0), Fr(-1)], Fr(9)))
tr = LC[0][0] + LC[1][1] + LC[2][2]
ck("counterexample: trace 12 -> third eigenvalue 3 -> spectrum {0,3,9} ALL DISTINCT",
   tr == 12 and len({Fr(0), Fr(9), tr - 9}) == 3)
# impossibility of the uniform all-discordant K3 as an R2 readout: uniformity forces
# ax = by = (a+b)(x+y) = s, which algebraically requires a^2+ab+b^2 = 0 (no nonzero
# rational solution: a^2+ab+b^2 = (a+b/2)^2 + 3b^2/4 > 0). Identity check, exact:
okimp = True
for (a, b) in [(Fr(1), Fr(2)), (Fr(-3), Fr(5)), (Fr(7, 3), Fr(-1, 4))]:
    s = Fr(-6)
    x, y = s / a, s / b
    # (a+b)(x+y) - s must equal s*(a^2+ab+b^2)/(ab) exactly:
    if (a + b) * (x + y) - s != s * (a * a + a * b + b * b) / (a * b):
        okimp = False
    if a * a + a * b + b * b <= 0:
        okimp = False
ck("uniform all-discordant K3 impossible: constraint reduces to a^2+ab+b^2=0, and "
   "a^2+ab+b^2 > 0 exactly on all test gap-pairs", okimp)
print("""  ==> CORRECTED READING (Dr): the earlier 'partial disorder <-> 3 distinct levels'
  claim is WITHDRAWN (refuted by this counterexample — R2's weights are the discordance
  values, not 5.1's uniform w). What survives, exactly: under R2 weights BOTH the K3
  total-disorder witness ({0,3,9}) and every positive-weight P3-support give 3 distinct
  levels, and 5.1's degenerate uniform-K3 spectrum is UNREACHABLE as an R2 readout.
  The R2 mechanism generically avoids degeneracy. No generation identification (CRRC).""")

print()
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS (exact arithmetic throughout; no floats anywhere)")
