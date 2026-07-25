#!/usr/bin/env python3
"""Native branch-time -> real decay-lifetime bridge, v0.1.

Stacked on the merged primitive-branch parameter reduction. Per the founder's explicit direction
(2026-07-25, "เอาหน่วยเวลาดีกว่า เพราะเวลามันเกี่ยวกับสรรพสิ่งทั้งหมด แหละหน่วยมันก็ชัดเจนกว่า" --
use the TIME unit instead, since time relates to everything and the unit is clearer): tries TIME
(seconds) as the physical-unit target, instead of the 5 already-failed GeV/mass-based routes today.

REQUIRED SCOPE CHECK, done before building (per the 2026-07-25 self-critique discipline): a prior
candidate (native_causal_memory_consistency, PR #81) already computed a single global
`tau_c_native := M_joint/D`. Using that ONE number to "predict" multiple different real particle
lifetimes would be VACUOUS -- every prediction would trivially equal whatever one real lifetime it
was fit against, since there is only one native quantity to work with. This file avoids that by
using the primitive-branch construction's THREE distinct branch costs (`Delta_U`, `Delta_D`,
`Delta_E`, from the already-merged `primitive_branch_parameter_reduction`) to build THREE distinct
native "decay times": `tau_j_native := T_traj / Delta_j` (trajectory duration divided by
accumulated branch cost -- Dr-tier, disclosed as a modeling choice: `lambda_j=exp(-Delta_j)` reads
as a survival probability over the trajectory's own duration `T_traj`, so `Delta_j/T_traj` reads as
a decay RATE and its reciprocal as a decay TIME; this is not the only possible such mapping).

Real targets: 5 well-measured PDG particle mean lifetimes, in seconds, spanning ~15 orders of
magnitude (shortest: tau lepton 2.9e-13 s; longest: neutron 878.4 s) -- pre-registered
before any comparison is computed. `Lambda_time` is fit from ONE pairing (E branch <-> muon, the
most defensible single pairing since E is this repo's own "lepton" branch label and muon is a
lepton) and the SAME Lambda_time is then applied, with NO refitting, to U and D against all 5
targets -- a full, disclosed 3x5=15-row table, no cherry-picking.

Tier: `fit_calibrated` (Delta_U/D/E, all real PDG lifetimes -- reused, not re-derived).
`Dr` (the `tau_j_native:=T_traj/Delta_j` mapping and the E<->muon fit pairing are both disclosed
modeling choices, not derivations). `finite_diagnostic` (the 15 computed comparisons).
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import List, Mapping

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BRANCH_DIR = ROOT / "domains" / "standard_model" / "item1_exploration" / "primitive_branch_parameter_reduction"
if str(BRANCH_DIR) not in sys.path:
    sys.path.insert(0, str(BRANCH_DIR))

from domains.standard_model.item1_exploration.primitive_branch_parameter_reduction.primitive_branch_fixture_v0_1 import (  # noqa: E402
    run_fixture as run_branch_fixture,
    N_STEPS,
)
from domains.standard_model.item1_exploration.retained_transition_operational_closure.operational_exchange_closure_v0_1 import (  # noqa: E402
    load_stepper,
)

EPS = 1e-15

# Real PDG mean lifetimes, seconds. Pre-registered before any comparison is computed.
REAL_LIFETIMES_S = {
    "muon": 2.1969811e-6,
    "tau_lepton": 2.903e-13,
    "neutron": 878.4,
    "charged_pion": 2.6033e-8,
    "charged_kaon": 1.238e-8,
}

FIT_BRANCH = "E"
FIT_TARGET = "muon"


class LifetimeBridgeError(ValueError):
    """Fail-closed native-lifetime-bridge contract error."""


def native_branch_times(deltas: Mapping[str, float], t_traj: float) -> Mapping[str, float]:
    """tau_j_native := t_traj / Delta_j for each branch. Refuses on non-finite/non-positive
    Delta_j or t_traj (a non-positive branch cost or trajectory duration has no decay-time
    interpretation)."""
    if not math.isfinite(t_traj) or t_traj <= 0:
        raise LifetimeBridgeError("t_traj must be finite and positive")
    if not deltas:
        # nice-to-have fix (independent review, 2026-07-25): fail closed on an empty branch set
        # rather than silently returning {} and letting a downstream lookup raise an unhelpful
        # bare KeyError instead of this module's own error type.
        raise LifetimeBridgeError("deltas must be a non-empty mapping")
    out = {}
    for branch, delta in deltas.items():
        if not math.isfinite(delta) or delta <= 0:
            raise LifetimeBridgeError(f"Delta_{branch} must be finite and positive, got {delta}")
        out[branch] = t_traj / delta
    return out


def run_fixture() -> Mapping[str, object]:
    branch_report = run_branch_fixture()
    deltas = {b: float(branch_report["branches"][b]["Delta"]) for b in ("U", "D", "E")}
    stepper = load_stepper()
    t_traj = N_STEPS * stepper.dt

    tau_native = native_branch_times(deltas, t_traj)

    if FIT_TARGET not in REAL_LIFETIMES_S:
        raise LifetimeBridgeError(f"fit target {FIT_TARGET!r} not in REAL_LIFETIMES_S")
    lambda_time = REAL_LIFETIMES_S[FIT_TARGET] / tau_native[FIT_BRANCH]
    if not math.isfinite(lambda_time) or lambda_time <= 0:
        raise LifetimeBridgeError("Lambda_time must be finite and positive")

    rows: List[Mapping[str, object]] = []
    for branch, tnat in tau_native.items():
        pred_s = lambda_time * tnat
        for target_name, target_s in REAL_LIFETIMES_S.items():
            err_pct = abs(pred_s - target_s) / target_s * 100.0
            rows.append({
                "branch": branch,
                "tau_native": tnat,
                "target": target_name,
                "target_s": target_s,
                "predicted_s": pred_s,
                "relative_error_pct": err_pct,
                "used_for_fit": (branch == FIT_BRANCH and target_name == FIT_TARGET),
            })

    rows_sorted = sorted(rows, key=lambda r: r["relative_error_pct"])
    non_fit_rows = [r for r in rows_sorted if not r["used_for_fit"]]
    n_under_5pct = sum(1 for r in non_fit_rows if r["relative_error_pct"] < 5.0)
    n_under_1000pct = sum(1 for r in non_fit_rows if r["relative_error_pct"] < 1000.0)

    return {
        "schema": "native-tau-c-lifetime-bridge-report-v0.1",
        "status": "FULL_GRID_COMPUTED_NO_CHERRY_PICKING",
        "tier": "fit_calibrated (Delta_j, PDG lifetimes) / Dr (tau_native mapping + fit pairing) / finite_diagnostic (15 rows, 14 held-out)",
        "t_traj_native": t_traj,
        "tau_native_by_branch": tau_native,
        "lambda_time_s_per_native_unit": lambda_time,
        "fit_pairing": {"branch": FIT_BRANCH, "target": FIT_TARGET},
        "full_table_sorted_by_error": rows_sorted,
        "n_held_out_rows": len(non_fit_rows),
        "n_held_out_under_5_percent": n_under_5pct,
        "n_held_out_under_1000_percent": n_under_1000pct,
        "honest_verdict": (
            f"Of {len(non_fit_rows)} held-out (branch, target) pairs (excludes the 1 row used to "
            f"fit Lambda_time by construction), {n_under_5pct} land under 5% and only "
            f"{n_under_1000pct} land under even 1000% error. The predicted native times span only "
            f"~2 orders of magnitude ({min(tau_native.values()):.2f} to "
            f"{max(tau_native.values()):.2f} native units), while the real target lifetimes span "
            f"~15 orders of magnitude (2.9e-13 s to 878.4 s) -- this architecture's branch "
            f"structure structurally CANNOT reproduce that dynamic range no matter how Lambda_time "
            f"is chosen. This is a clearer, more decisive negative result than any of today's "
            f"GeV/mass-based attempts: the time-unit route does not merely miss numerically, it "
            f"fails on dynamic range grounds that no single conversion factor can fix."
        ),
        "claim_boundary": [
            "the E<->muon fit pairing is a disclosed Dr-tier modeling choice (most defensible "
            "single pairing available: E is this repo's own lepton-branch label, muon is a "
            "lepton) -- not a derivation, and not claimed to be uniquely correct",
            "tau_j_native := t_traj/Delta_j is one possible, disclosed mapping from branch cost "
            "to a time-like quantity -- not the only one, not derived from root structure",
            "the core finding here is architectural, not a missed constant: real particle "
            "lifetimes span far more dynamic range than this construction's branch costs can "
            "produce, so no choice of Lambda_time could have closed this gap",
            "does not touch or resolve the ZERO_INFINITY_DUAL_DIAGNOSIS.md readout-vs-readout "
            "tension named earlier today -- real PDG lifetimes are used here exactly as "
            "routinely elsewhere in this project, that tension remains explicitly unresolved",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_fixture(), indent=2, sort_keys=True))
