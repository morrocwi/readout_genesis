#!/usr/bin/env python3
"""Safe, incremental scaling test with memory monitoring and a hard state-count cap.
Fully self-contained -- does NOT import the earlier (unsafe, uncapped) script."""
import time, resource
from itertools import product

D = 4
def unit(mu):
    e=[0]*D; e[mu]=1; return tuple(e)
def sub(x,y): return tuple(a-b for a,b in zip(x,y))

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

MAX_STATES = 20000

def frontier_dp_monitored(edge_sweep, seed, forget_lag=2):
    init_state = frozenset([seed])
    states = {init_state: {0: 1}}
    for i, edge in enumerate(edge_sweep):
        touching = plaquettes_touching_edge(edge)
        new_states = {}
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
                    cur_site0 = edge[0][0]
                    kept = {p: v for p, v in nsd.items() if p[0][0] >= cur_site0 - forget_lag}
                    nstate = frozenset(kept.items())
                    for a, c in areapoly.items():
                        na = a + step_area
                        new_states.setdefault(nstate, {})
                        new_states[nstate][na] = new_states[nstate].get(na, 0) + c
        states = new_states
        rss_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
        print(f"  edge {i+1}/{len(edge_sweep)}: {len(states)} frontier states, RSS={rss_mb:.1f}MB", flush=True)
        if len(states) > MAX_STATES:
            print(f"  !!! SAFETY CAP HIT ({MAX_STATES} states) -- STOPPING !!!", flush=True)
            return states, False
    return states, True

for N in [1, 2, 3]:
    print(f"=== N={N} ({N*4} edges) ===", flush=True)
    sweep = make_sweep(N)
    seedp = plaquettes_touching_edge(sweep[0])[0]
    t0 = time.time()
    states, completed = frontier_dp_monitored(sweep, (seedp, 1), forget_lag=2)
    print(f"  completed={completed}, time={time.time()-t0:.2f}s", flush=True)
    if not completed:
        print("  STOPPING further N escalation.", flush=True)
        break
    print()
