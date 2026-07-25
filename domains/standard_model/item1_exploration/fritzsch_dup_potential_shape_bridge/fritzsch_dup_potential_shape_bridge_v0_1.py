#!/usr/bin/env python3
"""Fritzsch D_up -> mother-potential shape bridge, v0.1.

Stacked on the merged order-vacuum threshold closure. Per the founder's own explicit direction
(2026-07-25): use `D_up` (the fit_calibrated (2,2) entry of the up-quark mass matrix from
`item22_exploration/fritzsch_extended_texture_v1.py` / `item24_exploration/
cp_phase_jarlskog_v1.py`, D_up=5.5200 GeV, fit to real PDG CKM angles + the Jarlskog CP invariant)
to replace the mother potential's currently-arbitrary, never-justified `b=1` coefficient, INSTEAD
of trying (again) to connect Fritzsch's real-data result to `M` directly.

*** REGIME-MATCH CHECK, done explicitly BEFORE building this file (required discipline, per the
    2026-07-25 self-critique on PR #81 comparing two mismatched-regime quantities without this
    check first): `M` is the coefficient of the mother PDE's SECOND TIME DERIVATIVE (a kinetic/
    inertia term). `D_up` is an entry of a MASS MATRIX / Yukawa-like coupling structure -- the
    same STRUCTURAL ROLE as `K` (the L_R coupling coefficient) or `a,b` (the potential-shape
    coefficients), NOT the same role as `M`. This file therefore does NOT attempt to identify
    D_up with M (that would repeat PR #81's mistake) -- it uses D_up to inform the POTENTIAL
    SHAPE (`b`), a role-matched substitution. ***

METHOD: b_new := D_up / m_c (m_c = charm quark mass, GeV, from `fit_calibrated_registry.py` --
the same up-type sector D_up itself was fit within, giving a dimensionless ratio from two
ALREADY-fit_calibrated real quantities, no new external anchor invented). alpha_order stays
`a/2=-0.5` (a is untouched by this experiment). Re-solves the order-vacuum phase with this ONE
changed coefficient and reports what changes, honestly, whichever way it goes.

Tier: `fit_calibrated` for D_up and the quark masses (both already established elsewhere, reused
not re-derived here). `Dr` for the `b_new := D_up/m_c` mapping itself -- an explicitly disclosed
MODELING CHOICE, not a derivation; a different, equally defensible normalization (e.g. D_up/m_t)
would give a different b_new, and this file does not claim m_c is uniquely the right denominator.
`finite_diagnostic` for the resulting order-vacuum numbers.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parents[4]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

ORDER_DIR = ROOT / "domains" / "standard_model" / "item1_exploration" / "order_vacuum_threshold_closure"
if str(ORDER_DIR) not in sys.path:
    sys.path.insert(0, str(ORDER_DIR))

from domains.standard_model.item1_exploration.order_vacuum_threshold_closure.order_vacuum_threshold_closure_v0_1 import (  # noqa: E402
    run_fixture as run_order_fixture,
    solve_phase,
)
from domains.standard_model.fit_calibrated_registry import PDG_MASSES_GEV  # noqa: E402

EPS = 1e-15

# D_up: fit_calibrated, reused verbatim from item24_exploration/cp_phase_jarlskog_v1.py's own
# disclosed grid-search result (2026-07-24/25). Re-cited here, not re-run -- re-running that
# file's own grid search is out of scope for this bridge; if it ever drifts, this constant will
# go stale and should be refreshed from that file's own live output.
D_UP_GEV = 5.5200

# m_c: charm quark mass, GeV, PDG-fit_calibrated, same up-type sector D_up was fit within.
M_C_GEV = PDG_MASSES_GEV["c"]


class FritzschBridgeError(ValueError):
    """Fail-closed Fritzsch-D_up-bridge contract error."""


def derive_b_new(d_up_gev: float = D_UP_GEV, m_c_gev: float = M_C_GEV) -> Mapping[str, object]:
    """b_new := D_up / m_c -- a disclosed Dr-tier modeling choice, not a derivation."""
    if not math.isfinite(d_up_gev) or d_up_gev <= 0:
        raise FritzschBridgeError("D_up_gev must be finite and positive")
    if not math.isfinite(m_c_gev) or m_c_gev <= 0:
        raise FritzschBridgeError("m_c_gev must be finite and positive")
    b_new = d_up_gev / m_c_gev
    if not math.isfinite(b_new):
        # REQUIRED FIX (independent review, 2026-07-25): the two pre-checks above validate
        # d_up_gev and m_c_gev individually, but their quotient can still overflow to inf for
        # sufficiently extreme (still individually finite/positive) inputs -- not exploitable via
        # this file's own fixed D_UP_GEV/M_C_GEV constants, but a real gap in a function whose own
        # class promises fail-closed behavior.
        raise FritzschBridgeError(f"b_new=D_up/m_c must be finite, got {b_new}")
    return {
        "bridge_id": "fritzsch-Dup-over-mc-potential-shape-v0.1",
        "tier": "Dr (disclosed modeling choice, not a derivation)",
        "D_up_gev": d_up_gev,
        "m_c_gev": m_c_gev,
        "b_new": b_new,
        "status": "MODELING_CHOICE_NOT_DERIVED",
    }


def run_fixture() -> Mapping[str, object]:
    baseline = run_order_fixture()
    lambdas = baseline["primitive_branch_source"]["lambdas"]
    alpha_order = baseline["phase"]["alpha_order"]  # a/2, UNCHANGED by this experiment

    bridge = derive_b_new()
    beta_order_new = bridge["b_new"] / 4.0
    if beta_order_new <= 0:
        raise FritzschBridgeError("beta_order_new=b_new/4 must be positive for the v1.13 convexity theorem")

    phase_new = solve_phase(alpha=alpha_order, beta=beta_order_new, lambdas=lambdas)

    return {
        "schema": "fritzsch-dup-potential-shape-bridge-report-v0.1",
        "status": phase_new["status"],
        "tier": "fit_calibrated (D_up, m_c) / Dr (b_new mapping) / finite_diagnostic (phase numbers)",
        "b_new_bridge": bridge,
        "baseline_phase": {
            "alpha_order": baseline["phase"]["alpha_order"],
            "beta_order": baseline["phase"]["beta_order"],
            "status": baseline["phase"]["status"],
            "r_star": baseline["phase"]["r_star"],
            "order_margin": baseline["phase"]["order_margin"],
        },
        "experiment_phase": {
            "alpha_order": alpha_order,
            "beta_order": beta_order_new,
            "status": phase_new["status"],
            "r_star": phase_new["r_star"],
            "order_margin": phase_new["order_margin"],
            "Pi0": phase_new["Pi0"],
        },
        "comparison": {
            "r_star_baseline": baseline["phase"]["r_star"],
            "r_star_experiment": phase_new["r_star"],
            "r_star_ratio": phase_new["r_star"] / baseline["phase"]["r_star"],
            "beta_order_ratio": beta_order_new / baseline["phase"]["beta_order"],
        },
        "claim_boundary": [
            "D_up and m_c are both fit_calibrated (real PDG-fit quantities), reused not "
            "re-derived here -- D_up from item24_exploration/cp_phase_jarlskog_v1.py's own "
            "disclosed grid search, m_c from fit_calibrated_registry.py",
            "NICE-TO-HAVE DISCLOSURE (independent review, 2026-07-25): D_up is not itself a "
            "principled anchor -- its own source files (fritzsch_extended_texture_v1.py, "
            "cp_phase_jarlskog_v1.py) already disclose it as an OPENLY DECLARED, ADDITIONAL free "
            "fit parameter, chosen by grid search to minimize CKM-angle mismatch, not derived. "
            "This file's b_new inherits that upstream un-derived-ness on top of its own "
            "denominator-choice arbitrariness -- two stacked disclosed modeling choices, not one.",
            "b_new := D_up/m_c is an explicitly disclosed Dr-tier MODELING CHOICE, not a "
            "derivation -- a different, equally defensible normalization (e.g. D_up/m_t) would "
            "give a different b_new; this file does not claim m_c is uniquely correct",
            "REGIME CHECK (required discipline after the 2026-07-25 self-critique): D_up plays a "
            "potential/coupling-matrix role, matching a,b's role in the mother potential -- NOT "
            "M's kinetic/inertia role. This file deliberately does NOT identify D_up with M.",
            "still Pi0>alpha_order structurally guaranteed on this stepper regardless of branch "
            "data (unchanged from order_vacuum_threshold_closure_v0_1.py's own disclosure) -- "
            "the ORDERED_READY status itself remains uninformative; what is informative here is "
            "whether r_star moves in a principled, non-arbitrary way when beta_order is set from "
            "real data instead of an unexplained b=1",
            "no GeV-scale physical prediction is made or claimed anywhere in this file -- "
            "r_star/Pi0/order_margin remain native-unit quantities throughout",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run_fixture(), indent=2, sort_keys=True))
