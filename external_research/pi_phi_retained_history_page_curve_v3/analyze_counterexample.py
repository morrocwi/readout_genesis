from __future__ import annotations

import json
import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
AUDIT_ONLY = os.environ.get("READOUT_AUDIT_ONLY") == "1"
frame = pd.read_csv(ROOT / "simple_phi_pagecurve_summary.csv")
indexed = frame.set_index("schedule")
random_rmse = float(indexed.loc["random", "purity_rmse"])
golden_rmse = float(indexed.loc["golden", "purity_rmse"])
relative_improvement = (random_rmse - golden_rmse) / random_rmse
check = {
    "status": "COUNTEREXAMPLE_PROTOCOL_GOLDEN_LOSES",
    "golden_vs_random_relative_improvement": relative_improvement,
    "golden_has_higher_negative_readout_rate": bool(
        indexed.loc["golden", "negative_readout_rate"]
        > indexed.loc["random", "negative_readout_rate"]
    ),
    "interpretation": "Golden scheduling is not universally superior; the effect is estimator- and protocol-dependent.",
}
if not AUDIT_ONLY:
    (ROOT / "counterexample_check.json").write_text(json.dumps(check, indent=2), encoding="utf-8")

    fig, ax = plt.subplots(figsize=(7.2, 4.5))
    ax.bar(frame["schedule"], frame["purity_rmse"])
    ax.set_ylabel("Signed-purity RMSE")
    ax.set_title("Simple direct protocol: golden schedule loses")
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(ROOT / "phi_counterexample.png", dpi=220)
    fig.savefig(ROOT / "phi_counterexample.pdf")
    plt.close(fig)
print(json.dumps(check, indent=2))
