#!/usr/bin/env python3
"""
Panel B's designed held-out test, executed exactly as specified (no modification):
fit v_EW from branches U and D jointly (2 data points, least-squares on lambda=exp(-m/v)),
then compare the fitted v to the real v_EW=246 GeV. Branch E (lepton) is held out entirely
from the fit -- it is not used anywhere in this script until the final comparison.
Pass criterion (Panel B's own, stated before running): v_fit in [82, 738] GeV (factor-of-3).
"""
import math

gm_U, gm_D, gm_E = 0.779260, 0.122165, 0.045785   # real PDG geometric means (GeV)

print("== held-out test: fit v_EW from U,D ONLY; E is held out, used only for the final check ==")
print(f"  fit set: gm_U={gm_U} GeV, gm_D={gm_D} GeV")
print(f"  held out (not used in the fit): gm_E={gm_E} GeV")

# lambda_j = exp(-m_j/v). With only 2 points and 1 unknown (v), solve via least-squares on
# log-lambda = -m/v, i.e. treat "ln(lambda_j)" as the observable. Since lambda_j itself depends
# on v circularly, instead fit v directly from the RATIO structure: for a single-parameter
# family lambda_j=exp(-m_j/v), the MLE-style closed form for v from a set of "target lambda"
# is not directly available without an independent lambda measurement -- so instead we fit v by
# requiring the SAME Pi0-style combination (3*lambda_U+3*lambda_D) computed at the true PDG
# masses to match the SAME combination computed at v=246 exactly (i.e. solve numerically for v
# such that the U,D contribution alone is self-consistent -- in practice, with only U,D and no
# second independent equation, v is UNDERDETERMINED by 2 branch-level numbers and 1 unknown v
# UNLESS a second constraint is added. Report this honestly rather than force a fake solve.
def pi0_UD(v):
    return 3*math.exp(-gm_U/v) + 3*math.exp(-gm_D/v)

print("\n== honest finding: v is NOT identifiable from U,D alone with this 1-parameter model ==")
print("  lambda_j=exp(-m_j/v) has exactly ONE unknown (v). With 2 branch inputs (gm_U, gm_D) but")
print("  NO independent lambda measurement to anchor v (lambda itself is never independently")
print("  observed -- only m_j and the ASSUMED v=246 were used to construct lambda in Attempt 5),")
print("  there is no second equation to pin v uniquely from U,D alone. Every v>0 gives SOME")
print("  (lambda_U, lambda_D) pair; nothing in the U,D data forces a particular v without already")
print("  assuming a target Pi0 or alpha value to solve for.")
print("  This means Panel B's test, as specified, needs ONE further assumption to be well-posed:")
print("  a target value for 3*lambda_U+3*lambda_D (or equivalently for Pi0_UD) to solve v against.")

print("\n== fallback (explicitly a further assumption, not in Panel B's original spec): ==")
print("  assume the SAME target Pi0_UD implied by v=246 exactly (i.e. this only checks whether")
print("  solving backwards for v from Pi0_UD(246) recovers v=246 -- which it must, by")
print("  construction/tautology, NOT an independent test).")
target = pi0_UD(246.0)
print(f"  Pi0_UD at v=246 (the tautological target): {target:.8f}")
# solve v from target via bisection (sanity: should recover v=246 exactly)
lo, hi = 1.0, 1e6
for _ in range(200):
    mid = (lo+hi)/2
    if pi0_UD(mid) > target: lo = mid
    else: hi = mid
v_recovered = (lo+hi)/2
print(f"  v recovered by solving Pi0_UD(v)=target: {v_recovered:.4f} GeV (tautological check, not a real test)")

print("\n== CONCLUSION: Panel B's test, as designed, is NOT well-posed with only 2 branch-level ==")
print("numbers and no independent lambda anchor. This is a real, honest finding about a gap in")
print("the test design itself -- not a pass or a fail of the underlying model. A genuinely")
print("well-posed held-out test needs either (a) a THIRD branch-level observable independent of")
print("mass to anchor v, or (b) abandoning the single-v_EW-for-all-branches assumption and testing")
print("something else entirely (e.g. Test 1's qualitative-ordering approach, which IS well-posed).")
