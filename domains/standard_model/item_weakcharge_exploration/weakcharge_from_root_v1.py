#!/usr/bin/env python3
"""
"Weak charge" (T_3, weak isospin) FROM ROOT -- 2026-07-24. Prerequisite work for interpreting
mixing angles: `hypercharge_global_quotient_v1_5.py` currently uses T_3=+-1/2 as a bare comment
("Q doublet: T_3=+-1/2, Y=1/6") -- POSITED, never derived from this project's own primitives.
This file builds the SAME kind of ground-up argument SM_INFORMATION_PHILOSOPHY_MASTER.md's
Section 3 already built for color (dim V>=3 => SU(3)), but INDEPENDENTLY, for the binary
doublet carrier -- NOT by reusing color's specific numeral or formula (that would be Cross-Role
Readout Contamination, forbidden per HANDOFF_NEXT_SESSION.md Section 0.-1 / ITEM1_EXPLORATION_LOG.md).

ROOT PRIMITIVES REUSED (the general TOOLS, not any specific readout/number):
  Section 1.1 -- retained difference: "what has no effect on any readout should not be counted as
    a retained difference." Two carrier basis states are only genuinely DISTINGUISHABLE if some
    generator's readout actually separates them.
  Section 1.3 -- retained metric: <x,y>_G = x^dagger G y, G>0 (root-native, general-purpose tool).
  Section 3.2's METHOD (not its number): "retain metric: U^dagger G U = G, basis G=I => U in U(n)."
    Applied HERE to n=2 (the doublet carrier W~=C^2), independently, from scratch.

CONSTRUCTION:
  1. Carrier W ~= C^2 -- the "binary distinction" (order-parameter doublet) already named
     structurally in H1 (docs/OPEN_PROBLEM_HYPOTHESES.md, Dr/Open) and used as an unexplained
     input in v1.5. This file does not re-derive WHY the carrier is 2-dimensional (that is H1's
     own still-open closing condition -- "derive SU(2) as the automorphism group of the minimal
     cell's retained-state space" -- NOT attempted here); it takes the doublet's existence as
     already-named context and asks the NARROWER, answerable question: given a 2-dim carrier,
     what does "weak charge" have to look like?
  2. Retained metric G_W>0 on W; basis G_W=I (WLOG, same normalization freedom Section 3.2 uses).
  3. Automorphisms preserving the metric: U^dagger U = I => U(2).
  4. "Weak charge" is DEFINED as the eigenvalue readout of a Cartan generator T (Hermitian,
     diagonal in the metric-preserving basis) whose readout must ACTUALLY DISTINGUISH the two
     basis states (Section 1.1's retained-difference principle: a generator with equal
     eigenvalues on both basis vectors reads out NO difference between them, so cannot be what
     "charge" means -- charge is a retained distinction by definition, Section 1.1).
  5. T lies in su(2) (the traceless part of u(2) -- the same "cut common trace" move Section 3.4
     uses for su(3), i.e. remove the U(1) direction v1.5 already separately assigns as
     hypercharge, so T carries genuinely NEW information, not double-counted with Y).
  6. NOT-A-DISCOVERY, disclosed as such (corrected after independent adversarial review,
     2026-07-24): "trace(T)=0 for diag(t,-t) means the eigenvalues sum to zero" is true by the
     DEFINITION of "diagonal" and "trace" -- t+(-t)=0 cannot fail, it is arithmetic, not a
     derived constraint. The actually non-trivial, standard representation-theory fact this
     stands in for is: ANY legitimate su(2) Cartan generator (any traceless 2x2 Hermitian
     matrix, not merely one already written in diagonal form) is UNITARILY CONJUGATE to a
     traceless-diagonal matrix -- diagonalizability of Hermitian operators plus the trace being
     conjugation-invariant. THAT (standard, not reproved here) fact is what licenses "weak
     charge is exactly two equal-and-opposite values" as a basis-independent statement, not the
     trivial arithmetic of one already-diagonal example.
  7. NOT forced (flagged, not smuggled): the MAGNITUDE |t| is a normalization/unit choice for
     what "one unit of weak charge" means, structurally the same kind of choice as ℏ or c
     (BORROWED-SCALE per docs/root/BORROWED_VS_DERIVED_LEDGER.md row 14/18) -- NOT root-derived.
     The conventional choice t=1/2 is NOT forced by anything built here.
  8. ALSO NOT forced, disclosed plainly (added after review): the identification "weak charge :=
     the Cartan-generator eigenvalue" is itself a NAMING CHOICE, not something forced by anything
     beyond "the doublet needs SOME U(2)-generator label to be called a charge by." Nothing built
     here shows this particular algebraic object is what PHYSICAL weak charge measures, as
     opposed to merely a same-shaped candidate label -- exactly analogous to how "color charge :=
     an SU(3) Casimir label" is also a naming choice layered on top of the SU(3) derivation, not
     an additional forced fact.

Run: python3 weakcharge_from_root_v1.py
"""
from fractions import Fraction as Fr

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 1. metric-preserving automorphisms of a 2-dim carrier (Section 3.2's METHOD, independent) ==")
print("   G_W = I (WLOG), U^dagger U = I  =>  U(2)  [same general tool as Section 3.2, dim=2 not 3]")

print("\n== 2. traceless (su(2)) generator: exact algebraic fact, not a postulate ==")
def is_traceless_diag(t1, t2):
    return t1 + t2 == 0

for t in (Fr(1, 2), Fr(3, 7), Fr(-1, 4), Fr(1)):
    t1, t2 = t, -t
    ck(f"t={t}: diag(t,-t) has trace 0 (definition of su(2)'s Cartan generator)",
       is_traceless_diag(t1, t2))
    ck(f"t={t}: the two doublet components carry EQUAL-MAGNITUDE, OPPOSITE-SIGN weak charge",
       t1 == -t2 and t1 != t2 if t != 0 else t1 == t2)

print("\n== 3. TERMINOLOGICAL RESTATEMENT ONLY, not an argument (flagged after independent review) ==")
print("   An earlier draft framed 't!=0 distinguishes the two basis states' as a use of Section")
print("   1.1's retained-difference principle. Independent adversarial review correctly found this")
print("   CIRCULAR: it defines distinguishability as t!=0, then verifies t!=0 gives")
print("   distinguishability -- no independent content, just vocabulary. Kept here, demoted, only")
print("   to record that t=0 is excluded from being called \"weak charge\" at all (a generator that")
print("   reads out nothing is not a charge by any definition, trivially) -- NOT cited as a")
print("   nontrivial application of Section 1.1.")

print("\n== 4. what is FORCED vs what is a NORMALIZATION CHOICE (not smuggled) ==")
print("   FORCED (exact, from trace(T)=0): T_3(component_1) = -T_3(component_2) for ANY t != 0.")
print("   NOT FORCED: the magnitude |t| itself. Nothing built here selects t=1/2 over t=1, t=3, etc.")
print("   -- same epistemic status as ℏ, c (BORROWED-SCALE, docs/root/BORROWED_VS_DERIVED_LEDGER.md")
print("   rows 14/18): a unit-defining convention, not a root-derived value.")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier Dr -- structural argument, not yet Coq-machine-checked; corrected after
independent adversarial review, 2026-07-24, verdict SURVIVES_WITH_CORRECTION):
- WHAT THIS ESTABLISHES: "weak charge" (T_3), read in this framework's own vocabulary, is a NAMED
  candidate (see point (d) below -- naming, not forcing) for the eigenvalue-readout of the
  traceless (su(2)) Cartan generator on a 2-dim retained-metric carrier. The genuine, non-trivial
  content is the STANDARD representation-theory fact (cited, not re-proved here) that any su(2)
  Cartan generator is conjugate to traceless-diagonal form, which is basis-independent; the
  same-line arithmetic "diag(t,-t) sums to zero" is NOT itself a discovery (t+(-t)=0 by
  construction) -- an earlier draft oversold this as "FORCED, exact," corrected here.
- WHAT THIS DOES NOT ESTABLISH: (a) WHY the carrier is 2-dimensional in the first place -- that is
  H1's own named, still-open closing condition (docs/OPEN_PROBLEM_HYPOTHESES.md: "derive SU(2) ...
  as the automorphism group of the minimal cell's retained-state space; show no other simple
  factors survive. [Dr]/[Open]"), NOT attempted here. (b) the MAGNITUDE |t| -- t=1/2 is a
  normalization convention, structurally identical to choosing units for ℏ or c, not root-derived.
  (c) any connection to mixing angles yet -- this is prerequisite groundwork only. (d) that "Cartan
  eigenvalue" is what physical weak charge MUST mean, as opposed to a same-shaped candidate LABEL
  -- this is a naming choice layered on the U(2)/su(2) derivation, exactly analogous to "color
  charge := an SU(3) Casimir label," not an additional forced fact; flagged, not smuggled, per
  review point 5.
- Part 3 above is DEMOTED to a terminological note, not an argument -- an earlier draft's
  "retained-difference" framing of t!=0 was found circular by independent review (defines
  distinguishability as t!=0, then verifies t!=0 gives distinguishability) and is corrected here.
- Method reused from Section 3.2 (metric-preserving automorphism => U(n)) and Section 3.4 (cut the
  common trace) is the SAME GENERAL TOOL applied fresh to a genuinely different object (dim-2
  carrier, not dim-3 color carrier) -- confirmed clean of CRRC by independent review (no color-
  specific number or formula anywhere in this file).
- Reviewed: verdict SURVIVES_WITH_CORRECTION, all corrections applied above before this file is
  treated as more than a first-pass draft.
""")
