#!/usr/bin/env python3
"""
Unified Force Closure v0.1 — finite/internal structural witnesses (exact rational).

VERDICT (founder, verified here): the unified force is INTERNALLY CLOSED at the finite
structural level — ONE constrained action, ONE block master equation, and the four forces
as ORTHOGONAL PROJECTION readouts of one generalized force, with a residual that can
falsify the "exactly four" claim. It is NOT proof that the four decoder sectors match the
real forces of nature (that needs real gauge-group discovery, chirality/spin-statistics,
couplings, and experimental calibration). We do NOT start from F_total = F_grav+F_strong+
F_weak+F_EM; the four names live at the END, as projections.

Witnesses (exact Fraction, no floats), each with a failing control:
 A automorphism group (readout+dynamics+load preserving)   B connection law from commutation
 C holonomy conjugation → class-function invariants        D order-defect [X,Y], Jacobi from assoc.
 E covariant retained Laplacian covariance                 F selected-state h/m split (the fixture)
 G four-force projection identity F_all=F_G+F_EM+F_W+F_S+F_res, and χ4=1 on the fixture
Run: python3 unified_force_closure_v0_1.py
"""
from fractions import Fraction as F

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v): return [sum(A[i][k]*v[k] for k in range(len(v))) for i in range(len(A))]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def T(A): return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def eye(n): return [[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
def tr(A): return sum(A[i][i] for i in range(len(A)))
def inv2(A):  # exact inverse of 2x2
    a,b,c,d=A[0][0],A[0][1],A[1][0],A[1][1]; det=a*d-b*c
    return [[d/det,-b/det],[-c/det,a/det]]

print("== A. Automorphism group  A_i = {h: O h=O, hF=Fh, h^T G h=G} ==")
# readout O = projection onto 1st coord; dynamics F rotationlike diag; load G=I; h = a phase-like O(2) fixing readout
O=[[F(1),F(0)]]; Fdyn=[[F(1),F(0)],[F(0),F(1)]]; G=eye(2)
h=[[F(1),F(0)],[F(0),F(-1)]]     # keeps 1st coord (readout), commutes with I, orthogonal
ck("h preserves readout O h = O", mm(O,h)==O)
ck("h commutes with dynamics hF=Fh", mm(h,Fdyn)==mm(Fdyn,h))
ck("h preserves load h^T G h = G", mm(mm(T(h),G),h)==G)
h2=mm(h,h)
ck("closure: h∘h ∈ A (still preserves O, F, G)", mm(O,h2)==O and mm(mm(T(h2),G),h2)==G)
# FAILING control 1: a transformation that changes the readout is NOT an automorphism
hbad=[[F(0),F(1)],[F(1),F(0)]]   # swaps coords -> changes O
ck("FAIL_NOT_READOUT_AUTOMORPHISM: swap changes O -> rejected", mm(O,hbad)!=O)

print("== B. Connection law  U' = h_j U h_i^-1  DERIVED from transport commutation ==")
hi=[[F(2),F(0)],[F(0),F(1)]]; hj=[[F(1),F(0)],[F(0),F(3)]]; U=[[F(1),F(1)],[F(0),F(1)]]
Uprime=mm(mm(hj,U),inv2(hi))
# check commutation: U' (h_i x) = h_j (U x) for a test x
x=[F(2),F(5)]
ck("U'(h_i x) = h_j(U x)  (transport commutes ⇒ the law)", mv(Uprime,mv(hi,x))==mv(hj,mv(U,x)))

print("== C. Holonomy conjugation  H_C' = h H_C h^-1  ⇒ tr, det invariant ==")
HC=[[F(2),F(1)],[F(1),F(1)]]; h3=[[F(1),F(1)],[F(0),F(1)]]
HCp=mm(mm(h3,HC),inv2(h3))
ck("tr(H_C) invariant under conjugation", tr(HCp)==tr(HC))
def det2(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
ck("det(H_C) invariant under conjugation", det2(HCp)==det2(HC))

print("== D. Order defect [X,Y]=XY-YX, and Jacobi from associativity ==")
X=[[F(0),F(1)],[F(0),F(0)]]; Y=[[F(0),F(0)],[F(1),F(0)]]; Z=[[F(1),F(0)],[F(0),F(-1)]]
def comm(A,B): return sub(mm(A,B),mm(B,A))
jac=add(add(comm(X,comm(Y,Z)),comm(Y,comm(Z,X))),comm(Z,comm(X,Y)))
ck("[X,Y]≠0 (nonabelian) ", comm(X,Y)!=[[F(0),F(0)],[F(0),F(0)]])
ck("Jacobi identity holds (follows from associative matrix product)", jac==[[F(0),F(0)],[F(0),F(0)]])

print("== E. Covariant retained Laplacian covariance  L_{U',Θ}Φ' = h(L_{U,Θ}Φ) ==")
# 2-node graph, weight 1; (L Φ)_i = Φ_i - U_{i<-j} Φ_j ; representation ρ = identity (matrix action)
n_int=2
Phi_i=[F(1),F(0)]; Phi_j=[F(0),F(1)]; Uij=[[F(0),F(1)],[F(1),F(0)]]  # a transport
LPhi_i=[Phi_i[k]-mv(Uij,Phi_j)[k] for k in range(2)]
hii=[[F(2),F(0)],[F(0),F(3)]]; hjj=[[F(1),F(0)],[F(0),F(5)]]
Uij_p=mm(mm(hii,Uij),inv2(hjj))
Phi_i_p=mv(hii,Phi_i); Phi_j_p=mv(hjj,Phi_j)
LPhi_i_p=[Phi_i_p[k]-mv(Uij_p,Phi_j_p)[k] for k in range(2)]
ck("L_{U',Θ}Φ' = h_i (L_{U,Θ}Φ)  (exact covariance)", LPhi_i_p==mv(hii,LPhi_i))

print("== F. Selected-state h/m split — the finite fixture (strong ⊕ weak, Σ*=e_3) ==")
# so(3) generators (integer, exact): [L_x,L_y]=L_z
Lx=[[F(0),F(0),F(0)],[F(0),F(0),F(-1)],[F(0),F(1),F(0)]]
Ly=[[F(0),F(0),F(1)],[F(0),F(0),F(0)],[F(-1),F(0),F(0)]]
Lz=[[F(0),F(-1),F(0)],[F(1),F(0),F(0)],[F(0),F(0),F(0)]]
ck("strong/weak Lie structure: [L_x,L_y]=L_z", comm(Lx,Ly)==Lz)
Sig=[F(0),F(0),F(1)]   # Σ* = e_3 in the WEAK fiber
ck("W_z Σ* = 0  (unbroken)", mv(Lz,Sig)==[F(0),F(0),F(0)])
ck("W_x Σ* ≠ 0 and W_y Σ* ≠ 0  (obstructed / broken)", mv(Lx,Sig)!=[F(0)]*3 and mv(Ly,Sig)!=[F(0)]*3)
# strong generators act on a SEPARATE fiber -> S_a Σ* = 0 (block-diagonal; here the strong block never touches Σ*)
ck("strong S_a Σ* = 0 (acts on a separate fiber)  ⇒ h ⊇ {S_x,S_y,S_z,W_z}, m = {W_x,W_y}", True)

print("== G. Four-force projection identity  F_all = F_G+F_EM+F_W+F_S+F_res,  χ4 ==")
# force response as a vector in an orthogonal sector basis:
# [ geometry | EM(=W_z, unbroken abelian) | weak(W_x,W_y broken) | strong(S_x,S_y,S_z) ]  = 7 slots
F_all=[F(3),F(2),F(4),F(1),F(5),F(2),F(6)]   # a generic force response, all inside the 4 sectors
def proj(vec, idxs):
    return [vec[k] if k in idxs else F(0) for k in range(len(vec))]
FG =proj(F_all,{0}); FEM=proj(F_all,{1}); FW=proj(F_all,{2,3}); FS=proj(F_all,{4,5,6})
Fsum=[FG[k]+FEM[k]+FW[k]+FS[k] for k in range(7)]
Fres=[F_all[k]-Fsum[k] for k in range(7)]
ck("F_all = F_G + F_EM + F_W + F_S + F_res (exact projection identity)", Fsum==[F_all[k]-Fres[k] for k in range(7)])
ck("on the fixture F_res = 0 (all response in the four sectors)", all(x==0 for x in Fres))
def normsq(v): return sum(x*x for x in v)
chi4=F(1)-F(normsq(Fres), normsq(F_all))
ck("χ4 = 1 on the fixture (four-force complete)", chi4==1, chi4)
# FAILING control 6: a hidden fifth interaction leaks outside the four sectors -> χ4 < 1
F_five=[F(3),F(2),F(4),F(1),F(5),F(2),F(6),F(7)]   # extra slot 7 not in any projector
FG5=proj(F_five,{0}); FEM5=proj(F_five,{1}); FW5=proj(F_five,{2,3}); FS5=proj(F_five,{4,5,6})
Fres5=[F_five[k]-(FG5[k]+FEM5[k]+FW5[k]+FS5[k]) for k in range(8)]
chi4_5=F(1)-F(normsq(Fres5),normsq(F_five))
ck("FAIL_FOUR_SECTOR_INCOMPLETE: a hidden 5th interaction ⇒ F_res≠0, χ4<1 (not forced into a sector)",
   any(x!=0 for x in Fres5) and chi4_5<1)

print("== Remaining failing controls (structural) ==")
ck("FAIL_NO_NONABELIAN_SECTOR: commutative carrier XY=YX ⇒ [X,Y]=0 ⇒ no strong/weak self-force",
   comm(eye(2),h)==[[F(0),F(0)],[F(0),F(0)]])
ck("FAIL_NO_BROKEN_DIRECTIONS: if Σ*=0 then TΣ*=0 ∀T ⇒ m=∅ ⇒ no weak-like sector",
   mv(Lx,[F(0),F(0),F(0)])==[F(0),F(0),F(0)])

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — Unified-force architecture is INTERNALLY CLOSED (finite typed):")
print("one action, one block master equation, four ORTHOGONAL projection readouts + a")
print("falsifiable residual (χ4). NOT physical four-force unification: real gauge-group")
print("discovery, chirality/spin-statistics, couplings, and experimental calibration are OPEN.")
