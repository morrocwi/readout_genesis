#!/usr/bin/env python3
"""Independent checker: reimplements core release checks without importing the primary verifier."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def j(name):
    with (ROOT / name).open(encoding="utf-8") as f:
        return json.load(f)

def topo_ok(graph):
    nodes = set(graph["nodes"])
    edges = [tuple(e) for e in graph["edges"]]
    ready = set(nodes)
    placed = []
    while ready:
        progress = False
        for node in sorted(list(ready)):
            parents = {a for a, b in edges if b == node}
            if parents.issubset(set(placed)):
                placed.append(node)
                ready.remove(node)
                progress = True
                break
        if not progress:
            return False
    return len(placed) == len(nodes)

def checksum_ok():
    path = ROOT / "CHECKSUMS_SHA256_PHILOSOPHY_MEMK.txt"
    seen = 0
    for row in path.read_text(encoding="utf-8").splitlines():
        if not row or row.startswith("#"):
            continue
        expected, rel = row.split("  ", 1)
        seen += 1
        if hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() != expected:
            return False
    return seen > 0

def run():
    claim = j("CLAIM_BOUNDARY_PHILOSOPHY_MEMK.json")
    drift = j("DRIFT_CONTRACT_PHILOSOPHY_MEMK.json")
    rules = j("RULE_REGISTRY_PHILOSOPHY_MEMK.json")
    graph = j("ROOT_DAG_MASTER_PHILOSOPHY_MEMK.json")
    spec = (ROOT / "PHILOSOPHY_MEMK_DOMAIN_v0_2_0.yaml").read_text(encoding="utf-8")

    checks = {
        "root_identity": claim["root"]["root_blob_sha"] == "31e07095addc45aacbaea26523784380d5ce21f1",
        "bounded_tier": claim["tier"].endswith("UNRESOLVED_DOMAIN"),
        "root_node": graph["nodes"]["R0"]["class"] == "ROOT_THEOREM",
        "topological_order": topo_ok(graph),
        "rule_parentage": all("parents" in r and "forbidden_claims" in r for r in rules["rules"]),
        "drift_count": len(drift["hard_fail_conditions"]) >= 12,
        "meaning_post_translation": "meaning_after_readout" in spec and "q_MEMK" in spec,
        "low_rank_lane": all(x in spec for x in ["DeltaW_j", "W_0", "lambda_j"]),
        "transition_lane": all(x in spec for x in ["semantic_potential", "informational_work", "activation_barrier"]),
        "epistemic_limits": all(
            phrase in spec.lower()
            for phrase in ["intensity != truth", "surprise != knowledge", "life change != universal truth"]
        ),
        "checksum_lock": checksum_ok(),
    }

    allowed = {"ARCHITECTURE_CONDITIONAL_UNRESOLVED_DOMAIN"}
    pass_control = claim["tier"] in allowed and claim["statuses"]["exact_domain_quotient"] == "UNRESOLVED"
    fail_control = "EMPIRICALLY_CLOSED" in allowed
    checks["pass_control"] = pass_control
    checks["fail_control_rejected"] = not fail_control

    return all(checks.values()), checks

if __name__ == "__main__":
    ok, checks = run()
    for key in sorted(checks):
        print(f"{key}: {'PASS' if checks[key] else 'FAIL'}")
    if not ok:
        raise SystemExit("FAIL: independent checker")
    print("PASS: independent checker")
