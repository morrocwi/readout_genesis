#!/usr/bin/env python3
"""
[finite_diagnostic] CFL sufficiency guard — synthetic fixture only, NOT a claim about any
real PDE solver or physical system.

Demonstrates that the core's CFL-style bound Delta_theta_CFL (root of the cubic
D*lambda_max*h^3 + gamma*h = 1) is a CONSERVATIVE SUFFICIENT gate for stability of the
per-mode stepper amplification matrix

    A_lambda(h) = [[1 - D*lambda*h^3,  h*(1 - gamma*h)],
                   [-D*lambda*h^2,     1 - gamma*h    ]]

and NOT a tight instability threshold: there exist step sizes h that VIOLATE the file's
CFL bound yet remain spectrally stable (rho(A) <= 1) over many steps, and the TRUE
stability boundary h_exact (largest h with rho(A_{lambda_max}(h)) <= 1) sits well above
the conservative bound.

Arithmetic is exact Fraction where the object is rational (the fixture graph W, D=D_W-W,
gamma, D_diffusion, the CFL cubic coefficients). lambda_max of L_R is an IRRATIONAL
eigenvalue of a real symmetric matrix, so THIS ONE PIECE is necessarily numeric
(power iteration, float, with a stated tolerance) — clearly flagged below. Root-finding
for h_exact and the spectral radius of the 2x2 stepper matrix are likewise numeric
[finite_diagnostic] computations, not exact-rational claims.

Run: python3 scripts/cfl_sufficiency_guard.py
"""
from fractions import Fraction as F
import math

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

# ------------------------------------------------------------------ fixture graph (exact)
# W = weighted adjacency of a 4-node ring-with-diagonals graph.
W = [[F(0),   F(1),   F(1,2), F(0)],
     [F(1),   F(0),   F(1),   F(1,2)],
     [F(1,2), F(1),   F(0),   F(1)],
     [F(0),   F(1,2), F(1),   F(0)]]
n = 4
D_W = [[sum(W[i]) if i == j else F(0) for j in range(n)] for i in range(n)]
L_R = [[D_W[i][j] - W[i][j] for j in range(n)] for i in range(n)]

check("D_W row sums exact: (3/2, 5/2, 5/2, 3/2)",
      [D_W[i][i] for i in range(n)] == [F(3,2), F(5,2), F(5,2), F(3,2)],
      [D_W[i][i] for i in range(n)])
check("L_R = D_W - W built exact (row0 = 3/2,-1,-1/2,0)",
      L_R[0] == [F(3,2), F(-1), F(-1,2), F(0)], L_R[0])

# ------------------------------------------------------------- lambda_max (NUMERIC, flagged)
# L_R is real symmetric -> real eigenvalues; lambda_max recovered by power iteration.
# NUMERIC-DIAGNOSTIC: lambda_max is irrational in general; floats + tolerance used here only.
def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

def power_iteration(M, iters=500):
    Mf = [[float(x) for x in row] for row in M]
    v = [1.0, 0.3, -0.2, 0.7]
    for _ in range(iters):
        Mv = [sum(Mf[i][j] * v[j] for j in range(len(v))) for i in range(len(v))]
        norm = math.sqrt(sum(x * x for x in Mv))
        v = [x / norm for x in Mv]
    Mv = [sum(Mf[i][j] * v[j] for j in range(len(v))) for i in range(len(v))]
    rayleigh = sum(vi * mvi for vi, mvi in zip(v, Mv)) / sum(vi * vi for vi in v)
    return rayleigh

lambda_max = power_iteration(L_R)
TOL = 1e-4
check("lambda_max(L_R) numerically ~ 3.618034 (power iteration, tol 1e-4) [NUMERIC]",
      abs(lambda_max - 3.618034) < TOL, lambda_max)

# ------------------------------------------------------------------------ CFL bound (numeric)
gamma = F(2, 5)
D = F(3)
gamma_f = float(gamma)
D_f = float(D)

def cfl_cubic(h):
    # D*lambda_max*h^3 + gamma*h - 1
    return D_f * lambda_max * h**3 + gamma_f * h - 1.0

def bisect(f, lo, hi, tol=1e-9, iters=200):
    flo = f(lo)
    for _ in range(iters):
        mid = (lo + hi) / 2
        fmid = f(mid)
        if (fmid > 0) == (flo > 0):
            lo, flo = mid, fmid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return (lo + hi) / 2

h_cfl = bisect(cfl_cubic, 0.0, 2.0)
check("Delta_theta_CFL (cubic root) numerically ~ 0.4244865 (tol 1e-5) [NUMERIC]",
      abs(h_cfl - 0.4244865) < 1e-5, h_cfl)

# --------------------------------------------------------------- per-mode stepper amplification
def A_lambda(h, lam):
    return [[1 - D_f * lam * h**3, h * (1 - gamma_f * h)],
            [-D_f * lam * h**2,    1 - gamma_f * h]]

def spectral_radius_2x2(M):
    # exact quadratic formula for a general 2x2 real matrix (may have complex eigenvalues)
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    tr = a + d
    det = a * d - b * c
    disc = tr * tr - 4 * det
    if disc >= 0:
        sq = math.sqrt(disc)
        e1, e2 = (tr + sq) / 2, (tr - sq) / 2
        return max(abs(e1), abs(e2))
    else:
        sq = math.sqrt(-disc)
        # eigenvalues = tr/2 +- i*sq/2 ; modulus = sqrt((tr/2)^2+(sq/2)^2)
        return math.sqrt((tr / 2) ** 2 + (sq / 2) ** 2)

def simulate_norm_growth(h, lam, steps=50):
    M = A_lambda(h, lam)
    x = [1.0, 1.0]
    norms = [math.sqrt(x[0] ** 2 + x[1] ** 2)]
    for _ in range(steps):
        x = [M[0][0] * x[0] + M[0][1] * x[1], M[1][0] * x[0] + M[1][1] * x[1]]
        norms.append(math.sqrt(x[0] ** 2 + x[1] ** 2))
    return norms

# --------------------------------------------------------- PASSING control: h = 0.55
# violates the file's conservative CFL bound (0.55 > h_cfl ~ 0.4244865) yet IS stable.
h_pass = 0.55
check("PASSING control h=0.55 VIOLATES file CFL bound (0.55 > Delta_theta_CFL)",
      h_pass > h_cfl, (h_pass, h_cfl))
rho_pass = spectral_radius_2x2(A_lambda(h_pass, lambda_max))
check("PASSING control h=0.55: rho(A_lambda_max(h)) ~ 0.883176 < 1 (tol 1e-4) [NUMERIC]",
      abs(rho_pass - 0.883176) < 1e-4 and rho_pass < 1.0, rho_pass)
norms_pass = simulate_norm_growth(h_pass, lambda_max, steps=50)
check("PASSING control h=0.55: ||X|| decays over 50 steps despite bound violation",
      norms_pass[-1] < norms_pass[0], (norms_pass[0], norms_pass[-1]))

# --------------------------------------------------------- FAILING control: h = 0.75
h_fail = 0.75
rho_fail = spectral_radius_2x2(A_lambda(h_fail, lambda_max))
check("FAILING control h=0.75: rho(A_lambda_max(h)) ~ 2.610975 > 1 (tol 1e-4) [NUMERIC]",
      abs(rho_fail - 2.610975) < 1e-4 and rho_fail > 1.0, rho_fail)
norms_fail = simulate_norm_growth(h_fail, lambda_max, steps=50)
check("FAILING control h=0.75: ||X|| blows up over 50 steps (correctly unstable)",
      norms_fail[-1] > norms_fail[0] * 10, (norms_fail[0], norms_fail[-1]))

# --------------------------------------------------------- true boundary vs conservative bound
def rho_minus_one(h):
    return spectral_radius_2x2(A_lambda(h, lambda_max)) - 1.0

h_exact = bisect(rho_minus_one, 0.4244865, 1.5)
check("true stability boundary h_exact numerically ~ 0.6827093 (tol 1e-4) [NUMERIC]",
      abs(h_exact - 0.6827093) < 1e-4, h_exact)

ratio = h_exact / h_cfl
check("h_exact is ~60.8% larger than the file's conservative CFL bound (tol 1e-3)",
      abs(ratio - 1.608) < 1e-3, ratio)
check("CFL bound is SUFFICIENT (h_cfl < h_exact) not TIGHT (h_cfl != h_exact)",
      h_cfl < h_exact and abs(h_cfl - h_exact) > 0.2, (h_cfl, h_exact))

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — file CFL bound confirmed CONSERVATIVE SUFFICIENT (not tight):")
print("h=0.55 violates it yet is stable; h=0.75 is correctly rejected as unstable; true")
print("boundary h_exact ~60.8% above the file bound. [finite_diagnostic] synthetic fixture,")
print("eigenvalue/spectral-radius/root-finding steps are NUMERIC with stated tolerances.")
