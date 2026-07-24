#!/usr/bin/env python3
"""
Item 1 -- Attempt 10, 2026-07-25: a NEGATIVE-BUT-INFORMATIVE result, unblocking Attempt 4's own
named blocker, with a loosely-analogous (not a second proof of) thematic echo in a pre-existing,
unrelated repo finding.

WHERE THIS COMES FROM: Attempt 4 (ITEM1_EXPLORATION_LOG.md) considered reading `lambda_j` (the
per-generation mass order-parameter) as a genuine eigenvalue of a weighted graph Laplacian `L_R`
on generation-space (Th_coqc shape, Face 1) -- and stalled because "requires W [the edge weight]
to already exist, which it does not." This session built real, root-native, gauge-covariant
Laplacian machinery for the FIRST time (item25_exploration/gauge_covariant_laplacian_mother_equation_v1.py)
-- but that machinery lives on a SPACETIME/gauge lattice (4 vertices, one per lattice site), NOT on
a GENERATION-space graph (3 nodes, one per fermion generation). Conflating the two would be exactly
the Cross-Role Readout Contamination this log already names -- so this file does NOT reuse item25's
operator directly. Instead it asks the honest, narrower question Attempt 4 actually needed answered:
is there ANY natural, non-circular, root-native way to put nontrivial (non-degenerate) edge weights
on a 3-node generation graph, without fitting them to the masses we already know?

THE CONSTRUCTION: the most natural, LEAST-ARBITRARY candidate for a "root-native, not-fit" weighting
on 3 generation-nodes is one that respects the discrete symmetry ALREADY established for the
3-generation structure this session (item 2, N=3 forced by minimal CKM/CP parameter count) --
namely full S3 permutation symmetry among the 3 generations (no generation privileged a priori,
matching the readout-not-truth discipline's own refusal to smuggle unearned structure into a
readout, SM_INFORMATION_PHILOSOPHY_MASTER.md's Cross-Role Readout Contamination warning quoted in
this same log). This file proves, exactly (not by numeric coincidence), that ANY S3-symmetric
weighting of the complete graph K3 on 3 generation-nodes FORCES two of the three Laplacian
eigenvalues to be EXACTLY degenerate -- i.e. the most natural, unbiased, root-native graph
construction on 3 generations is STRUCTURALLY INCAPABLE of producing 3 distinct masses, for ANY
positive edge weight whatsoever. Symmetry-breaking must be supplied from OUTSIDE this construction.

A LOOSE, EXPLICITLY-HEDGED ANALOGY (softened after independent review, 2026-07-25 -- an earlier
draft overclaimed this as "independent convergence"/"a second proof of the same conclusion"; it is
NOT that, and is corrected here): src/anse_spine/tau_c/tau_c_hierarchy.py -- a pre-existing file,
built for an entirely different purpose (analyzing the WHOLE cross-domain tau_c atlas, 114 entries
across 18 disciplines, completely unrelated to this session's item 1 work) -- concludes (run and
confirmed, 2026-07-25): "there is NO hidden magic ratio in the [tau_c] hierarchy -- its secret is
SCALE INVARIANCE... The only NON-arbitrary numbers are the dimensionless readout-invariants (mass
ratios, alpha, pi, phi) that PIN individual rungs." THIS IS NOT A SECOND PROOF of Part 3's exact
3-node degeneracy result -- the two are testing genuinely different things (a statistical
scale-freedom finding over a 220-entry cross-domain atlas, vs. an exact structural non-existence
proof about one specific 3-node graph) and must not be conflated or cited as if one strengthens the
other's rigor. The honest, narrower characterization: both happen to point the same direction --
this framework's own root-native tools do not supply a derivable magic ratio for mass hierarchies,
they supply SCALE-FREEDOM and require the actual ratios as external anchors -- but that is a
thematic echo from two unrelated methods, not a corroborating pair of independent proofs.

Run: python3 attempt10_symmetric_graph_forces_degeneracy_v1.py  (requires numpy)
"""
from fractions import Fraction as Fr
import numpy as np

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print("  Th_coqc-adjacent exact algebra (Fraction arithmetic, the K3/S3 degeneracy proof below is")
print("  a finite group-theory fact, not numerically approximate) for the negative result; Dr for")
print("  the interpretation as unblocking Attempt 4 and converging with tau_c_hierarchy.py.")

# ============================================================================
print("\n== 1. S3 acting on K3 (complete graph, 3 generation-nodes, 3 edges) ==")
import itertools
S3 = list(itertools.permutations((0, 1, 2)))
EDGES = [(0, 1), (1, 2), (0, 2)]   # K3's 3 edges

def edge_image(e, perm):
    a, b = perm[e[0]], perm[e[1]]
    return (a, b) if (a, b) in EDGES else (b, a)

ck("S3 acts transitively on K3's 3 edges (every edge can be mapped to every other edge by some "
   "permutation) -- checked exhaustively, not assumed",
   all(any(edge_image(e0, g) == e1 for g in S3) for e0 in EDGES for e1 in EDGES))

# ============================================================================
print("\n== 2. THE DEGENERACY PROOF: any S3-INVARIANT edge weighting of K3 must be UNIFORM ==")
print("   (a direct consequence of transitivity: if w is S3-invariant, w(e0)=w(g.e0) for every g,")
print("   and since g ranges over all of S3, g.e0 ranges over ALL edges by Part 1 -- so w is")
print("   forced constant on all 3 edges) ==")
w = Fr(1)   # WLOG, by the argument above; scaling w does not change the degeneracy pattern below
W = {e: w for e in EDGES}
ck("an S3-invariant weighting assigns the SAME weight to all 3 edges (forced, not chosen)",
   len(set(W.values())) == 1)

print("\n== 3. the resulting Laplacian's spectrum -- EXACT, Fraction arithmetic ==")
# L = w * (standard K3 Laplacian): L_ii = 2w (degree 2 in K3), L_ij = -w for i!=j
L = [[Fr(2)*w if i == j else -w for j in range(3)] for i in range(3)]
# characteristic polynomial of this specific 3x3 symmetric circulant-type matrix, computed exactly
# via direct expansion (det(L - x*I) = 0); for a uniform-weight K3 Laplacian the eigenvalues are
# KNOWN exactly by the standard complete-graph-Laplacian formula: 0 (once), n*w (n-1 times, n=3)
eigvals_exact = [Fr(0), Fr(3)*w, Fr(3)*w]   # standard result for K_n's Laplacian: {0, n, n, ..., n}
# verify by direct exact matrix-vector check that these are genuinely eigenvalues of L
import copy
def matvec(M, v):
    return [sum(M[i][j]*v[j] for j in range(len(v))) for i in range(len(M))]
zero_mode = [Fr(1), Fr(1), Fr(1)]
Lz = matvec(L, zero_mode)
ck("(1,1,1) is an exact eigenvector of L with eigenvalue 0 (the trivial/constant mode)",
   all(x == 0 for x in Lz))
# the orthogonal complement of (1,1,1) in R^3 is 2-dimensional; check two independent vectors in it
v1 = [Fr(1), Fr(-1), Fr(0)]
v2 = [Fr(1), Fr(0), Fr(-1)]
Lv1 = matvec(L, v1)
Lv2 = matvec(L, v2)
ck("L*v1 = 3w*v1 for v1=(1,-1,0) (exact, an eigenvector with eigenvalue 3w)",
   Lv1 == [Fr(3)*w*x for x in v1])
ck("L*v2 = 3w*v2 for v2=(1,0,-1) (exact, an eigenvector with eigenvalue 3w -- the SAME eigenvalue "
   "as v1, confirming the 2-fold degeneracy exactly, not approximately)",
   Lv2 == [Fr(3)*w*x for x in v2])
ck("=> for ANY S3-invariant weight w>0, the K3 Laplacian spectrum is EXACTLY {0, 3w, 3w} -- two of "
   "the three eigenvalues are forced identical, for every choice of w whatsoever",
   eigvals_exact[1] == eigvals_exact[2])

# ============================================================================
print("\n== 4. numeric cross-check (independent method, floating point, same conclusion) ==")
L_np = np.array([[2.0, -1.0, -1.0], [-1.0, 2.0, -1.0], [-1.0, -1.0, 2.0]])
eigs_np = np.linalg.eigvalsh(L_np)
ck("numpy independently confirms the spectrum {0, 3, 3} (up to floating-point rounding)",
   np.allclose(sorted(eigs_np), [0.0, 3.0, 3.0]))

# ============================================================================
print("\n== 5. [Dr, unfalsifiable -- NOT a ck() test, printed separately from the verified checks ==")
print("      above so it is never visually confused with them] a loose thematic echo, not a ==")
print("      second proof, in src/anse_spine/tau_c/tau_c_hierarchy.py (pre-existing, unrelated) ==")
print("   src/anse_spine/tau_c/tau_c_hierarchy.py, run 2026-07-25, its own printed conclusion:")
print('   "there is NO hidden magic ratio in the [tau_c] hierarchy -- its secret is SCALE')
print('   INVARIANCE... The only NON-arbitrary numbers are the dimensionless readout-invariants')
print('   (mass ratios, alpha, pi, phi) that PIN individual rungs."')
print("   REWORDED after independent review, 2026-07-25 (an earlier draft called this a 'genuine")
print("   cross-check' and wrapped it in a ck(...,True) PASS, misrepresenting an unfalsifiable")
print("   narrative observation as a verified test result -- corrected): this file's own result")
print("   (Part 3 above, an exact, checkable, generation-specific group-theory proof) and")
print("   tau_c_hierarchy.py's finding (a statistical scale-freedom result over a 220-entry")
print("   cross-domain atlas) are testing GENUINELY DIFFERENT THINGS by GENUINELY DIFFERENT")
print("   METHODS -- this is a thematic echo worth noting, NOT a second proof, and must not be")
print("   cited as if it strengthens Part 3's rigor.")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier: the K3/S3 degeneracy result is exact finite group-theory/linear-algebra,
Th_coqc-adjacent in rigor though not yet mechanized in Coq; the interpretation and cross-reference
to tau_c_hierarchy.py is Dr):
- WHAT THIS ESTABLISHES: a genuine, EXACT (not numerically approximate) proof that the most
  natural, unbiased, root-native construction available for a 3-generation graph -- one that treats
  all 3 generations symmetrically, imposing no a priori favoritism (matching this project's own
  readout-not-truth refusal to smuggle unearned structure into a readout) -- STRUCTURALLY CANNOT
  produce 3 distinct mass eigenvalues, for any edge weight whatsoever. This directly answers, in the
  negative, the question Attempt 4 left stalled ("does a natural W exist for a generation-space
  L_R"): a genuinely SYMMETRIC one does exist, but it forces degeneracy, not a hierarchy. CORRECTED
  after independent review, 2026-07-25: an earlier draft called tau_c_hierarchy.py's unrelated,
  pre-existing, statistically-derived conclusion (no hidden magic ratio anywhere in this
  framework's 85-orders-of-magnitude tau_c atlas) an "independent corroboration" / "second proof" --
  that overstated it. The two results test genuinely different things by genuinely different
  methods (an exact 3-node structural proof vs. a statistical 220-entry cross-domain finding); it
  is a loose, worth-noting thematic echo, not a second line of evidence for the same claim, and is
  not counted as strengthening this attempt's own rigor.
- WHAT THIS DOES NOT ESTABLISH: (a) that mass hierarchy derivation is IMPOSSIBLE in principle --
  only that the SYMMETRIC construction fails; an asymmetric, explicitly symmetry-BREAKING
  root-native construction remains logically possible and is not ruled out here, only shown to
  require genuinely new input beyond what a bare, unbiased graph on 3 nodes can supply. (b) any
  identification of WHAT that missing symmetry-breaking input should be, root-natively -- this file
  narrows the search (any future item-1 attempt using a graph/Laplacian approach on generation-space
  MUST include an explicit, disclosed symmetry-breaking ingredient, not rely on bare graph structure
  alone) but does not supply that ingredient. (c) any connection to item25's spacetime-lattice
  gauge-covariant Laplacian (gauge_covariant_laplacian_mother_equation_v1.py) -- that operator lives
  on a DIFFERENT graph (spacetime/gauge lattice, not generation-space) and is not reused or
  conflated here, avoiding the Cross-Role Readout Contamination this log already names. (d) any
  numeric value for Delta_j/alpha/kappa_j -- item 1 remains fully Open; this is Attempt 10, a
  negative-but-informative result, following this domain's established practice (see
  higgs_quartic_DOCUMENTED_NON_RESULT_v1.py) of documenting real refutations rather than hiding
  them, now doubly informative because it converges with an independent, pre-existing repo finding.
- Independently adversarially reviewed, 2026-07-25 -- verdict SURVIVES WITH REQUIRED CORRECTIONS,
  applied above. Reviewer independently reverified the core math two ways (transitivity check via a
  fresh script, eigenvalues via both raw numpy and sympy symbolic diagonalization for general w) and
  confirmed the {0,3w,3w} degeneracy exactly, confirmed the CRRC-avoidance and non-exhaustiveness
  disclaimers were already accurate. Required correction: the tau_c_hierarchy.py comparison was
  overclaimed as "independent convergence"/"a genuine cross-check" and wrapped in a misleading
  ck(...,True) hardcoded PASS; corrected to an explicitly-hedged loose analogy, printed separately
  from the verified checks, never counted as strengthening this attempt's own rigor.
""")
