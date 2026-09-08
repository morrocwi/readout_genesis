#!/usr/bin/env python3
"""
SHARED READOUT <=> SHARED RETAINED STRUCTURE — finite_diagnostic companion to
formal/InfoSharedReadoutForcesSharedMemory_attempt.v (Face XI as an iff), 2026-08-29.

Exact rational arithmetic throughout (Fractions; no floats, no numpy). Fail-able.

WHAT IT CHECKS (three squares, all finite, all exact):

  (1) FACE XI, BOTH DIRECTIONS, AS ARITHMETIC — the Coq file's own witnesses re-run:
      two systems with the same tau_c = M/D return the same discrete decay readout
      ratio = 1 - dt*(D/M) at EVERY dt; two systems with different tau_c return
      different readouts at ANY dt != 0 (one reading suffices); the readout retains
      NOTHING finer than tau_c (M is not recoverable from it).

  (2) SAME RETAINED COMPONENT => SAME SPECTRAL READOUT: for a weighted graph Laplacian
      L_R = D_W - W, the characteristic polynomial (computed EXACTLY by Faddeev-
      LeVerrier over Q) is invariant under every relabeling of the vertices. Two
      readers who differ only in how they label the same retained structure read the
      same invariant — the discrete form of "under the same sky, g reads the same".

  (3) DIFFERENT RETAINED STRUCTURE => DIFFERENT READOUT, AND A DISCONNECTED PIECE READS
      ITS OWN ZERO: the three n=4 living support shapes the Theta program found
      (star, P4 path, 4-cycle; theta_minimal_living_v1.py) with unit weights have
      pairwise DISTINCT characteristic polynomials; an isolated vertex contributes an
      exact factor x (its own zero mode) — a reader on the dead component reads only 0.

WHAT IT DOES NOT ESTABLISH (binding): any physical identification of `ratio` or of the
spectrum with a measured constant (Dr); anything about c, h, Lambda, alpha, the CMB, or
Earth gravity (the external analogy that seeded the question contributed no evidence —
see the Coq file's LINEAGE block); any generation/Theta identification (CRRC guard —
the n=4 shapes are used only as concrete graphs). Unit weights in (3) are a declared
choice, not the Theta program's R2 stationary weights. Tier: finite_diagnostic.

Run: python3 scripts/shared_readout_component_check.py
"""
from fractions import Fraction as F
from itertools import permutations

FAILS = []


def check(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- (1) Face XI iff
print("== (1) Face XI both directions, exact ==")


def tau_c(M, D):
    return F(M) / F(D)


def ratio(M, D, dt):
    return 1 - F(dt) * (F(D) / F(M))


same_tau = [(2, 1), (4, 2), (6, 3), (F(1, 2), F(1, 4))]
dts = [F(1, 10), F(1, 3), 1, 7, F(-2, 5)]
check("forward: equal tau_c => equal readout at every dt (4 systems x 5 steps)",
      all(ratio(M, D, dt) == ratio(2, 1, dt) for (M, D) in same_tau for dt in dts))
diff_tau = [(2, 1), (3, 1), (2, 3), (5, 2)]
check("converse: different tau_c => different readout at ANY single dt != 0",
      all(ratio(a[0], a[1], dt) != ratio(b[0], b[1], dt)
          for a in diff_tau for b in diff_tau if tau_c(*a) != tau_c(*b) for dt in dts))
check("dt = 0 reads nothing (every system returns 1) — the excluded non-readout",
      all(ratio(M, D, 0) == 1 for (M, D) in diff_tau + same_tau))
check("limit: readout retains tau_c only — (2,1) and (4,2) indistinguishable, M differs",
      all(ratio(2, 1, dt) == ratio(4, 2, dt) for dt in dts) and 2 != 4)


# ---------------------------------------------------------------- exact Laplacian tools
def laplacian(n, wedges):
    L = [[F(0)] * n for _ in range(n)]
    for (i, j), w in wedges.items():
        w = F(w)
        L[i][i] += w
        L[j][j] += w
        L[i][j] -= w
        L[j][i] -= w
    return L


def charpoly(A):
    """Faddeev-LeVerrier, exact over Q. Returns coefficients c_n..c_0 of det(xI - A)."""
    n = len(A)
    I = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    M = [[F(0)] * n for _ in range(n)]
    coeffs = [F(1)]
    for k in range(1, n + 1):
        # M_k = A*M_{k-1} + c_{k-1} I
        AM = [[sum(A[i][l] * M[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
        M = [[AM[i][j] + coeffs[-1] * I[i][j] for j in range(n)] for i in range(n)]
        AMk = [[sum(A[i][l] * M[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
        c = -sum(AMk[i][i] for i in range(n)) / k
        coeffs.append(c)
    return tuple(coeffs)


def relabel(wedges, perm):
    return {tuple(sorted((perm[i], perm[j]))): w for (i, j), w in wedges.items()}


# ---------------------------------------------------------------- (2) relabeling invariance
print("== (2) same retained component, any labeling => same spectral readout (exact) ==")
n = 4
shapes = {
    "star (1,1,1,3)": {(0, 1): 1, (0, 2): 1, (0, 3): 1},
    "P4 path (1,1,2,2)": {(0, 1): 1, (0, 2): 1, (1, 3): 1},
    "C4 cycle (2,2,2,2)": {(0, 1): 1, (0, 2): 1, (1, 3): 1, (2, 3): 1},
}
# also a non-uniform weighting, so the invariance is not an artifact of unit weights
shapes["C4 non-uniform weights"] = {(0, 1): F(1, 2), (0, 2): 3, (1, 3): F(5, 7), (2, 3): 2}
for name, we in shapes.items():
    base = charpoly(laplacian(n, we))
    check(f"{name}: charpoly identical under all 24 relabelings",
          all(charpoly(laplacian(n, relabel(we, p))) == base for p in permutations(range(n))))
    check(f"{name}: one zero mode exactly (constant term 0, linear term != 0) — connected",
          base[-1] == 0 and base[-2] != 0, base)

# ---------------------------------------------------------------- (3) different structure
print("== (3) different retained structure => different readout; dead piece reads 0 ==")
polys = {k: charpoly(laplacian(n, v)) for k, v in shapes.items() if "non-uniform" not in k}
names = list(polys)
check("star / P4 / C4 (unit weights) have pairwise DISTINCT charpolys",
      all(polys[a] != polys[b] for i, a in enumerate(names) for b in names[i + 1:]),
      polys)
path3_in_4 = {(0, 1): 1, (0, 2): 1}  # the (0,1,1,2) class: vertex 3 isolated
p = charpoly(laplacian(n, path3_in_4))
check("isolated vertex contributes an extra exact zero mode (charpoly has x^2 | p)",
      p[-1] == 0 and p[-2] == 0 and p[-3] != 0, p)
p3 = charpoly(laplacian(3, {(0, 1): 1, (0, 2): 1}))
check("and the living 3-path's readout is unchanged by the dead neighbour (p = x * p3)",
      p[:-1] == p3, (p, p3))
for k, v in polys.items():
    print(f"    {k}: det(xI - L) coeffs = {tuple(str(c) for c in v)}")

print()
print("Tier: finite_diagnostic (exact Q). Companion to the Th_coqc file; no physics constant claimed.")
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS")
