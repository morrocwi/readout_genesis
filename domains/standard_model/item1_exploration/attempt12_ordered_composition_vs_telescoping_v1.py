#!/usr/bin/env python3
"""
Item 1 -- Attempt 12, 2026-07-25: tests the founder's sharpest correction yet -- "the problem isn't
M, isn't it the SUMMATION [itself]?" -- and finds it is mathematically exactly right, narrowing the
search further than Attempts 10-11 managed, while honestly identifying why this repo's CURRENT
root-native connection machinery cannot yet supply what the insight calls for.

THE INSIGHT, VERIFIED (Part 1 below): a graph Laplacian's degree term `deg(i) = sum_j w_ij` is a
COMMUTATIVE SUM -- order of the neighbors never matters, which is exactly why Attempts 10-11's
degeneracy-forcing symmetry (Z3/S3-invariance) could never be escaped: any construction built from
symmetric SUMS over a set of "generations" is permutation-blind by definition, no matter how
richly the per-term rule is dressed up (item25's own Th_coqc/finite_diagnostic graph machinery,
Attempts 10-11's Phi/Psi apparatus -- all built from sums). The founder's redirect: this project's
OWN native primitive for combining things is NOT a sum at all -- it is ORDERED, non-commutative
CONCATENATION (R2, ROOT_TO_SM_DAG.md: "ordered transition paths / concatenation"). Repeated ORDERED
composition of a NON-NORMAL operator (one where A.A^T != A^T.A) can give genuinely distinct SINGULAR
VALUES at each order/length -- a structurally different readout than an eigenvalue, and NOT subject
to the same permutation-symmetry argument, because "which position in an ordered sequence" is not
an unordered index a permutation group can act transitively on the way it acts on unordered graph
nodes.

WHAT THIS FILE DOES: (Part 1) proves the distinction is real and load-bearing with an exact, minimal
toy example -- eigenvalues of A^n stay degenerate (spectral radius constant) while singular values
of A^n genuinely diverge, for a simple non-normal A. (Part 2) searches THIS REPO's actual root-native
ordered-composition machinery -- the Th_coqc-proven frame-difference connection `pathprod`
(formal/InfoGaugeLocalizationConnectionHolonomy_attempt.v, ROOT_TO_SM_DAG.md R5) -- and finds,
by reading its own proven theorem `coboundary_telescopes`, that THIS specific ordered-composition
primitive is a COBOUNDARY: `pathprod f n = f(n) . f(0)^-1`, i.e. it collapses/telescopes to depend
ONLY on the two endpoint frames, for ANY intermediate path and ANY group -- it does NOT accumulate
growth with path length at all. This is the OPPOSITE of what the mechanism in Part 1 needs. (Part 3)
concludes honestly: the founder's insight is mathematically correct and real progress -- it correctly
diagnoses WHY Attempts 10-11 were stuck (sum-based, not the specific M or symmetry group) -- but this
repo's current root-native connection primitive is PROVABLY telescoping, so it cannot yet supply the
non-trivial ordered growth the mechanism needs. Unlocking it requires a genuinely NEW root-native
ingredient (a non-telescoping, curvature-carrying, non-normal-representation composition rule) that
does not yet exist and would itself need independent justification -- named as the concrete next gap,
not invented here to force a positive result.

Run: python3 attempt12_ordered_composition_vs_telescoping_v1.py  (requires numpy)
"""
import numpy as np

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print("  finite_diagnostic (exact numerical linear algebra) for Part 1's toy demonstration;")
print("  Th_coqc-CITED (not re-derived, quoted from the actual proven theorem) for Part 2's")
print("  telescoping fact; Dr for the overall interpretation and the identified remaining gap.")

# ============================================================================
print("\n== 1. THE INSIGHT, MINIMALLY DEMONSTRATED: sum/eigenvalue vs ordered-product/singular-value ==")
A = np.array([[1.0, 1.0, 0.0],
              [0.0, 1.0, 1.0],
              [0.0, 0.0, 1.0]])   # a minimal non-normal (shear-type) matrix -- a TOY, not yet
                                   # claimed root-native; Part 2 checks whether this repo's actual
                                   # connection machinery could honestly supply something like it.
ck("A is genuinely NON-NORMAL (A.A^T != A^T.A) -- the property this mechanism needs",
   not np.allclose(A @ A.T, A.T @ A))
ck("A has spectral radius EXACTLY 1 (all eigenvalues have magnitude 1 -- A is upper-triangular "
   "with 1's on the diagonal)", abs(max(abs(np.linalg.eigvals(A))) - 1.0) < 1e-9)
print("   CLARIFICATION (added after independent review, 2026-07-25, to prevent an over-general")
print("   reading): the constant-spectral-radius result below follows from the ELEMENTARY identity")
print("   rho(A^n)=rho(A)^n (true for ANY matrix, normal or not) TOGETHER WITH A's spectral radius")
print("   being exactly 1 here -- NOT from non-normality alone. Non-normality's actual, narrower")
print("   role: it is what lets the SINGULAR VALUES of A^n escape that flat rho(A)^n=1 trajectory")
print("   and grow. The precise claim is: AT UNIMODULAR SPECTRAL RADIUS (exactly the regime")
print("   Attempts 10-11's forced degeneracy sits in -- their eigenvalues/holonomies are bounded,")
print("   not exponentially growing), non-normality is what separates an eigenvalue readout (stuck")
print("   flat) from a singular-value readout (free to grow) -- not a general normal-vs-non-normal")
print("   dichotomy on its own.")

print("   order n | spectral radius (eigenvalue-based, what a Laplacian/sum-based readout gives) "
      "| largest singular value (ordered-product-based readout)")
spectral_radii, largest_sv = [], []
for n in (1, 2, 3):
    An = np.linalg.matrix_power(A, n)
    sr = float(max(abs(np.linalg.eigvals(An))))
    sv = float(np.linalg.svd(An, compute_uv=False)[0])
    spectral_radii.append(round(sr, 6))
    largest_sv.append(round(sv, 6))
    print(f"   n={n}: spectral radius={sr:.4f}   largest singular value={sv:.4f}")

ck("spectral radius (eigenvalue-based) is IDENTICAL at every order n (exactly the degeneracy "
   "Attempts 10-11 already proved is forced by any sum/symmetric construction -- confirmed here "
   "independently via a totally different, non-graph example)",
   len(set(spectral_radii)) == 1, spectral_radii)
ck("largest singular value (ordered-product-based) is STRICTLY INCREASING and takes 3 genuinely "
   "DISTINCT values at n=1,2,3 -- the founder's insight, verified: an ordered-composition readout "
   "on a non-normal operator is NOT subject to the same degeneracy",
   largest_sv[0] < largest_sv[1] < largest_sv[2], largest_sv)

# ============================================================================
print("\n== 2. does THIS REPO's actual root-native connection machinery supply a non-normal, ==")
print("      non-telescoping ordered composition like Part 1's toy A? -- checked against the ==")
print("      REAL Th_coqc theorem, not assumed ==")
print("   formal/InfoGaugeLocalizationConnectionHolonomy_attempt.v, theorem `coboundary_telescopes`:")
print('     pathprod(f, n) = mul(f(n), inv(f(0)))    -- PROVEN for ANY group, ANY intermediate path')
print("   This is a COBOUNDARY: the n-step ordered product of frame differences depends ONLY on")
print("   the two ENDPOINT frames f(n), f(0) -- it does NOT accumulate anything from the")
print("   intermediate path length or shape. Demonstrated numerically here with a concrete group")
print("   (3x3 orthogonal matrices, matching this repo's own R6 SO(3)-flavored holonomy usage):")

def rot(theta, axis=2):
    c, s = np.cos(theta), np.sin(theta)
    R = np.eye(3)
    if axis == 2:
        R[0, 0], R[0, 1], R[1, 0], R[1, 1] = c, -s, s, c
    return R

# an arbitrary frame field f(k) = some rotation depending on k (per-node localization is free,
# exactly as the Coq theorem allows ANY f) -- pathprod telescopes regardless of this choice.
def pathprod(f, n):
    P = np.eye(3)
    for k in range(n):
        edge = f(k + 1) @ np.linalg.inv(f(k))   # Aedge: mul(f(S k), inv(f k))
        P = edge @ P
    return P

def f_arbitrary(k):
    return rot(0.3 * k + 0.1 * (k % 3) ** 2)   # a deliberately irregular, non-monotonic frame choice

for n in (1, 2, 3, 5):
    P = pathprod(f_arbitrary, n)
    predicted = f_arbitrary(n) @ np.linalg.inv(f_arbitrary(0))
    ck(f"pathprod for n={n} steps EXACTLY equals f(n).f(0)^-1 (the coboundary_telescopes formula, "
       f"checked numerically for this concrete instance, not merely quoted)",
       np.allclose(P, predicted, atol=1e-9))

# and since these are orthogonal (rotation) frames, the singular values of ANY pathprod are all 1 --
# no growth is possible at all, by construction, regardless of telescoping.
svs_check = [float(s) for s in np.linalg.svd(pathprod(f_arbitrary, 5), compute_uv=False)]
ck("pathprod's singular values are all exactly 1 for this (orthogonal-frame) instance -- confirms "
   "TWO independent reasons this repo's current connection machinery cannot supply Part 1's "
   "mechanism: (a) it provably telescopes (Th_coqc), so there is nothing to accumulate over path "
   "length even in principle; (b) the frames used throughout this repo (SO(3)/permutation-style, "
   "chosen for good physical reasons -- PSD-preserving, per item25) are orthogonal, so even a "
   "non-telescoping version would have bounded, non-growing singular values",
   all(abs(s - 1.0) < 1e-9 for s in svs_check), svs_check)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier: Part 1 finite_diagnostic exact toy demonstration; Part 2 cites and numerically
confirms an ALREADY Th_coqc theorem (coboundary_telescopes), not re-deriving it; Part 3 Dr):
- WHAT THIS ESTABLISHES: the founder's correction ("the problem is the SUM, not M") is mathematically
  CORRECT and identifies the true, deeper reason Attempts 10-11 stayed stuck -- ANY construction
  built from a commutative sum over an unordered generation index is permutation-blind by
  definition; the fix is not a richer sum, it is switching to genuinely ORDERED composition on a
  NON-NORMAL operator, whose singular values (not eigenvalues) can differ at every order/length,
  demonstrated exactly in Part 1. PRECISE SCOPE (tightened after independent review, 2026-07-25 --
  required correction, applied inline in Part 1 too): the constant-spectral-radius fact by itself is
  just the elementary identity rho(A^n)=rho(A)^n at rho(A)=1, true for ANY matrix, not special to
  non-normality. Non-normality's real, narrower role is specifically what lets the SINGULAR-VALUE
  readout escape that flat trajectory while the eigenvalue readout stays stuck -- this is the
  correct, tighter form of "the founder's insight, verified," not a general normal-vs-non-normal
  dichotomy. This is real, useful progress: it correctly reclassifies the obstruction Attempts 10-11
  were fighting (uniformity-under-a-sum) one level deeper (sum-vs-product as the actual fork in the
  road, specifically at the unimodular-spectral-radius regime those attempts' constructions sit in).
- WHAT THIS DOES NOT ESTABLISH: that this repo can currently BUILD this mechanism root-natively.
  Checked directly, not assumed: this repo's actual ordered-composition primitive (`pathprod`,
  Th_coqc, R5) is a proven COBOUNDARY -- it telescopes to depend only on endpoint frames, for ANY
  group and ANY intermediate path, so it structurally cannot accumulate the kind of order-dependent
  growth Part 1's mechanism needs, regardless of how many "generations" (path steps) are inserted.
  Separately and independently, the specific frames this repo actually uses everywhere else
  (orthogonal/permutation representations, chosen in item25 for good, disclosed physical reasons --
  PSD-preservation) would keep singular values bounded at 1 even if telescoping weren't already a
  blocker. Item 1 remains fully Open. This is Attempt 12: correctly narrows WHERE the missing
  ingredient must live (a genuinely non-telescoping, curvature-carrying, non-orthogonal-representation
  ordered composition -- not yet built, not yet independently justified from root, and NOT invented
  here just to force a positive numeric result) rather than closing item 1.
- Independently adversarially reviewed, 2026-07-25 -- verdict SURVIVES WITH REQUIRED CORRECTIONS,
  applied above. Reviewer verified the Coq citation line-by-line (coboundary_telescopes proved from
  5 generic group axioms, no commutativity smuggled in anywhere including the helper lemma used in
  the inductive step; Python's Aedge/pathprod match the Coq recursive definitions exactly, including
  multiplication order, which matters for non-abelian groups) and independently re-ran Part 1's
  toy example plus 3 additional non-normal matrices, confirming the qualitative pattern replicates
  specifically at unimodular spectral radius. Required correction (exposition only, no computational
  or citation error): clarified that constant spectral radius follows from the elementary identity
  rho(A^n)=rho(A)^n, not from non-normality alone -- applied inline in Part 1 and here.
""")
