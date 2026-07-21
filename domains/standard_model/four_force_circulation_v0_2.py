#!/usr/bin/env python3
"""
Four-Force Circulation Tomography v0.2  —  exact-rational maker-checker.

STATUS (founder): [SimulatedData / FiniteFormalWitness].
The names (G, EM, W, S) are DECODER LABELS in a fixture, NOT forces calibrated
against nature. This script does NOT claim to compute real force transductions.
What it DOES, exactly (fractions.Fraction, no floats except the clearly-fenced
SimulatedData noise experiment in §16):

  A = H + Omega  (symmetric reciprocal load  +  antisymmetric circulation load)
  chi = A^{-1}   (susceptibility / full cross-response)
  and it reads the planted circulation Omega back as the unique ANTISYMMETRIC
  PART of the inverted response, Omega = 1/2 (chi^-1 - chi^-T): exact BY
  CONSTRUCTION (the unique symmetric/antisymmetric split), not by inference.
  The non-trivial content is Theorem 2, chi - chi^T = -2 chi^T Omega chi: the
  MEASURABLE nonreciprocity of the response equals the planted circulation
  conjugated by the full susceptibility. This is a scheme on a KNOWN fixture,
  not tomography of an unknown system.  Genuine failing controls included.

The maker-checker rule: every boxed number in the founder's v0.2 spec is
INDEPENDENTLY recomputed here and asserted; a discrepancy prints FAIL and exits 1.

Run: python3 four_force_circulation_v0_2.py
"""
from fractions import Fraction as Fr

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

# ---------- tiny exact rational 4x4 linear algebra ----------
def mat(rows): return [[Fr(x) for x in r] for r in rows]
def ident(n): return [[Fr(1) if i==j else Fr(0) for j in range(n)] for i in range(n)]
def T(A): return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scal(c,A): return [[c*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mul(A,B):
    n,m,p=len(A),len(B),len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def inv(A):
    n=len(A); M=[row[:]+ident(n)[i] for i,row in enumerate(A)]
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]!=0),None)
        if p is None: return None
        M[c],M[p]=M[p],M[c]
        pv=M[c][c]; M[c]=[x/pv for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]!=0:
                f=M[r][c]; M[r]=[M[r][k]-f*M[c][k] for k in range(2*n)]
    return [row[n:] for row in M]
def det(A):
    n=len(A); M=[row[:] for row in A]; d=Fr(1)
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]!=0),None)
        if p is None: return Fr(0)
        if p!=c: M[c],M[p]=M[p],M[c]; d=-d
        d*=M[c][c]
        for r in range(c+1,n):
            f=M[r][c]/M[c][c]; M[r]=[M[r][k]-f*M[c][k] for k in range(n)]
    return d
def charpoly(A):
    # Faddeev-LeVerrier -> coeffs of det(xI - A) = x^n + c1 x^{n-1} + ... + cn
    n=len(A); Mk=ident(n); c=[Fr(1)]
    for k in range(1,n+1):
        AMk=mul(A,Mk); ck=-sum(AMk[i][i] for i in range(n))/k
        c.append(ck); Mk=add(AMk,scal(ck,ident(n)))
    return c  # length n+1
def frob2(A): return sum(A[i][j]*A[i][j] for i in range(len(A)) for j in range(len(A[0])))

# ---------- the fixture ----------
H = mat([[4,1,0,1],[1,4,1,0],[0,1,4,1],[1,0,1,4]])
Om = scal(Fr(1,2), mat([[0,1,0,-1],[-1,0,1,0],[0,-1,0,1],[1,0,-1,0]]))
A = add(H,Om)
I4 = ident(4)

print("== 1. response operator A = H + Omega ==")
ck("A = H + Omega", eq(A, add(H,Om)))
ck("A[0] = [4, 3/2, 0, 1/2]", A[0]==[Fr(4),Fr(3,2),Fr(0),Fr(1,2)], A[0])
ck("H symmetric", eq(H,T(H)))
ck("Omega antisymmetric", eq(Om, scal(Fr(-1),T(Om))))

print("== 3. stability gate ==")
# H > 0 by Sylvester (all leading principal minors > 0) — exact
minors=[det([H[i][:k] for i in range(k)]) for k in range(1,5)]
ck("H positive-definite (Sylvester minors all > 0)", all(m>0 for m in minors), minors)
# spec(H) = {6,4,4,2}: charpoly == (x-6)(x-4)^2(x-2) = x^4 -16x^3 +92x^2 -224x +192
ck("charpoly(H) = x^4-16x^3+92x^2-224x+192  (spec {6,4,4,2})",
   charpoly(H)==[Fr(1),Fr(-16),Fr(92),Fr(-224),Fr(192)], charpoly(H))
# spec(A) = {6,2,4+i,4-i}: charpoly == (x-6)(x-2)(x^2-8x+17) = x^4-16x^3+93x^2-232x+204
ck("charpoly(A) = x^4-16x^3+93x^2-232x+204  (spec {6,2,4±i}, Re>0)",
   charpoly(A)==[Fr(1),Fr(-16),Fr(93),Fr(-232),Fr(204)], charpoly(A))
ck("det(A) = 204 = 6*2*17", det(A)==204, det(A))

print("== 4. susceptibility chi = A^{-1} (exact) ==")
chi = inv(A)
Mchi = mat([[58,-23,10,-11],[-11,58,-23,10],[10,-11,58,-23],[-23,10,-11,58]])
ck("chi = (1/204) * circulant[58,-23,10,-11]", eq(chi, scal(Fr(1,204), Mchi)))
ck("A * chi = I", eq(mul(A,chi), I4))

print("== 5-8. single-source responses z = chi J  (columns of chi) ==")
def col(M,j): return [M[i][j] for i in range(4)]
ck("z_G  = (1/204)[58,-11,10,-23]^T", col(chi,0)==[Fr(58,204),Fr(-11,204),Fr(10,204),Fr(-23,204)])
ck("z_EM = (1/204)[-23,58,-11,10]^T", col(chi,1)==[Fr(-23,204),Fr(58,204),Fr(-11,204),Fr(10,204)])
ck("z_W  = (1/204)[10,-23,58,-11]^T", col(chi,2)==[Fr(10,204),Fr(-23,204),Fr(58,204),Fr(-11,204)])
ck("z_S  = (1/204)[-11,10,-23,58]^T", col(chi,3)==[Fr(-11,204),Fr(10,204),Fr(-23,204),Fr(58,204)])
# directional ratio |chi_{S<-G}| / |chi_{EM<-G}| = 23/11
ck("|chi_{S<-G}|/|chi_{EM<-G}| = 23/11", abs(chi[3][0])/abs(chi[1][0])==Fr(23,11))
# nonreciprocity chi_{G<-EM} != chi_{EM<-G}
ck("chi_{G<-EM} != chi_{EM<-G}  (nonreciprocal)", chi[0][1]!=chi[1][0])
ck("|chi_{G<-EM}|/|chi_{EM<-G}| = 23/11", abs(chi[0][1])/abs(chi[1][0])==Fr(23,11))

print("== 9-10. two-step reciprocity + antisymmetric susceptibility ==")
ck("chi_{G<-W} = chi_{W<-G}  (two-step reciprocal)", chi[0][2]==chi[2][0]==Fr(10,204))
ck("chi_{EM<-S} = chi_{S<-EM} (two-step reciprocal)", chi[1][3]==chi[3][1]==Fr(10,204))
Dchi = sub(chi,T(chi))
Dexp = scal(Fr(1,17), mat([[0,-1,0,1],[1,0,-1,0],[0,1,0,-1],[-1,0,1,0]]))
ck("chi - chi^T = (1/17)*circulant[0,-1,0,1]", eq(Dchi,Dexp))
ck("screening: D_chi[G,W]=0 and D_chi[EM,S]=0 (opposite pairs)", Dchi[0][2]==0 and Dchi[1][3]==0)

print("== 11. EXACT directed-response identity  chi - chi^T = -2 chi^T Omega chi ==")
rhs = scal(Fr(-2), mul(mul(T(chi),Om),chi))
ck("chi - chi^T = -2 chi^T Omega chi  (exact, not approx)", eq(Dchi, rhs))

print("== 12-13. recover circulation graph from response data ==")
Arec = inv(chi)
Hrec = scal(Fr(1,2), add(Arec,T(Arec)))
Omrec = scal(Fr(1,2), sub(Arec,T(Arec)))
# also via the pure-chi formula Omega = -1/2 chi^{-T} (chi-chi^T) chi^{-1}
Omrec2 = scal(Fr(-1,2), mul(mul(T(inv(chi)),Dchi),inv(chi)))
ck("A_rec = chi^{-1} = A", eq(Arec,A))
ck("H_rec = planted H  (exact)", eq(Hrec,H))
ck("Omega_rec = planted Omega  (exact)", eq(Omrec,Om))
ck("Omega_rec (pure-chi formula) = planted Omega", eq(Omrec2,Om))
# signed edges -> directed cycle G->S->W->EM->G
ck("edge signs: Om[G,EM]=+1/2, Om[EM,W]=+1/2, Om[W,S]=+1/2, Om[S,G]=+1/2",
   Om[0][1]==Fr(1,2) and Om[1][2]==Fr(1,2) and Om[2][3]==Fr(1,2) and Om[3][0]==Fr(1,2))

print("== 14. reciprocal failing control: Omega=0 => chi symmetric => Omega_rec=0 ==")
A0=H; chi0=inv(A0)
Mchi0=mat([[7,-2,1,-2],[-2,7,-2,1],[1,-2,7,-2],[-2,1,-2,7]])
ck("chi_0 = H^{-1} = (1/24)*circulant[7,-2,1,-2]", eq(chi0, scal(Fr(1,24),Mchi0)))
ck("chi_0 = chi_0^T (symmetric)", eq(chi0,T(chi0)))
Om0rec=scal(Fr(1,2), sub(inv(chi0),T(inv(chi0))))
ck("Omega_rec = 0  (no directed circulation discovered)", eq(Om0rec,[[Fr(0)]*4 for _ in range(4)]))

print("== 15. missing-edge control: cut S-G edge, must NOT hallucinate it back ==")
Omcut=[row[:] for row in Om]; Omcut[3][0]=Fr(0); Omcut[0][3]=Fr(0)  # remove S<->G
Acut=add(H,Omcut)
ck("A_cut invertible (det != 0)", det(Acut)!=0, det(Acut))
chicut=inv(Acut); Omcutrec=scal(Fr(1,2), sub(inv(chicut),T(inv(chicut))))
eps=Fr(1,1000000)
ck("recovered |Omega[S,G]| <= eps  (cut edge stays cut)", abs(Omcutrec[3][0])<=eps, Omcutrec[3][0])
ck("surviving edge |Omega[G,EM]| > eps  (real edges kept)", abs(Omcutrec[0][1])>eps, Omcutrec[0][1])
ck("recovered == planted-cut  (exact, no hallucination)", eq(Omcutrec,Omcut))

print("== 17. force-circulation scalar observable  C_F = 1/2 ||chi-chi^T||_F ==")
CF2 = Fr(1,4)*frob2(Dchi)     # C_F^2, exact rational (C_F = sqrt(2)/17 is the irrational surface readout)
ck("C_F^2 = 2/289  (exact; C_F = sqrt2/17 ~ 0.08319)", CF2==Fr(2,289), CF2)
CF2_0 = Fr(1,4)*frob2(sub(chi0,T(chi0)))
ck("Omega=0 => C_F = 0", CF2_0==0)

print("== 18. the three closed identities (summary, all verified above) ==")
ck("Thm1  chi = (H+Omega)^{-1}", eq(chi, inv(add(H,Om))))
ck("Thm2  chi - chi^T = -2 chi^T Omega chi", eq(sub(chi,T(chi)), scal(Fr(-2),mul(mul(T(chi),Om),chi))))
ck("Thm3  Omega = -1/2 chi^{-T}(chi-chi^T)chi^{-1}", eq(Om, scal(Fr(-1,2),mul(mul(T(inv(chi)),sub(chi,T(chi))),inv(chi)))))

# ---------- 16. SimulatedData noise-robustness (clearly fenced, illustrative only) ----------
print("== 16. [SimulatedData] noise-robust reconstruction (illustrative, NOT a claimed result) ==")
import random
def finv(M):  # float inverse, Gauss-Jordan
    n=len(M); A=[[float(M[i][j]) for j in range(n)]+[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
    for c in range(n):
        p=max(range(c,n),key=lambda r:abs(A[r][c])); A[c],A[p]=A[p],A[c]
        pv=A[c][c]; A[c]=[x/pv for x in A[c]]
        for r in range(n):
            if r!=c:
                f=A[r][c]; A[r]=[A[r][k]-f*A[c][k] for k in range(2*n)]
    return [row[n:] for row in A]
def fmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def fT(A): return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
chi_f=[[float(chi[i][j]) for j in range(4)] for i in range(4)]
Om_f=[[float(Om[i][j]) for j in range(4)] for i in range(4)]
Om_fro=(sum(Om_f[i][j]**2 for i in range(4) for j in range(4)))**0.5
true_edges={(0,1),(1,2),(2,3),(3,0),(1,0),(2,1),(3,2),(0,3)}
# PREREGISTERED protocol: noise sigma, ridge lambda, edge threshold, trials
SIGMA=[0.0, 0.002, 0.005]; LAM=1e-3; THRESH=0.02; TRIALS=200; SEED=260721
random.seed(SEED)
print(f"    preregistered: sigma={SIGMA} lambda={LAM} thresh={THRESH} trials={TRIALS} seed={SEED}")
for sg in SIGMA:
    errs=[]; supps=[]
    for _ in range(TRIALS):
        chih=[[chi_f[i][j]+random.gauss(0,sg) for j in range(4)] for i in range(4)]
        # ridge: Ahat = chih^T (chih chih^T + lam I)^{-1}
        G=fmul(chih,fT(chih))
        for i in range(4): G[i][i]+=LAM
        Ahat=fmul(fT(chih),finv(G))
        Omh=[[0.5*(Ahat[i][j]-Ahat[j][i]) for j in range(4)] for i in range(4)]
        num=(sum((Omh[i][j]-Om_f[i][j])**2 for i in range(4) for j in range(4)))**0.5
        errs.append(num/Om_fro)
        rec={(i,j) for i in range(4) for j in range(4) if abs(Omh[i][j])>THRESH}
        supps.append(len(rec & true_edges)/len(true_edges))
    print(f"    sigma={sg}: mean eps_Omega={sum(errs)/len(errs):.4f}  mean SuppAcc={sum(supps)/len(supps):.3f}")
print("    (sigma=0 residual 0.0167 is ridge (lambda=1e-3) BIAS, not recovery error;")
print("     the exact 0-error recovery is the separate exact-rational split in sec 12-13.)")

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — Four-Force Circulation Tomography v0.2:")
print("exact four-sector response chi=(H+Omega)^{-1}, exact directed-response identity")
print("chi-chi^T=-2chi^T Omega chi (measurable nonreciprocity = conjugated circulation),")
print("and Omega_rec=Omega_planted as the unique antisym part of chi^-1 (exact by")
print("construction), with reciprocal + missing-edge failing controls. Fixture scheme.")
print("[SimulatedData/FiniteFormalWitness]: labels are decoder names, not calibrated forces.")
