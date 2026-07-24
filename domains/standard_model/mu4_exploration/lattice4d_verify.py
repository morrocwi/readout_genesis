#!/usr/bin/env python3
"""
Step 1: build the 4D hypercubic edge/plaquette incidence structure explicitly and brute-force
verify it against the TWO facts already established (and Coq/Python-verified) elsewhere in the
repo, before trusting anything built on top of it:

  FACT A (retained_confinement_certificate_v0_5.py): max degree of the plaquette-adjacency graph
         in 4D is Delta_p = 4*(2*(D-1)-1) = 20  (D=4)
  FACT B (surface_upper_automaton_v1_2.py): each edge touches 6 plaquettes; closing it (1 incoming,
         5 undecided, each in Z_3, sum constraint) has exactly 81 = 3^4 solutions total, split by
         #nonzero k as coeff = {1:5, 2:10, 3:30, 4:25, 5:11}
"""
from itertools import product

D = 4  # dimensions

def unit(mu):
    e = [0]*D; e[mu] = 1; return tuple(e)

def add(x, y):
    return tuple(a+b for a, b in zip(x, y))

def sub(x, y):
    return tuple(a-b for a, b in zip(x, y))

# plaquette identified by (base site x, mu, nu) with mu<nu -- the unit square with corners
# x, x+e_mu, x+e_nu, x+e_mu+e_nu
def plaquette_edges(x, mu, nu):
    # the 4 edges of the square, each as (site, direction)
    return [
        (x, mu),
        (x, nu),
        (add(x, unit(mu)), nu),
        (add(x, unit(nu)), mu),
    ]

def edges_touching_plaquette_of_edge(edge):
    """All plaquettes (x,mu,nu) that contain this edge, for ANY nu != mu (both orderings of base site)."""
    x, mu = edge
    plaqs = []
    for nu in range(D):
        if nu == mu: continue
        a, b = min(mu, nu), max(mu, nu)
        # plaquette anchored at x itself (if mu is the "smaller" or "larger" direction, both matter)
        # Case 1: this edge is the mu-edge of plaquette (x, a, b) directly (x is the base corner)
        if mu == a:
            plaqs.append((x, a, b))
        else:
            plaqs.append((x, a, b))
        # Case 2: this edge is the "opposite" mu-edge of a plaquette shifted by -e_nu
        xshift = sub(x, unit(nu))
        if mu == a:
            plaqs.append((xshift, a, b))
        else:
            plaqs.append((xshift, a, b))
    # dedupe (shouldn't be needed, but be safe)
    seen = set(); out = []
    for p in plaqs:
        if p not in seen:
            seen.add(p); out.append(p)
    return out

# ---- FACT A check: degree of plaquette-adjacency graph (plaquettes sharing an edge) ----
origin = (0,0,0,0)
p0 = (origin, 0, 1)   # a reference plaquette
edges0 = plaquette_edges(*p0)
neighbors = set()
for e in edges0:
    for p in edges_touching_plaquette_of_edge(e):
        if p != p0:
            neighbors.add(p)
print(f"plaquette {p0} has {len(neighbors)} adjacent plaquettes (sharing an edge) -- expect 20")
assert len(neighbors) == 20, f"MISMATCH: got {len(neighbors)}, expected 20 (Delta_p from v0_5)"
print("  PASS: matches Delta_p=20 from retained_confinement_certificate_v0_5.py")

# ---- FACT B check: each edge touches 6 plaquettes ----
e0 = (origin, 0)
touching = edges_touching_plaquette_of_edge(e0)
print(f"edge {e0} touches {len(touching)} plaquettes -- expect 6")
assert len(touching) == 6, f"MISMATCH: got {len(touching)}, expected 6"
print("  PASS: matches 'a 4D edge touches 6 plaquettes' from surface_upper_automaton_v1_2.py")

print()
print("Lattice incidence structure verified consistent with BOTH pre-existing facts.")

print()
print("=== Step 2: do two adjacent edge-closures share a plaquette? ===")
e1 = (origin, 0)
e2 = (origin, 1)
P1 = set(edges_touching_plaquette_of_edge(e1))
P2 = set(edges_touching_plaquette_of_edge(e2))
shared = P1 & P2
print(f"edge {e1} touches: {sorted(P1)}")
print(f"edge {e2} touches: {sorted(P2)}")
print(f"SHARED plaquette(s): {sorted(shared)}")
assert len(shared) >= 1, "expected e1,e2 to share at least the plaquette (origin,0,1)"

print()
print("=== Step 3: the actual correlation the scalar model B(z) misses ===")
from itertools import product as iproduct

P1_list = sorted(P1)   # 6 plaquettes touching e1, in a fixed order
shared_idx_in_P1 = P1_list.index(next(iter(shared)))
print(f"shared plaquette is index {shared_idx_in_P1} of e1's 6 touching plaquettes")

# e1's closure: pick ANY one of the 6 as 'incoming' (fixed=1, canonical), the other 5 free in
# Z_3 subject to sum(free) = 2 (mod 3) [v1.2's own rule]. We must NOT pick the shared plaquette
# as incoming (it must be one of the 5 FREE ones, since it's the one e2 will inherit).
incoming_idx = 0
assert incoming_idx != shared_idx_in_P1
free_slots = [i for i in range(6) if i != incoming_idx]   # 5 slots, includes shared_idx_in_P1
shared_pos_in_free = free_slots.index(shared_idx_in_P1)

completions = []
for x in iproduct((0,1,2), repeat=5):
    if sum(x) % 3 == 2:
        completions.append(x)
assert len(completions) == 81

shared_value_dist = {0:0, 1:0, 2:0}
for x in completions:
    shared_value_dist[x[shared_pos_in_free]] += 1
print(f"among e1's 81 valid completions, the SHARED plaquette gets value: {shared_value_dist}")
print(f"  -> P(shared=0) = {shared_value_dist[0]}/81 = {shared_value_dist[0]/81:.4f}")
print(f"  -> P(shared=1) = {shared_value_dist[1]}/81 = {shared_value_dist[1]/81:.4f}")
print(f"  -> P(shared=2) = {shared_value_dist[2]}/81 = {shared_value_dist[2]/81:.4f}")

print()
print("If v1.2's canonical rule 'incoming=1' is used for e2 regardless of what e1 actually")
print("produced, then whenever shared != 1 (i.e. P(shared=0)+P(shared=2) of the time), e2's")
print("closure is computed with the WRONG incoming value -- the true local rule for e2 in that")
print("branch is 'incoming + sum(new5) = 0 (mod 3)' with incoming in {0,2}, NOT the canonical")
print("'1 + sum(new5) = 0' that gives B(z). This is the exact mechanism of the discrepancy.")

# compute what the TRUE second-step polynomial is for each possible incoming value
def branch_poly_for_incoming(inc):
    coeff = {k:0 for k in range(6)}
    for x in iproduct((0,1,2), repeat=5):
        if (inc + sum(x)) % 3 == 0:
            k = sum(1 for xi in x if xi != 0)
            coeff[k] += 1
    return coeff

for inc in (0,1,2):
    c = branch_poly_for_incoming(inc)
    print(f"  incoming={inc}: branching coeffs = {[c[k] for k in range(1,6)]}  sum={sum(c.values())}")

print()
print("=== Step 4: the MINIMAL retained state (info-philosophy: delta_R, not geometry) ===")
print("Z_3 has a multiplicative symmetry {1,2} <-> {1,2} (mult by 2) that fixes 0 and swaps")
print("1<->2. Since the closure rule only depends on the incoming value THROUGH this symmetry")
print("(verified: incoming=1 and incoming=2 give the IDENTICAL branching polynomial above),")
print("the actual RETAINED DISTINCTION the past must hand the future is NOT 'which of 0,1,2'")
print("but only 'ZERO vs NONZERO' -- a 2-state chain, forced by symmetry, not chosen by us.")
print()

from itertools import product as iproduct

def build_transfer(incoming_is_zero):
    """Returns dict: {k: {next_state: count}} for one edge closure given incoming state."""
    target = 0 if incoming_is_zero else 1   # canonical: incoming=0, or incoming=1 (repr of nonzero)
    out = {}
    for x in iproduct((0,1,2), repeat=5):
        if (target + sum(x)) % 3 == 0:
            k = sum(1 for xi in x if xi != 0)
            next_state = 'Z' if x[0] == 0 else 'N'   # slot 0 = the plaquette handed to the next edge
            out.setdefault(k, {'Z':0, 'N':0})
            out[k][next_state] += 1
    return out

T_from_N = build_transfer(incoming_is_zero=False)   # incoming nonzero (repr by 1; ==2 by symmetry, verified above)
T_from_Z = build_transfer(incoming_is_zero=True)

print("transfer counts FROM nonzero-incoming, by area k, split by next-state:")
for k in sorted(T_from_N): print(f"  k={k}: {T_from_N[k]}")
print("transfer counts FROM zero-incoming, by area k, split by next-state:")
for k in sorted(T_from_Z): print(f"  k={k}: {T_from_Z[k]}")

def M(z):
    # rows/cols ordered [N, Z]
    def entry(Tdict, target):
        return sum(Tdict.get(k, {'Z':0,'N':0})[target] * z**k for k in range(0,6))
    return [
        [entry(T_from_N, 'N'), entry(T_from_N, 'Z')],
        [entry(T_from_Z, 'N'), entry(T_from_Z, 'Z')],
    ]

import numpy as np
def rho(z):
    Mz = np.array(M(z))
    return max(abs(np.linalg.eigvals(Mz)))

lo, hi = 1e-6, 0.99
for _ in range(100):
    m = (lo+hi)/2
    if rho(m) < 1: lo = m
    else: hi = m
zc = (lo+hi)/2
mu2state = 1/zc
print()
print(f"critical z_c = {zc:.9f}")
print(f"2-STATE MARKOV mu = 1/z_c = {mu2state:.9f}")
print(f"compare: v1.1 lower bound (position, single-sheet) = 3.875129794")
print(f"compare: v1.2 scalar-majorant upper bound (naively assumes incoming always symmetric) = 7.084096604")
print(f"is 2-state result inside the bracket? {3.875129794 <= mu2state <= 7.084096604}")
