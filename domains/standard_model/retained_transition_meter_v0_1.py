#!/usr/bin/env python3
"""
Retained Transition Meter v0.1

Operational calibrated readout from a segmented reader/record transition tape.
It estimates the scalar DRL exchange rate M from reader and record channels,
then uses the same tape events to compute retained-transition loads:

    c_n = |dPhi_n^T M dPsi_n| / (dt * cost_unit_rd)
    Delta_j^eff = median_path(sum c_n)
    lambda_j = exp(-Delta_j^eff)
    Pi0 = 3 lambda_U + 3 lambda_D + lambda_E

Tier: calibrated_readout / finite_diagnostic. The output is measured from the
tape; it is not a derivation of M or SM parameters from the unrestricted root.

Run without arguments for the deterministic simulated fixture, or:
  python3 retained_transition_meter_v0_1.py --input tape.json --pretty
  python3 retained_transition_meter_v0_1.py --demo --write-demo /tmp/tape.json
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

EPS = 1e-14


class MeterError(ValueError):
    pass


def dot(a: Sequence[float], b: Sequence[float]) -> float:
    if len(a) != len(b):
        raise MeterError(f"dimension mismatch: {len(a)} != {len(b)}")
    return sum(float(x) * float(y) for x, y in zip(a, b))


def vec_sub(a: Sequence[float], b: Sequence[float]) -> List[float]:
    if len(a) != len(b):
        raise MeterError("dimension mismatch in subtraction")
    return [float(x) - float(y) for x, y in zip(a, b)]


def second_difference(prev: Sequence[float], cur: Sequence[float], nxt: Sequence[float], dt: float) -> List[float]:
    if dt <= 0:
        raise MeterError("dt must be positive")
    if not (len(prev) == len(cur) == len(nxt)):
        raise MeterError("state dimensions must be constant within a path")
    scale = 1.0 / (dt * dt)
    return [(float(n) - 2.0 * float(c) + float(p)) * scale for p, c, n in zip(prev, cur, nxt)]


def rms(values: Iterable[float]) -> float:
    xs = [float(x) for x in values]
    if not xs:
        return 0.0
    return math.sqrt(sum(x * x for x in xs) / len(xs))


@dataclass(frozen=True)
class Sample:
    path_id: str
    branch: str
    phi: Tuple[float, ...]
    psi: Tuple[float, ...]
    reader_load: Optional[Tuple[float, ...]]
    record_load: Optional[Tuple[float, ...]]


@dataclass(frozen=True)
class FitRecord:
    path_id: str
    branch: str
    local_index: int
    acc_phi: Tuple[float, ...]
    acc_psi: Tuple[float, ...]
    reader_load: Tuple[float, ...]
    record_load: Tuple[float, ...]


def tuple_or_none(value: object, field: str) -> Optional[Tuple[float, ...]]:
    if value is None:
        return None
    if not isinstance(value, list) or not value:
        raise MeterError(f"{field} must be a non-empty numeric list or null")
    try:
        return tuple(float(x) for x in value)
    except (TypeError, ValueError) as exc:
        raise MeterError(f"{field} contains a non-numeric value") from exc


def parse_tape(payload: Mapping[str, object]) -> Tuple[float, float, List[Sample]]:
    if payload.get("schema") != "retained-transition-tape-v0.1":
        raise MeterError("expected schema retained-transition-tape-v0.1")
    try:
        dt = float(payload["dt"])
        cost_unit_rd = float(payload.get("cost_unit_rd", 1.0))
    except (KeyError, TypeError, ValueError) as exc:
        raise MeterError("dt and cost_unit_rd must be numeric") from exc
    if dt <= 0 or cost_unit_rd <= 0:
        raise MeterError("dt and cost_unit_rd must be positive")
    raw_samples = payload.get("samples")
    if not isinstance(raw_samples, list) or len(raw_samples) < 3:
        raise MeterError("samples must contain at least three entries")

    samples: List[Sample] = []
    expected_dim: Optional[int] = None
    for idx, raw in enumerate(raw_samples):
        if not isinstance(raw, dict):
            raise MeterError(f"sample {idx} is not an object")
        path_id = str(raw.get("path_id", "")).strip()
        branch = str(raw.get("branch", "")).strip()
        if not path_id or not branch:
            raise MeterError(f"sample {idx} needs path_id and branch")
        phi = tuple_or_none(raw.get("phi"), f"samples[{idx}].phi")
        psi = tuple_or_none(raw.get("psi"), f"samples[{idx}].psi")
        if phi is None or psi is None or len(phi) != len(psi):
            raise MeterError(f"sample {idx} phi/psi dimension mismatch")
        if expected_dim is None:
            expected_dim = len(phi)
        if len(phi) != expected_dim:
            raise MeterError("all samples must use one state dimension")
        reader_load = tuple_or_none(raw.get("reader_load"), f"samples[{idx}].reader_load")
        record_load = tuple_or_none(raw.get("record_load"), f"samples[{idx}].record_load")
        for name, load in (("reader_load", reader_load), ("record_load", record_load)):
            if load is not None and len(load) != expected_dim:
                raise MeterError(f"sample {idx} {name} dimension mismatch")
        samples.append(Sample(path_id, branch, phi, psi, reader_load, record_load))
    return dt, cost_unit_rd, samples


def build_fit_records(samples: Sequence[Sample], dt: float) -> List[FitRecord]:
    records: List[FitRecord] = []
    local_positions: Dict[str, int] = {}
    for i in range(1, len(samples) - 1):
        prev, cur, nxt = samples[i - 1], samples[i], samples[i + 1]
        if not (prev.path_id == cur.path_id == nxt.path_id):
            continue
        if cur.reader_load is None or cur.record_load is None:
            continue
        if not (prev.branch == cur.branch == nxt.branch):
            raise MeterError(f"branch changes inside path {cur.path_id}")
        local_index = local_positions.get(cur.path_id, 0)
        local_positions[cur.path_id] = local_index + 1
        records.append(FitRecord(
            path_id=cur.path_id,
            branch=cur.branch,
            local_index=local_index,
            acc_phi=tuple(second_difference(prev.phi, cur.phi, nxt.phi, dt)),
            acc_psi=tuple(second_difference(prev.psi, cur.psi, nxt.psi, dt)),
            reader_load=cur.reader_load,
            record_load=cur.record_load,
        ))
    if len(records) < 6:
        raise MeterError("fewer than six usable interior records; M is unidentifiable")
    return records


def split_records(records: Sequence[FitRecord], holdout_fraction: float = 0.30) -> Tuple[List[FitRecord], List[FitRecord]]:
    by_path: Dict[str, List[FitRecord]] = {}
    for rec in records:
        by_path.setdefault(rec.path_id, []).append(rec)
    train: List[FitRecord] = []
    holdout: List[FitRecord] = []
    for path_id in sorted(by_path):
        path_records = sorted(by_path[path_id], key=lambda r: r.local_index)
        if len(path_records) < 3:
            raise MeterError(f"path {path_id} has fewer than three usable interior records")
        n_hold = max(1, int(math.ceil(len(path_records) * holdout_fraction)))
        if n_hold >= len(path_records):
            n_hold = 1
        train.extend(path_records[:-n_hold])
        holdout.extend(path_records[-n_hold:])
    if not train or not holdout:
        raise MeterError("train/holdout split is empty")
    return train, holdout


def fit_scalar(records: Sequence[FitRecord], channel: str) -> float:
    numerator = 0.0
    denominator = 0.0
    for rec in records:
        if channel == "joint":
            numerator += dot(rec.acc_phi, rec.reader_load) + dot(rec.acc_psi, rec.record_load)
            denominator += dot(rec.acc_phi, rec.acc_phi) + dot(rec.acc_psi, rec.acc_psi)
        else:
            acc, load = ((rec.acc_phi, rec.reader_load) if channel == "reader"
                         else (rec.acc_psi, rec.record_load))
            numerator += dot(acc, load)
            denominator += dot(acc, acc)
    if denominator <= EPS:
        raise MeterError(f"{channel} acceleration rank is zero")
    return numerator / denominator


def channel_nrmse(records: Sequence[FitRecord], m_value: float, channel: str) -> float:
    residuals: List[float] = []
    targets: List[float] = []
    for rec in records:
        acc, load = ((rec.acc_phi, rec.reader_load) if channel == "reader"
                     else (rec.acc_psi, rec.record_load))
        residuals.extend(float(y) - m_value * float(a) for a, y in zip(acc, load))
        targets.extend(float(y) for y in load)
    scale = rms(targets)
    if scale <= EPS:
        raise MeterError(f"{channel} holdout target is zero")
    return rms(residuals) / scale


def negative_control_nrmse(train: Sequence[FitRecord], holdout: Sequence[FitRecord], channel: str) -> float:
    rotated = list(train[1:]) + [train[0]]
    numerator = 0.0
    denominator = 0.0
    for rec, donor in zip(train, rotated):
        acc = rec.acc_phi if channel == "reader" else rec.acc_psi
        load = donor.reader_load if channel == "reader" else donor.record_load
        numerator += dot(acc, load)
        denominator += dot(acc, acc)
    if denominator <= EPS:
        raise MeterError("negative-control acceleration rank is zero")
    return channel_nrmse(holdout, numerator / denominator, channel)


def branch_fit(records: Sequence[FitRecord]) -> Dict[str, float]:
    by_branch: Dict[str, List[FitRecord]] = {}
    for rec in records:
        by_branch.setdefault(rec.branch, []).append(rec)
    return {branch: fit_scalar(subset, "joint") for branch, subset in sorted(by_branch.items())}


def transition_costs(samples: Sequence[Sample], dt: float, cost_unit_rd: float, m_value: float) -> Tuple[Dict[str, float], Dict[str, str]]:
    path_costs: Dict[str, float] = {}
    path_branch: Dict[str, str] = {}
    for cur, nxt in zip(samples, samples[1:]):
        if cur.path_id != nxt.path_id:
            continue
        if cur.branch != nxt.branch:
            raise MeterError(f"branch changes inside path {cur.path_id}")
        dphi = vec_sub(nxt.phi, cur.phi)
        dpsi = vec_sub(nxt.psi, cur.psi)
        signed_exchange = m_value * dot(dphi, dpsi) / dt
        path_costs[cur.path_id] = path_costs.get(cur.path_id, 0.0) + abs(signed_exchange) / cost_unit_rd
        path_branch[cur.path_id] = cur.branch
    if not path_costs:
        raise MeterError("no within-path transitions")
    return path_costs, path_branch


def summarize_costs(path_costs: Mapping[str, float], path_branch: Mapping[str, str]) -> Tuple[Dict[str, float], Dict[str, float], Optional[float]]:
    branch_paths: Dict[str, List[float]] = {}
    for path_id, cost in path_costs.items():
        branch_paths.setdefault(path_branch[path_id], []).append(float(cost))
    delta_eff = {branch: statistics.median(costs) for branch, costs in sorted(branch_paths.items())}
    lambdas = {branch: math.exp(-delta) for branch, delta in delta_eff.items()}
    pi0 = None
    if all(branch in lambdas for branch in ("U", "D", "E")):
        pi0 = 3.0 * lambdas["U"] + 3.0 * lambdas["D"] + lambdas["E"]
    return delta_eff, lambdas, pi0


def analyze(payload: Mapping[str, object]) -> Dict[str, object]:
    dt, cost_unit_rd, samples = parse_tape(payload)
    records = build_fit_records(samples, dt)
    train, holdout = split_records(records)
    m_reader = fit_scalar(train, "reader")
    m_record = fit_scalar(train, "record")
    m_joint = fit_scalar(train, "joint")
    if m_joint <= 0:
        raise MeterError(f"estimated M must be positive; got {m_joint}")
    reader_nrmse = channel_nrmse(holdout, m_joint, "reader")
    record_nrmse = channel_nrmse(holdout, m_joint, "record")
    reader_negative = negative_control_nrmse(train, holdout, "reader")
    record_negative = negative_control_nrmse(train, holdout, "record")
    agreement = abs(m_reader - m_record) / max(abs(m_joint), EPS)
    path_costs, path_branch = transition_costs(samples, dt, cost_unit_rd, m_joint)
    delta_eff, lambdas, pi0 = summarize_costs(path_costs, path_branch)
    gates = {
        "positive_M": m_joint > 0,
        "reader_record_agreement_le_5pct": agreement <= 0.05,
        "reader_holdout_nrmse_le_10pct": reader_nrmse <= 0.10,
        "record_holdout_nrmse_le_10pct": record_nrmse <= 0.10,
        "reader_negative_control_worse": reader_negative >= 3.0 * reader_nrmse,
        "record_negative_control_worse": record_negative >= 3.0 * record_nrmse,
        "branch_costs_nonnegative": all(x >= 0 for x in delta_eff.values()),
        "lambda_in_0_1": all(0 < x <= 1 for x in lambdas.values()),
    }
    return {
        "schema": "retained-transition-meter-report-v0.1",
        "tier": "calibrated_readout/finite_diagnostic",
        "claim_boundary": "Measured from this tape; not derived from the unrestricted root and not a universal SM parameter.",
        "decision": "PASS" if all(gates.values()) else "FAIL",
        "sample_count": len(samples),
        "usable_fit_records": len(records),
        "train_records": len(train),
        "holdout_records": len(holdout),
        "dt": dt,
        "cost_unit_rd": cost_unit_rd,
        "M": {
            "reader": m_reader,
            "record": m_record,
            "joint": m_joint,
            "reader_record_relative_gap": agreement,
            "by_branch_joint": branch_fit(train),
        },
        "holdout": {
            "reader_nrmse": reader_nrmse,
            "record_nrmse": record_nrmse,
            "reader_negative_control_nrmse": reader_negative,
            "record_negative_control_nrmse": record_negative,
        },
        "path_cost_rd": dict(sorted(path_costs.items())),
        "delta_eff_by_branch": delta_eff,
        "lambda_by_branch": lambdas,
        "Pi0": pi0,
        "gates": gates,
    }


def generate_demo() -> Dict[str, object]:
    dt = 0.5
    m_true = 1.75
    cost_unit_rd = 16.0
    samples: List[Dict[str, object]] = []
    branch_config = {
        "U": (1.25, 0.95, 0.43),
        "D": (0.92, 0.72, 0.37),
        "E": (0.58, 0.44, 0.31),
    }
    for branch_index, (branch, (amp_phi, amp_psi, freq)) in enumerate(branch_config.items()):
        for path_number in range(3):
            path_id = f"{branch}-{path_number}"
            phase = 0.21 * path_number + 0.13 * branch_index
            start = len(samples)
            for k in range(12):
                t = k * dt
                samples.append({
                    "path_id": path_id,
                    "branch": branch,
                    "phi": [
                        amp_phi * math.sin(freq * t + phase),
                        0.67 * amp_phi * math.cos(0.83 * freq * t + 0.7 * phase),
                    ],
                    "psi": [
                        amp_psi * math.cos(0.91 * freq * t + 0.4 * phase),
                        0.61 * amp_psi * math.sin(1.07 * freq * t + phase),
                    ],
                    "reader_load": None,
                    "record_load": None,
                })
            end = len(samples)
            for idx in range(start + 1, end - 1):
                p, c, n = samples[idx - 1], samples[idx], samples[idx + 1]
                acc_phi = second_difference(p["phi"], c["phi"], n["phi"], dt)  # type: ignore[arg-type]
                acc_psi = second_difference(p["psi"], c["psi"], n["psi"], dt)  # type: ignore[arg-type]
                noise_scale = 0.0015
                reader_noise = [noise_scale * math.sin(0.7 * idx + j) for j in range(2)]
                record_noise = [noise_scale * math.cos(0.5 * idx + 0.3 * j) for j in range(2)]
                c["reader_load"] = [m_true * a + e for a, e in zip(acc_phi, reader_noise)]
                c["record_load"] = [m_true * a + e for a, e in zip(acc_psi, record_noise)]
    return {
        "schema": "retained-transition-tape-v0.1",
        "tier": "SimulatedData/finite_diagnostic",
        "dt": dt,
        "cost_unit_rd": cost_unit_rd,
        "demo_truth": {"M": m_true},
        "samples": samples,
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Measure reader/record exchange and branch costs from a transition tape.")
    source = parser.add_mutually_exclusive_group(required=False)
    source.add_argument("--input", type=Path)
    source.add_argument("--demo", action="store_true")
    parser.add_argument("--write-demo", type=Path)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.demo or args.input is None:
            payload = generate_demo()
            if args.write_demo:
                args.write_demo.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        else:
            payload = json.loads(args.input.read_text(encoding="utf-8"))
        result = analyze(payload)
        if args.demo or args.input is None:
            true_m = float(payload["demo_truth"]["M"])  # type: ignore[index]
            estimated = float(result["M"]["joint"])  # type: ignore[index]
            recovery_error = abs(estimated - true_m) / true_m
            result["demo_recovery"] = {"true_M": true_m, "relative_error": recovery_error}
            result["gates"]["demo_M_recovery_le_1pct"] = recovery_error <= 0.01  # type: ignore[index]
            result["decision"] = "PASS" if all(result["gates"].values()) else "FAIL"  # type: ignore[index]
        print(json.dumps(result, indent=2 if args.pretty else None, sort_keys=True))
        return 0 if result["decision"] == "PASS" else 1
    except (OSError, json.JSONDecodeError, MeterError) as exc:
        print(json.dumps({
            "schema": "retained-transition-meter-report-v0.1",
            "decision": "FAIL",
            "error": str(exc),
        }, sort_keys=True))
        return 2


if __name__ == "__main__":
    sys.exit(main())
