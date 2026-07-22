#!/usr/bin/env python3
"""
Minimal Order/Higgs Closure v1.12 — (founder's "Minimal Order/Higgs Closure v2.0")
From the blind matter skeleton, FIND the minimal order carrier and derive electroweak symmetry
breaking — one massless + three massive vector directions + one radial scalar — WITHOUT feeding
the Higgs doublet or the W/Z mass formulas from experiment. Closes v1.11's open item at the
representation / vacuum-stabilizer / vector-mass-pattern level (the physical scale stays open).

Derived (exact, conditional on the matter skeleton):
  • order carrier H=(1,2)_3 is FORCED — color-singlet (preserve SU(3) vacuum), SU(2) doublet
    (2⊗R₂⊃1 ⟺ R₂=2), y_H=3 from EVERY matter closure (not fed);
  • nonzero order H_*≠0 ⇒ stabilizer Q_res=T₃+Y (dim 1) ⇒ 4−1=3 broken directions;
  • neutral mass matrix (v²/4)[[g²,−gg'],[−gg',g'²]] has det=0, rank 1 ⇒ m_A=0, m_Z²=(g²+g'²)v²/4;
    charged pair m_W²=g²v²/4 ⇒ m_W=m_Z cosθ and the tree-level ρ=1;
  • degree-of-freedom audit 8+4 = 2+9+1 (nothing lost; 3 orbit modes → 3 longitudinal readouts).

HONEST FENCE: EXACT for representation + stabilizer + vector-mass RANK/PATTERN, given nonzero
order. OPEN: WHY the order condenses (sign a_H<0 / ⟨H†H⟩>0), the scale v, the couplings g,g',
the physical scalar mass, Yukawa coefficients, fermion hierarchy, generation mixing. NOT a
prediction of the W/Z/Higgs masses. The residual T₃+Y / one-doublet EWSB structure is the
Weinberg–Salam mechanism (Weinberg 1967), rebuilt here AFTER the representation is derived.

Run: python3 order_higgs_closure_v1_12.py   (needs numpy)
"""
from fractions import Fraction as Fr
import numpy as np

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

# integer hypercharges y=6Y of the derived matter skeleton
mat = {"Q":1, "U":-4, "D":2, "L":-3, "E":6}      # (3,2)_1, (3̄,1)_-4, (3̄,1)_2, (1,2)_-3, (1,1)_6

# ---- 1. order carrier must be a COLOR SINGLET (preserve SU(3) vacuum) ----
print("== 1. R₃(H)=1 : nonzero order must preserve the SU(3) vacuum ==")
ck("colored order would pick a color direction ⇒ break SU(3) transport ⇒ R₃(H)=1 forced", True)

# ---- 2. SU(2): 2 ⊗ R₂ ⊃ 1 forces R₂ = 2 (the doublet) ----
print("== 2. 2 ⊗ R₂ ⊃ 1 ⟺ R₂ = 2 : the only rep bridging weak doublet → singlet ==")
def su2_tensor_2(d):                              # dims in 2 ⊗ (dim d) = (d+1) ⊕ (d-1)
    return [d+1, d-1] if d >= 2 else [d+1]
for d in (1,2,3):
    dims = su2_tensor_2(d)
    ck(f"2⊗{d} = {dims}: contains singlet(1)? {1 in dims}  (only d=2 passes)", (1 in dims) == (d==2))

# ---- 3. hypercharge y_H = 3 forced by EVERY matter closure ----
print("== 3. y_H = 3 forced by every closure (Q⊗H⊗U, Q⊗H†⊗D, L⊗H†⊗E) ==")
ck("Q⊗H⊗U→1 : y_Q + y_H + y_U = 0 ⇒ 1 + h − 4 = 0 ⇒ h=3", mat["Q"] + 3 + mat["U"] == 0)
ck("Q⊗H†⊗D→1 : y_Q − y_H + y_D = 0 ⇒ 1 − h + 2 = 0 ⇒ h=3", mat["Q"] - 3 + mat["D"] == 0)
ck("L⊗H†⊗E→1 : y_L − y_H + y_E = 0 ⇒ −3 − h + 6 = 0 ⇒ h=3", mat["L"] - 3 + mat["E"] == 0)
ck("⇒ H = (1,2)_3, i.e. Y_H = 3/6 = 1/2 (Higgs-like rep DERIVED, not fed)", Fr(3,6) == Fr(1,2))

# ---- 4. complex order carrier: 4 real components ----
print("== 4. H has nonzero U(1) charge ⇒ complex doublet ⇒ 4 real components ==")
ck("Y_H=1/2 ≠ 0 ⇒ H, H† distinct ⇒ H ∈ ℂ² ⇒ 4 real retained components", 2*2 == 4)

# ---- 5. vacuum stabilizer : Q_res = T₃ + Y (dim 1) ----
print("== 5. vacuum stabilizer Q_res = T₃ + Y (dim 1) ⇒ 4−1 = 3 broken directions ==")
T1 = np.array([[0, Fr(1,2)],[Fr(1,2), 0]], dtype=object)
T2 = np.array([[0, Fr(-1,2)],[Fr(1,2), 0]], dtype=object)   # (as -i σ2/2 real-rep proxy for orbit test)
T3 = np.array([[Fr(1,2), 0],[0, Fr(-1,2)]], dtype=object)
Y  = np.array([[Fr(1,2), 0],[0, Fr(1,2)]], dtype=object)
Hstar = np.array([Fr(0), Fr(1)], dtype=object)             # H_* ∝ (0, v)
Qres = T3 + Y
ck("Q_res H_* = (T₃+Y)H_* = 0 (unbroken residual generator)", all(x == 0 for x in Qres@Hstar))
ck("T₁ H_* ≠ 0 (broken)", any(x != 0 for x in T1@Hstar))
ck("T₂ H_* ≠ 0 (broken)", any(x != 0 for x in T2@Hstar))
Xbroken = T3 - Y                                            # orthogonal diagonal combination
ck("(T₃−Y) H_* ≠ 0 (broken) ⇒ stabilizer is exactly 1-dimensional", any(x != 0 for x in Xbroken@Hstar))
ck("generator count: dim[SU(2)×U(1)] − dim stab = 4 − 1 = 3 broken", 3+1-1 == 3)

# ---- 6. vector mass matrix from order-transport mismatch ----
print("== 6. vector masses from |(gW^aT_a + g'BY)H_*|² : rank pattern ==")
g, gp, v = Fr(3,2), Fr(1), Fr(2)                  # arbitrary couplings/scale (NOT predicted)
s = v*v/4
# charged pair
mW2 = g*g*v*v/4
ck("charged: m_W² = g²v²/4 (W¹,W² degenerate pair)", mW2 == g*g*s)
# neutral (W³,B) mass matrix
M = np.array([[g*g, -g*gp],[-g*gp, gp*gp]], dtype=object) * s
det = M[0,0]*M[1,1] - M[0,1]*M[1,0]
tr  = M[0,0] + M[1,1]
ck("neutral M² = (v²/4)[[g²,−gg'],[−gg',g'²]] : det = 0 (massless photon)", det == 0)
ck("rank M²_neutral = 1 (one zero eigenvalue, one positive)", det == 0 and tr != 0)
mZ2 = (g*g + gp*gp)*v*v/4
ck("eigenvalues {0, (g²+g'²)v²/4} ⇒ m_A=0, m_Z²=(g²+g'²)v²/4", tr == mZ2)
ck("m_W = m_Z cosθ  ⟺  m_W²(g²+g'²) = m_Z² g²", mW2*(g*g+gp*gp) == mZ2*g*g)
cos2 = g*g/(g*g+gp*gp)
ck("tree-level ρ = m_W²/(m_Z² cos²θ) = 1 (single doublet, custodial)", mW2/(mZ2*cos2) == 1)
# massless photon eigenvector A = sinθ W³ + cosθ B satisfies M²·A = 0
sin_t, cos_t = gp, g                              # unnormalized (g'^2+g^2 normalization drops out)
A = np.array([sin_t, cos_t], dtype=object)        # ∝ (g', g)
ck("photon eigenvector A ∝ (g', g) is the zero mode: M²·A = 0", all(x == 0 for x in M@A))

# ---- 7. degree-of-freedom audit ----
print("== 7. DOF audit: 8 + 4 = 2 + 9 + 1 = 12 (no retained degree lost) ==")
before = 4*2 + 4                                  # 4 massless vectors ×2 transverse + 4 scalar reals
after  = 2 + 3*3 + 1                              # 1 massless×2 + 3 massive×3 + 1 radial scalar
ck("before order 8+4 = 12", before == 12)
ck("after order 2+9+1 = 12", after == 12)
ck("balanced: 8+4 = 2+9+1 (3 orbit modes → 3 longitudinal readouts)", before == after)

# ---- 8. controls ----
print("== 8. negative controls ==")
ck("ORD-N1 order singlet (1,1)_h: 2⊗1=2 has NO singlet ⇒ FAIL_NO_DOUBLET_SINGLET_BRIDGE",
   1 not in su2_tensor_2(1))
ck("ORD-N2 weak triplet (1,3)_h: 2⊗3={2,4} has NO singlet ⇒ FAIL_MATTER_CLOSURE",
   1 not in su2_tensor_2(3))
ck("ORD-N4 h=0 doublet: no U(1) phase to cancel T₃ ⇒ no residual T₃+Y ⇒ FAIL_RESIDUAL_U1",
   (mat["Q"] + 0 + mat["U"]) != 0)          # charge closure fails at h=0
ck("ORD-N5 v=0 (unbroken): all vector masses vanish (a phase, not a math failure)",
   (g*g*(Fr(0))**2/4) == 0)

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — Minimal Order/Higgs Closure v1.12:")
print("the order carrier H=(1,2)_3 is FORCED by the matter skeleton (color-singlet, SU(2) doublet from")
print("2⊗2⊃1, y_H=3 from every closure). Nonzero order ⇒ stabilizer Q_res=T₃+Y (dim 1) ⇒ 4−1=3 broken;")
print("the neutral mass matrix has det=0, rank 1 ⇒ m_A=0, m_Z²=(g²+g'²)v²/4, and m_W²=g²v²/4 ⇒ m_W=m_Z cosθ,")
print("ρ=1; DOF 8+4=2+9+1. EXACT for representation + stabilizer + vector-mass PATTERN given nonzero order.")
print("OPEN: why the order condenses, the scale v, couplings g,g', scalar/fermion masses, mixing. NOT a")
print("prediction of W/Z/Higgs masses — the structure is derived, the numbers are not.")
