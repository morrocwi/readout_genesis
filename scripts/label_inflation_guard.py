#!/usr/bin/env python3
"""
[finite_diagnostic] Label-inflation guard — synthetic fixture only, NOT a claim about any
real Coq development or physics correspondence.

Flags any card that pairs a `Th_coqc` (theorem, coq-checked) tag with a CONTINUUM-PHYSICS
proper noun (a named PDE / field theory whose actual mathematical content is a continuum
object: Schrodinger equation, Navier-Stokes, Einstein field equations, ...) when the
object actually discharged is merely a FINITE / SCALAR / DISCRETE identity. That pairing
inflates a scalar arithmetic fact into the appearance of a continuum-physics theorem.

A `Th_coqc` tag on a genuinely finite/discrete object named with a finite/discrete-scope
noun (an operator-to-metric map, a finite CHSH/Heisenberg-type inequality) is legitimate
and NOT flagged — the .v object's named content matches what it actually discharges.

Modeled as a small rule-checker over (claim_tag, named_noun, object_kind) tuples.

Run: python3 scripts/label_inflation_guard.py
"""
FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

# proper nouns whose REAL mathematical content is a continuum object (PDE / manifold field
# theory) -- naming one of these on a finite/scalar object is an inflation red flag.
CONTINUUM_PHYSICS_NOUNS = {
    "Schrodinger equation",
    "Navier-Stokes equations",
    "Einstein field equations",
    "Maxwell's equations",
    "heat equation",
    "wave equation",
    "general relativity",
}

# object_kind values that indicate the .v object actually discharged is finite/scalar/discrete
FINITE_KINDS = {"scalar-identity", "finite-inequality", "discrete-map", "arithmetic-identity"}

def check_card(claim_tag, named_noun, object_kind):
    """Returns True if the card should be FLAGGED (label inflation)."""
    if claim_tag != "Th_coqc":
        return False
    if object_kind not in FINITE_KINDS:
        return False           # object genuinely IS continuum-scope; no inflation claim made
    return named_noun in CONTINUUM_PHYSICS_NOUNS

# ============================================================ PASSING control (not flagged)
passing_cards = [
    ("Th_coqc", "operator-to-metric map (Face 8)", "discrete-map"),
    ("Th_coqc", "CHSH/Heisenberg finite inequality", "finite-inequality"),
]
for tag, noun, kind in passing_cards:
    flagged = check_card(tag, noun, kind)
    check(f"PASSING control NOT flagged: '{noun}' ({kind})", not flagged, flagged)

# ============================================================ FAILING control (must flag)
failing_cards = [
    ("Th_coqc", "Schrodinger equation", "scalar-identity"),   # continuum name on a scalar fact
]
for tag, noun, kind in failing_cards:
    flagged = check_card(tag, noun, kind)
    check(f"FAILING control IS flagged: '{noun}' ({kind}) — label inflation", flagged, flagged)

# -------- extra structural checks: verify the rule keys off BOTH conditions jointly ----------
check("non-Th_coqc tag on a continuum noun + scalar kind is NOT flagged (tag gate works)",
      not check_card("Th_prose", "Schrodinger equation", "scalar-identity"))
check("Th_coqc on a continuum noun with a genuinely continuum object_kind is NOT flagged"
      " (i.e. a real continuum theorem is legitimate, not an inflation case)",
      not check_card("Th_coqc", "Schrodinger equation", "continuum-pde-solution"))

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — label-inflation guard leaves genuine finite/discrete Th_coqc cards")
print("unflagged (operator-to-metric map, CHSH/Heisenberg) and correctly flags a Th_coqc tag")
print("naming a continuum-physics equation on a mere scalar identity (Schrodinger/scalar).")
print("[finite_diagnostic] on a synthetic rule-checker fixture ONLY.")
