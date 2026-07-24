#!/usr/bin/env python3
"""
Item 22, extension to 3x3 -- theta_12, theta_13, theta_23 via the Fritzsch (1979) nearest-neighbor
texture, 2026-07-24. Extends today's WORKING 2x2 texture-zero mechanism (gst_mechanism_texture_
zero_v1.py, theta_12 only) to the full 3-generation matrix, per the founder's direction to build on
what already works rather than re-guess independent ad hoc ratios (this morning's failed sqrt(m_c/
m_t), sqrt(m_s/m_b) attempts, which missed PDG by 2-5x -- logged in ITEM22_EXPLORATION_LOG.md).

METHOD, chosen specifically to avoid this session's own sin-vs-tan mistake (gst_mechanism_texture_
zero_v1.py's Part 6 reconciliation): NO hand-derived trig formula is used anywhere in this file.
The matrix is built from its eigenvalues via exact elementary-symmetric-polynomial matching, then
diagonalized NUMERICALLY (ground truth, same method used to resolve the earlier sin/tan discrepancy),
and the mixing readout is taken DIRECTLY as the Born-rule-shaped squared eigenvector overlap -- per
this session's own newly-adopted standing policy (ITEM22_EXPLORATION_LOG.md, "CRIAF corollary,
SIMPLIFIED TO A STANDING POLICY"). No sin(), cos(), tan(), acos(), atan() calls appear anywhere in
this file's PROPOSED readout.

THE TEXTURE (Fritzsch 1979, cited not invented -- real, standard, nearest-neighbor-only symmetric
mass matrix ansatz, a direct generalization of gst_mechanism_texture_zero_v1.py's 2x2 M=[[0,c],[c,b]]
to 3 generations by extending the "no bare self-coupling except the heaviest" idea and "only
adjacent generations couple directly" idea):

    M = [[0, C, 0],
         [C, 0, B],
         [0, B, A]]

Given target eigenvalues {-m1, +m2, +m3} (alternating sign is the standard real-matrix convention
for this texture to reproduce a strong mass hierarchy with real, not complex, parameters -- cited,
not invented), A,B,C are SOLVED exactly from the elementary symmetric polynomials of the
eigenvalues (trace, sum-of-principal-minors, determinant) -- ordinary linear algebra, no fit beyond
the 3 real masses already in fit_calibrated_registry.py.

Run: python3 fritzsch_texture_3x3_v1.py  (requires numpy)
"""
import numpy as np
import math

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 1. inputs: real PDG down-type masses, same registry as item 1/22's other work ==")
m1, m2, m3 = 0.00467, 0.0934, 4.18  # m_d, m_s, m_b (GeV)
print(f"   m1(d)={m1}, m2(s)={m2}, m3(b)={m3}")

print("\n== 2. solve A,B,C from elementary symmetric polynomials of target eigenvalues ==")
print("   (sign pattern searched exhaustively over all 8 combos of +-m1,+-m2,+-m3 -- only")
print("   (+m1,-m2,+m3) and its overall-flip (-m1,+m2,-m3) give a real Fritzsch texture for")
print("   these masses; (-m1,+m2,+m3), naively assumed by analogy to the 2x2 case, does NOT")
print("   admit a real solution here (B^2<0) -- caught by this file's own B^2>0 check below,")
print("   corrected before this file's first run)")
lam = [m1, -m2, m3]
e1 = sum(lam)                                  # trace = A
e2 = lam[0]*lam[1] + lam[0]*lam[2] + lam[1]*lam[2]   # = -C^2 - B^2
e3 = lam[0]*lam[1]*lam[2]                      # = -C^2 * A
A = e1
C_sq = -e3 / A
B_sq = -e2 - C_sq
print(f"   A (trace) = {A:.6f}")
print(f"   C^2 = -det/A = {C_sq:.6e}  =>  C = {math.sqrt(C_sq):.6e}")
print(f"   B^2 = -e2 - C^2 = {B_sq:.6f}  =>  B = {math.sqrt(B_sq):.6f}")
ck("B^2 > 0 (a real B exists for this texture and these masses)", B_sq > 0, B_sq)
ck("C^2 > 0 (a real C exists)", C_sq > 0, C_sq)
B, C = math.sqrt(B_sq), math.sqrt(C_sq)

print("\n== 3. build M and verify NUMERICALLY (ground truth, same method that caught the earlier ==")
print("   sin-vs-tan discrepancy) that it really has eigenvalues -m1,+m2,+m3 ==")
M = np.array([[0, C, 0], [C, 0, B], [0, B, A]])
eigvals, eigvecs = np.linalg.eigh(M)
print(f"   M =\n{M}")
print(f"   eigvals (numpy, sorted ascending) = {eigvals}")
print(f"   target sorted: {sorted(lam)}")
ck("numerically-diagonalized eigenvalues match the target {-m1,+m2,+m3} to high precision",
   all(abs(a - b) < 1e-6 for a, b in zip(sorted(eigvals), sorted(lam))))

print("\n== 4. Born-rule-shaped overlaps (per this session's standing policy -- NO trig functions,")
print("   direct squared eigenvector-component overlap only) ==")
standard_basis = np.eye(3)
# BUG FOUND AND FIXED (self-caught, 2026-07-24): an earlier draft assumed ascending-sorted
# eigenvalue order would be (+m1,-m2,+m3), but ascending order of {0.00467,-0.0934,4.18} is
# actually (-m2,+m1,+m3) -- -m2 is the SMALLEST, not +m1. That mislabeling attached "gen1(+m1)"
# to the -m2 eigenvector and vice versa, producing a bogus 0.93 "theta12" overlap that was really
# the gen2-vs-gen1-flavor-basis overlap mislabeled. FIX: match each label to its eigenvector by
# the CLOSEST actual target eigenvalue, not by assumed sort position.
target_by_label = {"gen1(+m1)": m1, "gen2(-m2)": -m2, "gen3(+m3)": m3}
labels = ["gen1(+m1)", "gen2(-m2)", "gen3(+m3)"]
order = [min(range(3), key=lambda i: abs(eigvals[i] - target_by_label[lbl])) for lbl in labels]
ck("label-to-eigenvector matching is a valid permutation (no two labels map to the same eigenvector)",
   len(set(order)) == 3, order)
overlaps = {}
for idx, lbl in zip(order, labels):
    v = eigvecs[:, idx]
    for i in range(3):
        e_i = standard_basis[i]
        ov = float(np.dot(v, e_i) ** 2)
        overlaps[(lbl, i)] = ov
    row = [overlaps[(lbl, i)] for i in range(3)]
    print(f"   {lbl}: overlaps vs (e1,e2,e3) = {[f'{x:.5f}' for x in row]}, sum={sum(row):.6f}")
    ck(f"{lbl}'s overlaps sum to 1 (Born-rule normalization)", abs(sum(row) - 1) < 1e-9)

print("\n== 5. compare to real PDG mixing magnitudes (sin^2 of PDG central angles, for reference only) ==")
theta12_pdg, theta23_pdg, theta13_pdg = 12.96, 2.38, 0.21  # degrees, PDG-consistent central values
sin2_12_pdg = math.sin(math.radians(theta12_pdg)) ** 2
sin2_23_pdg = math.sin(math.radians(theta23_pdg)) ** 2
sin2_13_pdg = math.sin(math.radians(theta13_pdg)) ** 2
print(f"   PDG sin^2(theta12)={sin2_12_pdg:.6f}, sin^2(theta23)={sin2_23_pdg:.6f}, sin^2(theta13)={sin2_13_pdg:.6f}")
print(f"   (converted from PDG's own degree convention ONLY for this one comparison line -- not")
print(f"   part of this file's own proposed readout, which stays overlap-fraction throughout)")
print(f"   this file's gen1-vs-e2 overlap (candidate theta12 analog): {overlaps[('gen1(+m1)',1)]:.6f}")
print(f"   this file's gen2-vs-e3 overlap (candidate theta23 analog): {overlaps[('gen2(-m2)',2)]:.6f}")
print(f"   this file's gen1-vs-e3 overlap (candidate theta13 analog): {overlaps[('gen1(+m1)',2)]:.6f}")

print("\n== 6. EXPLICIT PASS/FAIL comparison (added per honest-fence's own note that this was")
print("   missing) -- report the honest result, do not smooth over a failure ==")
cand_12 = overlaps[('gen1(+m1)', 1)]
cand_23 = overlaps[('gen2(-m2)', 2)]
cand_13 = overlaps[('gen1(+m1)', 2)]
print(f"   candidate theta12 overlap = {cand_12:.4f}  vs PDG sin^2(theta12) = {sin2_12_pdg:.4f}")
print(f"   candidate theta23 overlap = {cand_23:.4f}  vs PDG sin^2(theta23) = {sin2_23_pdg:.4f}")
print(f"   candidate theta13 overlap = {cand_13:.4f}  vs PDG sin^2(theta13) = {sin2_13_pdg:.4f}")
ck("candidate theta12 overlap is CLOSE to PDG (within a factor of 2)",
   0.5 < cand_12/sin2_12_pdg < 2, cand_12/sin2_12_pdg)
ck("candidate theta23 overlap is CLOSE to PDG (within a factor of 2) -- NOT expected to pass",
   0.5 < cand_23/sin2_23_pdg < 2, cand_23/sin2_23_pdg)
ck("candidate theta13 overlap is CLOSE to PDG (within a factor of 2) -- NOT expected to pass",
   0.5 < cand_13/sin2_13_pdg < 2, cand_13/sin2_13_pdg)
print(f"""   HONEST RESULT, after fixing the label-matching bug found in this same session (2026-07-24):
   theta12 candidate (0.0466) vs PDG (0.0503) -- ratio {cand_12/sin2_12_pdg:.3f}, a GOOD match,
   PASSES the factor-of-2 check. This confirms the Fritzsch 3x3 extension genuinely works for
   theta12, consistent with (and independent evidence for) the 2x2 mechanism's own success in
   gst_mechanism_texture_zero_v1.py.
   theta23 candidate (0.0198) vs PDG (0.0017) -- ratio {cand_23/sin2_23_pdg:.2f}, off by roughly
   11.5x. FAILS.
   theta13 candidate (0.0010) vs PDG (0.0000131) -- ratio {cand_13/sin2_13_pdg:.1f}, off by
   roughly 79x. FAILS badly.
   Reported as found, not smoothed over: this specific Fritzsch texture reproduces theta12 well
   but NOT theta13/theta23. A real, disclosed partial result -- 1 of 3 predictions works.""")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier Dr for the mechanism; finite_diagnostic for the numeric diagonalization itself
-- floating point, reproducible, no extrapolation; the underlying m1,m2,m3 are fit_calibrated
per DEV-SM-001/003):
- SELF-CAUGHT BUG, found and fixed before this file's first review (2026-07-24): an earlier draft
  assigned eigenvector-to-generation labels by assuming ascending-sorted eigenvalue order matched
  (+m1,-m2,+m3) -- WRONG, since `-m2` is numerically the SMALLEST of the three target eigenvalues,
  ascending order is actually `(-m2,+m1,+m3)`. That mislabeling produced a bogus `0.93` "theta12"
  overlap (really the gen2-vs-gen1-basis overlap, mislabeled as gen1-vs-gen2). Fixed by matching
  each label to its eigenvector by closest actual target eigenvalue, not assumed sort position
  (verified: a permutation check now confirms no two labels map to the same eigenvector). This is
  exactly the kind of indexing error the ground-truth-numerical-diagonalization METHOD (chosen
  specifically to avoid the earlier sin-vs-tan hand-algebra mistake) does NOT automatically catch
  -- the diagonalization itself was always correct; only the BOOKKEEPING of which eigenvector
  means which generation was wrong. A lesson for any future multi-generation construction: verify
  label-to-eigenvector assignment explicitly, do not assume sort order matches intended labeling.
- WHAT THIS ESTABLISHES (after the fix): a genuine, checked extension of today's 2x2 texture-zero
  mechanism to a real, standard, cited 3-generation texture (Fritzsch 1979) that WORKS for
  theta12: candidate overlap `0.0466` vs PDG `0.0503`, ratio `0.93`, a good match -- independent
  evidence (a second, different construction) for the same qualitative result
  `gst_mechanism_texture_zero_v1.py` already established via the pure 2x2 sub-case.
- WHAT THIS DOES NOT ESTABLISH: (a) theta23 or theta13 -- Part 6's explicit PASS/FAIL check shows
  theta23 candidate off by ~11.5x and theta13 candidate off by ~79x from PDG, both FAIL. This
  specific Fritzsch texture, with the one real-valued sign pattern it admits for these masses,
  reproduces theta12 but not the other two angles -- a genuine, disclosed PARTIAL result (1 of 3),
  not forced or smoothed over. (b) that the sign pattern chosen for the eigenvalues is the FORCED
  or unique choice -- it was the only real-valued option for THIS texture and these masses, but a
  different texture (different zero pattern) might admit different, better-fitting sign choices.
  (c) that this texture (nearest-neighbor-only, 2 zero entries) is THE correct or unique
  3-generation extension -- other real textures exist in the literature (e.g. different zero
  patterns, or complex-phase textures this real-only construction cannot capture) and were not
  compared; a natural next step given theta12's success. (d) any root-native justification for the
  Fritzsch texture itself, same open status as the 2x2 texture-zero ansatz (DEV-SM-003, H6-
  PROVISIONAL in docs/OPEN_PROBLEM_HYPOTHESES.md). (e) any value for PMNS angles -- untouched,
  same reasons as gst_mechanism_texture_zero_v1.py (item 23 Open, PMNS angles near-maximal not
  hierarchical).
- BYPASSES item 21 (Yukawa coefficients, still fully Open) exactly as cabibbo_angle_gst_v1.py
  does -- substitutes real PDG masses for the not-yet-derived Yukawa couplings.
- Not yet independently adversarially reviewed -- per house discipline, needs that review before
  being treated as more than a first-pass, self-corrected draft.
""")
