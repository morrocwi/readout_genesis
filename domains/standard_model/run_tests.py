#!/usr/bin/env python3
"""Run the standard_model frontier witnesses.

Python (always, stdlib only, no network):
  - unified_force_closure_v0_1.py   (Unified Force Closure v0.1, finite/internal)
  - four_force_circulation_v0_2.py  (Four-Force Circulation v0.2, fixture scheme)
  - electroweak_decoder_v0_3.py     (Unified Force v0.3, calibrated electroweak decoder)
Coq finite formal witnesses (only if `coqc` is on PATH; skipped otherwise):
  - InfoOrderDefectFromComposition.v      (SM-G0/G0.6 order-defect from ordered composition)
  - InfoFourForceCirculationRecovery.v    (v0.2 exact response identity + recovery + control)
  - InfoElectroweakNullDirection.v        (v0.3 rank-1 obstruction => massless photon + massive Z)
"""
import subprocess, sys, json, os, shutil, tempfile
os.chdir(os.path.dirname(os.path.abspath(__file__)))

out = {}
ok = True

for py in ("unified_force_closure_v0_1.py", "four_force_circulation_v0_2.py",
           "electroweak_decoder_v0_3.py"):
    r = subprocess.run([sys.executable, py])
    out[py] = r.returncode == 0
    ok = ok and r.returncode == 0

if shutil.which("coqc"):
    for v in ("InfoOrderDefectFromComposition.v", "InfoFourForceCirculationRecovery.v",
              "InfoElectroweakNullDirection.v"):
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
