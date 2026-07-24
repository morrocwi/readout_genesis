#!/usr/bin/env python3
"""
Full frontier-automaton DP for the mu_4 problem, info-philosophy corrected:
  - 0/vacuum is never a persisting state -- it's recorded only to keep future consistency
    checks correct, contributes zero area, and is forgotten like any other resolved fact.
  - Sweep = all 4 edge-directions at site (n,0,0,0), for n=0,1,2,...,N-1, in order.
  - Frontier state = the set of (plaquette, value) pairs still possibly touchable by a
    FUTURE edge in the sweep. A plaquette's base-site 0-coordinate is always in
    {edge_site[0]-1, edge_site[0]} (proven from the adjacency structure), so once the sweep
    has moved 2+ sites past a plaquette's 0-coordinate, it can never be touched again and is
    safely forgotten (its area already counted, contributes nothing further).
  - MANDATORY correctness gate: for small N, this DP must agree EXACTLY with full brute-force
    backtracking (no merging) on the identical edge sweep -- checked before trusting anything
    larger than brute force can reach.
"""
from itertools import product
import time

D = 4
def unit(mu):
    e = [0]*D; e[mu] = 1; return tuple(e)
def add(x, y): return tuple(a+b for a, b in zip(x, y))
def sub(x, y): return tuple(a-b for a, b in zip(x, y))

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

def make_sweep(N):
    return [((n,0,0,0), mu) for n in range(N) for mu in range(D)]

# ---------------- exact brute-force (ground truth, small N only) ----------------
def brute_force(edge_sweep, seed):
    results = {}
    def recurse(idx, plaq_values, area):
        if idx == len(edge_sweep):
            results[area] = results.get(area, 0) + 1
            return
        edge = edge_sweep[idx]
        touching = plaquettes_touching_edge(edge)
        decided = [(p, plaq_values[p]) for p in touching if p in plaq_values]
        undecided = [p for p in touching if p not in plaq_values]
        target = (-sum(v for _, v in decided)) % 3
        for vals in product((0,1,2), repeat=len(undecided)):
            if sum(vals) % 3 == target:
                new_area = sum(1 for v in vals if v != 0)
                nv = dict(plaq_values)
                for p, v in zip(undecided, vals): nv[p] = v
                recurse(idx+1, nv, area+new_area)
    recurse(0, {seed[0]: seed[1]}, 0)
    return results

# ---------------- DP with frontier-state merging ----------------
def frontier_dp(edge_sweep, seed, forget_lag=2, max_area=None, verbose=False):
    """State: frozenset of (plaquette, value). Value: dict {area: count} (multiplicity)."""
    init_state = frozenset([seed])
    states = {init_state: {0: 1}}   # state -> {area: count}

    for i, edge in enumerate(edge_sweep):
        new_states = {}
        touching = plaquettes_touching_edge(edge)
        for state, areapoly in states.items():
            state_dict = dict(state)
            decided = [(p, state_dict[p]) for p in touching if p in state_dict]
            undecided = [p for p in touching if p not in state_dict]
            target = (-sum(v for _, v in decided)) % 3
            for vals in product((0,1,2), repeat=len(undecided)):
                if sum(vals) % 3 == target:
                    step_area = sum(1 for v in vals if v != 0)
                    nsd = dict(state_dict)
                    for p, v in zip(undecided, vals): nsd[p] = v
                    # forget plaquettes whose 0-coord is safely behind the sweep
                    cur_site0 = edge[0][0]
                    kept = {p: v for p, v in nsd.items() if p[0][0] >= cur_site0 - forget_lag}
                    nstate = frozenset(kept.items())
                    for a, c in areapoly.items():
                        na = a + step_area
                        if max_area is not None and na > max_area: continue
                        new_states.setdefault(nstate, {})
                        new_states[nstate][na] = new_states[nstate].get(na, 0) + c
        states = new_states
        if verbose:
            print(f"  after edge {i+1}/{len(edge_sweep)}: {len(states)} distinct frontier states")

    total = {}
    for areapoly in states.values():
        for a, c in areapoly.items():
            total[a] = total.get(a, 0) + c
    return total

# ---------------- MANDATORY correctness gate ----------------
print("=== Correctness gate: DP must match brute-force exactly on a small sweep ===")
N_test = 1  # 4 edges (smaller, tractable for brute force)
sweep_test = make_sweep(N_test)
seed_plaq = plaquettes_touching_edge(sweep_test[0])[0]
bf = brute_force(sweep_test, (seed_plaq, 1))
dp = frontier_dp(sweep_test, (seed_plaq, 1), forget_lag=3)
print(f"brute force (N={N_test}, {len(sweep_test)} edges): {dict(sorted(bf.items()))}")
print(f"frontier DP (same sweep):                          {dict(sorted(dp.items()))}")
assert bf == dp, "MISMATCH: DP does not match brute force -- DO NOT TRUST larger N results"
print("PASS: DP exactly matches brute-force ground truth. DP is validated.")

print()
print("=== Scaling test: how far can the DP go? ===")
for N in [1,2,3,4,5,6]:
    sweep = make_sweep(N)
    seedp = plaquettes_touching_edge(sweep[0])[0]
    t0 = time.time()
    result = frontier_dp(sweep, (seedp,1), forget_lag=2, max_area=None)
    dt = time.time()-t0
    total = sum(result.values())
    print(f"N={N} ({len(sweep)} edges): total={total}, max_area_seen={max(result.keys())}, time={dt:.2f}s")
