#!/usr/bin/env python3
"""Core parsing and finite-difference layer for Retained Transition Meter v0.2."""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

EPS = 1e-14
SCHEMA = "retained-transition-tape-v0.2"
REPORT_SCHEMA = "retained-transition-meter-report-v0.2"
ALLOWED_DELTA_MODES = {"path_total", "rate_per_time"}
ALLOWED_PATH_SEMANTICS = {"primitive_closure", "observed_trajectory"}


class MeterError(ValueError):
    """Hard-fail input or identifiability error."""


def dot(a: Sequence[float], b: Sequence[float]) -> float:
    if len(a) != len(b):
        raise MeterError(f"dimension mismatch: {len(a)} != {len(b)}")
    return sum(float(x) * float(y) for x, y in zip(a, b))


def vec_add(*vectors: Sequence[float]) -> Tuple[float, ...]:
    if not vectors:
        raise MeterError("vec_add requires at least one vector")
    dim = len(vectors[0])
    if any(len(v) != dim for v in vectors):
        raise MeterError("dimension mismatch in vec_add")
    return tuple(sum(float(v[i]) for v in vectors) for i in range(dim))


def vec_scale(scale: float, vector: Sequence[float]) -> Tuple[float, ...]:
    return tuple(float(scale) * float(x) for x in vector)


def vec_sub(a: Sequence[float], b: Sequence[float]) -> Tuple[float, ...]:
    if len(a) != len(b):
        raise MeterError("dimension mismatch in subtraction")
    return tuple(float(x) - float(y) for x, y in zip(a, b))


def rms(values: Iterable[float]) -> float:
    xs = [float(x) for x in values]
    if not xs:
        return 0.0
    return math.sqrt(sum(x * x for x in xs) / len(xs))


def relative_gap(a: float, b: float) -> float:
    return abs(float(a) - float(b)) / max(abs(float(a)), abs(float(b)), EPS)


def tuple_numeric(value: object, field: str) -> Tuple[float, ...]:
    if not isinstance(value, list) or not value:
        raise MeterError(f"{field} must be a non-empty numeric list")
    try:
        result = tuple(float(x) for x in value)
    except (TypeError, ValueError) as exc:
        raise MeterError(f"{field} contains a non-numeric value") from exc
    if any(not math.isfinite(x) for x in result):
        raise MeterError(f"{field} contains a non-finite value")
    return result


def component_vector(raw: Mapping[str, object], name: str, dim: int) -> Tuple[float, ...]:
    if name not in raw:
        return tuple(0.0 for _ in range(dim))
    value = tuple_numeric(raw[name], name)
    if len(value) != dim:
        raise MeterError(f"component {name} dimension mismatch")
    return value


def resolve_load(raw: Mapping[str, object], channel: str, dim: int, field: str) -> Optional[Tuple[float, ...]]:
    direct_key = f"{channel}_load"
    component_key = f"{channel}_components"
    direct_present = direct_key in raw and raw[direct_key] is not None
    component_present = component_key in raw and raw[component_key] is not None
    if direct_present and component_present:
        raise MeterError(f"{field}: supply {direct_key} OR {component_key}, not both")
    if direct_present:
        value = tuple_numeric(raw[direct_key], f"{field}.{direct_key}")
        if len(value) != dim:
            raise MeterError(f"{field}.{direct_key} dimension mismatch")
        return value
    if not component_present:
        return None
    components = raw[component_key]
    if not isinstance(components, dict):
        raise MeterError(f"{field}.{component_key} must be an object")
    if channel == "reader":
        return vec_add(
            component_vector(components, "residual", dim),
            component_vector(components, "source", dim),
            vec_scale(-1.0, component_vector(components, "damping", dim)),
            vec_scale(-1.0, component_vector(components, "transport", dim)),
            vec_scale(-1.0, component_vector(components, "potential", dim)),
        )
    if channel == "record":
        return vec_add(
            component_vector(components, "residual", dim),
            component_vector(components, "damping", dim),
            vec_scale(-1.0, component_vector(components, "transport", dim)),
            vec_scale(-1.0, component_vector(components, "hessian", dim)),
        )
    raise MeterError(f"unknown channel {channel}")


@dataclass(frozen=True)
class Provenance:
    source_id: str
    adapter_id: str
    calibration_id: str


@dataclass(frozen=True)
class Sample:
    path_id: str
    branch: str
    time: float
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


@dataclass(frozen=True)
class ParsedTape:
    cost_unit_rd: float
    delta_mode: str
    path_semantics: str
    provenance: Provenance
    paths: Mapping[str, Tuple[Sample, ...]]


def parse_tape(payload: Mapping[str, object]) -> ParsedTape:
    if payload.get("schema") != SCHEMA:
        raise MeterError(f"expected schema {SCHEMA}")
    try:
        cost_unit_rd = float(payload["cost_unit_rd"])
    except (KeyError, TypeError, ValueError) as exc:
        raise MeterError("cost_unit_rd must be numeric") from exc
    if not math.isfinite(cost_unit_rd) or cost_unit_rd <= 0:
        raise MeterError("cost_unit_rd must be finite and positive")
    if payload.get("delta_is_dimensionless") is not True:
        raise MeterError("delta_is_dimensionless must be true before lambda=exp(-Delta) is admissible")
    delta_mode = str(payload.get("delta_mode", "")).strip()
    if delta_mode not in ALLOWED_DELTA_MODES:
        raise MeterError(f"delta_mode must be one of {sorted(ALLOWED_DELTA_MODES)}")
    path_semantics = str(payload.get("path_semantics", "")).strip()
    if path_semantics not in ALLOWED_PATH_SEMANTICS:
        raise MeterError(f"path_semantics must be one of {sorted(ALLOWED_PATH_SEMANTICS)}")
    raw_provenance = payload.get("provenance")
    if not isinstance(raw_provenance, dict):
        raise MeterError("provenance object is required")
    provenance_values = {}
    for key in ("source_id", "adapter_id", "calibration_id"):
        value = str(raw_provenance.get(key, "")).strip()
        if not value:
            raise MeterError(f"provenance.{key} is required")
        provenance_values[key] = value
    provenance = Provenance(**provenance_values)

    raw_samples = payload.get("samples")
    if not isinstance(raw_samples, list) or len(raw_samples) < 9:
        raise MeterError("samples must contain at least nine entries")

    path_lists: Dict[str, List[Sample]] = {}
    expected_dim: Optional[int] = None
    path_branches: Dict[str, str] = {}
    for idx, raw in enumerate(raw_samples):
        field = f"samples[{idx}]"
        if not isinstance(raw, dict):
            raise MeterError(f"{field} is not an object")
        path_id = str(raw.get("path_id", "")).strip()
        branch = str(raw.get("branch", "")).strip()
        if not path_id or not branch:
            raise MeterError(f"{field} needs path_id and branch")
        try:
            time = float(raw["time"])
        except (KeyError, TypeError, ValueError) as exc:
            raise MeterError(f"{field}.time must be numeric") from exc
        if not math.isfinite(time):
            raise MeterError(f"{field}.time must be finite")
        phi = tuple_numeric(raw.get("phi"), f"{field}.phi")
        psi = tuple_numeric(raw.get("psi"), f"{field}.psi")
        if len(phi) != len(psi):
            raise MeterError(f"{field} phi/psi dimension mismatch")
        if expected_dim is None:
            expected_dim = len(phi)
        if len(phi) != expected_dim:
            raise MeterError("all samples must use one state dimension")
        if path_id in path_branches and path_branches[path_id] != branch:
            raise MeterError(f"branch changes inside path {path_id}")
        path_branches[path_id] = branch
        reader_load = resolve_load(raw, "reader", expected_dim, field)
        record_load = resolve_load(raw, "record", expected_dim, field)
        path_lists.setdefault(path_id, []).append(
            Sample(path_id, branch, time, phi, psi, reader_load, record_load)
        )

    if len(path_lists) < 3:
        raise MeterError("at least three independent paths are required")
    if len(set(path_branches.values())) < 2:
        raise MeterError("at least two branches are required for leave-one-branch-out transport")
    paths: Dict[str, Tuple[Sample, ...]] = {}
    for path_id, values in sorted(path_lists.items()):
        ordered = sorted(values, key=lambda s: s.time)
        if len(ordered) < 5:
            raise MeterError(f"path {path_id} needs at least five samples")
        times = [s.time for s in ordered]
        if any(t1 <= t0 for t0, t1 in zip(times, times[1:])):
            raise MeterError(f"path {path_id} times must be strictly increasing")
        paths[path_id] = tuple(ordered)
    return ParsedTape(cost_unit_rd, delta_mode, path_semantics, provenance, paths)


def irregular_second_difference(prev: Sample, cur: Sample, nxt: Sample, field: str) -> Tuple[float, ...]:
    h0 = cur.time - prev.time
    h1 = nxt.time - cur.time
    if h0 <= 0 or h1 <= 0:
        raise MeterError("non-positive time interval")
    x0 = prev.phi if field == "phi" else prev.psi
    x1 = cur.phi if field == "phi" else cur.psi
    x2 = nxt.phi if field == "phi" else nxt.psi
    slope0 = vec_scale(1.0 / h0, vec_sub(x1, x0))
    slope1 = vec_scale(1.0 / h1, vec_sub(x2, x1))
    return vec_scale(2.0 / (h0 + h1), vec_sub(slope1, slope0))


def build_fit_records(tape: ParsedTape) -> List[FitRecord]:
    records: List[FitRecord] = []
    for path_id, samples in tape.paths.items():
        for local_index in range(1, len(samples) - 1):
            prev, cur, nxt = samples[local_index - 1:local_index + 2]
            if cur.reader_load is None or cur.record_load is None:
                continue
            records.append(FitRecord(
                path_id=path_id,
                branch=cur.branch,
                local_index=local_index,
                acc_phi=irregular_second_difference(prev, cur, nxt, "phi"),
                acc_psi=irregular_second_difference(prev, cur, nxt, "psi"),
                reader_load=cur.reader_load,
                record_load=cur.record_load,
            ))
    if len(records) < 12:
        raise MeterError("fewer than twelve usable interior records; M is unidentifiable")
    return records
