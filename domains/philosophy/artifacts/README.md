# Information Epistemic Foundation — Lossless Source Archives

This folder retains deterministic source archives for standalone foundation companions. Each archive is gzip-compressed with fixed `mtime=0`, base64-encoded, split only for bounded connector writes, and rebuilt under exact SHA-256 and dimension checks.

## Current companion: v1.6.0

Run from this folder:

```bash
python -B rebuild_information_epistemic_foundation_v1_6_0.py
```

The script reconstructs:

```text
domains/philosophy/INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md
```

Expected identity:

```text
MARKDOWN_SHA256: ff8cbf6848d93f7579327dc628e25e91801d959669de4235fcdfbcb347f7a926
GZIP_SHA256: a05dabea3dd44c7fc07fddd19246bc382c2c35faef48f73453b0eab77ebc58f1
LINES: 5927
CHARACTERS: 153091
BYTES: 154653
TARGET_DOMAIN_ENCODING_AND_CALIBRATION: UNRESOLVED
```

Archive parts (19):

- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part01`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part02`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part03`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part04`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part05`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part06`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part07`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part08`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part09`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part10`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part11`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part12`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part12b`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part12c`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part12d`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part13`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part14`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part15`
- `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.md.gz.b64.part16`

Validation and canonicalization lineage are recorded one directory above in `INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.6.0.validation.yaml`.

## Retained predecessor: v1.2.0

The v1.2.0 archive and rebuild script remain present for append-only lineage. It is superseded only as the current standalone companion, not deleted or retroactively rewritten.

## Claim boundary

Archive integrity establishes byte identity and required structural content. It does not establish exact target-domain encoding, empirical calibration, external independent review, or universal truth.
