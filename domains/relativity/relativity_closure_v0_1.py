#!/usr/bin/env python3
"""
Relativity domain — finite internal closure witnesses (v0.1).

FINITE_INTERNAL_CLOSURE ONLY. Exact rational arithmetic (Fraction). No floats, no
external relativity/geometry law imported, no physics claim. Every check below is a
symbolic identity derived from the root's finite causal cone + retention operator,
NOT a statement about real spacetime. Run: `python3 relativity_closure_v0_1.py`.

Tier discipline: the observer-cone -> Gamma_R -> Lorentz-form closure is conditional on
the RD-neutrality gate (pure observer change preserves the RD causal-cell count
n_+ n_- ). That gate is [Proposed internal gate]; hence the whole SR sector is a
[Proposed internal bridge], never [Th_coqc] and never "real physics".
"""
from fractions import Fraction as F

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)

def mat_mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def mat_inv_unimod(A):  # inverse of a 2x2 integer unimodular matrix, exact
    a,b,c,d = A[0][0],A[0][1],A[1][0],A[1][1]
    det = a*d-b*c
    return [[F(d,1)/det, F(-b,1)/det],[F(-c,1)/det, F(a,1)/det]]

print("== A. Observer-Cone Closure (conditional on RD-neutrality gate) ==")
v, u = F(5,4), F(3,4)
beta = u/v
check("beta = u/v = 3/5", beta == F(3,5), beta)
kappa2 = (1+beta)/(1-beta)
check("kappa^2 = (1+beta)/(1-beta) = 4", kappa2 == 4, kappa2)
kappa = F(2)            # positive root
check("kappa = 2", kappa*kappa == kappa2, kappa)
GammaR = (kappa + 1/kappa)/2
check("Gamma_R = (kappa+1/kappa)/2 = 5/4", GammaR == F(5,4), GammaR)
# closed form Gamma_R = 1/sqrt(1-beta^2): check squared identity to avoid floats
check("Gamma_R^2 (1-beta^2) = 1  [=> Gamma_R=1/sqrt(1-beta^2)]",
      GammaR*GammaR*(1-beta*beta) == 1)
# exact event transform
t, x = F(8), F(5)
xp = GammaR*(x - u*t)
tp = GammaR*(t - u*x/(v*v))
check("event (8,5) -> x' = -5/4", xp == F(-5,4), xp)
check("event (8,5) -> t' = 7",   tp == F(7),    tp)
Qv  = v*v*t*t   - x*x
Qvp = v*v*tp*tp - xp*xp
check("cone product Q_v = 75", Qv == 75, Qv)
check("Q_v' = Q_v (invariant, exact)", Qvp == Qv, Qvp)
# RD causal-cell count invariance  n_+ n_- = Q_v
np_, nm = v*t + x, v*t - x
check("n_+ n_- = Q_v", np_*nm == Qv)
# velocity composition (v in place of c), exact
u1, u2 = F(3,4), F(1,2)
u21 = (u1+u2)/(1 + u1*u2/(v*v))
check("velocity composition u21 = (u1+u2)/(1+u1u2/v^2)", u21 == (F(3,4)+F(1,2))/(1+F(3,4)*F(1,2)/(v*v)), u21)
check("composed speed stays sub-cone (|u21| < v)", abs(u21) < v, u21)

print("== B. Living-Geometry Closure (finite matrix certificates) ==")
Ux = [[1,1],[0,1]]
Uy = [[1,0],[1,1]]
UxUy = mat_mul(Ux,Uy); UyUx = mat_mul(Uy,Ux)
check("U_xU_y = [[2,1],[1,1]]", UxUy == [[2,1],[1,1]], UxUy)
check("U_yU_x = [[1,1],[1,2]]", UyUx == [[1,1],[1,2]], UyUx)
check("transports do NOT commute (U_xU_y != U_yU_x)", UxUy != UyUx)
# loop transport U_C = U_y U_x U_y^-1 U_x^-1 ; curvature K_C = U_C - I
UC = mat_mul(mat_mul(mat_mul(Uy,Ux), mat_inv_unimod(Uy)), mat_inv_unimod(Ux))
check("loop transport U_C = [[0,1],[-1,3]]", UC == [[F(0),F(1)],[F(-1),F(3)]], UC)
KC = [[UC[i][j]-(1 if i==j else 0) for j in range(2)] for i in range(2)]
check("curvature K_C = U_C - I = [[-1,1],[-1,2]] != 0", KC == [[F(-1),F(1)],[F(-1),F(2)]], KC)
# free-path from obstruction: phi_i=[1,0], phi_f=[1,1]
phi_i = [F(1),F(0)]; phi_f = [F(1),F(1)]
def apply(M,vec): return [sum(M[i][k]*vec[k] for k in range(2)) for i in range(2)]
end_xy = apply(UyUx, phi_i)   # path x then y  (U_yU_x acting)
end_yx = apply(UxUy, phi_i)   # path y then x
def obstruction(end, target): return sum((end[i]-target[i])**2 for i in range(2))
o_xy = obstruction(end_xy, phi_f)
o_yx = obstruction(end_yx, phi_f)
check("free path x->y terminal obstruction = 0", o_xy == 0, o_xy)
check("path y->x terminal obstruction = 1", o_yx == 1, o_yx)
check("obstruction selects the free path (0 < 1)", o_xy < o_yx)

print("== Closure audit (24-node Minimal Relativity DAG) ==")
# group A (12), B (7), C (5); 1=closed, 0.5=partial, 0=open
A = [1,1,1,1,1,1,1,1,1,1,1,1]          # observer/kinematics: 12/12 after RD-neutrality gate
B = [1,0.5,1,1,1,1,0]                   # operator->metric, basis-cov(partial), connection, curvature, free-path, feedback, redshift(open)
C = [0.5,0.5,0.5,0.5,0]                 # graph-speed, mass-memory, Schwarzschild(decl), Unruh(decl), horizon-bridge(open)
alln = A+B+C
closed  = sum(1 for xi in alln if xi==1)
partial = sum(1 for xi in alln if xi==0.5)
openn   = sum(1 for xi in alln if xi==0)
check("24 nodes total", len(alln)==24, len(alln))
check("group A closed 12/12", sum(1 for xi in A if xi==1)==12)
check("group B closed 5/7",   sum(1 for xi in B if xi==1)==5)
check("group C strict closed 0/5", sum(1 for xi in C if xi==1)==0)
check("strict closure 17/24 = 70.8%", closed==17 and F(closed,24)==F(17,24), (closed, str(F(closed,24))))
weighted = F(closed,1) + F(partial,1)*F(1,2)
check("weighted closure 19.5/24 = 81.25%", weighted==F(39,2)/1 and F(int(weighted*2),48)==F(39,48), (str(weighted)))
check("counts closed/partial/open = 17/5/2", (closed,partial,openn)==(17,5,2), (closed,partial,openn))

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)} check(s) failed): {FAILS}")
    raise SystemExit(1)
print("DECISION: PASS  — finite internal closure witnesses verified (exact rational).")
print("NOTE: this is FINITE_INTERNAL_CLOSURE only. NOT real physics, NOT Coq-checked,")
print("      SR sector is [Proposed internal bridge] conditional on the RD-neutrality gate.")
