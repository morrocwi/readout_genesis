#!/usr/bin/env python3
"""Native-RD primitive-branch parameter reduction engine v0.1.

Closes the operational subchain
    calibrated M -> primitive U/D/E tapes -> Delta_j -> lambda_j -> Pi0
without treating C_RD or branch lambdas as tunable inputs.

Tier: declared_finite_architecture / calibrated_readout / finite_diagnostic.
This is not an unrestricted-root derivation and does not certify a laboratory U/D/E encoding.

REQUIRED CORRECTIONS applied after independent adversarial review (2026-07-25):
(1) `primitive_certificate` fields (`no_internal_reset`, `orientation_quotiented`,
    `branch_encoding_tier`) are checked ONLY for presence/exact-match against caller-supplied
    values in `validate_payload` -- they are NEVER independently verified against the actual
    `phi`/`psi` trajectory arrays. A caller could declare `no_internal_reset=True` on a tape that
    in fact resets internally and this gate would not catch it. Unlike the "does not certify a
    laboratory U/D/E encoding" disclaimer (which correctly scopes the PHYSICS claim), this is a
    narrower, previously-undisclosed limitation on the ARCHITECTURAL/mathematical claims
    themselves -- see `SELF_DECLARED_UNVERIFIED_CERTIFICATE_FIELDS` below and its use in
    `analyze()`'s returned report.
(2) The `parameter_reduction.after_count=0` claim is corrected: the 3 branches' initial
    conditions (`primitive_branch_fixture_v0_1.py`'s `BRANCH_INITIAL_CONDITIONS`, currently
    phi0=0.2/0.5/0.8, unexplained/undocumented) are NOT counted as dials in the original 5-dial
    list, yet they deterministically fix `lambda_U/D/E` (and `Pi0` is highly sensitive to them,
    branch E dominates the sum) through the same fixed stepper. This closure does not eliminate
    that freedom -- it RELOCATES it from the 3 named lambda dials into 3 (or more; each is a
    4-tuple) unexplained initial-condition choices. See `parameter_reduction["relocated_not_
    eliminated"]` below, added by this correction.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Mapping, Sequence

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from domains.standard_model.item1_exploration.retained_transition_operational_closure.operational_exchange_estimator_v0_1 import (  # noqa: E402
    exchange_path,
    pi0_from_branch_lambdas,
)

SCHEMA = "primitive-branch-tape-set-v0.1"
NATIVE_UNIT_ID = "native-rd-v1"
NATIVE_COST_UNIT_RD = 1.0
REQUIRED_BRANCHES = ("U", "D", "E")
MAX_SEGMENTATION_GAP = 0.01
EPS = 1e-15

# Disclosed, not fixed: these certificate fields are checked for presence/exact-match only, never
# cross-verified against the actual phi/psi trajectory arrays (required correction, 2026-07-25 review).
SELF_DECLARED_UNVERIFIED_CERTIFICATE_FIELDS = (
    "primitive_certificate.no_internal_reset",
    "primitive_certificate.orientation_quotiented",
    "primitive_certificate.branch_encoding_tier",
)


class ContractError(ValueError):
    """Fail-closed primitive-branch contract error."""


def _finite_vector(value: object, field: str) -> np.ndarray:
    if not isinstance(value, list) or len(value) < 5:
        raise ContractError(f"{field} must be a numeric list with at least five samples")
    try:
        arr = np.asarray(value, dtype=float)
    except (TypeError, ValueError) as exc:
        raise ContractError(f"{field} contains a nonnumeric value") from exc
    if arr.ndim != 1 or not np.all(np.isfinite(arr)):
        raise ContractError(f"{field} must be a finite one-dimensional array")
    return arr


def _required_text(mapping: Mapping[str, object], key: str, field: str) -> str:
    value = str(mapping.get(key, "")).strip()
    if not value:
        raise ContractError(f"{field}.{key} is required")
    return value


def _coarsen(values: np.ndarray, stride: int) -> np.ndarray:
    idx = list(range(0, len(values), stride))
    if idx[-1] != len(values) - 1:
        idx.append(len(values) - 1)
    return values[idx]


def _relative_gap(a: float, b: float) -> float:
    return abs(float(a) - float(b)) / max(abs(float(a)), abs(float(b)), EPS)


def validate_payload(payload: Mapping[str, object]) -> Mapping[str, object]:
    if payload.get("schema") != SCHEMA:
        raise ContractError(f"expected schema {SCHEMA}")

    native = payload.get("native_unit")
    if not isinstance(native, dict):
        raise ContractError("native_unit object is required")
    if native.get("unit_id") != NATIVE_UNIT_ID:
        raise ContractError(f"native_unit.unit_id must be {NATIVE_UNIT_ID}")
    try:
        cost_unit = float(native["cost_unit_rd"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ContractError("native_unit.cost_unit_rd must be numeric") from exc
    if cost_unit != NATIVE_COST_UNIT_RD:
        raise ContractError("C_RD is gauge-fixed by the native RD unit and must equal exactly 1")
    if native.get("is_tunable") is not False:
        raise ContractError("native_unit.is_tunable must be false")

    if payload.get("delta_is_dimensionless") is not True:
        raise ContractError("delta_is_dimensionless must be true")

    calibration = payload.get("m_calibration")
    if not isinstance(calibration, dict):
        raise ContractError("m_calibration object is required")
    if calibration.get("status") != "CALIBRATED_READY":
        raise ContractError("m_calibration.status must be CALIBRATED_READY")
    calibration_id = _required_text(calibration, "calibration_id", "m_calibration")
    try:
        m_joint = float(calibration["M_joint"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ContractError("m_calibration.M_joint must be numeric") from exc
    if not math.isfinite(m_joint) or m_joint <= 0:
        raise ContractError("m_calibration.M_joint must be finite and positive")

    raw_branches = payload.get("branches")
    if not isinstance(raw_branches, list) or len(raw_branches) != 3:
        raise ContractError("branches must contain exactly U, D, and E")

    parsed = {}
    seen_paths = set()
    seen_initial_conditions = set()
    trajectory_signatures = set()
    for index, raw in enumerate(raw_branches):
        field = f"branches[{index}]"
        if not isinstance(raw, dict):
            raise ContractError(f"{field} must be an object")
        branch = str(raw.get("branch", "")).strip()
        if branch not in REQUIRED_BRANCHES:
            raise ContractError(f"{field}.branch must be U, D, or E")
        if branch in parsed:
            raise ContractError(f"duplicate branch {branch}")
        if raw.get("path_semantics") != "primitive_closure":
            raise ContractError(f"{field}.path_semantics must be primitive_closure")
        if raw.get("delta_is_dimensionless") is not True:
            raise ContractError(f"{field}.delta_is_dimensionless must be true")

        provenance = raw.get("provenance")
        if not isinstance(provenance, dict):
            raise ContractError(f"{field}.provenance is required")
        path_id = _required_text(provenance, "path_id", f"{field}.provenance")
        _required_text(provenance, "source_id", f"{field}.provenance")
        _required_text(provenance, "adapter_id", f"{field}.provenance")
        branch_calibration_id = _required_text(provenance, "calibration_id", f"{field}.provenance")
        initial_condition_id = _required_text(provenance, "initial_condition_id", f"{field}.provenance")
        if branch_calibration_id != calibration_id:
            raise ContractError(f"{field} calibration_id does not match m_calibration")
        if path_id in seen_paths:
            raise ContractError("branch path_id values must be independent")
        if initial_condition_id in seen_initial_conditions:
            raise ContractError("branch initial_condition_id values must be independent")
        seen_paths.add(path_id)
        seen_initial_conditions.add(initial_condition_id)

        # NOTE (required correction, 2026-07-25 review): the three checks below confirm the
        # caller DECLARED these properties -- they do NOT verify them against phi/times/psi
        # below. A tape that actually resets internally, or is not orientation-quotiented, would
        # still pass here if its certificate dict simply asserts otherwise. See
        # SELF_DECLARED_UNVERIFIED_CERTIFICATE_FIELDS and analyze()'s claim_boundary.
        certificate = raw.get("primitive_certificate")
        if not isinstance(certificate, dict):
            raise ContractError(f"{field}.primitive_certificate is required")
        _required_text(certificate, "rule_id", f"{field}.primitive_certificate")
        if certificate.get("no_internal_reset") is not True:
            raise ContractError(f"{field} primitive path must have no internal reset")
        if certificate.get("orientation_quotiented") is not True:
            raise ContractError(f"{field} primitive path must declare orientation quotienting")
        if certificate.get("branch_encoding_tier") != "declared_finite_architecture":
            raise ContractError(f"{field} branch_encoding_tier must be declared_finite_architecture")

        times = _finite_vector(raw.get("times"), f"{field}.times")
        phi = _finite_vector(raw.get("phi"), f"{field}.phi")
        psi = _finite_vector(raw.get("psi"), f"{field}.psi")
        if not (len(times) == len(phi) == len(psi)):
            raise ContractError(f"{field} times/phi/psi lengths differ")
        if np.any(np.diff(times) <= 0):
            raise ContractError(f"{field}.times must be strictly increasing")
        signature = (tuple(np.round(phi, 14)), tuple(np.round(psi, 14)))
        if signature in trajectory_signatures:
            raise ContractError("U/D/E trajectories must not be duplicate copies")
        trajectory_signatures.add(signature)
        parsed[branch] = {
            "raw": raw,
            "times": times,
            "phi": phi,
            "psi": psi,
            "path_id": path_id,
            "initial_condition_id": initial_condition_id,
        }

    if tuple(sorted(parsed)) != tuple(sorted(REQUIRED_BRANCHES)):
        raise ContractError("branches must be exactly U, D, and E")

    return {
        "M_joint": m_joint,
        "calibration_id": calibration_id,
        "branches": parsed,
    }


def analyze(payload: Mapping[str, object]) -> Mapping[str, object]:
    parsed = validate_payload(payload)
    m_joint = float(parsed["M_joint"])
    branch_reports = {}
    lambdas = {}

    for branch in REQUIRED_BRANCHES:
        item = parsed["branches"][branch]
        times = item["times"]
        phi = item["phi"]
        psi = item["psi"]
        native = exchange_path(
            phi,
            psi,
            times,
            M_value=m_joint,
            cost_unit_rd=NATIVE_COST_UNIT_RD,
            path_semantics="primitive_closure",
            delta_is_dimensionless=True,
        )
        if native["status"] != "CALIBRATED_READY" or native["lambda"] is None:
            raise ContractError(f"branch {branch} did not produce a calibrated primitive closure")

        gaps = {}
        for stride in (2, 3):
            coarse = exchange_path(
                _coarsen(phi, stride),
                _coarsen(psi, stride),
                _coarsen(times, stride),
                M_value=m_joint,
                cost_unit_rd=NATIVE_COST_UNIT_RD,
                path_semantics="primitive_closure",
                delta_is_dimensionless=True,
            )
            gap = _relative_gap(native["Delta_candidate"], coarse["Delta_candidate"])
            gaps[str(stride)] = gap
            if gap > MAX_SEGMENTATION_GAP:
                raise ContractError(
                    f"branch {branch} segmentation gap {gap:.3%} exceeds {MAX_SEGMENTATION_GAP:.1%}"
                )

        value = float(native["lambda"])
        lambdas[branch] = value
        branch_reports[branch] = {
            "path_id": item["path_id"],
            "initial_condition_id": item["initial_condition_id"],
            "signed_exchange_total_rd": float(native["signed_exchange_total_rd"]),
            "Delta": float(native["Delta_candidate"]),
            "lambda": value,
            "orientation_cancellation_fraction": float(native["orientation_cancellation_fraction"]),
            "segmentation_relative_gap": gaps,
            "status": "CALIBRATED_READY",
        }

    pi0 = pi0_from_branch_lambdas(lambdas)
    if pi0 is None:
        raise ContractError("Pi0 requires all U/D/E branch lambdas")

    return {
        "schema": "primitive-branch-parameter-reduction-report-v0.1",
        "status": "CALIBRATED_READY",
        "tier": "declared_finite_architecture / calibrated_readout / finite_diagnostic",
        "native_unit": {
            "unit_id": NATIVE_UNIT_ID,
            "C_RD": NATIVE_COST_UNIT_RD,
            "status": "GAUGE_FIXED_NOT_TUNABLE",
        },
        "M_joint": m_joint,
        "m_calibration_id": parsed["calibration_id"],
        "branches": branch_reports,
        "Pi0": float(pi0),
        "parameter_reduction": {
            "before_operational_dials": ["M", "C_RD", "lambda_U", "lambda_D", "lambda_E"],
            "before_count": 5,
            "after_free_dials": [],
            "after_count": 0,
            "calibrated_outputs": ["M"],
            "native_unit_gauge_fixed": ["C_RD"],
            "computed_outputs": ["lambda_U", "lambda_D", "lambda_E", "Pi0"],
            "not_reduced_here": ["alpha", "beta", "physical gauge couplings", "Yukawa data"],
            # REQUIRED CORRECTION (2026-07-25 review): the 5 named dials above are genuinely
            # removed from THAT list, but the freedom does not vanish -- it relocates into the
            # branch tapes' initial conditions (currently 3 hardcoded, undocumented 4-tuples in
            # primitive_branch_fixture_v0_1.py's BRANCH_INITIAL_CONDITIONS), which deterministically
            # fix lambda_U/D/E (and Pi0 is highly sensitive to them). "after_count=0" therefore
            # describes only the named-dial subchain, not the full degrees of freedom in this
            # construction -- do not read it as "zero remaining free choices."
            "relocated_not_eliminated": [
                "branch initial conditions (phi0/phi1/psi0/psi1 per branch, 3 branches) are "
                "currently unexplained/undocumented free choices that deterministically set "
                "lambda_U, lambda_D, lambda_E through the fixed stepper -- this closure moves "
                "freedom out of the named 5 dials, it does not remove it from the construction",
            ],
        },
        "claim_boundary": [
            "five NAMED operational dials (M, C_RD, lambda_U, lambda_D, lambda_E) are removed "
            "from this declared finite-architecture subchain -- this is narrower than \"zero "
            "free choices remain\", see parameter_reduction.relocated_not_eliminated",
            "branch tapes and provenance remain empirical/architectural inputs, not fitted constants",
            "does not prove that fixture U/D/E encodings are laboratory Standard-Model branches",
            "does not derive alpha or beta and does not by itself prove Pi0 > alpha",
            "primitive_certificate fields (no_internal_reset, orientation_quotiented, "
            "branch_encoding_tier) are checked for presence/exact-match only -- they are "
            "self-declared by the caller and NOT independently verified against the tape's own "
            "phi/psi data, see SELF_DECLARED_UNVERIFIED_CERTIFICATE_FIELDS",
        ],
    }
