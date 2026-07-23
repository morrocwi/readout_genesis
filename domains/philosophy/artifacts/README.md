# Information Epistemic Foundation v1.2.0 — Lossless Source Archive

This folder stores the exact standalone Markdown artifact as a deterministic split base64 archive.
The split exists only to keep connector writes bounded; it is not a conceptual decomposition.

## Rebuild

From `domains/philosophy/artifacts/`:

```bash
python -B rebuild_information_epistemic_foundation_v1_2_0.py
```

The script concatenates four parts, decodes the gzip archive, verifies both compressed and Markdown SHA-256 hashes, verifies dimensions and required sections, and writes:

```text
domains/philosophy/INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.2.0.md
```

Expected output:

```text
PASS: rebuilt .../INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.2.0.md
SHA256: c9d395ba32ef156199078658ff9951dddbaac069cedbd17ff206d41b40f94a00
LINES: 3358
CHARACTERS: 98406
EMPIRICAL_AND_DOCTRINAL_IDENTITY: UNRESOLVED
```

## Archive files

- `...part01`
- `...part02`
- `...part03`
- `...part04`
- `rebuild_information_epistemic_foundation_v1_2_0.py`

The validation receipt is stored one directory above as:

`INFORMATION_EPISTEMIC_FOUNDATION_STANDALONE_v1.2.0.validation.yaml`

## Claim boundary

The artifact is complete as a specification. It does not establish empirical universality, exact Buddhist doctrinal identity, literal biological LoRA, or transfer of chemical/biological/quantum/Standard-Model semantics into the root.
