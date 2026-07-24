#!/usr/bin/env python3
"""
Item 25 -- discrete gauge-orbit + measure, extended from an abelian (Z2) precedent to a genuine
NON-ABELIAN test group, 2026-07-24. This is Attempt 1 at ITEM25_26_SCOPING_LOG.md's missing piece
(1): "A discrete analogue of the gauge orbit (the space of connections modulo gauge transformations
h_i) with an actual volume/measure on it -- nothing in this repo currently defines 'the set of all
connections' as an object with a measure; only single connections/holonomies are built."

WHERE THIS COMES FROM (root-native, not borrowed -- per an ultracode cross-domain sweep this
session that found a runnable Z2-gauge-orbit-quotient construction in a sibling standalone package
by the same author/root, `ROOT_NATIVE_PAGE_CURVE_COMPLETE_EXPERIMENT_PACKAGE_v1.0.0/
08_FOUNDATION_TESTS/z2_mass_gap_adversarial_test.py`): that file builds "all gauge orbits and the
physical quotient" for an ABELIAN Z2 lattice gauge theory. ITS OWN SUBJECT (a mass-gap adversarial
test) is explicitly OUT OF SCOPE here -- HANDOFF_NEXT_SESSION.md item 27 forbids pursuing the
continuum Yang-Mills mass gap (Clay Millennium Problem, readout-not-truth non-goal). This file
extracts and reuses ONLY that source's gauge-orbit-quotient CONSTRUCTION TECHNIQUE (partition
configuration space into orbits under simultaneous vertex gauge transformations; build a normalized
orbit-indicator basis), never anything about a mass gap, on a DIFFERENT, non-abelian test group.

WHY NON-ABELIAN, AND WHY THIS IS NOT ARBITRARY: item 25 ultimately needs SU(3)xSU(2)xU(1), which is
non-abelian -- the Z2 precedent's abelian character-theory shortcuts (used there to prove
positivity) do not obviously generalize. This file's gauge transformation law is
`U'_{j<-i} = g_j . U_{j<-i} . g_i^{-1}` -- THE EXACT SAME LAW this repo's own
`InfoGaugeLocalizationConnectionHolonomy.v` (ROOT_TO_SM_DAG.md, gates G0.3/G0.4) already proves
Th_coqc, both existence and uniqueness, for ANY group (G, id, mul, inv), not just abelian ones. This
file is therefore the first time that ALREADY-PROVEN general theorem is actually EXERCISED on a
genuine non-abelian example (S3, the symmetric group on 3 letters, order 6 -- the smallest
non-abelian group, chosen only for tractability, not physical significance).

Run: python3 nonabelian_gauge_orbit_v1.py  (requires numpy)
"""
import itertools
import numpy as np

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print("  finite_diagnostic (exact finite-group enumeration, reproducible) for the orbit/basis")
print("  construction; Dr for the interpretation as a step toward item 25's missing piece (1).")

# ============================================================================
# (1) S3 -- the smallest non-abelian group, as permutations of (0,1,2), composed left-to-right.
print("\n== 1. S3 group table (permutations of 3 letters, the smallest non-abelian group) ==")
S3 = list(itertools.permutations((0, 1, 2)))   # 6 elements, tuples
ID = (0, 1, 2)

def mul(a, b):
    """a . b : apply b first, then a (standard permutation composition)."""
    return tuple(a[b[i]] for i in range(3))

def inv(a):
    r = [0, 0, 0]
    for i, v in enumerate(a):
        r[v] = i
    return tuple(r)

ck("S3 has 6 elements", len(S3) == 6, len(S3))
ck("identity is in S3", ID in S3)
ck("S3 is non-abelian (found a genuine non-commuting pair)",
   any(mul(a, b) != mul(b, a) for a in S3 for b in S3))
ck("every element has an inverse in S3 (closure of inv)",
   all(mul(a, inv(a)) == ID for a in S3))

# ============================================================================
# (2) Tiny lattice -- a single elementary square loop: 4 vertices, 4 directed links (a plaquette),
#     the smallest nontrivial closed loop, matching this repo's own R5-R7 connection/holonomy/
#     curvature primitives (ROOT_TO_SM_DAG.md) exactly: U_{j<-i}, H_C=U_C (product around the loop),
#     K_C = H_C - I (readout of curvature).
print("\n== 2. tiny lattice: one plaquette, 4 vertices (0,1,2,3), 4 directed links forming a loop ==")
VERTICES = [0, 1, 2, 3]
LINKS = [(0, 1), (1, 2), (2, 3), (3, 0)]   # link k: from vertex LINKS[k][0] to LINKS[k][1]
N_LINKS = len(LINKS)
ck("lattice has 4 vertices and 4 links (elementary plaquette)", len(VERTICES) == 4 and N_LINKS == 4)

# Configuration space: an assignment U: link -> S3 element. |S3|^4 = 1296 configs.
CONFIGS = list(itertools.product(S3, repeat=N_LINKS))
ck("configuration space size = |S3|^4 = 1296", len(CONFIGS) == 1296, len(CONFIGS))

# ============================================================================
# (3) Gauge transformation law -- EXACTLY this repo's own Th_coqc law, G0.4:
#     U'_{j<-i} = g_j . U_{j<-i} . g_i^{-1}   for g: vertex -> G (any group).
print("\n== 3. gauge transformation law U'_{j<-i} = g_j . U_{j<-i} . g_i^-1 (this repo's own ==")
print("      G0.4 law, InfoGaugeLocalizationConnectionHolonomy.v, proved for ANY group) ==")

def gauge_transform(config, g):
    """Apply vertex gauge transformation g: vertex -> S3 element to every link in config."""
    out = []
    for k, (i, j) in enumerate(LINKS):
        out.append(mul(mul(g[j], config[k]), inv(g[i])))
    return tuple(out)

# CORRECTED after independent adversarial review, 2026-07-24: an earlier draft of this file fixed
# vertex 0's gauge to identity (the trick the Z2 precedent uses), reasoning it only removes a
# trivial global redundancy. Review caught this is WRONG for non-abelian S3: fixing one vertex
# removes *local* redundancy but leaves a residual GLOBAL SIMULTANEOUS-CONJUGATION symmetry
# unfixed (config -> h.config.h^-1 pointwise, for a single h, is NOT reachable by any g with
# g[0]=ID unless h=ID) -- for abelian Z2 conjugation is trivial so the shortcut is harmless there;
# for S3 it silently double-counts. FIX: use the FULL, UNFIXED gauge group G^4 (g at every one of
# the 4 vertices, matching G0.4's own stated generality), exactly as this repo's own Th_coqc law
# is proved for (InfoGaugeLocalizationConnectionHolonomy.v allows a frame choice at every node).
GAUGE_GROUP_ELEMS = list(itertools.product(S3, repeat=4))   # (g0, g1, g2, g3), ALL 4 vertices free
ck("gauge-transformation parameter space size = |S3|^4 = 1296 (all 4 vertices free, matching this "
   "repo's own G0.4 law -- corrected from an earlier vertex-0-fixed draft, see note above)",
   len(GAUGE_GROUP_ELEMS) == 1296, len(GAUGE_GROUP_ELEMS))

def apply_gauge(config, g0123):
    g = {0: g0123[0], 1: g0123[1], 2: g0123[2], 3: g0123[3]}
    return gauge_transform(config, g)

# spot check: identity gauge transformation is a no-op
ck("identity gauge transformation (g0=g1=g2=g3=ID) leaves every config fixed (spot check, 20 samples)",
   all(apply_gauge(CONFIGS[i], (ID, ID, ID, ID)) == CONFIGS[i] for i in range(0, 1296, 65)))

# ============================================================================
# (4) Build all gauge orbits (the physical quotient) -- algorithmic technique adapted from the Z2
#     precedent (z2_mass_gap_adversarial_test.py), generalized from an abelian sign-flip group to
#     genuine S3 composition, and corrected to use the FULL unfixed gauge group (see note above).
print("\n== 4. construct all gauge orbits under the FULL, unfixed gauge group (1296 elements) ==")
config_index = {cfg: idx for idx, cfg in enumerate(CONFIGS)}
seen = set()
orbits = []
for idx, cfg in enumerate(CONFIGS):
    if idx in seen:
        continue
    orbit_indices = sorted({config_index[apply_gauge(cfg, g0123)] for g0123 in GAUGE_GROUP_ELEMS})
    orbits.append(orbit_indices)
    seen.update(orbit_indices)

N_PHYS = len(orbits)
print(f"   {len(CONFIGS)} raw configs partition into {N_PHYS} gauge orbits (physical/gauge-")
print(f"   invariant classes)")
ck("every config belongs to exactly one orbit (orbits partition the full 1296-config space)",
   sum(len(o) for o in orbits) == 1296 and len(seen) == 1296)
ck("orbit sizes divide the gauge-parameter-space size 1296 (orbit-stabilizer theorem sanity check)",
   all(1296 % len(o) == 0 for o in orbits))
ck("N_phys < 1296 (the quotient is a genuine, nontrivial reduction -- gauge redundancy is real)",
   N_PHYS < 1296, N_PHYS)
ck("N_phys == 3, orbit sizes == {216, 432, 648} -- EXACTLY S3's 3 conjugacy classes ({e}, the 3 "
   "transpositions, the 2 3-cycles), independently re-derived by adversarial review via a separate "
   "holonomy-fiber method and matched exactly -- confirms the correction (was wrongly 6 orbits of "
   "216 each under the vertex-0-fixed shortcut, an earlier draft's bug, now fixed)",
   N_PHYS == 3 and sorted(len(o) for o in orbits) == [216, 432, 648],
   (N_PHYS, sorted(len(o) for o in orbits)))

# ============================================================================
# (5) Orbit basis / measure -- normalized indicator vectors per orbit (the discrete "volume" on
#     the orbit space this repo currently lacks, per ITEM25_26_SCOPING_LOG.md's own wording).
print("\n== 5. orbit basis B: normalized indicator per orbit (the discrete gauge-orbit MEASURE) ==")
B = np.zeros((1296, N_PHYS))
for j, orbit in enumerate(orbits):
    w = 1.0 / np.sqrt(len(orbit))
    for idx in orbit:
        B[idx, j] = w

BtB = B.T @ B
ck("B^T B = I_{N_phys} (B is an isometry -- the orbit basis is a well-defined, orthonormal ==",
   np.allclose(BtB, np.eye(N_PHYS)))
ck("B has no negative or complex entries (a genuine nonnegative measure/partition-of-mass, ==",
   np.all(B >= 0))

# ============================================================================
# (6) NEW CHECK (not present in the Z2 precedent): does this repo's OWN curvature readout
#     K_C = H_C - I actually respect the orbit structure -- i.e. is K_C's TRACE (a gauge-invariant
#     scalar readout, since tr(g A g^-1) = tr(A)) constant across every config within one orbit?
#     This is a genuine, previously-unchecked consistency test between the orbit construction here
#     and this repo's own existing R5-R7 connection/holonomy/curvature primitives.
print("\n== 6. NEW CHECK: is tr(K_C) (this repo's own curvature readout) gauge-orbit-invariant? ==")

def holonomy(config):
    """H_C = product of link elements around the closed loop 0->1->2->3->0 (this repo's own R6)."""
    h = ID
    for u in config:
        h = mul(u, h)
    return h

def trace_proxy(perm):
    """A permutation-representation trace proxy: number of fixed points of the permutation matrix
    (a genuine, standard invariant of a permutation under conjugation -- conjugate permutations
    have identical cycle type, hence identical fixed-point count)."""
    return sum(1 for i in range(3) if perm[i] == i)

orbit_trace_consistent = True
for orbit in orbits:   # only N_PHYS=3 orbits total after the correction -- check ALL of them, not a sample
    traces = {trace_proxy(holonomy(CONFIGS[idx])) for idx in orbit}
    if len(traces) != 1:
        orbit_trace_consistent = False
        break
ck(f"tr(H_C) (fixed-point count of the holonomy permutation) is IDENTICAL for every config within "
   f"the same gauge orbit, checked EXHAUSTIVELY across all {len(orbits)} orbits (this repo's own "
   f"curvature readout is a genuine function OF THE ORBIT). NOTE (reworded after independent review, "
   f"2026-07-24): within these 3 correctly-computed conjugacy-class orbits, every holonomy value in "
   f"one orbit is an EXACT conjugate of every other (h' = g h g^-1 for some g), so this check "
   f"re-confirms an algebraic identity already guaranteed by construction (conjugate permutations "
   f"share cycle type, hence fixed-point count) -- it is a genuine, correct consistency check, but "
   f"NOT evidence of any surprising robustness beyond that guarantee; an earlier draft's wording "
   f"overstated this as testing something not already forced by the orbit definition itself",
   orbit_trace_consistent)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier finite_diagnostic for the exact finite-group/orbit computation; Dr for the
interpretation as progress toward item 25):
- CORRECTED AFTER INDEPENDENT ADVERSARIAL REVIEW, 2026-07-24 (verdict: SURVIVES WITH REQUIRED
  CORRECTIONS, applied): an earlier draft fixed vertex 0's gauge to identity (mirroring the Z2
  precedent's trick), which is valid for an ABELIAN group but silently fails for non-abelian S3 --
  it leaves a residual global-conjugation redundancy unfixed, producing a wrong "6 orbits of size
  216" result. The reviewer independently recomputed the TRUE quotient under the full, unfixed
  gauge group and found exactly 3 orbits of sizes {216,432,648} = S3's 3 conjugacy classes. This
  file now uses the full unfixed gauge group throughout (Part 3-4) and reproduces that same
  independently-derived 3-orbit result exactly (matched, not merely asserted). The earlier 6-orbit
  version is NOT kept as a separate historical file (unlike some refuted attempts elsewhere in this
  domain) because it was corrected in-place before any commit -- no version with the bug was ever
  merged or cited.
- WHAT THIS ESTABLISHES: a genuine, first-time instantiation of this repo's OWN already-Th_coqc-
  proven gauge transformation law (U'=g_j U g_i^-1, InfoGaugeLocalizationConnectionHolonomy.v,
  G0.4 -- proved for ANY group) on a real NON-ABELIAN test group (S3, order 6) on a tiny plaquette
  lattice, using the FULL unfixed gauge group (1296 elements, matching G0.4's own generality):
  (a) the gauge orbits (configuration space modulo simultaneous vertex gauge transformations) are
  constructed exactly and match S3's 3 conjugacy classes exactly (1296 raw configs -> genuine orbit
  partition into 3 classes of size 216/432/648, checked exhaustively, cross-verified against an
  independent reviewer computation); (b) a normalized orbit-indicator basis B is built and verified
  to be an honest isometry (B^T B = I) with nonnegative entries -- i.e. a genuine discrete MEASURE on
  the orbit space, which is exactly what ITEM25_26_SCOPING_LOG.md named as entirely missing piece
  (1); (c) a consistency check (adapted from, not present in, the abelian Z2 precedent this
  technique was adapted from, and reworded after review to state its true, more modest scope --
  see Part 6's own comment): this repo's own curvature readout is confirmed to be gauge-orbit-
  invariant on this
  construction, i.e. the orbit structure here is genuinely compatible with, not independent of,
  this repo's pre-existing R5-R7 connection/holonomy/curvature primitives.
- WHAT THIS DOES NOT ESTABLISH: (a) SU(3)xSU(2)xU(1) -- S3 is a small FINITE test group chosen only
  for tractability (smallest non-abelian group), not a step in representation content or a claim
  about the real SM gauge group; extending this construction to a continuous Lie group is a
  separate, much larger undertaking (finite enumeration of configs/orbits does not generalize
  automatically to an uncountable gauge group -- a Haar-measure-analogue would be needed, itself
  unbuilt). (b) any Faddeev-Popov ghost sector or orbit-VOLUME-weighted subtraction -- this file
  builds the orbit SET and a uniform counting measure on it (equal-weight per config within an
  orbit's own normalization), not the ghost-determinant device item 25 also names as missing;
  those are numerically different objects (a ghost determinant reweights orbits by their local
  stabilizer/Jacobian, which this file does not compute or attempt). (c) any one-loop fluctuation
  Hessian of an actual gauge ACTION -- this file has no action/energy functional on configs at all,
  only the bare orbit/quotient structure; item 25's requested "gauge-orbit fluctuation Hessian"
  needs a second-variation computation on top of an action this file does not define. (d) any
  connection to the Yang-Mills mass gap (item 27) -- explicitly out of scope, not attempted, not
  claimed, despite this file's technique being adapted from a source (z2_mass_gap_adversarial_test.py)
  whose OWN original subject was a mass-gap test; only its orbit-construction TECHNIQUE was reused.
  (e) items 25/26 remain FULLY OPEN after this file -- this is progress on missing piece (1) alone
  (for a finite non-abelian test group), not a closure of item 25, and item 26 (continuum limit)
  remains untouched and un-well-posed until an actual action/Hessian exists.
- Independently adversarially reviewed, 2026-07-24 -- verdict SURVIVES WITH REQUIRED CORRECTIONS,
  all applied (see the correction note at the top of this fence): the vertex-0-fixing bug was a
  real, substantive finding (not a nitpick) that would have silently double-counted orbits for any
  non-abelian test group; the reviewer's independent from-scratch reimplementation (group
  composition, group-action bijectivity over 2000 samples, holonomy-fiber orbit recomputation,
  hand-proved algebraic telescoping of the holonomy invariance) confirms every remaining claim in
  this file, and confirms zero mass-gap-adjacent language anywhere (item 27 non-goal compliance
  clean).
""")
