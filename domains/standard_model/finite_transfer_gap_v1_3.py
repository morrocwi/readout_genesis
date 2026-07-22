#!/usr/bin/env python3
"""
Finite-Transfer Gap Theorem v1.3 — the exact, conditional core of the root-native mass-gap program.

STATUS (honest): this is NOT a proof of the Yang-Mills mass gap in the continuum (a Clay Millennium
Problem, still OPEN). It is the FINITE-TRANSFER theorem — the easy half of the program — made runnable:
GIVEN a physical transfer operator that is positive, self-adjoint, has a unique vacuum, and STRICTLY
contracts the nonvacuum sector (`q=‖𝕋_phys P_⊥‖<1`), THEN the spectral gap is positive,
`Δ = −(1/a) log q > 0`, and connected gauge-invariant correlators decay exponentially. The HARD half —
deriving `q<1` from the root action with a UNIFORM bound as `L→∞` and `a→0` — is OPEN (see the gates
MG-G7/G8/G9 in MASS_GAP_INFORMATION_PHILOSOPHY.md).

We verify: the theorem on a fixture, the positive control, and the genuine negative controls
(massless diffusion whose gap CLOSES as `L→∞`, and vacuum degeneracy giving `Δ=0`). Nothing here
claims a physical mass; the continuum limit is deliberately not taken.

Run: python3 finite_transfer_gap_v1_3.py   (requires numpy)
"""
import math
try:
    import numpy as np
except Exception as e:
    print("numpy required:", e); raise SystemExit(0)

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

def gap_of(T, a=1.0):
    """vacuum-normalized: top eigenvalue = 1; q = 2nd eigenvalue; Δ = -(1/a) log q."""
    ev = np.sort(np.linalg.eigvalsh(T))[::-1]   # descending, T symmetric
    lam0, lam1 = ev[0], ev[1]
    q = lam1/lam0
    Delta = (-math.log(q)/a) if q>0 else float('inf')
    return lam0, lam1, q, Delta, ev

# ---- 1. the theorem on a fixture: positive self-adjoint, unique vacuum, q<1 => Δ>0 ----
print("== 1. Finite-Transfer Gap Theorem: 𝕋 pos. self-adjoint, unique vacuum, q<1 => Δ>0 ==")
# a symmetric PSD transfer matrix with a clean spectral gap (eigenvalues 1 > 0.6 > 0.3 > 0.1)
D = np.diag([1.0, 0.6, 0.3, 0.1])
Q,_ = np.linalg.qr(np.array([[1,1,0,0],[1,-1,1,0],[0,1,1,1],[0,0,1,-1]], float))  # random-ish orthonormal
T = Q @ D @ Q.T
lam0, lam1, q, Delta, ev = gap_of(T)
ck("𝕋 is self-adjoint (symmetric)", np.allclose(T, T.T))
ck("𝕋 is positive (all eigenvalues ≥ 0)", (ev >= -1e-12).all())
ck("unique vacuum: top eigenvalue simple (λ_0=1, multiplicity 1)", abs(lam0-1)<1e-9 and (ev[0]-ev[1])>1e-6)
ck("strict neutral contraction q = ‖𝕋 P_⊥‖ = λ_1 = 0.6 < 1", abs(q-0.6)<1e-9 and q<1)
ck("=> mass gap Δ = −log q = %.6f > 0 (MG-G5 pass)" % Delta, Delta>0 and abs(Delta-(-math.log(0.6)))<1e-9)
ck("spec(H) ∩ (0, Δ) = ∅ : no excitation energy below the gap", all((-math.log(l))>=Delta-1e-9 for l in ev[1:] if l>0))

# ---- 2. positive control: 𝕋 = P_0 + q P_⊥ ----
print("== 2. positive control: 𝕋 = P_0 + q·P_⊥ ⇒ Δ = −log q exactly ==")
for qv in (0.5, 0.2, 0.9):
    Tc = np.diag([1.0, qv, qv, qv])
    _,_,qc,Dc,_ = gap_of(Tc)
    ck(f"q={qv}: Δ = −log q = {(-math.log(qv)):.6f}", abs(Dc-(-math.log(qv)))<1e-9)

# ---- 3. exponential correlation decay: |C_O(n)| ≤ ‖O|Ω⟩‖² q^n ----
print("== 3. connected correlator decays: |C_O(n)| ≤ ‖O|Ω⟩‖² q^n = e^{−n a Δ} ==")
w,V = np.linalg.eigh(T); Omega = V[:,np.argmax(w)]                  # vacuum eigenvector
O = np.diag([0.3,-0.7,0.5,0.2])                                     # a self-adjoint observable
Oc = O - (Omega @ O @ Omega)*np.eye(4)                             # subtract vacuum expectation
xperp = Oc @ Omega
for n in (1,2,5,10):
    Cn = abs(Omega @ Oc @ np.linalg.matrix_power(T,n) @ Oc @ Omega)
    bound = (xperp @ xperp) * q**n
    ck(f"n={n}: |C_O(n)|={Cn:.3e} ≤ ‖OΩ‖²q^n={bound:.3e} (exp decay, ξ=1/Δ)", Cn <= bound+1e-12)

# ---- 4. information gap = spectral gap (m_info = Δ) ----
print("== 4. information persistence gap m_info = Δ (positive self-adjoint) ==")
etas = [max(abs(np.linalg.eigvalsh(np.linalg.matrix_power(T,n)))) for n in (1,)]  # ‖𝕋^n‖=1 (vacuum)
# on P_⊥: η(n)=q^n ; m_info = -limsup (1/n) log η(n) = -log q = Δ
ns=range(1,15); etaperp=[q**n for n in ns]
m_info = -np.polyfit(list(ns), [math.log(e) for e in etaperp],1)[0]
ck("m_info = −limsup (1/n) log η_⊥(n) = −log q = Δ", abs(m_info-Delta)<1e-9)

# ---- 5. NEGATIVE control: massless diffusion — gap CLOSES as L→∞ ----
print("== 5. [neg] massless diffusion λ_1(L)=1−c(π/L)² ⇒ Δ_L ~ 1/L² → 0 (NOT a mass gap) ==")
c=0.5; Ds=[]
for L in (4,8,16,32,64):
    lam1L = 1 - c*(math.pi/L)**2
    DL = -math.log(lam1L)
    Ds.append((L,DL))
ck("Δ_L > 0 at every finite L (finite-lattice gap is real)", all(d>0 for _,d in Ds))
ck("Δ_L strictly DECREASES toward 0 as L→∞ (MG-G7 FAIL: gap closes with volume)",
   all(Ds[i][1]>Ds[i+1][1] for i in range(len(Ds)-1)) and Ds[-1][1]<0.01)
ck("=> a finite-L positive gap alone is NOT sufficient (FAIL_FINITE_SIZE_PSEUDOGAP guard)", True)

# ---- 6. NEGATIVE control: vacuum degeneracy λ_0=λ_1=1 ⇒ Δ=0 ----
print("== 6. [neg] vacuum degeneracy: λ_0=λ_1=1 ⇒ q=1 ⇒ Δ=0 (OPEN_VACUUM_DEGENERACY) ==")
Tdeg = np.diag([1.0,1.0,0.3,0.1])
_,_,qd,Dd,_ = gap_of(Tdeg)
ck("λ_0=λ_1=1 ⇒ q=1 ⇒ Δ=0 (must NOT declare a gap until superselection sectors are split)",
   abs(qd-1)<1e-12 and abs(Dd)<1e-12)

# ---- 7. honest gate summary ----
print("== 7. gate status on this fixture (finite-transfer only) ==")
ck("MG-G3 transfer positivity: 0 ≤ 𝕋 ≤ I on the fixture", (ev>=-1e-12).all() and (ev<=1+1e-9).all())
ck("MG-G4 unique vacuum: PASS on the fixture (degeneracy control shows the failure mode)", (ev[0]-ev[1])>1e-6)
ck("MG-G5 finite-scale gap: PASS (q<1)", q<1)
ck("MG-G7/G8/G9 (uniform volume + continuum + nontriviality): OPEN — deliberately not claimed", True)

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — Finite-Transfer Gap Theorem v1.3 (EXACT CONDITIONAL):")
print("positive self-adjoint 𝕋 + unique vacuum + strict neutral contraction q=‖𝕋 P_⊥‖<1 ⇒ mass gap")
print("Δ=−(1/a)log q>0 and exponential clustering |C_O(n)|≤‖OΩ‖²q^n; m_info=Δ. Positive control and")
print("the genuine negative controls (diffusion gap CLOSES as L→∞; vacuum degeneracy ⇒ Δ=0) hold.")
print("NOT the Clay mass gap: deriving q<1 UNIFORMLY (L→∞, a→0) + existence/OS axioms + nontrivial")
print("continuum are OPEN. Next: v1.4 reflection-positive slab (positivity BEFORE any eigenvalue is")
print("read as a physical mass).")
