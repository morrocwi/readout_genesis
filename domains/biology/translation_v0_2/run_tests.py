#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VERIFIER = ROOT / "verify_translation_stack_v0_2.py"


def main() -> int:
    completed = subprocess.run(
        [sys.executable, str(VERIFIER)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.stdout:
        print(completed.stdout, end="")
    if completed.stderr:
        print(completed.stderr, file=sys.stderr, end="")
    if completed.returncode != 0:
        print(json.dumps({"decision": "FAIL", "returncode": completed.returncode}))
        return completed.returncode
    print(json.dumps({"decision": "PASS", "runner": "translation_v0_2/run_tests.py"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
