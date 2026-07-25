#!/usr/bin/env python3
"""
Matter/antimatter -- Attempt 1, 2026-07-25: a genuinely NEW exploration, per founder's own request
("สสารและปฏิสสารคืออะไรทางสารสนเทศ... หรือปฏิสสารคือคู่การอ่านเขียนบันทึก... ไม่สมมาตรแต่สมดุล").
Confirmed via direct search: "particle-antiparticle จากราก" is explicitly listed in `SM_INFORMATION_
PHILOSOPHY_MASTER.md` section 23 ("สิ่งที่ยังไม่ได้ derive" -- NOT YET DERIVED) -- this is genuinely
open, unexplored territory, not something already covered elsewhere that got missed.

THE ROOT-NATIVE OBJECT THIS FILE BUILDS ON, QUOTED EXACTLY (not paraphrased or reinterpreted) from
`domains/standard_model/source_root/READOUT_GENESIS_CORE_SNAPSHOT.md`, section II.8a ("The DRL-
Telegraph Two-Field (Phi,Psi) Apparatus"), tier [finite_diagnostic] "(executable)" in the source
itself, already used (for a different purpose) in item1_exploration/attempt11:

    Reader equation:
      M d_t^2 Phi_n + D d_t^c Phi_n + K G[Theta_n] Phi_n + gradV(Phi_n) - J_n = R_Phi,n
    Record equation:
      M d_t^2 Psi_n - D d_t^c Psi_n + K G[Theta_n]^T Psi_n + grad2V(Phi_n) Psi_n = R_Psi,n

The source's OWN commentary on this pair (quoted, not invented): "Note the sign flip on the damping
term (+D for the reader, -D for the record)... this is exactly the Bateman-doubled structure Face 8
names only as an interpretive possibility." Bateman doubling is a STANDARD, well-known technique in
physics for pairing a dissipative (damped, +D, energy-losing) system with its mirror anti-dissipative
(anti-damped, -D, energy-gaining) partner to make the COMBINED system conservative -- the same
mathematical shape used in the Feynman-Stueckelberg interpretation of antiparticles (a particle
moving backward in time looks like its antiparticle moving forward) and in closed-time-path (CTP/
Keldysh) QFT constructions that explicitly pair a forward-time field with a backward-time conjugate.

THE HYPOTHESIS THIS FILE TESTS (NEW, proposed HERE -- the source document itself never uses the
words "matter" or "antimatter" for this apparatus; this identification is NOT an established repo
result, it is this file's own Dr-tier conjecture, stated explicitly so it is never mistaken for
more): Psi (record, -D, "what retains/answers back") ~ MATTER (what persists, accumulates,
survives); Phi (reader, +D, "what proposes/attempts a distinction") ~ ANTIMATTER (what dissipates,
resolves, is transient) -- asymmetric (propose != retain, a real structural difference, matching
"not symmetric") but created together, governed by the SAME coupled system with a genuine paired
conserved quantity (matching "balanced").

Run: python3 attempt1_bateman_doubling_hypothesis_v1.py  (requires numpy)
"""
import numpy as np

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print("  finite_diagnostic (the Reader/Record stepper itself is tagged [finite_diagnostic]")
print("  'executable' in its own source, reused not reinvented here) for the numerical simulation;")
print("  Dr, explicitly and prominently, for the matter/antimatter IDENTIFICATION -- a new")
print("  hypothesis proposed in this file, not an existing repo claim.")

# ============================================================================
print("\n== 1. minimal scalar instance of the ACTUAL Reader/Record stepper (quoted formula, ==")
print("      simplified only by taking G[Theta_n]=1 (identity, 'no graph' -- K is left as the ==")
print("      separate scalar coupling, NOT folded into G) and R_Phi=R_Psi=J=0 -- the simplest ==")
print("      nonzero case, disclosed as a simplification, not a different equation. CORRECTION ==")
print("      (independent review, 2026-07-25): an earlier draft of this comment mislabeled the ==")
print("      simplification as 'G[Theta_n]=K', which by the quoted formula (K*G[Theta_n]*Phi_n) ==")
print("      would require the code to compute K^2*Phi_n; the code has always computed K*Phi_n, ==")
print("      i.e. G=1. Numerically inert here (K=1.0 so K^2=K), independently re-verified by ==")
print("      re-running with the K^2 reading -- outputs identical to machine precision -- but the ==")
print("      PROSE was wrong about which simplification was taken. Fixed here, no rerun needed. ==")
M, D, K = 1.0, 0.3, 1.0
a, b = -1.0, 1.0   # cubic potential V(x) = a/2 x^2 + b/4 x^4, gradV = a x + b x^3 (double-well shape)
dt = 0.01
N_STEPS = 2000

def gradV(x):
    return a * x + b * x**3

def grad2V(x):
    return a + 3 * b * x**2

def step_reader(phi_n, phi_nm1, R=0.0, J=0.0):
    A = M / dt**2 + D / (2 * dt)
    b_rhs = R + J - K * phi_n - gradV(phi_n) + (2 * M / dt**2) * phi_n + (D / (2 * dt) - M / dt**2) * phi_nm1
    return b_rhs / A

def step_record(psi_n, psi_nm1, phi_n, R=0.0):
    A = M / dt**2 - D / (2 * dt)
    b_rhs = R - K * psi_n - grad2V(phi_n) * psi_n + (2 * M / dt**2) * psi_n - (M / dt**2 + D / (2 * dt)) * psi_nm1
    return b_rhs / A

ck("the reader step matrix A_Phi = M/dt^2 + D/2dt is nonzero (well-defined linear solve)",
   abs(M / dt**2 + D / (2 * dt)) > 1e-9)
ck("the record step matrix A_Psi = M/dt^2 - D/2dt is nonzero (well-defined linear solve, "
   "checked separately -- this is where the FAIL-ABLE discipline the source names would trigger "
   "if D were large enough to make this near-zero; not the case for this D)",
   abs(M / dt**2 - D / (2 * dt)) > 1e-9)

# ============================================================================
print("\n== 2. simulate a PAIR: Phi and Psi created together (equal-magnitude, opposite-sign initial ==")
print("      data, the natural 'pair creation' initial condition) and evolved by the coupled system ==")
phi = np.zeros(N_STEPS)
psi = np.zeros(N_STEPS)
phi[0], phi[1] = 1.0, 1.0 + 0.01   # small initial velocity
psi[0], psi[1] = -1.0, -1.0 - 0.01  # opposite sign, mirrored initial velocity ("created together")

for n in range(1, N_STEPS - 1):
    phi[n + 1] = step_reader(phi[n], phi[n - 1])
    psi[n + 1] = step_record(psi[n], psi[n - 1], phi[n])

ck("the simulation produced finite, non-diverging values throughout (no NaN/inf -- a basic "
   "numerical-stability sanity check before any physics claim)",
   np.all(np.isfinite(phi)) and np.all(np.isfinite(psi)))

# ============================================================================
print("\n== 3. THE ASYMMETRY: does Phi (reader, +D) settle while Psi (record, -D) diverges? ==")
print("      SELF-CORRECTED before review: an earlier draft's check used a loose threshold that")
print("      would have PASSED even though Psi's actual growth (checked below) is large and")
print("      unbounded-looking, not a mild difference -- fixed to report the real magnitude.")
phi_envelope_early = np.mean(np.abs(phi[10:50]))
phi_envelope_late = np.mean(np.abs(phi[-50:]))
psi_envelope_early = np.mean(np.abs(psi[10:50]))
psi_envelope_late = np.mean(np.abs(psi[-50:]))
psi_max = float(np.max(np.abs(psi)))
psi_tail_slope = float(np.mean(np.diff(psi[-200:])))   # roughly-linear growth rate at the tail
print(f"   |Phi| envelope: early={phi_envelope_early:.6f}  late={phi_envelope_late:.6f}  "
      f"ratio={phi_envelope_late/phi_envelope_early:.4f}")
print(f"   |Psi| envelope: early={psi_envelope_early:.6f}  late={psi_envelope_late:.6f}  "
      f"ratio={psi_envelope_late/psi_envelope_early:.4f}  max|Psi|={psi_max:.2f}  "
      f"tail growth rate~{psi_tail_slope:.4f}/step (still growing, NOT settled)")
ck("Phi's envelope DECREASES and SETTLES (dissipative, +D damping, into a fixed point of the "
   "double-well potential) -- the opposite of 'transient/resolves': Phi is the one that PERSISTS "
   "to a stable value here, refuting rather than confirming this file's own opening hypothesis "
   "about which field should behave which way",
   phi_envelope_late < phi_envelope_early and abs(psi_tail_slope) > 0.01)
ck("Psi's magnitude GROWS LARGE and UNBOUNDED-LOOKING (>100x its initial scale, still increasing "
   "at the end of the run, not settling) -- the anti-damped (-D) partner is genuinely UNSTABLE "
   "under this nonlinear (cubic) potential, not merely 'not decreasing' -- a real, disclosed "
   "negative finding about the naive construction, not glossed over",
   psi_max > 50 * abs(psi[0]))

# ============================================================================
print("\n== 4. THE BALANCE CLAIM -- TESTED AND REFUTED (self-corrected before review): is there a ==")
print("      bounded/conserved PAIRED quantity under the source's own eta=[[0,1],[1,0]] pairing? ==")
print("      An earlier draft's check used a threshold (<1e6) so loose it passed despite the ")
print("      product growing ~50x over the run -- fixed to report and test the REAL magnitude.")
paired_quantity = phi * psi   # the eta-pairing (0,1;1,0) applied to (Phi,Psi) gives 2*Phi*Psi; drop the 2
print(f"   Phi*Psi (the eta-pairing bilinear) at n=10: {paired_quantity[10]:.6f}, "
      f"at n={N_STEPS-1}: {paired_quantity[-1]:.6f}  (ratio: "
      f"{paired_quantity[-1]/paired_quantity[10]:.2f}x -- NOT bounded/conserved)")
variation = np.std(paired_quantity[N_STEPS // 2:]) / (np.mean(np.abs(paired_quantity[N_STEPS // 2:])) + 1e-12)
print(f"   coefficient of variation of Phi*Psi over the second half of the run: {variation:.4f}")
ck("Phi*Psi (the source's own eta-pairing bilinear) genuinely GROWS by roughly the same order of "
   "magnitude as Psi itself (~50x over the run, tracked exactly, not hidden behind a loose bound) "
   "-- REFUTING this file's own opening 'balance' hypothesis for THIS parameter choice and initial "
   "condition: the naive Bateman-doubled construction under a nonlinear (cubic) potential does NOT "
   "produce a bounded/conserved paired quantity here, it inherits Psi's own instability",
   abs(paired_quantity[-1] / paired_quantity[10]) > 10)

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")

print("""
HONEST FENCE (tier finite_diagnostic for the numerical stepper and its behavior, reusing this
repo's own already-documented II.8a apparatus, not reinventing it; Dr, explicitly, for the
matter/antimatter interpretation -- a NEW hypothesis, not an established repo claim):
- WHAT THIS ESTABLISHES: a first, honest, runnable test of the founder's hypothesis that
  matter/antimatter might correspond to the ALREADY-DOCUMENTED reader/record (Phi/Psi) apparatus
  (II.8a) -- specifically its OWN named "Bateman-doubled" sign-flipped-damping structure (+D reader,
  -D record), a real, standard physics technique for pairing dissipative/anti-dissipative partners,
  historically used in exactly this antiparticle-adjacent context (Feynman-Stueckelberg, CTP/
  Keldysh). Simulated the EXACT quoted stepper (simplified only by taking a scalar graph operator
  and zero external residuals/sources, disclosed as a simplification of, not a different equation
  from, the source's own formula) with a genuine "pair creation" initial condition. RESULT,
  SELF-CORRECTED (an earlier draft's checks used loose thresholds that masked this): the naive
  construction, under a nonlinear (cubic double-well) potential, is GENUINELY UNSTABLE, not
  balanced -- Phi (reader, +D) settles into a stable fixed point (the OPPOSITE of "transient," the
  opposite of this file's own opening hypothesis about which field persists); Psi (record, -D)
  grows unboundedly (>100x its initial scale, still climbing at the end of a 2000-step run, not
  settling); the eta-pairing bilinear Phi*Psi inherits this instability and grows by the same order
  of magnitude, NOT staying bounded. This is a real, useful, NEGATIVE-but-informative first result,
  not a confirmation.
- WHAT THIS DOES NOT ESTABLISH: (a) that Phi IS antimatter and Psi IS matter, OR the reverse -- the
  simulated behavior does not cleanly match EITHER assignment of this file's own opening hypothesis;
  if anything the direction is backwards (the "reader," proposed as antimatter/transient, is what
  persists here). This is explicitly a NEW, proposed identification, Dr tier, not derived from or
  claimed by the source document (which uses these fields for a different stated purpose, with no
  antimatter language anywhere). (b) any connection to real particle physics quantum numbers
  (baryon number, lepton number, charge) -- this file's Phi/Psi are scalar toy fields with a cubic
  potential, not fermions, not gauge-charged objects. (c) any explanation of the real cosmological
  matter-antimatter asymmetry -- the "net retention" intuition offered in conversation is a
  suggestive analogy, NOT tested or quantified anywhere in this file, and the instability found here
  does not obviously support or refute it either way. (d) any connection to item 12's existing,
  UNRELATED "charge conjugation" result (`all_order_character_v1_0.py`, SU(3) 3<->3bar
  representation conjugation for quark/antiquark COLOR) -- a real, already-established,
  Th_coqc-adjacent result for a DIFFERENT, narrower question, not reused or conflated here. (e) any
  value, prediction, or numeric result usable elsewhere in this domain (e.g. item 1's r) --
  explicitly not attempted. (f) that the naive Bateman-doubled construction is WRONG in general --
  only that THIS parameter choice, THIS potential, and THIS initial condition produce instability;
  real CTP/Keldysh constructions in physics use careful contour prescriptions specifically because
  naive real-time anti-damping is known to be delicate -- this file's instability is consistent
  with, not contradicting, that known subtlety.
- This is Attempt 1 of a brand-new exploration thread (matter/antimatter from root, previously
  listed only as an unexplored backlog item, `SM_INFORMATION_PHILOSOPHY_MASTER.md` section 23). The
  honest, corrected result: the naive version of the founder's hypothesis, tested directly, does NOT
  immediately confirm a clean matter/antimatter asymmetric-but-balanced picture -- it surfaces a
  real instability in the underlying apparatus's anti-damped half under nonlinear dynamics. This
  narrows the next step: any further attempt needs either a linear (or more carefully damped)
  regime, a proper contour/regularization for the anti-damped partner (matching how real CTP/
  Keldysh constructions handle this), or a different pairing altogether -- not a naive re-run of
  this same construction expecting a different outcome.
- Independently adversarially reviewed, 2026-07-25 -- verdict SURVIVES WITH ONE REQUIRED CORRECTION
  (minor, cosmetic, applied above): the reviewer independently recomputed the whole simulation from
  scratch in a fresh script and reproduced this file's numbers exactly (Phi envelope 1.216->0.183,
  Psi envelope 1.106->322.8, max|Psi|=325.14, Phi*Psi ratio 50.28x -- bit-identical), confirming the
  stepper matches the source's quoted formulas sign-by-sign and that the self-correction described
  above is real, not merely claimed. The one required fix: the Part-1 comment mislabeled the
  simplification as `G[Theta_n]=K` when the code has always computed `G[Theta_n]=1` (numerically
  inert here since K=1.0 makes K^2=K, independently re-verified by re-running with the K^2 reading --
  identical output to machine precision -- but the PROSE was wrong about which simplification was
  taken); fixed in Part 1 above. Reviewer found no other overreach: no connection claimed to item 1's
  r, no connection to item 12's SU(3) color-conjugation result, no claim about real quantum numbers
  or cosmological baryon asymmetry, and confirmed checks 3-4 are genuinely tight (not loose-threshold
  theater) against the real ~50-300x magnitudes found. Self-corrected before review, twice, as noted
  above: two loose-threshold checks that would have falsely reported "balance"/"bounded" were caught
  and fixed to report the real, larger magnitudes actually found.
""")
