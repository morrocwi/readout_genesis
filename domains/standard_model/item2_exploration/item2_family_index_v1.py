#!/usr/bin/env python3
"""
Item 2 (generation multiplicity), Attempt 1 — formalize the family-index slot, then test
whether GAUGE anomaly-consistency (the one thing the intertwiner/anomaly work in this domain
already closes) can bound its size N. Independent of SM_INFORMATION_PHILOSOPHY_MASTER.md
§2.2's cyclic-tape-closure argument (CRRC-forbidden here per HANDOFF_NEXT_SESSION.md §0.-1) —
this attempt never touches k, cyclic order, or antisymmetric swap at all.

SHAPE of the family-index slot (the actual construction, minimal and explicit): per
item2_exploration/ITEM2_EXPLORATION_LOG.md, the currently-closed matter search
(blind_matter_search_v1_6.py) finds ONE copy of the gauge representation content V_R (the
(Q,u^c,d^c,L,e^c) skeleton). A "generation" is then, by definition, an element of a further
tensor factor: total matter space = V_R ⊗ ℂ^N, where every gauge automorphism h∈𝒜
(G0.1-G0.5, closed Th_coqc) acts ONLY on V_R and as the IDENTITY on ℂ^N — i.e. N labels
copies that gauge transformations never rotate into each other (exactly the real-world fact
that a top quark cannot be gauge-rotated into a charm quark). This is the minimal formal
statement of "what a generation index even IS" in this framework's own vocabulary; it is not
yet a derivation of any value of N.

QUESTION TESTED: does gauge-anomaly-freedom (local mixed anomalies + the global Witten SU(2)
anomaly), the one consistency condition this domain has already closed for ONE copy
(hypercharge_global_quotient_v1_5.py), constrain N at all?

Reuses v1.5's own closed hypercharge values (Q,u^c,d^c,L,e^c) = y/6 = (1,-4,2,-3,6)/6 and its
closed anomaly formulas (A_grav, A_111, Witten doublet-parity) EXACTLY as v1.5 defines them —
no new physics input, only linearity in the family-copy count is tested.

Run: python3 item2_family_index_v1.py
"""
from fractions import Fraction as Fr

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

# ---- v1.5's own closed one-generation hypercharges (reused verbatim, not re-derived) ----
q, u, d, l, e = Fr(1), Fr(-4), Fr(2), Fr(-3), Fr(6)   # y = 6Y, from hypercharge_global_quotient_v1_5.py §3
n_doublets_1gen = 3 + 1   # Q has 3 color copies, L has 1 (v1.5 §5)

print("== 1. per-generation anomalies are exactly zero (v1.5's own closed result, reused) ==")
A_grav_1 = 6*q + 3*u + 3*d + 2*l + e
A_111_1  = 6*q**3 + 3*u**3 + 3*d**3 + 2*l**3 + e**3
ck("A_grav(1 gen) = 0", A_grav_1 == 0, A_grav_1)
ck("A_111(1 gen) = 0", A_111_1 == 0, A_111_1)
ck("N_doublet(1 gen) = 4 ≡ 0 (mod 2)  [Witten SU(2) global anomaly]", n_doublets_1gen % 2 == 0)

print("== 2. N identical copies (family index ℂ^N, trivial under gauge automorphisms 𝒜) ==")
print("   total anomaly is LINEAR in the copy count (each copy contributes independently,")
print("   since 𝒜 acts block-diagonally and identically on every copy — no cross-copy term")
print("   appears anywhere in A_grav/A_111/Witten's own defining sums):")
for N in range(0, 8):
    A_grav_N = N * A_grav_1
    A_111_N  = N * A_111_1
    doublets_N = N * n_doublets_1gen
    ck(f"N={N}: A_grav(N)=N·A_grav(1)=0", A_grav_N == 0, A_grav_N)
    ck(f"N={N}: A_111(N)=N·A_111(1)=0", A_111_N == 0, A_111_N)
    ck(f"N={N}: N_doublet(N)={doublets_N} ≡ 0 (mod 2)", doublets_N % 2 == 0, doublets_N)

print("== 3. Scope-narrowing result (not new physics — see honest fence below): local + global")
print("   gauge anomaly cancellation is IDENTICALLY SATISFIED for every N ≥ 0, because it is")
print("   zero already at N=1 and the total is N times that zero. This is an algebraic fact")
print("   (linearity, verified above on THIS domain's own closed v1.5 numbers), not a fitted")
print("   coincidence — it holds for ANY N. It rules out one natural-looking candidate")
print("   direction for item 2 (\"maybe anomaly-freedom itself forces N=3\") before further")
print("   work is spent on it in-repo.")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (corrected after independent adversarial review, 2026-07-24 — verdict SURVIVES
WITH CORRECTION): this attempt (a) formalizes the family-index slot ℂ^N as "what gauge
automorphisms 𝒜 act trivially on". This is NOT merely "unverified in Coq" — the review found
it borders on the exact practice SM_INFORMATION_PHILOSOPHY_MASTER.md's own opening rule
forbids ("physical names must come after, never fed as premise", lines 22-23): the physical
motivation for this shape ("gauge transforms can't rotate top into charm") is IMPORTED from
already-known real-world Standard-Model phenomenology, not built from anything G0.1-G0.5
actually closes (those close composition/inverse/localization/holonomy for a SINGLE frame;
nothing in them concerns multi-copy carriers at all). Stated plainly: the definition used here
is a physics-motivated ansatz, not a derived structure — treat it as a working hypothesis to be
independently earned later, not as an established object. (b) Given that ansatz, gauge-anomaly-
freedom (the one already-closed per-generation consistency condition) is verified N-blind — a
real, checked algebraic fact on this domain's own numbers, but ALSO not new physics: that
anomaly-freedom is generation-blind is well-known/textbook in real physics; the contribution
here is narrow (rules out one candidate direction using this framework's own closed numbers),
not a discovery. (c) does NOT propose, derive, or hint at any value of N, including 3. OPEN,
unchanged: what OTHER closure condition (if any) could bound N, AND whether the ℂ^N ansatz
itself can ever be earned from something already closed rather than imported. One un-built
candidate direction, named but not attempted (adequately quarantined per review): index-
theorem-style constructions (a discrete analogue of "net chirality count = a topological
invariant of the closure map"), by analogy with continuum QFT's index results — EXPLICITLY
flagged as an analogy, not a construction, and per CRRC must earn its own from-scratch
admissibility square before it can be attempted, not asserted by resemblance.
""")
