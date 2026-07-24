#!/usr/bin/env python3
"""Extract the per-layer growth factor Lambda(z) from the now-bounded, periodic quotiented DP,
and solve Lambda(z_c)=1 for the critical fugacity -> mu = 1/z_c."""
exec(open('mu4_quotient_dp.py').read().split("# ---- MANDATORY")[0])

def frontier_dp_quotiented_tracked(edge_sweep, seed, forget_before_t, layer_size, max_states=50000):
    """Same as frontier_dp_quotiented but returns the state dict at the END of every layer."""
    states = {canonicalize({seed[0]: seed[1]}, edge_sweep[0][0]): {0: 1}}
    prev_ref_site = edge_sweep[0][0]
    layer_snapshots = []
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
        if len(states) > max_states:
            return layer_snapshots, False
        if (i+1) % layer_size == 0:
            total = {}
            for poly in states.values():
                for a,c in poly.items(): total[a] = total.get(a,0)+c
            layer_snapshots.append(total)
    return layer_snapshots, True

N = 8
sweep = make_2d_sweep(N, 0)
seedp = plaquettes_touching_edge(sweep[0])[0]
snaps, ok = frontier_dp_quotiented_tracked(sweep, (seedp,1), forget_before_t=lambda e: e[0][0]-1, layer_size=3, max_states=40000)
print(f"completed={ok}, {len(snaps)} layer snapshots")

def evalpoly(d, z): return sum(c*z**k for k,c in d.items())

print()
print("layer-boundary totals and per-layer growth ratio, at several z:")
for z in (0.05, 0.1, 0.15, 0.2, 0.25, 0.258, 0.3):
    vals = [evalpoly(s, z) for s in snaps]
    ratios = [vals[i+1]/vals[i] for i in range(len(vals)-1) if vals[i] > 0]
    print(f"  z={z}: G(z) per layer = {[f'{v:.4g}' for v in vals]}")
    print(f"         ratios = {[f'{r:.6f}' for r in ratios]}")
