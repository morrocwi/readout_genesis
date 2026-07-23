#!/usr/bin/env python3
"""Run the standard_model frontier witnesses.

Python (always, stdlib only, no network):
  - unified_force_closure_v0_1.py   (Unified Force Closure v0.1, finite/internal)
  - four_force_circulation_v0_2.py  (Four-Force Circulation v0.2, fixture scheme)
  - electroweak_decoder_v0_3.py     (Unified Force v0.3, calibrated electroweak decoder)
  - sm_discovery_pipeline_v0_4.py    (SM Discovery Pipeline v0.4, finite blind discovery)
  - ordered_tape_closure_v0_2.py     (Ordered-Tape Closure v0.2: color=3, SU(3), Z3 from tape rules)
  - center_confinement_v0_3.py       (Center-Confinement v0.3: Z3 2D area law, V(R)=σR)
  - retained_confinement_certificate_v0_5.py  (v0.5: 𝔠=μ4·ρt<1 certificate from the action)
  - triality_spectral_flow_v0_6.py   (v0.6: RG of ρt; block-scale existence 𝔠(b_*)<1)
  - full_block_closure_v0_7.py       (v0.7: b=2 block, first correlated shell u^4(1+16u^4))
  - retained_metric_intertwiner_v0_9.py  (v0.9: CORRECTED criterion mu4*u_hat<1; intertwiner ||P||<=1)
  - all_order_character_v1_0.py      (v1.0: all-order u,v via Weyl integrals; needs numpy)
  - surface_automaton_v1_1.py        (v1.1: Z3 frontier automaton; mu_short=3.87513, bracket)
  - surface_upper_automaton_v1_2.py  (v1.2: upper automaton; mu^+=7.084, bracket [3.875,7.084])
  - finite_transfer_gap_v1_3.py      (v1.3: finite-transfer mass-gap theorem; q<1 => Delta>0; needs numpy)
  - universal_rp_slab_v1_4.py        (v1.4: universal reflection-positive slab; Gram=>PSD, mass reader; needs numpy)
  - hypercharge_global_quotient_v1_5.py  (v1.5: hypercharges + A111=(A_grav)^3 + Z6 center-lock)
  - blind_matter_search_v1_6.py      (v1.6: matter skeleton found BLIND over a minimal alphabet, D=15)
  - root_native_chirality_v1_7.py    (v1.7: chirality grading Gamma_T + exact no-go; needs numpy)
  - tape_kinetic_operator_v1_8.py    (v1.8: Ginsparg-Wilson kinetic operator + no-doubling fixture; needs numpy)
  - relation_channel_dimension_v1_9.py  (v1.9: d=4 derived from the minimal orientation/incidence carrier; needs numpy)
  - isotropic_fixed_point_v1_10.py   (v1.10: finite-frame twirl contraction, rho_frame=0.858...; needs numpy)
  - frame_mixing_from_action_v1_11.py  (v1.11: mixing weights derived from a reflection-positive slab; needs numpy)
  - order_higgs_closure_v1_12.py     (v1.12: minimal order carrier H=(1,2)_1/2 forced; vector mass-rank pattern; needs numpy)
  - intertwiner_order_vacuum_v1_13.py  (v1.13: CORRECTED intertwiner-rank order criterion Pi0>alpha; supersedes an earlier exponential draft; needs numpy)
NOTE: this list is illustrative, not authoritative — the actual test set is the tuple below.
Coq finite formal witnesses (only if `coqc` is on PATH; skipped otherwise):
  - InfoOrderDefectFromComposition.v      (SM-G0/G0.6 order-defect from ordered composition)
  - InfoFourForceCirculationRecovery.v    (v0.2 exact response identity + recovery + control)
  - InfoElectroweakNullDirection.v        (v0.3 rank-1 obstruction => massless photon + massive Z)
  - InfoHyperchargeAnomalyClosure.v       (v0.4 SM hypercharges + cubic anomaly = 0, exact)
  - InfoOrderedTapeClosure.v              (v0.2 oddness-derived => k=3 => SU(3) + Z3 center)
  - InfoCenterConfinement.v               (v0.3 Z3 area law: <W>=q^A, sigma>0, V(R)=sigma R)
  - InfoConfinementCertificate.v          (v0.5 Frobenius/center/Delta_p/geometric-suppression exact)
  - InfoTrialitySpectralFlow.v            (v0.6 serial a_R^m + block contraction + existence witness)
  - InfoBlockCorrelation.v                (v0.7 bump counting + rho_geom=u^4(1+16u^4) + correlations-help)
  - InfoRetainedIntertwiner.v             (v0.9 intertwiner contraction + corrected linear criterion)
  - InfoAllOrderCharacter.v               (v1.0 fusion 3x3bar=1+8 + recursion c0'=2c3)
  - InfoSurfaceAutomaton.v                (v1.1 critical polynomials + root/mu brackets)
  - InfoSurfaceUpperAutomaton.v           (v1.2 branching poly sum=81=3^4 + upper mu bracket)
  - InfoFiniteTransferGap.v               (v1.3 eigenvalue gap q<1=>1-q>0 + diffusion/degeneracy controls)
  - InfoUniversalRPSlab.v                 (v1.4 Gram=>PSD + Fock lift + gauge char-coeff + mass-ratio a-indep)
  - InfoHyperchargeGlobalQuotient.v       (v1.5 A_grav=h-3q, A111=(A_grav)^3, Z6 center-lock)
  - InfoBlindMatterSearch.v               (v1.6 unbounded D_total>=15 via lia; witness+conjugate at 15)
  - InfoRootChirality.v                   (v1.7 Gamma_T involution/self-adjoint/reversal + no-go witness)
  - InfoTapeKineticGW.v                   (v1.8 Ginsparg-Wilson identity + no-doubling arithmetic)
  - InfoDimensionFourClosure.v            (v1.9 d<=4 bound + parity + carrier dimension over Q/Z)
  - InfoIsotropicFixedPoint.v             (v1.10 contraction algebra + rational sextic root bracket)
  - InfoFrameMixingAction.v               (v1.11 Gram-derived weight algebra + rational root bracket)
  - InfoOrderHiggsClosure.v               (v1.12 hypercharge-closure algebra + neutral-matrix det=0 + DOF)
  - InfoIntertwinerOrderVacuum.v          (v1.13 CORRECTED Fock-factor Z_j(0)=1 + automatic-convexity algebra)
  - InfoGaugeAutomorphismGroup.v          (SM-G0.1/G0.2: path composition is a monoid + Aut(F,O) is a group under composition+inverse, fully abstract)
NOTE: this list is illustrative, not authoritative — the actual test set is the tuple below;
this docstring must be updated whenever the tuple changes (do not let it silently drift again).
"""
import subprocess, sys, json, os, shutil, tempfile
os.chdir(os.path.dirname(os.path.abspath(__file__)))

out = {}
ok = True

for py in ("unified_force_closure_v0_1.py", "four_force_circulation_v0_2.py",
           "electroweak_decoder_v0_3.py", "sm_discovery_pipeline_v0_4.py",
           "ordered_tape_closure_v0_2.py",
           "center_confinement_v0_3.py",
           "retained_confinement_certificate_v0_5.py",
           "triality_spectral_flow_v0_6.py",
           "full_block_closure_v0_7.py",
           "retained_metric_intertwiner_v0_9.py", "all_order_character_v1_0.py",
           "surface_automaton_v1_1.py",
           "surface_upper_automaton_v1_2.py",
           "finite_transfer_gap_v1_3.py",
           "universal_rp_slab_v1_4.py",
           "hypercharge_global_quotient_v1_5.py",
           "blind_matter_search_v1_6.py",
           "root_native_chirality_v1_7.py",
           "tape_kinetic_operator_v1_8.py",
           "relation_channel_dimension_v1_9.py",
           "isotropic_fixed_point_v1_10.py",
           "frame_mixing_from_action_v1_11.py",
           "order_higgs_closure_v1_12.py",
           "intertwiner_order_vacuum_v1_13.py"):
    r = subprocess.run([sys.executable, py])
    out[py] = r.returncode == 0
    ok = ok and r.returncode == 0

if shutil.which("coqc"):
    for v in ("InfoOrderDefectFromComposition.v", "InfoFourForceCirculationRecovery.v",
              "InfoElectroweakNullDirection.v", "InfoHyperchargeAnomalyClosure.v",
              "InfoOrderedTapeClosure.v",
              "InfoCenterConfinement.v",
              "InfoConfinementCertificate.v",
              "InfoTrialitySpectralFlow.v",
              "InfoBlockCorrelation.v",
              "InfoRetainedIntertwiner.v", "InfoAllOrderCharacter.v",
              "InfoSurfaceAutomaton.v",
              "InfoSurfaceUpperAutomaton.v",
              "InfoFiniteTransferGap.v",
              "InfoUniversalRPSlab.v",
              "InfoHyperchargeGlobalQuotient.v",
              "InfoBlindMatterSearch.v",
              "InfoRootChirality.v",
              "InfoTapeKineticGW.v",
              "InfoDimensionFourClosure.v",
              "InfoIsotropicFixedPoint.v",
              "InfoFrameMixingAction.v",
              "InfoOrderHiggsClosure.v",
              "InfoIntertwinerOrderVacuum.v",
              "InfoGaugeAutomorphismGroup.v"):
        with tempfile.TemporaryDirectory() as d:
            # compile a COPY inside the tempdir so coqc build artifacts never touch the repo
            shutil.copy(v, os.path.join(d, v))
            r = subprocess.run(["coqc", "-q", v], cwd=d)
        out[v] = r.returncode == 0
        ok = ok and r.returncode == 0
else:
    out["coqc"] = "not found (Coq witnesses skipped)"

out["decision"] = "PASS" if ok else "FAIL"
print(json.dumps(out))
sys.exit(0 if ok else 1)
