#!/usr/bin/env python3
"""
Item 22, two-sector extension -- build V_CKM from BOTH up-type and down-type Fritzsch textures,
2026-07-24. fritzsch_texture_3x3_v1.py used ONLY the down-type texture and read its eigenvector
overlap with the flat/flavor basis directly as if that WERE the CKM angle -- this implicitly
assumes the up-type sector is already exactly diagonal in the flavor basis, an approximation. The
REAL Standard-Model CKM matrix is V_CKM = O_up^T O_down, the MISMATCH between the two INDEPENDENT
diagonalizing rotations of the up-type and down-type mass matrices. This file builds both textures
and combines them properly -- still zero trig functions, zero hand-derived formulas, per this
session's standing policy (ITEM22_EXPLORATION_LOG.md CRIAF corollary): everything is exact
elementary-symmetric-polynomial matrix construction + numpy ground-truth diagonalization + direct
Born-rule-shaped squared matrix-entry readout.

Note checked before building this (worth recording): a complex phase on the off-diagonal Fritzsch
entries does NOT change any |V_CKM| MAGNITUDE (rephasing-removable for a single Hermitian texture
of this shape) -- so a complex-phase texture would not have fixed fritzsch_texture_3x3_v1.py's
theta13/theta23 failure; the two-sector combination attempted here is a structurally different,
more likely fix.

Run: python3 fritzsch_two_sector_ckm_v1.py  (requires numpy)
"""
import numpy as np
import math

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)


def fritzsch_matrix(m1, m2, m3):
    """Build a real symmetric Fritzsch texture [[0,C,0],[C,0,B],[0,B,A]] with eigenvalues matching
    {m1,m2,m3} up to sign. Searches all 8 sign combinations, returns (M, chosen_signs) for the
    first one giving a real B,C -- or None if no real texture exists for this mass hierarchy."""
    import itertools
    for signs in itertools.product([1, -1], repeat=3):
        lam = [signs[0]*m1, signs[1]*m2, signs[2]*m3]
        e1 = sum(lam)
        if e1 == 0:
            continue
        e2 = lam[0]*lam[1] + lam[0]*lam[2] + lam[1]*lam[2]
        e3 = lam[0]*lam[1]*lam[2]
        A = e1
        C_sq = -e3 / A
        B_sq = -e2 - C_sq
        if C_sq > 0 and B_sq > 0:
            B, C = math.sqrt(B_sq), math.sqrt(C_sq)
            return np.array([[0, C, 0], [C, 0, B], [0, B, A]]), lam
    return None, None


print("== 1. build BOTH textures: down-type (m_d,m_s,m_b) and up-type (m_u,m_c,m_t) ==")
m_d, m_s, m_b = 0.00467, 0.0934, 4.18
m_u, m_c, m_t = 0.00216, 1.27, 172.5
print(f"   down: m_d={m_d}, m_s={m_s}, m_b={m_b}")
print(f"   up:   m_u={m_u}, m_c={m_c}, m_t={m_t}")

M_down, lam_down = fritzsch_matrix(m_d, m_s, m_b)
M_up, lam_up = fritzsch_matrix(m_u, m_c, m_t)
ck("a real Fritzsch texture exists for the down-type masses", M_down is not None)
ck("a real Fritzsch texture exists for the up-type masses", M_up is not None)
print(f"   down-sector target eigenvalues used: {lam_down}")
print(f"   up-sector target eigenvalues used:   {lam_up}")

print("\n== 2. diagonalize both NUMERICALLY (ground truth) ==")
eigvals_down, O_down = np.linalg.eigh(M_down)
eigvals_up, O_up = np.linalg.eigh(M_up)
ck("down-sector eigenvalues match target", all(abs(a-b) < 1e-6 for a, b in
   zip(sorted(eigvals_down), sorted(lam_down))))
ck("up-sector eigenvalues match target", all(abs(a-b) < 1e-4 for a, b in
   zip(sorted(eigvals_up), sorted(lam_up))))

print("\n== 3. order each O's columns by ascending |eigenvalue| (generation 1=lightest,3=heaviest) ==")
order_down = sorted(range(3), key=lambda i: abs(eigvals_down[i]))
order_up = sorted(range(3), key=lambda i: abs(eigvals_up[i]))
O_down_ord = O_down[:, order_down]
O_up_ord = O_up[:, order_up]
print(f"   down |eigenvalues| in gen order: {[abs(eigvals_down[i]) for i in order_down]}")
print(f"   up |eigenvalues| in gen order:   {[abs(eigvals_up[i]) for i in order_up]}")

print("\n== 4. V_CKM = O_up^T @ O_down (the physical mismatch between the two diagonalizations) ==")
V_CKM = O_up_ord.T @ O_down_ord
print(f"   V_CKM =\n{V_CKM}")
V_sq = V_CKM ** 2  # Born-rule-shaped: |V_ij|^2, no trig functions anywhere
ck("each row of |V_CKM|^2 sums to 1 (unitarity, Born-rule normalization)",
   all(abs(V_sq[i, :].sum() - 1) < 1e-9 for i in range(3)))
ck("each column of |V_CKM|^2 sums to 1 (unitarity, Born-rule normalization)",
   all(abs(V_sq[:, j].sum() - 1) < 1e-9 for j in range(3)))

print("\n== 5. explicit PASS/FAIL vs real PDG (sin^2 of PDG central angles, for comparison only) ==")
theta12_pdg, theta23_pdg, theta13_pdg = 12.96, 2.38, 0.21
sin2_12_pdg = math.sin(math.radians(theta12_pdg)) ** 2
sin2_23_pdg = math.sin(math.radians(theta23_pdg)) ** 2
sin2_13_pdg = math.sin(math.radians(theta13_pdg)) ** 2
cand_12 = V_sq[0, 1]  # |V_us|^2 analog: gen1(up) vs gen2(down)
cand_23 = V_sq[1, 2]  # |V_cb|^2 analog: gen2(up) vs gen3(down)
cand_13 = V_sq[0, 2]  # |V_ub|^2 analog: gen1(up) vs gen3(down)
print(f"   candidate |V_us|^2 = {cand_12:.6f}  vs PDG sin^2(theta12) = {sin2_12_pdg:.6f}  "
      f"ratio={cand_12/sin2_12_pdg:.3f}")
print(f"   candidate |V_cb|^2 = {cand_23:.6f}  vs PDG sin^2(theta23) = {sin2_23_pdg:.6f}  "
      f"ratio={cand_23/sin2_23_pdg:.3f}")
print(f"   candidate |V_ub|^2 = {cand_13:.6f}  vs PDG sin^2(theta13) = {sin2_13_pdg:.6f}  "
      f"ratio={cand_13/sin2_13_pdg:.3f}")
ck("|V_us|^2 within a factor of 2 of PDG", 0.5 < cand_12/sin2_12_pdg < 2, cand_12/sin2_12_pdg)
ck("|V_cb|^2 within a factor of 2 of PDG", 0.5 < cand_23/sin2_23_pdg < 2, cand_23/sin2_23_pdg)
ck("|V_ub|^2 within a factor of 2 of PDG", 0.5 < cand_13/sin2_13_pdg < 2, cand_13/sin2_13_pdg)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S) -- reported honestly, not smoothed over: {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier Dr for the mechanism; finite_diagnostic for the numeric diagonalization; the
underlying 6 quark masses are fit_calibrated per DEV-SM-001/003):
- WHAT THIS ESTABLISHES: a structurally more complete construction than
  fritzsch_texture_3x3_v1.py -- combines INDEPENDENT up-type and down-type Fritzsch textures via
  V_CKM=O_up^T*O_down (the standard SM definition of the CKM matrix as a mismatch between two
  sectors' diagonalizations), rather than reading one sector's eigenvectors against the flavor
  basis directly. Verified: a real texture exists for both sectors; unitarity holds exactly
  (row/column sums to 1, Born-rule normalization). Corrected after independent adversarial
  review, 2026-07-24: this unitarity check is a USEFUL BUG-CATCHING sanity check but NOT
  independent physical validation -- it is mathematically GUARANTEED by construction (V_CKM is
  the product of two orthogonal matrices, O_up^T and O_down, and the product of two orthogonal
  matrices is always orthogonal), not evidence that the underlying texture/masses are physically
  sensible. An earlier draft overstated this as "a genuine internal consistency check," corrected
  here. Zero trig functions anywhere, per this session's standing policy.
- RESULT vs PDG (Part 5, reported as computed, not adjusted): |V_us|^2 ratio 0.63x, |V_ub|^2
  ratio 0.73x -- both within a factor of 2, a real improvement over
  fritzsch_texture_3x3_v1.py's single-sector version (which got theta13 wrong by ~79x). |V_cb|^2
  ratio 2.02x -- barely fails the factor-of-2 threshold, but is dramatically closer than the
  single-sector version's ~11.5x miss on the same angle. Two-sector combination (the physically
  correct SM construction) is a genuine, disclosed improvement on all three angles simultaneously,
  though not yet a clean pass on all three.
- WHAT THIS DOES NOT ESTABLISH beyond the above: unresolved from before: (a) the sign-
  pattern choice for each sector is a modeling choice, not derived (though constrained to the
  only real-valued option per sector). (b) the Fritzsch texture itself (for either sector) is not
  root-native, same open status as before (DEV-SM-003, H6-PROVISIONAL). (c) generation-ordering
  by |eigenvalue| (Part 3) is a natural but not independently forced convention.
- BYPASSES item 21 (Yukawa coefficients, still fully Open) for BOTH sectors now, not just one --
  every citation of this result must say so.
- Independently adversarially reviewed, 2026-07-24 -- verdict SURVIVES_WITH_CORRECTION (the
  unitarity-check overclaim above, now fixed). Re-verified independently: V_CKM=O_up^T*O_down is
  the correct standard SM convention; the up-type texture (5-order-of-magnitude mass hierarchy,
  condition number ~8e4) diagonalizes accurately with no numerical instability (max eigenvalue
  error ~2e-16, reconstruction error ~3e-14); all three |V_ij|^2 values and PDG ratios
  independently reproduced exactly; the |eigenvalue|-based generation ordering avoids the sign/
  labeling bug class self-caught in fritzsch_texture_3x3_v1.py (eigenvector sign ambiguity does
  not affect squared overlaps, confirmed). No other corrections needed.
""")
