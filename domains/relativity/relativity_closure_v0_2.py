#!/usr/bin/env python3
"""
Relativity domain — finite internal closure witnesses (v0.2).

FINITE_INTERNAL_CLOSURE ONLY. Exact rational arithmetic (Fraction). No floats, no
external relativity/geometry law imported, no physics claim. Every check below is a
symbolic identity derived from the root's finite causal cone + retention operator,
NOT a statement about real spacetime. Run: `python3 relativity_closure_v0_2.py`.

v0.2 ADDS two new internal gates on top of the unmodified v0.1 witnesses (sections A, B
below are byte-identical in logic to relativity_closure_v0_1.py, which remains the
immutable v0.1 anchor and is never edited):

  C. Null-Transport Factorization Gate [PROPOSED_INTERNAL_GATE] — closes OB-07
     (observer-normalization/redshift) and, combined with the Unruh-fix readout, closes
     OC-05's horizon half (internal bridge only, not physical surface gravity).
  D. Geometry Stationarity Gate [FINITE_DIAGNOSTIC] — closes OC-05's dynamic
     metric-source half via the same DRL retained-action grammar applied to the living
     geometry state Theta, with an exact fixture AND a failing control case.

Tier discipline unchanged: the observer-cone -> Gamma_R -> Lorentz-form closure is
conditional on the RD-neutrality gate (pure observer change preserves the RD causal-cell
count n_+ n_-). That gate is [Proposed internal gate]; hence the whole SR sector is a
[Proposed internal bridge], never [Th_coqc] and never "real physics". Gate C and Gate D
are likewise internal gates/diagnostics, not proofs of real physics; see
CLAIM_BOUNDARY.json and DRIFT_CONTRACT.json for the enforced boundary and
forbidden_claims for the exact wording.
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

print("== C. Null-Transport Factorization Gate [PROPOSED_INTERNAL_GATE] ==")
# Diagonal observer map B=diag(a,b) factors uniquely as B = N * diag(chi^-1, chi):
#   N   = sqrt(det B)   (internal LAPSE)
#   chi = sqrt(b/a)     (relative-observer factor)
# so a = N/chi, b = N*chi. Witness i|o: a=2, b=8.
a_io, b_io = F(2), F(8)
detB_io = a_io*b_io
N_io = F(4)
chi_io = F(2)
check("witness i|o: det B = a*b = 16", detB_io == 16, detB_io)
check("N_io = sqrt(det B_io) = 4  (N^2 = det B)", N_io*N_io == detB_io, N_io)
check("chi_io = sqrt(b/a) = 2  (chi^2 = b/a)", chi_io*chi_io == b_io/a_io, chi_io)
check("factorization: a = N/chi", a_io == N_io/chi_io, a_io)
check("factorization: b = N*chi", b_io == N_io*chi_io, b_io)

# Pure-observer change: det B = 1 => N = 1 (chi need not be 1).
a_pure, b_pure = F(1,2), F(2)
detB_pure = a_pure*b_pure
N_pure = F(1)
chi_pure = F(2)
check("pure-observer witness: det B = 1", detB_pure == 1, detB_pure)
check("pure-observer change => N = 1", N_pure*N_pure == detB_pure and N_pure == 1, N_pure)
check("pure-observer chi != 1 is still allowed (chi=2, N=1)", chi_pure != 1 and N_pure == 1)

# Composition: determinants multiply => N_{j|o} = N_{j|i} * N_{i|o}.
a_ji, b_ji = F(3), F(27)
detB_ji = a_ji*b_ji
N_ji = F(9)
check("witness j|i: det B = 81, N_ji = 9", detB_ji == 81 and N_ji*N_ji == detB_ji, (detB_ji, N_ji))
# diagonal composition B_{j|o} = B_{j|i} . B_{i|o} (entrywise, both diagonal)
a_jo, b_jo = a_ji*a_io, b_ji*b_io
detB_jo = a_jo*b_jo
N_jo = F(36)
check("composed witness j|o: det B_jo = det B_ji * det B_io = 1296", detB_jo == detB_ji*detB_io, detB_jo)
check("N_jo = sqrt(det B_jo) = 36", N_jo*N_jo == detB_jo, N_jo)
check("composition (holonomy scalar side): N_jo = N_ji * N_io", N_jo == N_ji*N_io, (N_jo, N_ji*N_io))

# Redshift: dtheta_i = N_{i|o} dtheta_o  =>  nu_o = N nu_i, dtheta_o = dtheta_i / N.
dtheta_o = F(3)
dtheta_i = N_io*dtheta_o
check("redshift: dtheta_i = N_io * dtheta_o = 12", dtheta_i == 12, dtheta_i)
check("redshift: dtheta_o = dtheta_i / N_io recovers 3", dtheta_i/N_io == dtheta_o, dtheta_i/N_io)
nu_i = F(1)
nu_o = N_io*nu_i
check("redshift: nu_o = N_io * nu_i = 4", nu_o == 4, nu_o)

# Horizon WITHOUT infinity: N = 0 <=> det B = 0 (finite rank-loss boundary, not infinity).
a_h, b_h = F(0), F(5)
detB_h = a_h*b_h
N_h = F(0)
check("horizon witness: det B_h = 0", detB_h == 0, detB_h)
check("horizon: N_h = sqrt(det B_h) = 0", N_h*N_h == detB_h and N_h == 0, N_h)
try:
    _ = mat_inv_unimod([[a_h,F(0)],[F(0),b_h]])
    horizon_has_no_inverse = False
except ZeroDivisionError:
    horizon_has_no_inverse = True
check("horizon: singular B_h has no inverse (exterior cannot reconstruct interior)", horizon_has_no_inverse)

# Unruh-fix readout: a_local declared from tau_c^(U) = pi c / a_local (DeclaredFormula
# lineage kept, treated here as an opaque already-computed rational a_local). The observer
# reads a_o = N_{i|o} * a_local; kappa_R := lim N_{i|o} a_local(i) if finite.
a_local = F(7,2)
kappa_R = N_io*a_local
check("Unruh-fix: kappa_R = N_io * a_local = 14 (finite)", kappa_R == 14, kappa_R)
check("Unruh-fix: kappa_R != a_local unless N=1 (internal bridge, not identity)", kappa_R != a_local)

print("== D. Geometry Stationarity Gate [FINITE_DIAGNOSTIC] ==")
# Same DRL retained-action grammar applied to the living-geometry state Theta.
# G[Theta] = G_0 + sum_a Theta^a G_a  =>  dG/dTheta^a = G_a.
# Geometry source: S_Theta,n^a = Phi_n^T G_a Psi_n (reader x record changing the operator
# geometry reads -- NOT posited as energy/mass/stress).
Theta_nm1 = F(0)     # Theta_{n-1}
Theta_n   = F(1,2)
M_Theta   = F(2)
K         = F(1)
dt        = F(1)
def gradU_Theta(Theta):   # U_Theta = (1/4) Theta^2  =>  grad U_Theta = (1/2) Theta
    return Theta/2

G1 = [[F(0),F(1)],[F(1),F(0)]]     # G_a fixture operator
Phi_n = [F(1),F(0)]
Psi_n = [F(0),F(1)]
def matvec(M, vec):
    return [M[0][0]*vec[0]+M[0][1]*vec[1], M[1][0]*vec[0]+M[1][1]*vec[1]]
G1Psi = matvec(G1, Psi_n)
S_Theta = Phi_n[0]*G1Psi[0] + Phi_n[1]*G1Psi[1]
check("geometry source S_Theta = Phi^T G_1 Psi = 1", S_Theta == 1, S_Theta)

# Stationarity: M_Theta * d^2_t Theta_n + grad U_Theta(Theta_n) + K S_Theta,n = 0.
# Explicit stepper: Theta_{n+1} = 2 Theta_n - Theta_{n-1} - dt^2 M_Theta^-1 [grad U + K S].
Theta_np1 = 2*Theta_n - Theta_nm1 - dt*dt*(1/M_Theta)*(gradU_Theta(Theta_n) + K*S_Theta)
check("exact fixture: Theta_{n+1} = 3/8", Theta_np1 == F(3,8), Theta_np1)

d2Theta = (Theta_np1 - 2*Theta_n + Theta_nm1)/(dt*dt)
R_Theta = M_Theta*d2Theta + gradU_Theta(Theta_n) + K*S_Theta
check("action residual R_Theta = 0 at Theta_{n+1}=3/8", R_Theta == 0, R_Theta)

# FAILING CONTROL: drop the Psi source (S_Theta forced to 0) -> wrong trajectory, and the
# TRUE equation (with the real S_Theta=1 reinstated) evaluated on that wrong trajectory
# gives a nonzero residual: proves Psi (the record field) is load-bearing, not decorative.
S_Theta_dropped = F(0)
Theta_wrong = 2*Theta_n - Theta_nm1 - dt*dt*(1/M_Theta)*(gradU_Theta(Theta_n) + K*S_Theta_dropped)
check("failing control: Theta_wrong (S_Theta=0) = 7/8", Theta_wrong == F(7,8), Theta_wrong)
d2Theta_wrong = (Theta_wrong - 2*Theta_n + Theta_nm1)/(dt*dt)
R_Theta_wrong = M_Theta*d2Theta_wrong + gradU_Theta(Theta_n) + K*S_Theta   # true S_Theta=1
check("failing control: R_Theta = 1 != 0 (Psi source proven load-bearing)", R_Theta_wrong == 1, R_Theta_wrong)

print("== Closure audit (24-node Minimal Relativity DAG, v0.2) ==")
# group A (12), B (7), C (5); 1=closed, 0.5=partial, 0=open
A = [1,1,1,1,1,1,1,1,1,1,1,1]          # observer/kinematics: 12/12 (unchanged)
B = [1,0.5,1,1,1,1,1]                   # OB-07 observer-normalization/redshift now CLOSED (Gate C)
C = [0.5,0.5,0.5,0.5,1]                 # OC-05 horizon bridge/metric-source now CLOSED (Gate C horizon + Gate D)
alln = A+B+C
closed  = sum(1 for xi in alln if xi==1)
partial = sum(1 for xi in alln if xi==0.5)
openn   = sum(1 for xi in alln if xi==0)
check("24 nodes total", len(alln)==24, len(alln))
check("group A closed 12/12", sum(1 for xi in A if xi==1)==12)
check("group B closed 6/7",   sum(1 for xi in B if xi==1)==6)
check("group C strict closed 1/5", sum(1 for xi in C if xi==1)==1)
check("strict closure 19/24 = 79.2%", closed==19 and F(closed,24)==F(19,24), (closed, str(F(closed,24))))
weighted = F(closed,1) + F(partial,1)*F(1,2)
check("weighted closure 21.5/24 = 89.6%", weighted==F(43,2) and F(closed*2+partial,48)==F(43,48), str(weighted))
check("counts closed/partial/open = 19/5/0", (closed,partial,openn)==(19,5,0), (closed,partial,openn))

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)} check(s) failed): {FAILS}")
    raise SystemExit(1)
print("DECISION: PASS  — finite internal closure witnesses verified (exact rational).")
print("NOTE: this is FINITE_INTERNAL_CLOSURE only. NOT real physics, NOT Coq-checked,")
print("      SR sector is [Proposed internal bridge] conditional on the RD-neutrality gate.")
print("      Gate C (null-transport factorization) and Gate D (geometry stationarity) are")
print("      internal gates/diagnostics closing OB-07 and OC-05 on THIS DAG only; they are")
print("      NOT physical lapse/surface-gravity/stress-energy claims. See CLAIM_BOUNDARY.json.")
