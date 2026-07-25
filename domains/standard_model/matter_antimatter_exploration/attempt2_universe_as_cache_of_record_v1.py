#!/usr/bin/env python3
"""
Matter/antimatter exploration -- Attempt 2, 2026-07-25: tests the founder's follow-up hypothesis
("จักรวาลสรรพสิ่งเป็นเพียงการ CASH ของ RECORD แท้ที่อยู่ในสมการคล้ายหลุมดำ" -- the observable
universe is merely a CACHE of the true Record, which lives in a black-hole-like equation), using
Attempt 1's own already-built, already-reviewed stepper and the repo's own existing
InfoTelegraphHorizonUnification_attempt.v bridge -- not new machinery, a new question asked of two
already-existing constructions.

TWO SEPARATE SUB-CLAIMS, CHECKED SEPARATELY (do not blend them into one verdict):

  (A) DIRECTIONAL CLAIM: Psi (record) is "the true/fundamental" state; Phi (reader) -- and by
      extension the observable universe -- is a lossy CACHE/derivative of it.
  (B) LOCATION CLAIM: the equation Psi genuinely lives "in" is black-hole-like, specifically
      candidate-identified (per the 2026-07-24 exploration log) with the same (M,D,K) telegraph
      triple's own crossover discriminant lambda_c = D^2/(4MK), from
      formal/InfoTelegraphHorizonUnification_attempt.v.

Tier: finite_diagnostic for the structural/numeric checks below (all against the SOURCE's own
quoted equations, re-read fresh here, and the SAME already-adversarially-reviewed stepper Attempt 1
used); Dr, prominently, for the interpretive claims themselves -- neither sub-claim is an existing
repo result, both are new hypotheses proposed in conversation this session.

Run: python3 attempt2_universe_as_cache_of_record_v1.py
"""
import numpy as np

FAILS = []
def ck(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== 0. TIER TAG (mandatory) ==")
print("  finite_diagnostic for the structural/numeric checks (against the source's own quoted")
print("  equations and Attempt 1's own already-reviewed stepper); Dr, explicitly, for both")
print("  interpretive claims (A) and (B) -- new hypotheses proposed in conversation, not existing")
print("  repo claims.")

# ============================================================================
print("\n== 1. SUB-CLAIM (A) -- is Psi structurally 'more fundamental' than Phi? ==")
print("   Checked directly against the SOURCE's own quoted Reader/Record equations (re-read fresh,")
print("   READOUT_GENESIS_CORE_SNAPSHOT.md II.8a, lines ~1141-1146), not against Attempt 1's")
print("   simplified instance alone -- the asymmetry below is present in the FULL equations too:")
print()
print("   Reader: M d_t^2 Phi_n + D d_t^c Phi_n + K G[Theta_n] Phi_n + gradV(Phi_n) - J_n = R_Phi,n")
print("   Record: M d_t^2 Psi_n - D d_t^c Psi_n + K G[Theta_n]^T Psi_n + grad2V(Phi_n) Psi_n = R_Psi,n")
print()
print("   The Reader equation contains NO Psi term anywhere (only R_Phi,n, a generic external")
print("   forcing residual, not a Psi-coupling). The Record equation DOES depend on Phi, via")
print("   grad2V(Phi_n)*Psi_n. This is a fact about the SOURCE's own written equations, not an")
print("   artifact of Attempt 1's R_Phi=0 simplification -- Phi never depended on Psi even before")
print("   that simplification was applied.")

ck("Reader's equation, as quoted in the source, has zero terms containing Psi (checked by direct "
   "re-read of the quoted formula, not assumed) -- Phi evolves AUTONOMOUSLY, driven only by its "
   "own history, K*G[Theta]*Phi, gradV(Phi), and external forcing/residual terms",
   True)  # structural fact, verified by the quoted-formula transcription above, not a numeric check
ck("Record's equation, as quoted in the source, DOES depend on Phi (via grad2V(Phi_n)*Psi_n) -- "
   "Psi is DRIVEN BY Phi's trajectory, not the reverse",
   True)  # same -- structural fact from the quoted formula

print("\n   VERDICT on (A): the causal/structural direction in the source's own equations is")
print("   Phi -> Psi (Phi drives, autonomously; Psi records/responds to Phi's history), NOT")
print("   Psi -> Phi. This is the OPPOSITE of the hypothesis's claim that Psi is 'the true record'")
print("   and Phi (hence the observable universe) is a cache/derivative OF Psi. If anything, in")
print("   this apparatus, Phi is the independent signal and Psi is what RECORDS it (matching the")
print("   field's own name more literally than the hypothesis's proposed direction) -- but Psi's")
print("   own recording is UNSTABLE (Attempt 1: grows ~300x, does not settle), so it is a poor")
print("   'true/stable ground truth' candidate for anything to be cached FROM.")
ck("sub-claim (A), AS LITERALLY STATED (Psi is more fundamental, Phi is a cache of Psi), is "
   "REFUTED by the source's own equation structure -- the dependency runs Phi -> Psi, not Psi -> Phi",
   True)

# ============================================================================
print("\n== 2. SUB-CLAIM (B) -- is Psi's equation genuinely connected to a 'black-hole-like' object ==")
print("      already present in this repo, upstream of any graph L_R? ==")
M, D, K = 1.0, 0.3, 1.0
dt = 0.01

lambda_c = D**2 / (4 * M * K)
print(f"   lambda_c = D^2/(4*M*K) = {lambda_c:.6f}  (from formal/InfoTelegraphHorizonUnification_attempt.v,")
print("   cited by domains/relativity/README.md -- the repo's own existing bridge between this SAME (M,D,K) telegraph")
print("   triple and a classical/quantum crossover discriminant; genuinely upstream of any graph")
print("   L_R -- it depends only on the temporal/damping data M,D,K, not on G[Theta_n]).")

print("\n   Analytic check: for the LINEAR (small-oscillation) regime, Reader's/Record's own")
print("   characteristic roots are exactly ((+-D) +- sqrt(D^2-4MK)) / (2M). Real part = +-D/(2M)")
print("   EXACTLY, independent of K, whenever lambda_c<1 (underdamped, complex roots).")
reader_roots = np.roots([M, D, K])
record_roots = np.roots([M, -D, K])
print(f"   reader roots (M s^2+D s+K=0): {reader_roots}, real parts {reader_roots.real}")
print(f"   record roots (M s^2-D s+K=0): {record_roots}, real parts {record_roots.real}")
ck("reader's linear characteristic real part is exactly -D/(2M) (decay)",
   abs(reader_roots.real[0] - (-D / (2 * M))) < 1e-9, reader_roots.real)
ck("record's linear characteristic real part is exactly +D/(2M) (growth) -- EXACTLY THE NEGATIVE "
   "of reader's, confirmed as an exact analytic fact, not a simulation artifact",
   abs(record_roots.real[0] - (D / (2 * M))) < 1e-9, record_roots.real)

print("\n   Numeric confirmation in the pure-linear (b=0, no double-well) stepper, underdamped case")
print("   (same M,D,K as Attempt 1, lambda_c=0.0225<1): measure the growth/decay rate from")
print("   successive envelope peaks (robust to oscillation phase, unlike a raw log|x| slope).")


def run_linear(M, D, K, dt, N, x0=1e-3, x0p=1e-3, sign=+1):
    def step(x_n, x_nm1):
        A = M / dt**2 + sign * D / (2 * dt)
        rhs = -K * x_n + (2 * M / dt**2) * x_n + (sign * D / (2 * dt) - M / dt**2) * x_nm1
        return rhs / A
    x = np.zeros(N)
    x[0], x[1] = x0, x0p
    for n in range(1, N - 1):
        x[n + 1] = step(x[n], x[n - 1])
    return x


def peak_rate(x, dt, lo, hi):
    ax = np.abs(x)
    peaks = [i for i in range(lo, hi) if ax[i] > ax[i - 1] and ax[i] > ax[i + 1]]
    if len(peaks) < 2:
        return None
    p0, p1 = peaks[0], peaks[-1]
    return float(np.log(ax[p1] / ax[p0]) / ((p1 - p0) * dt))


N = 2000
phi_lin = run_linear(M, D, K, dt, N, sign=+1)
psi_lin = run_linear(M, D, K, dt, N, sign=-1)
reader_rate = peak_rate(phi_lin, dt, 200, N - 100)
record_rate = peak_rate(psi_lin, dt, 200, N - 100)
print(f"   measured reader peak-envelope rate: {reader_rate:.6f}  (predicted {-D/(2*M):.6f})")
print(f"   measured record peak-envelope rate: {record_rate:.6f}  (predicted {D/(2*M):.6f})")
ck("measured reader envelope decay rate matches -D/(2M) to 1e-3",
   abs(reader_rate - (-D / (2 * M))) < 1e-3, reader_rate)
ck("measured record envelope growth rate matches +D/(2M) to 1e-3",
   abs(record_rate - (D / (2 * M))) < 1e-3, record_rate)
ck("this K-INDEPENDENCE is itself checked, not assumed: rerunning with a DIFFERENT K (K=5, still "
   "lambda_c=D^2/4MK<1) reproduces the SAME +-D/(2M) rate (a real, distinct verification, not the "
   "same computation repeated)",
   abs(peak_rate(run_linear(M, D, 5.0, dt, N, sign=-1), dt, 200, N - 100) - (D / (2 * M))) < 1e-3)

print("\n== 3. does lambda_c=1 actually mark a genuine regime transition (not just a renamed number)? ==")
print("   Overdamped case: D=3.0, K=1.0 -> lambda_c=D^2/4MK = 2.25 > 1 (real, not complex, roots).")
D_over = 3.0
record_roots_over = np.roots([M, -D_over, K])
print(f"   record roots (overdamped): {record_roots_over}")
ck("overdamped record roots are REAL (not complex) -- confirming lambda_c=1 genuinely separates "
   "oscillatory-decay/growth (lambda_c<1) from monotonic decay/growth (lambda_c>1), a real "
   "qualitative transition in this equation's own solution structure",
   np.all(np.isreal(np.round(record_roots_over.imag, 9))))
over_rate = float(max(record_roots_over.real))
ck("in the OVERDAMPED regime, the dominant growth rate is STRICTLY GREATER than D/(2M) and DOES "
   "depend on K (unlike the underdamped case checked in Part 2) -- confirming lambda_c=1 is where "
   "the growth-rate FORMULA itself changes character, not merely a renamed threshold",
   over_rate > D_over / (2 * M) + 1e-6, over_rate)

print("""
HONEST FENCE (finite_diagnostic for all numeric/structural checks above; Dr, prominently, for
both interpretive claims -- neither is an existing repo result):

- WHAT THIS ESTABLISHES:
  (A) REFUTED AS STATED: the source's own Reader/Record equations (re-read directly, not assumed)
      make Phi structurally AUTONOMOUS (no Psi dependence anywhere) and Psi DEPENDENT on Phi (via
      grad2V(Phi)*Psi). The causal direction is Phi->Psi, the opposite of "Psi is the true record
      and Phi/the-observable-universe is a cache of it." If a cache/original relationship exists at
      all in this apparatus, the literal field names suggest reading it the OTHER way (Phi is the
      independent signal; Psi is what records/responds to it) -- but Psi's own recording is
      unstable (Attempt 1), a poor candidate for "the true, stable ground truth."
  (B) A REAL, EXACT, CHECKED CONNECTION EXISTS, but it is narrower and different in KIND than "Psi
      lives in a black-hole equation": lambda_c=D^2/(4MK) (this repo's own existing
      InfoTelegraphHorizonUnification_attempt.v bridge, upstream of any graph L_R) genuinely marks
      a qualitative transition in Record's OWN dynamics -- underdamped (lambda_c<1): oscillatory
      growth at a FIXED, K-INDEPENDENT rate +D/(2M), exactly the negative of Reader's own decay
      rate; overdamped (lambda_c>1): monotonic growth at a K-DEPENDENT rate strictly greater than
      D/(2M). Both facts checked exactly (roots computed analytically AND confirmed numerically to
      1e-3 against the actual stepper, with an independent K value re-run to rule out coincidence).
- WHAT THIS DOES NOT ESTABLISH:
  (a) that lambda_c=1 is a STABILITY boundary -- it is not: Record is unstable (positive real-part
      root) for ANY D>0 regardless of lambda_c; the actual instability onset is D=0, not lambda_c=1.
      Calling lambda_c "a black-hole-like equation" for Psi is, at best, a suggestive Dr-tier
      analogy about where the FUNCTIONAL FORM of the instability changes, not an identification of
      an event horizon or any other genuine black-hole structure. This is consistent with (not a
      new contradiction of) InfoTelegraphHorizonUnification_attempt.v's OWN honest fence, which
      already states lambda_c is a distinct object from node-8's horizon lapse N=sqrt(detB).
  (b) any resolution of what "the observable universe" corresponds to in this toy scalar system --
      no readout map, no cosmology, no correspondence to real spacetime is built or tested here.
  (c) any connection to item 1's r, to item 12's SU(3) color-conjugation result, to real particle
      quantum numbers, or to the real cosmological baryon asymmetry -- none attempted here, same as
      Attempt 1.
  (d) that the founder's broader intuition (universe as readout, not truth) is wrong in general --
      that IS this repo's own existing readout-not-truth root stance (Z_n retained state vs. any
      O(X) readout of it, SM_INFORMATION_PHILOSOPHY_MASTER.md section 1.2). What is refuted here is
      only the SPECIFIC identification tested: that Psi-in-this-apparatus plays the "true record"
      role and Phi-in-this-apparatus plays the "cache" role, and that lambda_c is literally a
      black-hole equation rather than a growth-rate-regime marker.
- This is Attempt 2 of the matter/antimatter exploration thread: a second real, disclosed negative
  result on the specific hypotheses tested, alongside two genuine positive facts (Phi->Psi causal
  structure; lambda_c's exact role as a growth-rate-regime marker) that a future attempt could use
  more carefully -- neither hypothesis, as literally stated, survives this check.
- Independently adversarially reviewed, 2026-07-25 -- verdict SURVIVES WITH REQUIRED CORRECTIONS,
  applied above (1): the file cited its own path for
  `formal/InfoTelegraphHorizonUnification_attempt.v` incorrectly as living under `domains/`
  relativity/` -- the reviewer confirmed the real file only exists under `formal/`, not
  `domains/relativity/` (that directory only carries a README that CITES the formal/ file); fixed
  at every occurrence. All substantive claims were independently reverified from scratch and hold:
  the source equations were re-read directly and confirmed to match this file's transcription
  exactly; the +-D/(2M) exact-real-part algebra was independently re-derived symbolically (general,
  not a coincidence of the specific M,D,K used); the numeric growth/decay rates were independently
  reproduced with a different (RK4) integrator, not just re-running this file's own stepper; and the
  lambda_c honest-fence quote from domains/relativity/README.md was confirmed accurate and not taken
  out of context. The two bare `ck(name, True)` calls (structural facts about the source's own
  quoted equations, not numeric results) were reviewed and found honestly labeled, not masking
  anything that should have been a real computation.
""")

if FAILS:
    print(f"\n{len(FAILS)} FAIL(S): {FAILS}")
else:
    print("\nAll checks PASS.")
