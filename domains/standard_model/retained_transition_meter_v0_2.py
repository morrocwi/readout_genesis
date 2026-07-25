#!/usr/bin/env python3
"""
Retained Transition Meter v0.2 -- isolated candidate.

Tier: calibrated_readout / finite_diagnostic / candidate.
Not a root derivation. Not a physical Standard-Model identification.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Dict, List, MutableMapping, Optional, Sequence, Tuple

from retained_transition_meter_v0_2_core import *
from retained_transition_meter_v0_2_validation import *


def componentize_reader(load: Sequence[float]) -> Dict[str, List[float]]:
    return {
        "residual": list(vec_scale(0.40, load)),
        "source": list(vec_scale(0.80, load)),
        "damping": list(vec_scale(0.10, load)),
        "transport": list(vec_scale(0.05, load)),
        "potential": list(vec_scale(0.05, load)),
    }


def componentize_record(load: Sequence[float]) -> Dict[str, List[float]]:
    return {
        "residual": list(vec_scale(0.50, load)),
        "damping": list(vec_scale(0.70, load)),
        "transport": list(vec_scale(0.10, load)),
        "hessian": list(vec_scale(0.10, load)),
    }


def demo_state(branch_index: int, path_number: int, t: float) -> Tuple[List[float], List[float]]:
    base = (0.44, 0.57, 0.73)[branch_index]
    phase = 0.31 * path_number + 0.17 * branch_index
    amp_phi = (1.25, 0.97, 0.66)[branch_index] * (1.0 + 0.04 * path_number)
    amp_psi = (1.03, 0.79, 0.51)[branch_index] * (1.0 - 0.025 * path_number)
    phi = [
        amp_phi * (math.sin(base * t + phase) + 0.21 * math.sin(1.91 * base * t + 0.2 * phase)),
        0.71 * amp_phi * (math.cos(0.83 * base * t + 0.5 * phase) + 0.13 * math.sin(2.17 * base * t)),
        0.39 * amp_phi * math.sin(1.37 * base * t + 0.11 * path_number),
    ]
    psi = [
        amp_psi * (math.cos(0.91 * base * t + 0.4 * phase) + 0.17 * math.sin(1.63 * base * t)),
        0.63 * amp_psi * (math.sin(1.07 * base * t + phase) + 0.11 * math.cos(2.03 * base * t)),
        0.42 * amp_psi * math.cos(1.29 * base * t + 0.23 * path_number),
    ]
    return phi, psi


def generate_demo(path_semantics: str = "primitive_closure") -> Dict[str, object]:
    m_true = 1.75
    samples: List[MutableMapping[str, object]] = []
    branches = ("U", "D", "E")
    counts = (31, 38, 47, 56)
    duration = 6.0
    for branch_index, branch in enumerate(branches):
        for path_number, count in enumerate(counts):
            path_id = f"{branch}-{path_number}"
            path_samples: List[MutableMapping[str, object]] = []
            for k in range(count):
                u = k / (count - 1)
                warped = u + 0.018 * math.sin(math.pi * u) * math.sin(0.7 * path_number + 0.3 * branch_index)
                t = duration * warped
                phi, psi = demo_state(branch_index, path_number, t)
                path_samples.append({
                    "path_id": path_id,
                    "branch": branch,
                    "time": t,
                    "phi": phi,
                    "psi": psi,
                })
            for local_index in range(1, len(path_samples) - 1):
                p = Sample(path_id, branch, float(path_samples[local_index - 1]["time"]),
                           tuple(path_samples[local_index - 1]["phi"]), tuple(path_samples[local_index - 1]["psi"]), None, None)
                c = Sample(path_id, branch, float(path_samples[local_index]["time"]),
                           tuple(path_samples[local_index]["phi"]), tuple(path_samples[local_index]["psi"]), None, None)
                n = Sample(path_id, branch, float(path_samples[local_index + 1]["time"]),
                           tuple(path_samples[local_index + 1]["phi"]), tuple(path_samples[local_index + 1]["psi"]), None, None)
                acc_phi = irregular_second_difference(p, c, n, "phi")
                acc_psi = irregular_second_difference(p, c, n, "psi")
                noise_scale = 0.0012
                global_index = len(samples) + local_index
                reader_load = [m_true * a + noise_scale * math.sin(0.61 * global_index + 0.3 * j)
                               for j, a in enumerate(acc_phi)]
                record_load = [m_true * a + noise_scale * math.cos(0.47 * global_index + 0.2 * j)
                               for j, a in enumerate(acc_psi)]
                if (path_number + branch_index) % 2 == 0:
                    path_samples[local_index]["reader_load"] = reader_load
                    path_samples[local_index]["record_load"] = record_load
                else:
                    path_samples[local_index]["reader_components"] = componentize_reader(reader_load)
                    path_samples[local_index]["record_components"] = componentize_record(record_load)
            samples.extend(path_samples)
    return {
        "schema": SCHEMA,
        "tier": "SimulatedData/finite_diagnostic",
        "path_semantics": path_semantics,
        "delta_mode": "path_total",
        "delta_is_dimensionless": True,
        "cost_unit_rd": 18.0,
        "provenance": {
            "source_id": "deterministic-analytic-demo-v0.2",
            "adapter_id": "direct-and-core-term-component-demo-adapter-v0.2",
            "calibration_id": "native-rd-demo-scale-18",
        },
        "demo_truth": {"M": m_true},
        "samples": samples,
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Retained Transition Meter v0.2 candidate")
    source = parser.add_mutually_exclusive_group(required=False)
    source.add_argument("--input", type=Path)
    source.add_argument("--demo", action="store_true")
    parser.add_argument("--write-demo", type=Path)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.input is None:
            payload = generate_demo()
        else:
            payload = json.loads(args.input.read_text(encoding="utf-8"))
        if args.write_demo:
            args.write_demo.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        report = analyze(payload)
        if "demo_truth" in payload:
            true_m = float(payload["demo_truth"]["M"])
            estimated = float(report["M"]["joint"])
            recovery_error = abs(estimated - true_m) / true_m
            report["demo_recovery"] = {"true_M": true_m, "relative_error": recovery_error}
            report["gates"]["demo_M_recovery_le_1pct"] = recovery_error <= 0.01
            report["decision"] = "PASS" if all(report["gates"].values()) else "FAIL"
            report["downstream_enabled"] = (
                report["decision"] == "PASS" and report["path_semantics"] == "primitive_closure"
            )
            if not report["downstream_enabled"]:
                report["lambda_candidate_by_branch"] = None
                report["Pi0_candidate"] = None
        print(json.dumps(report, indent=2 if args.pretty else None, sort_keys=True))
        return 0 if report["decision"] == "PASS" else 1
    except (OSError, json.JSONDecodeError, MeterError) as exc:
        print(json.dumps({"schema": REPORT_SCHEMA, "decision": "FAIL", "error": str(exc)}, sort_keys=True))
        return 2


if __name__ == "__main__":
    sys.exit(main())
