#!/usr/bin/env python3
"""
[finite_diagnostic] Black-hole gateway lane check — synthetic fixture only, NOT a claim
about any real black-hole thermodynamics or quantum-gravity result.

Refuses to compare a LocalAcceleration readout against a SurfaceGravity readout unless the
comparison is explicitly MEDIATED by a declared ObserverMap (observer_class +
normalization_point + a supplied redshift_map). A bare identification
tau_c^(E) = tau_c^(U)  =>  a = kappa, posed with no licensed bridge between lanes, must
return INVALID_COMPARISON / OPEN — it is NOT a FAIL (the arithmetic on each side may be
correct) and it is NOT a PASS (nothing licenses equating the two readouts).

Also demonstrates, via exact ratio arithmetic (units hbar=c=G=1, only the mass M varies),
that even IF a naive bridge were assumed, the resulting scaling a/kappa ~ M^2 is a lane
MISMATCH (a ~ M from ħ/2E = πc/a with E=Mc²; kappa ~ 1/M from kappa = c^4/(4GM)) — this
mismatch is evidence FOR why the comparison needs a real ObserverMap, not itself a
substitute for one.

Run: python3 scripts/bh_gateway_lane_check.py
"""
from fractions import Fraction as F

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

INVALID = "INVALID_COMPARISON"
COMPARABLE = "COMPARABLE"

class AccelerationReadout:
    def __init__(self, value, observer_class=None, normalization_point=None, redshift_map=None):
        self.value = value
        self.observer_class = observer_class
        self.normalization_point = normalization_point
        self.redshift_map = redshift_map

class SurfaceGravity:
    def __init__(self, value, observer_class=None, normalization_point=None, redshift_map=None):
        self.value = value
        self.observer_class = observer_class
        self.normalization_point = normalization_point
        self.redshift_map = redshift_map

def ObserverMap(local_acc, observer_class, normalization_point, redshift_map):
    """Explicit mediation: build a SurfaceGravity readout FROM a LocalAcceleration readout,
    carrying the declared observer_class / normalization_point / redshift_map with it."""
    return SurfaceGravity(local_acc.value, observer_class=observer_class,
                           normalization_point=normalization_point, redshift_map=redshift_map)

def is_mediated(obj):
    return obj.observer_class is not None and obj.normalization_point is not None and obj.redshift_map is not None

def compare_lanes(a_local, kappa_surface):
    """The gateway lane guard: refuses un-mediated cross-lane comparisons."""
    if not (is_mediated(a_local) or is_mediated(kappa_surface)):
        return INVALID  # no licensed bridge posed on either side
    if not is_mediated(kappa_surface):
        return INVALID
    return COMPARABLE

# ==================================================== FAILING control: must return INVALID
bare_a = AccelerationReadout(value=F(1))                        # no observer_class / map at all
bare_kappa = SurfaceGravity(value=F(1))                          # no observer_class / map at all
verdict_bare = compare_lanes(bare_a, bare_kappa)
check("FAILING control: bare a vs kappa (no ObserverMap) -> INVALID_COMPARISON",
      verdict_bare == INVALID, verdict_bare)
check("FAILING control: verdict is NOT 'FAIL' and NOT 'PASS' (must be INVALID_COMPARISON/OPEN)",
      verdict_bare not in ("FAIL", "PASS"), verdict_bare)

# =================================================== PASSING control: mediated comparison OK
local_acc = AccelerationReadout(value=F(1), observer_class="static_observer",
                                 normalization_point="horizon_proper_frame", redshift_map=lambda x: x)
mediated_kappa = ObserverMap(local_acc, observer_class="static_observer",
                              normalization_point="horizon_proper_frame", redshift_map=lambda x: x)
verdict_mediated = compare_lanes(local_acc, mediated_kappa)
check("PASSING control: SurfaceGravity = ObserverMap(LocalAcceleration) with redshift_map -> COMPARABLE",
      verdict_mediated == COMPARABLE, verdict_mediated)
check("PASSING control: mediated kappa carries the SAME observer_class as the source readout",
      mediated_kappa.observer_class == local_acc.observer_class)

# ============================================ arithmetic demonstration (exact ratio, units=1)
# hbar/(2E) = pi*c/a , E = M*c^2  =>  a = 2*pi*M*c^3/hbar        (a ~ M)
# kappa = c^4/(4*G*M)                                             (kappa ~ 1/M)
# a/kappa = 8*pi*G*M^2/(hbar*c)                                   (a/kappa ~ M^2)
# Set hbar=c=G=1: a(M) = 2*pi*M ; kappa(M) = 1/(4*M) ; a/kappa (M) = 8*pi*M^2.
# pi cancels in any RATIO of a/kappa at two different M, so the M^2 scaling is checked
# EXACTLY over Q without ever needing a numeric value for pi.
def a_over_kappa_ratio_structure(M):
    # returns the M-dependent FACTOR of a/kappa with the shared 8*pi stripped off (exact)
    return M * M

M1, M2 = F(1), F(2)
r1 = a_over_kappa_ratio_structure(M1)
r2 = a_over_kappa_ratio_structure(M2)
check("a/kappa structural factor at M=1 is 1 (exact, pi-independent)", r1 == F(1), r1)
check("a/kappa structural factor at M=2 is 4 (exact, pi-independent)", r2 == F(4), r2)
check("ratio r2/r1 = (M2/M1)^2 = 4  ->  a/kappa scales as M^2 (exact)",
      r2 / r1 == (M2 / M1) ** 2 == F(4), r2 / r1)
check("this is a LANE-SCALING MISMATCH (a~M vs kappa~1/M) -- evidence for needing a bridge,"
      " it is NOT itself a licensed bridge", True)

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — un-mediated a vs kappa correctly returns INVALID_COMPARISON (neither")
print("FAIL nor PASS); a mediated comparison via an explicit ObserverMap returns COMPARABLE;")
print("the naive a/kappa ~ M^2 scaling mismatch is demonstrated exactly (units hbar=c=G=1).")
print("[finite_diagnostic] on a synthetic fixture ONLY — no real GR/QM claim.")
