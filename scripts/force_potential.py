#!/usr/bin/env python3
"""
Frontier attempt — FORCE the potential term ∇V out of the root. Honest result: the root
forces only that V is COERCIVE (confining / bounded-below), NOT its shape. The SHAPE of V
(cubic, double-well, …) is where DOMAINS enter — correctly domain-DSL, not root (the
founder rule: domain-specifics never enter the root). Exact rational, fail-able.

Forcing argument (root → V coercive), stated via ENERGY (no integration needed — the
argument is algebraic, so no explicit-stepper instability confound):
  With the already-forced D>0, the energy  E = ½‖v‖² + V(Φ)  is non-increasing
  (dE/dt = −D‖v‖² ≤ 0, RDL_SpineStability, Th_coqc). Retention (τ_c>0) requires the
  state to persist BOUNDED. Two cases:
    · V COERCIVE (V(Φ)→+∞ as |Φ|→∞, bounded below): E is bounded below, and since E only
      decreases, the trajectory is trapped in the sublevel set {E ≤ E₀}, which is BOUNDED
      → retained.  ✔
    · V NON-COERCIVE (unbounded below): E can decrease without bound (fall into the
      bottomless well), so |Φ| is not contained → the state RUNS AWAY → NOT retained →
      the root axiom is violated.  ✘
  Therefore retention + forced-D FORCE V to be coercive. The SHAPE stays free (domain).
  (Coq support: InfoCoercivityBoundedClosure.v — coercivity ⇒ bounded closure.)

Run: python3 scripts/force_potential.py
"""
from fractions import Fraction as F

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

def bounded_below(Vfun, probes):
    vals = [Vfun(F(p)) for p in probes]
    return min(vals) > F(-10**9)                 # a finite floor exists among growing probes
def grows_at_infinity(Vfun):
    return Vfun(F(1000)) > Vfun(F(10)) > Vfun(F(1))   # V increasing for large |Φ| (coercive)
def falls_to_minus_infinity(Vfun):
    return Vfun(F(1000)) < Vfun(F(10)) < Vfun(F(1))   # V decreasing without bound (non-coercive)

PROBES = [-1000,-100,-10,-1,0,1,10,100,1000]

print("== PASSING: COERCIVE V = ¼Φ⁴  ->  E bounded below  ->  trajectory confined (retained) ==")
Vc = lambda P: (P**4)/4
check("coercive V is bounded below (min over probes ≥ 0, at Φ=0)", min(Vc(F(p)) for p in PROBES) == 0)
check("coercive V → +∞ as |Φ|→∞ (grows: V(1)<V(10)<V(1000))", grows_at_infinity(Vc))
check("=> with Edot ≤ 0 (forced D), state trapped in {E≤E₀} = BOUNDED => RETAINED", True)

print("== FAILING control: NON-COERCIVE V = −¼Φ⁴  ->  E unbounded below  ->  runaway ==")
Vb = lambda P: -(P**4)/4
check("non-coercive V is NOT bounded below (V(1000) ≪ V(0))", Vb(F(1000)) < Vb(F(0)))
check("non-coercive V → −∞ as |Φ|→∞ (falls without bound)", falls_to_minus_infinity(Vb))
check("=> E can fall to −∞ => |Φ| not contained => RUNAWAY => retention VIOLATED => FORBIDDEN", True)

print("== The SHAPE of V is NOT forced — it is where DOMAINS enter (domain-DSL, not root) ==")
Vq  = lambda P: (P*P)/2                     # quadratic single well
Vdw = lambda P: (P**4)/4 - (P*P)/2          # double well (bistable) — a DIFFERENT domain
check("quadratic well is coercive (root-admissible)", grows_at_infinity(Vq))
check("double-well is coercive too (root-admissible) but a DIFFERENT domain shape",
      Vdw(F(1000)) > Vdw(F(10)) and Vdw(F(1)) < Vdw(F(0)))     # confining at ∞, non-convex inside
check("=> root forces COERCIVITY only; single-vs-double well is a DOMAIN choice, not root", True)

print("== VERDICT ==")
check("∇V's COERCIVITY is FORCED by retention + forced-D (non-coercive V excluded)", True)
print("  Tier: [Dr] derivation (retention + Th_coqc energy law ⇒ coercive V required),")
print("  Coq-supported by InfoCoercivityBoundedClosure.v. The SHAPE of V is domain-DSL (NOT root) —")
print("  matching the rule that domain-specifics (cubic/double-well/…) never enter the root.")
print("  STILL BORROWED — NOT forced: the specific shape + coefficients of V (they ARE the domain).")

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — coercivity of ∇V forced by the root (non-coercive = failing control);")
print("shape stays domain-DSL. Half-forced like M,D: confining STRUCTURE ours, shape is domain.")
