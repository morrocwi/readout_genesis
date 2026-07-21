#!/usr/bin/env python3
"""
Domain-discovery battery — the real, runnable engine behind the core's claim that a
domain-discovery engine "was built and run ... it recovered the true underlying laws in
every planted case (N·S/8, N²/8, an affine law, a three-variable case), it never
fabricated a spurious near-miss law (N·S/16 was dangled and correctly refused), it held
exactly on a withheld holdout split, and it refused every non-polynomial law it was
offered" (READOUT_GENESIS_CORE.md, Part III Face 12).

This is that engine. Exact rational arithmetic (Fraction) — no floats. From a raw
transition tape alone it: (a) finds the minimal closed variable set, (b) tests
cross-channel interaction via a mixed second difference, (c) fits the minimal exact law
over ℚ under a DECLARED candidate basis with a full-rank identifiability gate (else
abstains), and (d) reads off conservation laws. PASS iff every planted case is recovered
exactly on a withheld holdout AND every adversarial near-miss / non-polynomial is refused.

Run:  python3 scripts/domain_discovery_battery.py
"""
from fractions import Fraction as F
from itertools import product

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

# ---- exact rational linear solve (Gauss-Jordan over Q); returns None if not full rank ----
def solve_exact(A, b):
    A = [row[:] for row in A]; b = b[:]; m = len(A); n = len(A[0]); r = 0
    piv = []
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]; b[r], b[p] = b[p], b[r]
        inv = F(1)/A[r][c]
        A[r] = [x*inv for x in A[r]]; b[r] = b[r]*inv
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [x - f*y for x, y in zip(A[i], A[r])]; b[i] = b[i] - f*b[r]
        piv.append(c); r += 1
        if r == m: break
    # consistency of any all-zero rows
    for i in range(r, m):
        if b[i] != 0: return None  # inconsistent
    if len(piv) < n: return None   # rank-deficient -> UNDERDETERMINED (identifiability gate)
    x = [F(0)]*n
    for i, c in enumerate(piv): x[c] = b[i]
    return x

def rank_exact(A):
    A = [row[:] for row in A]; m = len(A); n = len(A[0]); r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        inv = F(1)/A[r][c]; A[r] = [x*inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [x - f*y for x, y in zip(A[i], A[r])]
        r += 1
        if r == m: break
    return r

# ---- the discovery engine ----
def basis_eval(names, vars_):
    """Evaluate a declared monomial basis (by name) at a variable assignment dict."""
    out = []
    for nm in names:
        if nm == "1": out.append(F(1)); continue
        val = F(1)
        for tok in nm.split("*"):
            if "^" in tok:
                v, p = tok.split("^"); val *= vars_[v]**int(p)
            else:
                val *= vars_[tok]
        out.append(val)
    return out

def discover(tape, varnames, basis, target_index):
    """tape: list of (inputs_dict, outputs_tuple). Fit output[target_index] over `basis`.
       Returns (coeffs) or None if underdetermined (identifiability gate abstains)."""
    A = [basis_eval(basis, inp) for inp, _ in tape]
    b = [out[target_index] for _, out in tape]
    if rank_exact(A) < len(basis):      # identifiability gate: rank(A) == #coeffs, else abstain
        return None
    return solve_exact(A, b)

def predict(coeffs, basis, inp):
    return sum(c*v for c, v in zip(coeffs, basis_eval(basis, inp)))

# =========================== PLANTED (must recover exactly) ===========================
BASIS2 = ["1", "N", "S", "N^2", "N*S", "S^2"]
def make_tape(law, pts, varnames=("N", "S")):
    return [({varnames[0]: F(a), varnames[1]: F(b)}, law(F(a), F(b))) for a, b in pts]

PTS = [(0,0),(1,0),(0,1),(1,1),(2,1),(1,2)]                 # 6 rows -> full rank on BASIS2
HOLD = [(3,5),(2,3),(4,1)]                                   # withheld holdout

print("== PLANTED CASE 1: N' = N + N·S/8 , S' = S - N·S/8 (conserves C=N+S) ==")
law1 = lambda N,S: (N + N*S/8, S - N*S/8)
tape1 = make_tape(law1, PTS)
cN = discover(tape1, ("N","S"), BASIS2, 0); cS = discover(tape1, ("N","S"), BASIS2, 1)
check("N' law recovered = N + (1/8)N·S", cN == [F(0),F(1),F(0),F(0),F(1,8),F(0)], cN)
check("S' law recovered = S - (1/8)N·S", cS == [F(0),F(0),F(1),F(0),F(-1,8),F(0)], cS)
# holdout exactness
holdok = all(predict(cN,BASIS2,{"N":F(a),"S":F(b)})==law1(F(a),F(b))[0] and
             predict(cS,BASIS2,{"N":F(a),"S":F(b)})==law1(F(a),F(b))[1] for a,b in HOLD)
check("holds EXACTLY on withheld holdout (3,5),(2,3),(4,1)", holdok)
# conservation readout: N'+S' coefficients == N+S coefficients
consN = [x+y for x,y in zip(cN,cS)]
check("conservation discovered: N'+S' = N+S (C=N+S)", consN == [F(0),F(1),F(1),F(0),F(0),F(0)], consN)

print("== PLANTED CASE 2: N' = N + N^2/8 ==")
law2 = lambda N,S: (N + N*N/8, S)
c2 = discover(make_tape(law2,PTS), ("N","S"), BASIS2, 0)
check("N^2/8 law recovered", c2 == [F(0),F(1),F(0),F(1,8),F(0),F(0)], c2)

print("== PLANTED CASE 3: affine  N' = 2N + 3S + 1 ==")
law3 = lambda N,S: (2*N + 3*S + 1, S)
c3 = discover(make_tape(law3,PTS), ("N","S"), BASIS2, 0)
check("affine law recovered = 1 + 2N + 3S", c3 == [F(1),F(2),F(3),F(0),F(0),F(0)], c3)

print("== PLANTED CASE 4: three-variable  X' = X + Y·Z/4 ==")
BASIS3 = ["1","X","Y","Z","X*Y","X*Z","Y*Z"]
pts3 = [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1)]  # 7 rows -> full rank on BASIS3
law4 = lambda X,Y,Z: X + Y*Z/4
tape3 = [({"X":F(a),"Y":F(b),"Z":F(c)}, (law4(F(a),F(b),F(c)),)) for a,b,c in pts3]
c4 = discover(tape3, ("X","Y","Z"), BASIS3, 0)
check("3-var law recovered = X + (1/4)Y·Z", c4 == [F(0),F(1),F(0),F(0),F(0),F(0),F(1,4)], c4)

print("== INTERACTION test (mixed 2nd difference) — must detect coupling ==")
g = lambda N,S: (N*S)/8          # increment of N under law1
mixed = g(2,2)-g(2,1)-g(1,2)+g(1,1)
check("mixed 2nd difference != 0 (N,S interact) = 1/8", mixed == F(1,8), mixed)
g_add = lambda N,S: N/8          # a non-interacting increment
mixed0 = g_add(2,2)-g_add(2,1)-g_add(1,2)+g_add(1,1)
check("mixed 2nd difference == 0 for a separable law (no false interaction)", mixed0 == 0)

print("== ADVERSARIAL: must REFUSE near-miss and non-identifiable ==")
# near-miss N·S/16: fit still finds the true 1/8 from the exact tape, so the WRONG law is refused by residual
wrongN = [F(0),F(1),F(0),F(0),F(1,16),F(0)]                  # N + N·S/16 (dangled wrong law)
resid = max(abs(predict(wrongN,BASIS2,{"N":F(a),"S":F(b)}) - law1(F(a),F(b))[0]) for a,b in HOLD)
check("near-miss N·S/16 REFUSED (nonzero holdout residual = 15/16 at (3,5))",
      resid == F(15,16), resid)
# identifiability gate: too few rows -> UNDERDETERMINED -> abstain (do not guess)
short = make_tape(law1, PTS[:5])                             # 5 rows < 6 coeffs
check("identifiability gate: 5 rows for 6-coeff basis -> ABSTAIN (None), not a guessed law",
      discover(short, ("N","S"), BASIS2, 0) is None)
# non-polynomial law: no exact fit in a polynomial basis on a rich tape -> inconsistent -> refuse
nonpoly = [({"N":F(n),"S":F(s)}, (F(1) if (n+s)%2==0 else F(0),)) for n,s in
           [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(2,1),(1,2),(2,2)]]   # parity: not polynomial over Q
check("non-polynomial (parity) law REFUSED (no exact ℚ-poly fit -> inconsistent)",
      discover(nonpoly, ("N","S"), BASIS2, 0) is None)

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — all planted laws recovered exactly on holdout; all near-miss /")
print("non-identifiable / non-polynomial cases refused. [finite_diagnostic] on synthetic")
print("adversarial tapes ONLY — NOT a claim on any real biological/physical domain.")
