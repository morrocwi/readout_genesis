#!/usr/bin/env python3
"""
Item 25 -- Attempt 2, 2026-07-24: build the actual "gauge-orbit fluctuation Hessian" DIRECTLY from
THIS REPO's OWN mother equation (docs/root/MOTHER_EQUATION_PHYSICS_MAP.md, docs/engineering/
SPINE_SYSTEM.md), not adapted from an external Z2 precedent (that was nonabelian_gauge_orbit_v1.py,
Attempt 1 -- kept, not superseded, since it establishes the orbit/measure piece this file does not
redo).

WHY THIS FILE EXISTS: the mother equation is
    M d^2Phi + D dPhi + K.L_R.Phi + gradV(Phi) = J - eta      (gauge: d_mu -> D_mu = d_mu + A_mu)
`L_R` is the SAME graph operator Branch 1 (quantum mechanics, docs/root/MOTHER_EQUATION_PHYSICS_MAP.md)
uses to DERIVE the energy spectrum (Th_coqc, InfoSchrodinger: E^2*M = hbar^2*K*lambda for lambda an
eigenvalue of L_R). This session found (Branch 4, just registered in MOTHER_EQUATION_PHYSICS_MAP.md)
that the SM's own discrete connection U_{j<-i} (ROOT_TO_SM_DAG.md R5, Th_coqc) is exactly what the
mother equation's gauge slot A_mu is FOR, but no file anywhere had ever verified the identification
A_mu := U is CONSISTENT -- i.e. that plugging U into the mother equation's own K.L_R.Phi term (via
D_mu) produces a well-defined, gauge-covariant object on the SAME graph.

THIS FILE builds and checks that identification directly: a GAUGE-COVARIANT graph Laplacian
    (L_R^A Phi)_i = deg(i)*Phi_i - sum_{j~i} rho(U_{ij}) Phi_j
on the SAME plaquette lattice and SAME S3 connection as nonabelian_gauge_orbit_v1.py (Attempt 1),
using the natural 3-dim permutation representation rho of S3. This is literally the mother
equation's K.L_R.Phi term with A_mu:=U substituted in, restricted to one static lattice (no time
evolution attempted here -- that is a separate, larger question).

THE QUADRATIC FORM Phi^dagger . L_R^A . Phi IS, by construction, the exact SHAPE item 25 asks for
(a positive-semidefinite quadratic form built from a background connection) -- but built from THIS
repo's own mother equation term, not an externally-adapted analogue (K_ret=M^T G M from the sibling
pi/phi paper, which nonabelian_gauge_orbit_v1.py's honest fence flagged as still a separate,
un-integrated template). If this checks out, it is a genuinely stronger claim than Attempt 1.

Run: python3 gauge_covariant_laplacian_mother_equation_v1.py  (requires numpy)
"""
import itertools
import numpy as np

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print("  finite_diagnostic (exact/numerically-verified linear algebra, reproducible) for the")
print("  construction and gauge-covariance checks; Dr for the interpretation as a step toward")
print("  item 25's fluctuation-Hessian piece.")

# ============================================================================
# (1) Same S3 group and same plaquette lattice as nonabelian_gauge_orbit_v1.py (Attempt 1) --
#     reused, not redefined differently, so the two files describe the SAME object.
print("\n== 1. S3 group and the natural 3-dim permutation representation rho ==")
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
    """Natural 3-dim permutation representation: rho(perm)[i, perm[i]] = 1."""
    M = np.zeros((3, 3))
    for i in range(3):
        M[perm[i], i] = 1.0
    return M

ck("rho is a homomorphism: rho(a).rho(b) == rho(mul(a,b)) (spot check all 36 pairs)",
   all(np.allclose(rho(a) @ rho(b), rho(mul(a, b))) for a in S3 for b in S3))
ck("rho(g) is orthogonal for every g in S3 (rho(g)^T rho(g) = I, permutation matrices)",
   all(np.allclose(rho(g).T @ rho(g), np.eye(3)) for g in S3))
ck("rho(g^-1) == rho(g)^T (orthogonality restated as inverse=transpose)",
   all(np.allclose(rho(inv(g)), rho(g).T) for g in S3))

# ============================================================================
# (2) Same plaquette lattice: 4 vertices, 4 links forming a closed loop (as Attempt 1).
print("\n== 2. same plaquette lattice as Attempt 1: 4 vertices, 4 links, one closed loop ==")
VERTICES = [0, 1, 2, 3]
LINKS = [(0, 1), (1, 2), (2, 3), (3, 0)]   # (i, j): transport i -> j
DEGREE = {v: 0 for v in VERTICES}
for (i, j) in LINKS:
    DEGREE[i] += 1
    DEGREE[j] += 1
ck("every vertex has degree 2 (a simple 4-cycle)", all(d == 2 for d in DEGREE.values()))

# A single fixed connection assignment U: link -> S3 (any nontrivial one; the specific choice is a
# background field, exactly like choosing a specific A_mu to expand the mother equation around).
U = {(0, 1): (1, 2, 0), (1, 2): (0, 2, 1), (2, 3): (2, 0, 1), (3, 0): (1, 0, 2)}
ck("U assigns a group element to each of the 4 links", all(e in U for e in LINKS))

# ============================================================================
# (3) THE GAUGE-COVARIANT LAPLACIAN -- literally the mother equation's K.L_R.Phi term with
#     A_mu := U substituted in, on this lattice, in the representation rho:
#         (L_R^A Phi)_i = deg(i)*Phi_i - sum_{j~i} rho(U_{i->j}) Phi_j   (outgoing links)
#                                        - sum_{j~i} rho(U_{j->i})^T Phi_j  (incoming links, via
#                                          the transpose = inverse, so the operator is symmetric)
print("\n== 3. build L_R^A: the mother equation's K.L_R.Phi term, A_mu := U, on this lattice ==")
N = len(VERTICES)
DIM = 3   # representation dimension
L_R_A = np.zeros((N * DIM, N * DIM))
for v in VERTICES:
    L_R_A[v*DIM:(v+1)*DIM, v*DIM:(v+1)*DIM] = DEGREE[v] * np.eye(DIM)
for (i, j), g in U.items():
    block = rho(g)
    L_R_A[j*DIM:(j+1)*DIM, i*DIM:(i+1)*DIM] -= block
    L_R_A[i*DIM:(i+1)*DIM, j*DIM:(j+1)*DIM] -= block.T

ck("L_R^A is symmetric (a genuine self-adjoint operator, required for a Hessian-shaped quadratic "
   "form)", np.allclose(L_R_A, L_R_A.T))

eigvals = np.linalg.eigvalsh(L_R_A)
ck("L_R^A is positive SEMI-definite (all eigenvalues >= -1e-9, same sign convention as the "
   "ordinary graph Laplacian L_R this repo already uses for Branch 1's quantum derivation)",
   np.all(eigvals >= -1e-9), eigvals.min())

# ============================================================================
# (4) CONSISTENCY CHECK with Branch 1 (quantum mechanics): if U is trivial (every link = identity),
#     L_R^A must reduce EXACTLY to (ordinary graph Laplacian L_R) tensor I_3 -- i.e. this
#     construction is a genuine GENERALIZATION of the object Branch 1 already derives the quantum
#     spectrum from, not an unrelated new object wearing the same name.
print("\n== 4. CONSISTENCY CHECK: U=identity everywhere must reduce to (ordinary L_R) tensor I_3 ==")
U_trivial = {e: ID for e in LINKS}
L_R_A_trivial = np.zeros((N * DIM, N * DIM))
for v in VERTICES:
    L_R_A_trivial[v*DIM:(v+1)*DIM, v*DIM:(v+1)*DIM] = DEGREE[v] * np.eye(DIM)
for (i, j), g in U_trivial.items():
    block = rho(g)
    L_R_A_trivial[j*DIM:(j+1)*DIM, i*DIM:(i+1)*DIM] -= block
    L_R_A_trivial[i*DIM:(i+1)*DIM, j*DIM:(j+1)*DIM] -= block.T

# ordinary (scalar) graph Laplacian of the same 4-cycle, standard definition
L_R_ordinary = np.zeros((N, N))
for v in VERTICES:
    L_R_ordinary[v, v] = DEGREE[v]
for (i, j) in LINKS:
    L_R_ordinary[i, j] -= 1
    L_R_ordinary[j, i] -= 1
L_R_ordinary_tensor_I3 = np.kron(L_R_ordinary, np.eye(DIM))

ck("L_R^A(U=identity) == (ordinary graph Laplacian of the 4-cycle) tensor I_3, EXACTLY "
   "(this construction genuinely generalizes the object Branch 1 already uses, confirmed by direct "
   "matrix equality, not merely asserted)",
   np.allclose(L_R_A_trivial, L_R_ordinary_tensor_I3))
ck("the ordinary L_R's own spectrum on a 4-cycle is the textbook {0, 2, 2, 4} (independent sanity "
   "check of the reduction target itself)",
   np.allclose(sorted(np.linalg.eigvalsh(L_R_ordinary)), [0, 2, 2, 4]))

# ============================================================================
# (5) GAUGE COVARIANCE -- the central check. Under a gauge transformation g: vertex -> S3 (this
#     repo's own G0.4 law, U'_{i->j} = g_j . U_{i->j} . g_i^-1, and Phi_i -> rho(g_i) Phi_i), does
#     L_R^A transform as L_R^A' = R L_R^A R^T for R = block-diag(rho(g_i))? If so, the SPECTRUM of
#     L_R^A (hence the quadratic form Phi^dagger L_R^A Phi up to the gauge choice of Phi's frame)
#     is gauge-invariant -- exactly the property a physical fluctuation Hessian must have.
print("\n== 5. GAUGE COVARIANCE of L_R^A under this repo's own G0.4 transformation law ==")
np.random.seed(0) if False else None  # no RNG allowed in this repo's discipline; use fixed samples
TEST_GAUGES = [
    (ID, ID, ID, ID),
    ((1, 0, 2), ID, ID, ID),
    ((1, 2, 0), (2, 0, 1), (0, 2, 1), (1, 0, 2)),
    ((0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 1, 0)),
]

def transform_connection(U, g):
    return {(i, j): mul(mul(g[j], U[(i, j)]), inv(g[i])) for (i, j) in LINKS}

def build_L(U_dict):
    L = np.zeros((N * DIM, N * DIM))
    for v in VERTICES:
        L[v*DIM:(v+1)*DIM, v*DIM:(v+1)*DIM] = DEGREE[v] * np.eye(DIM)
    for (i, j), g in U_dict.items():
        block = rho(g)
        L[j*DIM:(j+1)*DIM, i*DIM:(i+1)*DIM] -= block
        L[i*DIM:(i+1)*DIM, j*DIM:(j+1)*DIM] -= block.T
    return L

all_covariant = True
all_spectrum_invariant = True
for g_tuple in TEST_GAUGES:
    g = {v: g_tuple[v] for v in VERTICES}
    U_prime = transform_connection(U, g)
    L_prime = build_L(U_prime)
    R = np.zeros((N * DIM, N * DIM))
    for v in VERTICES:
        R[v*DIM:(v+1)*DIM, v*DIM:(v+1)*DIM] = rho(g[v])
    predicted = R @ L_R_A @ R.T
    if not np.allclose(L_prime, predicted, atol=1e-9):
        all_covariant = False
    if not np.allclose(sorted(np.linalg.eigvalsh(L_prime)), sorted(eigvals), atol=1e-9):
        all_spectrum_invariant = False

ck(f"L_R^A transforms covariantly (L_R^A' = R . L_R^A . R^T) under {len(TEST_GAUGES)} distinct "
   f"test gauge transformations (this repo's own G0.4 law applied to the connection U, matched "
   f"against the predicted conjugation of the operator itself -- a genuine algebraic identity, "
   f"not assumed)", all_covariant)
ck(f"the SPECTRUM (eigenvalues) of L_R^A is IDENTICAL before and after every one of the "
   f"{len(TEST_GAUGES)} gauge transformations tested (the physically meaningful, gauge-INVARIANT "
   f"content of the fluctuation operator -- exactly the property a real fluctuation Hessian needs)",
   all_spectrum_invariant)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier finite_diagnostic for the exact linear-algebra construction and checks; Dr for
the interpretation as progress toward item 25):
- WHAT THIS ESTABLISHES: for the first time, an explicit, verified instance of `A_mu := U` inside
  THIS REPO's OWN mother equation's gauge slot (D_mu = d_mu + A_mu, docs/engineering/SPINE_SYSTEM.md)
  on a shared lattice with `domains/standard_model/`'s own connection (ROOT_TO_SM_DAG.md R5, Th_coqc),
  closing Branch 4's named gap (docs/root/MOTHER_EQUATION_PHYSICS_MAP.md, added this session) for
  this one finite test case: (a) the resulting gauge-covariant Laplacian L_R^A is symmetric and
  positive-semidefinite -- a genuine quadratic-form/Hessian-shaped object; (b) it EXACTLY reduces to
  (ordinary graph Laplacian L_R) tensor I_3 when the connection is trivial, i.e. it is a real
  generalization of the SAME object Branch 1 already uses to derive the quantum energy spectrum
  (Th_coqc, InfoSchrodinger), not a differently-named unrelated construction; (c) it transforms
  covariantly under this repo's own already-Th_coqc-proven gauge law (G0.4), and its SPECTRUM is
  verified gauge-invariant across multiple independent test transformations -- the defining physical
  property a fluctuation Hessian must have. This is a stronger, more directly root-native result than
  nonabelian_gauge_orbit_v1.py (Attempt 1), which only built the orbit/measure piece via an adapted
  external technique; this file builds the actual Hessian-shaped OPERATOR, derived from this repo's
  own mother equation term, and checks it against this repo's own pre-existing quantum-mechanics
  result (Branch 1) as an internal consistency anchor.
- WHAT THIS DOES NOT ESTABLISH: (a) SU(3)xSU(2)xU(1) -- S3 remains a small FINITE test group for
  tractability; extending rho and the connection to a continuous Lie group representation is a
  separate, substantially larger undertaking (finite matrix linear algebra does not automatically
  generalize to infinite-dimensional or continuous-parameter representation spaces). (b) any
  Faddeev-Popov ghost sector or orbit-volume-subtraction weighting -- this file computes a
  gauge-covariant quadratic form on the FULL configuration space (not yet projected onto or
  reweighted by the physical/orbit quotient that Attempt 1 separately constructed); combining the
  two (Attempt 1's orbit projector B with this file's L_R^A, e.g. via B^T L_R^A B) is a natural next
  step, NOT YET DONE here. (c) any one-loop coefficient, running, or beta-function content -- this
  is a STATIC quadratic form on one fixed lattice with one fixed background connection, not an
  integral over field configurations, not a determinant, and involves no momentum space or loop
  integral of any kind. (d) any connection to the Yang-Mills mass gap (item 27) -- not attempted,
  not claimed; this file only checks static gauge-covariance properties of an operator, never a
  spectral gap claim, transfer-matrix contraction rate, or vacuum uniqueness statement. (e) items
  25/26 remain FULLY OPEN after this file -- this closes a genuine sub-piece (verifying the mother
  equation's own gauge slot is consistently instantiable by this repo's own SM connection, for one
  finite test case) but is not itself the fluctuation Hessian item 25 ultimately needs (that needs a
  real gauge ACTION, of which this Laplacian term is only one part of the mother equation, and a real
  orbit-volume-weighted integral, not a single fixed-background operator).
- Independently adversarially reviewed, 2026-07-24 -- verdict SURVIVES, no corrections required.
  Reviewer independently re-derived the PSD guarantee from scratch (x^T L_R^A x = sum over edges of
  |x_j - rho(U)x_i|^2, the same structural reason ordinary graph Laplacians are always PSD -- not an
  artifact of the one connection tested here), independently reimplemented the construction with a
  gauge choice not in TEST_GAUGES and confirmed covariance holds (ruling out the "convention
  mismatch masked by symmetry accident" failure mode that produced the sibling Attempt-1 file's real
  bug), and confirmed the U=identity reduction's index/block layout is genuinely consistent, not
  coincidentally matching.
""")
