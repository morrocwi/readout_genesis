#!/usr/bin/env python3
"""
GLOBAL reframing (information-hierarchy, not local generative simulation):
Closed admissible surfaces are n in C_2(K;Z_3) with boundary_2(n)=0 -- i.e. n in
Ker(boundary_2), a LINEAR SUBSPACE (a linear code over GF(3)), not a tree grown edge by edge.
No local branching, no non-terminating process, no lattice-coordinate state explosion --
just linear algebra over GF(3) on a finite window. mu_4 relates to the exponential growth
rate of |Ker| and its weight (area) distribution as the window grows.
"""
import numpy as np
from itertools import product

D = 4
def unit(mu):
    e=[0]*D; e[mu]=1; return tuple(e)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))

def plaquette_verts_edges(x, mu, nu):
    """The 4 boundary edges of plaquette (x,mu,nu), WITH SIGN (orientation), for a genuine
    boundary_2 map: d2(x,mu,nu) = e(x,mu) + e(x+e_mu,nu) - e(x+e_nu,mu) - e(x,nu)."""
    return [ ((x,mu), +1), ((add(x,unit(mu)),nu), +1), ((add(x,unit(nu)),mu), -1), ((x,nu), -1) ]

def window_plaquettes(R):
    """All plaquettes (x,mu,nu) with all coords of x in [0,R], mu<nu."""
    plaqs = []
    coords = range(0, R+1)
    for x in product(coords, repeat=D):
        for mu in range(D):
            for nu in range(mu+1, D):
                plaqs.append((x, mu, nu))
    return plaqs

def window_edges(plaqs):
    edges = set()
    for p in plaqs:
        for e, s in plaquette_verts_edges(*p):
            edges.add(e)
    return sorted(edges)

def build_boundary_matrix(R):
    plaqs = window_plaquettes(R)
    edges = window_edges(plaqs)
    eidx = {e:i for i,e in enumerate(edges)}
    M = np.zeros((len(edges), len(plaqs)), dtype=np.int64)
    for j, p in enumerate(plaqs):
        for e, s in plaquette_verts_edges(*p):
            if e in eidx:
                M[eidx[e], j] = (M[eidx[e], j] + s) % 3
    return M, plaqs, edges

def gf3_rank_and_kernel_basis(M):
    """Gaussian elimination over GF(3). Returns rank and a basis for the (right) kernel."""
    A = M.copy() % 3
    rows, cols = A.shape
    pivot_cols = []
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i,c] % 3 != 0:
                piv = i; break
        if piv is None: continue
        A[[r,piv]] = A[[piv,r]]
        inv = {1:1, 2:2}[A[r,c] % 3]  # GF(3) inverses: 1->1, 2->2
        A[r] = (A[r] * inv) % 3
        for i in range(rows):
            if i != r and A[i,c] % 3 != 0:
                A[i] = (A[i] - A[i,c]*A[r]) % 3
        pivot_cols.append(c)
        r += 1
        if r == rows: break
    rank = r
    free_cols = [c for c in range(cols) if c not in pivot_cols]
    basis = []
    for fc in free_cols:
        v = np.zeros(cols, dtype=np.int64)
        v[fc] = 1
        for i, pc in enumerate(pivot_cols):
            v[pc] = (-A[i, fc]) % 3
        basis.append(v)
    return rank, basis, len(free_cols)

print("=== building the boundary_2 matrix and its GF(3) kernel, small windows ===")
for R in [1, 2]:
    M, plaqs, edges = build_boundary_matrix(R)
    print(f"R={R}: {len(plaqs)} plaquettes, {len(edges)} edges, matrix shape {M.shape}")
    rank, basis, nullity = gf3_rank_and_kernel_basis(M)
    print(f"  rank={rank}, nullity(kernel dim)={nullity}, |Ker|=3^{nullity}={3**nullity}")

print()
print("=== R=1: EXACT weight (area) distribution of the full kernel (2187 elements) ===")
M, plaqs, edges = build_boundary_matrix(1)
rank, basis, nullity = gf3_rank_and_kernel_basis(M)
print(f"kernel dimension = {nullity}, enumerating all {3**nullity} elements exactly...")

weight_dist = {}
basis_arr = np.array(basis)  # shape (nullity, num_plaquettes)
for coeffs in product((0,1,2), repeat=nullity):
    v = np.zeros(basis_arr.shape[1], dtype=np.int64)
    for c, b in zip(coeffs, basis_arr):
        if c: v = (v + c*b) % 3
    w = int(np.count_nonzero(v))
    weight_dist[w] = weight_dist.get(w,0) + 1

print("weight distribution (area -> count):")
for w in sorted(weight_dist):
    print(f"  area={w}: {weight_dist[w]}")
print(f"  total = {sum(weight_dist.values())} (must equal 3^{nullity}={3**nullity})")
assert sum(weight_dist.values()) == 3**nullity

def evalpoly(d, z): return sum(c*z**k for k,c in d.items())
print()
print("evaluate at v1.1's/v1.2's critical z values for comparison:")
for z, label in [(0.2580558725, "v1.1 z_c (mu=3.875)"), (0.1411, "v1.2 z_c approx (mu=7.084)")]:
    print(f"  z={z} ({label}): G(z)={evalpoly(weight_dist,z):.6g}")
