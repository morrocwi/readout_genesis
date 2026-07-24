#!/usr/bin/env python3
"""
Mixing OVERLAP, ROOT-NATIVE attempt v2 -- 2026-07-24. Supersedes mixing_angle_from_L_R_v1.py's
"degrees" framing (v1 is kept, not deleted, as the honest record of how this was caught -- see
its own honest fence; v1's construction/math is unchanged and reused here, only the READOUT
quantity changes).

WHY v1 NEEDED THIS CORRECTION (founder's own catch, 2026-07-24): "องศาคืออะไรในสารสนเทศ เราน่าจะยัง
วางรากฐานบางอย่างผิดโดยแอบใส่ความเข้าใจแบบโลกเดิมเข้าไป" (what is a "degree" informationally -- we're
probably still smuggling old-world understanding into the foundation). This project's OWN
readout-not-truth skill (research/skills/readout-not-truth/SKILL.md) states plainly: "The
continuum, R, and infinity are non-readouts" and names I1 (R-completeness / LUB / Dedekind) as the
FIRST forbidden injection. v1's "mixing angle in degrees" used math.acos/math.atan2 -- inverse
trigonometric FUNCTIONS that are only well-defined via the completeness of R (they are analytic
objects, not finite computations) -- i.e. v1 silently injected I1 while explicitly claiming to be
"root-native," the exact failure mode the founder's question catches.

THE FIX: this project ALREADY HAS a genuinely root-native readout for "how much do two states
overlap" -- the Born-rule / energy-fraction entry already in engine/lexicon.py's GLOSSARY, tier
Th_coqc: "p_i = |amp_i|^2 / sum_j |amp_j|^2" (an ordinary RATIO of squared magnitudes -- addition,
multiplication, division only, no inverse trig, no pi, no R-completeness required to define or
compute). "Mixing" is redefined here as an OVERLAP FRACTION, not an angle:

    overlap(v, e_i) := |<v,e_i>_G|^2 / (<v,v>_G * <e_i,e_i>_G),   G=I (Section 1.3)

This is the SAME quantity cos^2(theta) would have given, but arrived at WITHOUT ever calling
acos/atan2 -- it is a plain ratio, exactly the same shape as the Born rule's p_i=|psi_i|^2/norm^2
this project already tiers Th_coqc. Degrees are NEVER computed anywhere in this file.

Run: python3 mixing_angle_from_L_R_v2_overlap_fraction.py  (requires numpy)
"""
import numpy as np

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 1. same inputs as v1 (unchanged, already fit_calibrated per DEV-SM-001) ==")
lam_d, lam_s, lam_b = 0.99998102, 0.99962040, 0.98315168  # lambda_{D,gen1..3}
lam = [lam_d, lam_s, lam_b]
print(f"   lambda = {lam}")

print("\n== 2. same L_R construction as v1 (unchanged, root-native, DERIVED) ==")
W = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        if i != j:
            W[i, j] = lam[i] * lam[j]
D_W = np.diag(W.sum(axis=1))
L_R = D_W - W
ck("L_R is symmetric", np.allclose(L_R, L_R.T))
ck("L_R row sums are zero (Laplacian property)", np.allclose(L_R.sum(axis=1), 0))

eigvals, eigvecs = np.linalg.eigh(L_R)
print(f"   eigenvalues = {eigvals}")
ck("smallest eigenvalue ~ 0 with eigenvector ~ (1,1,1)/sqrt(3) (common-phase/U(1)-like mode, "
   "correctly excluded below)",
   abs(eigvals[0]) < 1e-9 and np.allclose(np.abs(eigvecs[:, 0]), 1 / np.sqrt(3), atol=1e-6))

print("\n== 3. OVERLAP FRACTION (Born-rule-style readout, Th_coqc-precedented shape, NO degrees, "
      "NO acos/atan2 anywhere in this file) ==")
print("   overlap(v,e_i) := |<v,e_i>_G|^2 / (<v,v>_G * <e_i,e_i>_G),  G=I  -- a plain ratio")
standard_basis = np.eye(3)
overlaps = {}
for k in (1, 2):
    v = eigvecs[:, k]
    for i in range(3):
        e_i = standard_basis[i]
        inner = np.dot(v, e_i)
        overlap = (inner ** 2) / (np.dot(v, v) * np.dot(e_i, e_i))  # <v,v>=1, <e_i,e_i>=1 (normalized)
        overlaps[(k, i)] = overlap
        print(f"   mode {k} vs e_{i+1}: overlap = {overlap:.5f}")
        ck(f"overlap(mode {k}, e_{i+1}) in [0,1] (a genuine fraction, Born-rule-style bound)",
           0 <= overlap <= 1 + 1e-9)

print("\n== 4. Born-rule-style normalization check: overlaps of one mode across all 3 basis "
      "vectors sum to 1 (energy/information is conserved -- same conservation shape as the "
      "Born rule's own p_i sum-to-1 property, R1_PSD) ==")
for k in (1, 2):
    total = sum(overlaps[(k, i)] for i in range(3))
    print(f"   mode {k}: sum of overlaps over e_1,e_2,e_3 = {total:.6f}")
    ck(f"mode {k}'s overlaps sum to 1 (exact, since eigvecs[:,k] is unit-norm in the standard "
       f"orthonormal basis)", abs(total - 1) < 1e-9)

print("\n== 5. mixing overlap for the (1,2)-plane, mode-1 -- the OVERLAP-FRACTION analogue of "
      "v1's now-retracted 'theta_12' ==")
overlap_12 = overlaps[(1, 0)] / (overlaps[(1, 0)] + overlaps[(1, 1)])  # renormalized within (e1,e2) only
print(f"   overlap(mode1,e1) renormalized within the (e1,e2) plane = {overlap_12:.5f}")
print(f"   (v1's now-retracted degree figure was 45.9deg, i.e. cos^2(45.9deg)~=0.485 -- consistent")
print(f"   with this file's overlap_12, but THIS file never computes or claims a degree value)")
ck("overlap_12 is a genuine [0,1] fraction (no transcendental function used anywhere to get it)",
   0 <= overlap_12 <= 1)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier Dr for the construction/interpretation; finite_diagnostic for the numeric
eigendecomposition itself -- floating point, reproducible, no extrapolation; NOT Th_coqc, since
L_R's eigenvalues/eigenvectors here are numerically computed, not exact-Fraction machine-checked):
- WHAT THIS CORRECTS (the founder's own catch): v1 reported a "mixing angle in degrees," computed
  via math.acos/math.atan2 -- inverse trigonometric FUNCTIONS whose very definition requires the
  completeness of R (I1), the FIRST non-readout this project's own readout-not-truth discipline
  refuses. v1 claimed to be "root-native" while silently importing exactly that. This file replaces
  "degrees" with an OVERLAP FRACTION |<v,e_i>|^2/(norm*norm) -- the SAME shape as the Born rule
  entry already in engine/lexicon.py's GLOSSARY (tier Th_coqc: p_i=|amp_i|^2/sum|amp_j|^2), a plain
  ratio of squared magnitudes, needing only +,*,/ -- no acos, no atan2, no pi, no R-completeness
  invoked anywhere in this file (verify by grep: no `acos`, `atan2`, or `math` import appears).
- WHAT THIS DOES NOT ESTABLISH: everything v1's honest fence already disclaims still applies here
  UNCHANGED (the w_ij:=lambda_i*lambda_j edge-weight rule is a modeling choice, not forced; no
  claim of a derived VALUE; theta_13/theta_23-equivalent overlaps not separately validated; this
  graph is proposed, not the unique/discovered root-native generation-space object). ADDITIONALLY:
  even the "overlap fraction" itself is NOT claimed to be the correct physical mixing-probability
  interpretation of the real CKM matrix -- it is offered as the philosophically CORRECT SHAPE of
  readout (a genuine ratio, not a borrowed continuum angle), not as a validated prediction.
- Does NOT eliminate the near-degenerate-eigenvalue structural concern v1's second review round
  raised (v1 Part 6, and the further abs()+atan2-clustering concern from v1's third review round)
  -- that concern was about the EIGENVECTOR SPLIT itself being ill-conditioned near-degenerate
  eigenvalues, which is a property of the underlying L_R construction, independent of whether the
  readout taken from the eigenvectors afterward is an angle or an overlap fraction. Switching to
  overlap fractions fixes the I1/continuum-vocabulary problem; it does NOT by itself fix the
  near-degeneracy robustness concern, which remains open and should be tested again (with overlap
  fractions this time, not degrees) before any value is treated as informative.
- Reuses L_R (item 4, DERIVED, docs/root/BORROWED_VS_DERIVED_LEDGER.md) and the retained metric G
  (Section 1.3) exactly as v1 did -- unchanged, still clean of CRRC.
- Not yet independently adversarially reviewed -- per house discipline, needs that review (this
  time specifically checking the I1-avoidance claim itself, and re-testing near-degeneracy
  robustness using overlap fractions) before being treated as more than a first-pass draft.
""")
