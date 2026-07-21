from __future__ import annotations
import json
from pathlib import Path
from composition_kernel_v0_910 import run_composition_suite
from drift_validator_v0_910 import run_drift_audit
ROOT = Path(__file__).resolve().parent
# C7 is a release-level proof obligation, so regenerate the drift audit first.
drift = run_drift_audit()
(ROOT / "DRIFT_AUDIT_v0_910.json").write_text(json.dumps(drift, indent=2, sort_keys=True) + "\n", encoding="utf-8")
claim = json.loads((ROOT / "CLAIM_BOUNDARY_v0_910.json").read_text(encoding="utf-8"))
result = run_composition_suite()
result["statuses"]["C7"] = drift["decision"] == "PASS" and claim["tier"] == "FORMAL_COMPOSITION_QUOTIENT_ONLY"
result["decision"] = "PASS" if all(result["statuses"].values()) else "FAIL"
(ROOT / "PROOF_RECEIPT_v0_910.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(0 if result["decision"] == "PASS" else 1)
