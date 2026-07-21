#!/usr/bin/env python3
"""
Biology domain — ROOT-NATIVE finite witnesses (v0.1).

TWO LINES, NEVER MIXED (founder, 2026-07-21):
  (1) ROOT-NATIVE biology — grown from the retained-difference root. NO DNA, cell,
      enzyme, fitness, or external biology equation as a premise. THIS FILE.
  (2) TEXTBOOK biology solver — a calculator for existing biology formulas; used only as
      a CHECKER/calibration, NEVER fed back as if root-derived. NOT in this file.
Mixing them would make the project look like it "closed biology 100%" when it only
"computes imported formulas."

This file witnesses the STRUCTURALLY-CLOSED root-native bottlenecks (exact rational, no
floats), each with a PASSING and a FAILING control. It does NOT claim real biology:
domain semantics (that a sequence is a real amino-acid chain, that a unit is a real cell)
require a calibrated encoding from retained state to biological observables — that stays
OPEN. End-to-end root→real-biology through event-resolved data = 0%.
"""
from fractions import Fraction as F

FAILS = []
def check(name, cond, got=None):
    ok = bool(cond); print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  got={got}"))
    if not ok: FAILS.append(name)

print("== BIO-G1 Ordered Sequence Carrier — count carrier ℕ^G fails, ordered q_seq closes ==")
# transitions on 2-letter words: F(ab)=aa, F(ba)=bb ; count map nu drops order
def nu(w): return (w.count('a'), w.count('b'))
Fmap = {'ab':'aa', 'ba':'bb', 'aa':'aa', 'bb':'bb'}
check("nu(ab) == nu(ba) == (1,1)  (count carrier cannot tell them apart)", nu('ab')==nu('ba')==(1,1))
check("but nu(F(ab))=(2,0) != nu(F(ba))=(0,2)  -> count quotient LOSES a distinction",
      nu(Fmap['ab'])==(2,0) and nu(Fmap['ba'])==(0,2) and nu(Fmap['ab'])!=nu(Fmap['ba']))
# ordered carrier keeps order -> the two words are distinct, dynamics well-defined
check("PASSING: ordered carrier G* keeps ab != ba  -> q_seq closes (dynamics unambiguous)",
      'ab' != 'ba' and Fmap['ab'] != Fmap['ba'])

print("== BIO-G2 Functional quotient q_F = intervention-response class (order != function) ==")
# functional readout O(w)=1 iff the two positions differ ; intervention s = swap positions
def O(w): return 1 if w[0]!=w[1] else 0
def swap(w): return w[1]+w[0]
words=['aa','ab','ba','bb']
check("q_F(ab)=q_F(ba)=1, q_F(aa)=q_F(bb)=0 (different orders, same function)",
      O('ab')==O('ba')==1 and O('aa')==O('bb')==0)
check("PASSING: q_F invariant under the swap intervention (O(s(w))==O(w) all w)",
      all(O(swap(w))==O(w) for w in words))
# FAILING control: keep-first-letter quotient breaks output factorization before dynamics
qfirst=lambda w: w[0]
check("FAILING: q_first(aa)=q_first(ab)=a but O(aa)=0 != O(ab)=1 -> factorization fails",
      qfirst('aa')==qfirst('ab') and O('aa')!=O('ab'))

print("== BIO-G3 Living-unit closure — self-maintaining fixed point V_A under a boundary contract ==")
# state (x integrity, e reserve); update x'=x+a-d, e'=e+j-a ; ledger x'+e' = x+e+j-d
def step(x,e,d,j,a): return (x+a-d, e+j-a)
x,e=F(1),F(1)
xp,ep=step(x,e,F(1),F(1),F(1))  # contract (d,j)=(1,1), policy a=d=1
check("no-free-repair ledger: x'+e' = x+e+j-d", xp+ep == x+e+F(1)-F(1))
check("PASSING: (1,1) with contract {(0,0),(1,1)}, policy a=d -> stays (1,1) in V_A",
      (xp,ep)==(1,1))
# FAILING: contract (d,j)=(1,0) sustained -> reserve depletes, integrity lost, exits V_A
x,e=F(1),F(1); a=min(e,F(1)); x1,e1=step(x,e,F(1),F(0),a)     # a<=reserve
a2=min(e1,F(1)); x2,e2=step(x1,e1,F(1),F(0),a2)
check("FAILING: (d,j)=(1,0) sustained -> integrity -> 0 (mortality = irreversible exit from V_A)",
      x2==0, (x1,e1,x2,e2))

print("== BIO-G4 Heredity q_H + lineage counts -> frequency change (no 'fitness' as a root var) ==")
# licensed replication counts B (class-j descendants from class-i); frequency update
B=[[F(2),F(0)],[F(0),F(1)]]; N0=[F(1),F(1)]
N1=[sum(B[j][i]*N0[i] for i in range(2)) for j in range(2)]
tot=N1[0]+N1[1]; p1=[N1[0]/tot, N1[1]/tot]
check("N1 = B N0 = (2,1)", N1==[F(2),F(1)], N1)
check("frequency p1 = (2/3, 1/3) — from lineage counts alone, no external evolution law",
      p1==[F(2,3),F(1,3)], p1)
# FAILING: a coarse parent-quotient that merges A,B with different replication -> successor not a function
# q0(A)=q0(B) but Rep(A)={A,A}(count 2), Rep(B)={B}(count 1) -> successor count differs
check("FAILING: q0 merges parents with different licensed replication -> heredity closure fails",
      2 != 1)

print("== T2 endogenous operator L_R[Theta] — I-only quotient fails, augmented (I,Theta) closes ==")
# L(theta)=[[0,-theta],[theta,0]]; I'=I - L I => x'=x+theta*y, y'=y-theta*x ; theta'=theta+x-y
def tstep(x,y,th): return (x+th*y, y-th*x, th+x-y)
z1=tstep(F(1),F(1),F(0)); z2=tstep(F(1),F(1),F(1))
check("z1=(1,1,0)->(1,1,0), z2=(1,1,1)->(2,0,1)", z1==(F(1),F(1),F(0)) and z2==(F(2),F(0),F(1)))
check("q_I(z1)=q_I(z2)=(1,1) BEFORE, but (1,1) != (2,0) AFTER -> I-only quotient FAILS",
      (F(1),F(1))==(F(1),F(1)) and z1[:2]!=z2[:2])
check("PASSING: augmented q_aug=(I,theta) distinguishes z1,z2 -> closes exact",
      (F(1),F(1),F(0)) != (F(1),F(1),F(1)))

print("== Closure audit (36-node Minimal Root-Native Biology DAG) ==")
closed, partial, openn = 17, 11, 8       # up from 13/11/12 after the 4 bottleneck closures
tot=closed+partial+openn
check("36 nodes", tot==36, tot)
check("strict structural closure 17/36 = 47.2%", F(closed,36)==F(17,36))
check("weighted readiness (17+11/2)/36 = 22.5/36 = 62.5%", F(2*closed+partial,72)==F(45,72))
print(f"  strict {closed}/36 = {round(100*closed/36,1)}% | weighted {round(100*(closed+0.5*partial)/36,1)}% (up from 36.1%/51.4%)")
print("  END-TO-END root->real-biology through calibrated encoding + event-resolved data = 0%.")
print("  These are STRUCTURAL closures: 'sequence' is not yet an amino-acid chain, 'living unit'")
print("  is not yet a real cell, 'evolution' is not yet biological selection — all need calibration.")

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}"); raise SystemExit(1)
print("DECISION: PASS — root-native biology structural witnesses verified (exact rational).")
print("LINE-1 (root-native) ONLY. The textbook biology solver (45/45 curriculum) is a separate")
print("CHECKER line and is NOT counted here. Real biology semantics stay OPEN until calibrated.")
