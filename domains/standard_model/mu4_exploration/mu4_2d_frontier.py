#!/usr/bin/env python3
"""
2D cross-section frontier sweep, matching v1.1's own definition: "Restricted single-sheet
sector (height h=(y,z) in Z^2)". D=3 sub-lattice (t,y,z) -- the w-direction is excluded
entirely (the "single-sheet" restriction), so each edge touches only 4 plaquettes (not 6),
with 3 undecided slots per closure (not 5) -- a genuinely smaller, well-defined sub-problem.

Sweep: layer by layer in t; within a layer, all edges at all (y,z) in a bounded window
[-H,H]x[-H,H], each of the 2 remaining directions (t is direction 0, so within-layer edges
are direction 1 (y) and... wait we also need t-direction edges connecting layer t to t+1.
Edge directions available: 0=t, 1=y, 2=z.

Forgetting: a plaquette (x,a,b) with a,b in {0,1,2} has t-coordinate in {x[0], x[0]+1}
(if 0 in {a,b}) or exactly x[0] (if 0 not in {a,b}). Either way, once the sweep has fully
finished layer t=x[0]+1, the plaquette can never be touched again -- safe to forget.
"""
import time, resource
from itertools import product

DIM = 3  # t,y,z only (w excluded -- the "single-sheet" restriction)

def unit(mu):
    e=[0]*DIM; e[mu]=1; return tuple(e)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
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

def make_2d_sweep(N, H):
    """N layers in t=0..N-1, each layer visits all (y,z) in [-H,H]^2, edge directions y,z
    within the layer, plus one t-direction edge per (y,z) column connecting to the next layer."""
    sweep = []
    for t in range(N):
        for y in range(-H, H+1):
            for z in range(-H, H+1):
                sweep.append(((t,y,z), 1))  # y-direction edge
                sweep.append(((t,y,z), 2))  # z-direction edge
                sweep.append(((t,y,z), 0))  # t-direction edge (connects to t+1)
    return sweep

def brute_force(edge_sweep, seed, cap=2_000_000):
    results = {}
    count = [0]
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
                count[0]+=1
                if count[0] > cap:
                    raise RuntimeError("brute force cap exceeded -- aborting")
                new_area = sum(1 for v in vals if v!=0)
                nv = dict(plaq_values)
                for p,v in zip(undecided,vals): nv[p]=v
                recurse(idx+1, nv, area+new_area)
    recurse(0, {seed[0]:seed[1]}, 0)
    return results

def frontier_dp(edge_sweep, seed, forget_before_t, max_states=50000):
    states = {frozenset([seed]): {0:1}}
    for i, edge in enumerate(edge_sweep):
        touching = plaquettes_touching_edge(edge)
        new_states = {}
        for state, areapoly in states.items():
            sd = dict(state)
            decided = [(p, sd[p]) for p in touching if p in sd]
            undecided = [p for p in touching if p not in sd]
            target = (-sum(v for _,v in decided)) % 3
            for vals in product((0,1,2), repeat=len(undecided)):
                if sum(vals) % 3 == target:
                    step_area = sum(1 for v in vals if v!=0)
                    nsd = dict(sd)
                    for p,v in zip(undecided,vals): nsd[p]=v
                    kept = {p:v for p,v in nsd.items() if p[0][0] >= forget_before_t(edge)}
                    nstate = frozenset(kept.items())
                    for a,c in areapoly.items():
                        na = a+step_area
                        new_states.setdefault(nstate, {})
                        new_states[nstate][na] = new_states[nstate].get(na,0)+c
        states = new_states
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
        print(f"  edge {i+1}/{len(edge_sweep)} {edge}: {len(states)} states, RSS={rss:.1f}MB", flush=True)
        if len(states) > max_states:
            print(f"  SAFETY CAP HIT -- stopping"); return states, False
    return states, True

# ---- validation: smallest case, H=0 (single column), N=1 ----
print("=== validation: H=0, N=1 (3 edges: y,z,t at the single site) ===")
sweep = make_2d_sweep(1, 0)
print("sweep:", sweep)
seedp = plaquettes_touching_edge(sweep[0])[0]
bf = brute_force(sweep, (seedp,1))
print("brute force:", dict(sorted(bf.items())))
dp,_ = frontier_dp(sweep, (seedp,1), forget_before_t=lambda e: -999)  # no forgetting, must match exactly
print("DP (no forgetting):", dict(sorted({a:sum(v.get(a,0) for v in [{}]) for a in bf}.items())) if False else "")
total_dp = {}
for st, poly in {frozenset([seedp,1]):None}.items() if False else []:
    pass
