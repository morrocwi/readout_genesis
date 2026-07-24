#!/usr/bin/env python3
"""
Item 25 -- Attempt 4, 2026-07-24: a genuine LOOP VALUE, computed directly from THIS repo's own
mother equation, for the first time. Extends Attempt 3's split (loop-COUNTING, topological, closed
for item25's test lattice) into loop-VALUATION territory -- but honestly scoped to what this
construction actually gives (a MATTER-loop determinant), not the full gauge-orbit
Faddeev-Popov/ghost determinant item 25 ultimately asks for (a DIFFERENT object, still open).

CORRECTION to a claim in gauge_covariant_laplacian_mother_equation_v1.py's own honest fence: that
file proposed "combining Attempt 1's orbit projector B with this file's L_R^A, e.g. via
B^T L_R^A B" as a natural next step. THAT DOES NOT TYPE-CHECK: B (nonabelian_gauge_orbit_v1.py) is
an isometry on the CONNECTION-CONFIGURATION space (dimension |S3|^4=1296, one axis per possible
link assignment), while L_R^A is an operator on the FIELD space (dimension N_vertices*dim(rho)=12,
one axis per field value at each vertex, for a FIXED background connection). These are two
DIFFERENT vector spaces -- B^T L_R^A B is not a valid matrix product (dimension mismatch). This is
corrected here, not silently dropped: see the HONEST FENCE below for what actually plugs into what.

THE ACTUAL CONSTRUCTION: the standard QFT one-loop effective-action formula for a field with
quadratic action controlled by an operator L (here, THIS repo's own mother-equation term
K.L_R.Phi, gauge-covariantized as L_R^A in Attempt 2) is
    Gamma_1-loop = (1/2) * ln det(L_R^A)              [bosonic/scalar-type field]
On a FINITE lattice (this repo's own discretization, 12x12 here), det(L_R^A) is a finite,
EXACTLY COMPUTABLE NUMBER -- no regularization, no continuum limit, no UV divergence to subtract.
This is therefore a genuine LOOP VALUE (not just a loop count), for the first time, straight from
Attempt 2's already-built, already-reviewed operator, requiring no new machinery.

THE ZERO-MODE SUBTLETY (a real structural fact, checked not assumed): S3's natural 3-dim
permutation representation rho ALWAYS fixes the vector (1,1,1) (any permutation matrix fixes the
all-ones vector) -- so Phi_i=(1,1,1) at every vertex is an EXACT zero mode of L_R^A for ANY
connection U whatsoever (a structural fact of the representation, not an artifact of any specific
U). The standard, well-established convention for a determinant with an exact zero mode (used
throughout QFT/spectral geometry, e.g. zeta-function regularization of the string path integral)
is the FUNCTIONAL DETERMINANT det' := product of the NONZERO eigenvalues only. This file computes
det' explicitly and checks that the zero mode is exactly one-dimensional and exactly (1,1,1)-shaped,
not merely assumed.

Run: python3 loop_value_matter_determinant_v1.py  (requires numpy)
"""
import itertools
import numpy as np

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print("  finite_diagnostic (exact numerical linear algebra on a finite matrix, reproducible, no")
print("  regularization needed) for the determinant computation; Dr for the interpretation as a")
print("  genuine (if narrowly-scoped) 'loop value.'")

# ============================================================================
print("\n== 1. same S3 group, representation, and lattice as Attempt 1/2 (reused, not redefined) ==")
S3 = list(itertools.permutations((0, 1, 2)))
ID = (0, 1, 2)

def mul(a, b):
    return tuple(a[b[i]] for i in range(3))

def inv(a):
    r = [0, 0, 0]
    for i, v in enumerate(a):
        r[v] = i
    return tuple(r)

def rho(perm):
    M = np.zeros((3, 3))
    for i in range(3):
        M[perm[i], i] = 1.0
    return M

VERTICES = [0, 1, 2, 3]
LINKS = [(0, 1), (1, 2), (2, 3), (3, 0)]
DEGREE = {v: 0 for v in VERTICES}
for (i, j) in LINKS:
    DEGREE[i] += 1
    DEGREE[j] += 1
N, DIM = len(VERTICES), 3

def holonomy(U):
    h = ID
    for e in LINKS:
        h = mul(U[e], h)
    return h

def build_L(U):
    L = np.zeros((N * DIM, N * DIM))
    for v in VERTICES:
        L[v*DIM:(v+1)*DIM, v*DIM:(v+1)*DIM] = DEGREE[v] * np.eye(DIM)
    for (i, j), g in U.items():
        block = rho(g)
        L[j*DIM:(j+1)*DIM, i*DIM:(i+1)*DIM] -= block
        L[i*DIM:(i+1)*DIM, j*DIM:(j+1)*DIM] -= block.T
    return L

# ============================================================================
print("\n== 2. STRUCTURAL zero mode: rho(g).(1,1,1) = (1,1,1) for EVERY g in S3 (checked, not ==")
print("      assumed -- any permutation matrix fixes the all-ones vector) ==")
ones3 = np.ones(3)
ck("rho(g) fixes (1,1,1) for ALL 6 elements of S3 (exhaustive check, not a spot sample)",
   all(np.allclose(rho(g) @ ones3, ones3) for g in S3))
print("   => Phi_i=(1,1,1) at every vertex is an EXACT zero mode of L_R^A for ANY connection U --")
print("   a structural fact of the representation itself, independent of U's specific values.")

# ============================================================================
print("\n== 3. choose a CURVED background connection (nontrivial holonomy -- the physically ==")
print("      interesting case, distinct from a pure-gauge/flat connection) ==")
U_CURVED = {(0, 1): (1, 2, 0), (1, 2): (0, 2, 1), (2, 3): (2, 0, 1), (3, 0): (0, 2, 1)}
h = holonomy(U_CURVED)
ck("this connection has NONTRIVIAL holonomy (genuinely curved, not gauge-equivalent to the "
   "trivial connection)", h != ID, h)

L_curved = build_L(U_CURVED)
ck("L_R^A is symmetric (required for a well-defined determinant/spectrum)",
   np.allclose(L_curved, L_curved.T))
eigvals = np.linalg.eigvalsh(L_curved)
ck("L_R^A is positive SEMI-definite (all eigenvalues >= -1e-9, same PSD guarantee Attempt 2 proved "
   "structurally for ANY orthogonal-representation connection)", np.all(eigvals >= -1e-9), eigvals.min())

n_zero = int(np.sum(np.abs(eigvals) < 1e-9))
ck("exactly ONE zero eigenvalue for THIS SPECIFIC curved connection (matching the structural "
   "(1,1,1) mode found in Part 2). CORRECTED after independent review, 2026-07-24: an earlier "
   "draft's comment claimed 'curving the connection always lifts two of the three [flat-case zero "
   "modes], leaving exactly the structural one' as if this were a GENERAL consequence of "
   "nontrivial holonomy -- REFUTED by the reviewer's own scan of 300 independent random curved "
   "connections: only 119/300 (40%) give exactly 1 zero mode, 181/300 (60%) give 2. This file's "
   "particular U_CURVED happens to land in the 1-zero-mode case (confirmed: flat/pure-gauge "
   "connections always give exactly 3 in the reviewer's scan, that part held up) -- the exact "
   "zero-mode count for a given curved connection depends on finer structure (apparently related "
   "to how each link's holonomy interacts with the representation beyond just fixing (1,1,1)) not "
   "captured or claimed here. Only the STRUCTURAL lower bound (>=1 zero mode always, from Part 2) "
   "and THIS connection's specific count (1) are asserted below -- not a general 'curved=>1' rule.",
   n_zero == 1, n_zero)

zero_eigvec = np.linalg.eigh(L_curved)[1][:, 0]
expected_zero_mode = np.tile(ones3, N) / np.linalg.norm(np.tile(ones3, N))
ck("the zero eigenvector matches the predicted (1,1,1)-repeated shape exactly (up to overall sign), "
   "confirming Part 2's structural prediction, not merely counting multiplicities",
   np.allclose(np.abs(zero_eigvec), np.abs(expected_zero_mode), atol=1e-9))

# ============================================================================
print("\n== 4. THE LOOP VALUE: det'(L_R^A) := product of NONZERO eigenvalues (functional ==")
print("      determinant, standard convention for an operator with an exact zero mode) ==")
nonzero_eigs = eigvals[np.abs(eigvals) > 1e-9]
ck("exactly 11 nonzero eigenvalues remain (12 total - 1 structural zero mode)",
   len(nonzero_eigs) == 11, len(nonzero_eigs))
det_prime = float(np.prod(nonzero_eigs))
log_det_prime = float(np.sum(np.log(nonzero_eigs)))
print(f"   det'(L_R^A) = {det_prime:.6f}")
print(f"   ln det'(L_R^A) = {log_det_prime:.6f}")
print(f"   one-loop effective-action contribution (1/2)*ln det'(L_R^A) = {0.5*log_det_prime:.6f}")
ck("det'(L_R^A) > 0 (a genuine, well-defined functional determinant -- all included eigenvalues "
   "strictly positive, PSD plus zero-mode exclusion guarantees this)", det_prime > 0, det_prime)

# ============================================================================
print("\n== 5. GAUGE INVARIANCE of the loop value (the physically essential check) ==")
TEST_GAUGES = [
    (ID, ID, ID, ID),
    ((1, 0, 2), (2, 0, 1), (0, 2, 1), (1, 0, 2)),
    ((0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 1, 0)),
    ((2, 0, 1), (2, 0, 1), (2, 0, 1), (2, 0, 1)),
]

def transform_connection(U, g):
    return {(i, j): mul(mul(g[j], U[(i, j)]), inv(g[i])) for (i, j) in LINKS}

all_invariant = True
for g_tuple in TEST_GAUGES:
    g = {v: g_tuple[v] for v in VERTICES}
    U_prime = transform_connection(U_CURVED, g)
    L_prime = build_L(U_prime)
    eigs_prime = np.linalg.eigvalsh(L_prime)
    nz_prime = eigs_prime[np.abs(eigs_prime) > 1e-9]
    det_prime_transformed = float(np.prod(nz_prime))
    # tolerance tightened after independent review, 2026-07-24: this is exact permutation-matrix
    # (orthogonal representation) arithmetic, which should match to full floating-point precision
    # (~1e-14), not merely 1e-6 -- reviewer independently recomputed and confirmed ~7e-15 relative
    # agreement; a looser tolerance here would have risked silently hiding a real discrepancy
    if abs(det_prime_transformed - det_prime) > 1e-10 * abs(det_prime):
        all_invariant = False

ck(f"det'(L_R^A) is IDENTICAL (to numerical precision) across all {len(TEST_GAUGES)} gauge "
   f"transformations tested -- the loop VALUE is genuinely gauge-invariant, the essential physical "
   f"requirement for it to be a meaningful observable, not an artifact of a gauge choice",
   all_invariant)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print(f"""
HONEST FENCE (tier finite_diagnostic for the exact numerical determinant computation and
gauge-invariance checks; Dr for the physical interpretation):
- CORRECTION to gauge_covariant_laplacian_mother_equation_v1.py's own honest fence: that file
  proposed "B^T L_R^A B" (combining Attempt 1's orbit basis with Attempt 2's operator) as a natural
  next step. This does NOT type-check -- B lives on the 1296-dim CONNECTION-configuration space,
  L_R^A on the 12-dim FIELD space; they are different spaces and cannot be composed this way. That
  proposal is retracted here, not silently dropped. The actual next step, built in THIS file, needs
  no such combination: det'(L_R^A) alone is already a well-defined, computable loop value.
- WHAT THIS ESTABLISHES: for the first time, an actual NUMBER for a "loop" in this repo, computed
  directly from the mother equation's own K.L_R.Phi term (via Attempt 2's L_R^A, A_mu:=U), using
  the standard QFT one-loop formula Gamma_1-loop=(1/2)ln det(operator), with NO regularization
  needed (the lattice is finite, 12x12, so the determinant is an exact finite product, not a
  divergent continuum integral). Value: det'(L_R^A)~={det_prime:.4f} for the tested curved background.
  Confirmed: (a) a structural zero mode exists for ANY connection (S3's rep always fixes (1,1,1)),
  correctly excluded via the standard functional-determinant convention, not hidden; (b) the
  resulting value is exactly gauge-invariant across 4 independent test transformations -- the
  essential physical requirement for this to be a meaningful observable rather than a gauge
  artifact.
- WHAT THIS DOES NOT ESTABLISH: (a) this is a MATTER-loop determinant (integrating out a background
  field Phi in representation rho, coupled to a FIXED external connection U) -- it is explicitly
  NOT the GAUGE-orbit Faddeev-Popov/ghost determinant item 25's missing piece (2) asks for, which
  would integrate over the CONNECTION U itself (weighted by gauge-orbit volume, using Attempt 1's B,
  or the orbit measure it defines) -- a genuinely different variable being integrated, still fully
  open. (b) any regularization/renormalization methodology for the REAL, continuous SU(3)xSU(2)xU(1)
  case, where the analogous determinant would be UV-divergent and require an actual regulator +
  removal procedure (item 26) -- this file's "no regularization needed" only holds because the test
  lattice is finite; the real gauge theory's loop integrals are not automatically finite this way.
  (c) any connection to the loop-KINEMATIC weights (11/3,2/3,1/3) beta_function_coefficients_v1.py
  uses as external, or to the RGE running sm_eff.py already computes -- this is a single, static,
  zero-momentum-transfer determinant on one fixed background, not a beta-function coefficient or a
  running coupling. (d) items 25/26 remain FULLY OPEN -- this is a genuine, narrow loop-VALUE
  computation (distinct from and complementary to Attempt 3's loop-COUNT), not a closure of either
  item; the gauge-orbit ghost/Faddeev-Popov piece and the continuum-limit question are both
  untouched by this file.
- Independently adversarially reviewed, 2026-07-24 -- verdict SURVIVES WITH REQUIRED CORRECTIONS,
  applied above: reviewer confirmed the dimension-mismatch correction (B is 1296x3, L_R^A is 12x12,
  genuinely incompatible, not a strawman), hand-verified the zero-mode arithmetic exactly, and
  independently recomputed gauge-invariance to ~7e-15 relative precision. REAL FINDING (the same
  "narrow example generalized to a claimed pattern" failure mode as an earlier bug in this item25
  chain): scanning 300 random curved connections, only 40% give exactly 1 zero mode (60% give 2) --
  this file's specific U_CURVED happened to land in the 1-zero-mode case; the "curving always lifts "
  two of three" narrative was a real overclaim, now corrected in Part 3 above to state only what is
  actually established (>=1 zero mode always; THIS connection gives exactly 1). Gauge-invariance
  tolerance tightened from 1e-6 to 1e-10 to match the actual exact-arithmetic precision achieved.
""")
