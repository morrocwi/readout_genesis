#!/usr/bin/env python3
"""
Relativity domain — test runner (v0.2).

Runs relativity_closure_v0_1.py (immutable v0.1 anchor) and relativity_closure_v0_2.py
(current release) as subprocesses and reports a PASS/FAIL decision based on their exit
codes. Stdlib only, no network. FINITE_INTERNAL_CLOSURE tier only — see README.md and
CLAIM_BOUNDARY.json.
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
    ok_v01 = run_one("relativity_closure_v0_1.py")
    ok_v02 = run_one("relativity_closure_v0_2.py")
    overall = "PASS" if (ok_v01 and ok_v02) else "FAIL"
    print(json.dumps({"decision": overall, "v0_1": ok_v01, "v0_2": ok_v02}))
    return 0 if overall == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
