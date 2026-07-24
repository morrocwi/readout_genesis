#!/usr/bin/env python3
"""
Item 1 -- Attempt 11, 2026-07-25: tests the founder's own correction to Attempt 10 -- "our graph is
NOT symmetric; we already have the writer/reader L_R [structure], asymmetric but BALANCED" -- using
the REAL, already-documented two-field (Phi,Psi) apparatus (II.8a,
domains/standard_model/source_root/READOUT_GENESIS_CORE_SNAPSHOT.md line ~1017), not an invented
substitute. Finds a DEEPER, more general version of Attempt 10's negative result: it is not
"symmetric vs. directed" that matters -- ANY rule applied UNIFORMLY across the 3 generations, no
matter how richly structured (even a genuine two-field Phi/Psi apparatus with asymmetric, oriented,
Phi-forward/Psi-backward coupling), retains enough residual Z3 (cyclic) symmetry among the
generation index to block full, real, 3-way non-degeneracy.

WHAT WAS TESTED, PRECISELY (matching II.8a's own operator shape, read from the source, not
invented): the fuller operator is `𝔾_n = L_{G_n} ⊗ I_F + I_{G_n} ⊗ C_F + C_int,n` -- a graph part
tensored with a field part, plus an interaction term, split into symmetric (storage/restoration)
and skew (oriented/rotational, z^T 𝔾^(-) z=0) parts. This file builds the smallest honest instance:
3 generation-nodes, a 2-dim (Phi,Psi) field at each node (6-dim total), with:
  - Phi propagating FORWARD around the 3-cycle (0->1->2->0) -- the "reader proposes forward" role
  - Psi propagating BACKWARD around the 3-cycle (0->2->1->0) -- the "record retains backward" role
  - a LOCAL Phi<->Psi exchange at each generation, rate M (the SAME symbol II.8a's own DRL action
    uses, 𝕃^n=(1/Delta t) Delta Phi_n^T M_n Delta Psi_n), tested BOTH as a symmetric coupling
    (M_n=M_n^T, "storage-like") and a skew coupling (M_n=-M_n^T, "oriented-like", matching II.8a's
    own 𝔾^(-) description) -- since II.8a itself splits by symmetric/skew part, both are genuinely
    admissible instances of the SAME apparatus, not two different ad hoc guesses.

CRRC GUARD (explicit, matching this log's own standing warning): ITEM1_EXPLORATION_LOG.md's own
"Synthesis" section already flags that identifying THIS M_n with item 1's SM branch-closure
epsilon/alpha (a discrete tape/intertwiner cost, a completely different index structure) is an
UNBUILT admissibility square, not confirmed. This file does NOT make that identification. It asks a
narrower, purely structural question: does the RICHER two-field apparatus's shape, by itself, break
the generation-degeneracy problem Attempt 10 found -- independent of whether M_n is ever identified
with any specific SM quantity. The answer (below) is no, for a reason that applies regardless of
that identification, so the CRRC risk does not even need to be resolved to read this result.

Run: python3 attempt11_phi_psi_apparatus_still_degenerate_v1.py  (requires numpy)
"""
import numpy as np

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print("  finite_diagnostic (exact numerical linear algebra, reproducible) for the eigenvalue")
print("  computations; Dr for the interpretation. The II.8a apparatus itself is documented [Dr]/")
print("  [finite_diagnostic] in its own source section -- nothing here is claimed Th_coqc.")

P_fwd = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])   # forward cyclic shift (Phi's direction)
P_bwd = P_fwd.T                                        # backward cyclic shift (Psi's direction)
kappa = 1.0   # graph propagation rate, UNIFORM across generations (the 'balanced' condition)

L_phi = kappa * (np.eye(3) - P_fwd)
L_psi = kappa * (np.eye(3) - P_bwd)

def build_G(M, skew):
    """The full 6-dim tensor-product operator on (Phi0,Phi1,Phi2,Psi0,Psi1,Psi2), II.8a's own shape:
    graph part (directed, Phi forward / Psi backward) plus a LOCAL, generation-uniform Phi<->Psi
    exchange at rate M, either symmetric (storage-like) or skew (oriented-like, II.8a's G^(-))."""
    G = np.zeros((6, 6))
    G[0:3, 0:3] = L_phi
    G[3:6, 3:6] = L_psi
    for i in range(3):
        G[i, 3 + i] = M
        G[3 + i, i] = -M if skew else M
    return G

# ============================================================================
print("\n== 1. SYMMETRIC Phi<->Psi coupling (II.8a's G^(+), storage/restoration part) ==")
for M in (0.5, 1.0, 1.7, 2.3):
    G = build_G(M, skew=False)
    eigs = np.linalg.eigvals(G)
    all_real = np.allclose(eigs.imag, 0, atol=1e-9)
    print(f"   M={M}: eigenvalues={np.round(eigs, 4)}  all_real={all_real}  "
          f"distinct |magnitude| count={len(set(np.round(np.abs(eigs), 6)))}")
ck("symmetric M-coupling: eigenvalue realness is NOT guaranteed (found FALSE at M=0.5, TRUE at "
   "M=1.0/1.7/2.3) -- an important CORRECTION caught in-file before review: the full 6-dim operator "
   "G is NOT a symmetric matrix even when the M-block is 'symmetric,' because the directed graph "
   "blocks L_phi != L_phi^T (Phi forward, Psi backward) -- 'symmetric coupling' names only the local "
   "field-space block, not the whole operator; checked directly rather than assumed",
   not np.allclose(np.linalg.eigvals(build_G(0.5, False)).imag, 0, atol=1e-9)
   and np.allclose(np.linalg.eigvals(build_G(1.0, False)).imag, 0, atol=1e-9))
ck("symmetric M-coupling: NEVER gives 6 fully distinct |magnitude| values, for any of the 4 M "
   "values tested (the richer Phi/Psi structure does NOT resolve the degeneracy Attempt 10 found, "
   "whether or not the spectrum happens to be real for that particular M)",
   all(len(set(np.round(np.abs(np.linalg.eigvals(build_G(M, False))), 6))) < 6
       for M in (0.5, 1.0, 1.7, 2.3)))

# ============================================================================
print("\n== 2. SKEW Phi<->Psi coupling (II.8a's G^(-), oriented/rotational part) ==")
for M in (0.3, 0.7, 1.3, 2.0):
    G = build_G(M, skew=True)
    eigs = np.linalg.eigvals(G)
    mags = sorted(set(np.round(np.abs(eigs.real if np.allclose(eigs.imag,0,atol=1e-9) else eigs), 4)))
    print(f"   M={M}: eigenvalues={np.round(eigs, 4)}  distinct |magnitudes|={mags}")
ck("skew coupling: produces COMPLEX eigenvalues for every M tested (a real, checkable fact -- the "
   "oriented/rotational part behaves as expected, introducing genuine rotation, not just splitting)",
   all(not np.allclose(np.linalg.eigvals(build_G(M, True)).imag, 0, atol=1e-9)
       for M in (0.3, 0.7, 1.3, 2.0)))
ck("skew coupling: complex eigenvalues come in conjugate pairs with EQUAL magnitude (as they must, "
   "for any real matrix) -- so even fewer DISTINCT physical-magnitude readouts survive than the "
   "symmetric case, not more",
   all(len(set(np.round(np.abs(np.linalg.eigvals(build_G(M, True))), 6))) <= 3
       for M in (0.3, 0.7, 1.3, 2.0)))

# ============================================================================
print("\n== 3. WHY, structurally (not just by these numeric samples): the residual Z3 symmetry ==")
print("   Both build_G(M, skew=False/True) apply the SAME rate M and SAME kappa uniformly to all")
print("   3 generations -- the operator still commutes with the block-diagonal cyclic-shift action")
print("   diag(P_fwd, P_fwd) on the 6-dim space (rotating Phi and Psi generation-indices together)")
print("   for ANY uniform choice of M, kappa. This is a genuine algebraic fact, checked directly:")
Z3_action = np.zeros((6, 6))
Z3_action[0:3, 0:3] = P_fwd
Z3_action[3:6, 3:6] = P_fwd
commutes_sym = np.allclose(build_G(1.0, False) @ Z3_action, Z3_action @ build_G(1.0, False))
commutes_skew = np.allclose(build_G(1.0, True) @ Z3_action, Z3_action @ build_G(1.0, True))
ck("the full 6-dim operator (both symmetric and skew coupling variants) COMMUTES with the "
   "generation-cyclic-shift action, for uniform M/kappa -- confirmed directly, not inferred from "
   "the eigenvalue pattern alone: this is WHY no uniform rule, however richly structured (two "
   "fields, oriented coupling, directed propagation), can ever fully lift the 3-generation "
   "degeneracy -- the residual Z3 symmetry is a property of UNIFORMITY across generations, not of "
   "which specific rule is applied", commutes_sym and commutes_skew)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier finite_diagnostic for the exact eigenvalue/commutation computations; Dr for the
interpretation; the II.8a apparatus itself is sourced [Dr]/[finite_diagnostic], not Th_coqc):
- WHAT THIS ESTABLISHES: tests the founder's own correction to Attempt 10 -- that this project
  already has a genuinely ASYMMETRIC-BUT-BALANCED root-native structure (the reader/record Phi/Psi
  apparatus, II.8a, not invented for this file) that might supply the missing symmetry-breaking
  Attempt 10 found lacking. Built the smallest honest instance of II.8a's own tensor-product
  operator shape (graph-part tensor field-part plus interaction, split symmetric/skew exactly as
  II.8a itself defines) with Phi propagating forward and Psi backward around the generation cycle,
  and a local, uniform-rate Phi<->Psi exchange M_n. Result, checked both ways II.8a's own split
  allows (symmetric M and skew M), reading degeneracy by eigenvalue MAGNITUDE (the physically
  meaningful readout, since realness itself is not guaranteed -- self-caught in-file: 'symmetric
  M-coupling' names only the local field-space block, not the whole 6-dim operator, which stays
  non-symmetric throughout because the directed graph blocks satisfy L_phi != L_phi^T; realness
  varies with M, e.g. complex at M=0.5, real at M=1.0/1.7/2.3, checked exactly not assumed):
  NEITHER coupling choice EVER resolves the degeneracy, for any M tested. A DEEPER, more general
  reason is identified and directly verified (Part 3): the operator commutes with the
  generation-cyclic symmetry for ANY uniform (same rate at every generation) choice, regardless of
  how richly structured the per-node rule is -- so uniformity across generations, not the graph's
  symmetric-vs-directed shape specifically, is the real obstruction. HEDGE (added after independent
  review, 2026-07-25): "generalizes and strengthens Attempt 10" is true of the MECHANISM identified
  (a strictly weaker sufficient condition -- Z3/uniformity alone, not full S3-invariance -- already
  forces degeneracy), not of the per-instance numeric conclusion's strength (Attempt 10 gets an
  EXACT 2-eigenvalue collapse from S3; this file gets a PARTIAL magnitude-collapse from Z3, a
  different flavor of degeneracy, not a strictly stronger one instance-for-instance).
- WHAT THIS DOES NOT ESTABLISH: (a) any identification of this file's M_n with item 1's actual
  SM branch-closure epsilon/alpha/kappa_j -- explicitly NOT claimed, matching ITEM1_EXPLORATION_LOG.md's
  own standing warning that this admissibility square is unbuilt; this file's structural conclusion
  (uniform rules retain Z3 symmetry) holds regardless of that identification. (b) that NO
  root-native construction can ever break generation degeneracy -- only that UNIFORM ones (same
  rule/rate at every generation) cannot, whatever their internal richness; a genuinely
  generation-VARYING input (not merely a richer uniform rule) remains logically open and untested
  here. (c) any numeric value or claim about real fermion masses. (d) that II.8a's apparatus is
  somehow deficient in general -- it is a real, useful, richer structure for other purposes (its own
  documented motivation, V.13a's Scalar-Eigenmode Reduction Error repair); this file only tests one
  narrow question (does it break 3-generation degeneracy under uniformity) and answers it negatively.
- Item 1 remains fully Open. This is Attempt 11: another real, useful negative result, this time
  identifying WHY (uniformity, not merely symmetry) rather than just THAT (Attempt 10) -- narrowing
  the search further: any future attempt needs an explicit, disclosed, GENERATION-VARYING
  root-native input, not merely a richer but still generation-uniform construction.
- Independently adversarially reviewed, 2026-07-25 -- verdict SURVIVES, no required corrections.
  Reviewer independently reverified all three load-bearing claims via a fresh script (different
  code path): the M=0.5 complex-eigenvalue self-correction (exact sympy diagonalization matched),
  the commutation claim (verified for additional M values, stress-tested that non-uniform M and
  mismatched Z3-actions correctly BREAK commutation, and confirmed the algebraic reason generalizes:
  L_phi, L_psi are both polynomials in the cyclic shift P_fwd, hence automatically commute with it),
  and degeneracy persistence at additional M values. One optional hedge applied above (distinguishing
  mechanism-generality from per-instance numeric strength in the "generalizes/strengthens" claim).
""")
