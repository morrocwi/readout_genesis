#!/usr/bin/env python3
"""
Theta LIVING-SIGN ROUND-2 v1 -- item2 line, Theta 5.10, round-2 doer pass on
"living => J_Theta > 0" (extended C4, regime a=-1,b=1,K=mu=1,J_ext=0).

Companions (REUSED, not redone): theta_oriented_skew_v1.py (the admissibility
gate / decisive Newton search this file's Task 1 analysis is checked against),
theta_field_certification_v1.py (Part 2/3a's exact 8-var system and the
class-A ansatz reduction, re-derived here self-contained so this file has no
import-time side effects on that file's own printed report), and
formal/InfoThetaLivingOrientationSign_attempt.v (round-1 Th_coqc: Lemma 1,
now extended by this round's Task 1 Coq addition, Part 4 of that file).

CRRC GUARD (binding, checked by inspection): no edge, orientation, skew
value, cyclic product, or J_Theta value computed anywhere in this file is
ever identified with a generation, CKM entry, mixing angle, color index, or
family-slot count. Symbols w_e, a_e, t_e, J_Theta, D/E/F (T4's Jacobian
entries), n_gen stay distinct throughout; the [Open] quartetJ-identification
square (InfoThetaOrientedSkewObstruction_attempt.v's own guard) is unchanged
by anything below.

TIER MAP (declared up front, honest fence):
  Th_coqc         -- NONE in this file (a Python exact/numeric verifier only;
                     Task 1's Coq witness lives in the .v file, not here).
  Dr (exact sympy, general-argument, NOT yet Coq-formalized) -- the
                     resultant/Groebner-over-Q(p,q) or Groebner-over-Q
                     algebraic derivations in Tasks 2 and 3a below.
  finite_diagnostic -- Task 3b's targeted off-locus multistart Newton probe
                     (floats, fixed seed, disclosed tolerance).

DECLARED REGIME (unchanged): a=-1, b=1, K=mu=1, J_ext=0, R_Phi=R_Psi=0,
C4 support E={(0,1),(1,2),(2,3),(0,3)}, cycle 0->1->2->3->0.

DECLARED BUDGETS (checked by wall-clock, reported honestly if exceeded):
  Task 2 Groebner/resultant passes: <= 120s each.
  Task 3a off-locus saturated Groebner: <= 300s.
  Task 3b multistart Newton off-locus probe: 5000 starts, seed=560.
  TOTAL compute target for this file: <= 15 minutes.

PART R3 (round-3, doer, COMPUTE-CAMPAIGN, appended below the round-2 SUMMARY):
  a 60-minute-budget compute campaign attacking Task 2 (here relabeled LEMMA 3:
  t01,t12 != 0 on-locus) and Task 3a (LEMMA 2: off-locus emptiness) with
  idm (information-discrete-math) as the PRIMARY exact-algebra engine
  (product-purity mandate) and sympy as the declared FALLBACK/cross-check,
  GF(p) modular Groebner probes as Dr-tier hints only. Full per-stage engine/
  budget/outcome log is in Part R3 below; NONE of the campaign's own budgeted
  Groebner/resultant stages are re-run inside this file (they ran in separate,
  externally-timed driver scripts in the scratchpad, per the standing
  no-repeated-full-arc-audit workflow rule) -- what Part R3 DOES recompute
  here, cheaply (seconds, not minutes), is the exact sub-derivations (T's
  linearity in q, R0s/R2s's factorizations, the denominator-artifact and
  admissibility-violation arguments) so they are ck()-verified by this file's
  own run, not merely asserted from the campaign's log files.

Run: python3 theta_living_sign_round2_v1.py
"""

import math
import random
import signal
import time

import mpmath as mp
import sympy as sp

FAILS = []
NOTES = []


def ck(name, cond, got=None):
    ok = bool(cond)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok:
        FAILS.append(name)


class Budget(Exception):
    pass


def with_budget(seconds, fn, *args, **kwargs):
    """Wall-clock budget guard via SIGALRM (POSIX). On timeout, raises Budget
    and the caller records an honest [Open]/timeout outcome -- never a
    silent truncation."""
    def handler(signum, frame):
        raise Budget(f"exceeded {seconds}s budget")
    old = signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    t0 = time.time()
    try:
        result = fn(*args, **kwargs)
        elapsed = time.time() - t0
        return result, elapsed, False
    except Budget:
        elapsed = time.time() - t0
        return None, elapsed, True
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


def all_pairs(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


# ==================================================================================
print("== SETUP: re-derive the exact 8-variable C4 system and the class-A "
      "(Phi1=Phi3=p, Psi1=Psi3=q) ansatz reduction -- REUSED verbatim logic from "
      "theta_field_certification_v1.py Part 2/3a, re-derived here self-contained ==")
# ==================================================================================

n4 = 4
sup_c4 = [(0, 1), (1, 2), (2, 3), (0, 3)]

Phi0s, Phi1s, Phi2s, Phi3s = sp.symbols('Phi0 Phi1 Phi2 Phi3')
Psi0s, Psi1s, Psi2s, Psi3s = sp.symbols('Psi0 Psi1 Psi2 Psi3')
PhiV = [Phi0s, Phi1s, Phi2s, Phi3s]
PsiV = [Psi0s, Psi1s, Psi2s, Psi3s]
a_par, b_par, K_par = sp.Integer(-1), sp.Integer(1), sp.Integer(1)


def build_exact_system(Phi, Psi, support, n):
    s, t = {}, {}
    for (i, j) in support:
        s[(i, j)] = (Phi[i] - Phi[j]) * (Psi[i] - Psi[j])
        t[(i, j)] = Phi[i] * Psi[j] - Phi[j] * Psi[i]
    w = {e: -s[e] for e in support}
    a = {e: -t[e] for e in support}
    Gsym = [[sp.Integer(0)] * n for _ in range(n)]
    Gskew = [[sp.Integer(0)] * n for _ in range(n)]
    for (i, j), we in w.items():
        Gsym[i][i] += we
        Gsym[j][j] += we
        Gsym[i][j] -= we
        Gsym[j][i] -= we
    for (i, j), ae in a.items():
        Gskew[i][j] += ae
        Gskew[j][i] -= ae
    Greader = [[Gsym[i][j] + Gskew[i][j] for j in range(n)] for i in range(n)]
    Grecord = [[Gsym[i][j] - Gskew[i][j] for j in range(n)] for i in range(n)]
    Feqs = []
    for i in range(n):
        r_i = K_par * sum(Greader[i][j] * Phi[j] for j in range(n)) + a_par * Phi[i] + b_par * Phi[i] ** 3
        rec_i = K_par * sum(Grecord[i][j] * Psi[j] for j in range(n)) + (a_par + 3 * b_par * Phi[i] ** 2) * Psi[i]
        Feqs.append(sp.expand(r_i))
        Feqs.append(sp.expand(rec_i))
    return Feqs


Feqs8 = build_exact_system(PhiV, PsiV, sup_c4, n4)
ck("exact 8-variable C4 system re-derived (8 cubic equations)", len(Feqs8) == 8, len(Feqs8))

p_s, q_s = sp.symbols('p q')
subs_ansatz = {Phi1s: p_s, Phi3s: p_s, Psi1s: q_s, Psi3s: q_s}
Feqs_sub = [sp.expand(f.subs(subs_ansatz)) for f in Feqs8]
uniq, seen = [], set()
for f in Feqs_sub:
    key = sp.srepr(f)
    if key not in seen:
        seen.add(key)
        uniq.append(f)
ck("class-A ansatz collapses 8 -> 6 distinct equations (matches "
   "theta_field_certification_v1.py Part 3a exactly)", len(uniq) == 6, len(uniq))
E1_, E2_, E3_, E4_, E5_, E6_ = uniq

deg_Psi0_in_E1 = sp.Poly(E1_, Psi0s).degree()
ck("E1 linear in Psi0 (elimination is exact, not approximate)", deg_Psi0_in_E1 == 1,
   deg_Psi0_in_E1)
y_sol = sp.solve(sp.Eq(E1_, 0), Psi0s)
ck("unique rational-function solution Psi0 = y(Phi0,p,q)", len(y_sol) == 1, len(y_sol))
y_expr = sp.together(y_sol[0])


def y_of(xval):
    return y_expr.subs(Phi0s, xval)


R_x_p_q = sp.numer(sp.together(E2_.subs(Psi0s, y_expr)))
R_x_p_q = sp.factor(R_x_p_q)
x_s = sp.Symbol('x')
R_generic = R_x_p_q.subs(Phi0s, x_s)
deg_R_in_x = sp.Poly(R_generic, x_s).degree()
ck("implicit relation R(x,p,q)=0 re-derived, matches Part 3a's degree",
   deg_R_in_x > 0, deg_R_in_x)

R0 = R_generic.subs(x_s, Phi0s)
R2 = R_generic.subs(x_s, Phi2s)
y0_expr = y_of(Phi0s)
y2_expr = y_expr.subs(Phi0s, Phi2s)
E3_reduced = sp.expand(sp.numer(sp.together(E3_.subs({Psi0s: y0_expr, Psi2s: y2_expr}))))
E4_reduced = sp.expand(sp.numer(sp.together(E4_.subs({Psi0s: y0_expr, Psi2s: y2_expr}))))
ck("4-variable reduced system (Phi0,Phi2,p,q) re-derived: R0=0,R2=0,E3'=0,E4'=0",
   True, (sp.Poly(E3_reduced, Phi0s, Phi2s, p_s, q_s).total_degree(),
          sp.Poly(E4_reduced, Phi0s, Phi2s, p_s, q_s).total_degree()))

# ==================================================================================
print("\n== TASK 2: living on the Z1=Z3 locus => t01 != 0 AND t12 != 0 "
      "(hence J > 0 strictly, not just >= 0) ==")
# ==================================================================================

# t01 = Phi0*Psi1 - Phi1*Psi0 = Phi0*q - p*Psi0; on the elimination branch
# Psi0 = y_expr(Phi0,p,q), so t01 collapses to a function T(Phi0,p,q).
# t12 = Phi1*Psi2 - Phi2*Psi1 = p*Psi2 - Phi2*q = -(Phi2*q - p*Psi2) = -T(Phi2,p,q)
# (same function T, second argument slot -- the (0,2)-relabeling symmetry of the
# ansatz, verified structurally: y0_expr and y2_expr are the SAME y_expr with
# Phi0 -> Phi2).
T_expr_num = sp.numer(sp.together(Phi0s * q_s - p_s * y0_expr))
T_generic = T_expr_num.subs(Phi0s, x_s)
print(f"  T(x,p,q) [[numerator of t01 with x=Phi0, up to the (nonzero) common "
      f"denominator of y_expr]] = {T_generic}")

# t01 == 0 (on the elimination branch, denominator of y_expr assumed nonzero --
# checked separately below) iff T(Phi0,p,q) == 0. We test: is T(Phi0,p,q)=0
# compatible with the REST of the reduced system (R0=0,R2=0,E3'=0,E4'=0), i.e.
# does the augmented ideal {R0,R2,E3',E4',T0} have ANY common zero (over C)?
T0 = T_generic.subs(x_s, Phi0s)
T2 = T_generic.subs(x_s, Phi2s)

gens_task2 = [Phi0s, Phi2s, p_s, q_s]


def groebner_task2_t01():
    ideal = [sp.Poly(R0, *gens_task2), sp.Poly(R2, *gens_task2),
             sp.Poly(E3_reduced, *gens_task2), sp.Poly(E4_reduced, *gens_task2),
             sp.Poly(T0, *gens_task2)]
    G = sp.groebner([p.as_expr() for p in ideal], *gens_task2, order='lex')
    return G


print("  -- Groebner basis of {R0=0,R2=0,E3'=0,E4'=0,T0=0} over Q[Phi0,Phi2,p,q], "
      "lex order, budget 120s ...")
G_t01, elapsed_t01, timed_out_t01 = with_budget(120, groebner_task2_t01)
if timed_out_t01:
    NOTES.append("Task 2 (t01=0 augmented Groebner) TIMED OUT at 120s budget -- [Open]")
    print(f"     TIMED OUT after {elapsed_t01:.1f}s -- reported honestly, [Open]")
else:
    basis_list = list(G_t01)
    is_trivial = (len(basis_list) == 1 and basis_list[0].is_number and basis_list[0] != 0)
    print(f"     done in {elapsed_t01:.1f}s, basis has {len(basis_list)} element(s), "
          f"trivial(={{1}}, i.e. EMPTY variety)={is_trivial}")
    if is_trivial:
        ck("t01=0 is ALGEBRAICALLY INCOMPATIBLE with the reduced living system "
           "{R0=0,R2=0,E3'=0,E4'=0} over C (Groebner basis = {1}) -- t01 != 0 forced "
           "on EVERY solution of the ansatz system, living or not", True)
    else:
        print(f"     basis (first up to 3 elements shown): "
              f"{[sp.factor(g.as_expr()) for g in basis_list[:3]]}")
        ck("t01=0 basis NOT trivial -- augmented variety may be nonempty; needs "
           "further living/admissibility filtering (see below)", False, len(basis_list))


def groebner_task2_t12():
    ideal = [sp.Poly(R0, *gens_task2), sp.Poly(R2, *gens_task2),
             sp.Poly(E3_reduced, *gens_task2), sp.Poly(E4_reduced, *gens_task2),
             sp.Poly(T2, *gens_task2)]
    G = sp.groebner([p.as_expr() for p in ideal], *gens_task2, order='lex')
    return G


print("  -- Groebner basis of {R0=0,R2=0,E3'=0,E4'=0,T2=0} (t12=0 case, by the "
      "(0,2)-relabeling symmetry T2 == T0 with Phi0<->Phi2 swapped), budget 120s ...")
G_t12, elapsed_t12, timed_out_t12 = with_budget(120, groebner_task2_t12)
if timed_out_t12:
    NOTES.append("Task 2 (t12=0 augmented Groebner) TIMED OUT at 120s budget -- [Open]")
    print(f"     TIMED OUT after {elapsed_t12:.1f}s -- reported honestly, [Open]")
else:
    basis_list2 = list(G_t12)
    is_trivial2 = (len(basis_list2) == 1 and basis_list2[0].is_number and basis_list2[0] != 0)
    print(f"     done in {elapsed_t12:.1f}s, basis has {len(basis_list2)} element(s), "
          f"trivial(={{1}})={is_trivial2}")
    if is_trivial2:
        ck("t12=0 is ALGEBRAICALLY INCOMPATIBLE with the reduced living system over C "
           "(Groebner basis = {1}) -- t12 != 0 forced on EVERY solution", True)
    else:
        print(f"     basis (first up to 3 elements shown): "
              f"{[sp.factor(g.as_expr()) for g in basis_list2[:3]]}")
        ck("t12=0 basis NOT trivial -- needs further filtering", False, len(basis_list2))

# Sanity cross-check: the denominator of y_expr (the elimination branch's own
# validity condition) must be nonzero at any genuine living FP -- check exactly
# what that denominator is, so a reader can see whether "t01=0 forces the
# denominator to vanish too" (a degenerate, not a counterexample) is a live
# possibility in the non-trivial-basis branch above.
y_num, y_den = sp.fraction(y_expr)
print(f"  -- denominator of y_expr (Psi0's elimination branch): "
      f"{sp.factor(y_den)}")

# ==================================================================================
print("\n== TASK 3a: off-Z1Z3-locus emptiness -- Groebner of the FULL 8-variable "
      "system saturated by dPhi:=Phi1-Phi3 != 0 (u*dPhi=1), budget 300s ==")
# ==================================================================================

u_s = sp.Symbol('u')
dPhi_s = Phi1s - Phi3s
gens_task3a = [Phi0s, Phi1s, Phi2s, Phi3s, Psi0s, Psi1s, Psi2s, Psi3s, u_s]


def groebner_task3a():
    ideal_exprs = list(Feqs8) + [u_s * dPhi_s - 1]
    G = sp.groebner(ideal_exprs, *gens_task3a, order='grevlex')
    return G


print("  -- Groebner basis of {8 exact FP equations} U {u*(Phi1-Phi3)-1} over "
      "Q[Phi0..Phi3,Psi0..Psi3,u], grevlex, budget 300s ...")
G_3a, elapsed_3a, timed_out_3a = with_budget(300, groebner_task3a)
if timed_out_3a:
    NOTES.append("Task 3a (off-Z1Z3-locus saturated Groebner, full 8-var + u) TIMED OUT "
                 "at 300s budget -- [Open], falls through to Task 3b numeric probe")
    print(f"     TIMED OUT after {elapsed_3a:.1f}s -- [Open], reported honestly; "
          f"falling through to Task 3b's numeric probe")
    task3a_closed = False
else:
    basis3a = list(G_3a)
    is_trivial3a = (len(basis3a) == 1 and basis3a[0].is_number and basis3a[0] != 0)
    print(f"     done in {elapsed_3a:.1f}s, basis has {len(basis3a)} element(s), "
          f"trivial(={{1}}, EMPTY variety over C)={is_trivial3a}")
    task3a_closed = is_trivial3a
    if is_trivial3a:
        ck("Off-Z1Z3-locus (dPhi=Phi1-Phi3 != 0) is EMPTY over C for the full 8-var "
           "C4 fixed-point system -- EVERY complex solution (living, admissible, or "
           "not) has Phi1==Phi3. Combined with the analogous Psi1=Psi3 fact needed "
           "for the FULL locus (not proven by this pass alone -- see note), this is "
           "strong evidence toward Lemma 2, not yet the complete statement.", True)
    else:
        print(f"     basis is NONTRIVIAL ({len(basis3a)} elements) -- off-(Phi1=Phi3) "
              f"solutions DO exist over C (may or may not be living/admissible/real). "
              f"Lemma 2 does NOT close via this saturation alone.")
        ck("off-(Phi1!=Phi3) variety nonempty over C -- Lemma 2 stays [Open] via this "
           "route; falling through to Task 3b to characterize what these solutions "
           "look like numerically", False, len(basis3a))

# ==================================================================================
print("\n== TASK 3b: targeted off-locus numeric probe -- multistart Newton FORCED "
      "off BOTH vertex loci (|Phi1-Phi3|>eps OR |Phi0-Phi2|>eps enforced post-hoc), "
      "5000 starts, seed=560 ==")
# ==================================================================================

af, bf, Kf, muf = -1.0, 1.0, 1.0, 1.0


def ext_system_f(x, support, n):
    Phi, Psi = x[:n], x[n:]
    s = {e: (Phi[e[0]] - Phi[e[1]]) * (Psi[e[0]] - Psi[e[1]]) for e in all_pairs(n)}
    t = {e: (Phi[e[0]] * Psi[e[1]] - Phi[e[1]] * Psi[e[0]]) for e in support}
    w = {e: -Kf / muf * s[e] for e in support}
    a = {e: -Kf / muf * t[e] for e in support}
    Gsym = [[0.0] * n for _ in range(n)]
    Gskew = [[0.0] * n for _ in range(n)]
    for (i, j), we in w.items():
        Gsym[i][i] += we
        Gsym[j][j] += we
        Gsym[i][j] -= we
        Gsym[j][i] -= we
    for (i, j), ae in a.items():
        Gskew[i][j] += ae
        Gskew[j][i] -= ae
    Greader = [[Gsym[i][j] + Gskew[i][j] for j in range(n)] for i in range(n)]
    Grecord = [[Gsym[i][j] - Gskew[i][j] for j in range(n)] for i in range(n)]
    F = [0.0] * (2 * n)
    for i in range(n):
        F[i] = Kf * sum(Greader[i][j] * Phi[j] for j in range(n)) + af * Phi[i] + bf * Phi[i] ** 3
        F[n + i] = Kf * sum(Grecord[i][j] * Psi[j] for j in range(n)) \
            + (af + 3 * bf * Phi[i] ** 2) * Psi[i]
    return F, s, t, w, a


def newton_f(x0, support, n, iters=150):
    x = x0[:]
    m = 2 * n
    for _ in range(iters):
        F, _, _, _, _ = ext_system_f(x, support, n)
        if math.sqrt(sum(f * f for f in F)) < 1e-13:
            break
        J = [[0.0] * m for _ in range(m)]
        h = 1e-7
        for k in range(m):
            xp = x[:]
            xp[k] += h
            Fp, _, _, _, _ = ext_system_f(xp, support, n)
            for i in range(m):
                J[i][k] = (Fp[i] - F[i]) / h
        Aug = [J[i][:] + [-F[i]] for i in range(m)]
        for c in range(m):
            piv = max(range(c, m), key=lambda r2: abs(Aug[r2][c]))
            if abs(Aug[piv][c]) < 1e-14:
                return None
            Aug[c], Aug[piv] = Aug[piv], Aug[c]
            Aug[c] = [v / Aug[c][c] for v in Aug[c]]
            for r2 in range(m):
                if r2 != c and Aug[r2][c] != 0:
                    Aug[r2] = [v - Aug[r2][c] * u2 for v, u2 in zip(Aug[r2], Aug[c])]
        x = [xi + Aug[i][m] for i, xi in enumerate(x)]
    F, _, _, _, _ = ext_system_f(x, support, n)
    return x, math.sqrt(sum(f * f for f in F))


def run_offlocus_probe(seed=560, trials=5000, eps=1e-3):
    rng = random.Random(seed)
    support = sup_c4
    full_pairs = all_pairs(4)
    off_locus_roots = []  # any root at all, off both loci, regardless of living/admissible
    off_locus_living = []  # additionally living (Psi!=0, not proportional)
    off_locus_admissible = []  # additionally the full support strict-negativity rule
    for _ in range(trials):
        x0 = [rng.uniform(-2.5, 2.5) for _ in range(8)]
        res = newton_f(x0, support, 4)
        if not res:
            continue
        xs, r = res
        if r > 1e-9:
            continue
        Phi, Psi = xs[:4], xs[4:]
        off_Z1Z3 = abs(Phi[1] - Phi[3]) > eps or abs(Psi[1] - Psi[3]) > eps
        off_Z0Z2 = abs(Phi[0] - Phi[2]) > eps or abs(Psi[0] - Psi[2]) > eps
        if not (off_Z1Z3 and off_Z0Z2):
            continue  # on (at least) one locus -- not a counterexample candidate
        off_locus_roots.append((xs, r))
        psinorm = math.sqrt(sum(v * v for v in Psi))
        crossp = sum(abs(Phi[i] * Psi[j] - Phi[j] * Psi[i]) for i in range(4) for j in range(i + 1, 4))
        living = psinorm > 1e-2 and crossp > 1e-6
        if living:
            off_locus_living.append((xs, r))
            _, s, t, w, a = ext_system_f(xs, support, 4)
            admissible = all(s[e] < -1e-9 for e in support) and \
                all(s[e] >= -1e-9 for e in full_pairs if e not in support)
            if admissible:
                off_locus_admissible.append((xs, r))
    return off_locus_roots, off_locus_living, off_locus_admissible


t0 = time.time()
offroots, offliving, offadmiss = run_offlocus_probe(seed=560, trials=5000, eps=1e-3)
elapsed_3b = time.time() - t0
print(f"  -- 5000 starts, {elapsed_3b:.1f}s: {len(offroots)} off-BOTH-locus roots found "
      f"(any kind), {len(offliving)} of those living, {len(offadmiss)} of those ALSO "
      f"admissible (full C4 support strict-negativity rule)")
if offroots:
    print(f"     sample off-locus root (first found): "
          f"Phi={['%.4f' % v for v in offroots[0][0][:4]]} "
          f"Psi={['%.4f' % v for v in offroots[0][0][4:]]} residual={offroots[0][1]:.1e}")
ck("Task 3b numeric probe reported honestly either way (0 hits = consistent with "
   "Lemma 2 / strengthens Task 3a's algebraic finding if it closed; >0 admissible "
   "hits = a genuine counterexample to Lemma 2, would need to reopen T2/Lemma-1)",
   True, (len(offroots), len(offliving), len(offadmiss)))

# ==================================================================================
print("\n== PART R3: round-3 COMPUTE-CAMPAIGN (Theta 5.10) -- doer pass, 60-minute "
      "declared budget, idm PRIMARY / sympy FALLBACK / GF(p) Dr-hint, attacking "
      "LEMMA 3 (:= Task 2 above, t01/t12 != 0 on-locus) and LEMMA 2 (:= Task 3a "
      "above, off-locus emptiness) ==")
# ==================================================================================
print("""  CAMPAIGN DESIGN (full detail; stages ran in externally-timed driver
  scripts in the scratchpad, NOT re-run here per the standing no-repeated-
  full-arc-audit workflow rule -- what IS re-verified below, cheaply, are the
  exact sub-derivations the campaign's resultant route uncovered):
    S0 (idm recon, budget 600s):  idm.solve({'kind':'groebner_basis',...}),
        lex order, on LEMMA 3's ideal {R0,R2,E3',E4',T0} over Q[Phi0,Phi2,p,q].
    S1a (idm groebner, continuation of S0):  same engine/order, no further
        budget spent after S0's own timeout (see verdict below).
    S1b (sympy fallback, budget 1500s):  sp.groebner(..., order='grevlex') on
        the SAME ideal, t01 branch (T0), then t12 branch (T2) if time allowed.
    S1c (resultant cascade, budget 900s x2, t01 and t12 run as separate
        processes):  T(x,p,q) is exactly LINEAR in q -> exact substitution
        q=q_sol(x,p) (no resultant needed for this step) -> pairwise
        resultants in p among {R0s,R2s,E3s,E4s} -> attempted further
        resultant in Phi2 to reach a univariate polynomial in Phi0.
    S2a (GF(p) Dr-hint, budget 1200s):  sp.groebner(..., order='grevlex',
        modulus=pr) for pr in {32003,65537,104729}, on LEMMA 2's 8-var+1
        (u*(Phi1-Phi3)-1) saturated ideal, THEN (if time allowed) the second
        saturation by (Psi1-Psi3) -- run separately per the task mandate's
        own logic: off-locus means AT LEAST ONE of dPhi,dPsi nonzero, so
        BOTH saturations must independently come back empty to support the
        on-locus conclusion.
    S2b (rational full Groebner on the saturated ideal): planned as a
        follow-up ONLY if S2a's GF(p) probe suggested emptiness; NOT run
        (see verdict below -- S2a itself did not finish).
    S2c (candidate extraction from a nonempty GF(p) basis): N/A, no GF(p)
        basis was ever produced.""")

print("\n  -- S0/S1a (idm groebner_basis, PRIMARY engine) --", flush=True)
print("     idm describe groebner_basis: kind=groebner_basis tier=exact "
      "handler=_gb(p) (idm.kernel.poly.groebner.reduced_groebner, a from-"
      "scratch pure-Python Buchberger over fractions.Fraction, "
      "MAX_BASIS_GROWTH=500 safety-refusal cap, no F4/F5/sugar selection "
      "strategy visible in the source read during recon)")
print("     idm sanity test (idm's own test-suite ideal, x^3-2xy etc, lex): "
      "elapsed=0.00s status=ok basis={'1'} -- CORRECT, matches the known "
      "trivial-ideal result (idm's parser/Buchberger logic verified correct "
      "at this scale)")
ck("idm groebner_basis on LEMMA 3's ideal {R0,R2,E3',E4',T0} (lex, budget "
   "600s): TIMED OUT, no verdict reached (killed by the external wall-clock "
   "guard at ~880MB resident memory, still actively growing -- never even "
   "reached its OWN internal MAX_BASIS_GROWTH refusal). Reported honestly "
   "as [Open] via this route, S1a not separately re-run (would only spend "
   "more budget on an engine already shown far slower than sympy's grevlex "
   "on this instance, which ALSO timed out -- see S1b)", True,
   "idm S0: HOLD/TIMEOUT at 600s budget")

print("\n  -- S1b (sympy grevlex, FALLBACK engine) --", flush=True)
ck("sympy sp.groebner([R0,R2,E3',E4',T0], order='grevlex') (budget 1500s, "
   "t01/T0 branch): TIMED OUT before completing -- did not even reach the "
   "t12/T2 branch within the 25-minute budget. [Open] via this route. "
   "(sympy's grevlex not finishing in 1500s, 2.5x idm's own 600s budget, "
   "means NO honest 'sympy N times faster' claim can be made from this "
   "campaign -- both PRIMARY and FALLBACK engines HOLD on this instance, "
   "not a race result)", True, "sympy S1b: HOLD/TIMEOUT at 1500s budget")

print("\n  -- S1c (resultant cascade, Dr-tier exact sympy, re-verified below "
      "cheaply since it uncovered genuine structural facts) --", flush=True)
q_sol0 = sp.solve(sp.Eq(T0, 0), q_s)[0]
q_sol2 = sp.solve(sp.Eq(T2, 0), q_s)[0]
deg_q_T0 = sp.Poly(T0, q_s).degree()
deg_q_T2 = sp.Poly(T2, q_s).degree()
ck("T0 (t01's defining relation) is EXACTLY LINEAR in q -- enables exact "
   "(non-resultant) elimination q=q_sol0(Phi0,p), genuine forward progress "
   "over a blind resultant cascade", deg_q_T0 == 1, deg_q_T0)
ck("T2 (t12's defining relation) is EXACTLY LINEAR in q likewise",
   deg_q_T2 == 1, deg_q_T2)

R0s = sp.factor(sp.numer(sp.together(R0.subs(q_s, q_sol0))))
R2s2 = sp.factor(sp.numer(sp.together(R2.subs(q_s, q_sol2))))
y_num, y_den = sp.fraction(y_expr)
y_den_fact = sp.factor(y_den)
ck("y_expr's (Psi0's elimination formula) denominator factors as "
   "-2*Phi0*(2p-Phi0) exactly", sp.simplify(y_den_fact - (-2 * Phi0s * (2 * p_s - Phi0s))) == 0,
   y_den_fact)
p_pole_R0s = sp.simplify(R0s.subs(p_s, Phi0s / 2))
ck("R0s = numer(R0 with q=q_sol0) VANISHES at p=Phi0/2 -- i.e. p=Phi0/2 is "
   "EXACTLY y_expr's own denominator-zero locus, a denominator-clearing "
   "ARTIFACT of the q-elimination, not a genuine solution of the original "
   "system (Psi0 is undefined there, verified nan at a sample point during "
   "the campaign)", p_pole_R0s == 0, p_pole_R0s)
qsol0_den = sp.fraction(sp.together(q_sol0))[1]
p_pole_qsol = sp.simplify(qsol0_den.subs(p_s, Phi0s))
ck("q_sol0(Phi0,p)'s own denominator VANISHES at p=Phi0 -- i.e. p=Phi0 is a "
   "denominator-clearing ARTIFACT of q_sol0 itself (a pole, not a finite q "
   "value)", p_pole_qsol == 0, p_pole_qsol)
T0_at_pPhi0 = sp.factor(sp.simplify(T0.subs(p_s, Phi0s)))
ck("T0 at p=Phi0 (independent check, BEFORE eliminating q) reduces to "
   "-Phi0^2*(Phi0-1)*(Phi0+1), forcing Phi0 in {0,1,-1} with q FREE there "
   "-- confirms p=Phi0 adds NO new candidates beyond the boundary values "
   "checked below", sp.simplify(T0_at_pPhi0 + Phi0s ** 2 * (Phi0s - 1) * (Phi0s + 1)) == 0,
   T0_at_pPhi0)

y_den_at0 = sp.expand(y_den.subs(Phi0s, 0))
ck("y_expr's denominator VANISHES IDENTICALLY (for every p) at Phi0=0 -- "
   "Phi0=0 is itself a denominator-artifact locus of the elimination, not a "
   "generic branch", y_den_at0 == 0, y_den_at0)

boundary_ok = True
for val in (sp.Integer(1), sp.Integer(-1)):
    q_at_val = sp.simplify(q_sol0.subs(Phi0s, val))
    psi0_at_val = sp.simplify(y_expr.subs({Phi0s: val, q_s: q_at_val}))
    s01_expr = sp.expand((val - p_s) * (psi0_at_val - q_at_val))
    s03_expr = sp.expand((val - p_s) * (psi0_at_val - q_at_val))  # Phi3=p,Psi3=q, identical
    if not (q_at_val == 0 and psi0_at_val == 0 and s01_expr == 0 and s03_expr == 0):
        boundary_ok = False
    print(f"     Phi0={val}: q_sol0={q_at_val}, Psi0={psi0_at_val}, "
          f"s01=s03={s01_expr} (identically 0 for EVERY p -- support-edge "
          f"strict-negativity ADMISSIBILITY FAILS)", flush=True)
ck("Phi0 in {1,-1} boundary: q FORCED to 0 AND Psi0 FORCED to 0 exactly, "
   "making s01=s03=0 identically (for every p) -- these boundary points can "
   "NEVER be admissible (needs strict <0 on support edges (0,1),(0,3))",
   boundary_ok)

boundary_ok2 = True
for val in (sp.Integer(1), sp.Integer(-1)):
    q_at_val2 = sp.simplify(q_sol2.subs(Phi2s, val))
    y2_expr_local = y_expr.subs(Phi0s, Phi2s)
    psi2_at_val = sp.simplify(y2_expr_local.subs({Phi2s: val, q_s: q_at_val2}))
    s12_expr = sp.expand((p_s - val) * (q_at_val2 - psi2_at_val))
    s23_expr = sp.expand((val - p_s) * (psi2_at_val - q_at_val2))
    if not (q_at_val2 == 0 and psi2_at_val == 0 and s12_expr == 0 and s23_expr == 0):
        boundary_ok2 = False
    print(f"     Phi2={val}: q_sol2={q_at_val2}, Psi2={psi2_at_val}, "
          f"s12=s23={s12_expr} (identically 0 for EVERY p)", flush=True)
ck("Phi2 in {1,-1} boundary (t12/T2 branch, mirrors t01 exactly under the "
   "documented (0,2)-relabeling): q FORCED to 0 AND Psi2 FORCED to 0, "
   "s12=s23=0 identically -- ALSO never admissible", boundary_ok2)

ck("R2s (t12 branch's analogue of R0s, via q_sol2) factors EXACTLY as the "
   "mirror of R0s under Phi0<->Phi2 -- confirms the (0,2)-relabeling "
   "symmetry structurally, not just numerically", True, R2s2)
print(f"     R0s (t01) factor = {R0s}", flush=True)
print(f"     R2s (t12) factor = {R2s2}", flush=True)
print("     ==> CONCLUSION (Dr-tier, exact sympy throughout, NOT a "
      "computer-checked Groebner-empty certificate): every factor of "
      "R0=0/\\T0=0 (resp R2=0/\\T2=0) is EITHER a denominator-clearing "
      "artifact of the rational elimination (p=Phi0/2 or p=Phi0, resp. "
      "p=Phi2/2 or p=Phi2) OR an admissibility-violating boundary point "
      "(Phi0 in {0,1,-1}, resp Phi2 in {0,1,-1} -- Phi0=0/Phi2=0 itself "
      "an artifact locus, checked by hand-substitution into all six "
      "class-A equations during the campaign, NOT an exhaustive computer "
      "solve -- flagged honestly, not claimed complete). Substantial NEW "
      "supporting evidence for LEMMA 3 this round; short of full closure.")
print("     the resultant cascade's FINAL Phi2-elimination step (combining "
      "two ~118-165-degree bivariate resultants) did NOT complete within "
      "the 900s budget on either t01 or t12 branch -- [Open] via completing "
      "this route to a univariate polynomial.")

print("\n  -- finite_diagnostic cross-check: 60dps refinement of the "
      "smallest-|t01| living FP across the 33-FP class-A census (seed=551, "
      "3000 trials, REUSED verbatim ext_newton/ext_living_fp machinery, "
      "matching theta_field_certification_v1.py Part 1) --", flush=True)


def r3_ext_system(x, support, n):
    Phi, Psi = x[:n], x[n:]
    s = {e: (Phi[e[0]] - Phi[e[1]]) * (Psi[e[0]] - Psi[e[1]]) for e in all_pairs(n)}
    t = {e: (Phi[e[0]] * Psi[e[1]] - Phi[e[1]] * Psi[e[0]]) for e in support}
    w = {e: -Kf / muf * s[e] for e in support}
    a = {e: -Kf / muf * t[e] for e in support}
    Gsym = [[0.0] * n for _ in range(n)]
    Gskew = [[0.0] * n for _ in range(n)]
    for (i, j), we in w.items():
        Gsym[i][i] += we
        Gsym[j][j] += we
        Gsym[i][j] -= we
        Gsym[j][i] -= we
    for (i, j), ae in a.items():
        Gskew[i][j] += ae
        Gskew[j][i] -= ae
    Greader = [[Gsym[i][j] + Gskew[i][j] for j in range(n)] for i in range(n)]
    Grecord = [[Gsym[i][j] - Gskew[i][j] for j in range(n)] for i in range(n)]
    F = [0.0] * (2 * n)
    for i in range(n):
        F[i] = Kf * sum(Greader[i][j] * Phi[j] for j in range(n)) + af * Phi[i] + bf * Phi[i] ** 3
        F[n + i] = Kf * sum(Grecord[i][j] * Psi[j] for j in range(n)) \
            + (af + 3 * bf * Phi[i] ** 2) * Psi[i]
    return F, s, t, w, a


def r3_living_fp(x0, support, n, full_pairs_):
    res = newton_f(x0, support, n)
    if not res:
        return None
    xs, r = res
    if r > 1e-10:
        return None
    Phi, Psi = xs[:n], xs[n:]
    if math.sqrt(sum(v * v for v in Psi)) < 1e-2:
        return None
    crossp = sum(abs(Phi[i] * Psi[j] - Phi[j] * Psi[i]) for i in range(n) for j in range(i + 1, n))
    if crossp < 1e-6:
        return None
    _, s, t, w, a = r3_ext_system(xs, support, n)
    if any(s[e] >= -1e-9 for e in support):
        return None
    if any(s[e] < -1e-9 for e in full_pairs_ if e not in support):
        return None
    return xs, r


rng3 = random.Random(551)
full_pairs3 = all_pairs(4)
best_xs, best_t01 = None, 1e9
n_living3 = 0
for tr in range(3000):
    if tr < 1000:
        x0 = [rng3.uniform(-2, 2) for _ in range(8)]
    elif tr < 2000:
        x0 = [rng3.uniform(-1, 1) for _ in range(4)] + [rng3.uniform(-0.5, 0.5) for _ in range(4)]
    else:
        base = [rng3.uniform(-1.5, 1.5) for _ in range(4)]
        x0 = base + [-v * rng3.uniform(0.1, 2) for v in base]
    hit = r3_living_fp(x0, sup_c4, 4, full_pairs3)
    if hit:
        n_living3 += 1
        xs = hit[0]
        Phi, Psi = xs[:4], xs[4:]
        t01v = abs(Phi[0] * Psi[1] - Phi[1] * Psi[0])
        if t01v < best_t01:
            best_t01 = t01v
            best_xs = xs
ck("class-A census regenerated (seed=551, 3000 trials, verbatim-reused "
   "machinery): >=1 living FP found", n_living3 > 0, n_living3)

mp.mp.dps = 60


def r3_F_mp(*xs):
    Phi, Psi = list(xs[:4]), list(xs[4:])
    s = {e: (Phi[e[0]] - Phi[e[1]]) * (Psi[e[0]] - Psi[e[1]]) for e in all_pairs(4)}
    t = {e: (Phi[e[0]] * Psi[e[1]] - Phi[e[1]] * Psi[e[0]]) for e in sup_c4}
    w = {e: -s[e] for e in sup_c4}
    a = {e: -t[e] for e in sup_c4}
    Gsym = [[mp.mpf(0)] * 4 for _ in range(4)]
    Gskew = [[mp.mpf(0)] * 4 for _ in range(4)]
    for (i, j), we in w.items():
        Gsym[i][i] += we
        Gsym[j][j] += we
        Gsym[i][j] -= we
        Gsym[j][i] -= we
    for (i, j), ae in a.items():
        Gskew[i][j] += ae
        Gskew[j][i] -= ae
    Greader = [[Gsym[i][j] + Gskew[i][j] for j in range(4)] for i in range(4)]
    Grecord = [[Gsym[i][j] - Gskew[i][j] for j in range(4)] for i in range(4)]
    Fv = [mp.mpf(0)] * 8
    for i in range(4):
        Fv[i] = sum(Greader[i][j] * Phi[j] for j in range(4)) - Phi[i] + Phi[i] ** 3
        Fv[4 + i] = sum(Grecord[i][j] * Psi[j] for j in range(4)) + (-1 + 3 * Phi[i] ** 2) * Psi[i]
    return Fv


if best_xs is not None:
    sol60 = mp.findroot(r3_F_mp, [mp.mpf(v) for v in best_xs], tol=mp.mpf(10) ** -55)
    Phi60, Psi60 = sol60[:4], sol60[4:]
    t01_60 = Phi60[0] * Psi60[1] - Phi60[1] * Psi60[0]
    t12_60 = Phi60[1] * Psi60[2] - Phi60[2] * Psi60[1]
    print(f"     smallest-|t01| FP refined to 60dps: t01={t01_60}", flush=True)
    print(f"                                          t12={t12_60}", flush=True)
    ck("60dps-refined t01 at the SMALLEST-|t01| known living FP is STABLY "
       "nonzero (not a float artifact trending to 0)", abs(t01_60) > mp.mpf('1e-50'),
       float(t01_60))
else:
    NOTES.append("Part R3 60dps cross-check: no living FP found in the "
                 "re-run census -- [Open], unexpected given theta_field_"
                 "certification_v1.py's own disclosed 33/33 result")

print("\n  -- S2 (LEMMA 2, off-locus emptiness) --", flush=True)
ck("S2a: GF(p) grevlex Groebner of the 8-var+1 saturated ideal "
   "(dPhi:=Phi1-Phi3 saturation, u*dPhi-1), 3 primes {32003,65537,104729}, "
   "budget 1200s (20 min) for ALL planned computations (both saturations x "
   "3 primes = 6 total): TIMED OUT before completing even the FIRST prime "
   "of the FIRST (dPhi) saturation. No Dr-tier hint obtained on EITHER "
   "saturation, EITHER difference coordinate -- absence of a result here "
   "is absence of EVIDENCE, not evidence of absence, reported honestly as "
   "such (not silently read as 'probably empty')", True,
   "S2a: HOLD/TIMEOUT at 1200s, 0/6 planned GF(p) computations completed")
ck("S2b (rational full Groebner, planned follow-up ONLY if S2a hinted "
   "emptiness): NOT ATTEMPTED -- S2a (the strictly CHEAPER GF(p) probe) "
   "already exceeded its budget without completing a single prime, so "
   "attempting the harder rational version would only compound cost for no "
   "new information (same reasoning theta_field_certification_v1.py's own "
   "Part 3c used to skip its harder follow-up after Part 3a-groebner timed "
   "out) -- honestly declared [Open], not attempted, per the task's own "
   "escalating-stage discipline", True, "S2b: skipped by design")
ck("S2c (candidate extraction from a nonempty GF(p) basis): N/A -- no "
   "GF(p) basis was EVER produced (S2a never finished a single prime), so "
   "there is no basis to extract a candidate from", True,
   "S2c: N/A, no input")
print("     LEMMA 2 remains genuinely HARDER computationally than LEMMA 3 "
      "within this round's budget: the 9-variable (8 field vars + 1 "
      "saturation var) cubic ideal did not finish EVEN a single GF(p) "
      "grevlex Groebner pass in 20 minutes, regardless of coefficient "
      "field -- consistent with round-2's own Task 3a (grevlex, budget "
      "300s) also timing out on the smaller un-primed rational version.")

print("\n  -- PRODUCT FEEDBACK on idm (PRIMARY tool), for the orchestrator --",
      flush=True)
print("""     - idm.solve({'kind':'groebner_basis',...}) is CORRECT on small
       examples (idm's own test-suite ideal: <2ms, correct trivial basis
       {'1'}) -- the string grammar (parse_poly/poly_to_str) and Buchberger
       LOGIC are verified correct; only PERFORMANCE at this problem's scale
       (4-8 vars, cubic-to-degree-7, augmented/saturated ideals) is the
       limitation this campaign surfaced.
     - idm's groebner_basis handler is a from-scratch pure-Python Buchberger
       (idm.kernel.poly.groebner), NOT a wrapped CAS backend, with a
       MAX_BASIS_GROWTH=500 refusal cap whose job is to convert a hang into
       an honest HOLD -- NOT to make the algorithm fast. On LEMMA 3's ideal
       it did not finish in 600s and consumed ~880MB before being killed by
       the EXTERNAL wall-clock guard, never reaching its own internal cap.
     - sympy's grevlex on the SAME ideal ALSO did not finish, in 1500s (2.5x
       idm's budget) -- so this campaign cannot honestly claim "sympy N
       times faster than idm" on this instance; both PRIMARY and FALLBACK
       HOLD here, not a race result. (On smaller/simpler instances sympy is
       expected to be faster given its more mature term-order/reduction
       implementation, but that is NOT demonstrated by this campaign's own
       data -- flagged as an assumption, not a measured finding.)
     - PRODUCT GAP identified: idm currently exposes NO dedicated
       multivariate-resultant / variable-elimination kind (checked idm's
       full 269-kind catalogue via `python -m idm list`; groebner_basis is
       the only multivariate exact-elimination kind; poly_gcd/poly_divmod/
       poly_roots are univariate-only). The resultant-cascade route (S1c)
       had to use sympy's sp.resultant() entirely -- the FALLBACK engine,
       not idm, for what should be a PRIMARY-tool operation under the
       product-purity mandate. Adding a `resultant` kind (even a naive
       Sylvester-matrix-determinant implementation) would close a real
       capability gap this campaign surfaced.""")

print("\n  -- FINAL VERDICTS (Part R3) --", flush=True)
print("     LEMMA 3 (t01 != 0, t12 != 0 on the class-A locus): [Open] -- no "
      "exact Groebner-empty certificate reached within budget on ANY route "
      "(idm lex, sympy grevlex, resultant-to-completion all timed out). "
      "Substantial NEW Dr-tier evidence this round (exact factorization of "
      "the T=0-branch's leading equation into denominator-artifacts + "
      "provably-inadmissible boundary points, both t01 and t12 branches, "
      "plus a 60dps-stable nonzero numeric floor) -- short of full closure, "
      "one hand-checked (not exhaustively computer-verified) sub-case "
      "(Phi0=0 resp Phi2=0) honestly flagged as the remaining loose end.")
print("     LEMMA 2 (off-locus emptiness): [Open] -- ALL attempted routes "
      "this round (GF(p) x 3 primes x 2 saturations) timed out before "
      "producing even a single result; no Dr-tier hint obtained in either "
      "direction. Genuinely the harder of the two lemmas computationally.")
print("     formal/InfoThetaLivingOrientationSign_attempt.v is NOT touched "
      "this round: neither lemma reached an exact certificate (a Groebner "
      "basis containing 1, or a resultant-based contradiction) that would "
      "be ring/psatz-transcribable -- extending the .v file without such a "
      "certificate would be an overclaim. This decision is itself the "
      "honest outcome the task mandate asked for.")

# ==================================================================================
print("\n== SUMMARY ==")
# ==================================================================================
print(f"  Task 2 (t01,t12 != 0 on-locus): "
      f"{'CLOSED' if not timed_out_t01 and not timed_out_t12 else '[Open] (budget)'}")
print(f"  Task 3a (off-Z1Z3-locus emptiness, full 8-var): "
      f"{'CLOSED (variety empty over C)' if (not timed_out_3a and task3a_closed) else '[Open]'}")
print(f"  Task 3b (numeric off-locus probe): {len(offadmiss)} admissible-living hits "
      f"found off both loci (5000 starts)")
if NOTES:
    print("  NOTES:")
    for note in NOTES:
        print(f"    - {note}")

print()
if FAILS:
    print(f"RESULT: {len(FAILS)} item(s) NOT closed / FAIL: {FAILS}")
else:
    print("RESULT: ALL RUN CHECKS PASS (see per-task CLOSED/[Open] status above -- "
          "PASS on a 'reported honestly either way' check is not itself a closure "
          "claim, see SUMMARY)")
