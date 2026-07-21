from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_dag(dag):
    nodes = {n["id"]: n for n in dag["nodes"]}
    errors = []
    adjacency = {n: [] for n in nodes}
    indeg = {n: 0 for n in nodes}
    for a, b in dag["edges"]:
        if a not in nodes or b not in nodes:
            errors.append(f"unknown DAG edge {a}->{b}")
            continue
        adjacency[a].append(b)
        indeg[b] += 1
    queue = [n for n, d in indeg.items() if d == 0]
    visited = 0
    while queue:
        n = queue.pop()
        visited += 1
        for m in adjacency[n]:
            indeg[m] -= 1
            if indeg[m] == 0:
                queue.append(m)
    if visited != len(nodes):
        errors.append("DAG contains a cycle")
    return nodes, errors


def validate_registry(nodes, registry, contract):
    errors = []
    allowed = set(contract["allowed_rule_classes"])
    ids = set()
    forbidden_parent_types = {"EMPIRICAL_TAPE", "DISCOVERED_DOMAIN_LAW", "CALIBRATED_READOUT", "NUMERICAL_PROCEDURE"}
    for rule in registry["rules"]:
        rid = rule["rule_id"]
        if rid in ids:
            errors.append(f"duplicate rule id {rid}")
        ids.add(rid)
        if rule["class"] not in allowed:
            errors.append(f"unknown rule class {rule['class']}")
        for parent in rule["parents"]:
            if parent not in nodes:
                errors.append(f"rule {rid} has unknown parent {parent}")
            elif rule["class"] == "ROOT_THEOREM" and nodes[parent]["type"] in forbidden_parent_types:
                errors.append(f"root theorem {rid} depends on forbidden parent type {nodes[parent]['type']}")
        if not rule.get("forbidden_claims"):
            errors.append(f"rule {rid} lacks forbidden_claims")
    return errors


def scan_imported_tokens(contract):
    hits = []
    for name in contract["active_files_scanned_for_imported_laws"]:
        text = (ROOT / name).read_text(encoding="utf-8").lower()
        for token in contract["prohibited_active_domain_tokens"]:
            if token.lower() in text:
                hits.append({"file": name, "token": token})
    return hits


def validate_standalone():
    required = [
        "ROOT_DAG_MASTER_v0_901.json", "ROOT_DAG_MASTER_v0_901.md", "ROOT_DAG_DELTA_v0_901.json",
        "RULE_REGISTRY_v0_901.json", "DRIFT_CONTRACT_v0_901.json", "CLAIM_BOUNDARY_v0_901.json",
        "SOURCE_LOCKS_v0_901.json", "STANDALONE_MANIFEST_v0_901.json", "RELEASE_MANIFEST_v0_901.json",
        "README.md", "run_all_tests_v0_901.py", "proof_kernel_v0_901.py", "checker_v0_901.py",
        "anchor_v0_1/INFORMATION_CHEMISTRY_CANON_v0_1_STANDALONE.yaml",
        "anchor_v0_1/information_chemistry_kernel_v0_1.py",
        "anchor_v0_900/INFORMATION_CHEMISTRY_v0_900_ROOT_NATIVE_PEER_REVIEW_CHARTER_TH.md",
        "anchor_v0_900/INFORMATION_CHEMISTRY_v0_900_ROOT_NATIVE_PEER_REVIEW_CHARTER.json",
        "source_root/READOUT_GENESIS_CORE_SNAPSHOT.md"
    ]
    missing = [name for name in required if not (ROOT / name).is_file()]
    return missing


def run_drift_audit():
    dag = load("ROOT_DAG_MASTER_v0_901.json")
    registry = load("RULE_REGISTRY_v0_901.json")
    contract = load("DRIFT_CONTRACT_v0_901.json")
    nodes, errors = validate_dag(dag)
    errors.extend(validate_registry(nodes, registry, contract))
    imported_hits = scan_imported_tokens(contract)
    if imported_hits:
        errors.append("prohibited imported-domain tokens found in active files")
    missing = validate_standalone()
    if missing:
        errors.append("standalone files missing")
    result = {
        "version": "0.901",
        "dag_sha256": sha256(ROOT / "ROOT_DAG_MASTER_v0_901.json"),
        "rule_registry_sha256": sha256(ROOT / "RULE_REGISTRY_v0_901.json"),
        "errors": errors,
        "imported_token_hits": imported_hits,
        "missing_standalone_files": missing,
        "decision": "PASS" if not errors else "FAIL"
    }
    return result


if __name__ == "__main__":
    result = run_drift_audit()
    (ROOT / "DRIFT_AUDIT_v0_901.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
