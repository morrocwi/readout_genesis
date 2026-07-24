#!/usr/bin/env python3
"""
Mixing angle, translated into this project's own vocabulary -- 2026-07-24. Prerequisite: weak
charge is now root-defined (item_weakcharge_exploration/weakcharge_from_root_v1.py, T_3 = the
eigenvalue-readout of a traceless su(2) Cartan generator T) and mass is ALREADY root-defined
(docs/GENESIS_DEEP.md Tick 2 / engine/lexicon.py: m = hbar/(2 tau_c c^2), Th_coqc -- mass is a
READOUT of causal-memory time tau_c, not fundamental).

DEFINITION (Dr tier, this framework's own vocabulary, not physics-textbook language): a "mixing
angle" is the basis-mismatch angle between the eigenbasis of TWO DIFFERENT readout operators on
the SAME retained carrier -- the su(2) Cartan generator T (whose eigenbasis is what "weak charge"
diagonalizes) and the tau_c operator (whose eigenbasis is what "mass" diagonalizes). If [T, tau_c]
= 0 these coincide (no mixing); mixing angle theta_ij measures how far generations i,j's
tau_c-eigenvectors are rotated relative to T's own eigenbasis. This is the SAME standard fact
mainstream physics calls "mass basis != weak basis" -- translated here into readouts this project
already defines from root (T_3, tau_c), not asserted as new physics.

DIAGNOSTIC (why theta_12 >> theta_23, theta_13 -- but NOT why theta_23 >> theta_13): standard
nearly-degenerate perturbation theory gives mixing magnitude ~ |off-diagonal coupling| /
|tau_c_i - tau_c_j| (equivalently, mass gap |m_i - m_j|) -- SMALL gap => LARGE mixing (near-
degenerate directions rotate freely), LARGE gap => SMALL mixing (well-separated directions barely
rotate). This is a BORROWED, standard degenerate-perturbation-theory shape (cited, not root-
derived) -- what makes it expressible in THIS project's vocabulary is that tau_c (hence the mass
gap) is now root-native (Th_coqc), where before this session's weak-charge work there was no
root-native T operator to speak of a "basis mismatch" against at all.

Run: python3 mixing_angle_as_basis_mismatch_v1.py
"""
import math

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 1. real PDG down-type masses (same registry item1/item2 already use) ==")
m_d, m_s, m_b = 0.00467, 0.0934, 4.18  # GeV, fit_calibrated_registry.py

gap_12 = m_s - m_d
gap_13 = m_b - m_d
gap_23 = m_b - m_s
print(f"   gap(1,2) = m_s-m_d = {gap_12:.5f} GeV")
print(f"   gap(1,3) = m_b-m_d = {gap_13:.5f} GeV")
print(f"   gap(2,3) = m_b-m_s = {gap_23:.5f} GeV")

print("\n== 2. naive predicted mixing magnitude ~ 1/gap (off-diagonal coupling treated as ~equal")
print("   across pairs -- an explicitly UNTESTED simplifying assumption, flagged below) ==")
inv_12, inv_13, inv_23 = 1 / gap_12, 1 / gap_13, 1 / gap_23
print(f"   1/gap(1,2) = {inv_12:.4f}   1/gap(1,3) = {inv_13:.4f}   1/gap(2,3) = {inv_23:.4f}")

print("\n== 3. compare ORDERING to real PDG CKM angle magnitudes ==")
theta12_real, theta23_real, theta13_real = 12.96, 2.38, 0.21  # degrees, PDG-consistent central values
print(f"   real: theta12={theta12_real} deg, theta23={theta23_real} deg, theta13={theta13_real} deg")
ck("QUALITATIVE ordering theta12 >> theta23 AND theta12 >> theta13 is correctly predicted",
   inv_12 > 10 * inv_23 and inv_12 > 10 * inv_13)
ck("FINER ordering theta23 > theta13 (by ~10x in reality) is NOT correctly predicted -- naive",
   not (inv_23 > 5 * inv_13), f"inv_23/inv_13 = {inv_23/inv_13:.3f} (predicts near-equal, not ~10x)")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS (both the qualitative success AND the finer-structure failure are")
    print("the CORRECT, expected outcome of this honest diagnostic -- see fence).")

print("""
HONEST FENCE (tier Dr for the definition + interpretation; finite_diagnostic for the numeric
gap-ratio check itself, which is a reproducible finite computation, no extrapolation):
- WHAT THIS ESTABLISHES: (a) a root-vocabulary DEFINITION of "mixing angle" as a basis-mismatch
  between the T (weak charge) and tau_c (mass) eigenbases -- newly expressible because weak
  charge now has a root-native definition (this session's weakcharge_from_root_v1.py); before
  that, there was no root-native T to speak of a mismatch against. (b) a real, checked numeric
  fact: the mass-gap-based diagnostic CORRECTLY predicts the single largest qualitative feature
  of the real CKM matrix (theta_12 is far larger than theta_13 or theta_23), because generations
  1 and 2 are close in tau_c/mass while generation 3 is far separated from both.
- WHAT THIS DOES NOT ESTABLISH, disclosed plainly per the founder's standing "verify before
  claim" discipline: (a) the FINER distinction theta_23 > theta_13 by roughly 10x is NOT
  explained by this simple 1/gap picture -- the naive prediction gives inv_23/inv_13 close to 1
  (near-equal), not ~10, so a real, disclosed gap in the account remains; the "off-diagonal
  coupling is ~equal across pairs" assumption used to get a clean 1/gap prediction is an
  explicitly UNTESTED simplification, not derived from anything closed in this repo -- in the
  real Standard Model this coupling is itself set by the (still fully [Open] in this repo's own
  terms) Yukawa texture, item 21. (b) the mixing-magnitude-vs-gap SHAPE itself (perturbation
  theory ~ coupling/gap) is a BORROWED, standard result, not root-derived -- it is not built from
  this project's own primitives (tape order, cyclic closure, Aut(F,O), retained metric), it is
  imported honestly, same status as the Gatto-Sartori-Tonin formula item 22's other work already
  uses. (c) does not derive, fit, or predict any specific mixing angle VALUE -- item 22's actual
  value-level work (theta_12 via GST, theta_13/theta_23 Open) is unaffected by this file; this is
  purely an INTERPRETIVE layer explaining the qualitative shape of that earlier result.
- This is prerequisite/interpretive groundwork, requested explicitly by the founder as a
  follow-up to the weak-charge root definition, before any further value-level mixing-angle work.
""")
