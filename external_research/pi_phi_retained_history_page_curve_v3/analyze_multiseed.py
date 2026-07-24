from __future__ import annotations

import json
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
AUDIT_ONLY = os.environ.get("READOUT_AUDIT_ONLY") == "1"
CSV_PATH = ROOT / "phi_schedule_v5_3_multiseed.csv"
REPORT_PATH = ROOT / "phi_schedule_pagecurve_v5_3_multiseed_report.json"
OUT_CSV = ROOT / "recomputed_summary.csv"
OUT_JSON = ROOT / "recomputed_check.json"
OUT_FIG_PNG = ROOT / "phi_multiseed_comparison.png"
OUT_FIG_PDF = ROOT / "phi_multiseed_comparison.pdf"

frame = pd.read_csv(CSV_PATH)
means = {
    "golden": float(frame["golden_rmse"].mean()),
    "random": float(frame["random_rmse"].mean()),
    "cyclic": float(frame["cyclic_rmse"].mean()),
}
check = {
    "rows": int(len(frame)),
    "golden_beats_random": int((frame["golden_rmse"] < frame["random_rmse"]).sum()),
    "golden_unique_best": int(frame["unique_best"].astype(bool).sum()),
    "mean_relative_change_vs_random": float(frame["golden_vs_random_rel"].mean()),
    "mean_rmse": means,
    "negative_pair_not_worse": int((frame["golden_neg"] <= frame["random_neg"]).sum()),
    "entropy_admission_not_worse": int((frame["golden_admit"] >= frame["random_admit"]).sum()),
}

with REPORT_PATH.open("r", encoding="utf-8") as handle:
    declared = json.load(handle)

expected = declared["results"]
assert check["rows"] == expected["n_seeds"]
assert check["golden_beats_random"] == expected["golden_beats_random_rmse_seeds"]
assert check["golden_unique_best"] == expected["golden_unique_best_rmse_seeds"]
assert np.isclose(check["mean_relative_change_vs_random"], expected["mean_relative_rmse_change_vs_random"])
assert np.isclose(means["golden"], expected["mean_golden_rmse"])
assert np.isclose(means["random"], expected["mean_random_rmse"])
assert np.isclose(means["cyclic"], expected["mean_cyclic_rmse"])

if not AUDIT_ONLY:
    pd.DataFrame([check["mean_rmse"]]).to_csv(OUT_CSV, index=False)
    OUT_JSON.write_text(json.dumps(check, indent=2), encoding="utf-8")

    x = np.arange(len(frame))
    fig, ax = plt.subplots(figsize=(8.2, 4.8))
    ax.plot(x, frame["random_rmse"], marker="o", label="random")
    ax.plot(x, frame["cyclic_rmse"], marker="o", label="cyclic")
    ax.plot(x, frame["golden_rmse"], marker="o", label="golden")
    ax.set_xlabel("Validation seed index")
    ax.set_ylabel("Spectral-purity RMSE")
    ax.set_title("Reduced multiseed protocol: golden schedule wins 8/8")
    ax.set_xticks(x)
    ax.set_xticklabels(frame["seed"].astype(str), rotation=45, ha="right")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT_FIG_PNG, dpi=220)
    fig.savefig(OUT_FIG_PDF)
    plt.close(fig)

print(json.dumps(check, indent=2))
