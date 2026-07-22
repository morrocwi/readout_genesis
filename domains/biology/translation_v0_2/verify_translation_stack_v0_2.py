#!/usr/bin/env python3
"""Fail-closed verifier for the root-to-biological semantic compiler v0.2.

This script verifies architecture and claim discipline only. It does not verify
real biology, the Standard Model, chemistry, or disease causation.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
SPEC = ROOT / "BIOLOGICAL_TRANSLATION_STACK_v0_2.yaml"
CLAIMS = ROOT / "CLAIM_BOUNDARY.json"
DRIFT = ROOT / "DRIFT_CONTRACT.json"

ROOT_STAGE = "S0_ROOT_NATIVE"
REQUIRED_MODULE_KEYS = {
    "id",
    "stage",
    "parents",
    "root_native_inputs",
    "biological_output",
    "required_observables",
    "gate",
    "controls",
    "status",
}
FORBIDDEN_ROOT_PREMISE_TOKENS = {
    "particle",
    "atom",
    "molecule",
    "gene",
    "protein",
    "enzyme",
    "membrane",
    "cell",
    "tissue",
    "immune",
    "mutation",
    "fitness",
    "cancer",
}


class VerificationError(Exception):
    pass


def load_json_compatible_yaml(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise VerificationError(f"PARSE_FAIL:{path.name}:{exc}") from exc
    if not isinstance(value, dict):
        raise VerificationError(f"TOP_LEVEL_NOT_OBJECT:{path.name}")
    return value


def require(condition: bool, code: str) -> None:
    if not condition:
        raise VerificationError(code)


def check_english_and_standalone(spec: dict[str, Any]) -> None:
    doc = spec.get("document", {})
    require(doc.get("language") == "English", "LANGUAGE_NOT_ENGLISH")
    require(doc.get("standalone") is True, "NOT_STANDALONE")
    require(doc.get("status") == "PARTIAL_UNCALIBRATED_SEMANTIC_COMPILER", "BAD_DOCUMENT_STATUS")


def check_compiler_stages(spec: dict[str, Any]) -> dict[str, dict[str, Any]]:
    stages = spec.get("compiler_stages")
    require(isinstance(stages, list) and stages, "MISSING_COMPILER_STAGES")
    index: dict[str, dict[str, Any]] = {}
    for stage in stages:
        require(isinstance(stage, dict), "BAD_STAGE_RECORD")
        sid = stage.get("id")
        require(isinstance(sid, str) and sid, "MISSING_STAGE_ID")
        require(sid not in index, f"DUPLICATE_STAGE:{sid}")
        index[sid] = stage
    for sid, stage in index.items():
        for parent in stage.get("parents", []):
            require(parent in index, f"MISSING_STAGE_PARENT:{sid}:{parent}")
    assert_acyclic({sid: list(stage.get("parents", [])) for sid, stage in index.items()}, "STAGE_DAG_CYCLE")
    return index


def check_modules(spec: dict[str, Any], stages: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    modules = spec.get("translation_modules")
    require(isinstance(modules, list) and len(modules) >= 19, "MISSING_TRANSLATION_MODULES")
    index: dict[str, dict[str, Any]] = {}
    for module in modules:
        require(isinstance(module, dict), "BAD_MODULE_RECORD")
        missing = REQUIRED_MODULE_KEYS - set(module)
        require(not missing, f"MISSING_MODULE_KEYS:{module.get('id')}:{sorted(missing)}")
        mid = module["id"]
        require(isinstance(mid, str) and mid, "MISSING_MODULE_ID")
        require(mid not in index, f"DUPLICATE_MODULE:{mid}")
        require(module["stage"] in stages, f"UNKNOWN_MODULE_STAGE:{mid}:{module['stage']}")
        require(isinstance(module["parents"], list), f"BAD_MODULE_PARENTS:{mid}")
        require(isinstance(module["required_observables"], list) and module["required_observables"], f"MISSING_OBSERVABLES:{mid}")
        require(isinstance(module["gate"], str) and module["gate"].strip(), f"MISSING_GATE:{mid}")
        controls = module["controls"]
        require(isinstance(controls, dict), f"BAD_CONTROLS:{mid}")
        require(bool(controls.get("passing")), f"MISSING_PASSING_CONTROL:{mid}")
        require(bool(controls.get("failing")), f"MISSING_FAILING_CONTROL:{mid}")
        require(module["status"] in {"Th_coqc", "finite_diagnostic", "exact_within_declared_architecture", "calibrated_readout", "Dr", "Open"}, f"BAD_STATUS:{mid}")
        index[mid] = module

    external_stage_nodes = {stage_id for stage_id in stages}
    graph: dict[str, list[str]] = {}
    for mid, module in index.items():
        parents: list[str] = []
        for parent in module["parents"]:
            require(parent in index or parent in external_stage_nodes, f"MISSING_PARENT:{mid}:{parent}")
            if parent in index:
                parents.append(parent)
        graph[mid] = parents
    assert_acyclic(graph, "MODULE_DAG_CYCLE")
    return index


def assert_acyclic(graph: dict[str, list[str]], code: str) -> None:
    temporary: set[str] = set()
    permanent: set[str] = set()

    def visit(node: str) -> None:
        if node in permanent:
            return
        if node in temporary:
            raise VerificationError(f"{code}:{node}")
        temporary.add(node)
        for parent in graph.get(node, []):
            visit(parent)
        temporary.remove(node)
        permanent.add(node)

    for node in graph:
        visit(node)


def check_no_semantic_preload(spec: dict[str, Any], stages: dict[str, dict[str, Any]]) -> None:
    root_stage = stages.get(ROOT_STAGE)
    require(root_stage is not None, "ROOT_STAGE_MISSING")
    text = json.dumps(root_stage, sort_keys=True).lower()
    violations = sorted(token for token in FORBIDDEN_ROOT_PREMISE_TOKENS if token in text)
    require(not violations, f"SEMANTIC_PRELOAD_DRIFT:{violations}")


def check_dependencies(spec: dict[str, Any]) -> None:
    deps = spec.get("dependency_stack", {})
    for name in ("root", "standard_model", "chemistry", "biology_v0_1"):
        require(name in deps, f"MISSING_DEPENDENCY:{name}")
        require(bool(deps[name].get("status")), f"MISSING_DEPENDENCY_STATUS:{name}")
    sm = json.dumps(deps["standard_model"]).lower()
    chem = json.dumps(deps["chemistry"]).lower()
    require("open_debts" in deps["standard_model"], "STANDARD_MODEL_DEBT_NOT_DECLARED")
    require("open_debts" in deps["chemistry"], "CHEMISTRY_DEBT_NOT_DECLARED")
    require("end-to-end root-derived standard model" in sm, "STANDARD_MODEL_END_TO_END_DEBT_MISSING")
    require("real atomic and molecular identity" in chem, "REAL_CHEMISTRY_DEBT_MISSING")


def check_equation_backbone(spec: dict[str, Any]) -> None:
    equations = spec.get("equation_backbone", {})
    required = {f"E{i:02d}_{name}" for i, name in [
        (0, "root"),
        (1, "operator"),
        (2, "state"),
        (3, "stepper"),
        (4, "domain_gate"),
        (5, "readout_gate"),
        (6, "viability"),
        (7, "ledger"),
        (8, "lineage"),
        (9, "cross_scale"),
        (10, "meta_defect"),
        (11, "orchestration_defect"),
        (12, "joint_admissibility"),
        (13, "repair_set"),
        (14, "onset"),
        (15, "operator_capture"),
        (16, "viability_inversion"),
    ]}
    missing = required - set(equations)
    require(not missing, f"MISSING_EQUATIONS:{sorted(missing)}")


def check_key_path(modules: dict[str, dict[str, Any]]) -> None:
    required_path = [
        "BTR-01_MOLECULAR_IDENTITY",
        "BTR-06_MEMBRANE_AND_COMPARTMENT",
        "BTR-10_CELL_IDENTITY_AND_VIABILITY",
        "BTR-12_SPATIAL_TISSUE_ORGANIZATION",
        "BTR-15_TISSUE_REPAIR_AND_CORRIGIBILITY",
        "BTR-16_UNREPORTED_DECODER_DRIFT",
        "BTR-17_CROSS_SCALE_CORRIGIBILITY_RUPTURE",
        "BTR-18_HIERARCHY_INVERSION_AND_OPERATOR_CAPTURE",
        "BTR-19_CANCER_LIKE_REGIME",
    ]
    for mid in required_path:
        require(mid in modules, f"MISSING_KEY_PATH_NODE:{mid}")


def check_claims_and_drift(claims: dict[str, Any], drift: dict[str, Any]) -> None:
    require(claims.get("tier") == "PARTIAL_UNCALIBRATED_SEMANTIC_COMPILER", "CLAIM_TIER_INFLATION")
    not_established = json.dumps(claims.get("not_established", [])).lower()
    require("end-to-end standard model" in not_established, "SM_NONCLAIM_MISSING")
    require("calibrated encoder" in not_established, "BIO_CALIBRATION_NONCLAIM_MISSING")
    require(claims.get("relation_to_biology_v0_1", {}).get("closure_score_changed") is False, "V0_1_SCORE_MUTATED")
    hard_fails = drift.get("hard_fail_conditions", [])
    require(isinstance(hard_fails, list) and len(hard_fails) >= 15, "DRIFT_CONTRACT_TOO_WEAK")
    required_codes = set(drift.get("required_failure_codes", []))
    for code in ("SEMANTIC_PRELOAD_DRIFT", "STANDARD_MODEL_TIER_INFLATION", "CHEMISTRY_SEMANTIC_INFLATION", "CORRIGIBILITY_UNRESOLVED", "OPERATOR_CAPTURE_UNRESOLVED"):
        require(code in required_codes, f"MISSING_FAILURE_CODE:{code}")


def run_negative_controls(spec: dict[str, Any]) -> list[str]:
    passed: list[str] = []

    bad_stage = {"id": "S0_ROOT_NATIVE", "parents": [], "output": "cell mutation cancer", "tier": "Th_coqc", "biological_semantics": False}
    try:
        check_no_semantic_preload(spec, {ROOT_STAGE: bad_stage})
    except VerificationError as exc:
        require(str(exc).startswith("SEMANTIC_PRELOAD_DRIFT"), "NEGATIVE_CONTROL_WRONG_FAILURE:semantic_preload")
        passed.append("semantic_preload_rejected")
    else:
        raise VerificationError("NEGATIVE_CONTROL_FAILED:semantic_preload")

    bad_graph = {"A": ["B"], "B": ["A"]}
    try:
        assert_acyclic(bad_graph, "DAG_CYCLE")
    except VerificationError as exc:
        require(str(exc).startswith("DAG_CYCLE"), "NEGATIVE_CONTROL_WRONG_FAILURE:cycle")
        passed.append("cycle_rejected")
    else:
        raise VerificationError("NEGATIVE_CONTROL_FAILED:cycle")

    bad_module = {
        "id": "BAD",
        "stage": "S3_BIOMOLECULAR",
        "parents": [],
        "root_native_inputs": [],
        "biological_output": "bad",
        "required_observables": [],
        "gate": "",
        "controls": {"passing": "", "failing": ""},
        "status": "Open",
    }
    bad_spec = dict(spec)
    bad_spec["translation_modules"] = [bad_module for _ in range(19)]
    try:
        check_modules(bad_spec, {"S3_BIOMOLECULAR": {"id": "S3_BIOMOLECULAR", "parents": []}})
    except VerificationError:
        passed.append("incomplete_module_rejected")
    else:
        raise VerificationError("NEGATIVE_CONTROL_FAILED:incomplete_module")

    return passed


def main() -> int:
    try:
        spec = load_json_compatible_yaml(SPEC)
        claims = load_json_compatible_yaml(CLAIMS)
        drift = load_json_compatible_yaml(DRIFT)
        check_english_and_standalone(spec)
        stages = check_compiler_stages(spec)
        check_no_semantic_preload(spec, stages)
        check_dependencies(spec)
        check_equation_backbone(spec)
        modules = check_modules(spec, stages)
        check_key_path(modules)
        check_claims_and_drift(claims, drift)
        negatives = run_negative_controls(spec)
    except VerificationError as exc:
        print(json.dumps({"decision": "FAIL", "error": str(exc)}, indent=2))
        return 1

    result = {
        "decision": "PASS",
        "scope": "architecture and claim discipline only",
        "document": spec["document"]["id"],
        "compiler_stages": len(stages),
        "translation_modules": len(modules),
        "negative_controls": negatives,
        "real_biology": "UNRESOLVED",
        "standard_model_end_to_end": "OPEN",
        "real_chemistry": "OPEN",
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
