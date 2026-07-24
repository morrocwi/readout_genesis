#!/usr/bin/env python3
"""
Apply the fusion-grammar technique (tau x tau = 1 + tau -> d_tau=phi, generalized) to our
ALREADY-DERIVED branching polynomial B(z) = 5z+10z^2+30z^3+25z^4+11z^5, treating each closure
as a NODE of a branching tree: node closes, spawns k new "tau" children (k with multiplicity
coeff[k], area cost z^k), each child independently runs the SAME process.

Standard branching-process/tree-counting fixed point:
    Y(z) = sum_k coeff[k] * z^k * Y(z)^k      (Y = generating function of one full subtree)
Criticality (radius of convergence of Y in z) is where BOTH
    Y = phi(z,Y)   and   1 = d(phi)/dY (z,Y)
hold simultaneously (standard singularity analysis for tree/branching generating functions --
NOT simply B(z)=1, which is what v1.2 used as a simplified/different criterion).

Pure algebra, zero lattice simulation, zero memory risk -- a genuinely different, independent
way to probe the same B(z) already validated against the repo's own code.
"""
import numpy as np

coeff = {0:0, 1:5, 2:10, 3:30, 4:25, 5:11}

def phi(z, Y):
    return sum(c * z**k * Y**k for k, c in coeff.items())

def dphi_dY(z, Y):
    return sum(c * k * z**k * Y**(k-1) for k, c in coeff.items() if k >= 1)

# solve the pair {Y = phi(z,Y), 1 = dphi/dY(z,Y)} for (z,Y) simultaneously.
# Strategy: for a candidate z, solve Y = phi(z,Y) for the smallest positive root Y(z)
# (the "physical" branch, Y(0)=0), then check dphi/dY there; bisect on z until it hits 1.

def solve_Y_for_z(z, y0=0.01, iters=200):
    y = y0
    for _ in range(iters):
        y_new = phi(z, y)
        if not (0 <= y_new < 1e6):
            return None
        y = y_new
    return y

def dphi_at_critical(z):
    y = solve_Y_for_z(z)
    if y is None: return None
    return dphi_dY(z, y), y

# scan z to find where dphi/dY crosses 1
print("scanning z for the tree-counting criticality condition dphi/dY = 1:")
zs = np.linspace(0.02, 0.20, 19)
for z in zs:
    r = dphi_at_critical(z)
    if r is None:
        print(f"  z={z:.4f}: fixed-point iteration diverged")
        continue
    dpdy, y = r
    print(f"  z={z:.4f}: Y(z)={y:.6f}  dphi/dY={dpdy:.6f}")
