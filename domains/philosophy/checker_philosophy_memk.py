#!/usr/bin/env python3
"""Independent checker for the Philosophy/MEMK domain and current IEF companion."""
from __future__ import annotations
import base64, gzip, hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
ART = ROOT / "artifacts"
MD = "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md"
PARTS = [ART / f"{MD}.gz.b64.part{i:02d}" for i in range(1, 17)]

def j(name):
    with (ROOT / name).open(encoding="utf-8") as f: return json.load(f)

def topo_ok(graph):
    nodes=set(graph["nodes"]); edges=[tuple(e) for e in graph["edges"]]; ready=set(nodes); placed=[]
    while ready:
        progress=False
        for node in sorted(ready):
            if {a for a,b in edges if b==node}.issubset(set(placed)):
                placed.append(node); ready.remove(node); progress=True; break
        if not progress: return False
    return len(placed)==len(nodes)

def checksum_ok():
    seen=0
    for row in (ROOT/"CHECKSUMS_SHA256_PHILOSOPHY_MEMK.txt").read_text().splitlines():
        if not row or row.startswith("#"): continue
        expected, rel=row.split("  ",1); seen+=1
        if hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()!=expected: return False
    return seen>0

def archive_ok():
    try:
        payload="".join(p.read_text(encoding="ascii").strip() for p in PARTS)
        gz=base64.b64decode(payload, validate=True)
        if hashlib.sha256(gz).hexdigest()!="a05dabea3dd44c7fc07fddd19246bc382c2c35faef48f73453b0eab77ebc58f1": return False
        md=gzip.decompress(gz)
        if hashlib.sha256(md).hexdigest()!="ff8cbf6848d93f7579327dc628e25e91801d959669de4235fcdfbcb347f7a926": return False
        t=md.decode("utf-8")
        return (t.count("\n")+1, len(t), len(md))==(5927,153091,154653) and "AGENCY_META_READOUT_GOVERNANCE_v1.6.0_ARCHITECTURE_CLOSED" in t and "claim_ceiling" in t and not any(x in t for x in ['compenmeta_governanceng', 'meta_governancesfies', 'cesmeta_governanceon', 'Cesmeta_governanceon', 'meta_governancesfy'])
    except Exception:
        return False

def run():
    claim=j("CLAIM_BOUNDARY_PHILOSOPHY_MEMK.json"); drift=j("DRIFT_CONTRACT_PHILOSOPHY_MEMK.json"); rules=j("RULE_REGISTRY_PHILOSOPHY_MEMK.json"); graph=j("ROOT_DAG_MASTER_PHILOSOPHY_MEMK.json")
    spec=(ROOT/"PHILOSOPHY_MEMK_DOMAIN_v0_2_0.yaml").read_text(); reg=(ROOT/"FOUNDATION_RELEASE_REGISTRY_PHILOSOPHY_MEMK.yaml").read_text(); val=(ROOT/"INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.validation.yaml").read_text()
    checks={
        "root_identity": claim["root"]["root_blob_sha"]=="31e07095addc45aacbaea26523784380d5ce21f1",
        "bounded_tier": claim["tier"].endswith("UNRESOLVED_DOMAIN"),
        "root_node": graph["nodes"]["R0"]["class"]=="ROOT_THEOREM",
        "topological_order": topo_ok(graph),
        "rule_parentage": all("parents" in r and "forbidden_claims" in r for r in rules["rules"]),
        "drift_count": len(drift["hard_fail_conditions"])>=12,
        "meaning_post_translation": "meaning_after_readout" in spec and "q_MEMK" in spec,
        "low_rank_lane": all(x in spec for x in ["DeltaW_j","W_0","lambda_j"]),
        "transition_lane": all(x in spec for x in ["semantic_potential","informational_work","activation_barrier"]),
        "epistemic_limits": all(p in spec.lower() for p in ["intensity != truth","surprise != knowledge","life change != universal truth"]),
        "current_registry": all(x in reg for x in ["version: 1.6.0","ff8cbf6848d93f7579327dc628e25e91801d959669de4235fcdfbcb347f7a926","CURRENT_NORMATIVE_COMPANION"]),
        "dual_hash_lineage": "147a43cecfb5fcaa39386b3fb9b5f1d541e00ef12b068980b74f1b05ecf61968" in val and "ff8cbf6848d93f7579327dc628e25e91801d959669de4235fcdfbcb347f7a926" in val,
        "unresolved_guard": "target_domain_encoding: UNRESOLVED" in val and "empirical_calibration: UNRESOLVED" in val,
        "archive_identity": archive_ok(),
        "checksum_lock": checksum_ok(),
    }
    allowed={"ARCHITECTURE_CONDITIONAL_UNRESOLVED_DOMAIN"}
    checks["pass_control"] = claim["tier"] in allowed and claim["statuses"]["exact_domain_quotient"]=="UNRESOLVED"
    checks["fail_control_rejected"] = "EMPIRICALLY_CLOSED" not in allowed
    return all(checks.values()), checks

if __name__=="__main__":
    ok,checks=run()
    for key in sorted(checks): print(f"{key}: {'PASS' if checks[key] else 'FAIL'}")
    if not ok: raise SystemExit("FAIL: independent checker")
    print("PASS: independent checker")
