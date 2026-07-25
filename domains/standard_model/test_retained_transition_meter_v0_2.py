#!/usr/bin/env python3
"""Candidate tests for retained_transition_meter_v0_2.py (stdlib only)."""
from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "retained_transition_meter_v0_2.py"
spec = importlib.util.spec_from_file_location("rtm_v02", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load retained_transition_meter_v0_2.py")
rtm = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = rtm
spec.loader.exec_module(rtm)

FAILS = []


def ck(name, condition, got=None):
    ok = bool(condition)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f" got={got}"))
    if not ok:
        FAILS.append(name)


print("== 1. deterministic recovery + transport/invariance gates ==")
payload = rtm.generate_demo()
report = rtm.analyze(payload)
true_m = payload["demo_truth"]["M"]
recovery = abs(report["M"]["joint"] - true_m) / true_m
ck("demo decision PASS", report["decision"] == "PASS", report["decision"])
ck("hidden M recovery <=1%", recovery <= 0.01, recovery)
ck("leave-one-path-out gate", report["gates"]["leave_one_path_out_worst_nrmse_le_15pct"])
ck("leave-one-branch-out gate", report["gates"]["leave_one_branch_out_worst_nrmse_le_20pct"])
ck("stride-2/3 segmentation gate", report["gates"]["segmentation_worst_gap_le_10pct"])
ck("three negative controls pass", all(report["gates"][name] for name in (
    "shift_control_is_worse", "reverse_control_is_worse", "cross_path_control_is_worse")))
ck("coordinate relabeling invariance passes", report["gates"]["coordinate_M_invariant"] and report["gates"]["coordinate_cost_invariant"])
ck("primitive-closure demo enables downstream", report["downstream_enabled"] and report["Pi0_candidate"] is not None)

print("\n== 2. semantic lock: observed trajectory cannot emit lambda/Pi0 ==")
trajectory_payload = rtm.generate_demo(path_semantics="observed_trajectory")
trajectory_report = rtm.analyze(trajectory_payload)
ck("instrument can pass on an observed trajectory", trajectory_report["decision"] == "PASS")
ck("downstream disabled", trajectory_report["downstream_enabled"] is False)
ck("lambda suppressed", trajectory_report["lambda_candidate_by_branch"] is None)
ck("Pi0 suppressed", trajectory_report["Pi0_candidate"] is None)

print("\n== 3. direct load and component adapter are numerically identical ==")
parsed = rtm.parse_tape(payload)
component_samples = [raw for raw in payload["samples"] if "reader_components" in raw]
direct_samples = [raw for raw in payload["samples"] if "reader_load" in raw]
ck("fixture exercises component adapter", len(component_samples) > 0)
ck("fixture exercises direct adapter", len(direct_samples) > 0)
directified = copy.deepcopy(payload)
for index, raw in enumerate(directified["samples"]):
    if "reader_components" not in raw:
        continue
    dim = len(raw["phi"])
    reader = rtm.resolve_load(raw, "reader", dim, f"directified[{index}]")
    record = rtm.resolve_load(raw, "record", dim, f"directified[{index}]")
    raw["reader_load"] = list(reader)
    raw["record_load"] = list(record)
    del raw["reader_components"]
    del raw["record_components"]
direct_report = rtm.analyze(directified)
ck("component/direct M identical", abs(direct_report["M"]["joint"] - report["M"]["joint"]) <= 1e-14,
   abs(direct_report["M"]["joint"] - report["M"]["joint"]))
ck("component/direct Pi0 identical", abs(direct_report["Pi0_candidate"] - report["Pi0_candidate"]) <= 1e-14,
   abs(direct_report["Pi0_candidate"] - report["Pi0_candidate"]))
ck("parsed path count is 12", len(parsed.paths) == 12, len(parsed.paths))

print("\n== 4. provenance and time-order hard failures ==")
missing_provenance = copy.deepcopy(payload)
del missing_provenance["provenance"]
try:
    rtm.parse_tape(missing_provenance)
    provenance_failed = False
except rtm.MeterError:
    provenance_failed = True
ck("missing provenance hard-fails", provenance_failed)

duplicate_time = copy.deepcopy(payload)
first_path = duplicate_time["samples"][0]["path_id"]
indices = [i for i, raw in enumerate(duplicate_time["samples"]) if raw["path_id"] == first_path]
duplicate_time["samples"][indices[1]]["time"] = duplicate_time["samples"][indices[0]]["time"]
try:
    rtm.parse_tape(duplicate_time)
    time_failed = False
except rtm.MeterError:
    time_failed = True
ck("duplicate path time hard-fails", time_failed)

print("\n== 5. branch-specific M is rejected as a global scalar ==")
branch_variant = rtm.generate_demo()
for raw in branch_variant["samples"]:
    if raw["branch"] != "E":
        continue
    if "reader_load" in raw:
        raw["reader_load"] = [1.35 * x for x in raw["reader_load"]]
        raw["record_load"] = [1.35 * x for x in raw["record_load"]]
    if "reader_components" in raw:
        for values in raw["reader_components"].values():
            for index in range(len(values)):
                values[index] *= 1.35
        for values in raw["record_components"].values():
            for index in range(len(values)):
                values[index] *= 1.35
branch_variant_report = rtm.analyze(branch_variant)
ck("branch-varying exchange fails global candidate", branch_variant_report["decision"] == "FAIL")
ck("leave-one-branch gate catches it", not branch_variant_report["gates"]["leave_one_branch_out_worst_nrmse_le_20pct"])
ck("branch estimates visibly separate", branch_variant_report["M"]["by_branch_joint"]["E"] > 1.25 * branch_variant_report["M"]["by_branch_joint"]["U"])

print("\n== 6. report is JSON serializable and bounded honestly ==")
encoded = json.dumps(report, sort_keys=True)
ck("report serializes", len(encoded) > 100)
ck("candidate tier explicit", "candidate" in report["tier"])
ck("claim boundary denies root derivation", "Not derived" in report["claim_boundary"])

print()
if FAILS:
    print(f"DECISION: FAIL ({len(FAILS)}): {FAILS}")
    raise SystemExit(1)
print("DECISION: PASS -- v0.2 candidate recovery, semantic lock, transport, invariance, and hard-fail tests pass.")
