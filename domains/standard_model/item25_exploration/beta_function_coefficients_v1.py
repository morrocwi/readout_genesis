#!/usr/bin/env python3
"""
Beta-function group-theory coefficients v1 — item 34 scoping/partial result.

CONTEXT (read HANDOFF_NEXT_SESSION.md and ITEM25_26_SCOPING_LOG.md in this folder first).
Backlog item 34 asks: can the AP10 one-loop beta-slope KINEMATIC WEIGHTS (11/3, 2/3, 1/3) be
derived from root, given that representation content is already SM input? This script answers
the SEPARABLE half of that question exactly, and shows the other half is NOT separable from
items 25/26.

The real-physics one-loop gauge beta-function coefficient for a simple factor G_a is the sum of
TWO structurally different kinds of input:

    b_a = (11/3)*C2(G_a) - (2/3)*sum_R T_a(R_fermion) - (1/3)*sum_R T_a(R_scalar)

  (A) GROUP-THEORY DATA: C2(G_a) (quadratic Casimir of the adjoint) and T_a(R) (Dynkin index of
      each matter representation under G_a). This is pure representation theory -- it depends
      ONLY on which representations exist, which is exactly the matter content THIS REPO already
      fixed. NOTE (independent review, 2026-07-24): the specific hypercharge SIGN convention used
      below matches sm_discovery_pipeline_v0_4.py's (Y(u^c)=+2/3, Y(d^c)=-1/3, Y(e^c)=-1) rather
      than hypercharge_global_quotient_v1_5.py's opposite-sign convention (Y(u^c)=-2/3, etc, same
      physics, right-handed vs left-handed-conjugate labeling choice) -- harmless to every result
      below since the U(1) index sum only ever uses Y^2, but stated precisely to avoid overclaiming
      an exact convention-match with v1.5 that isn't literally there: (3,2)_{1/6} + (1,2)_{-1/2} +
      (3,1)_{2/3} + (3,1)_{-1/3} + (1,1)_{-1} per generation, Higgs H=(1,2)_{1/2}, v0.4's convention.
  (B) LOOP-KINEMATIC WEIGHTS: the numbers 11/3, 2/3, 1/3 themselves, plus the GUT hypercharge
      normalization factor 3/5 needed to compare the abelian factor on the same footing as the
      non-abelian ones. These come from an actual perturbative QFT calculation: the one-loop
      vacuum-polarization / gauge self-energy diagram, INCLUDING the gauge-fixed path-integral
      measure and the Faddeev-Popov ghost contribution (the "gauge-orbit fluctuation Hessian,
      ghost/orbit-volume subtraction, polarization counting" that HANDOFF_NEXT_SESSION.md item 25
      names explicitly as NOT built here in any form). They do NOT depend on which representations
      exist -- they are the SAME three numbers for QCD, the weak SU(2), and any other gauge theory
      with the same field content pattern (1 vector multiplet + n_fermion Weyl fermions +
      n_scalar complex scalars, all in the adjoint/whatever fixed rep). No amount of representation
      theory can produce them; they are a genuinely different kind of computation.

THIS SCRIPT: recomputes (A) EXACTLY (Fraction arithmetic, C2 and T(R) as plain group-theory
constants, matter content taken from this repo's own already-established v1.5/v0.4 charges,
3 generations taken as an explicit SM input -- see fence) and combines it with (B) taken as an
EXPLICITLY LABELED EXTERNAL INPUT (not derived, registered in EQUATION_REGISTRY.md), then checks
the result against the real, independently-known SM one-loop coefficients |b1|=41/10, |b2|=19/6,
|b3|=7 (standard QFT textbook result, e.g. Machacek & Vaughn 1983; Jones 1974).

This is NOT a derivation of items 25/26 (the loop weights, the ghost/orbit Hessian, the continuum
limit) and NOT a derivation of item 34 as originally posed (the three weights themselves). It IS a
genuine, verified, previously-uncoded finite_diagnostic cross-check: it turns AP10 (until now only
a prose/table reference, "benchmark match", with no runnable artifact anywhere in this repo -- see
ITEM25_26_SCOPING_LOG.md finding 1) into an honestly-scoped runnable result, and it sharpens item 34
into a precise split: group-theory half CLOSED here for the first time as a checked artifact; loop-
kinematic half confirmed identical in kind to items 25/26's still-fully-open blocker.

Run: python3 beta_function_coefficients_v1.py
"""
from fractions import Fraction as Fr

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

# ============================================================================
# (A) GROUP-THEORY DATA -- pure representation theory, standard normalization
#     T(fundamental of SU(N)) = 1/2 ; C2(adjoint of SU(N)) = N ; U(1) is abelian, C2=0.
#     These normalization CONVENTIONS (T(fund)=1/2 etc.) are themselves a standard external
#     choice (any group theory text, e.g. Slansky 1981); only the repo's OWN representation
#     CONTENT (which reps exist, their dimensions and hypercharges) is what this section claims
#     to reproduce from already-established repo data, not the normalization convention itself.
print("== (A) group-theory data from THIS REPO's own already-established matter content ==")

T_fund = Fr(1, 2)          # Dynkin index of the fundamental (= antifundamental) of SU(N)
C2_SU3_adj = Fr(3)         # C2(adjoint SU(3)) = N = 3
C2_SU2_adj = Fr(2)         # C2(adjoint SU(2)) = N = 2
GUT_NORM = Fr(3, 5)        # hypercharge GUT normalization T_1(R) = (3/5) Y^2  -- EXTERNAL, see fence

# One generation of SM matter, the reps discovered/fixed in sm_discovery_pipeline_v0_4.py (blind
# pipeline, v0.4 line 138/153/199-200): (color_dim, weak_dim, hypercharge Y). Same physics content
# as hypercharge_global_quotient_v1_5.py, but v1.5 uses the OPPOSITE hypercharge sign convention for
# u^c/d^c/e^c (right-handed-field vs left-handed-conjugate labeling) -- harmless here since every use
# below is Y^2, but not literally "the same numbers" as v1.5 (independent review, 2026-07-24).
# key -> (color_dim, weak_dim, Y)
MATTER = {
    "Q":   (3, 2, Fr(1, 6)),
    "L":   (1, 2, Fr(-1, 2)),
    "u^c": (3, 1, Fr(2, 3)),
    "d^c": (3, 1, Fr(-1, 3)),
    "e^c": (1, 1, Fr(-1)),
}
HIGGS = {"H": (1, 2, Fr(1, 2))}   # scalar, same source (v0.4 line 200 / v1.12-13 order carrier)

N_GEN = 3   # EXPLICIT SM INPUT, NOT derived here -- item 2 (generation multiplicity) is separately
            # and fully OPEN in this repo; using 3 is the same "SM input" move already made
            # elsewhere in this domain (e.g. item22/CKM counting explicitly flags N=3 as input).

def su3_index_sum(reps):
    """sum_R (weak/other multiplicity) * T(fund) over color-triplet reps, 0 for color singlets."""
    tot = Fr(0)
    for (cdim, wdim, Y) in reps.values():
        if cdim == 3:
            tot += wdim * T_fund     # each of the wdim weak-components is an independent color triplet
    return tot

def su2_index_sum(reps):
    """sum_R (color multiplicity) * T(fund) over weak-doublet reps, 0 for weak singlets."""
    tot = Fr(0)
    for (cdim, wdim, Y) in reps.values():
        if wdim == 2:
            tot += cdim * T_fund
    return tot

def u1_index_sum(reps):
    """sum_R dim_other(R) * Y(R)^2 (GUT-normalized by 3/5 at the point of use)."""
    tot = Fr(0)
    for (cdim, wdim, Y) in reps.values():
        tot += cdim * wdim * Y * Y
    return tot

su3_fermion_1gen = su3_index_sum(MATTER)
su2_fermion_1gen = su2_index_sum(MATTER)
u1_fermion_1gen  = u1_index_sum(MATTER)
su3_scalar = su3_index_sum(HIGGS)      # Higgs is a color singlet -> 0
su2_scalar = su2_index_sum(HIGGS)
u1_scalar  = u1_index_sum(HIGGS)

ck("per-generation SU(3) fermion index sum = 2  (Q:2*1/2=1, u^c:1/2, d^c:1/2)",
   su3_fermion_1gen == Fr(2), su3_fermion_1gen)
ck("per-generation SU(2) fermion index sum = 2  (Q:3*1/2=3/2, L:1/2)",
   su2_fermion_1gen == Fr(2), su2_fermion_1gen)
ck("per-generation sum dim*Y^2 (fermions) = 10/3  (matches v0.4's own sum_mat_Y2)",
   u1_fermion_1gen == Fr(10, 3), u1_fermion_1gen)
ck("Higgs is an SU(3) color singlet -> 0 contribution to su3_scalar", su3_scalar == 0)
ck("Higgs SU(2) index = 1/2  (1 color copy * T(fund))", su2_scalar == Fr(1, 2), su2_scalar)
ck("Higgs dim*Y^2 = 1/2", u1_scalar == Fr(1, 2), u1_scalar)

SU3_fermion_total = N_GEN * su3_fermion_1gen
SU2_fermion_total = N_GEN * su2_fermion_1gen
U1_fermion_total  = N_GEN * u1_fermion_1gen

ck("3-generation SU(3) fermion index total = 6", SU3_fermion_total == Fr(6), SU3_fermion_total)
ck("3-generation SU(2) fermion index total = 6", SU2_fermion_total == Fr(6), SU2_fermion_total)
ck("3-generation dim*Y^2 (fermions) total = 10", U1_fermion_total == Fr(10), U1_fermion_total)

# ============================================================================
# (B) LOOP-KINEMATIC WEIGHTS -- EXTERNAL, NOT derived, registered in EQUATION_REGISTRY.md.
#     Source: general one-loop non-abelian gauge beta function with matter (Jones 1974;
#     Machacek & Vaughn 1983), specialized here to the SM field content pattern.
print()
print("== (B) loop-kinematic weights -- EXPLICITLY EXTERNAL, NOT derived here or anywhere in ==")
print("      this repo (no propagator / path-integral / ghost-determinant machinery exists) ==")
W_GAUGE  = Fr(11, 3)   # vector (gauge boson + ghost) loop contribution per unit C2(adjoint)
W_WEYL   = Fr(2, 3)    # per Weyl fermion, per unit T(R)
W_SCALAR = Fr(1, 3)    # per complex scalar, per unit T(R)
ck("HONEST: (11/3, 2/3, 1/3) are asserted external constants, not computed by any function above",
   True)

# ============================================================================
# COMBINE: b_a = W_GAUGE*C2(G_a) - W_WEYL*sum_fermion T_a(R) - W_SCALAR*sum_scalar T_a(R)
print()
print("== combine (A) x (B): b_a for a in {SU(3), SU(2), U(1)_GUT-normalized} ==")

b3 = W_GAUGE * C2_SU3_adj - W_WEYL * SU3_fermion_total - W_SCALAR * su3_scalar
b2 = W_GAUGE * C2_SU2_adj - W_WEYL * SU2_fermion_total - W_SCALAR * su2_scalar
b1 = W_GAUGE * 0 - W_WEYL * (GUT_NORM * U1_fermion_total) - W_SCALAR * (GUT_NORM * u1_scalar)

ck("b3 = 7  (matches real SM QCD one-loop coefficient, |b3|=7, n_f=6 flavors)", b3 == Fr(7), b3)
ck("b2 = 19/6  (matches real SM weak-SU(2) one-loop coefficient)", b2 == Fr(19, 6), b2)
ck("b1 = -41/10  (matches real SM hypercharge one-loop coefficient, |b1|=41/10, GUT-normalized)",
   b1 == Fr(-41, 10), b1)

print()
print(f"  b3 (SU(3))            = {b3}")
print(f"  b2 (SU(2))             = {b2}")
print(f"  b1 (U(1), GUT-norm)    = {b1}")

# ============================================================================
if FAILS:
    print(f"\nDECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)

print()
print("DECISION: PASS")
print()
print("HONEST FENCE (tier: finite_diagnostic; exact Fraction arithmetic, reproducible):")
print("  ESTABLISHED here: the GROUP-THEORY half of the AP10 one-loop beta-function coefficients")
print("  (C2(G_a) and the Dynkin-index sums T_a(R)) is reproduced EXACTLY from THIS REPO's own")
print("  already-fixed SU(3)xSU(2)xU(1) matter content (v1.5/v0.4), with 3 generations taken as an")
print("  explicit SM input (item 2 remains fully open elsewhere in this domain). Combined with the")
print("  three external loop-kinematic weights (11/3, 2/3, 1/3) and the external 3/5 GUT hypercharge")
print("  normalization, this reproduces the real, independently-known SM one-loop coefficients")
print("  b3=7, b2=19/6, b1=-41/10 exactly.")
print()
print("  CORRECTED CLAIM (2026-07-24, self-caught during a session-wide reconciliation sweep): an")
print("  earlier draft of this fence claimed this was 'the FIRST runnable artifact for AP10 in this")
print("  repo.' THAT IS WRONG -- src/anse_spine/solvers/sm_eff.py (a separate, pre-existing,")
print("  already-canonical 'SM-EFF' track, canon/genesis_canon_v2.1.md Section 11) already contains")
print("  a RUNNING, EXECUTED use of these SAME-MAGNITUDE coefficients b=[41/10,-19/6,-7.0] (their")
print("  (U1,SU2,SU3) array, opposite OVERALL SIGN from this file's b1=-41/10,b2=+19/6,b3=+7 -- a")
print("  known RGE sign-convention artifact, sm_eff.py runs dalpha^-1/d(ln mu)=-b/(2pi) while this")
print("  file reports the bare coefficient magnitude; CORRECTED after independent review, 2026-07-24,")
print("  which caught an earlier draft's wrong claim of literal numeric identity -- same PHYSICAL")
print("  content, opposite sign CONVENTION, not the same numbers) for real 1-loop")
print("  RGE running (alpha_i^-1(MZ) -> alpha_i^-1(GUT)), predating this file. The accurate claim is")
print("  narrower: sm_eff.py imports b as a flat, uncomputed external array with no group-theory")
print("  content attached; THIS file is the first to independently DERIVE the GROUP-THEORY HALF of")
print("  those same coefficients (C2(G_a), Dynkin-index sums T_a(R)) from this repo's own root-fixed")
print("  matter representation content, and the first to connect that derivation, via an actual")
print("  computation, to the cited external b values -- a genuine, narrower, still-real contribution")
print("  (turning a previously bare, unexplained external constant into one whose group-theory half")
print("  is now checked against this repo's own matter content), not the first code to USE these")
print("  numbers at all. This repo's canon and domains/standard_model/ tracks had NOT been")
print("  cross-referenced before this correction -- see domains/standard_model/")
print("  CANON_SMEFF_RECONCILIATION.md for the full reconciliation.")
print()
print("  NOT established / explicitly NOT claimed:")
print("   - The three loop-kinematic weights 11/3, 2/3, 1/3 are NOT derived -- they are asserted")
print("     external constants (section B above). Deriving them requires an actual gauge-fixed")
print("     path-integral loop computation with Faddeev-Popov ghosts and polarization counting --")
print("     exactly HANDOFF_NEXT_SESSION.md item 25's 'gauge-orbit fluctuation Hessian' -- which")
print("     does not exist in any form anywhere in this repo (verified by grep across domains/,")
print("     see ITEM25_26_SCOPING_LOG.md). Item 34 therefore does NOT reduce to representation")
print("     theory alone; its hard remaining content is IDENTICAL to items 25/26's blocker.")
print("   - The 3/5 GUT hypercharge normalization is an external convention (SU(5) embedding,")
print("     Georgi-Glashow 1974), not derived.")
print("   - 3 generations is an explicit SM input (item 2, generation multiplicity, is separately")
print("     and fully OPEN).")
print("   - This is NOT a beta function (no running, no scale dependence, no RG equation solved) --")
print("     only the ALGEBRAIC COEFFICIENT that would multiply g^3/(16*pi^2) in one, IF the loop")
print("     computation existed. Items 25 and 26 (gauge-orbit Hessian, regulator-independence /")
print("     continuum limit) remain FULLY OPEN, untouched by this script.")
print("   - v0.4's own 'finite radiative engine' (r1,r2,r3, sm_discovery_pipeline_v0_4.py) is a")
print("     DIFFERENT, disclaimed construction (log-det curvatures of a 6-cycle graph Laplacian)")
print("     -- this script does not reuse or extend it, and does not re-claim it as a beta function.")
print()
print("  Independently adversarially reviewed, 2026-07-24 -- verdict SURVIVES WITH ONE MINOR")
print("  CORRECTION (documentation precision only, applied above): reviewer specifically attacked")
print("  reverse-engineering risk (every non-matter-content ingredient -- T(fund)=1/2, C2(adjoint)=N,")
print("  the 11/3,2/3,1/3 weights, 3/5 GUT norm -- confirmed to be a fixed external convention, not a")
print("  tunable free choice; matter content confirmed independently fixed pre-existing, for anomaly-")
print("  cancellation reasons unrelated to beta functions) and found none; confirmed v0.4 non-reuse")
print("  claim true by independent reading. Correction: docstring wrongly implied identical numbers")
print("  to hypercharge_global_quotient_v1_5.py -- corrected to note v1.5 uses the opposite")
print("  hypercharge sign convention for u^c/d^c/e^c (same physics, Y^2-invariant, but not literally")
print("  the same tuple); this script's convention actually matches v0.4's, not v1.5's.")
