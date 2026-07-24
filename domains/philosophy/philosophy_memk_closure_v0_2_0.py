#!/usr/bin/env python3
"""Primary structural verifier for Philosophy/MEMK v0.2.0 and the current IEF companion."""
from __future__ import annotations
import base64, gzip, hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "artifacts"
PREFIX = "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part"
EXPECTED_MD_SHA = "ff8cbf6848d93f7579327dc628e25e91801d959669de4235fcdfbcb347f7a926"
EXPECTED_GZIP_SHA = "a05dabea3dd44c7fc07fddd19246bc382c2c35faef48f73453b0eab77ebc58f1"
EXPECTED_PARTS = 19
REQUIRED = [
    "README.md", "PHILOSOPHY_MEMK_DOMAIN_v0_2_0.yaml",
    "FOUNDATION_RELEASE_REGISTRY_PHILOSOPHY_MEMK.yaml",
    "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.validation.yaml",
    "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.2.0.validation.yaml",
    "CLAIM_BOUNDARY_PHILOSOPHY_MEMK.json", "RULE_REGISTRY_PHILOSOPHY_MEMK.json",
    "ROOT_DAG_MASTER_PHILOSOPHY_MEMK.json", "DRIFT_CONTRACT_PHILOSOPHY_MEMK.json",
    "source_root/READOUT_GENESIS_CORE_SNAPSHOT.md", "PROOF_RECEIPT_PHILOSOPHY_MEMK.json",
    "CLOSURE_AUDIT_PHILOSOPHY_MEMK.json", "CHECKSUMS_SHA256_PHILOSOPHY_MEMK.txt",
    "artifacts/README.md", "artifacts/rebuild_information_epistemic_foundation_v1_6_0.py",
]


def load_json(name: str):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def acyclic(graph: dict) -> bool:
    nodes = set(graph["nodes"]); edges = [tuple(edge) for edge in graph["edges"]]
    indegree = {node: 0 for node in nodes}; children = {node: [] for node in nodes}
    for parent, child in edges:
        if parent not in nodes or child not in nodes: return False
        indegree[child] += 1; children[parent].append(child)
    queue = [node for node, degree in indegree.items() if degree == 0]; seen = 0
    while queue:
        node = queue.pop(); seen += 1
        for child in children[node]:
            indegree[child] -= 1
            if indegree[child] == 0: queue.append(child)
    return seen == len(nodes)


def verify_checksums() -> bool:
    rows = 0
    for line in (HERE / "CHECKSUMS_SHA256_PHILOSOPHY_MEMK.txt").read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"): continue
        expected, rel = line.split("  ", 1); rows += 1
        if hashlib.sha256((HERE / rel).read_bytes()).hexdigest() != expected: return False
    return rows > 0


def verify_archive() -> bool:
    try:
        parts = sorted(ART.glob(f"{PREFIX}*"))
        if len(parts) != EXPECTED_PARTS: return False
        compressed = base64.b64decode("".join(p.read_text(encoding="ascii").strip() for p in parts), validate=True)
        if hashlib.sha256(compressed).hexdigest() != EXPECTED_GZIP_SHA: return False
        markdown = gzip.decompress(compressed)
        if hashlib.sha256(markdown).hexdigest() != EXPECTED_MD_SHA: return False
        text = markdown.decode("utf-8")
        required = ["root_native_closure_v1_3:", "maker_checker_firewall:",
                    "AGENCY_META_READOUT_GOVERNANCE_v1.6.0_ARCHITECTURE_CLOSED", "flowchart TD"]
        forbidden = ["compenmeta_governanceng", "meta_governancesfies", "cesmeta_governanceon",
                     "Cesmeta_governanceon", "meta_governancesfy"]
        return all(token in text for token in required) and not any(token in text for token in forbidden)
    except Exception:
        return False


def run():
    claim = load_json("CLAIM_BOUNDARY_PHILOSOPHY_MEMK.json")
    graph = load_json("ROOT_DAG_MASTER_PHILOSOPHY_MEMK.json")
    rules = load_json("RULE_REGISTRY_PHILOSOPHY_MEMK.json")["rules"]
    drift = load_json("DRIFT_CONTRACT_PHILOSOPHY_MEMK.json")
    spec = (HERE / "PHILOSOPHY_MEMK_DOMAIN_v0_2_0.yaml").read_text(encoding="utf-8")
    registry = (HERE / "FOUNDATION_RELEASE_REGISTRY_PHILOSOPHY_MEMK.yaml").read_text(encoding="utf-8")
    validation = (HERE / "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.validation.yaml").read_text(encoding="utf-8")
    results = {
        "required_files": all((HERE / path).is_file() for path in REQUIRED),
        "claim_tier": claim["tier"] == "ARCHITECTURE_CONDITIONAL_UNRESOLVED_DOMAIN",
        "exact_q_unresolved": claim["statuses"]["exact_domain_quotient"] == "UNRESOLVED",
        "dag_root": graph["root"] == "R0",
        "dag_acyclic": acyclic(graph),
        "rule_parentage": all("parents" in rule and "forbidden_claims" in rule for rule in rules),
        "drift_fail_closed": drift["fail_closed"] is True,
        "domain_contract": all(token in spec for token in ["q_MEMK", "meaning_after_readout", "DeltaW_j", "maker_checker_firewall", "UNRESOLVED"]),
        "current_release": all(token in registry for token in ["version: 1.6.0", EXPECTED_MD_SHA, "CURRENT_NORMATIVE_COMPANION"]),
        "dual_hash_lineage": all(token in validation for token in ["147a43cecfb5fcaa39386b3fb9b5f1d541e00ef12b068980b74f1b05ecf61968", EXPECTED_MD_SHA]),
        "claim_boundary": "target_domain_encoding: UNRESOLVED" in validation and "empirical_calibration: UNRESOLVED" in validation,
        "current_archive": verify_archive(),
        "checksums": verify_checksums(),
    }
    return all(results.values()), results


if __name__ == "__main__":
    passed, results = run()
    for key in sorted(results): print(f"{key}: {'PASS' if results[key] else 'FAIL'}")
    if not passed: raise SystemExit("FAIL: PHILOSOPHY_MEMK_STRUCTURAL_REGISTRATION")
    print("PASS: PHILOSOPHY_MEMK_STRUCTURAL_REGISTRATION")
    print("DOMAIN_CLOSURE: UNRESOLVED")
    print("EMPIRICAL_CALIBRATION: UNRESOLVED")
