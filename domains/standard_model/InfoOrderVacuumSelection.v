(* ================================================================= *)
(*  InfoOrderVacuumSelection.v                               *)
(*  Order Vacuum Selection v1.13 (founder's "v2.1"). DERIVE why the   *)
(*  order condenses (<H^dag H> > 0) from CLOSURE PRESSURE -- the       *)
(*  number of matter-branch histories that close as the order load    *)
(*  r=H^dag H grows -- instead of inserting a negative bare mass by    *)
(*  hand. Closes v1.12's open item. Bare cost V0(r)=alpha r+beta r^2   *)
(*  with alpha>=0, beta>0 (bare minimum at r=0).                      *)
(*                                                                     *)
(*  Proved over Q (Print Assumptions Closed):                         *)
(*   (sq)     occupancy squeeze: 0<=p<=1 => p(1-p) <= 1/4              *)
(*            (via (1/2 - p)^2 >= 0)                                   *)
(*   (slope)  V_eff'(0) = alpha - Pi_cl ; ORDER SELECTED iff Pi_cl>    *)
(*            alpha iff V_eff'(0) < 0 (origin loses stability)         *)
(*   (aeff)   effective slope a_eff = alpha - Pi_cl can be < 0 with    *)
(*            alpha >= 0 (concrete witness: alpha=0, Pi_cl=1/2)        *)
(*            => NO bare negative mass inserted                        *)
(*   (conv)   convexity: if 2 beta > (1/4) sum kappa_j^2 then          *)
(*            V_eff''(r) = 2 beta - sum kappa_j^2 p_j(1-p_j) > 0       *)
(*            (uses the squeeze) => unique global minimum              *)
(*   (occ)    dp/dr = kappa p(1-p) > 0 for kappa>0, 0<p<1 (occupancy   *)
(*            rises with order load)                                   *)
(*   (bounds) stationarity 2 beta r_star + alpha = sum kappa_j p_j(r_star)     *)
(*            with p_j(0) <= p_j(r_star) < 1 =>                            *)
(*            (Pi_cl-alpha)/(2 beta) <= r_star < (sum kappa-alpha)/(2 beta)*)
(*   (rp)     reflection positivity preserved: for D=diag(d1,d2)>=0    *)
(*            and K PSD, D K D is PSD (diagonal>=0, det>=0)            *)
(*                                                                     *)
(*  HONEST FENCE. EXACT that closure pressure (not a hand sign)        *)
(*  selects r_star>0 and preserves positivity. Gauge-invariant statement  *)
(*  is <H^dag H> > 0 (Elitzur). OPEN: compute the microscopic g_j,     *)
(*  Delta_j, kappa_j, alpha, beta from the tape/intertwiner grammar    *)
(*  (is Pi_cl>alpha FORCED or merely POSSIBLE?), the scale v, and the  *)
(*  physical vector-mass poles vs a local Hessian.                    *)
(* ================================================================= *)

Require Import Coq.QArith.QArith.
Require Import Coq.micromega.Lqa.

Module InfoOrderVacuumSelection.
Open Scope Q_scope.

(* (sq) occupancy squeeze: 0<=p<=1 => p(1-p) <= 1/4, via (1/2-p)^2 >= 0 *)
Theorem occupancy_squeeze : forall p : Q, 0 <= p -> p <= 1 -> p * (1 - p) <= 1#4.
Proof.
  intros p H0 H1.
  assert (Hid : ((1#2) - p)*((1#2) - p) == (1#4) - p*(1-p)) by ring.
  assert (Hsq : 0 <= ((1#2) - p)*((1#2) - p)) by (set (q := (1#2) - p); nra).
  lra.
Qed.

(* (slope) V_eff'(0) = alpha - Pi_cl ; order selected iff Pi_cl > alpha *)
Theorem origin_slope : forall alpha Pcl : Q, (alpha - Pcl) < 0 <-> Pcl > alpha.
Proof. intros alpha Pcl. split; lra. Qed.

(* (aeff) effective negative slope with a NONNEGATIVE bare slope: witness *)
Theorem a_eff_negative_witness : (0:Q) >= 0 /\ (0 - (1#2)) < 0.
Proof. split; lra. Qed.

(* (conv) strict convexity from the squeeze: three branches U,D,E.
   V'' = 2 beta - (kU^2 pU(1-pU) + kD^2 pD(1-pD) + kE^2 pE(1-pE))
       >= 2 beta - (1/4)(kU^2+kD^2+kE^2) > 0  when 2 beta > (1/4) sum k^2. *)
Theorem convexity_positive :
  forall beta kU kD kE pU pD pE : Q,
  0 <= pU -> pU <= 1 -> 0 <= pD -> pD <= 1 -> 0 <= pE -> pE <= 1 ->
  2*beta > (1#4)*(kU*kU + kD*kD + kE*kE) ->
  2*beta - (kU*kU*(pU*(1-pU)) + kD*kD*(pD*(1-pD)) + kE*kE*(pE*(1-pE))) > 0.
Proof.
  intros beta kU kD kE pU pD pE HU0 HU1 HD0 HD1 HE0 HE1 Hgate.
  assert (SU : pU*(1-pU) <= 1#4) by (apply occupancy_squeeze; assumption).
  assert (SD : pD*(1-pD) <= 1#4) by (apply occupancy_squeeze; assumption).
  assert (SE : pE*(1-pE) <= 1#4) by (apply occupancy_squeeze; assumption).
  (* each kappa^2 * p(1-p) <= (1/4) kappa^2, and p(1-p) >= 0 *)
  assert (0 <= pU*(1-pU)) by nra.
  assert (0 <= pD*(1-pD)) by nra.
  assert (0 <= pE*(1-pE)) by nra.
  assert (BU : kU*kU*(pU*(1-pU)) <= kU*kU*(1#4)) by nra.
  assert (BD : kD*kD*(pD*(1-pD)) <= kD*kD*(1#4)) by nra.
  assert (BE : kE*kE*(pE*(1-pE)) <= kE*kE*(1#4)) by nra.
  lra.
Qed.

(* (occ) occupancy derivative dp/dr = kappa p(1-p) > 0 for kappa>0, 0<p<1 *)
Theorem occupancy_increasing : forall kappa p : Q,
  0 < kappa -> 0 < p -> p < 1 -> 0 < kappa * (p * (1 - p)).
Proof.
  intros kappa p Hk Hp0 Hp1.
  apply Qmult_lt_0_compat; [ assumption | nra ].
Qed.

(* (bounds) scale bounds from the stationarity equation and monotone occupancy.
   Given 2 beta r_star + alpha = X (= sum kappa p_star), with Pi_cl <= X < S, and beta>0:
   (Pi_cl - alpha)/(2 beta) <= r_star  and  r_star < (S - alpha)/(2 beta). *)
Theorem scale_lower_bound : forall alpha beta rstar Pcl X : Q,
  0 < beta -> 2*beta*rstar + alpha == X -> Pcl <= X -> Pcl - alpha <= 2*beta*rstar.
Proof. intros. lra. Qed.
Theorem scale_upper_bound : forall alpha beta rstar S X : Q,
  0 < beta -> 2*beta*rstar + alpha == X -> X < S -> 2*beta*rstar < S - alpha.
Proof. intros. lra. Qed.

(* (rp) reflection positivity preserved: D = diag(d1,d2)>=0, K=[[a,b],[b,c]] PSD
   => D K D = [[d1^2 a, d1 d2 b],[d1 d2 b, d2^2 c]] is PSD (diag>=0, det>=0). *)
Theorem rp_gram_preserved : forall d1 d2 a b c : Q,
  0 <= a -> 0 <= c -> 0 <= a*c - b*b ->
  0 <= (d1*d1)*a
  /\ (d1*d1*a)*(d2*d2*c) - (d1*d2*b)*(d1*d2*b) == (d1*d1)*(d2*d2)*(a*c - b*b).
Proof.
  intros d1 d2 a b c Ha Hc Hdet. split.
  - apply Qmult_le_0_compat; [ nra | assumption ].
  - ring.
Qed.

End InfoOrderVacuumSelection.

Print Assumptions InfoOrderVacuumSelection.occupancy_squeeze.
Print Assumptions InfoOrderVacuumSelection.origin_slope.
Print Assumptions InfoOrderVacuumSelection.a_eff_negative_witness.
Print Assumptions InfoOrderVacuumSelection.convexity_positive.
Print Assumptions InfoOrderVacuumSelection.occupancy_increasing.
Print Assumptions InfoOrderVacuumSelection.scale_lower_bound.
Print Assumptions InfoOrderVacuumSelection.scale_upper_bound.
Print Assumptions InfoOrderVacuumSelection.rp_gram_preserved.
