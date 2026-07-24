from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
phi = (1.0 + math.sqrt(5.0)) / 2.0
N_tau = np.array([[0.0, 1.0], [1.0, 1.0]])
eigenvalues = np.linalg.eigvals(N_tau)
spectral_radius = float(np.max(np.abs(eigenvalues)))
checks = {
    "fusion_matrix": N_tau.tolist(),
    "characteristic_polynomial": "lambda^2-lambda-1",
    "spectral_radius": spectral_radius,
    "phi": phi,
    "spectral_radius_equals_phi": bool(np.isclose(spectral_radius, phi)),
    "fusion_identity_residual": float(abs(phi * phi - phi - 1.0)),
    "golden_rotation": 1.0 / (phi * phi),
    "golden_angle_radians": 2.0 * math.pi / (phi * phi),
    "status": "PASS" if np.isclose(spectral_radius, phi) else "FAIL",
}
(ROOT / "retained_history_phi_check.json").write_text(json.dumps(checks, indent=2), encoding="utf-8")
print(json.dumps(checks, indent=2))
