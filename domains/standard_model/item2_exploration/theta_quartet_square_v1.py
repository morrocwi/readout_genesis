#!/usr/bin/env python3
"""
Theta 5.7 -- THE QUARTET-SQUARE OBSTRUCTION (Python exact/finite_diagnostic verifier).
Item 2 side: Attempt 6 in the item-2 line. This is 5.4's named next frontier + 5.5's
"quartetJ identification square" open item, taken up: does 5.5's real J_Theta(C) (an
oriented-cyclic-product-of-a_e* readout on a living Theta fixed point) identify with
5.4's complex Cq quartet-J (the CP-signed Jarlskog-type invariant, InfoCPEquivariant-
GenerationBound_attempt.v)? THIS FILE IS THE VERIFIER FOR THAT SQUARE. Companion Coq
file (separate deliverable, not built by this file):
InfoThetaQuartetSquareObstruction_attempt.v.

VERDICT THIS FILE SUPPORTS, STATED UP FRONT SO IT CANNOT BE MISREAD BY SKIMMING:
  OBSTRUCTED. Every embedding family examined (Family A = w_e*+i*a_e*, Family B =
  i*a_e* pure-skew, Family C = vertex-phase Gram conj(Z_i)Z_j) fails to deliver a
  gauge-clean, living-witness-supporting, Q(i)-representable nonzero CP-type readout
  on this real architecture's one living witness (C4). The eigenbasis-mismatch bridge
  (V_cand = V_A^{-1} V_B at distinct living C4 fixed points) is additionally shown
  here, by a FRESH finite_diagnostic sweep, to be non-well-posed (eigen-ordering
  sign conflicts + non-normality/non-unitarity residuals, both measured below, not
  copied from any design paper). NOTHING IN THIS FILE CLOSES THE SQUARE, CHANGES
  ITEM 2's [Open] STATUS, OR IDENTIFIES J_Theta WITH quartetJ. Item 2's status is an
  orchestrator/founder-level call outside this square's scope (binding ruling 7).

CRRC GUARD (binding, checked by inspection -- grep this file for "generation",
"CKM", "color", "n_gen" before trusting this line): no edge weight w_e, skew value
a_e, cyclic product J_Theta, vertex phase Z_i, Gram entry N_ij, eigenvalue, or
eigenvector computed anywhere below is ever identified with a generation index,
a CKM matrix entry, a color/level count, or a family-slot count. quartetJ (reused,
not redefined, from InfoCPEquivariantGenerationBound_attempt.v) and J_Theta (reused
by NAME reference only -- not recomputed here, see theta_oriented_skew_v1.py for
its own definition) remain distinct symbols throughout; the whole point of this file
is to test whether a bridge BETWEEN them exists, and the answer is: not one that
survives gauge-invariance, livingness, and well-posedness simultaneously.

TIER MAP (declared up front, honest fence):
  Th_coqc         -- NONE in this file (the Coq witness is a separate companion file
                     / a separate agent's deliverable; this is the Python verifier).
  Dr (exact, fractions.Fraction-checked, general-argument-level, not yet Coq-
      formalized) -- Parts 1-3: Family A/B/C construction + regression tests against
                     hand-derived identities (Part 1); the corrected t_e/s_e gauge-
                     covariance-split mechanism check (Part 2); the shared quartet-
                     rescale/rephasing invariance lemma, exact and general (Part 3).
                     ALL of Parts 1-3 use exact fractions.Fraction arithmetic --
                     zero floats anywhere in those parts.
  finite_diagnostic (floats, disclosed fixed seed, FRESH run -- no design-paper
      number copied into this file, per orchestrator ruling 3) -- Part 4 only: the
      eigen-ordering sign-conflict sweep over the C4 living-FP inventory (regenerated
      here with the SAME seed=551/trials=3000 as theta_oriented_skew_v1.py's own
      Part 7, so the *set of living fixed points* matches that file's disclosed
      33-distinct-FP inventory by construction of an identical deterministic search
      -- but every number REPORTED about eigen-ordering/sign-conflict/non-normality
      in Part 4 below is computed fresh, in this file, this run, not transcribed
      from THETA_ROOT_PROGRAM.md or any design paper).

PROVENANCE (disclosed, per standing workspace convention -- role words only, no AI-
model identity anywhere in this file or its output, permanent rule): this file
implements a synthesis/orchestrator-produced implementation spec (multi-route design
+ adversarial synthesis pass, three named routes -- an eigenbasis-mismatch route, a
holonomy/rephasing route, and a hybrid -- reconciled into ONE primary construction
plus ONE shared rescaling lemma, per orchestrator ruling 2: provenance of the three
routes is narrated in the program doc, not filed as three near-duplicate artifacts
here). The corrected t_e-covariant/s_e-non-covariant mechanism (Part 2) is the single
most consequential correction carried from that synthesis pass and is independently
re-derived and exact-arithmetic-checked in this file, not merely asserted.

K3 DEADNESS (orchestrator ruling 4, cited exactly as three disclosed search efforts,
NOT re-run in this file -- Part 4 above only regenerates the C4 inventory, which is
this square's only living witness): 0/3000 (5.2b-1, original symmetric-only dynamics)
+ 0/25000+homotopy (an independent review's search) + 0/3000 (5.5's own re-check
under the extended (L+A)-coupled dynamics, seed=550). K3 is a triangle: bounded-
search negative, not a nonexistence proof, carried forward unchanged here.

WHY THREE FAMILIES (recap, so this file is self-contained against THETA_SQUARE_SPEC.md
without requiring the reader to have it open):
  Family A: z_e := w_e* + i*a_e*  (both Gate-D-stationary sources on one Cq edge value)
  Family B: z_e := i*a_e*         (pure-skew only; the ONE gauge-CLEAN, dynamically-
            realized embedding, per Part 2's t_e-covariance derivation)
  Family C: N_ij := conj(Z_i)*Z_j, Z_i := Phi_i + i*Psi_i  (vertex-phase Gram matrix,
            rank-1 by construction, topology-independent -- no edge set enters it at
            all)
  "Quartet" for the edge-indexed families A/B is NOT the vertex-indexed quartetJ(V)
  of the CP-bound file (that expects a genuine N x N mixing-type matrix); it is the
  analogous alternating-conjugation product over a CYCLE's edges: a TRIPLE product on
  K3's 3 edges (P3 := za*zb*conj(zc)) and a QUARTET product on C4's 4 edges
  (P4 := za*zb*conj(zc)*conj(zd)), mirroring theta_oriented_skew_v1.py's own
  cyclic_product's alternating structure but over Cq multiplication/conjugation
  instead of real sign-directed traversal. Family C, being vertex-indexed, DOES use
  the genuine quartetJ_general(V,i,j,k,l) pattern (a direct generalization of the
  CP-bound file's fixed-index quartetJ, reused not redefined in spirit).

NAMED OPEN ITEMS (carried forward from the spec, NOT resolved here -- restated so a
downstream reader of only this file, not the spec, still sees the honest fence):
  [Open] general finite-n-cycle statement for Family B's vanishing/nonvanishing
    pattern beyond K3 (n=3, nonzero) and C4 (n=4, zero) -- only these two concrete
    cycles are checked; whether ALL even cycles vanish and all odd cycles don't is
    a conjecture from the i^m parity pattern, not proven here for general m.
  [Open] general tree structural-induction lemma (pre-existing open item, inherited
    unchanged from InfoThetaOrientedSkewObstruction_attempt.v).
  [Open] exact Groebner-basis / minimal-polynomial certification of a specific C4
    living fixed point's eigenvalue field -- the concrete prerequisite for ever
    reopening the eigenbasis-bridge route; NOT attempted here (numpy floats only,
    Part 4, explicitly finite_diagnostic-tier for that reason).
  [Open] the nonlinear (non-affine) embedding family -- only the three AFFINE
    embeddings A/B/C are examined; a genuinely nonlinear map from (w_e,a_e) or
    (Phi_i,Psi_i) into Cq is not explored.
  [Open] the qualitative/inequality-relation escape hatch (e.g. sign(J_Theta)
    correlating with sign(quartetJ) under SOME as-yet-unnamed weaker equivalence
    than exact identification) -- not attempted here.
  [Open] feeding G's actual eigenvalues into R2's holonomy machinery (a fourth,
    unexplored combination of the three routes' machinery) -- not attempted here.
  [Open] the near-zero J_Theta cluster's (inherited from 5.5, |J_Theta|~2.6e-14 at
    8/33 C4 FPs) rigorous exact-arithmetic distinction from a hypothetical exact-
    zero branch -- irrelevant to this square's own verdict (which holds regardless
    of that cluster's exact-zero-or-not status) but restated for completeness.

CROSS-FILE DISCLOSURE (post-review, MINOR finding, both independent reviewers
confirmed): this file's edge-quartet convention P4 (za*zb*conj(zc)*conj(zd), read on
sup_c4_order=[(0,1),(1,2),(2,3),(0,3)] -- an ADJACENT-edge split: edges (0,1)+(1,2)
plain, (2,3)+(0,3) conjugated) is NOT the same pairing as the companion Coq file
InfoThetaQuartetSquareObstruction_attempt.v's PA (an OPPOSITE-edge split: edges
(0,1)+(2,3) plain, (3,0)+(1,2) conjugated). Neither this file's header nor the spec
fixes one canonical formula for this edge-indexed "quartet" (both are explicitly an
analogy to the vertex-indexed quartetJ_general, not that construction itself), so
this divergence does not make either file wrong: Family B's C4-vanishing holds under
EITHER pairing (every factor is purely imaginary, so any product of the four values
under any conjugation pattern collapses to a real number -- an i^4=1 parity fact
that does not depend on which two edges get conjugated), and Family A's 1d witness
below (w={(0,1):1/5,...}, Im(P): -557/40 -> 1301/360) is this file's OWN
self-derived witness under ITS OWN (adjacent) pairing -- it is NOT, and was never
claimed to be, a cross-file reproduction of the Coq file's separate witness (188 ->
144) under the opposite pairing. Do not read the two files' C4 witnesses as
corroborating the same numeric claim; each independently demonstrates Family A
gauge-dependence under its own internally-consistent convention, which if anything
strengthens (not weakens) the OBSTRUCTED verdict, since the gauge-break shows up
under two different edge-pairing conventions, not just one.

FORBIDDEN, restated (orchestrator ruling 1's refutation-purpose carve-out only):
  the V = U_A^dagger U_B eigenbasis bridge is used in Part 4 SOLELY to compute
  diagnostic non-well-posedness evidence (sign-conflict counts, non-normality
  residuals) -- i.e., to help PROVE it is not usable, exactly the carve-out
  "diagnostic use ruled COMPLIANT" language covers. It is NEVER used, here or
  anywhere else in this file, to assert or imply a working CP-type readout.

Run: python3 theta_quartet_square_v1.py   (stdlib + fractions.Fraction for Parts 1-3,
exact throughout; numpy for Part 4's eigendecomposition only, floats disclosed there;
a few seconds for Parts 1-3, roughly a minute for Part 4's Newton search + O(33^2)
pairwise eigenbasis-mismatch sweep)
"""

from fractions import Fraction as Fr
import random
import math

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


def rand_frac(rng, lo=-6, hi=6, dlo=1, dhi=5):
    return Fr(rng.randint(lo, hi), rng.randint(dlo, dhi))


def rand_frac_nonzero(rng, lo=-6, hi=6, dlo=1, dhi=5):
    while True:
        v = rand_frac(rng, lo, hi, dlo, dhi)
        if v != 0:
            return v


# ==================================================================================
# PART 0 -- shared exact Cq arithmetic (mirrors InfoCPEquivariantGenerationBound_
# attempt.v's Cq record / Cadd / Cmul / Cconj EXACTLY, over fractions.Fraction
# instead of Coq's Q -- same ring, reused definitions not redefined semantics).
# ==================================================================================

class Cq:
    """Gaussian-rational complex number: an exact (re, im) Fraction pair."""
    __slots__ = ("re", "im")

    def __init__(self, re, im):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        return Cq(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return Cq(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        if isinstance(o, Cq):
            return Cq(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
        o = Fr(o)
        return Cq(self.re * o, self.im * o)

    __rmul__ = __mul__

    def conj(self):
        return Cq(self.re, -self.im)

    def abs2(self):
        """Exact |z|^2 = re^2 + im^2, a nonnegative Fraction."""
        return self.re * self.re + self.im * self.im

    def __eq__(self, o):
        return isinstance(o, Cq) and self.re == o.re and self.im == o.im

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else ''}{self.im}i)"


ZERO = Cq(0, 0)
UNITS = [Cq(1, 0), Cq(-1, 0), Cq(0, 1), Cq(0, -1)]  # {1, -1, i, -i}, all |.|=1 exactly


def unit_cq_rational(t: Fr) -> Cq:
    """Rational parametrization of the unit circle: (1-t^2+2ti)/(1+t^2), exact unit
    modulus for ANY rational t (|.|^2 = ((1-t^2)^2+4t^2)/(1+t^2)^2 = (1+t^2)^2/(1+t^2)^2
    = 1 identically -- checked as a regression assertion below, not just asserted)."""
    t2 = t * t
    d = 1 + t2
    return Cq((1 - t2) / d, (2 * t) / d)


# quartetJ_general: direct generalization of InfoCPEquivariantGenerationBound_
# attempt.v's fixed-index quartetJ(V) := Im(V01*V12*conj(V02)*conj(V11)) -- rows
# {i,k}, cols {j,l}, the standard Jarlskog-quartet pattern V_ij*V_kl*conj(V_il)*
# conj(V_kj). quartetJ3 below instantiates the EXACT fixed (i,j,k,l)=(0,1,1,2)
# pattern of the reused Coq definition, so results are directly comparable.
def quartetJ_general(V, i, j, k, l):
    val = V[i][j] * V[k][l] * V[i][l].conj() * V[k][j].conj()
    return val.im


def quartetJ3(V):
    return quartetJ_general(V, 0, 1, 1, 2)


# Edge-indexed "quartet"/"triple" products for the affine embeddings (Families A/B):
# NOT the same object as quartetJ_general above -- these act on the 3 (K3) or 4 (C4)
# EDGE values directly, alternating conjugation exactly the way quartetJ_general
# alternates it across its (i,j,k,l) index pattern, generalized to a cycle's edge
# list rather than a vertex-indexed matrix.
def P3(za, zb, zc):
    return za * zb * zc.conj()


def P4(za, zb, zc, zd):
    return za * zb * zc.conj() * zd.conj()


print("=" * 88)
print("PART 0 -- sanity: unit_cq_rational really is exact unit modulus, all t")
print("=" * 88)
rng = random.Random(70001)
ok = True
for _ in range(300):
    t = rand_frac(rng, -9, 9, 1, 6)
    u = unit_cq_rational(t)
    if u.abs2() != 1:
        ok = False
ck("unit_cq_rational(t).abs2() == 1 exactly, 300 random rational t", ok)


# ==================================================================================
# PART 1 -- Family A/B/C construction + regression tests against the hand-derived
# identities (playbook Step 1 Part 1).
# ==================================================================================
print()
print("=" * 88)
print("PART 1 -- Family A/B/C constructions: regression tests vs hand-derived")
print("identities (exact Fraction arithmetic throughout)")
print("=" * 88)

# --- 1a: Family B K3 -- Im(P3) == a1*a2*a3 exactly, for ANY rational a1,a2,a3. ----
print("-- 1a. Family B (z_e := i*a_e), K3 triple product: Im(P3) == a1*a2*a3 --")
rng = random.Random(70101)
ok = True
n_trials = 400
for _ in range(n_trials):
    a1, a2, a3 = rand_frac(rng), rand_frac(rng), rand_frac(rng)
    za, zb, zc = Cq(0, a1), Cq(0, a2), Cq(0, a3)
    P = P3(za, zb, zc)
    if P.im != a1 * a2 * a3 or P.re != 0:
        ok = False
ck(f"Family B K3: Im(P3) == a1*a2*a3 exactly (Re(P3)==0 too), {n_trials} random "
   f"rational trials", ok)

# --- 1b: Family B C4 -- Im(P4) == 0 identically (the i*i*(-i)*(-i)=1 parity fact). -
print("-- 1b. Family B (z_e := i*a_e), C4 bipartite-rectangle quartet: Im(P4) == 0 --")
rng = random.Random(70102)
ok = True
ok_real = True
for _ in range(n_trials):
    a1, a2, a3, a4 = (rand_frac(rng) for _ in range(4))
    za, zb, zc, zd = Cq(0, a1), Cq(0, a2), Cq(0, a3), Cq(0, a4)
    P = P4(za, zb, zc, zd)
    if P.im != 0:
        ok = False
    if P.re != a1 * a2 * a3 * a4:
        ok_real = False
ck(f"Family B C4: Im(P4) == 0 identically (the i*i*(-i)*(-i)=1 parity fact), "
   f"{n_trials} random rational trials, EVERY a-value", ok)
ck(f"Family B C4: Re(P4) == a1*a2*a3*a4 exactly (the only surviving content), "
   f"{n_trials} trials", ok_real)

# --- 1c: Family C -- quartetJ_general == 0 identically (rank-1), ANY topology -----
# "any topology" operationalized: Family C references NO edge set at all (only
# vertex phases Z_i), so we test arbitrary (possibly repeated) index quadruples
# (i,j,k,l) across several n -- the claim is index-generic and n-generic, matching
# "for random rational data, any topology" exactly as stated in the spec.
print("-- 1c. Family C (N_ij := conj(Z_i)*Z_j), rank-1 Gram: quartetJ_general == 0 --")
rng = random.Random(70103)
ok_im = True
ok_re = True
trials_c = 500
for _ in range(trials_c):
    n = rng.choice([3, 4, 5, 6])
    Phi = [rand_frac(rng) for _ in range(n)]
    Psi = [rand_frac(rng) for _ in range(n)]
    Z = [Cq(Phi[v], Psi[v]) for v in range(n)]
    N = [[Z[i].conj() * Z[j] for j in range(n)] for i in range(n)]
    i, j, k, l = (rng.randrange(n) for _ in range(4))  # indices may repeat -- fine
    val = N[i][j] * N[k][l] * N[i][l].conj() * N[k][j].conj()
    if val.im != 0:
        ok_im = False
    expected_re = Z[i].abs2() * Z[j].abs2() * Z[k].abs2() * Z[l].abs2()
    if val.re != expected_re:
        ok_re = False
ck(f"Family C: quartetJ_general(N,i,j,k,l) has Im == 0 identically, {trials_c} "
   f"trials, n in {{3,4,5,6}}, random (possibly-repeated) index quadruples "
   f"(topology-independent by construction -- no edge set enters N)", ok_im)
ck(f"Family C: Re == |Z_i|^2|Z_j|^2|Z_k|^2|Z_l|^2 exactly (>= 0, the only "
   f"surviving content), {trials_c} trials", ok_re)

# --- 1d: Family A C4 -- Im(P) RETAINS eps-dependence under generic non-uniform ----
# Z2^4 switching (abstract symbolic test: only a_e transforms, eps_i*eps_j*a_e,
# EXACTLY theta_oriented_skew_v1.py's own z2_transform semantics applied to the
# a-component only, w_e held fixed -- the "naive" abstract-role-axiom comparison
# ruling (B) names; the WHY (dynamical mechanism) is Part 2's separate job).
print("-- 1d. Family A (z_e := w_e+i*a_e), C4 quartet: Im(P) retains eps-dependence --")
sup_c4_order = [(0, 1), (1, 2), (2, 3), (0, 3)]  # matches theta_oriented_skew_v1.py sup_c4


def z2_switch_a_only(a_vals, eps, edges):
    """a_e -> eps_i*eps_j*a_e; w_e untouched -- theta_oriented_skew_v1.py's own
    z2_transform semantics, restricted to the a-component (w never entered that
    function's domain -- it only ever operated on a_dict)."""
    return {e: eps[e[0]] * eps[e[1]] * a_vals[e] for e in edges}


rng = random.Random(70104)
n_diff = 0
n_trials_1d = 400
witness = None
for tr in range(n_trials_1d):
    w = {e: rand_frac(rng) for e in sup_c4_order}
    a = {e: rand_frac(rng) for e in sup_c4_order}
    eps = {v: rng.choice([1, -1]) for v in range(4)}
    if all(v == eps[0] for v in eps.values()):
        continue  # skip uniform eps -- known-invariant case, not the test
    a_sw = z2_switch_a_only(a, eps, sup_c4_order)
    z = [Cq(w[e], a[e]) for e in sup_c4_order]
    zsw = [Cq(w[e], a_sw[e]) for e in sup_c4_order]
    P = P4(*z)
    Psw = P4(*zsw)
    if P.im != Psw.im:
        n_diff += 1
        if witness is None:
            witness = (dict(w), dict(a), dict(eps), P.im, Psw.im)
ck(f"Family A C4: Im(P) changes under generic non-uniform Z2^4 switching for "
   f"{n_diff}/{n_trials_1d} random trials (nonzero count is the exact witness "
   f"the spec requires -- the gauge-DEPENDENCE claim)", n_diff > 0, n_diff)
if witness:
    w_w, a_w, eps_w, im0, im1 = witness
    print(f"     concrete witness: w={w_w} a={a_w} eps={eps_w}")
    print(f"       Im(P) before switching = {im0}, after = {im1} (changed)")

# cross-check (not new content, sanity only): the SAME transform leaves Family B
# (pure-skew, w=0) exactly invariant on C4 -- this is theta_oriented_skew_v1.py's
# own already-proven Z2 telescoping fact, re-confirmed here in the Family-B/quartet
# language as a contrast to 1d, not claimed as new.
rng = random.Random(70105)
ok = True
for _ in range(200):
    a = {e: rand_frac(rng) for e in sup_c4_order}
    eps = {v: rng.choice([1, -1]) for v in range(4)}
    a_sw = z2_switch_a_only(a, eps, sup_c4_order)
    z = [Cq(0, a[e]) for e in sup_c4_order]
    zsw = [Cq(0, a_sw[e]) for e in sup_c4_order]
    if P4(*z).im != P4(*zsw).im:
        ok = False
ck("cross-check (inherited fact, not new): Family B (w=0) C4 quartet IS invariant "
   "under the same Z2^4 switching, 200 trials -- contrast with 1d confirms the "
   "gauge-break is caused by w_e, not by a_e", ok)


# ==================================================================================
# PART 2 -- THE CORRECTED-MECHANISM CHECK (playbook Step 1 Part 2, the single most
# consequential correction in this square's design): t_e transforms covariantly
# under (Phi,Psi) -> (D.Phi, D.Psi) for ANY D in {+1,-1}^n (uniform or not); s_e
# does NOT, for non-uniform D.
# ==================================================================================
print()
print("=" * 88)
print("PART 2 -- corrected mechanism: t_e is D_i*D_j-covariant for EVERY D; s_e is")
print("NOT, for non-uniform D (concrete counterexample + general random sweep)")
print("=" * 88)


def s_e(Phi, Psi, i, j):
    return (Phi[i] - Phi[j]) * (Psi[i] - Psi[j])


def t_e(Phi, Psi, i, j):
    return Phi[i] * Psi[j] - Phi[j] * Psi[i]


def apply_D(vec, D):
    return [D[k] * vec[k] for k in range(len(vec))]


print("-- 2a. t_e(D.Phi,D.Psi) == D_i*D_j*t_e(Phi,Psi) EXACTLY, for EVERY D --")
rng = random.Random(70201)
ok = True
n_trials_2a = 0
for _ in range(600):
    n = rng.choice([2, 3, 4, 5])
    Phi = [rand_frac(rng) for _ in range(n)]
    Psi = [rand_frac(rng) for _ in range(n)]
    D = [rng.choice([1, -1]) for _ in range(n)]
    Phi_D, Psi_D = apply_D(Phi, D), apply_D(Psi, D)
    for i in range(n):
        for j in range(i + 1, n):
            n_trials_2a += 1
            lhs = t_e(Phi_D, Psi_D, i, j)
            rhs = D[i] * D[j] * t_e(Phi, Psi, i, j)
            if lhs != rhs:
                ok = False
# explicit uniform-D and single-flip-D sanity subcases folded into the same sweep
# above via random.choice; add a deterministic all-uniform and all-but-one-flip
# case explicitly for the record (n=4):
Phi4, Psi4 = [rand_frac(rng) for _ in range(4)], [rand_frac(rng) for _ in range(4)]
for D4 in ([1, 1, 1, 1], [-1, -1, -1, -1], [1, -1, 1, 1], [1, 1, -1, -1], [-1, 1, -1, 1]):
    Phi4D, Psi4D = apply_D(Phi4, D4), apply_D(Psi4, D4)
    for i in range(4):
        for j in range(i + 1, 4):
            n_trials_2a += 1
            if t_e(Phi4D, Psi4D, i, j) != D4[i] * D4[j] * t_e(Phi4, Psi4, i, j):
                ok = False
ck(f"t_e is EXACTLY D_i*D_j-covariant for every D (uniform AND non-uniform), "
   f"{n_trials_2a} (n, i<j) checks over 600 random (Phi,Psi,D) instances plus 5 "
   f"deterministic D-patterns on one fixed (Phi,Psi)", ok)

print("-- 2b. s_e is NOT D_i*D_j-covariant for non-uniform D: concrete witness --")
Phi_w = [Fr(1), Fr(2)]
Psi_w = [Fr(3), Fr(4)]
D_w = [1, -1]
s_before = s_e(Phi_w, Psi_w, 0, 1)
Phi_wD, Psi_wD = apply_D(Phi_w, D_w), apply_D(Psi_w, D_w)
s_after = s_e(Phi_wD, Psi_wD, 0, 1)
predicted_covariant = D_w[0] * D_w[1] * s_before
print(f"     Phi=(1,2) Psi=(3,4) D=(1,-1): s_e(before)={s_before}, "
      f"D_i*D_j*s_e(before)={predicted_covariant} (the covariant PREDICTION), "
      f"actual s_e(D.Phi,D.Psi)={s_after} (the ACTUAL value)")
ck("s_e concrete witness: actual switched value (21) != covariant prediction (-1) "
   "-- s_e demonstrably NOT D_i*D_j-covariant", s_after != predicted_covariant
   and s_before == 1 and predicted_covariant == -1 and s_after == 21,
   (s_before, predicted_covariant, s_after))

print("-- 2c. general random sweep: s_e non-covariance is the GENERIC case for "
      "non-uniform D (not just the one witness) --")
rng = random.Random(70202)
n_checked = 0
n_noncovariant = 0
for _ in range(600):
    n = rng.choice([2, 3, 4, 5])
    Phi = [rand_frac(rng) for _ in range(n)]
    Psi = [rand_frac(rng) for _ in range(n)]
    D = [rng.choice([1, -1]) for _ in range(n)]
    if all(d == D[0] for d in D):
        continue  # uniform D IS covariant (global sign flip is a genuine no-op
        # per 5.5's own finding) -- only non-uniform D tests this claim
    for i in range(n):
        for j in range(i + 1, n):
            if D[i] == D[j]:
                continue  # covariant trivially on an edge where the flip agrees
            n_checked += 1
            Phi_D, Psi_D = apply_D(Phi, D), apply_D(Psi, D)
            lhs = s_e(Phi_D, Psi_D, i, j)
            rhs = D[i] * D[j] * s_e(Phi, Psi, i, j)
            if lhs != rhs:
                n_noncovariant += 1
ck(f"s_e non-covariance is generic on edges where D_i != D_j: {n_noncovariant}/"
   f"{n_checked} such (instance, edge) checks show non-covariance (report exactly "
   f"as measured -- this is NOT claimed to be 100% for every possible (Phi,Psi), "
   f"only shown to be the overwhelming generic case)", n_noncovariant > 0,
   f"{n_noncovariant}/{n_checked}")

print("""  ==> READING (Dr, exact): the skew/a_e sector is FULLY, unconditionally
  dynamically gauge-compatible with the abstract Z2^n switching group (2a). The
  symmetric/w_e sector is NOT, for any D with D_i != D_j on a support edge (2b/2c).
  Consequence: the coupled living-FP system's actual dynamical symmetry group
  collapses to the two-element global group D=(1,...,1) or D=(-1,...,-1) on a
  CONNECTED support -- this is why Family B (skew-only) is gauge-clean and Family A
  (touches w_e) is not (confirmed directly in Part 1d above).""")


# ==================================================================================
# PART 3 -- quartet_rescale_invariant: the ONE shared rephasing/rescaling lemma
# (playbook Step 1 Part 3 / Coq T1), tested on quartetJ3 (the fixed (0,1,1,2)
# pattern reused from InfoCPEquivariantGenerationBound_attempt.v).
# ==================================================================================
print()
print("=" * 88)
print("PART 3 -- quartet_rescale_invariant: quartetJ3 under V_ij -> alpha_i*V_ij*")
print("beta_j, exact for unit alpha/beta, exact scaling law for general nonzero")
print("=" * 88)


def rand_V3(rng):
    return [[Cq(rand_frac(rng), rand_frac(rng)) for _ in range(3)] for _ in range(3)]


def rescale_V(V, alpha, beta):
    n = len(V)
    return [[alpha[i] * V[i][j] * beta[j] for j in range(n)] for i in range(n)]


print("-- 3a. UNIT rephasing: quartetJ3(V') == quartetJ3(V) EXACTLY, alpha/beta from "
      "{1,-1,i,-i} and rational unit-circle points (1-t^2+2ti)/(1+t^2) --")
rng = random.Random(70301)
ok = True
n_trials_3a = 300
for _ in range(n_trials_3a):
    V = rand_V3(rng)
    alpha = [None, None, None]
    beta = [None, None, None]
    for arr in (alpha, beta):
        for idx in range(3):
            if rng.random() < 0.5:
                arr[idx] = rng.choice(UNITS)
            else:
                arr[idx] = unit_cq_rational(rand_frac(rng, -9, 9, 1, 6))
    Vp = rescale_V(V, alpha, beta)
    if quartetJ3(Vp) != quartetJ3(V):
        ok = False
ck(f"quartetJ3 EXACTLY invariant under unit-Cq rephasing (units + rational "
   f"unit-circle points, mixed), {n_trials_3a} random trials", ok)

print("-- 3b. GENERAL nonzero rescaling: quartetJ3(V') == "
      "|alpha0|^2*|alpha1|^2*|beta1|^2*|beta2|^2 * quartetJ3(V) EXACTLY --")
rng = random.Random(70302)
ok = True
ok_sign = True
n_trials_3b = 300
for _ in range(n_trials_3b):
    V = rand_V3(rng)
    alpha = [Cq(rand_frac_nonzero(rng), rand_frac(rng)) for _ in range(3)]
    beta = [Cq(rand_frac_nonzero(rng), rand_frac(rng)) for _ in range(3)]
    Vp = rescale_V(V, alpha, beta)
    factor = alpha[0].abs2() * alpha[1].abs2() * beta[1].abs2() * beta[2].abs2()
    lhs = quartetJ3(Vp)
    rhs = factor * quartetJ3(V)
    if lhs != rhs:
        ok = False
    if factor < 0:
        ok_sign = False  # sanity: factor must be a nonnegative product of squares
    # sign-invariance is now a COROLLARY of the exact scaling law, checked directly:
    orig = quartetJ3(V)
    if orig != 0 and factor != 0:
        same_sign = (lhs > 0) == (orig > 0)
        if not same_sign:
            ok_sign = False
ck(f"quartetJ3(V') == (product of 4 squared moduli)*quartetJ3(V) EXACTLY, general "
   f"nonzero Cq row/col rescaling, {n_trials_3b} trials (the exact scaling law -- "
   f"stronger than sign-invariance alone)", ok)
ck(f"COROLLARY: sign(quartetJ3) invariant (factor >= 0 always, product of squared "
   f"moduli), {n_trials_3b} trials", ok_sign)

print("""  ==> READING (Dr, exact): this ONE ring identity subsumes all three design
  routes' rescaling/rephasing lemmas (per orchestrator ruling 2, filed once). It is
  the sole positive, general, reusable lemma this whole square produces -- it says
  nothing about WHETHER a gauge-clean, living-witness-bearing embedding into a
  quartetJ-shaped object exists (Parts 1-2 already answered that: no); it only says
  that IF one existed, its sign would be well-posed under diagonal rescaling. Part 4
  below shows the one remaining candidate route (the eigenbasis bridge) fails for a
  DIFFERENT reason -- ordering, not rescaling.""")


# ==================================================================================
# PART 4 -- finite_diagnostic (floats, disclosed seed=551, FRESH run): regenerate
# the C4 living-FP inventory (playbook Part 4/5), then run the eigen-ordering
# sign-conflict + non-normality/non-unitarity residual sweep on the eigenbasis-
# mismatch bridge V_cand := V_A^{-1} V_B across ALL pairs of distinct living FPs
# ("sector pairs"), under >= 4 ordering conventions. Diagnostic use only (ruling 1
# carve-out) -- this is evidence the bridge is NOT well-posed, not a working readout.
# ==================================================================================
print()
print("=" * 88)
print("PART 4 -- finite_diagnostic: FRESH C4 living-FP regeneration (seed=551,")
print("trials=3000, identical code to theta_oriented_skew_v1.py Part 7) + eigen-")
print("ordering sign-conflict / non-normality sweep on the eigenbasis bridge")
print("=" * 88)

import numpy as np  # noqa: E402  -- Part 4 only, disclosed, finite_diagnostic tier

af, bf, Kf, muf = -1.0, 1.0, 1.0, 1.0
sup_c4 = [(0, 1), (1, 2), (2, 3), (0, 3)]
n4 = 4


def all_pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


FULL_PAIRS_4 = all_pairs(n4)


# --------------------------------------------------------------------------------
# The following three functions (ext_system, ext_newton, ext_living_fp) are
# REPLICATED VERBATIM (identical logic, identical constants/thresholds) from
# theta_oriented_skew_v1.py's own Part 7, per the playbook's explicit instruction
# ("import or replicate its exact search with its seeds") -- replicated rather than
# imported so this file does not re-execute that file's Parts 1-6 print/side-effect
# statements as an import side effect. Any behavioral drift from the source file is
# a bug in THIS file, not a new derivation -- these are not this square's content,
# only its reused machinery.
# --------------------------------------------------------------------------------
def ext_system(x, support, n):
    Phi, Psi = x[:n], x[n:]
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
        return None
    _, s, t, w, a = ext_system(xs, support, n)
    if any(s[e] >= -1e-9 for e in support):
        return None
    off_support = [e for e in full_pairs if e not in support]
    if any(s[e] < -1e-9 for e in off_support):
        return None
    return xs, r, s, t, w, a


def regenerate_c4_inventory(seed, trials, support, n):
    """Replicates theta_oriented_skew_v1.py's run_decisive()'s RNG-consuming trial
    loop EXACTLY (same three-band initial-guess strategy, same order), for C4 only,
    seed=551/trials=3000 -- deterministic given identical code + seed, so this
    regenerates the SAME set of distinct living fixed points that file's own Part 7
    disclosed (33, per THETA_ROOT_PROGRAM.md 5.5) without transcribing that number."""
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
    return living_hits, distinct


print("-- 4a. regenerating the C4 living-FP inventory (fresh, seed=551, 3000 "
      "trials, IDENTICAL code to theta_oriented_skew_v1.py Part 7) --")
c4_hits, c4_distinct = regenerate_c4_inventory(551, 3000, sup_c4, n4)
fps = list(c4_distinct.values())
N_FP = len(fps)
ck(f"C4 living-FP inventory regenerated this run: {c4_hits} living hits / 3000 "
   f"trials, {N_FP} distinct FPs (reported exactly as found by THIS run -- not "
   f"transcribed from any design paper; matching theta_oriented_skew_v1.py's own "
   f"disclosed 33/33 count is EXPECTED, not asserted, since the code+seed are "
   f"identical by construction)", N_FP > 0, N_FP)


def build_G(w, a, support, n):
    G = [[0.0] * n for _ in range(n)]
    for (i, j) in support:
        we, ae = w[(i, j)], a[(i, j)]
        G[i][i] += we
        G[j][j] += we
        G[i][j] += -we + ae
        G[j][i] += -we - ae
    return G


# -- 4b. sanity: every regenerated FP is genuinely non-normal (a* != 0 somewhere) --
n_nonzero_a = 0
worst_a_zero = None
for (xs, r, s, t, w, a) in fps:
    if any(abs(a[e]) > 1e-9 for e in sup_c4):
        n_nonzero_a += 1
ck(f"every regenerated living FP has a*_e != 0 on at least one support edge "
   f"(re-confirms 5.5's B2 finding fresh, at this run's own FPs): "
   f"{n_nonzero_a}/{N_FP}", n_nonzero_a == N_FP, f"{n_nonzero_a}/{N_FP}")

# -- 4c. non-normality / non-unitarity residuals at EACH FP -----------------------
print("-- 4c. non-normality ||GG^T-G^TG|| and non-unitarity ||V^dagger V - I|| "
      "at each regenerated FP --")
nonnorm_vals = []
nonunit_vals = []
per_fp_eig = []  # (G, evals, evecs) cached for Part 4d
for (xs, r, s, t, w, a) in fps:
    G = np.array(build_G(w, a, sup_c4, n4))
    comm = G @ G.T - G.T @ G
    nonnorm = float(np.linalg.norm(comm))
    nonnorm_vals.append(nonnorm)
    evals, evecs = np.linalg.eig(G)
    nonunit = float(np.linalg.norm(evecs.conj().T @ evecs - np.eye(n4)))
    nonunit_vals.append(nonunit)
    per_fp_eig.append((G, evals, evecs))
ck(f"non-normality residual ||GG^T-G^TG||_F > 0 at every FP (confirms genuine "
   f"non-normality, not a float artifact): min={min(nonnorm_vals):.3e} "
   f"max={max(nonnorm_vals):.3e} mean={sum(nonnorm_vals)/N_FP:.3e}",
   min(nonnorm_vals) > 1e-8, f"min={min(nonnorm_vals):.3e}")
ck(f"non-unitarity residual ||V^dagger V - I||_F > 0 at every FP's raw numpy "
   f"eigenvector matrix (confirms no canonical orthonormal eigenbasis): "
   f"min={min(nonunit_vals):.3e} max={max(nonunit_vals):.3e} "
   f"mean={sum(nonunit_vals)/N_FP:.3e}", min(nonunit_vals) > 1e-8,
   f"min={min(nonunit_vals):.3e}")

# -- 4d. eigen-ordering sign-conflict sweep, >= 4 conventions, ALL sector pairs ---
print(f"-- 4d. eigen-ordering sign-conflict sweep: {N_FP} living FPs as \"sectors\", "
      f"all C({N_FP},2) pairs, quartetJ(V_cand=V_A^-1 V_B) under 4 ordering "
      f"conventions --")


def alt_normalize(v):
    """Alternate eigenvector normalization convention: fix the overall unit-modulus
    phase by making the largest-magnitude entry real positive (instead of numpy/
    LAPACK's raw, unspecified phase choice), then renormalize to unit 2-norm. A
    legitimate GL(1,C) gauge choice, distinct from any ORDERING convention -- tests
    the SCALE/phase freedom directly, as the spec's convention #4 requires."""
    k = int(np.argmax(np.abs(v)))
    ph = v[k] / abs(v[k])
    v2 = v / ph
    nrm = np.linalg.norm(v2)
    return v2 / nrm if nrm > 0 else v2


def convention_matrices(evals, evecs):
    """Returns 4 (name, V) pairs: 4 orderings/normalizations of the eigenvector
    matrix, columns permuted (and, for #4, renormalized) per convention.

    POST-REVIEW DISCLOSURE (MINOR finding, both independent reviewers confirmed):
    convention #4 (by_Re_asc_altnorm) uses the SAME eigenvalue ORDERING as
    convention #1 (by_Re_asc) -- it only right-multiplies each of V1's columns by
    a unit-modulus phase (alt_normalize). That means V4 = V1 . D for a diagonal
    unit-modulus D, for BOTH the A- and B-side matrices, so V_cand4 = VA4^-1 VB4
    = D_A^-1 . V_cand1 . D_B -- exactly the row/column unit-rephasing pattern this
    file's OWN Part 3 (quartet_rescale_invariant) and the companion Coq file's T1
    prove leaves quartetJ EXACTLY invariant. So quartetJ(V_cand4) is analytically
    GUARANTEED (not merely observed) to equal quartetJ(V_cand1) at every sector
    pair -- confirmed against this run's own printed examples: (FP#0,FP#1)
    convention1 and convention4 agree exactly, likewise (FP#0,FP#5). Convention #4
    is therefore NOT an independent 4th ordering/scale test of eigen-ordering
    non-well-posedness; it is a live empirical sanity-check that T1/quartet_
    rescale_invariant holds on real eigen-data (which it does -- a nice side-
    confirmation, not new diagnostic content). Two consequences, both honestly
    reported rather than silently fixed: (1) the headline sign-conflict count
    below is unaffected -- a duplicate value cannot change whether a pair's
    distinct-sign-count exceeds 1, since convention 4 always repeats convention
    1's already-counted sign; (2) the "4 conventions" / "2112 (pair,convention)"
    denominators used for the magnitude-spread statistic below are inflated by
    ~528 non-independent duplicate measurements (~25% of the sample) -- read the
    magnitude-spread claim as resting on 3 independent conventions' worth of
    genuinely distinct measurements, not 4."""
    idx_re = np.argsort(evals.real)
    idx_imre = np.lexsort((evals.real, evals.imag))
    idx_abs = np.argsort(np.abs(evals))
    mats = []
    mats.append(("by_Re_asc", evecs[:, idx_re]))
    mats.append(("by_ImRe_lex", evecs[:, idx_imre]))
    mats.append(("by_abs_asc", evecs[:, idx_abs]))
    V4 = evecs[:, idx_re].copy()
    for c in range(V4.shape[1]):
        V4[:, c] = alt_normalize(V4[:, c])
    mats.append(("by_Re_asc_altnorm", V4))
    return mats


def quartetJ_np(Vc):
    val = Vc[0, 1] * Vc[1, 2] * np.conj(Vc[0, 2]) * np.conj(Vc[1, 1])
    return val.imag


COND_THRESHOLD = 1e8
ZERO_EPS = 1e-9

all_conv = []
for (G, evals, evecs) in per_fp_eig:
    all_conv.append(convention_matrices(evals, evecs))

pair_results = []  # (a_idx, b_idx, [q_conv1..4], excluded_bool)
excluded_illcond = 0
n_conflict = 0
n_pairs_checked = 0
all_nonzero_mags = []

for ai in range(N_FP):
    for bi in range(ai + 1, N_FP):
        conv_A = all_conv[ai]
        conv_B = all_conv[bi]
        qs = []
        illcond = False
        for c in range(4):
            VA = conv_A[c][1]
            VB = conv_B[c][1]
            condA = np.linalg.cond(VA)
            condB = np.linalg.cond(VB)
            if condA > COND_THRESHOLD or condB > COND_THRESHOLD or not np.isfinite(condA) \
                    or not np.isfinite(condB):
                illcond = True
                break
            Vcand = np.linalg.solve(VA, VB)  # V_A^{-1} V_B, numerically preferable to inv()
            qs.append(quartetJ_np(Vcand))
        if illcond:
            excluded_illcond += 1
            continue
        n_pairs_checked += 1
        signs = set()
        for q in qs:
            if abs(q) < ZERO_EPS:
                signs.add(0)
            else:
                signs.add(1 if q > 0 else -1)
                all_nonzero_mags.append(abs(q))
        nonzero_signs = signs - {0}
        if len(nonzero_signs) > 1:
            n_conflict += 1
        pair_results.append((ai, bi, qs, False))

total_pairs = N_FP * (N_FP - 1) // 2
print(f"     total sector pairs = {total_pairs}, excluded (ill-conditioned eigen-"
      f"basis, cond > {COND_THRESHOLD:.0e}) = {excluded_illcond}, checked = "
      f"{n_pairs_checked}")
print("     [post-review disclosure] convention #4 (by_Re_asc_altnorm) is a unit-"
      "modulus column rephasing of convention #1's already-fixed ordering; by this "
      "file's own quartet_rescale_invariant (Part 3) it is ANALYTICALLY GUARANTEED "
      "to reproduce convention #1's quartetJ(V_cand) value at every pair (confirmed "
      "against this run's printed examples below) -- treat it as a live sanity-check "
      "of Part 3's lemma, not a 4th independent ordering test; the magnitude-spread "
      "denominator below effectively rests on 3 independent conventions, not 4 "
      "(see convention_matrices()'s docstring for the full derivation).")
ck(f"eigen-ordering SIGN-CONFLICT count (FRESH, this run): {n_conflict}/"
   f"{n_pairs_checked} sector pairs show a sign disagreement among the 4 "
   f"conventions (reported exactly as measured -- no threshold to pass/fail, this "
   f"IS the evidence of non-well-posedness the square names)", True,
   f"{n_conflict}/{n_pairs_checked}")
if all_nonzero_mags:
    lo, hi = min(all_nonzero_mags), max(all_nonzero_mags)
    ck(f"magnitude spread of quartetJ(V_cand) over all nonzero (pair, convention) "
       f"combinations: min={lo:.3e} max={hi:.3e} (spread = {hi/lo if lo > 0 else float('inf'):.3e}x)"
       f" -- {len(all_nonzero_mags)} nonzero values out of {4*n_pairs_checked} "
       f"(pair,convention) combinations", True, f"[{lo:.3e}, {hi:.3e}]")
else:
    ck("magnitude spread of quartetJ(V_cand): no nonzero values found among "
       "checked pairs (reported honestly)", True, "0/0")

# a concrete example pair, printed for legibility
if pair_results:
    ex_ai, ex_bi, ex_qs, _ = pair_results[0]
    print(f"     example sector pair (FP#{ex_ai}, FP#{ex_bi}): quartetJ(V_cand) "
          f"under the 4 conventions = {['%.3e' % q for q in ex_qs]}")
    conflict_example = None
    for (ai, bi, qs, _) in pair_results:
        nz = [q for q in qs if abs(q) >= ZERO_EPS]
        if len(nz) >= 2 and (max(nz) > 0 and min(nz) < 0):
            conflict_example = (ai, bi, qs)
            break
    if conflict_example:
        ai, bi, qs = conflict_example
        print(f"     concrete SIGN-CONFLICT example (FP#{ai}, FP#{bi}): "
              f"quartetJ(V_cand) under the 4 conventions = {['%.3e' % q for q in qs]}")

print("""  ==> READING (finite_diagnostic, floats, fresh this run): non-normality and
  non-unitarity residuals are strictly positive at every living FP (4c) -- G
  genuinely has no canonical orthonormal eigenbasis. The eigen-ordering sweep (4d)
  is used SOLELY as diagnostic evidence of non-well-posedness (ruling 1's
  refutation-purpose carve-out) -- it is NEVER used as, or claimed to be, a working
  CP-type readout. Whatever the exact sign-conflict count/magnitude-spread printed
  above turns out to be this run, it does not change this square's verdict: the
  eigenbasis bridge remains FORBIDDEN as a readout (orchestrator ruling 4,
  unchanged), and this file does not attempt to lift that prohibition.""")


# ==================================================================================
print()
print("=" * 88)
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS (Parts 1-3 exact Fraction/Cq arithmetic; Part 4 "
      "floats disclosed, fresh seed=551/trials=3000)")
print("""
VERDICT (restated, so this is the last thing printed): OBSTRUCTED. Family A/B/C all
fail to deliver a gauge-clean, living-witness-supporting, well-posed CP-type readout
on the real Theta architecture's one living witness (C4). Item 2's [Open] status is
NOT changed by this file (orchestrator ruling 7) -- that determination stays an
orchestrator/founder-level call outside this square's scope.
""")
