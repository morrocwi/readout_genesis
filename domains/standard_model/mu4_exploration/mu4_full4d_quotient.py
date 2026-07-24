#!/usr/bin/env python3
"""Full 4D (t,y,z,w) symmetry-quotiented frontier DP -- same technique validated in 3D,
now with the genuine w-direction included (6 touching plaquettes/edge, 81-solution local
rule, matching v1.2's TRUE combinatorics). Validated against brute force before scaling."""
import time, resource
from itertools import product

DIM = 4
def unit(mu):
    e=[0]*DIM; e[mu]=1; return tuple(e)
def sub(x,y): return tuple(a-b for a,b in zip(x,y))

def plaquettes_touching_edge(edge):
    x, mu = edge
    plaqs = []
    for nu in range(DIM):
        if nu == mu: continue
        a, b = min(mu,nu), max(mu,nu)
        plaqs.append((x, a, b))
        plaqs.append((sub(x, unit(nu)), a, b))
    seen=set(); out=[]
    for p in plaqs:
        if p not in seen: seen.add(p); out.append(p)
    return out

def make_4d_sweep(N, H):
    """N layers in t=0..N-1; each layer visits (y,z,w) in [-H,H]^3, directions y,z,w,t."""
    sweep = []
    for t in range(N):
        for y in range(-H,H+1):
            for z in range(-H,H+1):
                for w in range(-H,H+1):
                    sweep.append(((t,y,z,w), 1))
                    sweep.append(((t,y,z,w), 2))
                    sweep.append(((t,y,z,w), 3))
                    sweep.append(((t,y,z,w), 0))
    return sweep

SWAP = {0:0, 1:2, 2:1}

def canonicalize_rel(kept_dict):
    rel = tuple(sorted((off, a, b, v) for (off, a, b), v in kept_dict.items()))
    rel_swapped = tuple(sorted((off, a, b, SWAP[v]) for (off, a, b), v in kept_dict.items()))
    return min(rel, rel_swapped)

def canonicalize(kept_dict, ref_site):
    rel = tuple(sorted((sub(p[0], ref_site), p[1], p[2], v) for p, v in kept_dict.items()))
    rel_swapped = tuple(sorted((sub(p[0], ref_site), p[1], p[2], SWAP[v]) for p, v in kept_dict.items()))
    return min(rel, rel_swapped)

def frontier_dp_quotiented(edge_sweep, seed, forget_before_t, max_states=50000, verbose=True):
    states = {canonicalize({seed[0]: seed[1]}, edge_sweep[0][0]): {0: 1}}
    prev_ref_site = edge_sweep[0][0]
    for i, edge in enumerate(edge_sweep):
        touching = plaquettes_touching_edge(edge)
        new_states = {}
        ref_site = edge[0]
        shift = sub(prev_ref_site, ref_site)
        touching_rel = [(sub(p[0], ref_site), p[1], p[2]) for p in touching]
        for state, areapoly in states.items():
            sd = {}
            for (off, a, b, v) in state:
                newoff = tuple(o + s for o, s in zip(off, shift))
                sd[(newoff, a, b)] = v
            decided = [(p, sd[p]) for p in touching_rel if p in sd]
            undecided = [p for p in touching_rel if p not in sd]
            target = (-sum(v for _,v in decided)) % 3
            for vals in product((0,1,2), repeat=len(undecided)):
                if sum(vals) % 3 == target:
                    step_area = sum(1 for v in vals if v!=0)
                    nsd = dict(sd)
                    for p,v in zip(undecided,vals): nsd[p]=v
                    kept = {p:v for p,v in nsd.items() if p[0][0] >= (forget_before_t(edge) - ref_site[0])}
                    canon = canonicalize_rel(kept)
                    for a,c in areapoly.items():
                        na = a+step_area
                        new_states.setdefault(canon, {})
                        new_states[canon][na] = new_states[canon].get(na,0)+c
        states = new_states
        prev_ref_site = ref_site
        if verbose:
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
            print(f"  edge {i+1}/{len(edge_sweep)} {edge}: {len(states)} states, RSS={rss:.1f}MB", flush=True)
        if len(states) > max_states:
            print("  SAFETY CAP HIT -- stopping"); return states, False
    return states, True

def brute_force(edge_sweep, seed):
    results = {}
    def recurse(idx, plaq_values, area):
        if idx == len(edge_sweep):
            results[area] = results.get(area,0)+1
            return
        edge = edge_sweep[idx]
        touching = plaquettes_touching_edge(edge)
        decided = [(p, plaq_values[p]) for p in touching if p in plaq_values]
        undecided = [p for p in touching if p not in plaq_values]
        target = (-sum(v for _,v in decided)) % 3
        for vals in product((0,1,2), repeat=len(undecided)):
            if sum(vals) % 3 == target:
                new_area = sum(1 for v in vals if v!=0)
                nv = dict(plaq_values)
                for p,v in zip(undecided,vals): nv[p]=v
                recurse(idx+1, nv, area+new_area)
    recurse(0, {seed[0]:seed[1]}, 0)
    return results

# ---- validation: single layer, H=0 (4 edges: y,z,w,t) ----
print("=== validation: full 4D, H=0, N=1 (4 edges) ===")
sweep = make_4d_sweep(1, 0)
print("sweep:", sweep)
seedp = plaquettes_touching_edge(sweep[0])[0]
bf = brute_force(sweep, (seedp,1))
print("brute force:", dict(sorted(bf.items())))
states, ok = frontier_dp_quotiented(sweep, (seedp,1), forget_before_t=lambda e: e[0][0]-1)
dp_total = {}
for st, poly in states.items():
    for a,c in poly.items(): dp_total[a] = dp_total.get(a,0)+c
print("quotiented DP:", dict(sorted(dp_total.items())))
print("MATCH:", bf == dp_total)
