#!/usr/bin/env python3
"""Run the standard_model frontier witnesses.

Python (always, stdlib only, no network):
  - unified_force_closure_v0_1.py   (Unified Force Closure v0.1, finite/internal)
  - four_force_circulation_v0_2.py  (Four-Force Circulation v0.2, fixture scheme)
  - electroweak_decoder_v0_3.py     (Unified Force v0.3, calibrated electroweak decoder)
  - sm_discovery_pipeline_v0_4.py    (SM Discovery Pipeline v0.4, finite blind discovery)
  - ordered_tape_closure_v0_2.py     (Ordered-Tape Closure v0.2: color=3, SU(3), Z3 from tape rules)
  - center_confinement_v0_3.py       (Center-Confinement v0.3: Z3 2D area law, V(R)=σR)
Coq finite formal witnesses (only if `coqc` is on PATH; skipped otherwise):
  - InfoOrderDefectFromComposition.v      (SM-G0/G0.6 order-defect from ordered composition)
  - InfoFourForceCirculationRecovery.v    (v0.2 exact response identity + recovery + control)
  - InfoElectroweakNullDirection.v        (v0.3 rank-1 obstruction => massless photon + massive Z)
  - InfoHyperchargeAnomalyClosure.v       (v0.4 SM hypercharges + cubic anomaly = 0, exact)
  - InfoOrderedTapeClosure.v              (v0.2 oddness-derived => k=3 => SU(3) + Z3 center)
  - InfoCenterConfinement.v               (v0.3 Z3 area law: <W>=q^A, sigma>0, V(R)=sigma R)
"""
import subprocess, sys, json, os, shutil, tempfile
os.chdir(os.path.dirname(os.path.abspath(__file__)))

out = {}
ok = True

for py in ("unified_force_closure_v0_1.py", "four_force_circulation_v0_2.py",
           "electroweak_decoder_v0_3.py", "sm_discovery_pipeline_v0_4.py",
           "ordered_tape_closure_v0_2.py",
           "center_confinement_v0_3.py"):
    r = subprocess.run([sys.executable, py])
    out[py] = r.returncode == 0
    ok = ok and r.returncode == 0

if shutil.which("coqc"):
    for v in ("InfoOrderDefectFromComposition.v", "InfoFourForceCirculationRecovery.v",
              "InfoElectroweakNullDirection.v", "InfoHyperchargeAnomalyClosure.v",
              "InfoOrderedTapeClosure.v",
              "InfoCenterConfinement.v"):
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
