#!/usr/bin/env python3
"""Run the Unified Force Closure v0.1 witness. stdlib only, no network."""
import subprocess, sys, json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
r = subprocess.run([sys.executable, "unified_force_closure_v0_1.py"])
print(json.dumps({"decision": "PASS" if r.returncode == 0 else "FAIL",
                  "unified_force_closure_v0_1": r.returncode == 0}))
sys.exit(r.returncode)
