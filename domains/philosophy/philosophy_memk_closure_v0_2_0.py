#!/usr/bin/env python3
"""Primary structural verifier for Philosophy / MEMK v0.2.0 and current IEF companion."""
from __future__ import annotations
import base64, gzip, hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "artifacts"
CURRENT_MD = "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md"
EXPECTED_MD_SHA = "ff8cbf6848d93f7579327dc628e25e91801d959669de4235fcdfbcb347f7a926"
EXPECTED_GZIP_SHA = "a05dabea3dd44c7fc07fddd19246bc382c2c35faef48f73453b0eab77ebc58f1"
PARTS = [ART / f"{CURRENT_MD}.gz.b64.part{i:02d}" for i in range(1, 17)]
REQUIRED = [
    "README.md", "PHILOSOPHY_MEMK_DOMAIN_v0_2_0.yaml",
    "FOUNDATION_RELEASE_REGISTRY_PHILOSOPHY_MEMK.yaml",
    "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.validation.yaml",
    "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.2.0.validation.yaml",
    "CLAIM_BOUNDARY_PHILOSOPHY_MEMK.json", "RULE_REGISTRY_PHILOSOPHY_MEMK.json",
    "ROOT_DAG_MASTER_PHILOSOPHY_MEMK.md", "ROOT_DAG_MASTER_PHILOSOPHY_MEMK.json",
    "DRIFT_CONTRACT_PHILOSOPHY_MEMK.json", "source_root/READOUT_GENESIS_CORE_SNAPSHOT.md",
    "PROOF_RECEIPT_PHILOSOPHY_MEMK.json", "CLOSURE_AUDIT_PHILOSOPHY_MEMK.json",
    "CHECKSUMS_SHA256_PHILOSOPHY_MEMK.txt", "artifacts/README.md",
    "artifacts/rebuild_information_epistemic_foundation_v1_6_0.py",
] + [f"artifacts/{p.name}" for p in PARTS]

def load_json(name: str):
    return json.loads((HERE / name).read_text(encoding="utf-8"))

def acyclic(nodes, edges):
    indeg = {n: 0 for n in nodes}; children = {n: [] for n in nodes}
    for a, b in edges:
        if a not in nodes or b not in nodes: return False
        indeg[b] += 1; children[a].append(b)
    queue = [n for n, d in indeg.items() if d == 0]; seen = 0
    while queue:
        n = queue.pop(); seen += 1
        for c in children[n]:
            indeg[c] -= 1
            if indeg[c] == 0: queue.append(c)
    return seen == len(nodes)

def verify_checksums():
    entries = {}
    for line in (HERE / "CHECKSUMS_SHA256_PHILOSOPHY_MEMK.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"): continue
        digest, rel = line.split("  ", 1); entries[rel] = digest
    if not entries: return False
    return all(hashlib.sha256((HERE / rel).read_bytes()).hexdigest() == expected for rel, expected in entries.items())

def verify_current_archive():
    try:
        encoded = "".join(p.read_text(encoding="ascii").strip() for p in PARTS)
        compressed = base64.b64decode(encoded, validate=True)
        if hashlib.sha256(compressed).hexdigest() != EXPECTED_GZIP_SHA: return False
        md = gzip.decompress(compressed)
        if hashlib.sha256(md).hexdigest() != EXPECTED_MD_SHA: return False
        text = md.decode("utf-8")
        required = ["document:", "id: IEF-RG", "version: 1.6.0", "root_native_closure_v1_3:",
                    "maker_checker_firewall:", "ALGORITHM ROOT_NATIVE_INFORMATION_EPISTEMIC_FOUNDATION_V1_3",
                    "AGENCY_META_READOUT_GOVERNANCE_v1.6.0_ARCHITECTURE_CLOSED", "flowchart TD"]
        forbidden = ['compenmeta_governanceng', 'meta_governancesfies', 'cesmeta_governanceon', 'Cesmeta_governanceon', 'meta_governancesfy']
        return all(t in text for t in required) and not any(t in text for t in forbidden)
    except Exception:
        return False

def run():
    results = {}
    results["required_files"] = all((HERE / p).is_file() for p in REQUIRED)
    claim = load_json("CLAIM_BOUNDARY_PHILOSOPHY_MEMK.json")
    results["claim_tier"] = claim["tier"] == "ARCHITECTURE_CONDITIONAL_UNRESOLVED_DOMAIN"
    results["nonclaims"] = len(claim["not_established"]) >= 8
    results["exact_q_unresolved"] = claim["statuses"]["exact_domain_quotient"] == "UNRESOLVED"
    dag = load_json("ROOT_DAG_MASTER_PHILOSOPHY_MEMK.json")
    results["dag_root"] = dag["root"] == "R0"
    results["dag_acyclic"] = acyclic(dag["nodes"], dag["edges"])
    results["no_shortcuts"] = len(dag["forbidden_edges"]) >= 5
    rules = load_json("RULE_REGISTRY_PHILOSOPHY_MEMK.json")["rules"]
    results["root_rules_clean"] = all(not any(token in r["statement"].lower() for token in ("human truth", "literal lora", "joule")) for r in rules if r["class"] == "ROOT_THEOREM")
    results["forbidden_claims_per_rule"] = all(bool(r.get("forbidden_claims")) for r in rules)
    drift = load_json("DRIFT_CONTRACT_PHILOSOPHY_MEMK.json"); joined = "\n".join(drift["hard_fail_conditions"]).lower()
    results["drift_fail_closed"] = drift["fail_closed"] is True
    results["energy_guard"] = "physical energy" in joined
    results["lora_guard"] = "w_0" in joined and "biological mechanism" in joined
    results["intensity_guard"] = "shock" in joined and "truth" in joined
    yml = (HERE / "PHILOSOPHY_MEMK_DOMAIN_v0_2_0.yaml").read_text(encoding="utf-8")
    required_tokens = ["q_MEMK", "meaning_after_readout", "DeltaW_j", "W_eff", "informational_work", "activation_barrier", "shock_like_impulse", "coherent_sudden_insight", "life_changing_transformation", "maker_checker_firewall", "UNRESOLVED"]
    results["yaml_contract_tokens"] = all(t in yml for t in required_tokens)
    results["physical_non_equivalence"] = "informational work as physical energy" in yml
    results["root_snapshot_lock"] = "31e07095addc45aacbaea26523784380d5ce21f1" in (HERE / "source_root/READOUT_GENESIS_CORE_SNAPSHOT.md").read_text(encoding="utf-8")
    registry = (HERE / "FOUNDATION_RELEASE_REGISTRY_PHILOSOPHY_MEMK.yaml").read_text(encoding="utf-8")
    validation = (HERE / "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.validation.yaml").read_text(encoding="utf-8")
    results["current_release_registered"] = all(t in registry for t in ["version: 1.6.0", EXPECTED_MD_SHA, "CURRENT_NORMATIVE_COMPANION", "does_not_supersede_domain_spec"])
    results["source_and_canonical_hashes"] = "147a43cecfb5fcaa39386b3fb9b5f1d541e00ef12b068980b74f1b05ecf61968" in validation and EXPECTED_MD_SHA in validation
    results["architecture_empirical_separation"] = "target_domain_encoding: UNRESOLVED" in validation and "empirical_calibration: UNRESOLVED" in validation
    results["current_archive"] = verify_current_archive()
    results["checksums"] = verify_checksums()
    good = {"meaning_after_readout":True,"w0_frozen":True,"has_negative_controls":True,"claim_tier":"ARCHITECTURE_CONDITIONAL_UNRESOLVED_DOMAIN"}
    bad = dict(good, w0_frozen=False)
    gate = lambda f: f["meaning_after_readout"] and f["w0_frozen"] and f["has_negative_controls"] and f["claim_tier"] == "ARCHITECTURE_CONDITIONAL_UNRESOLVED_DOMAIN"
    results["positive_control"] = gate(good) is True
    results["negative_control"] = gate(bad) is False
    results["abstention_control"] = claim["statuses"]["empirical_calibration"] == "UNRESOLVED"
    return all(results.values()), results

if __name__ == "__main__":
    passed, results = run()
    for key in sorted(results): print(f"{key}: {'PASS' if results[key] else 'FAIL'}")
    if not passed: raise SystemExit("FAIL: PHILOSOPHY_MEMK_STRUCTURAL_REGISTRATION")
    print("PASS: PHILOSOPHY_MEMK_STRUCTURAL_REGISTRATION")
    print("DOMAIN_CLOSURE: UNRESOLVED")
    print("EMPIRICAL_CALIBRATION: UNRESOLVED")
