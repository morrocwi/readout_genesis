#!/usr/bin/env python3
"""Validation, controls, invariance, and reporting for RTM v0.2 candidate."""
from __future__ import annotations

import math
import statistics
from typing import Dict, List, Mapping, Optional, Sequence, Tuple

from retained_transition_meter_v0_2_core import *


def fit_scalar(records: Sequence[FitRecord], channel: str = "joint") -> float:
    numerator = 0.0
    denominator = 0.0
    for rec in records:
        pairs: Sequence[Tuple[Sequence[float], Sequence[float]]]
        if channel == "joint":
            pairs = ((rec.acc_phi, rec.reader_load), (rec.acc_psi, rec.record_load))
        elif channel == "reader":
            pairs = ((rec.acc_phi, rec.reader_load),)
        elif channel == "record":
            pairs = ((rec.acc_psi, rec.record_load),)
        else:
            raise MeterError(f"unknown channel {channel}")
        for acc, load in pairs:
            numerator += dot(acc, load)
            denominator += dot(acc, acc)
    if denominator <= EPS:
        raise MeterError(f"{channel} acceleration rank is zero")
    value = numerator / denominator
    if not math.isfinite(value):
        raise MeterError(f"{channel} estimate is non-finite")
    return value


def channel_nrmse(records: Sequence[FitRecord], m_value: float, channel: str) -> float:
    residuals: List[float] = []
    targets: List[float] = []
    for rec in records:
        if channel == "reader":
            acc, load = rec.acc_phi, rec.reader_load
        elif channel == "record":
            acc, load = rec.acc_psi, rec.record_load
        else:
            raise MeterError(f"unknown channel {channel}")
        residuals.extend(float(y) - m_value * float(a) for a, y in zip(acc, load))
        targets.extend(float(y) for y in load)
    scale = rms(targets)
    if scale <= EPS:
        raise MeterError(f"{channel} target scale is zero")
    return rms(residuals) / scale


def joint_nrmse(records: Sequence[FitRecord], m_value: float) -> float:
    return math.sqrt((channel_nrmse(records, m_value, "reader") ** 2 +
                      channel_nrmse(records, m_value, "record") ** 2) / 2.0)


def group_records(records: Sequence[FitRecord], attr: str) -> Dict[str, List[FitRecord]]:
    grouped: Dict[str, List[FitRecord]] = {}
    for rec in records:
        key = str(getattr(rec, attr))
        grouped.setdefault(key, []).append(rec)
    return grouped


def cross_validate(records: Sequence[FitRecord], attr: str) -> Dict[str, object]:
    groups = group_records(records, attr)
    folds: Dict[str, Dict[str, float]] = {}
    for held_key, held in sorted(groups.items()):
        train = [rec for rec in records if str(getattr(rec, attr)) != held_key]
        if not train:
            raise MeterError(f"empty training set for held-out {attr}={held_key}")
        m_value = fit_scalar(train, "joint")
        folds[held_key] = {
            "M": m_value,
            "reader_nrmse": channel_nrmse(held, m_value, "reader"),
            "record_nrmse": channel_nrmse(held, m_value, "record"),
            "joint_nrmse": joint_nrmse(held, m_value),
        }
    joint_values = [item["joint_nrmse"] for item in folds.values()]
    return {
        "folds": folds,
        "median_joint_nrmse": statistics.median(joint_values),
        "worst_joint_nrmse": max(joint_values),
    }


def transform_vector(vector: Sequence[float]) -> Tuple[float, ...]:
    reversed_values = list(reversed([float(x) for x in vector]))
    return tuple((1.0 if i % 2 == 0 else -1.0) * value
                 for i, value in enumerate(reversed_values))


def transform_record(rec: FitRecord) -> FitRecord:
    return FitRecord(
        rec.path_id, rec.branch, rec.local_index,
        transform_vector(rec.acc_phi), transform_vector(rec.acc_psi),
        transform_vector(rec.reader_load), transform_vector(rec.record_load),
    )


def transform_paths(paths: Mapping[str, Tuple[Sample, ...]]) -> Dict[str, Tuple[Sample, ...]]:
    result: Dict[str, Tuple[Sample, ...]] = {}
    for path_id, samples in paths.items():
        result[path_id] = tuple(Sample(
            s.path_id, s.branch, s.time,
            transform_vector(s.phi), transform_vector(s.psi),
            None if s.reader_load is None else transform_vector(s.reader_load),
            None if s.record_load is None else transform_vector(s.record_load),
        ) for s in samples)
    return result


def contaminate_records(records: Sequence[FitRecord], mode: str) -> List[FitRecord]:
    by_path = group_records(records, "path_id")
    ordered_paths = {key: sorted(values, key=lambda r: r.local_index) for key, values in by_path.items()}
    contaminated: List[FitRecord] = []
    if mode in {"shift_one", "reverse"}:
        for path_id, values in sorted(ordered_paths.items()):
            donors = values[1:] + values[:1] if mode == "shift_one" else list(reversed(values))
            for rec, donor in zip(values, donors):
                contaminated.append(FitRecord(
                    rec.path_id, rec.branch, rec.local_index,
                    rec.acc_phi, rec.acc_psi, donor.reader_load, donor.record_load,
                ))
        return contaminated
    if mode == "cross_path_same_branch":
        by_branch: Dict[str, List[str]] = {}
        for path_id, values in ordered_paths.items():
            by_branch.setdefault(values[0].branch, []).append(path_id)
        for branch, path_ids in sorted(by_branch.items()):
            path_ids = sorted(path_ids)
            if len(path_ids) < 2:
                raise MeterError(f"branch {branch} needs at least two paths for cross-path control")
            donor_ids = path_ids[1:] + path_ids[:1]
            for path_id, donor_id in zip(path_ids, donor_ids):
                values = ordered_paths[path_id]
                donors = ordered_paths[donor_id]
                for index, rec in enumerate(values):
                    donor = donors[index % len(donors)]
                    contaminated.append(FitRecord(
                        rec.path_id, rec.branch, rec.local_index,
                        rec.acc_phi, rec.acc_psi, donor.reader_load, donor.record_load,
                    ))
        return contaminated
    raise MeterError(f"unknown contamination mode {mode}")


def negative_control(records: Sequence[FitRecord], mode: str) -> Dict[str, float]:
    bad_records = contaminate_records(records, mode)
    bad_m = fit_scalar(bad_records, "joint")
    return {
        "fitted_M": bad_m,
        "genuine_reader_nrmse": channel_nrmse(records, bad_m, "reader"),
        "genuine_record_nrmse": channel_nrmse(records, bad_m, "record"),
        "genuine_joint_nrmse": joint_nrmse(records, bad_m),
    }


def coarsen_samples(samples: Sequence[Sample], stride: int) -> Tuple[Sample, ...]:
    if stride < 1:
        raise MeterError("stride must be positive")
    indices = list(range(0, len(samples), stride))
    if indices[-1] != len(samples) - 1:
        indices.append(len(samples) - 1)
    return tuple(samples[i] for i in indices)


def path_exchange(samples: Sequence[Sample], m_value: float, cost_unit_rd: float) -> Dict[str, float]:
    signed_total = 0.0
    absolute_total = 0.0
    for cur, nxt in zip(samples, samples[1:]):
        dt = nxt.time - cur.time
        if dt <= 0:
            raise MeterError("non-positive transition interval")
        dphi = vec_sub(nxt.phi, cur.phi)
        dpsi = vec_sub(nxt.psi, cur.psi)
        signed = m_value * dot(dphi, dpsi) / (dt * cost_unit_rd)
        signed_total += signed
        absolute_total += abs(signed)
    duration = samples[-1].time - samples[0].time
    if duration <= 0:
        raise MeterError("path duration must be positive")
    return {
        "signed_total_rd": signed_total,
        "absolute_total_rd": absolute_total,
        "rate_per_time_rd": absolute_total / duration,
        "duration": duration,
        "transitions": float(len(samples) - 1),
        "orientation_cancellation_fraction": 0.0 if absolute_total <= EPS else 1.0 - abs(signed_total) / absolute_total,
    }


def all_path_exchange(paths: Mapping[str, Tuple[Sample, ...]], m_value: float, cost_unit_rd: float,
                      stride: int = 1) -> Dict[str, Dict[str, float]]:
    return {
        path_id: path_exchange(coarsen_samples(samples, stride), m_value, cost_unit_rd)
        for path_id, samples in sorted(paths.items())
    }


def segmentation_stability(paths: Mapping[str, Tuple[Sample, ...]], m_value: float,
                           cost_unit_rd: float) -> Dict[str, object]:
    native = all_path_exchange(paths, m_value, cost_unit_rd, 1)
    by_stride: Dict[str, Dict[str, float]] = {}
    all_gaps: List[float] = []
    for stride in (2, 3):
        coarse = all_path_exchange(paths, m_value, cost_unit_rd, stride)
        gaps = {
            path_id: relative_gap(native[path_id]["absolute_total_rd"], coarse[path_id]["absolute_total_rd"])
            for path_id in native
        }
        by_stride[str(stride)] = gaps
        all_gaps.extend(gaps.values())
    return {
        "relative_gap_by_stride_and_path": by_stride,
        "median_relative_gap": statistics.median(all_gaps),
        "worst_relative_gap": max(all_gaps),
    }


def summarize_branches(path_metrics: Mapping[str, Mapping[str, float]], paths: Mapping[str, Tuple[Sample, ...]],
                       delta_mode: str) -> Tuple[Dict[str, float], Dict[str, float], Optional[float]]:
    branch_values: Dict[str, List[float]] = {}
    metric_name = "absolute_total_rd" if delta_mode == "path_total" else "rate_per_time_rd"
    for path_id, metrics in path_metrics.items():
        branch = paths[path_id][0].branch
        branch_values.setdefault(branch, []).append(float(metrics[metric_name]))
    delta = {branch: statistics.median(values) for branch, values in sorted(branch_values.items())}
    lambdas = {branch: math.exp(-value) for branch, value in delta.items()}
    pi0 = None
    if all(branch in lambdas for branch in ("U", "D", "E")):
        pi0 = 3.0 * lambdas["U"] + 3.0 * lambdas["D"] + lambdas["E"]
    return delta, lambdas, pi0


def dispersion(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    mean = statistics.fmean(values)
    if abs(mean) <= EPS:
        return float("inf")
    return statistics.pstdev(values) / abs(mean)


def analyze(payload: Mapping[str, object]) -> Dict[str, object]:
    tape = parse_tape(payload)
    records = build_fit_records(tape)
    m_reader = fit_scalar(records, "reader")
    m_record = fit_scalar(records, "record")
    m_joint = fit_scalar(records, "joint")
    if m_joint <= 0:
        raise MeterError(f"estimated M must be positive; got {m_joint}")
    baseline_reader = channel_nrmse(records, m_joint, "reader")
    baseline_record = channel_nrmse(records, m_joint, "record")
    baseline_joint = joint_nrmse(records, m_joint)
    path_cv = cross_validate(records, "path_id")
    branch_cv = cross_validate(records, "branch")
    controls = {
        mode: negative_control(records, mode)
        for mode in ("shift_one", "reverse", "cross_path_same_branch")
    }
    transformed_records = [transform_record(rec) for rec in records]
    transformed_m = fit_scalar(transformed_records, "joint")
    path_metrics = all_path_exchange(tape.paths, m_joint, tape.cost_unit_rd)
    transformed_path_metrics = all_path_exchange(transform_paths(tape.paths), transformed_m, tape.cost_unit_rd)
    coordinate_cost_gap = max(
        relative_gap(path_metrics[path_id]["absolute_total_rd"],
                     transformed_path_metrics[path_id]["absolute_total_rd"])
        for path_id in path_metrics
    )
    segment = segmentation_stability(tape.paths, m_joint, tape.cost_unit_rd)
    delta, lambdas, pi0 = summarize_branches(path_metrics, tape.paths, tape.delta_mode)
    by_path_m = {
        path_id: fit_scalar(values, "joint")
        for path_id, values in sorted(group_records(records, "path_id").items())
    }
    by_branch_m = {
        branch: fit_scalar(values, "joint")
        for branch, values in sorted(group_records(records, "branch").items())
    }
    shift_control_floor = max(0.02, 5.0 * baseline_joint)
    severe_control_floor = max(0.20, 5.0 * baseline_joint)
    gates = {
        "positive_M": m_joint > 0,
        "reader_record_agreement_le_5pct": relative_gap(m_reader, m_record) <= 0.05,
        "full_fit_joint_nrmse_le_10pct": baseline_joint <= 0.10,
        "leave_one_path_out_worst_nrmse_le_15pct": float(path_cv["worst_joint_nrmse"]) <= 0.15,
        "leave_one_branch_out_worst_nrmse_le_20pct": float(branch_cv["worst_joint_nrmse"]) <= 0.20,
        "shift_control_is_worse": controls["shift_one"]["genuine_joint_nrmse"] >= shift_control_floor,
        "reverse_control_is_worse": controls["reverse"]["genuine_joint_nrmse"] >= severe_control_floor,
        "cross_path_control_is_worse": controls["cross_path_same_branch"]["genuine_joint_nrmse"] >= severe_control_floor,
        "coordinate_M_invariant": relative_gap(m_joint, transformed_m) <= 1e-12,
        "coordinate_cost_invariant": coordinate_cost_gap <= 1e-12,
        "segmentation_worst_gap_le_10pct": float(segment["worst_relative_gap"]) <= 0.10,
        "lambda_in_0_1": all(0 < value <= 1 for value in lambdas.values()),
    }
    decision = "PASS" if all(gates.values()) else "FAIL"
    downstream_enabled = decision == "PASS" and tape.path_semantics == "primitive_closure"
    report: Dict[str, object] = {
        "schema": REPORT_SCHEMA,
        "tier": "calibrated_readout/finite_diagnostic/candidate",
        "claim_boundary": (
            "Measured from this tape and its declared adapter/calibration. Not derived from the unrestricted root; "
            "not a universal M; not a physical SM identification."
        ),
        "decision": decision,
        "provenance": {
            "source_id": tape.provenance.source_id,
            "adapter_id": tape.provenance.adapter_id,
            "calibration_id": tape.provenance.calibration_id,
        },
        "path_semantics": tape.path_semantics,
        "delta_mode": tape.delta_mode,
        "cost_unit_rd": tape.cost_unit_rd,
        "sample_count": sum(len(path) for path in tape.paths.values()),
        "path_count": len(tape.paths),
        "usable_fit_records": len(records),
        "M": {
            "reader": m_reader,
            "record": m_record,
            "joint": m_joint,
            "reader_record_relative_gap": relative_gap(m_reader, m_record),
            "by_path_joint": by_path_m,
            "by_branch_joint": by_branch_m,
            "path_coefficient_of_variation": dispersion(list(by_path_m.values())),
            "branch_coefficient_of_variation": dispersion(list(by_branch_m.values())),
        },
        "fit": {
            "reader_nrmse": baseline_reader,
            "record_nrmse": baseline_record,
            "joint_nrmse": baseline_joint,
            "leave_one_path_out": path_cv,
            "leave_one_branch_out": branch_cv,
        },
        "negative_controls": controls,
        "invariance": {
            "coordinate_relabel_M_relative_gap": relative_gap(m_joint, transformed_m),
            "coordinate_relabel_cost_worst_relative_gap": coordinate_cost_gap,
            "segmentation": segment,
        },
        "path_exchange": path_metrics,
        "delta_eff_candidate_by_branch": delta,
        "lambda_candidate_by_branch": lambdas if downstream_enabled else None,
        "Pi0_candidate": pi0 if downstream_enabled else None,
        "downstream_enabled": downstream_enabled,
        "downstream_disabled_reason": None if downstream_enabled else (
            "All gates must pass and path_semantics must be primitive_closure before lambda/Pi0 are emitted."
        ),
        "gates": gates,
    }
    return report
