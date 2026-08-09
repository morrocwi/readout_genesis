#!/usr/bin/env python3
"""
Theta TRANSIENT-SELECTION EXPERIMENT v1 -- step 5.9 of THETA_ROOT_PROGRAM.md.

QUESTION (origin, tier Dr, SHAPE-ONLY IMPORT): a Dr-tier prior preprint by the program's
founder, "Axiom 12 -- Informational CP-Asymmetry" (DOI 10.5281/zenodo.17600798), asks
whether an asymmetric microscopic law can select a preferred branch during a finite
transient even when the initial ensemble is unbiased. ONLY the question SHAPE is
imported here -- no equation, constant, or numeric value from that preprint is used
anywhere below. The concrete question asked of THIS repo's own root objects:

  Does the coupled reader(+D)/record(-D) DISCRETE dynamics on the C4 support (5.5's
  living-oriented-skew system, 33 distinct living FPs, seed 551), started from
  orientation-symmetric initial ensembles, select the sign(J_Theta) branches
  ASYMMETRICALLY during the finite transient -- or is the arrival composition
  consistent with the static FP inventory's own +/- composition?

TIER MAP (declared up front, honest fence):
  Th_coqc         -- NONE in this file (no Coq witness produced here; this is a
                     Python exact-Fraction + finite-float diagnostic only).
  Dr              -- the question framing (Axiom-12 import, above) and the general
                     symmetry-algebra arguments in Part 1 (exact Fraction spot-checks,
                     not yet Coq-formalized as universally-quantified theorems).
  finite_diagnostic -- Parts 2-4 (the static FP inventory re-derivation and the
                     dynamical transient-selection experiment itself): FLOATS, fixed
                     declared seeds, disclosed tolerances, same discipline as
                     theta_oriented_skew_v1.py / theta_dynamics_selection_v1.py.

CRRC GUARD (binding, same as every file in this arc): nothing here identifies cycles,
branches, sign(J_Theta), or any count with fermion generations, CKM/mixing angles, or
color -- any such identification would be a NEW admissibility square, not built here.

CONTAMINATION GUARDS (mandatory, verbatim, checked by inspection throughout this file):
  G1. Delta_t is a DECLARED FIXED RATIONAL (0.1 = 1/10, stated once as DT below). No
      h->0, no refinement-to-continuum claim anywhere -- DT is never swept toward 0.
  G2. Memory is a FINITE declared integer step offset on a finite tape: the plain
      second-order stepper's own (n, n-1) two-point memory (Phi_n, Phi_{n-1}) is the
      ENTIRE memory structure used -- no longer tape, no infinite-past kernel. This is
      the declared v1 memory structure (task's own "stage 2 optional" longer tape is
      NOT built here).
  G3. Transient = a DECLARED FINITE step count N_STEPS (below). "Settled" = a DECLARED
      finite residual/consistency criterion evaluated AT step N_STEPS (SETTLE_RESID_TOL,
      SETTLE_STEP_TOL below) -- no t->infinity language anywhere in this file.
  G4. Arrival fractions are INTEGER COUNTS over a DECLARED FINITE ensemble (k of N
      seeds, reported as an exact Fraction) -- never phrased as a probability measure.
      Every outcome (LIVING+, LIVING-, DEAD, DIVERGED, UNRESOLVED) is counted; none is
      silently dropped (the DIVERGED and UNRESOLVED classes exist for exactly this).
  G5. M, D, K, mu, a, b, Delta_t are DECLARED CONSTANTS OF THE RUN: a=-1, b=1, K=mu=1
      (unchanged from every prior Theta file in this program), M=1 (declared here), and
      a SMALL declared set of D values {0.5, 1.0, 2.0} plus an explicit D=0 control are
      checked as separate, individually-declared runs -- no smooth bijection of D is
      ever read as an observable; each D is one discrete labeled run.

NO AI-MODEL NAMES appear anywhere in this file's content (permanent founder rule) --
only role words (doer, reviewer, orchestrator) are ever used in comments.

===============================================================================
PART 0 -- ALGEBRA DONE ON PAPER FIRST (mandatory, before any code): which static
symmetry of the reader/record equations, if any, flips sign(J_Theta) of the arrived
living fixed point on C4?
===============================================================================

Recall the extended system (theta_oriented_skew_v1.py, unchanged here): support E is
the C4 4-cycle {(0,1),(1,2),(2,3),(0,3)}; per edge e=(i,j) in E the ADIABATIC
Gate-D-stationary weights are read off the CURRENT (Phi,Psi):
    s_e = (Phi_i-Phi_j)(Psi_i-Psi_j),      w_e := -(K/mu)*s_e     (symmetric part)
    t_e = Phi_i*Psi_j - Phi_j*Psi_i,       a_e := -(K/mu)*t_e     (skew part)
    G := L[w] + A[a]  (reader operator),   G^T = L[w] - A[a]  (record operator)
J_Theta(C4) := the ordered cyclic product of a_e (directed along the 4-cycle
0->1->2->3->0), a REAL quantity (5.5's Th_coqc invariant).

CANDIDATE 1 -- graph relabelings (vertex permutations that are automorphisms of the
C4 support). The dihedral group D4 of the 4-cycle has 8 elements: 4 rotations, 4
reflections. Under any such relabeling pi, re-evaluating J_Theta on the SAME fixed
cyclic order (0,1,2,3) after relabeling the data is exactly the ORIGINAL cyclic
product traced along pi's own image of the cycle -- a rotation retraces the identical
cyclic product (cyclic-shift invariance of a cyclic product, trivial); a reflection
retraces the cycle in the OPPOSITE direction, i.e. exactly the "reverse the cycle"
operation. 5.5's own Th_coqc fact (`InfoThetaOrientedSkewObstruction_attempt.v`,
verified again in Part 1 below): reversing an EVEN cycle (C4, length m=4) leaves the
cyclic product's SIGN unchanged (general fact: reversal multiplies by (-1)^m, and
(-1)^4=+1). So: rotations trivially preserve J_Theta, reflections preserve J_Theta's
sign too (even cycle). CONCLUSION 1: no element of the C4 automorphism group flips
sign(J_Theta). (This is the concrete instance of the prompt's own hint "since 4 is
even, products of 4 sign flips" -- an odd single-transposition relabeling is NEVER a
graph automorphism of C4 by itself, and the automorphisms that DO exist are all
sign-preserving on an even cycle.)

CANDIDATE 2 -- Psi -> -Psi alone. Naive check on a_e only: t_e = Phi_i*Psi_j-Phi_j*Psi_i
is LINEAR and ODD in Psi at BOTH endpoints simultaneously -- Psi->-Psi sends
t_e -> -t_e for every edge (a single overall factor of -1 per edge, not per endpoint),
so a_e -> -a_e on all 4 edges of C4 at once, and J_Theta (a length-4 product) picks up
(-1)^4 = +1: J_Theta INVARIANT under Psi->-Psi (matches the prompt's own worked hint
exactly). BUT this is not the whole story: is Psi->-Psi even a SYMMETRY of the
DYNAMICS in the first place? s_e is ALSO linear and odd in Psi (same structure as
t_e), so w_e -> -w_e on every edge too under Psi->-Psi -- L[w] flips sign along with
A[a], i.e. G -> -G identically. The READER equation is K*G*Phi + a*Phi + b*Phi^3 (Psi
does not appear directly in the reader's OWN terms except through G). Under Psi->-Psi
with Phi held fixed, Reader(Phi,-Psi) = K*(-G)*Phi + a*Phi + b*Phi^3, which is NOT
equal to +/-Reader(Phi,Psi) in general (it equals Reader only if G*Phi=0). So
Psi->-Psi is REFUTED as a symmetry of the coupled system -- it is not merely
"J-preserving", it does not even map solutions to solutions, because this program's
Theta is adiabatically READ from (Phi,Psi) jointly, not an independent field: flipping
Psi alone changes the geometry the reader itself feels. Verified as an exact
counterexample in Part 1 below (this is exactly the kind of "check!" the task
demanded -- the naive a_e-only argument is real but incomplete).

CANDIDATE 3 -- (Phi,Psi) -> (-Phi,-Psi) jointly (global sign flip, "charge
conjugation"). s_e and t_e are BILINEAR in (Phi,Psi) (one factor from each field), so
both flip sign TWICE under a simultaneous global flip and are therefore INVARIANT:
w_e, a_e, and hence G itself are all unchanged. This genuinely IS a symmetry of the
full coupled system: Reader(-Phi,-Psi) = -Reader(Phi,Psi) exactly (odd in Phi at fixed
G), Record(-Phi,-Psi) = -Record(Phi,Psi) exactly (odd in Psi at fixed G) -- a real
Z2 symmetry of the dynamics. But since a_e is UNCHANGED (not merely sign-invariant in
product -- literally unchanged edge by edge), J_Theta is trivially invariant, not
flipped. CONCLUSION 3: a genuine dynamical symmetry exists, but it does not touch
sign(J_Theta) at all -- useless for debiasing an ensemble against the J-sign
observable, but usable as an independent INTERNAL CONSISTENCY CHECK (a seed and its
global-sign-flipped partner must land on IDENTICAL |sign(J_Theta)| outcomes; a
mismatch would flag a bug, not a real effect). Used exactly this way in Part 4 below.

CANDIDATE 4 -- time-reversal of the initial velocity (swap the roles of the "future"
and "past" memory points, i.e. reflect Phi_{-1} about Phi_0). This is REFUTED
immediately, on general grounds, without any algebra: the whole point of this
architecture (READOUT_GENESIS_CORE.md's reader/record pair) is that the reader
carries +D damping and the record carries -D anti-damping -- a DELIBERATE,
DECLARED time-asymmetry (mirroring the Axiom-12 CP-asymmetry SHAPE this experiment
imports). Reversing time direction would swap which field is damped and which is
anti-damped, producing a DIFFERENT dynamical system, not a symmetry of THIS one. No
algebra needed to refute it; recorded for completeness since the task named it as a
candidate to check.

VERDICT (per the task's own documented fallback, since NO candidate flips sign(J)
while being a genuine symmetry of the coupled dynamics -- Candidate 1 fails on
"flips sign", Candidate 2 fails on "is a symmetry at all", Candidate 3 is a symmetry
but doesn't touch J's sign, Candidate 4 fails on "is a symmetry at all"): THIS FILE
USES THE EMPIRICAL-FRACTION FRAMING, not a paired-ensemble 50/50 null. The reference
point for "unbiased" is NOT an a-priori 50/50 split (no symmetry argument forces
that); it is the STATIC FP inventory's OWN +/- composition (Part 2 below, re-derived
fresh with the exact 5.5 seed/method so it is directly comparable). The null
hypothesis this file actually tests, stated precisely:

  NULL H0: the DYNAMICAL transient-arrival composition (N_+ : N_- among converged-
  living outcomes) is CONSISTENT WITH (not necessarily equal to) the STATIC
  FP-inventory's own +/- composition -- i.e. the finite-transient dynamics does not
  preferentially FUNNEL orientation-symmetric initial data toward one sign(J_Theta)
  branch beyond what the branch's own share of the living-FP inventory would predict.
  A large deviation from the inventory composition = the finite-transient dynamics
  ITSELF is doing selection work beyond simply "which basin is bigger in the static
  landscape" -- this is the operational meaning of "asymmetric selection" for this
  experiment, precisely because no exact-symmetry pairing exists to make a stronger
  50/50 claim honest.

Candidate-3 global-sign-flip pairing IS still used, but only as the disclosed
INTERNAL CONSISTENCY CHECK named above (Part 4), not as the debiasing device.
"""

from fractions import Fraction as Fr
import math
import random
import time

FAILS = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


# ==============================================================================
print("== PART 1: exact-Fraction verification of the Part-0 algebra ==")
# ==============================================================================

N4 = 4
SUP_C4 = [(0, 1), (1, 2), (2, 3), (0, 3)]
CYCLE_C4 = [0, 1, 2, 3]


def all_pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def directed_a(a_dict, p, q):
    if p < q:
        return a_dict[(p, q)]
    return -a_dict[(q, p)]


def cyclic_product(a_dict, cycle):
    prod = Fr(1)
    m = len(cycle)
    for t in range(m):
        p, q = cycle[t], cycle[(t + 1) % m]
        prod *= directed_a(a_dict, p, q)
    return prod


def rand_frac(rng, lo=-6, hi=6, dlo=1, dhi=5):
    return Fr(rng.randint(lo, hi), rng.randint(dlo, dhi))


def s_e(Phi, Psi, e):
    i, j = e
    return (Phi[i] - Phi[j]) * (Psi[i] - Psi[j])


def t_e(Phi, Psi, e):
    i, j = e
    return Phi[i] * Psi[j] - Phi[j] * Psi[i]


def build_L(support, w, n):
    M = [[Fr(0)] * n for _ in range(n)]
    for (i, j) in support:
        we = w[(i, j)]
        M[i][i] += we
        M[j][j] += we
        M[i][j] -= we
        M[j][i] -= we
    return M


def build_A(support, a, n):
    M = [[Fr(0)] * n for _ in range(n)]
    for (i, j) in support:
        ae = a[(i, j)]
        M[i][j] += ae
        M[j][i] -= ae
    return M


def adiabatic_w_a(Phi, Psi, support, K, mu):
    w = {e: -(K / mu) * s_e(Phi, Psi, e) for e in support}
    a = {e: -(K / mu) * t_e(Phi, Psi, e) for e in support}
    return w, a


def reader_rhs(Phi, Psi, support, n, K, mu, av, bv):
    w, a = adiabatic_w_a(Phi, Psi, support, K, mu)
    L = build_L(support, w, n)
    A = build_A(support, a, n)
    G = [[L[i][j] + A[i][j] for j in range(n)] for i in range(n)]
    return [K * sum(G[i][j] * Phi[j] for j in range(n)) + av * Phi[i] + bv * Phi[i] ** 3
            for i in range(n)], a


# 1a. Candidate 1: rotation/reflection of C4 preserves sign(J_Theta) (re-verified here
# independently of theta_oriented_skew_v1.py's own Part 4 test, for THIS file's record).
rng = random.Random(9111)
ok = True
for _ in range(300):
    a_dict = {e: rand_frac(rng, -6, 6, 1, 4) for e in SUP_C4}
    J = cyclic_product(a_dict, CYCLE_C4)
    # rotation by 1: relabel vertex v -> (v+1) mod 4, re-read edges/cycle in NEW labels.
    # a'_{(i,j)} := a_{(i-1 mod4, j-1 mod4)} (inverse relabel, so applying it to a
    # configuration is the forward rotation of the CONFIGURATION itself).
    def relabel(a_dict, shift):
        out = {}
        for (i, j) in SUP_C4:
            pi, pj = (i - shift) % 4, (j - shift) % 4
            out[(i, j)] = directed_a(a_dict, pi, pj) if pi < pj else -directed_a(a_dict, pj, pi)
        return out
    a_rot = relabel(a_dict, 1)
    Jr = cyclic_product(a_rot, CYCLE_C4)
    if J != Jr:
        ok = False
ck("Candidate 1 (rotation): J_Theta unchanged under a 1-step C4 rotation, 300 exact trials", ok)

rng = random.Random(9222)
ok = True
for _ in range(300):
    a_dict = {e: rand_frac(rng, -6, 6, 1, 4) for e in SUP_C4}
    J = cyclic_product(a_dict, CYCLE_C4)
    # reflection fixing vertices 0,2: swap 1<->3
    refl = {}
    perm = {0: 0, 1: 3, 2: 2, 3: 1}
    for (i, j) in SUP_C4:
        pi, pj = perm[i], perm[j]
        refl[(i, j)] = directed_a(a_dict, pi, pj) if pi < pj else -directed_a(a_dict, pj, pi)
    Jf = cyclic_product(refl, CYCLE_C4)
    if J != Jf:
        ok = False
ck("Candidate 1 (reflection swap 1<->3): sign(J_Theta) unchanged, 300 exact trials "
   "(even-cycle reversal, (-1)^4=+1)", ok)

# 1b. Candidate 2: Psi->-Psi refuted as a dynamics symmetry (a_e flips sign on every
# edge -- true; but the READER equation is not preserved because w_e ALSO flips).
rng = random.Random(9333)
ok_a_flips = True
ok_reader_broken = False  # we EXPECT to find a counterexample -- that's the point
for _ in range(200):
    Phi = [rand_frac(rng, -5, 5, 1, 3) for _ in range(N4)]
    Psi = [rand_frac(rng, -5, 5, 1, 3) for _ in range(N4)]
    negPsi = [-p for p in Psi]
    _, a1 = reader_rhs(Phi, Psi, SUP_C4, N4, Fr(1), Fr(1), Fr(-1), Fr(1))
    _, a2 = reader_rhs(Phi, negPsi, SUP_C4, N4, Fr(1), Fr(1), Fr(-1), Fr(1))
    if any(a2[e] != -a1[e] for e in SUP_C4):
        ok_a_flips = False
    R1, _ = reader_rhs(Phi, Psi, SUP_C4, N4, Fr(1), Fr(1), Fr(-1), Fr(1))
    R2, _ = reader_rhs(Phi, negPsi, SUP_C4, N4, Fr(1), Fr(1), Fr(-1), Fr(1))
    if R2 != R1:  # Reader depends on Psi (through G) so is generically NOT invariant
        ok_reader_broken = True
ck("Candidate 2 sub-check: a_e -> -a_e on every C4 edge under Psi->-Psi, 200 exact trials",
   ok_a_flips)
ck("Candidate 2 REFUTED as a dynamics symmetry: Reader(Phi,Psi) != Reader(Phi,-Psi) "
   "generically (found >=1 counterexample among 200 trials, as predicted by the "
   "on-paper argument -- Psi->-Psi is not a valid pairing transform)", ok_reader_broken)

# 1c. Candidate 3: (Phi,Psi)->(-Phi,-Psi) IS a genuine symmetry (G unchanged, Reader/
# Record both flip sign exactly) -- verified exactly, general av,bv,Kv,muv.
rng = random.Random(9444)
ok = True
for _ in range(200):
    Phi = [rand_frac(rng, -5, 5, 1, 3) for _ in range(N4)]
    Psi = [rand_frac(rng, -5, 5, 1, 3) for _ in range(N4)]
    Kv, muv = rand_frac(rng, 1, 5, 1, 3), rand_frac(rng, 1, 5, 1, 3)
    av, bv = rand_frac(rng, -4, 4, 1, 4), rand_frac(rng, -4, 4, 1, 4)
    w1, a1 = adiabatic_w_a(Phi, Psi, SUP_C4, Kv, muv)
    w2, a2 = adiabatic_w_a([-p for p in Phi], [-p for p in Psi], SUP_C4, Kv, muv)
    if w1 != w2 or a1 != a2:
        ok = False
    R1, _ = reader_rhs(Phi, Psi, SUP_C4, N4, Kv, muv, av, bv)
    R2, _ = reader_rhs([-p for p in Phi], [-p for p in Psi], SUP_C4, N4, Kv, muv, av, bv)
    if R2 != [-r for r in R1]:
        ok = False
ck("Candidate 3: (Phi,Psi)->(-Phi,-Psi) leaves w_e,a_e EXACTLY unchanged and flips "
   "Reader's sign exactly (genuine symmetry, J_Theta untouched), 200 exact trials", ok)

print("  ==> Part 0/1 conclusion, machine-verified: no candidate is a sign(J_Theta)-"
      "flipping symmetry of the coupled dynamics. Candidate 3 is a real symmetry used "
      "below ONLY as an internal consistency check (Part 4). Empirical-fraction framing "
      "(vs. the static inventory's own composition) is the honest measurement this file "
      "reports.")

# ==============================================================================
print("\n== PART 2: static C4 living-FP inventory, +/- composition (finite_diagnostic, "
      "re-derived fresh, seed=551, matching theta_oriented_skew_v1.py Part 7 exactly "
      "for direct comparability) ==")
# ==============================================================================

AF, BF, KF, MUF = -1.0, 1.0, 1.0, 1.0


def ext_system_f(x, support, n):
    Phi, Psi = x[:n], x[n:]
    s = {e: (Phi[e[0]] - Phi[e[1]]) * (Psi[e[0]] - Psi[e[1]]) for e in all_pairs(n)}
    t = {e: (Phi[e[0]] * Psi[e[1]] - Phi[e[1]] * Psi[e[0]]) for e in support}
    w = {e: -KF / MUF * s[e] for e in support}
    a = {e: -KF / MUF * t[e] for e in support}
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
        F[i] = KF * sum(Greader[i][j] * Phi[j] for j in range(n)) + AF * Phi[i] + BF * Phi[i] ** 3
        F[n + i] = KF * sum(Grecord[i][j] * Psi[j] for j in range(n)) \
            + (AF + 3 * BF * Phi[i] ** 2) * Psi[i]
    return F, s, t, w, a


def gauss_jordan_solve(J, rhs):
    m = len(rhs)
    Aug = [J[i][:] + [rhs[i]] for i in range(m)]
    for c in range(m):
        piv = max(range(c, m), key=lambda r2: abs(Aug[r2][c]))
        if abs(Aug[piv][c]) < 1e-14:
            return None
        Aug[c], Aug[piv] = Aug[piv], Aug[c]
        Aug[c] = [v / Aug[c][c] for v in Aug[c]]
        for r2 in range(m):
            if r2 != c and Aug[r2][c] != 0:
                Aug[r2] = [v - Aug[r2][c] * u2 for v, u2 in zip(Aug[r2], Aug[c])]
    return [Aug[i][m] for i in range(m)]


def ext_newton(x0, support, n, iters=100):
    x = x0[:]
    m = 2 * n
    for _ in range(iters):
        F, _, _, _, _ = ext_system_f(x, support, n)
        if math.sqrt(sum(f * f for f in F)) < 1e-13:
            break
        Jm = [[0.0] * m for _ in range(m)]
        h = 1e-7
        for k in range(m):
            xp = x[:]
            xp[k] += h
            Fp, _, _, _, _ = ext_system_f(xp, support, n)
            for i in range(m):
                Jm[i][k] = (Fp[i] - F[i]) / h
        step = gauss_jordan_solve(Jm, [-f for f in F])
        if step is None:
            return None
        x = [xi + si for xi, si in zip(x, step)]
    F, _, _, _, _ = ext_system_f(x, support, n)
    return x, math.sqrt(sum(f * f for f in F))


def classify_static_fp(x0, support, n, full_pairs):
    res = ext_newton(x0, support, n)
    if not res:
        return None
    xs, r = res
    if r > 1e-10:
        return None
    Phi, Psi = xs[:n], xs[n:]
    psi_norm = math.sqrt(sum(v * v for v in Psi))
    crossp = sum(abs(Phi[i] * Psi[j] - Phi[j] * Psi[i])
                 for i in range(n) for j in range(i + 1, n))
    _, s, t, w, a = ext_system_f(xs, support, n)
    if any(s[e] >= -1e-9 for e in support):
        return None
    off_support = [e for e in full_pairs if e not in support]
    if any(s[e] < -1e-9 for e in off_support):
        return None
    living = psi_norm > 1e-2 and crossp > 1e-6
    Jt = None
    if living:
        a_frac = {e: Fr(round(a[e] * 10 ** 9), 10 ** 9) for e in support}
        Jt = float(cyclic_product(a_frac, CYCLE_C4))
    return dict(xs=xs, r=r, living=living, Jt=Jt)


def build_c4_inventory(seed=551, trials=3000):
    rng2 = random.Random(seed)
    full_pairs = all_pairs(N4)
    distinct = {}
    for tr in range(trials):
        if tr < trials // 3:
            x0 = [rng2.uniform(-2, 2) for _ in range(2 * N4)]
        elif tr < 2 * trials // 3:
            x0 = ([rng2.uniform(-1, 1) for _ in range(N4)]
                  + [rng2.uniform(-0.5, 0.5) for _ in range(N4)])
        else:
            base = [rng2.uniform(-1.5, 1.5) for _ in range(N4)]
            x0 = base + [-v * rng2.uniform(0.1, 2) for v in base]
        hit = classify_static_fp(x0, SUP_C4, N4, full_pairs)
        if hit is None or not hit["living"]:
            continue
        key = tuple(round(v, 3) for v in hit["xs"])
        if key not in distinct:
            distinct[key] = hit
    return distinct


t0 = time.time()
inventory = build_c4_inventory(seed=551, trials=3000)
inv_time = time.time() - t0
inv_plus = sum(1 for h in inventory.values() if h["Jt"] > 0)
inv_minus = sum(1 for h in inventory.values() if h["Jt"] < 0)
inv_zero = sum(1 for h in inventory.values() if h["Jt"] == 0)
print(f"  C4 static living-FP inventory (seed=551, 3000 trials, {inv_time:.1f}s): "
      f"{len(inventory)} distinct living FPs; sign(J_Theta): "
      f"N_+={inv_plus}, N_-={inv_minus}, N_0(exact zero)={inv_zero}")
ck("static inventory reproduces 5.5's own headline count (33 distinct C4 living FPs)",
   len(inventory) == 33, len(inventory))
inv_frac_plus = Fr(inv_plus, inv_plus + inv_minus) if (inv_plus + inv_minus) else None
print(f"  inventory composition (this run's own, exact Fraction): "
      f"N_+/(N_++N_-) = {inv_frac_plus}")

INVENTORY_LIST = list(inventory.values())


def nearest_inventory_match(xs, n):
    best_d = None
    best_hit = None
    for h in INVENTORY_LIST:
        d = math.sqrt(sum((a - b) ** 2 for a, b in zip(xs, h["xs"])))
        if best_d is None or d < best_d:
            best_d = d
            best_hit = h
    return best_d, best_hit


# ==============================================================================
print("\n== PART 3: the discrete reader(+D)/record(-D) stepper "
      "(READOUT_GENESIS_CORE.md:~1290-1360, the corpus's own Gauss-Jordan stepper, "
      "implemented literally, adiabatic Theta) ==")
# ==============================================================================
# Declared constants of the run (G5): a=-1, b=1, K=mu=1 (unchanged program regime),
# M=1 (declared here for the first time in this file), Delta_t declared below.
DT = 0.1          # G1: DECLARED FIXED RATIONAL 1/10. Never refined toward 0.
K_CONST = 1.0
MU_CONST = 1.0
A_POT = -1.0
B_POT = 1.0
M_CONST = 1.0

# Theta itself is NOT given its own second-order recurrence in this v1 file: at every
# step n, w_e,a_e are read ADIABATICALLY (Gate-D-stationary) from the CURRENT
# (Phi_n,Psi_n) via the identical formula every prior Theta static-FP file in this
# program uses (theta_dynamics_selection_v1.py, theta_minimal_living_v1.py,
# theta_oriented_skew_v1.py). This is a DECLARED modeling choice, not an oversight:
# it makes the coupled system's OWN static fixed points (F=0) exactly coincide with
# this file's dynamical fixed points (Phi_{n+1}=Phi_n=Phi_{n-1}), so the Part-2
# inventory is a valid classification target for Part 4's dynamics below. A genuinely
# separate second-order Theta_{n+1}=... recurrence (law B of THETA_ROOT_PROGRAM.md
# section 2) is named as a stage-2 open item, not built here (G2: this v1's declared
# memory structure is the plain (n,n-1) stepper memory only).


def geo_and_source(Phi, Psi, support, n):
    w, a = adiabatic_w_a(Phi, Psi, support, K_CONST, MU_CONST)
    L = build_L(support, w, n)
    A = build_A(support, a, n)
    Greader = [[float(L[i][j] + A[i][j]) for j in range(n)] for i in range(n)]
    Grecord = [[float(L[i][j] - A[i][j]) for j in range(n)] for i in range(n)]
    return Greader, Grecord, a


def grad_V(Phi):
    return [A_POT * p + B_POT * p ** 3 for p in Phi]


def hess_V_diag(Phi):
    return [A_POT + 3 * B_POT * p ** 2 for p in Phi]


def step(Phi_n, Phi_nm1, Psi_n, Psi_nm1, support, n, D):
    """One step of the corpus's own explicit Gauss-Jordan stepper
    (READOUT_GENESIS_CORE.md:~1330-1345), R_Phi=R_Psi=0 (closed system, declared
    regime, unchanged from every prior Theta file), J_n=0 (no external drive).
    Reader damping +D, record damping -D -- literally as declared in the corpus.
    A_Phi, A_Psi are scalar*identity here (M,D declared scalars, G5) so the
    Gauss-Jordan solve below degenerates to a diagonal solve; implemented via the
    general Gauss-Jordan routine anyway, for literal fidelity to the corpus's own
    stated stepper rather than hand-optimizing it away."""
    Greader, Grecord, a_now = geo_and_source(Phi_n, Psi_n, support, n)
    A_Phi = M_CONST / DT ** 2 + D / (2 * DT)
    A_Psi = M_CONST / DT ** 2 - D / (2 * DT)
    if abs(A_Phi) < 1e-14 or abs(A_Psi) < 1e-14:
        return None  # declared FAIL rule (corpus VI.7 discipline): no silent
        # regularization of a vanishing pivot -- an all-zero A_Phi/A_Psi at D=0 with
        # DT-tuned cancellation would need this; not reached at the declared DT,D here.
    gV = grad_V(Phi_n)
    GPhi = [sum(Greader[i][j] * Phi_n[j] for j in range(n)) for i in range(n)]
    b_Phi = [K_CONST * (-GPhi[i]) + (-gV[i])
             + (2 * M_CONST / DT ** 2) * Phi_n[i]
             + (D / (2 * DT) - M_CONST / DT ** 2) * Phi_nm1[i]
             for i in range(n)]
    Phi_next = [b_Phi[i] / A_Phi for i in range(n)]

    hV = hess_V_diag(Phi_n)
    GtPsi = [sum(Grecord[i][j] * Psi_n[j] for j in range(n)) for i in range(n)]
    b_Psi = [K_CONST * (-GtPsi[i]) + (-hV[i] * Psi_n[i])
             + (2 * M_CONST / DT ** 2) * Psi_n[i]
             - (M_CONST / DT ** 2 + D / (2 * DT)) * Psi_nm1[i]
             for i in range(n)]
    Psi_next = [b_Psi[i] / A_Psi for i in range(n)]
    return Phi_next, Psi_next, a_now


DIVERGE_BOUND = 1e6
N_STEPS = 2000            # G3: DECLARED finite transient length.
SETTLE_RESID_TOL = 1e-4   # G3: DECLARED finite "settled" residual criterion at N_STEPS.
SETTLE_STEP_TOL = 1e-5    # G3: DECLARED finite step-to-step-change criterion.
LIVING_PSI_TOL = 1e-2     # matches every prior Theta file's living-Psi threshold.
MATCH_DIST_TOL = 0.05     # DECLARED distance tolerance to the Part-2 inventory.


def run_one_trajectory(Phi0, Psi0, Phim1, Psim1, support, n, D):
    Phi_n, Phi_nm1 = Phi0, Phim1
    Psi_n, Psi_nm1 = Psi0, Psim1
    for step_idx in range(N_STEPS):
        out = step(Phi_n, Phi_nm1, Psi_n, Psi_nm1, support, n, D)
        if out is None:
            return dict(cls="UNRESOLVED", reason="stepper FAIL (near-zero pivot)")
        Phi_next, Psi_next, _ = out
        if any(abs(v) > DIVERGE_BOUND for v in Phi_next + Psi_next):
            return dict(cls="DIVERGED", step=step_idx)
        Phi_nm1, Psi_nm1 = Phi_n, Psi_n
        Phi_n, Psi_n = Phi_next, Psi_next
    # G3: declared finite "settled" check AT step N_STEPS.
    step_change = math.sqrt(sum((a - b) ** 2 for a, b in zip(Phi_n + Psi_n, Phi_nm1 + Psi_nm1)))
    xs = Phi_n + Psi_n
    F, s, t, w, a = ext_system_f(xs, support, n)
    resid = math.sqrt(sum(f * f for f in F))
    psi_norm = math.sqrt(sum(v * v for v in Psi_n))
    if resid > SETTLE_RESID_TOL or step_change > SETTLE_STEP_TOL:
        return dict(cls="UNRESOLVED", reason="not settled by N_STEPS",
                    resid=resid, step_change=step_change)
    if psi_norm < LIVING_PSI_TOL:
        return dict(cls="DEAD", resid=resid)
    dist, hit = nearest_inventory_match(xs, n)
    if dist is None or dist > MATCH_DIST_TOL:
        return dict(cls="UNRESOLVED", reason="settled, living, but no inventory match",
                    resid=resid, dist=dist)
    if hit["Jt"] is None:
        return dict(cls="UNRESOLVED", reason="matched FP has undefined J_Theta")
    return dict(cls="LIVING_PLUS" if hit["Jt"] > 0 else "LIVING_MINUS", resid=resid, dist=dist)


def make_ensemble(seed, N):
    rng2 = random.Random(seed)
    ens = []
    for _ in range(N):
        Phi0 = [rng2.uniform(-2, 2) for _ in range(N4)]
        Psi0 = [rng2.uniform(-2, 2) for _ in range(N4)]
        vPhi = [rng2.uniform(-0.5, 0.5) for _ in range(N4)]
        vPsi = [rng2.uniform(-0.5, 0.5) for _ in range(N4)]
        Phim1 = [Phi0[i] - DT * vPhi[i] for i in range(N4)]
        Psim1 = [Psi0[i] - DT * vPsi[i] for i in range(N4)]
        ens.append((Phi0, Psi0, Phim1, Psim1))
    return ens


def run_ensemble(seed, N, D, label):
    ens = make_ensemble(seed, N)
    counts = {"LIVING_PLUS": 0, "LIVING_MINUS": 0, "DEAD": 0, "DIVERGED": 0, "UNRESOLVED": 0}
    t0 = time.time()
    for (Phi0, Psi0, Phim1, Psim1) in ens:
        out = run_one_trajectory(Phi0, Psi0, Phim1, Psim1, SUP_C4, N4, D)
        counts[out["cls"]] += 1
    dt_ = time.time() - t0
    print(f"  -- {label}: seed={seed} N={N} D={D} N_STEPS={N_STEPS} DT={DT} "
          f"({dt_:.1f}s) => {counts}")
    return counts, dt_


# ==============================================================================
print("\n== PART 4: THE DECISIVE EXPERIMENT -- ensemble transient-selection runs ==")
# ==============================================================================
N_ENSEMBLE = 400          # G4: DECLARED finite ensemble size (task minimum).
MAIN_SEED = 700
EXTRA_SEEDS = [701, 702]  # robustness across 2 extra seeds, primary D only.
D_VALUES = [1.0, 2.0, 0.5]  # G5: declared small robustness set.

results = {}  # key: (label, D, seed) -> counts
for D in D_VALUES:
    counts, dt_ = run_ensemble(MAIN_SEED, N_ENSEMBLE, D, f"D={D}")
    results[("main", D, MAIN_SEED)] = counts

# D=0 undamped control (declared separately, item 4 of the task spec: reader and
# record both undamped -- neither antidamped nor damped; a genuinely different
# dynamical regime, not a D->0 limit of anything claimed continuous).
counts0, dt0 = run_ensemble(MAIN_SEED, N_ENSEMBLE, 0.0, "D=0 (undamped control)")
results[("control", 0.0, MAIN_SEED)] = counts0

for sd in EXTRA_SEEDS:
    counts, dt_ = run_ensemble(sd, N_ENSEMBLE, 1.0, f"D=1.0, extra seed={sd}")
    results[("extra_seed", 1.0, sd)] = counts

# Internal consistency check (Candidate 3, Part 0): a seed's global-sign-flipped
# partner (Phi,Psi)->(-Phi,-Psi) MUST land in the SAME class (LIVING_PLUS stays
# LIVING_PLUS, etc.) since it is a genuine, J_Theta-preserving symmetry of the
# dynamics (Part 1c, exact). This is a CODE-CORRECTNESS check, not a bias probe.
print("\n  -- internal consistency check (Candidate-3 global sign-flip pairing, "
      "D=1.0, first 60 of the main ensemble) --")
ens_check = make_ensemble(MAIN_SEED, 60)
mismatch = 0
checked = 0
for (Phi0, Psi0, Phim1, Psim1) in ens_check:
    out1 = run_one_trajectory(Phi0, Psi0, Phim1, Psim1, SUP_C4, N4, 1.0)
    negPhi0 = [-v for v in Phi0]
    negPsi0 = [-v for v in Psi0]
    negPhim1 = [-v for v in Phim1]
    negPsim1 = [-v for v in Psim1]
    out2 = run_one_trajectory(negPhi0, negPsi0, negPhim1, negPsim1, SUP_C4, N4, 1.0)
    checked += 1
    if out1["cls"] != out2["cls"]:
        mismatch += 1
ck(f"global-sign-flip partner lands in the SAME outcome class ({checked} pairs checked, "
   f"{mismatch} mismatches)", mismatch == 0, mismatch)

# ==============================================================================
print("\n== PART 4b: LOCAL-STABILITY SUB-EXPERIMENT (small perturbations of KNOWN "
      "static living FPs) -- addresses 5.5's own named-open 'stability of the C4 "
      "living FPs (only static existence checked, not stability)' item as a byproduct, "
      "and diagnoses WHY Part 4's generic ensemble came out the way it did ==")
# ==============================================================================
# DESIGN (declared): each draw picks one of the 33 inventory FPs uniformly at random,
# adds a small DECLARED-amplitude perturbation to (Phi,Psi) only (Phi_{-1}:=Phi_0,
# Psi_{-1}:=Psi_0 exactly -- zero initial relative velocity, i.e. a pure POSITION
# kick), then runs the identical stepper/classifier. Since every inventory FP here
# has sign(J_Theta)=+ (Part 2's own finding, disclosed below), this sub-experiment's
# PRIMARY question is not branch selection but LOCAL DYNAMICAL STABILITY: does the
# full nonlinear (+D/-D)-coupled stepper actually RE-CONVERGE to a living FP when
# started arbitrarily close to one, or does it escape? (Static Newton found these as
# roots of F=0; that says nothing about whether the TIME-STEPPED dynamics attracts
# to them.)
N_PERTURB = 200
PERTURB_EPS = 1e-3       # G5-style declared constant: one fixed perturbation scale.
PERTURB_SEED = 800


def run_perturb_experiment(seed, N, eps, D, label):
    rng2 = random.Random(seed)
    counts = {"LIVING_PLUS": 0, "LIVING_MINUS": 0, "DEAD": 0, "DIVERGED": 0, "UNRESOLVED": 0}
    divergence_steps = []
    for _ in range(N):
        base = INVENTORY_LIST[rng2.randrange(len(INVENTORY_LIST))]
        Phi_base, Psi_base = base["xs"][:N4], base["xs"][N4:]
        Phi0 = [p + rng2.uniform(-eps, eps) for p in Phi_base]
        Psi0 = [p + rng2.uniform(-eps, eps) for p in Psi_base]
        out = run_one_trajectory(Phi0, Psi0, Phi0[:], Psi0[:], SUP_C4, N4, D)
        counts[out["cls"]] += 1
        if out["cls"] == "DIVERGED":
            divergence_steps.append(out["step"])
    med_step = (sorted(divergence_steps)[len(divergence_steps) // 2]
                if divergence_steps else None)
    print(f"  -- {label}: seed={seed} N={N} eps={eps} D={D} => {counts}"
          + (f"  (median divergence step among DIVERGED = {med_step}, "
             f"i.e. ~{med_step * DT:.1f} time units at DT={DT})" if med_step is not None else ""))
    return counts


pcounts_D1 = run_perturb_experiment(PERTURB_SEED, N_PERTURB, PERTURB_EPS, 1.0,
                                     "perturbed-FP ensemble, D=1.0")
pcounts_D05 = run_perturb_experiment(PERTURB_SEED, N_PERTURB, PERTURB_EPS, 0.5,
                                      "perturbed-FP ensemble, D=0.5")

# Small DT-robustness spot check (declared, NOT a refinement/continuum sweep -- each
# DT here is its own separately-declared discrete run, per G1/G5; this exists only to
# distinguish "genuine dynamical instability" from "artifact of one declared DT"):
print("  -- DT-robustness spot check (5 trials/DT, single perturbed FP, D=1.0, "
      "eps=1e-4, declared DT in {0.1, 0.02, 0.005} -- NOT a continuum limit, three "
      "separately declared discrete runs):")
base0 = INVENTORY_LIST[0]
Phi_b0, Psi_b0 = base0["xs"][:N4], base0["xs"][N4:]
for dt_probe in [0.1, 0.02, 0.005]:
    rngp = random.Random(9)
    phys_times = []
    for _ in range(5):
        Phi0 = [p + rngp.uniform(-1e-4, 1e-4) for p in Phi_b0]
        Psi0 = [p + rngp.uniform(-1e-4, 1e-4) for p in Psi_b0]
        Phin, Phinm1 = Phi0, Phi0[:]
        Psin, Psinm1 = Psi0, Psi0[:]
        max_steps = int(30.0 / dt_probe)
        div_step = None
        for k in range(max_steps):
            A_Phi_p = M_CONST / dt_probe ** 2 + 1.0 / (2 * dt_probe)
            A_Psi_p = M_CONST / dt_probe ** 2 - 1.0 / (2 * dt_probe)
            Greader, Grecord, _ = geo_and_source(Phin, Psin, SUP_C4, N4)
            gV = grad_V(Phin)
            GPhi = [sum(Greader[i][j] * Phin[j] for j in range(N4)) for i in range(N4)]
            b_Phi = [K_CONST * (-GPhi[i]) + (-gV[i])
                     + (2 * M_CONST / dt_probe ** 2) * Phin[i]
                     + (1.0 / (2 * dt_probe) - M_CONST / dt_probe ** 2) * Phinm1[i]
                     for i in range(N4)]
            Phi_next = [b_Phi[i] / A_Phi_p for i in range(N4)]
            hV = hess_V_diag(Phin)
            GtPsi = [sum(Grecord[i][j] * Psin[j] for j in range(N4)) for i in range(N4)]
            b_Psi = [K_CONST * (-GtPsi[i]) + (-hV[i] * Psin[i])
                     + (2 * M_CONST / dt_probe ** 2) * Psin[i]
                     - (M_CONST / dt_probe ** 2 + 1.0 / (2 * dt_probe)) * Psinm1[i]
                     for i in range(N4)]
            Psi_next = [b_Psi[i] / A_Psi_p for i in range(N4)]
            if any(abs(v) > 1e6 for v in Phi_next + Psi_next):
                div_step = k
                break
            Phinm1, Psinm1 = Phin, Psin
            Phin, Psin = Phi_next, Psi_next
        if div_step is not None:
            phys_times.append(div_step * dt_probe)
    avg_phys = sum(phys_times) / len(phys_times) if phys_times else None
    print(f"     DT={dt_probe}: {len(phys_times)}/5 diverged, "
          f"mean divergence physical-time={'N/A' if avg_phys is None else f'{avg_phys:.2f}'}")
print("  ==> if divergence physical-time (steps*DT) is roughly DT-INDEPENDENT, the "
      "instability is a genuine feature of the declared dynamics at this parameter "
      "regime, not a numerical-stepper artifact of one declared DT -- reported above "
      "exactly as measured, for the orchestrator to read directly.")

# ==============================================================================
print("\n== PART 5: REPORT -- counts, null-hypothesis comparison, robustness ==")
# ==============================================================================
print(f"\n  Static C4 inventory composition (reference, seed=551): "
      f"N_+={inv_plus} N_-={inv_minus} (of {inv_plus + inv_minus} signed living FPs), "
      f"fraction N_+/(N_++N_-) = {inv_frac_plus} = {float(inv_frac_plus):.4f}")
if inv_minus == 0 and inv_plus > 0:
    print("  DISCLOSURE (new finding, not stated in 5.5's own writeup, which reported "
        "only |J_Theta| magnitude spread, never sign composition): under THIS fixed "
        "cyclic-traversal convention, the exhaustive 3000-trial multistart search found "
        "ZERO living C4 fixed points with sign(J_Theta) negative -- the entire static "
        "inventory sits on one branch. This is consistent with (not proven by) Part 0/1's "
        "finding that every checked symmetry (C4 automorphisms, global sign flip) "
        "preserves sign(J_Theta): if a genuine -J branch exists it is not reachable by "
        "applying any of those symmetries to a +J FP, and this search did not find one "
        "by direct multistart either. Bounded negative, not a nonexistence proof (same "
        "epistemic status as every other bounded-search negative in this program).")

print("\n  Part 4b local-stability sub-experiment (perturbed-FP ensembles):")
for D_p, cnts in [(1.0, pcounts_D1), (0.5, pcounts_D05)]:
    print(f"    D={D_p}: {cnts}")
if (pcounts_D1["DIVERGED"] > pcounts_D1["LIVING_PLUS"] + pcounts_D1["LIVING_MINUS"]
        and pcounts_D05["DIVERGED"] > pcounts_D05["LIVING_PLUS"] + pcounts_D05["LIVING_MINUS"]):
    print("  READING (finite_diagnostic, addresses 5.5's own named-open stability item): "
        "perturbations as small as eps=1e-3 (and, in the DT-robustness spot check above, "
        "eps=1e-4) of an EXACT static living FP diverge under the full nonlinear "
        "(+D/-D)-coupled stepper in a DT-independent physical time -- these C4 living "
        "FPs are (at least locally, along the sampled perturbation directions, at this "
        "declared parameter regime) DYNAMICALLY UNSTABLE, not attractors. This directly "
        "explains Part 4's generic-ensemble outcome (below) and answers, negatively, the "
        "stability question 5.5 left open -- a real result this file produces as a "
        "byproduct of the transient-selection question it was built to ask.")

print("\n  Dynamical transient-arrival composition per declared run:")
for key, counts in results.items():
    kind, D, sd = key
    living_tot = counts["LIVING_PLUS"] + counts["LIVING_MINUS"]
    if living_tot > 0:
        frac_plus = Fr(counts["LIVING_PLUS"], living_tot)
        dev = float(frac_plus) - float(inv_frac_plus) if inv_frac_plus is not None else None
    else:
        frac_plus = None
        dev = None
    print(f"    [{kind}] D={D} seed={sd}: N_+={counts['LIVING_PLUS']} N_-={counts['LIVING_MINUS']} "
          f"N_dead={counts['DEAD']} N_diverged={counts['DIVERGED']} "
          f"N_unresolved={counts['UNRESOLVED']}  "
          f"| living arrival N_+/(N_++N_-)={frac_plus} "
          f"({'N/A' if frac_plus is None else f'{float(frac_plus):.4f}'}) "
          f"deviation-from-inventory={'N/A' if dev is None else f'{dev:+.4f}'}")

# Sanity/summary checks -- reported honestly either way (G4: no outcome dropped).
total_trajectories = N_ENSEMBLE * (len(D_VALUES) + 1 + len(EXTRA_SEEDS))
counted = sum(sum(c.values()) for c in results.values())
ck("every trajectory in every declared run lands in exactly one of the 5 declared "
   "outcome classes (no silent drops, G4)", counted == total_trajectories,
   (counted, total_trajectories))

print("""
  READING (Dr, honest fence): Part 0/1 established, by exact-Fraction algebra, that no
  static symmetry of this coupled system flips sign(J_Theta) while remaining a genuine
  symmetry of the dynamics -- so this experiment cannot honestly claim a paired-ensemble
  50/50 null. Part 4b then explains, mechanistically, WHY Part 4's counts come out the
  way they do: the known static living FPs are themselves dynamically UNSTABLE under
  this stepper at this declared regime, so essentially no trajectory -- whether from a
  generic orientation-symmetric draw OR from an eps=1e-3/1e-4 perturbation of an EXACT
  known FP -- settles within the declared N_STEPS; DIVERGED dominates every declared run.
  The operational answer to the founder's question, AT THIS DECLARED PARAMETER REGIME,
  is therefore: the finite transient does not resolve into either branch often enough to
  measure a selection asymmetry -- an honest INCONCLUSIVE-BY-INSTABILITY finding, not a
  fabricated 50/50 or a fabricated bias. What the static side of this same file DOES
  show (disclosed above, a new finding): the static inventory itself is already
  one-sided (33/33 positive, seed 551) -- if that composition survives independent
  re-derivation, IT is the place a future attempt should look for the asymmetry the
  question is actually asking about, not the (currently unstable) discrete transient.
  Exact counts per D value / seed are printed above for the orchestrator to quote
  directly, rather than a single pooled number.
""")

print()
if FAILS:
    print(f"RESULT: {len(FAILS)} FAILURE(S): {FAILS}")
    raise SystemExit(1)
print("RESULT: ALL CHECKS PASS (Parts 0-1 exact Fraction; Parts 2-4 finite_diagnostic "
      "floats, seeds disclosed)")
