#!/usr/bin/env python3
"""
Exact backtracking surface-counting simulator, info-philosophy corrected:
  - 0 (vacuum / no retained distinction) is NEVER treated as a persisting Markov state --
    it is simply "this plaquette is not part of the surface," full stop. No self-loops.
  - The lattice genuinely has cycles (Delta_p=20, verified) -- so when closing an edge, any
    of its 6 touching plaquettes that were ALREADY decided by an earlier edge in the sweep
    (because the lattice loops back) are used AS-IS (not re-randomized). This is the exact
    mechanism the naive scalar B(z) product ignores.
  - No global "incoming=1" assumption: the true constraint at each edge is
        sum(values of all 6 touching plaquettes) == 0 (mod 3)
    (closed surface, no source j_C on this edge -- prescribed sources can be added later).
    Signs are irrelevant to the k-distribution (Z_3 negation is a bijection on {1,2}), matching
    what surface_upper_automaton_v1_2.py already assumes (it uses plain sums too).

This is EXACT (full enumeration, no approximation) for whatever small bounded edge-sweep is
given -- the only approximation is the FINITE size of the sweep (same honest limitation as
v1.1's finite-strip H=0..4 convergence check).
"""
from itertools import product

D = 4
def unit(mu):
    e = [0]*D; e[mu] = 1; return tuple(e)
def add(x, y): return tuple(a+b for a, b in zip(x, y))
def sub(x, y): return tuple(a-b for a, b in zip(x, y))

def plaquette_edges(x, mu, nu):
    return [(x, mu), (x, nu), (add(x, unit(mu)), nu), (add(x, unit(nu)), mu)]

def plaquettes_touching_edge(edge):
    x, mu = edge
    plaqs = []
    for nu in range(D):
        if nu == mu: continue
        a, b = min(mu, nu), max(mu, nu)
        plaqs.append((x, a, b))
        plaqs.append((sub(x, unit(nu)), a, b))
    seen = set(); out = []
    for p in plaqs:
        if p not in seen:
            seen.add(p); out.append(p)
    return out

def exact_generating_function(edge_sweep, max_area=None):
    """
    Exact backtracking over the given ordered list of edges. Returns a dict {area: count}
    -- the EXACT coefficients of z^area in the true joint generating function for this
    finite edge-sweep, no approximation beyond the sweep's finiteness.
    """
    results = {}  # area -> count of ways

    def recurse(idx, plaq_values, area_so_far):
        if max_area is not None and area_so_far > max_area:
            return
        if idx == len(edge_sweep):
            results[area_so_far] = results.get(area_so_far, 0) + 1
            return
        edge = edge_sweep[idx]
        touching = plaquettes_touching_edge(edge)
        decided = [(p, plaq_values[p]) for p in touching if p in plaq_values]
        undecided = [p for p in touching if p not in plaq_values]
        target = (-sum(v for _, v in decided)) % 3
        # enumerate all Z_3 assignments to `undecided` summing to target (mod 3)
        for vals in product((0, 1, 2), repeat=len(undecided)):
            if sum(vals) % 3 == target:
                new_area = sum(1 for v in vals if v != 0)
                # philosophy check: a plaquette assigned 0 is NOT retained -- do not add it
                # to plaq_values as if it were a real decided fact worth remembering as an
                # active surface element. It IS still "decided" in the sense that future edges
                # touching it must be consistent (still 0), so we DO record it (for
                # consistency across cycles) but it contributes NO area and is not "active."
                new_plaq_values = dict(plaq_values)
                for p, v in zip(undecided, vals):
                    new_plaq_values[p] = v
                recurse(idx + 1, new_plaq_values, area_so_far + new_area)

    recurse(0, {}, 0)
    return results

# ---- sanity check 1: a single edge, with ONE neighbor pre-seeded (the 'incoming' from an
# earlier step in a real sweep), must reproduce v1.2's B(z) exactly ----
origin = (0,0,0,0)
e0 = (origin, 0)
touching0 = plaquettes_touching_edge(e0)
seed_plaquette = touching0[0]

def exact_generating_function_seeded(edge_sweep, seed, max_area=None):
    results = {}
    def recurse(idx, plaq_values, area_so_far):
        if max_area is not None and area_so_far > max_area: return
        if idx == len(edge_sweep):
            results[area_so_far] = results.get(area_so_far, 0) + 1
            return
        edge = edge_sweep[idx]
        touching = plaquettes_touching_edge(edge)
        decided = [(p, plaq_values[p]) for p in touching if p in plaq_values]
        undecided = [p for p in touching if p not in plaq_values]
        target = (-sum(v for _, v in decided)) % 3
        for vals in product((0, 1, 2), repeat=len(undecided)):
            if sum(vals) % 3 == target:
                new_area = sum(1 for v in vals if v != 0)
                new_plaq_values = dict(plaq_values)
                for p, v in zip(undecided, vals):
                    new_plaq_values[p] = v
                recurse(idx + 1, new_plaq_values, area_so_far + new_area)
    recurse(0, {seed[0]: seed[1]}, 0)
    return results

single = exact_generating_function_seeded([e0], (seed_plaquette, 1))
print("single-edge exact result, ONE neighbor pre-seeded incoming=1 (must match v1.2's B(z)):")
print(" ", single)
expected_v12 = {1:5, 2:10, 3:30, 4:25, 5:11}
for k in range(1,6):
    assert single.get(k,0) == expected_v12[k], f"MISMATCH at k={k}: got {single.get(k,0)}, expected {expected_v12[k]}"
print("  PASS: single-edge case (properly seeded) reproduces v1.2's branching polynomial exactly.")

print()
print("=== TWO edges, exact joint generating function vs naive independent product ===")
e1 = (origin, 0)
e2 = (origin, 1)
touching1 = plaquettes_touching_edge(e1)
seed_for_e1 = touching1[0]  # arbitrary neighbor, pre-seeded incoming=1 (start of this local sweep)

joint = exact_generating_function_seeded([e1, e2], (seed_for_e1, 1))
print("EXACT joint (e1 then e2, properly tracking the shared plaquette):")
for k in sorted(joint): print(f"  area={k}: {joint[k]}")
print(f"  total = {sum(joint.values())}")

# naive independent product: convolve B(z) with itself
Bcoeff = {1:5, 2:10, 3:30, 4:25, 5:11}
naive = {}
for k1, c1 in Bcoeff.items():
    for k2, c2 in Bcoeff.items():
        naive[k1+k2] = naive.get(k1+k2, 0) + c1*c2
print("NAIVE independent product B(z)*B(z):")
for k in sorted(naive): print(f"  area={k}: {naive[k]}")
print(f"  total = {sum(naive.values())}")

print()
print(f"exact total = {sum(joint.values())}  vs  naive total = {sum(naive.values())}")
print(f"ratio = {sum(joint.values())/sum(naive.values()):.4f}  (this IS the real overcounting factor)")

# compare at a specific small z to see magnitude of the gap in the generating function itself
def evalpoly(d, z):
    return sum(c * z**k for k, c in d.items())
for z in (0.1, 0.2, 0.25805587):  # last one is v1.1's shortest-path z_c
    print(f"  at z={z}: exact G(z)={evalpoly(joint,z):.6f}  naive B(z)^2={evalpoly(naive,z):.6f}  ratio={evalpoly(joint,z)/evalpoly(naive,z):.6f}")

print()
print("=== DEBUG: is the shared plaquette actually being reused, or is this coincidence? ===")
t1 = set(plaquettes_touching_edge(e1))
t2 = set(plaquettes_touching_edge(e2))
shared_dbg = t1 & t2
print(f"e1 touches: {sorted(t1)}")
print(f"e2 touches: {sorted(t2)}")
print(f"shared: {sorted(shared_dbg)}")
print(f"seed_for_e1 = {seed_for_e1}  (is it the shared one? {seed_for_e1 in shared_dbg})")

# Manually verify by re-deriving G_2(z) two ways: (a) my hand-derived weighted-branch formula,
# (b) the brute force -- if these three (hand-derived, brute-force, naive) all agree, the
# agreement is real, not a bug.
Tn = {1:{'Z':4,'N':1}, 2:{'Z':6,'N':4}, 3:{'Z':12,'N':18}, 4:{'Z':5,'N':20}, 5:{'Z':0,'N':11}}
C0 = {1:0, 2:20, 3:20, 4:30, 5:10}
Bz = {1:5, 2:10, 3:30, 4:25, 5:11}

handderived = {}
for k1 in Tn:
    zcount = Tn[k1]['Z']; ncount = Tn[k1]['N']
    for k2, c in C0.items():
        handderived[k1+k2] = handderived.get(k1+k2,0) + zcount*c
    for k2, c in Bz.items():
        handderived[k1+k2] = handderived.get(k1+k2,0) + ncount*c
print()
print("hand-derived weighted-branch G_2(z) coefficients:")
for k in sorted(handderived): print(f"  area={k}: {handderived[k]}")
print(f"  total = {sum(handderived.values())}")
print(f"  matches brute-force joint exactly? {handderived == joint}")
print(f"  matches naive B(z)^2 exactly? {handderived == naive}")

print()
print("=== CORRECTED: seed e1 with a plaquette that is NOT shared with e2 ===")
non_shared_for_e1 = [p for p in plaquettes_touching_edge(e1) if p not in shared_dbg][0]
print(f"corrected seed_for_e1 = {non_shared_for_e1}  (shared? {non_shared_for_e1 in shared_dbg})")

joint2 = exact_generating_function_seeded([e1, e2], (non_shared_for_e1, 1))
print("CORRECTED exact joint (shared plaquette genuinely free for e1):")
for k in sorted(joint2): print(f"  area={k}: {joint2[k]}")
print(f"  total = {sum(joint2.values())}")
print(f"  matches hand-derived weighted-branch formula exactly? {joint2 == handderived}")
print(f"  matches naive B(z)^2 exactly? {joint2 == naive}")
print(f"  total vs naive total: {sum(joint2.values())} vs {sum(naive.values())}  ratio={sum(joint2.values())/sum(naive.values()):.6f}")

for z in (0.1, 0.2, 0.25805587):
    ej = evalpoly(joint2, z); nj = evalpoly(naive, z)
    print(f"  at z={z}: CORRECTED exact G(z)={ej:.6f}  naive B(z)^2={nj:.6f}  ratio={ej/nj:.6f}")

print()
print("=== Extend to THREE edges (still small enough to brute-force exactly) ===")
e3 = (origin, 2)
t3 = set(plaquettes_touching_edge(e3))
print(f"e3 shares with e1: {sorted(t1 & t3)}")
print(f"e3 shares with e2 (via t2 recomputed): {sorted(set(plaquettes_touching_edge(e2)) & t3)}")

import time
t0 = time.time()
joint3 = exact_generating_function_seeded([e1, e2, e3], (non_shared_for_e1, 1))
print(f"THREE-edge exact joint (took {time.time()-t0:.1f}s):")
for k in sorted(joint3): print(f"  area={k}: {joint3[k]}")
print(f"  total = {sum(joint3.values())}  (naive would be 81^3={81**3})")

naive3 = {}
for k1,c1 in Bcoeff.items():
    for k2,c2 in Bcoeff.items():
        for k3,c3 in Bcoeff.items():
            naive3[k1+k2+k3] = naive3.get(k1+k2+k3,0) + c1*c2*c3
print(f"  naive B(z)^3 total = {sum(naive3.values())}")

for z in (0.1, 0.2, 0.25805587):
    e3v = evalpoly(joint3, z); n3v = evalpoly(naive3, z)
    print(f"  at z={z}: exact-3edge={e3v:.6f}  naive-3edge={n3v:.6f}  ratio={e3v/n3v:.6f}")
