#!/usr/bin/env python3
"""
Theta SECTOR census v1 — step 5.1 of THETA_ROOT_PROGRAM.md, 2026-08-09: which
Theta-directions survive the declared symmetry, and what spectra the survivors give.

WHAT THIS STEP ESTABLISHES (exact arithmetic throughout, no floats):

FACT 0 (scoping, verified against the corpus, not new): the established gauge automorphisms
  act on the INTERNAL representation space and as the IDENTITY on any family slot (the C^N
  working ansatz, item2_family_index_v1.py, flagged there as imported). So the gauge
  quotient does NOT cut family-graph Theta-directions at all; the group that cuts them is
  the FAMILY GRAPH'S OWN declared symmetry. The sector census is therefore an EDGE-ORBIT
  census under that graph symmetry — machinery built here.

CENSUS RULE (from the Theta-direction census, formal/InfoThetaEdgeCensus_attempt.v):
  independent Theta-directions = edges. Under a declared vertex symmetry group H, the
  directions that survive as INDEPENDENT INVARIANT parameters = edge-ORBITS of H (an
  H-invariant admissible operator must give every edge in one orbit the same weight —
  checked exactly below; dimension of the invariant weight space = number of edge-orbits).

RDI COUNT + THE STRUCTURAL FINDING (proven exactly here; Coq witness for the two 3-vertex
  cases in formal/InfoThetaSectorSpectrum_attempt.v):
  - K3 (complete graph, 3 vertices) under its full symmetry S3: ONE edge-orbit -> one
    invariant direction w; spectrum of the invariant operator = {0, 3w, 3w} — DEGENERATE
    for every w. This re-derives item1 Attempt 10's negative result at the census level:
    the symmetric complete topology structurally cannot give 3 distinct levels.
  - P3 (path 0-1-2) under its full symmetry Z2 (end swap): ONE edge-orbit -> one invariant
    direction w; spectrum = {0, w, 3w} — THREE DISTINCT levels for every w > 0.
  ==> the distinguishing power lives in the TOPOLOGY, not in breaking the symmetry or
  adding parameters: a path gives 3 distinct spectral levels from a single invariant
  parameter; the complete/cyclic topology cannot (C3 = K3 at n=3). This is the exact
  structural content behind DISCRETE_MASS_ITEM1_PLAN.md's "reduction lever" (P3 -> {0,1,3}),
  now census-grounded and (for these two instances) machine-checked.

WHAT THIS DOES NOT ESTABLISH (CRRC guard, binding):
  - That P3 (or any graph) IS the family structure, that its 3 levels ARE 3 generations,
    or that n=3 vertices is forced. The identification "spectral level <-> generation"
    is an unbuilt admissibility square. This file only builds the census machinery and
    the structural facts any future candidate must be measured against.
  - Nothing about which topology the ROOT forces — that is named next step 5.2.
  - The empirical per-sector shape constraint (up/lepton decelerate, down accelerates —
    CONTINUUM_ARC_ERROR_NOTE lesson 3) is NOT tested here; single-parameter uniform
    spectra have fixed ratios (P3: 3:1) and would need per-sector structure to vary —
    recorded as the known hard target, untouched.

Tier: census machinery + spectra = exact/finite_diagnostic here; the two 3-vertex spectrum
      facts are Th_coqc via the companion Coq file; interpretations = Dr.

Run: python3 theta_sector_census_v1.py   (stdlib only; exact Fractions)
"""

from fractions import Fraction as Fr
from itertools import combinations, permutations

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


def edge_orbits(n, edges, group):
    """Orbits of the edge set under a vertex-permutation group (exact, brute force)."""
    edges = [tuple(sorted(e)) for e in edges]
    seen, orbits = set(), []
    for e in edges:
        if e in seen:
            continue
        orb = set()
        for g in group:
            img = tuple(sorted((g[e[0]], g[e[1]])))
            orb.add(img)
        orbits.append(sorted(orb))
        seen |= orb
    return orbits


def laplacian(n, wmap):
    L = [[Fr(0)] * n for _ in range(n)]
    for (i, j), w in wmap.items():
        L[i][i] += w
        L[j][j] += w
        L[i][j] -= w
        L[j][i] -= w
    return L


def mat_vec(L, v):
    return [sum(L[i][j] * v[j] for j in range(len(v))) for i in range(len(v))]


def is_eigen(L, v, lam):
    return mat_vec(L, v) == [lam * x for x in v]


def perm_invariant(L, g):
    n = len(L)
    return all(L[g[i]][g[j]] == L[i][j] for i in range(n) for j in range(n))


print("== 0. Scoping fact: gauge cuts nothing on the family slot ==")
print("""  Verified against item2_family_index_v1.py (Attempt 1): every gauge automorphism h
  acts on V_R and as the IDENTITY on the family slot C^N (the imported working ansatz,
  flagged there). Under readout equivalence (master 1.2: O(hX)=O(X) => h is internal
  renaming), the gauge quotient identifies NO two family-graph edge-directions.
  ==> the cutting group for the Theta family census is the FAMILY GRAPH'S OWN declared
  symmetry group H, not the gauge group. (Dr-tier scoping, resting on the same imported
  ansatz — inherited caveat, not new.)""")

print("== 1. Edge-orbit census machinery (exact, brute force over the full group) ==")
# K3 under S3 (full symmetric group on 3 vertices)
S3 = [dict(enumerate(p)) for p in permutations(range(3))]
K3_edges = list(combinations(range(3), 2))
orb_K3 = edge_orbits(3, K3_edges, S3)
ck("K3 under S3: exactly ONE edge-orbit (all 3 edges identified)",
   len(orb_K3) == 1 and len(orb_K3[0]) == 3, orb_K3)

# P3 (path 0-1-2) under Aut(P3) = {id, swap(0,2)}
Z2 = [{0: 0, 1: 1, 2: 2}, {0: 2, 1: 1, 2: 0}]
P3_edges = [(0, 1), (1, 2)]
orb_P3 = edge_orbits(3, P3_edges, Z2)
ck("P3 under Z2: exactly ONE edge-orbit (both edges identified)",
   len(orb_P3) == 1 and len(orb_P3[0]) == 2, orb_P3)

# invariance forces per-orbit equal weights: an H-invariant admissible L must satisfy
# L[g(i)][g(j)] == L[i][j]; check that unequal weights on one orbit break invariance,
# and equal weights restore it (exact, both graphs):
w_uneq = laplacian(3, {(0, 1): Fr(1), (1, 2): Fr(2)})
ck("P3: UNEQUAL weights on the single orbit break Z2-invariance (exact)",
   not perm_invariant(w_uneq, Z2[1]))
w_eq = laplacian(3, {(0, 1): Fr(5, 7), (1, 2): Fr(5, 7)})
ck("P3: equal weights are Z2-invariant (exact)",
   all(perm_invariant(w_eq, g) for g in Z2))
k_uneq = laplacian(3, {(0, 1): Fr(1), (0, 2): Fr(1), (1, 2): Fr(3)})
ck("K3: unequal weights on the single orbit break S3-invariance (exact)",
   not all(perm_invariant(k_uneq, g) for g in S3))
k_eq = laplacian(3, {(0, 1): Fr(2, 3), (0, 2): Fr(2, 3), (1, 2): Fr(2, 3)})
ck("K3: equal weights are S3-invariant (exact)",
   all(perm_invariant(k_eq, g) for g in S3))
print("""  ==> RDI COUNT: after the symmetry quotient, BOTH candidate topologies retain exactly
  ONE independent invariant Theta-direction (one edge-orbit each). Same retained-parameter
  budget — the spectra below differ by TOPOLOGY alone.""")

print("== 2. Spectra of the invariant operators (exact eigenvector witnesses) ==")
w = Fr(5, 7)  # arbitrary positive rational; results hold for every w > 0 (Coq: general w)
LK = laplacian(3, {(0, 1): w, (0, 2): w, (1, 2): w})
ck("K3(w): (1,1,1) is eigenvector for 0", is_eigen(LK, [Fr(1)] * 3, Fr(0)))
ck("K3(w): (1,-1,0) is eigenvector for 3w", is_eigen(LK, [Fr(1), Fr(-1), Fr(0)], 3 * w))
ck("K3(w): (1,0,-1) is eigenvector for 3w (independent) -> DEGENERATE {0,3w,3w}",
   is_eigen(LK, [Fr(1), Fr(0), Fr(-1)], 3 * w))

LP = laplacian(3, {(0, 1): w, (1, 2): w})
ck("P3(w): (1,1,1) is eigenvector for 0", is_eigen(LP, [Fr(1)] * 3, Fr(0)))
ck("P3(w): (1,0,-1) is eigenvector for w", is_eigen(LP, [Fr(1), Fr(0), Fr(-1)], w))
ck("P3(w): (1,-2,1) is eigenvector for 3w", is_eigen(LP, [Fr(1), Fr(-2), Fr(1)], 3 * w))
ck("P3(w): three DISTINCT levels 0 < w < 3w for w > 0 (exact)",
   Fr(0) < w < 3 * w)


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


# completeness (added per independent review): 3 spanning eigenvectors in dim 3 exhaust
# the spectrum — checked by exact determinant, so "spectrum = {...}" is earned, not
# membership-only.
ck("K3: the three eigenvectors SPAN (det=3 != 0) -> {0,3w,3w} is the ENTIRE spectrum",
   det3([[1, 1, 1], [1, -1, 0], [1, 0, -1]]) == 3)
ck("P3: the three eigenvectors SPAN (det=-6 != 0) -> {0,w,3w} is the ENTIRE spectrum",
   det3([[1, 1, 1], [1, 0, -1], [1, -2, 1]]) == -6)
print("""  ==> STRUCTURAL FINDING (census-grounded; 3-vertex instances Th_coqc in the companion
  Coq file): with the SAME retained-parameter budget (one invariant direction), the path
  topology P3 yields THREE distinct spectral levels {0, w, 3w}; the complete topology K3
  yields only TWO {0, 3w(x2)} — degenerate for every w. Distinguishing power lives in
  TOPOLOGY, not in symmetry breaking or extra parameters. Re-derives item1 Attempt 10's
  negative (K3/S3 forced degeneracy) as the orbit-census special case, and grounds the
  DISCRETE_MASS_ITEM1_PLAN 'reduction lever' (P3 -> {0,1,3} at w=1) structurally.""")

print("== 3. What a family-candidate graph must now clear (recorded gates, not tested) ==")
print("""  G1 >=3 distinct spectral levels from invariant directions (P3 passes, K3/C3 fail).
  G2 per-sector-distinct spectra with BOTH hierarchy shapes (up/lepton decelerate, down
     accelerates) — a single uniform-parameter spectrum has FIXED ratios (P3: 3:1),
     so per-sector structure must differ; hard target, untouched here.
  G3 the CP gate (item 2 Attempt 3): the structure must retain a CP-odd signed readout
     (conditional N >= 3, machine-checked).
  G4 root-forcing: WHICH topology the root forces is step 5.2 — nothing here forces P3.""")

print()
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS (exact arithmetic throughout; no floats anywhere)")
