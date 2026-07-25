#!/usr/bin/env python3
"""Standalone checks for RTM bias diagnosis v0.1."""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("diag", HERE / "rtm_bias_diagnosis_v0_1.py")
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)

report = MOD.diagnose(mc_seeds=60)
assert report["decision"] == "PASS", report["gates"]
assert report["acceleration_energy"]["record_to_reader_ratio"] > 100.0

s2 = report["sweep"]["2e-06"]["deterministic"]
s1 = report["sweep"]["1e-05"]["deterministic"]
s4 = report["sweep"]["1e-04"]["deterministic"]
assert abs(s2["reader_full"] - 0.9897237666) < 1e-8
assert abs(s1["reader_full"] - 0.7947136899) < 1e-8
assert abs(s4["record_full"] - 0.9385369552) < 1e-8
assert abs(s1["reader_full"] - s1["reader_eiv_only"]) < 1e-4
assert abs(s1["reader_target_only"] - 1.0) < 1e-4
print("PASS: RTM bias diagnosis v0.1")
