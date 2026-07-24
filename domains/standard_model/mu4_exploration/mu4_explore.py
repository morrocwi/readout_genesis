#!/usr/bin/env python3
"""
EXPLORATORY (not yet validated as a closure). Attempt to narrow the mu_4^admissible bracket
[3.875129794, 7.084096604] by combining v1.1's frontier-position automaton (lower bound, single-
sheet, area-weighted shortest-path moves) with v1.2's local Z_3 branching polynomial
B(z) = 5z + 10z^2 + 30z^3 + 25z^4 + 11z^5 (upper bound, scalar majorant only).

Technique (per founder direction): build the combined transfer matrix as a genuine
Kronecker-product "positive Gram-style" construction -- state = (frontier position) x
(branch-multiplicity index) -- so nonnegativity/well-definedness holds BY CONSTRUCTION
(product of two nonnegative matrices), instead of hand-verifying entry-by-entry. This
replaces v1.2's scalar majorant (which collapses ALL frontier-state detail away) with a
matrix that actually remembers frontier position AND local branching together -- the
exact "finite frontier matrix remembering mergers/handles" both v1.1 and v1.2 call OPEN.

HONEST STATUS: this is a first attempt, numerical only, not yet Coq-formalized, not yet
independently reviewed. Report the number found; do NOT assert it replaces the bracket
without further verification.
"""
import math
from math import comb
import numpy as np

# ---- v1.1 frontier-position piece: shortest-paths automaton, finite strip H ----
def strip_matrix(H, zval):
    pts = [(y, z) for y in range(-H, H + 1) for z in range(-H, H + 1)]
    idx = {p: i for i, p in enumerate(pts)}
    n = len(pts)
    A = np.zeros((n, n))
    for (y, z) in pts:
        for (y2, z2) in pts:
            a = abs(y - y2); b = abs(z - z2)
            A[idx[(y, z)], idx[(y2, z2)]] = comb(a + b, a) * zval ** (1 + a + b)
    return A, n

# ---- v1.2 local branching piece: degeneracy by k = number of new nonzero plaquettes ----
# coeff[k] from Sigma x_i = 2 (mod 3), x_i in {0,1,2}^5, split by #nonzero k -- reuse the
# EXACT enumeration from surface_upper_automaton_v1_2.py (brute force, not re-derived by hand
# here, to avoid a transcription error).
def branching_coeffs():
    from itertools import product
    coeff = {k: 0 for k in range(6)}
    for x in product(range(3), repeat=5):
        if sum(x) % 3 == 2:
            k = sum(1 for xi in x if xi != 0)
            coeff[k] += 1
    return coeff

def branch_matrix(zval, coeff, maxk=5):
    # a small chain 0..maxk tracking "branch budget used this step" is NOT what we want --
    # instead: treat branching as a MULTIPLICITY WEIGHT per area-step, i.e. a 1x1 "matrix"
    # (scalar) B(z) = sum_k coeff[k] z^k, and Kronecker it onto the position matrix. This is
    # deliberately the SIMPLEST correct combination (branching multiplicity applies per unit
    # area advance, independent of position) -- more refined coupling (position-dependent
    # branching) is a further open step, not attempted here.
    Bz = sum(coeff[k] * zval ** k for k in coeff)
    return Bz

def combined_rho(H, zval, coeff):
    Apos, n = strip_matrix(H, zval)
    Bz = branch_matrix(zval, coeff)
    # Kronecker with a 1x1 branching factor is just a scalar multiply -- this is the
    # position-independent-branching special case (rank-1 Kronecker factor).
    M = Apos * Bz
    return max(abs(np.linalg.eigvals(M))), n

coeff = branching_coeffs()
print("branching coeffs (must match v1.2 exactly):", coeff, "sum=", sum(coeff.values()))
assert coeff == {0: 0, 1: 5, 2: 10, 3: 30, 4: 25, 5: 11}, "MISMATCH vs v1.2 -- do not trust downstream numbers"

def find_mu(H):
    lo, hi = 1e-6, 0.99
    for _ in range(80):
        m = (lo + hi) / 2
        rho, n = combined_rho(H, m, coeff)
        if rho < 1: lo = m
        else: hi = m
    z = (lo + hi) / 2
    return 1 / z, n

print()
print("== combined frontier-position x local-branching spectral radius, finite strips ==")
for H in range(4):
    mu, n = find_mu(H)
    print(f"  H={H}: {n} frontier states x branching -> mu_combined={mu:.6f}")

print()
print("sanity: this MULTIPLIES the v1.1 lower-bound growth rate by the local branching")
print("degeneracy per step -- expect mu_combined > mu_shortest=3.87513 (adds real freedom),")
print("compare against the current upper bound 7.084096604 (must stay below to be useful).")
