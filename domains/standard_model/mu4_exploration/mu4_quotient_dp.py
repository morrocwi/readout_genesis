#!/usr/bin/env python3
"""
Info-philosophy-native frontier DP: the retained state is NOT absolute (coordinate, Z_3-value)
pairs -- it is the state QUOTIENTED by every symmetry that doesn't change what's actually
retained:
  (1) TRANSLATION quotient: shift every retained coordinate relative to the CURRENT sweep
      position before using it as a state key. Two configurations that are "the same shape,
      just further along the sweep" are the SAME retained state -- this is exactly q_D(F) = F,
      the weld's own requirement that a state's identity commutes with the stepper.
  (2) Z_3-RELABELING quotient: the global rescaling 1<->2 (proven earlier to be a genuine
      symmetry of the closure rule) means a state and its 1<->2-swapped twin are the SAME
      retained distinction. Store the canonical (lexicographically smaller) representative.
Both are symmetries of the retained structure, not the raw coordinate/value data -- exactly
the retained-distinction (delta_R) philosophy applied to engineering, not borrowed lattice-QFT
machinery patched after the fact.
"""
import time, resource
from itertools import product

DIM = 3
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

def make_2d_sweep(N, H):
    sweep = []
    for t in range(N):
        for y in range(-H, H+1):
            for z in range(-H, H+1):
                sweep.append(((t,y,z), 1))
                sweep.append(((t,y,z), 2))
                sweep.append(((t,y,z), 0))
    return sweep

SWAP = {0:0, 1:2, 2:1}

def canonicalize_rel(kept_dict):
    """Like canonicalize but input is ALREADY relative -- only apply the Z_3-swap quotient."""
    rel = tuple(sorted((off, a, b, v) for (off, a, b), v in kept_dict.items()))
    rel_swapped = tuple(sorted((off, a, b, SWAP[v]) for (off, a, b), v in kept_dict.items()))
    return min(rel, rel_swapped)

def canonicalize(kept_dict, ref_site):
    """Quotient by translation (relative to ref_site) AND by the 1<->2 relabeling symmetry."""
    rel = tuple(sorted((sub(p[0], ref_site), p[1], p[2], v) for p, v in kept_dict.items()))
    rel_swapped = tuple(sorted((sub(p[0], ref_site), p[1], p[2], SWAP[v]) for p, v in kept_dict.items()))
    return min(rel, rel_swapped)

def frontier_dp_quotiented(edge_sweep, seed, forget_before_t, max_states=50000):
    # states keyed by CANONICAL (relative-to-prev_ref_site) tuples; track prev_ref_site
    # separately since all states in a round share the same reference frame.
    states = {canonicalize({seed[0]: seed[1]}, edge_sweep[0][0]): {0: 1}}
    prev_ref_site = edge_sweep[0][0]
    for i, edge in enumerate(edge_sweep):
        touching = plaquettes_touching_edge(edge)
        new_states = {}
        ref_site = edge[0]
        shift = sub(prev_ref_site, ref_site)   # old_relative + shift = new_relative
        touching_rel = [(sub(p[0], ref_site), p[1], p[2]) for p in touching]
        for state, areapoly in states.items():
            # reconstruct working dict in the NEW reference frame from the canonical (old-frame) tuple
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
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
        print(f"  edge {i+1}/{len(edge_sweep)} {edge}: {len(states)} QUOTIENTED states, RSS={rss:.1f}MB", flush=True)
        if len(states) > max_states:
            print(f"  SAFETY CAP HIT -- stopping"); return states, False
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

# ---- MANDATORY correctness gate: quotiented DP must give the SAME totals as brute force ----
print("=== correctness gate: quotiented DP vs brute force, H=0, N=2 ===")
sweep = make_2d_sweep(2, 0)
seedp = plaquettes_touching_edge(sweep[0])[0]
bf = brute_force(sweep, (seedp,1))
states, ok = frontier_dp_quotiented(sweep, (seedp,1), forget_before_t=lambda e: e[0][0]-1)
dp_total = {}
for st, poly in states.items():
    for a,c in poly.items(): dp_total[a] = dp_total.get(a,0)+c
print("brute force:", dict(sorted(bf.items())))
print("quotiented DP:", dict(sorted(dp_total.items())))
print("MATCH:", bf == dp_total)
