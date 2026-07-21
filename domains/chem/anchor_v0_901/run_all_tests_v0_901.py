from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def run(cmd):
    p = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    return {"command": cmd, "returncode": p.returncode, "stdout": p.stdout, "stderr": p.stderr}

steps = []
steps.append(run([sys.executable, "make_proof_receipt_v0_901.py"]))
steps.append(run([sys.executable, "drift_validator_v0_901.py"]))
steps.append(run([sys.executable, "checker_v0_901.py"]))
steps.append(run([sys.executable, "-m", "unittest", "-v", "test_proof_kernel_v0_901.py", "test_drift_contract_v0_901.py", "test_release_integrity_v0_901.py"]))
result = {
    "version": "0.901",
    "steps": steps,
    "decision": "PASS" if all(s["returncode"] == 0 for s in steps) else "FAIL"
}
(ROOT / "TEST_REPORT_v0_901.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["decision"] == "PASS" else 1)
