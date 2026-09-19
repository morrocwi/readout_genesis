#!/usr/bin/env python3
"""Rebuild the exact Information Epistemic Foundation v1.2.0 Markdown artifact.

The source archive is split into four base64 text parts to keep repository connector
writes deterministic. This script concatenates, decodes, verifies, decompresses,
and writes the exact standalone Markdown file.
"""
from __future__ import annotations

import base64
import gzip
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEM = "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.2.0.md.gz.b64.part"
PARTS = [HERE / f"{STEM}{index:02d}" for index in range(1, 5)]
OUTPUT = HERE.parent / "INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.2.0.md"
EXPECTED_GZIP_SHA256 = "7ed7f7321c6d4fb07dff415ad540d7f6f70a6c43b16cff6b2d83d030db3b85cd"
EXPECTED_MARKDOWN_SHA256 = "c9d395ba32ef156199078658ff9951dddbaac069cedbd17ff206d41b40f94a00"
EXPECTED_LINES = 3358
EXPECTED_CHARACTERS = 98406


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
        raise SystemExit(
            f"Compressed SHA-256 mismatch: {compressed_hash} != {EXPECTED_GZIP_SHA256}"
        )

    markdown_bytes = gzip.decompress(compressed)
    markdown_hash = sha256(markdown_bytes)
    if markdown_hash != EXPECTED_MARKDOWN_SHA256:
        raise SystemExit(
            f"Markdown SHA-256 mismatch: {markdown_hash} != {EXPECTED_MARKDOWN_SHA256}"
        )

    markdown = markdown_bytes.decode("utf-8")
    lines = markdown.count("\n") + 1
    characters = len(markdown)
    if lines != EXPECTED_LINES or characters != EXPECTED_CHARACTERS:
        raise SystemExit(
            "Document dimensions mismatch: "
            f"lines={lines}/{EXPECTED_LINES}, characters={characters}/{EXPECTED_CHARACTERS}"
        )

    required_tokens = [
        "conditioned_agency_layer:",
        "contact_valence_drive_appropriation_chain:",
        "release_and_cessation_dynamics:",
        "transformative_knowledge_layer:",
        "ALGORITHM CONTINUOUS_INFORMATION_TRANSFORMATIVE_EPISTEMOLOGY_V1_2",
        "flowchart TD",
    ]
    missing_tokens = [token for token in required_tokens if token not in markdown]
    if missing_tokens:
        raise SystemExit(f"Required content missing: {missing_tokens}")

    OUTPUT.write_bytes(markdown_bytes)
    print(f"PASS: rebuilt {OUTPUT}")
    print(f"SHA256: {markdown_hash}")
    print(f"LINES: {lines}")
    print(f"CHARACTERS: {characters}")
    print("EMPIRICAL_AND_DOCTRINAL_IDENTITY: UNRESOLVED")


if __name__ == "__main__":
    main()
