#!/usr/bin/env python3
"""
Quantum domain — test runner (v0.1).

Runs quantum_closure_v0_1.py (the immutable exact-rational verifier anchor) as a
subprocess and reports a PASS/FAIL decision based on its exit code. Stdlib only, no
network. QUANTUM_ROOT_CLOSURE_PARTIAL tier only -- see README.md and CLAIM_BOUNDARY.json.
"""
import json
import subprocess
import sys
from pathlib import Path

def run_one(script_name):
    script = Path(__file__).resolve().parent / script_name
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
    )
    print(f"--- {script_name} ---")
    print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    decision = "PASS" if result.returncode == 0 else "FAIL"
    print(json.dumps({"script": script_name, "decision": decision, "returncode": result.returncode}))
    return decision == "PASS"

def main():
    ok = run_one("quantum_closure_v0_1.py")
    overall = "PASS" if ok else "FAIL"
    print(json.dumps({"decision": overall, "quantum_closure_v0_1": ok}))
    return 0 if overall == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
