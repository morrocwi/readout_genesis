#!/usr/bin/env python3
"""
Biology domain — test runner (v0.1).

Runs biology_closure_v0_1.py (the immutable exact-rational verifier anchor) as a
subprocess and reports a PASS/FAIL decision based on its exit code. Stdlib only, no
network. BIOLOGY_ROOT_NATIVE_PARTIAL tier only -- see README.md and CLAIM_BOUNDARY.json.
LINE-1 (root-native) only; the LINE-2 textbook curriculum solver is a separate checker
and is not run or counted here.
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
    ok = run_one("biology_closure_v0_1.py")
    overall = "PASS" if ok else "FAIL"
    print(json.dumps({"decision": overall, "biology_closure_v0_1": ok}))
    return 0 if overall == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
