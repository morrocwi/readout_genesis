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
           "surface_automaton_v1_1.py"):
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
              "InfoSurfaceAutomaton.v"):
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
