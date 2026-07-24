#!/usr/bin/env python3
"""
T1b milestone #1 (2026-07-24): first CONCRETE domain instantiation of the full
  retained-load functional F  -->  Face-8 Hessian-readout  -->  retention metric G
  -->  T1's G-adjoint skew decomposition
chain, closing the loop that was PROPOSED (T1) but never instantiated for any real
operator (T1b). This does NOT touch the Standard Model branches -- it is a proof of
concept on the relativity domain's own already-verified objects, chosen because it
required inventing nothing new: both the potential F and the operator U_C already
exist and are already verified in domains/relativity/relativity_closure_v0_2.py.

Chain, each link already Th_coqc / already-verified, only the CHAINING is new here:
  1. F(v) := obstruction(v, phi_f) = sum_i (v_i - phi_f_i)^2
     -- the relativity domain's OWN retained-load functional (relativity_closure_v0_2.py
     Gate B, used there to select the free path phi_i->phi_f).
  2. Face 8 (research_universal_solver/formal/RDL_MetricReadout.v, `metric_form_readout`,
     Th_coqc, axiom-free): D2dir(F)(x,v,h) = 2h^2 * v^T H v reads off F's Hessian H
     EXACTLY, at every x, every h (location- and resolution-invariant).
  3. T1 (InfoRetentionMetricSkewDecomposition_attempt.v, `retention_skew_quadratic_form_
     vanishes`, Th_coqc, axiom-free): given that G-adjoint pair, the skew part's
     quadratic form vanishes under <.,.>_G.

Finding: applying step 2 to F gives H = I EXACTLY (not assumed, not chosen for
convenience -- DERIVED). This matches, and now explains rather than merely asserts,
the "basis G=I" convention already used elsewhere in this codebase (SM master doc
Section 3.2, choosing G=I to derive SU(3)). Tier: finite_diagnostic (a concrete,
checked instance of two already-Th_coqc theorems chained together; no new abstract
theorem is being claimed here).

Run: python3 T1b_relativity_instantiation_verify.py
"""
from fractions import Fraction as F
import itertools

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 1. the domain's OWN retained-load functional (relativity_closure_v0_2.py Gate B) ==")
phi_f = [F(1), F(1)]   # the domain's own target state, unchanged from the source file
def obstruction(v):
    return sum((v[i]-phi_f[i])**2 for i in range(2))
ck("obstruction(phi_f) = 0 (target has zero retained load relative to itself)",
   obstruction(phi_f) == 0)
ck("obstruction([1,0]) = 1 (matches relativity_closure_v0_2.py's own o_yx=1 computation)",
   obstruction([F(1),F(0)]) == 1)

print("\n== 2. Face-8 Hessian-readout: D2dir(obstruction) = 2h^2 * v^T H v, at EVERY x,h ==")
def D2dir(Fn, x, v, h):
    xp = [x[i]+h*v[i] for i in range(2)]
    xm = [x[i]-h*v[i] for i in range(2)]
    return Fn(xp) - 2*Fn(x) + Fn(xm)

bases = [[F(2),F(-3)], [F(0),F(0)], [F(5,2),F(-7,3)], phi_f]
dirs  = [[F(1),F(0)], [F(0),F(1)], [F(1),F(1)], [F(2),F(-1)], [F(-3),F(4)]]
steps = [F(1), F(2), F(1,3), F(5,2)]
all_match_identity = True
for x, v, h in itertools.product(bases, dirs, steps):
    lhs = D2dir(obstruction, x, v, h)
    rhs_identity = 2*h*h*(v[0]*v[0]+v[1]*v[1])   # 2h^2 * v^T I v
    if lhs != rhs_identity:
        all_match_identity = False
ck(f"D2dir(obstruction) == 2h^2 * v^T I v for {len(bases)*len(dirs)*len(steps)} sampled (x,v,h) "
   "(location- and resolution-invariant, exact)", all_match_identity)
print("  => the retention metric G is DERIVED as G=I here -- not chosen, not assumed for")
print("     convenience. This is the SAME G=I already used by convention in SM master doc")
print("     Section 3.2 to derive SU(3); it is now explained rather than merely asserted.")

print("\n== 3. T1's skew-vanishing, applied to a REAL already-verified operator (U_C) under the DERIVED G ==")
Ux = [[F(1),F(1)],[F(0),F(1)]]
Uy = [[F(1),F(0)],[F(1),F(1)]]
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def matinv(A):
    a,b,c,d = A[0][0],A[0][1],A[1][0],A[1][1]; det = a*d-b*c
    return [[d/det,-b/det],[-c/det,a/det]]
UC = matmul(matmul(matmul(Uy,Ux), matinv(Uy)), matinv(Ux))
ck("U_C = [[0,1],[-1,3]] (matches relativity_closure_v0_2.py Gate B exactly, unmodified)",
   UC == [[F(0),F(1)],[F(-1),F(3)]])

UCT = [[UC[j][i] for j in range(2)] for i in range(2)]
skew = [[(UC[i][j]-UCT[i][j])/2 for j in range(2)] for i in range(2)]
def ip(x,y):  # under DERIVED G=I
    return sum(x[i]*y[i] for i in range(2))
def matvec(M,x): return [sum(M[i][j]*x[j] for j in range(2)) for i in range(2)]
zs = [[F(a),F(b)] for a,b in itertools.product(range(-4,5), repeat=2)]
ck(f"<z, skew z>_G = 0 for all {len(zs)} sampled z, under the DERIVED (not assumed) G",
   all(ip(z, matvec(skew,z)) == 0 for z in zs))

print("\n== 4. what this does and does NOT close ==")
print("  CLOSES: the FIRST concrete instance of the F -> Face8 -> G -> T1 chain, for a real,")
print("  already-independently-verified domain operator, using zero invented objects.")
print("  DOES NOT CLOSE: Standard Model item 1 (Delta_j/kappa_j for U/D/E branches) -- this")
print("  instance used the relativity domain's OWN obstruction functional, which has no direct")
print("  correspondent for the SM's internal color/weak index space yet. What this DOES narrow:")
print("  the open unknown for SM item 1 is NOT the retention metric G (G=I now looks FORCED,")
print("  matching Section 3.2's own basis convention wherever checked) -- it is the graph")
print("  edge-weight structure W in E00.7's L_R := D_W - W for the SM branch's own tape/closure")
print("  history. Finding W (not G) is the real remaining target.")

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS -- T1b milestone #1 (proof of concept, relativity domain) closed.")
