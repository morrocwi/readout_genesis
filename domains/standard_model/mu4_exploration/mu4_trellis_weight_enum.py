#!/usr/bin/env python3
"""
Trellis-style weight enumerator for Ker(boundary_2) over GF(3), exploiting the LOCALITY of the
kernel basis (verified: support size 6-10 plaquettes, spanning only 1-2 layers, out of a much
larger window) -- process basis vectors in sweep order (by min t-coordinate), track only the
CUMULATIVE partial value on plaquettes still shared with FUTURE basis vectors as DP state.
MANDATORY correctness gate: must reproduce the R=1 exact weight distribution before trusting R=2.
"""
import numpy as np
from itertools import product
import resource

D = 4
def unit(mu):
    e=[0]*D; e[mu]=1; return tuple(e)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))

def plaquette_verts_edges(x, mu, nu):
    return [ ((x,mu), +1), ((add(x,unit(mu)),nu), +1), ((add(x,unit(nu)),mu), -1), ((x,nu), -1) ]

def window_plaquettes(R):
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
        inv = {1:1, 2:2}[A[r,c] % 3]
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

def trellis_weight_enumerator(basis, plaqs, max_states=200000):
    """Process basis vectors (each a length-len(plaqs) GF(3) vector) in an order that keeps
    overlap between 'already processed' and 'not yet processed' bounded. Sweep order: by the
    basis vector's own minimum plaquette t-coordinate.
    State: for each plaquette index still touched by a FUTURE basis vector, its cumulative
    value so far (as a tuple, keyed by plaquette index) -- once a plaquette index is touched by
    NO future basis vector, its FINAL value is known: fold it into area immediately."""
    n = len(basis)
    # precompute each basis vector's support (nonzero plaquette indices)
    supports = [set(np.nonzero(b)[0].tolist()) for b in basis]
    # sweep order: by min plaquette-site t-coordinate touched
    def min_t(i):
        return min(plaqs[j][0][0] for j in supports[i]) if supports[i] else 0
    order = sorted(range(n), key=min_t)

    # for each step, determine which plaquette indices become "final" (no longer touched by
    # any LATER basis vector in the order) right after processing this step
    future_support = [set() for _ in range(n+1)]
    for k in range(n-1, -1, -1):
        future_support[k] = future_support[k+1] | supports[order[k]]
    # future_support[k] = union of supports of order[k], order[k+1], ..., order[n-1]

    states = {(): {0: 1}}   # state = tuple of (plaquette_idx, value) sorted, still "live"
    max_seen = 0
    for k, bi in enumerate(order):
        b = basis[bi]
        sup = supports[bi]
        new_states = {}
        live_after = future_support[k+1]  # what's still needed after this step
        for state, areapoly in states.items():
            sd = dict(state)
            for c in (0,1,2):
                # apply coefficient c to this basis vector, update sd
                nsd = dict(sd)
                for j in sup:
                    nsd[j] = (nsd.get(j,0) + c*int(b[j])) % 3
                # fold any index no longer live into area, keep the rest
                step_area = 0
                kept = {}
                for j, v in nsd.items():
                    if j in live_after:
                        kept[j] = v
                    else:
                        if v != 0: step_area += 1
                nstate = tuple(sorted(kept.items()))
                for a, cnt in areapoly.items():
                    na = a + step_area
                    new_states.setdefault(nstate, {})
                    new_states[nstate][na] = new_states[nstate].get(na,0) + cnt
        states = new_states
        max_seen = max(max_seen, len(states))
        if len(states) > max_states:
            return None, False, max_seen
    # combine all final states (should be just the empty state with everything folded in)
    total = {}
    for st, poly in states.items():
        for a,c in poly.items():
            total[a] = total.get(a,0) + c
    return total, True, max_seen

print("=== MANDATORY gate: trellis weight enumerator must match R=1 exact result ===")
M, plaqs, edges = build_boundary_matrix(1)
rank, basis, nullity = gf3_rank_and_kernel_basis(M)
print(f"R=1: nullity={nullity}")
total, ok, max_states_seen = trellis_weight_enumerator(basis, plaqs)
print(f"trellis result: {dict(sorted(total.items())) if ok else 'FAILED'}")
print(f"max states seen during sweep: {max_states_seen}")
expected = {0:1, 6:16, 10:48, 11:48, 12:96, 14:288, 15:224, 16:342, 17:576, 18:392, 19:96, 20:60}
print(f"expected (from full enumeration): {expected}")
print(f"MATCH: {total == expected}")
