from __future__ import annotations
import hashlib
import json
from pathlib import Path
from proof_kernel_v0_901 import run_proof_suite

ROOT = Path(__file__).resolve().parent
result = run_proof_suite()
source_hash = hashlib.sha256((ROOT / "proof_kernel_v0_901.py").read_bytes()).hexdigest()
receipt = {
    "version": "0.901",
    "proof_kernel_sha256": source_hash,
    "result": result,
}
(ROOT / "PROOF_RECEIPT_v0_901.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"decision": result["decision"], "receipt": "PROOF_RECEIPT_v0_901.json"}))
