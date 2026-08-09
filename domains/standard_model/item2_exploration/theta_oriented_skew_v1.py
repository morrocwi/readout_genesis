#!/usr/bin/env python3
"""
Theta ORIENTED SKEW EXTENSION v1 -- step 5.5 of THETA_ROOT_PROGRAM.md (PRIMARY branch
only, per orchestrator ruling 2026-08-09; the Q(i)/mu_4 FALLBACK branch is NOT built here --
no theta_oriented_gaussian_*.py file exists in this repo, and none should).

CRRC GUARD (binding, checked by inspection): no edge, orientation, weight, skew value,
or cyclic product computed anywhere in this file is ever identified with a generation,
CKM entry, mixing angle, or family-slot count. J_Theta is read out purely as a
topological/index-set quantity of the declared graph object. Its identification with
5.4's Cq quartet-J (the complex Jarlskog-type invariant) is an UNBUILT admissibility
square -- declared [Open], Q3 identity-by-role discipline: w_e, a_e, J_Theta, k_color,
n_gen stay distinct symbols throughout.

TIER MAP (declared up front, honest fence):
  Th_coqc        -- NONE in this file (Coq witness is a separate file/agent's job;
                    this is the Python exact-and-numeric verifier only).
  finite_diagnostic -- Part 7 (the decisive multistart-Newton coupled living-FP
                    search): FLOATS, fixed seeds, disclosed below, tolerance 1e-10
                    residual / 1e-2 living-Psi threshold, matching the existing
                    theta_dynamics_selection_v1.py / theta_minimal_living_v1.py
                    convention exactly (same discipline, same file family).
  Dr (exact, sympy/Fraction-checked, general-argument sketch not yet Coq-formalized)
                 -- Parts 1-6: linear-independence census, regression test, skew-
                    source identity, Z2 gauge invariance, tree gauge-fixing, and the
                    B1/B2-transfer supporting identities. ALL of these are EXACT
                    (fractions.Fraction, no floats) random-trial verifications of
                    general algebraic claims -- not floating numerics, but also not
                    yet machine-checked as universally-quantified Coq theorems (that
                    is Step 2 of the playbook, a separate file).

DECLARED REGIME (unchanged from 5.2b-1/5.2b-2, stated once, used throughout Part 7):
  a = -1, b = 1, K = mu = 1, J_ext = 0 (no external drive), R_Phi = R_Psi = 0
  (closed system, no boundary current). "Living" fixed point := Psi != 0 AND Phi not
  proportional to Psi (unchanged meaning from every prior Theta file).

DISCLOSED FLOATS / FIXED SEEDS (Part 7 only; everything else is exact Fraction/sympy):
  K3   (n=3, all 3 edges, the re-verification target 5.4 named): seed=550, 3000 trials
  C4   (n=4, the 4-cycle, the newly-tractable escape hatch):    seed=551, 3000 trials
  P3   (n=3, support {(0,1),(0,2)}, CONTROL -- 5.2b-1's known symmetric-only living
        support, re-run here under the EXTENDED dynamics to see if the repair changes
        anything on a support with NO cycle, where J_Theta is undefined by construction):
                                                                  seed=552, 3000 trials
  Newton: numeric Jacobian via forward differences h=1e-7, up to 100 iterations,
  convergence threshold residual < 1e-13 (early stop) / living-accept threshold
  residual < 1e-10, ||Psi|| > 1e-2, cross-product(Phi,Psi) > 1e-6 (not proportional).

  DISCLOSURE (repair-review MAJOR finding, fixed): earlier printed output rounded
  J_Theta to 6 decimal places, which silently displayed any |J_Theta| < 5e-7 as
  "0.000000" -- e.g. a genuine, non-artifactual C4 fixed-point cluster with
  |J_Theta| approx 2.6e-14 (confirmed a real isolated root, not float noise, by an
  independent reviewer's 60-digit mpmath re-solve) would read as exactly zero at
  that precision. FIXED: per-FP J_Theta now prints in scientific notation, and each
  support's block ends with a magnitude-spread summary (min/max |J_Theta| over all
  nonzero-J FPs found, plus the support's worst Newton residual) so the FULL spread
  -- not just the largest values -- is visible directly in this file's own output.
  A downstream reader (e.g. the Step 4 THETA_ROOT_PROGRAM.md writeup) MUST use that
  full spread, not a hand-picked subset, when characterizing "how nonzero" a
  support's found J_Theta values are.

REPAIR UNDER TEST (the load-bearing fix this whole file exists to verify, orchestrator
ruling 1 + repaired-design section 1): the original ("Route B") construction let
a_e be computed on EVERY ordered pair in V x V, independent of whether w_e > 0 --
a confirmed bug two of three independent judges missed. THE REPAIR: A[a]'s support
is forced identical to L[w]'s support -- a_e := 0 for every {i,j} NOT IN the declared
edge set E, by construction, not by a separate optimization. Part 2 below is the
literal regression test guarding this repair (spec Step 1b, "the single most
load-bearing repair in this whole design" per the playbook's own Step 6 checklist).

NAMED OPEN ITEMS (carried forward, not resolved here):
  [Open] quartetJ-identification square -- whether THIS file's real J_Theta(C) (an
    oriented-cyclic-product-of-a_e readout) can be identified with 5.4's complex
    Cq quartet-J (the CP-signed Jarlskog-type invariant) is an entirely separate,
    unbuilt admissibility square. Finding J_Theta != 0 here would NOT automatically
    close it -- a new square must be built and Coq-checked first (CRRC guard).
  [Open] 5.6 untied reframing -- orchestrator ruling 2: the BOLDER "untied" construction
    (a_e defined over the full C(n,2) index set independent of L's support, closing
    the census differently) is logged here as a NAMED FUTURE CANDIDATE STEP (5.6),
    not pursued in this file. 5.5 is the support-tied repair ONLY.
  [Open] full diagonal-rescaling gauge invariance -- Part 4/5 below verify Z2
    (sign-flip) gauge invariance only, per orchestrator ruling design section; the FULL
    continuous diagonal-rescaling group is Route B's own inherited, unresolved risk
    #2, not attempted here.
  [Open] V=U_A^dagger*U_B eigenbasis bridge -- REMAINS FORBIDDEN as a J readout in
    this file (orchestrator ruling 4, gauge-artifact trap, two routes converged on this
    independently). Not used anywhere below; flagged as future work needing its own
    gauge-invariance square if ever revisited, since L+A is genuinely non-symmetric
    and its eigenpairs can be genuinely complex.

ROOT-NATIVITY ANCHOR (verified verbatim against READOUT_GENESIS_CORE.md by the
synthesis pass that produced the design spec this file implements; not re-verified
against the source by this Python file itself -- that check is out of scope for a
numeric verifier and is carried as inherited context):
    Reader:  M dt^2 Phi_n + D dt^c Phi_n + K G[Theta_n]   Phi_n + grad V(Phi_n) - J_n = R_Phi,n
    Record:  M dt^2 Psi_n - D dt^c Psi_n + K G[Theta_n]^T Psi_n + grad^2 V(Phi_n) Psi_n = R_Psi,n
  The record's coupling to G is the operator's LITERAL TRANSPOSE, not a conjugate-
  transpose/dagger -- this is why this PRIMARY branch needs no field extension, no
  Wirtinger calculus, and no complexification: G[Theta] := L[w] + A[a] is already a
  real, generally non-symmetric matrix, and G^T = L[w] - A[a] falls straight out of
  L symmetric / A antisymmetric. omega = [[0,1],[-1,0]] is the corpus's own
  pre-existing pairing object (named alongside eta = [[0,1],[1,0]]), used below only
  as a bookkeeping identity, never as an imported physics claim.

THE EXTENDED STATIONARITY IDENTITY -- derived on paper here, then machine-verified
exactly in Part 6, THEN checked numerically at every found living FP in Part 7
(orchestrator ruling 3c, the mandatory B1/B2 transfer sub-task):

  Write G := L[w] + A[a] (reader operator), so record uses G^T = L[w] - A[a]
  (L symmetric, A antisymmetric, both tied to the SAME support E, per the repair).
  Reader_i := K*(G Phi)_i + a*Phi_i + b*Phi_i^3
  Record_i := K*(G^T Psi)_i + (a + 3*b*Phi_i^2)*Psi_i

  THE B1 BALANCE LAW TRANSFERS EXACTLY, FOR A MORE GENERAL REASON THAN 5.2b-1 NEEDED:
    combo := <Psi,Reader> - <Phi,Record>
           = K*(Psi^T G Phi - Phi^T G^T Psi) + a*(Psi.Phi - Phi.Psi)
             + b*<Psi,Phi^3> - 3*b*<Phi,Phi^2 . Psi>
    The scalar identity  Psi^T G Phi == Phi^T G^T Psi  holds for ANY n x n matrix G
    (it is nothing but "a 1x1 matrix equals its own transpose"), NOT only for
    symmetric G -- 5.2b-1's proof used G=G^T as a special case of this more general
    fact without stating it that way. So the K-term vanishes identically regardless
    of the skew part A, the a-term vanishes trivially (Psi.Phi=Phi.Psi), and
        combo == -2*b*<Phi^3,Psi>   EXACTLY, UNCHANGED, even with A != 0.
    Hence: at ANY J=0 static fixed point of the EXTENDED (L+A)-coupled system with
    b != 0, <Phi^3,Psi> = 0 is STILL FORCED. B1 transfers unchanged. Verified
    exactly (Fraction, random trials, ANY w/a, not only Gate-D-stationary ones) in
    Part 6c below, and re-checked numerically at every living FP found in Part 7.

  B2 (SYMMETRY IS DEAD) ALSO TRANSFERS, BUT VIA A GENUINELY NEW MECHANISM, NOT THE
  OLD "graph term cancels" ARGUMENT (which does NOT survive verbatim -- disclosed):
    S^{e,skew} := Phi_i*Psi_j - Phi_j*Psi_i vanishes IDENTICALLY whenever Psi = c*Phi
    for ANY scalar c (both the agree case c=1 and the mirror case c=-1) -- it is the
    2x2 determinant of two proportional vectors. So at EITHER symmetric configuration,
    Gate-D stationarity (mu*a_e* = -K*S^{e,skew}) forces a_e* = 0 on every edge,
    hence A[a]=0 identically, G collapses back to the plain symmetric L[w], and
    5.2b-1's ORIGINAL B2 proof (both the agree-case and mirror-case arguments)
    applies to that reduced system VERBATIM. Conclusion unchanged: a living
    (Psi != 0) fixed point of the extended system is necessarily NOT-symmetric
    (Psi not proportional to +/-Phi) yet balanced (B1) -- but the ROUTE is new:
    the old mirror-case argument relied on K*(G-G^T)=0 by G's symmetry, which is
    FALSE in general once A != 0 (G-G^T = 2A != 0 off a proportional configuration);
    what actually rescues the conclusion is that A itself is forced to 0 exactly
    where the old argument needed it. Verified exactly in Part 6d below.

Run: python3 theta_oriented_skew_v1.py   (stdlib + sympy(unused directly, Fraction
only) for exact parts; float multistart Newton for Part 7; a few minutes)
"""

from fractions import Fraction as Fr
from itertools import combinations
import math
import random

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


# --------------------------------------------------------------------------------
# Shared exact-arithmetic building blocks (Fraction throughout Parts 1-6).
# --------------------------------------------------------------------------------

def all_pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def L_e_matrix(e, n):
    """Symmetric single-edge Laplacian L_e (existing, Th_coqc elsewhere)."""
    i, j = e
    M = [[Fr(0)] * n for _ in range(n)]
    M[i][i] += 1
    M[j][j] += 1
    M[i][j] -= 1
    M[j][i] -= 1
    return M


def A_e_matrix(e, n):
    """Antisymmetric single-edge oriented generator A_e = e_i e_j^T - e_j e_i^T,
    e=(i,j) with i<j -- support-tied construction: this function is only ever
    called with e drawn from the declared support E, never a free pair."""
    i, j = e
    M = [[Fr(0)] * n for _ in range(n)]
    M[i][j] += 1
    M[j][i] -= 1
    return M


def build_L(support, w, n):
    M = [[Fr(0)] * n for _ in range(n)]
    for e in support:
        i, j = e
        we = w[e]
        M[i][i] += we
        M[j][j] += we
        M[i][j] -= we
        M[j][i] -= we
    return M


def build_A(support, a, n):
    """THE REPAIR, literally: a_e is only ever read for e in `support`; every
    other matrix entry is left at its Fraction(0) initial value by construction --
    there is no code path here that can populate an off-support entry."""
    M = [[Fr(0)] * n for _ in range(n)]
    for e in support:
        i, j = e
        ae = a[e]
        M[i][j] += ae
        M[j][i] -= ae
    return M


def flatten(M):
    return [x for row in M for x in row]


def exact_rank(vectors):
    """Exact rank of a list of equal-length Fraction vectors via Gaussian elim."""
    if not vectors:
        return 0
    m = [row[:] for row in vectors]
    rows, cols = len(m), len(m[0])
    rank = 0
    for col in range(cols):
        piv = None
        for r in range(rank, rows):
            if m[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        pivval = m[rank][col]
        m[rank] = [v / pivval for v in m[rank]]
        for r in range(rows):
            if r != rank and m[r][col] != 0:
                factor = m[r][col]
                m[r] = [v - factor * u for v, u in zip(m[r], m[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def rand_frac(rng, lo=-6, hi=6, dlo=1, dhi=5):
    return Fr(rng.randint(lo, hi), rng.randint(dlo, dhi))


# --------------------------------------------------------------------------------
print("== 1. L_e, A_e census + exact-rank linear independence "
      "(n=3 all 8 supports, n=4 four named supports) ==")
# --------------------------------------------------------------------------------

EDGES3 = [(0, 1), (0, 2), (1, 2)]
supports_n3 = []
for k in range(len(EDGES3) + 1):
    for c in combinations(EDGES3, k):
        supports_n3.append(list(c))

supports_n4 = {
    "K3-embedded (isolated vertex 3)": [(0, 1), (0, 2), (1, 2)],
    "C4 (4-cycle)": [(0, 1), (1, 2), (2, 3), (0, 3)],
    "P4 (path)": [(0, 1), (1, 2), (2, 3)],
    "star (center 0)": [(0, 1), (0, 2), (0, 3)],
}

ok = True
for sup in supports_n3:
    vecs = [flatten(L_e_matrix(e, 3)) for e in sup] + [flatten(A_e_matrix(e, 3)) for e in sup]
    r = exact_rank(vecs)
    if r != 2 * len(sup):
        ok = False
ck("n=3: {L_e} U {A_e} linearly independent on all 8 supports (rank == 2|E| exactly)",
   ok)

ok = True
detail = {}
for name, sup in supports_n4.items():
    vecs = [flatten(L_e_matrix(e, 4)) for e in sup] + [flatten(A_e_matrix(e, 4)) for e in sup]
    r = exact_rank(vecs)
    detail[name] = (r, 2 * len(sup))
    if r != 2 * len(sup):
        ok = False
ck("n=4: {L_e} U {A_e} linearly independent on K3/C4/P4/star (rank == 2|E| exactly)",
   ok, detail)
print("  ==> the census's own 𝔾=𝔾^(+)+𝔾^(-) split instantiates concretely: for a "
      "fixed support E, {w_e,a_e}_{e in E} are independent coordinates.")

# --------------------------------------------------------------------------------
print("== 2. REGRESSION TEST guarding the repair: a_e forced to 0 off support ==")
# --------------------------------------------------------------------------------
rng = random.Random(9001)
ok = True
checked_pairs = 0
for n, supports in [(3, supports_n3), (4, list(supports_n4.values()))]:
    full = all_pairs(n)
    for sup in supports:
        a_vals = {e: Fr(rng.randint(-9, 9), rng.randint(1, 6)) for e in sup}
        A = build_A(sup, a_vals, n)
        off_support = [e for e in full if e not in sup]
        for (i, j) in off_support:
            checked_pairs += 1
            if A[i][j] != 0 or A[j][i] != 0:
                ok = False
ck(f"for every support E and every pair NOT in E, a_ij forced to 0 by construction "
   f"({checked_pairs} off-support pairs checked across 12 supports)", ok)

# --------------------------------------------------------------------------------
print("== 3. Exact skew-source identity: S^{e,skew} = Phi_i*Psi_j - Phi_j*Psi_i "
      "== X_i^T omega X_j (150 random rational trials) ==")
# --------------------------------------------------------------------------------
omega = [[Fr(0), Fr(1)], [Fr(-1), Fr(0)]]
rng = random.Random(1234)
ok = True
for _ in range(150):
    Pi, Si = rand_frac(rng), rand_frac(rng)
    Pj, Sj = rand_frac(rng), rand_frac(rng)
    Xi = [Pi, Si]
    Xj = [Pj, Sj]
    # X_i^T . omega . X_j, computed literally via the omega matrix (not the shortcut)
    tmp = [sum(Xi[k] * omega[k][l] for k in range(2)) for l in range(2)]
    val = sum(tmp[l] * Xj[l] for l in range(2))
    skew = Pi * Sj - Pj * Si
    if val != skew:
        ok = False
ck("S^{e,skew} = Phi_i*Psi_j - Phi_j*Psi_i == X_i^T omega X_j exactly, 150 trials", ok)

# --------------------------------------------------------------------------------
print("== 4. Z2 telescoping gauge invariance of J_Theta on K3 (n=3) and C4 (n=4) ==")
# --------------------------------------------------------------------------------


def directed_a(a_dict, p, q):
    if p < q:
        return a_dict[(p, q)]
    return -a_dict[(q, p)]


# ORIENTATION NOTE (repair-review finding, non-defect, disclosed per house discipline):
# J_Theta's SIGN (never its nonzero-ness) depends on the arbitrary choice of
# cycle-traversal direction. Reversing the cycle multiplies the product by (-1)^m
# where m = cycle length: an ODD cycle (K3, m=3) flips sign under reversal; an EVEN
# cycle (C4, m=4) does not. This is exactly the "orientation-odd cyclic product"
# the orchestrator ruling already names -- not a bug, just spelled out here explicitly so a
# future reader of the Step 4 writeup does not mistake a K3 sign for something a
# different traversal convention would preserve.
def cyclic_product(a_dict, cycle):
    prod = Fr(1)
    m = len(cycle)
    for t in range(m):
        p, q = cycle[t], cycle[(t + 1) % m]
        prod *= directed_a(a_dict, p, q)
    return prod


def z2_transform(a_dict, eps):
    return {e: eps[e[0]] * eps[e[1]] * a_dict[e] for e in a_dict}


rng = random.Random(4242)
cycle_k3 = [0, 1, 2]
sup_k3 = [(0, 1), (0, 2), (1, 2)]
ok = True
for _ in range(200):
    a_dict = {e: rand_frac(rng, -6, 6, 1, 4) for e in sup_k3}
    eps = {v: rng.choice([1, -1]) for v in range(3)}
    J = cyclic_product(a_dict, cycle_k3)
    Jp = cyclic_product(z2_transform(a_dict, eps), cycle_k3)
    if J != Jp:
        ok = False
ck("Z2 gauge invariance of J_Theta on K3 (n=3): 200 random (a,eps) trials, exact", ok)

rng = random.Random(4343)
cycle_c4 = [0, 1, 2, 3]
sup_c4 = [(0, 1), (1, 2), (2, 3), (0, 3)]
ok = True
for _ in range(200):
    a_dict = {e: rand_frac(rng, -6, 6, 1, 4) for e in sup_c4}
    eps = {v: rng.choice([1, -1]) for v in range(4)}
    J = cyclic_product(a_dict, cycle_c4)
    Jp = cyclic_product(z2_transform(a_dict, eps), cycle_c4)
    if J != Jp:
        ok = False
ck("Z2 gauge invariance of J_Theta on C4 (n=4): 200 random (a,eps) trials, exact", ok)

# --------------------------------------------------------------------------------
print("== 5. Tree-gauge-fixing: eps_c := eps_p * sign(a_pc) drives every transformed "
      "tree weight >= 0 (P3/star n=3, P4/star n=4) ==")
# --------------------------------------------------------------------------------


def fsign(x):
    return 1 if x >= 0 else -1


def bfs_tree_order(support, root, n):
    adj = {v: [] for v in range(n)}
    for (i, j) in support:
        adj[i].append(j)
        adj[j].append(i)
    seen = {root}
    order = []  # list of (parent, child)
    queue = [root]
    while queue:
        p = queue.pop(0)
        for c in adj[p]:
            if c not in seen:
                seen.add(c)
                order.append((p, c))
                queue.append(c)
    return order


def check_tree_gauge_fix(support, root, n, a_dict):
    """eps_c := eps_p * sign(a_pc) where a_pc is the PARENT-TO-CHILD directed
    entry A[p][c] (root-outward orientation) -- the well-posed reading of the
    design formula, since an antisymmetric matrix entry's sign is only
    meaningful once a direction is fixed. Verified along that SAME direction
    (not the canonical i<j storage order, which can disagree in sign whenever
    a tree edge's parent index exceeds its child index)."""
    order = bfs_tree_order(support, root, n)
    eps = {root: 1}
    for (p, c) in order:
        eps[c] = eps[p] * fsign(directed_a(a_dict, p, c))
    for (p, c) in order:
        transformed = eps[p] * eps[c] * directed_a(a_dict, p, c)
        if transformed < 0:
            return False, transformed
    return True, None


trees_n3 = {
    "star/path @ (0,1)-(0,2)": [(0, 1), (0, 2)],
    "star/path @ (0,1)-(1,2)": [(0, 1), (1, 2)],
    "star/path @ (0,2)-(1,2)": [(0, 2), (1, 2)],
}
trees_n4 = {
    "P4 path": [(0, 1), (1, 2), (2, 3)],
    "star center 0": [(0, 1), (0, 2), (0, 3)],
}

rng = random.Random(5151)
ok = True
for name, sup in trees_n3.items():
    for _ in range(200):
        a_dict = {e: rand_frac(rng, -9, 9, 1, 4) for e in sup}
        good, bad = check_tree_gauge_fix(sup, 0, 3, a_dict)
        if not good:
            ok = False
ck("n=3 tree gauge-fixing (3 labelings x 200 trials): every transformed tree weight "
   ">= 0 exactly", ok)

rng = random.Random(5252)
ok = True
for name, sup in trees_n4.items():
    for _ in range(200):
        a_dict = {e: rand_frac(rng, -9, 9, 1, 4) for e in sup}
        good, bad = check_tree_gauge_fix(sup, 0, 4, a_dict)
        if not good:
            ok = False
ck("n=4 tree gauge-fixing (P4 + star x 200 trials): every transformed tree weight "
   ">= 0 exactly", ok)
print("  ==> Claim 2 (tree-triviality) now validly scoped: since A's support IS L's "
      "support (the repair), 'no cycle in L's support' and 'no cycle in A's support' "
      "are the SAME statement -- the confirmed Route-B bug is closed.")

# --------------------------------------------------------------------------------
print("== 6. Exact supporting identities for the B1/B2 transfer derivation "
      "(ruling 3c) ==")
# --------------------------------------------------------------------------------

# 6a: Psi^T G Phi == Phi^T G^T Psi for ANY n x n G (not only symmetric) -- the fact
# that makes B1's K-term vanish even with A != 0.
rng = random.Random(6161)
ok = True
n4 = 4
for _ in range(150):
    G = [[rand_frac(rng, -5, 5, 1, 3) for _ in range(n4)] for _ in range(n4)]
    Phi = [rand_frac(rng, -5, 5, 1, 3) for _ in range(n4)]
    Psi = [rand_frac(rng, -5, 5, 1, 3) for _ in range(n4)]
    GPhi = [sum(G[i][j] * Phi[j] for j in range(n4)) for i in range(n4)]
    GtPsi = [sum(G[j][i] * Psi[j] for j in range(n4)) for i in range(n4)]
    lhs = sum(Psi[i] * GPhi[i] for i in range(n4))
    rhs = sum(Phi[i] * GtPsi[i] for i in range(n4))
    if lhs != rhs:
        ok = False
ck("Psi^T G Phi == Phi^T G^T Psi exactly for ANY (not nec. symmetric) G, 150 trials "
   "(n=4)", ok)

# 6b: S^{e,skew} vanishes identically whenever Psi = c*Phi, for ANY scalar c
# (both c=1 agree and c=-1 mirror as special cases) -- the fact that makes B2's
# agree/mirror configurations force A[a]=0 in the extended system.
rng = random.Random(6262)
ok = True
for _ in range(150):
    Pi, Pj = rand_frac(rng, -6, 6, 1, 4), rand_frac(rng, -6, 6, 1, 4)
    c = rand_frac(rng, -5, 5, 1, 3)
    Si, Sj = c * Pi, c * Pj
    skew = Pi * Sj - Pj * Si
    if skew != 0:
        ok = False
ck("S^{e,skew} == 0 identically whenever Psi=c*Phi (any scalar c), 150 trials", ok)

# 6c: THE central check -- the full combo identity holds for the ACTUAL extended
# (L[w]+A[a])-coupled reader/record system, for ARBITRARY w,a on an arbitrary
# support (not only Gate-D-stationary values) -- this is the strongest form of
# "B1 transfers": combo := <Psi,Reader> - <Phi,Record> == -2b<Phi^3,Psi> EXACTLY.
rng = random.Random(6363)
ok = True
all_named_supports = supports_n3[1:] + list(supports_n4.values())  # skip empty(n=3)
for _ in range(150):
    n = rng.choice([3, 4])
    pairs = all_pairs(n)
    k = rng.randint(0, len(pairs))
    sup = list(rng.sample(pairs, k)) if k > 0 else []
    w = {e: rand_frac(rng, -6, 6, 1, 4) for e in sup}
    a = {e: rand_frac(rng, -6, 6, 1, 4) for e in sup}
    av, bv, Kv = rand_frac(rng, -4, 4, 1, 4), rand_frac(rng, -4, 4, 1, 4), rand_frac(rng, 1, 5, 1, 4)
    Phi = [rand_frac(rng, -5, 5, 1, 3) for _ in range(n)]
    Psi = [rand_frac(rng, -5, 5, 1, 3) for _ in range(n)]
    Lm = build_L(sup, w, n)
    Am = build_A(sup, a, n)
    Greader = [[Lm[i][j] + Am[i][j] for j in range(n)] for i in range(n)]
    Grecord = [[Lm[i][j] - Am[i][j] for j in range(n)] for i in range(n)]
    Reader = [Kv * sum(Greader[i][j] * Phi[j] for j in range(n)) + av * Phi[i] + bv * Phi[i] ** 3
              for i in range(n)]
    Record = [Kv * sum(Grecord[i][j] * Psi[j] for j in range(n)) + (av + 3 * bv * Phi[i] ** 2) * Psi[i]
              for i in range(n)]
    combo = sum(Psi[i] * Reader[i] for i in range(n)) - sum(Phi[i] * Record[i] for i in range(n))
    target = -2 * bv * sum(Phi[i] ** 3 * Psi[i] for i in range(n))
    if combo != target:
        ok = False
ck("EXTENDED combo identity <Psi,Reader>-<Phi,Record> == -2b<Phi^3,Psi> exactly, "
   "150 random trials over arbitrary support/w/a/n (B1 TRANSFERS UNCHANGED)", ok)

# 6d: at Psi=c*Phi (agree c=1, mirror c=-1), the Gate-D-STATIONARY a_e (not an
# arbitrary a_e) is exactly 0 on every support edge -- the new mechanism behind B2.
rng = random.Random(6464)
ok = True
for _ in range(150):
    n = rng.choice([3, 4])
    pairs = all_pairs(n)
    k = rng.randint(1, len(pairs))
    sup = list(rng.sample(pairs, k))
    Phi = [rand_frac(rng, -5, 5, 1, 3) for _ in range(n)]
    c = rng.choice([Fr(1), Fr(-1)])
    Psi = [c * p for p in Phi]
    Kv, muv = rand_frac(rng, 1, 5, 1, 3), rand_frac(rng, 1, 5, 1, 3)
    for (i, j) in sup:
        skew = Phi[i] * Psi[j] - Phi[j] * Psi[i]
        a_star = -Kv / muv * skew
        if a_star != 0:
            ok = False
ck("Gate-D-stationary a_e* == 0 on every support edge at Psi=+/-Phi, 150 trials "
   "(agree AND mirror both force A[a]=0 -> G collapses to symmetric L[w] -> "
   "original B2 argument applies verbatim -> B2 TRANSFERS)", ok)

# --------------------------------------------------------------------------------
print("== 7. THE DECISIVE EXPERIMENT: extended coupled Newton search "
      "K3 (n=3), C4 (n=4), P3 control (n=3) ==")
# --------------------------------------------------------------------------------
af, bf, Kf, muf = -1.0, 1.0, 1.0, 1.0


def ext_system(x, support, n):
    Phi, Psi = x[:n], x[n:]
    # s (discordance) computed on ALL pairs -- needed both to build w on `support`
    # AND to check off-support admissibility (s_e >= 0 required there); t (skew
    # source) only ever needed/used on `support` (the repair: a_e stays 0 off it).
    s = {e: (Phi[e[0]] - Phi[e[1]]) * (Psi[e[0]] - Psi[e[1]]) for e in all_pairs(n)}
    t = {e: (Phi[e[0]] * Psi[e[1]] - Phi[e[1]] * Psi[e[0]]) for e in support}
    w = {e: -Kf / muf * s[e] for e in support}
    a = {e: -Kf / muf * t[e] for e in support}
    Gsym = [[0.0] * n for _ in range(n)]
    Gskew = [[0.0] * n for _ in range(n)]
    for (i, j), we in w.items():
        Gsym[i][i] += we
        Gsym[j][j] += we
        Gsym[i][j] -= we
        Gsym[j][i] -= we
    for (i, j), ae in a.items():
        Gskew[i][j] += ae
        Gskew[j][i] -= ae
    Greader = [[Gsym[i][j] + Gskew[i][j] for j in range(n)] for i in range(n)]
    Grecord = [[Gsym[i][j] - Gskew[i][j] for j in range(n)] for i in range(n)]
    F = [0.0] * (2 * n)
    for i in range(n):
        F[i] = Kf * sum(Greader[i][j] * Phi[j] for j in range(n)) + af * Phi[i] + bf * Phi[i] ** 3
        F[n + i] = Kf * sum(Grecord[i][j] * Psi[j] for j in range(n)) \
            + (af + 3 * bf * Phi[i] ** 2) * Psi[i]
    return F, s, t, w, a


def ext_newton(x0, support, n, iters=100):
    x = x0[:]
    m = 2 * n
    for _ in range(iters):
        F, _, _, _, _ = ext_system(x, support, n)
        if math.sqrt(sum(f * f for f in F)) < 1e-13:
            break
        J = [[0.0] * m for _ in range(m)]
        h = 1e-7
        for k in range(m):
            xp = x[:]
            xp[k] += h
            Fp, _, _, _, _ = ext_system(xp, support, n)
            for i in range(m):
                J[i][k] = (Fp[i] - F[i]) / h
        Aug = [J[i][:] + [-F[i]] for i in range(m)]
        for c in range(m):
            piv = max(range(c, m), key=lambda r2: abs(Aug[r2][c]))
            if abs(Aug[piv][c]) < 1e-14:
                return None
            Aug[c], Aug[piv] = Aug[piv], Aug[c]
            Aug[c] = [v / Aug[c][c] for v in Aug[c]]
            for r2 in range(m):
                if r2 != c and Aug[r2][c] != 0:
                    Aug[r2] = [v - Aug[r2][c] * u2 for v, u2 in zip(Aug[r2], Aug[c])]
        x = [xi + Aug[i][m] for i, xi in enumerate(x)]
    F, _, _, _, _ = ext_system(x, support, n)
    return x, math.sqrt(sum(f * f for f in F))


def ext_living_fp(x0, support, n, full_pairs):
    res = ext_newton(x0, support, n)
    if not res:
        return None
    xs, r = res
    if r > 1e-10:
        return None
    Phi, Psi = xs[:n], xs[n:]
    if math.sqrt(sum(v * v for v in Psi)) < 1e-2:
        return None
    crossp = sum(abs(Phi[i] * Psi[j] - Phi[j] * Psi[i])
                 for i in range(n) for j in range(i + 1, n))
    if crossp < 1e-6:
        return None  # Psi proportional to Phi -- not living
    _, s, t, w, a = ext_system(xs, support, n)
    if any(s[e] >= -1e-9 for e in support):
        return None
    off_support = [e for e in full_pairs if e not in support]
    if any(s[e] < -1e-9 for e in off_support):
        return None
    # BOUNDARY NOTE (disclosed, same precedent as 5.2b-1's P3 "leaf-swap tie"): an
    # off-support discordance s[e] can land exactly (or numerically indistinguishably
    # from) 0 for a symmetric configuration -- the s[e] >= -1e-9 / s[e] < -1e-9 splits
    # above correctly still accept such a tie. Not a new defect; flagged here so it is
    # visible in-file rather than only in a downstream reviewer's notes.
    return xs, r, s, t, w, a


def sign_str(x):
    return "+" if x >= 0 else "-"


def run_decisive(name, support, n, cycle, seed, trials=3000):
    rng2 = random.Random(seed)
    full_pairs = all_pairs(n)
    living_hits = 0
    distinct = {}
    for tr in range(trials):
        if tr < trials // 3:
            x0 = [rng2.uniform(-2, 2) for _ in range(2 * n)]
        elif tr < 2 * trials // 3:
            x0 = ([rng2.uniform(-1, 1) for _ in range(n)]
                  + [rng2.uniform(-0.5, 0.5) for _ in range(n)])
        else:
            base = [rng2.uniform(-1.5, 1.5) for _ in range(n)]
            x0 = base + [-v * rng2.uniform(0.1, 2) for v in base]
        hit = ext_living_fp(x0, support, n, full_pairs)
        if hit:
            living_hits += 1
            xs = hit[0]
            key = tuple(round(v, 3) for v in xs)
            if key not in distinct:
                distinct[key] = hit
    print(f"  -- {name}: support={support}, {trials} trials, "
          f"living hits={living_hits}, distinct FPs={len(distinct)}")
    j_vals = []  # (Jt_f, residual) for every FP with a defined J_Theta, for the
                 # magnitude-spread summary below -- disclosed fix for a repair-review
                 # MAJOR finding: a fixed-precision '%.6f' print silently rounds any
                 # |J_Theta| < 5e-7 to "0.000000", which can misrepresent a genuinely
                 # nonzero (but tiny) fixed point as absent from the reported set.
    for key, (xs, r, s, t, w, a) in distinct.items():
        Phi, Psi = xs[:n], xs[n:]
        bal = sum(Phi[i] ** 3 * Psi[i] for i in range(n))
        if cycle is not None and all(
            (min(cycle[k], cycle[(k + 1) % len(cycle)]), max(cycle[k], cycle[(k + 1) % len(cycle)]))
            in support for k in range(len(cycle))
        ):
            a_frac = {e: Fr(round(a[e] * 10 ** 9), 10 ** 9) for e in support}
            Jt = cyclic_product(a_frac, cycle)
            Jt_f = float(Jt)
            j_vals.append((Jt_f, r))
        else:
            Jt_f = None
        # scientific notation (not fixed '%.6f'): a tiny-but-genuinely-nonzero
        # J_Theta must be VISIBLE in the printed output, not rounded to 0.000000.
        print(f"     FP: Phi={['%.4f' % v for v in Phi]} Psi={['%.4f' % v for v in Psi]} "
              f"residual={r:.1e} <Phi^3,Psi>={bal:.2e} "
              f"J_Theta={'N/A (no cycle in support)' if Jt_f is None else f'{Jt_f:.6e}'}")
    if j_vals:
        nz = [(abs(j), r) for j, r in j_vals if j != 0.0]
        if nz:
            mags = [m for m, _ in nz]
            worst_res = max(r for _, r in j_vals)
            lo, hi = min(mags), max(mags)
            # DISCLOSURE (repair-review MAJOR finding): report the FULL |J_Theta|
            # spread across distinct FPs, not just the largest values -- some found
            # J_Theta can sit within 1-2 orders of magnitude of this same run's own
            # Newton residuals and should not be characterized as uniformly "many
            # orders of magnitude above the noise floor" without checking each one.
            flag = " <-- WITHIN ~3 ORDERS OF MAGNITUDE OF WORST RESIDUAL, INSPECT" \
                if lo > 0 and lo < 1e3 * worst_res else ""
            print(f"     [J_Theta spread over {len(nz)} nonzero-J FPs: "
                  f"min|J_Theta|={lo:.3e}, max|J_Theta|={hi:.3e}; "
                  f"worst residual this support={worst_res:.1e}{flag}]")
    return living_hits, distinct


print("  [n=3, K3 -- the re-verification target; OLD symmetric-only dynamics found "
      "0/3000 + independent review 0/25000+homotopy]")
k3_hits, k3_distinct = run_decisive("K3 (n=3)", sup_k3, 3, cycle_k3, seed=550, trials=3000)

print("  [n=4, C4 -- the newly-tractable escape hatch, first non-tree living support]")
c4_hits, c4_distinct = run_decisive("C4 (n=4)", sup_c4, 4, cycle_c4, seed=551, trials=3000)

print("  [n=3, P3 control {(0,1),(0,2)} -- 5.2b-1's known symmetric-only living "
      "support, no cycle, re-run under the extended dynamics]")
p3_support = [(0, 1), (0, 2)]
p3_hits, p3_distinct = run_decisive("P3 control (n=3)", p3_support, 3, None, seed=552, trials=3000)

ck("K3 under the EXTENDED (L+A)-coupled dynamics: reported honestly either way "
   "(0 hits = strengthened negative; >0 hits = discovery)", True,
   f"{k3_hits} living hits / 3000 trials, {len(k3_distinct)} distinct")
ck("C4 under the EXTENDED (L+A)-coupled dynamics: reported honestly either way",
   True, f"{c4_hits} living hits / 3000 trials, {len(c4_distinct)} distinct")
ck("P3 control under the EXTENDED (L+A)-coupled dynamics: reported honestly either "
   "way (support has no cycle -> J_Theta undefined by construction, expected)",
   True, f"{p3_hits} living hits / 3000 trials, {len(p3_distinct)} distinct")

# B1/B2 transfer check across every living FP actually found, all three supports
all_found = list(k3_distinct.values()) + list(c4_distinct.values()) + list(p3_distinct.values())
ok = True
worst = 0.0
for (xs, r, s, t, w, a) in all_found:
    n_here = len(xs) // 2
    Phi, Psi = xs[:n_here], xs[n_here:]
    bal = abs(sum(Phi[i] ** 3 * Psi[i] for i in range(n_here)))
    worst = max(worst, bal)
    if bal > 1e-6:
        ok = False
ck(f"B1/B2 TRANSFER CHECK: <Phi^3,Psi> ~ 0 at every living FP actually found "
   f"({len(all_found)} FPs checked, worst |<Phi^3,Psi>|={worst:.2e})", ok or not all_found,
   worst)

print("""  ==> READING (tiered honestly): the analytic derivation (Part 6, exact) proves
  B1 transfers UNCONDITIONALLY to the extended system for ANY w,a (Dr, general
  algebraic argument, not yet Coq-formalized). The numeric search above is the
  disclosed finite_diagnostic re-check of livingness itself under the genuinely
  different (L+A)-coupled dynamics -- reported above exactly as found, whichever
  way it came out; see the printed per-support lines for the actual K3/C4/P3
  counts and (if any) J_Theta values.""")

print()
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS (exact parts in Fractions; Part 7 floats disclosed)")
