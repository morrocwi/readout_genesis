#!/usr/bin/env python3
"""Rebuild and verify the canonical Information Epistemic Foundation v1.6.0 artifact."""
from __future__ import annotations
import base64
import gzip
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEM = "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part"
PARTS = [HERE / f"{STEM}{index:02d}" for index in range(1, 17)]
OUTPUT = HERE.parent / "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md"
EXPECTED_GZIP_SHA256 = "a05dabea3dd44c7fc07fddd19246bc382c2c35faef48f73453b0eab77ebc58f1"
EXPECTED_MARKDOWN_SHA256 = "ff8cbf6848d93f7579327dc628e25e91801d959669de4235fcdfbcb347f7a926"
EXPECTED_LINES = 5927
EXPECTED_CHARACTERS = 153091
EXPECTED_BYTES = 154653


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    missing = [str(path) for path in PARTS if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing archive part(s): {missing}")
    encoded = "".join(path.read_text(encoding="ascii").strip() for path in PARTS)
    compressed = base64.b64decode(encoded, validate=True)
    compressed_hash = sha256(compressed)
    if compressed_hash != EXPECTED_GZIP_SHA256:
        raise SystemExit(f"Compressed SHA-256 mismatch: {compressed_hash} != {EXPECTED_GZIP_SHA256}")
    markdown_bytes = gzip.decompress(compressed)
    markdown_hash = sha256(markdown_bytes)
    if markdown_hash != EXPECTED_MARKDOWN_SHA256:
        raise SystemExit(f"Markdown SHA-256 mismatch: {markdown_hash} != {EXPECTED_MARKDOWN_SHA256}")
    markdown = markdown_bytes.decode("utf-8")
    lines = markdown.count("\n") + 1
    characters = len(markdown)
    if (lines, characters, len(markdown_bytes)) != (EXPECTED_LINES, EXPECTED_CHARACTERS, EXPECTED_BYTES):
        raise SystemExit(
            "Document dimensions mismatch: "
            f"lines={lines}/{EXPECTED_LINES}, characters={characters}/{EXPECTED_CHARACTERS}, "
            f"bytes={len(markdown_bytes)}/{EXPECTED_BYTES}"
        )
    required_tokens = [
        "## 3. The Belief Layer",
        "## 4. Our Normative Proposal of Knowledge",
        "root_native_closure_v1_3:",
        "# PART X — AGENCY META-READOUT GOVERNANCE",
        "maker_checker_firewall:",
        "ALGORITHM ROOT_NATIVE_INFORMATION_EPISTEMIC_FOUNDATION_V1_3",
        "AGENCY_META_READOUT_GOVERNANCE_v1.6.0_ARCHITECTURE_CLOSED",
        "flowchart TD",
    ]
    missing_tokens = [token for token in required_tokens if token not in markdown]
    if missing_tokens:
        raise SystemExit(f"Required content missing: {missing_tokens}")
    forbidden_tokens = [
        "compenmeta_governanceng", "meta_governancesfies", "cesmeta_governanceon",
        "Cesmeta_governanceon", "meta_governancesfy",
    ]
    present_forbidden = [token for token in forbidden_tokens if token in markdown]
    if present_forbidden:
        raise SystemExit(f"Corruption tokens remain: {present_forbidden}")
    OUTPUT.write_bytes(markdown_bytes)
    print(f"PASS: rebuilt {OUTPUT}")
    print(f"MARKDOWN_SHA256: {markdown_hash}")
    print(f"GZIP_SHA256: {compressed_hash}")
    print(f"LINES: {lines}")
    print(f"CHARACTERS: {characters}")
    print(f"BYTES: {len(markdown_bytes)}")
    print("TARGET_DOMAIN_ENCODING_AND_CALIBRATION: UNRESOLVED")


if __name__ == "__main__":
    main()
