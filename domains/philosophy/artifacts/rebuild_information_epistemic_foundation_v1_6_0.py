#!/usr/bin/env python3
"""Rebuild and verify the canonical Information Epistemic Foundation v1.6.0 artifact."""
from __future__ import annotations
import base64, gzip, hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT = HERE.parent / "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md"
PREFIX = "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part"
EXPECTED_PARTS = 19
EXPECTED_GZIP_SHA256 = "a05dabea3dd44c7fc07fddd19246bc382c2c35faef48f73453b0eab77ebc58f1"
EXPECTED_MARKDOWN_SHA256 = "ff8cbf6848d93f7579327dc628e25e91801d959669de4235fcdfbcb347f7a926"
EXPECTED_DIMENSIONS = (5927, 153091, 154653)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parts = sorted(HERE.glob(f"{PREFIX}*"))
    if len(parts) != EXPECTED_PARTS:
        raise SystemExit(f"Archive part count mismatch: {len(parts)} != {EXPECTED_PARTS}")
    encoded = "".join(path.read_text(encoding="ascii").strip() for path in parts)
    compressed = base64.b64decode(encoded, validate=True)
    compressed_hash = sha256(compressed)
    if compressed_hash != EXPECTED_GZIP_SHA256:
        raise SystemExit(f"Compressed SHA-256 mismatch: {compressed_hash}")
    markdown_bytes = gzip.decompress(compressed)
    markdown_hash = sha256(markdown_bytes)
    if markdown_hash != EXPECTED_MARKDOWN_SHA256:
        raise SystemExit(f"Markdown SHA-256 mismatch: {markdown_hash}")
    markdown = markdown_bytes.decode("utf-8")
    dimensions = (markdown.count("\n") + 1, len(markdown), len(markdown_bytes))
    if dimensions != EXPECTED_DIMENSIONS:
        raise SystemExit(f"Document dimensions mismatch: {dimensions} != {EXPECTED_DIMENSIONS}")
    required = [
        "## 3. The Belief Layer",
        "## 4. Our Normative Proposal of Knowledge",
        "root_native_closure_v1_3:",
        "# PART X — AGENCY META-READOUT GOVERNANCE",
        "maker_checker_firewall:",
        "ALGORITHM ROOT_NATIVE_INFORMATION_EPISTEMIC_FOUNDATION_V1_3",
        "AGENCY_META_READOUT_GOVERNANCE_v1.6.0_ARCHITECTURE_CLOSED",
        "flowchart TD",
    ]
    forbidden = [
        "compenmeta_governanceng", "meta_governancesfies", "cesmeta_governanceon",
        "Cesmeta_governanceon", "meta_governancesfy",
    ]
    if missing := [token for token in required if token not in markdown]:
        raise SystemExit(f"Required content missing: {missing}")
    if present := [token for token in forbidden if token in markdown]:
        raise SystemExit(f"Corruption tokens remain: {present}")
    OUTPUT.write_bytes(markdown_bytes)
    print(f"PASS: rebuilt {OUTPUT}")
    print(f"MARKDOWN_SHA256: {markdown_hash}")
    print(f"GZIP_SHA256: {compressed_hash}")
    print(f"LINES: {dimensions[0]}")
    print(f"CHARACTERS: {dimensions[1]}")
    print(f"BYTES: {dimensions[2]}")
    print("TARGET_DOMAIN_ENCODING_AND_CALIBRATION: UNRESOLVED")


if __name__ == "__main__":
    main()
