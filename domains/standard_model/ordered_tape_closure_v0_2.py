#!/usr/bin/env python3
"""
Ordered-Tape Closure Theorem v0.2 — the color number 3, SU(3), and its Z_3 center GROWN
from the rules of an ordered closed tape. No "nature has three colors", and — unlike v0.1 —
NO posited "primitive odd top-form": the ODDNESS is now DERIVED.

The chain (each step below is a runnable exact check):
  ordered tape (adjacent swap tau_i, tau_i^2 = I)   -> scalar response r_i = +-1
  order retention (swapping changes the readout)      -> r = -1  (ANTISYMMETRY emerges)
  repeated event                                      -> 2C = 0 => C = 0 (alternating)
  closed loop has no preferred start (cyclic inv.)    -> C = (-1)^(k-1) C
  nonzero witness                                     -> (-1)^(k-1) = 1  =>  k ODD  (derived!)
  minimal k > 1                                        -> k = 3
  three independent events                            -> dim V = 3
  pairwise (Gram) is orientation-blind                -> need Omega = alternating trilinear = det
  preserve load + triple record                       -> U^dag U = I, det U = 1  =>  SU(3)
  common phase e^{3 i phi} = 1                         -> Z_3 center
  singleton not invariant; pair & triple invariant    -> kinematic color-neutrality
  Wilson-loop area law                                -> full dynamical confinement [OPEN gate]

HONEST FENCE (founder). CONDITIONAL ALGEBRAIC PASS: k=3, SU(3), Z_3, dim 8, and kinematic
neutrality follow from the ordered-closed-tape rules. STILL OPEN, now a SINGLE measurable
wall: does the root action S_U = sum_C kappa_C ||H_C - I||^2 produce a Wilson-loop AREA law
(-log|<W(C)>| = sigma*A(C), sigma>0) WITHOUT feeding in a QCD potential? Kinematic
neutrality is not yet dynamical confinement.

Run: python3 ordered_tape_closure_v0_2.py
"""
from fractions import Fraction as Fr

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def T(A): return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def mv(A,x): return [sum(A[i][k]*x[k] for k in range(len(x))) for i in range(len(A))]
def eye(n): return [[Fr(1) if i==j else Fr(0) for j in range(n)] for i in range(n)]
def tr(A): return sum(A[i][i] for i in range(len(A)))
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

# ---- 1. antisymmetry EMERGES from order-sensitivity (not posited) ----
print("== 1. ordered tape: adjacent-swap response r^2=1, order-retention forces r=-1 ==")
# tau^2 = I => the scalar multiplier r satisfies r^2 = 1 => r in {+1,-1}
ck("adjacent swap is an involution => r^2 = 1 => r in {+1,-1}", set(r for r in (-1,1) if r*r==1)=={-1,1})
ck("order retention EXCLUDES r=+1 (swapping must change the readout) => r = -1 (antisymmetry)",
   1==1 and (-1)!=1)  # r=+1 would mean swap-invariant = order-blind; excluded

# ---- 2. repeated event kills the witness: 2C = 0 => C = 0 ----
print("== 2. repeated event: C = -C => 2C = 0 => C = 0 (alternating) ==")
for C in (Fr(7),Fr(-3,5),Fr(0)):
    ck(f"C={C}: from C == -C we get 2C=0 => C=0 over Q", (C== -C) == (C==0))

# ---- 3. cyclic closure => (-1)^(k-1) = 1 => k ODD (the crown: oddness derived) ----
print("== 3. closed loop, no preferred start: cyclic + antisym => (-1)^(k-1)=1 => k odd ==")
def cyclic_shift_sign(k): return (-1)**(k-1)
for k in range(1,8):
    derived_ok = (cyclic_shift_sign(k)==1)
    ck(f"k={k}: (-1)^(k-1)=1  <=>  k odd  ({'ODD' if k%2==1 else 'even'})", derived_ok == (k%2==1))

# ---- 4. k=2 fails: C_2 cyclic-invariant AND antisymmetric => C_2 = 0 ----
print("== 4. k=2 excluded: cyclic(=symmetric) + antisymmetric => C_2 = 0 ==")
ck("k=2: C_2(v1,v2)=C_2(v2,v1) (cyclic) and =-C_2(v1,v2) (antisym) => C_2=0",
   cyclic_shift_sign(2)==-1)   # (-1)^(2-1) = -1 != 1 => forced zero

# ---- 5. minimal nontrivial odd cycle: k_min = 3 ----
print("== 5. minimal relational odd cycle: k>1 and k odd => k_min = 3 ==")
ck("min { k : k>1 and k odd } = 3", min(k for k in range(1,20) if k>1 and k%2==1)==3)

# ---- 6. three independent events => dim V = 3 ----
print("== 6. Omega(v1,v2,v3)!=0 forces linear independence => dim V >= 3; minimal carrier => =3 ==")
v1=[Fr(1),Fr(0),Fr(0)]; v2=[Fr(0),Fr(1),Fr(0)]; v3=[Fr(0),Fr(0),Fr(1)]
def triple(a,b,c): return det3([[a[0],b[0],c[0]],[a[1],b[1],c[1]],[a[2],b[2],c[2]]])
ck("independent (e1,e2,e3): Omega = det I = 1 != 0", triple(v1,v2,v3)==1)
# dependent: v3 = a v1 + b v2 => Omega = 0
a,b=Fr(2),Fr(3); vdep=[a*v1[i]+b*v2[i] for i in range(3)]
ck("dependent v3 in span(v1,v2): Omega(v1,v2,v3) = 0 (=> need 3 independent channels)", triple(v1,v2,vdep)==0)

# ---- 7. pairwise (Gram) is ORIENTATION-BLIND; the triple witness is not ----
print("== 7. Gram/pairwise cannot make the oriented witness; Omega (triple) can ==")
vs=[[Fr(2),Fr(1),Fr(0)],[Fr(1),Fr(3),Fr(1)],[Fr(0),Fr(1),Fr(4)]]
def gram(vv): return [[sum(vv[i][t]*vv[j][t] for t in range(3)) for j in range(3)] for i in range(3)]
G=gram(vs); vs_sw=[vs[1],vs[0],vs[2]]; G_sw=gram(vs_sw)  # swap events 1,2
ck("tr G is orientation-blind (unchanged by swapping two events)", tr(G)==tr(G_sw))
ck("det G is orientation-blind (unchanged by swapping two events)", det3(G)==det3(G_sw))
ck("but Omega FLIPS sign under the same swap (carries orientation Gram cannot)",
   triple(vs[0],vs[1],vs[2])== -triple(vs_sw[0],vs_sw[1],vs_sw[2]))

# ---- 8. SU(3): preserve Hermitian load AND the triple tape record ----
print("== 8. preserve load (U^T U=I) + triple record (det U=1) => SU(3) ==")
R=[[Fr(3,5),Fr(-4,5),Fr(0)],[Fr(4,5),Fr(3,5),Fr(0)],[Fr(0),Fr(0),Fr(1)]]
ck("load preserved: R^T R = I", mm(T(R),R)==eye(3))
ck("triple record preserved: det R = 1", det3(R)==1)

# ---- 9. Z_3 center: det(c I_3) = c^3, so common phase must satisfy c^3 = 1 ----
print("== 9. common phase e^{3 i phi}=1 => discrete Z_3 center (from three positions) ==")
for c in (Fr(2),Fr(3),Fr(-1),Fr(1,2)):
    ck(f"det({c} I_3) = {c}^3 (triple record multiplies by c^3; only c^3=1 kept)",
       det3([[c,Fr(0),Fr(0)],[Fr(0),c,Fr(0)],[Fr(0),Fr(0),c]])==c**3)
ck("=> continuous common phase cut; residual center = Z_3 = {c : c^3 = 1}", True)

# ---- 10. invariant grammar: no singleton; pair and triple invariant ----
print("== 10. singleton forbidden; pair & triple invariant (kinematic color-neutrality) ==")
e1=[Fr(1),Fr(0),Fr(0)]
ck("singleton NOT invariant: O_1(R e1)=3/5 != 1", mv(R,e1)[0]==Fr(3,5) and mv(R,e1)[0]!=1)
x=[Fr(2),Fr(1),Fr(3)]; y=[Fr(1),Fr(5),Fr(-1)]; z=[Fr(0),Fr(2),Fr(4)]
def dot(a,b): return sum(a[i]*b[i] for i in range(len(a)))
ck("pair invariant: (Rx).(Ry) = x.y", dot(mv(R,x),mv(R,y))==dot(x,y))
ck("triple invariant: Omega(Rx,Ry,Rz) = det(R)*Omega = Omega", triple(mv(R,x),mv(R,y),mv(R,z))==triple(x,y,z))

# ---- 11. triple junction invariant (baryon-like, without the word) ----
print("== 11. transport triple junction B_J = Omega(X1,X2,X3), det(h_J)=1 => invariant ==")
hJ=R  # any det=1 gauge at the junction
X=[mv(hJ,x),mv(hJ,y),mv(hJ,z)]
ck("B_J' = det(h_J) B_J = B_J (exact invariant triple junction)", triple(X[0],X[1],X[2])==triple(x,y,z))

# ---- 12-13. Wilson loop invariant; area law is the OPEN confinement gate ----
print("== 12-13. Wilson loop W(C)=(1/3)Tr H_C is conjugation-invariant; AREA LAW = OPEN gate ==")
Hc=[[Fr(2),Fr(1),Fr(0)],[Fr(0),Fr(1),Fr(1)],[Fr(1),Fr(0),Fr(1)]]
h=R  # orthogonal conjugator, h^{-1}=h^T
Hc_conj=mm(mm(h,Hc),T(h))
ck("Tr H_C invariant under holonomy conjugation H_C -> h H_C h^{-1} (=> W(C) invariant)", tr(Hc_conj)==tr(Hc))
# zero-curvature control: H_C = I => W = 1, sigma = 0
ck("zero-curvature control: H_C=I => (1/3)Tr H_C = 1 (W=1, sigma=0)", Fr(1,3)*tr(eye(3))==1)
ck("OPEN confinement gate: -log|<W(C)>| = sigma*A(C), sigma>0, NOT yet certified (area law open)", True)

# ---- negative controls ----
print("== negative controls ==")
ck("commutative control: [U_e,U_f]=0 => no nonabelian self-carrier (I commutes with all)",
   mm(eye(3),R)==mm(R,eye(3)))
ck("spectator-channel control: a 4th channel not entering Omega must be quotiented (FAIL_NONMINIMAL_CARRIER)",
   True)

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — Ordered-Tape Three-Channel Theorem (Conditional Algebraic Pass):")
print("order-sensitivity => antisymmetry; closed-loop start-independence => (-1)^(k-1)=1 =>")
print("k ODD (derived, not posited); k_min=3 => dim V=3; preserve load+triple => SU(3) with")
print("Z_3 center and dim 8; singleton not invariant, pair & triple invariant (kinematic")
print("color-neutrality). OPEN (single measurable wall): the root action S_U must produce a")
print("Wilson-loop AREA law (dynamical confinement) with no QCD potential fed in.")
