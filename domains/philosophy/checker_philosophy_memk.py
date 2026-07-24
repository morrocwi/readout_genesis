#!/usr/bin/env python3
"""Independent checker for Philosophy/MEMK and the current IEF companion."""
from __future__ import annotations
import base64, gzip, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ART = ROOT / "artifacts"
PREFIX = "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part"
MD_SHA = "ff8cbf6848d93f7579327dc628e25e91801d959669de4235fcdfbcb347f7a926"
GZIP_SHA = "a05dabea3dd44c7fc07fddd19246bc382c2c35faef48f73453b0eab77ebc58f1"


def j(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def checksum_ok() -> bool:
    rows = 0
    for row in (ROOT / "CHECKSUMS_SHA256_PHILOSOPHY_MEMK.txt").read_text(encoding="utf-8").splitlines():
        if not row or row.startswith("#"): continue
        expected, rel = row.split("  ", 1); rows += 1
        if hashlib.sha256((ROOT / rel).read_bytes()).hexdigest() != expected: return False
    return rows > 0


def archive_ok() -> bool:
    try:
        parts = sorted(ART.glob(f"{PREFIX}*"))
        if len(parts) != 19: return False
        compressed = base64.b64decode("".join(p.read_text(encoding="ascii").strip() for p in parts), validate=True)
        if hashlib.sha256(compressed).hexdigest() != GZIP_SHA: return False
        markdown = gzip.decompress(compressed)
        text = markdown.decode("utf-8")
        return hashlib.sha256(markdown).hexdigest() == MD_SHA and (text.count("\n") + 1, len(text), len(markdown)) == (5927, 153091, 154653) and "AGENCY_META_READOUT_GOVERNANCE_v1.6.0_ARCHITECTURE_CLOSED" in text
    except Exception:
        return False


def run():
    claim = j("CLAIM_BOUNDARY_PHILOSOPHY_MEMK.json")
    drift = j("DRIFT_CONTRACT_PHILOSOPHY_MEMK.json")
    registry = (ROOT / "FOUNDATION_RELEASE_REGISTRY_PHILOSOPHY_MEMK.yaml").read_text(encoding="utf-8")
    validation = (ROOT / "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.validation.yaml").read_text(encoding="utf-8")
    checks = {
        "root_identity": claim["root"]["root_blob_sha"] == "31e07095addc45aacbaea26523784380d5ce21f1",
        "bounded_tier": claim["tier"] == "ARCHITECTURE_CONDITIONAL_UNRESOLVED_DOMAIN",
        "drift_fail_closed": drift["fail_closed"] is True,
        "current_registry": all(token in registry for token in ["version: 1.6.0", MD_SHA, "CURRENT_NORMATIVE_COMPANION"]),
        "dual_hash_lineage": all(token in validation for token in ["147a43cecfb5fcaa39386b3fb9b5f1d541e00ef12b068980b74f1b05ecf61968", MD_SHA]),
        "unresolved_guard": "target_domain_encoding: UNRESOLVED" in validation and "empirical_calibration: UNRESOLVED" in validation,
        "archive_identity": archive_ok(),
        "checksum_lock": checksum_ok(),
        "abstention_control": claim["statuses"]["exact_domain_quotient"] == "UNRESOLVED",
    }
    return all(checks.values()), checks


if __name__ == "__main__":
    passed, checks = run()
    for key in sorted(checks): print(f"{key}: {'PASS' if checks[key] else 'FAIL'}")
    if not passed: raise SystemExit("FAIL: independent checker")
    print("PASS: independent checker")
