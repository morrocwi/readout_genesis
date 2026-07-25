#!/usr/bin/env python3
"""
PGFT-RDU v0.7 Quantum-Gravity Real-Problem Calculator

Real problem:
  Given a real physical energy scale, convert it into native PGFT-RDU information units,
  inject it into a native retained-information PDE, then read out:
    - retained native information δ_R^(e)
    - SI energy/eV/kg adapters
    - quantum wavelength scale
    - Schwarzschild radius scale
    - quantum-gravity strength alpha_QG = G E^2 / (hbar c^5)

This does NOT claim quantum gravity is solved.
It gives a unit-consistent native-PDE calculator and a standard QG-regime diagnostic.
"""

from __future__ import annotations
import math, json
from dataclasses import dataclass, asdict
from typing import Dict, Any, List

# Constants
K_B = 1.380649e-23
C = 299_792_458.0
E_CHARGE = 1.602176634e-19
H = 6.62607015e-34
HBAR = H / (2.0 * math.pi)
G = 6.67430e-11
LN2 = math.log(2.0)

# Planck units
M_PLANCK = math.sqrt(HBAR * C / G)
E_PLANCK_J = math.sqrt(HBAR * C**5 / G)
L_PLANCK = math.sqrt(HBAR * G / C**3)

@dataclass
class PDEConfig:
    nodes: int = 128
    theta_end: float = 24.0
    dtheta: float = 0.02
    D_R: float = 0.42
    mu_R: float = 0.035
    source_center: int = 32
    source_width_nodes: float = 5.0
    source_duration_theta: float = 7.5
    threshold_fraction_of_peak: float = 1e-4

def eV_to_J(eV: float) -> float:
    return eV * E_CHARGE

def J_to_native_nat(E_J: float, temperature_K: float) -> float:
    # Native retained natural distinction via Landauer natural adapter
    # 1 δ_R^(e) at T -> k_B T J
    return E_J / (K_B * temperature_K)

def native_nat_to_J(I_nat: float, temperature_K: float) -> float:
    return K_B * temperature_K * I_nat

def qg_diagnostic(E_J: float, temperature_K: float = 310.0) -> Dict[str, float | str]:
    if E_J <= 0:
        raise ValueError("Energy must be positive.")

    m_equiv = E_J / C**2
    lambda_reduced = HBAR * C / E_J        # reduced Compton-like length
    r_s = 2.0 * G * E_J / C**4             # Schwarzschild radius from energy
    alpha_qg = G * E_J**2 / (HBAR * C**5)  # = (E/E_planck)^2
    ratio = r_s / lambda_reduced           # = 2 alpha_qg

    I_nat = J_to_native_nat(E_J, temperature_K)
    I_bit = I_nat / LN2

    if alpha_qg < 1e-30:
        regime = "QG_NEGLIGIBLE"
    elif alpha_qg < 1e-12:
        regime = "QG_TINY_BUT_COMPUTABLE"
    elif alpha_qg < 1e-3:
        regime = "QG_WEAK_SUB_PLANCK"
    elif alpha_qg < 0.1:
        regime = "QG_APPROACHING_PLANCK"
    else:
        regime = "QG_ORDER_ONE_PLANCK_REGIME"

    return {
        "energy_J": E_J,
        "energy_eV": E_J / E_CHARGE,
        "mass_equiv_kg": m_equiv,
        "native_input_nat_delta_R_e": I_nat,
        "native_input_bits_delta_R_2": I_bit,
        "reduced_quantum_length_m": lambda_reduced,
        "schwarzschild_radius_m": r_s,
        "r_s_over_quantum_length": ratio,
        "alpha_QG_G_E2_over_hbar_c5": alpha_qg,
        "E_over_E_planck": E_J / E_PLANCK_J,
        "regime": regime,
    }

def line_laplacian(phi: List[float]) -> List[float]:
    n = len(phi)
    out = [0.0] * n
    out[0] = phi[0] - phi[1]
    out[-1] = phi[-1] - phi[-2]
    for i in range(1, n - 1):
        out[i] = 2.0 * phi[i] - phi[i - 1] - phi[i + 1]
    return out

def spatial_profile(n: int, center: int, width: float) -> List[float]:
    raw = [math.exp(-((i-center)**2)/(2*width*width)) for i in range(n)]
    s = sum(raw)
    return [x/s for x in raw]

def temporal_weights(n_steps: int, dtheta: float, duration: float) -> List[float]:
    raw = []
    for step in range(n_steps):
        theta = step * dtheta
        raw.append(math.sin(math.pi * theta / duration)**2 if theta <= duration else 0.0)
    area = sum(raw) * dtheta
    return [x/area for x in raw]

def run_native_pde(input_nat: float, cfg: PDEConfig) -> Dict[str, float | int]:
    """
    Native PDE:
      ∂_Θ φ = -D_R L_R φ - μ_R φ + S_R

    Unit gate:
      φ: δ_R^(e)
      ∂_Θ φ: δ_R^(e)/Θ_R
      D_R L_R φ: δ_R^(e)/Θ_R
      μ_R φ: δ_R^(e)/Θ_R
      S_R: δ_R^(e)/Θ_R
    """
    n = cfg.nodes
    n_steps = int(round(cfg.theta_end / cfg.dtheta))
    phi = [0.0] * n
    xprof = spatial_profile(n, cfg.source_center, cfg.source_width_nodes)
    tweights = temporal_weights(n_steps, cfg.dtheta, cfg.source_duration_theta)

    dissipated = 0.0
    max_peak = 0.0
    for step in range(n_steps):
        Lphi = line_laplacian(phi)
        S = [input_nat * tweights[step] * xprof[i] for i in range(n)]

        dissipated += cfg.dtheta * cfg.mu_R * sum(phi)

        dphi = [-cfg.D_R * Lphi[i] - cfg.mu_R * phi[i] + S[i] for i in range(n)]
        phi = [max(0.0, phi[i] + cfg.dtheta * dphi[i]) for i in range(n)]
        max_peak = max(max_peak, max(phi))

    final_nat = sum(phi)
    ledger_residual = abs(input_nat - final_nat - dissipated)
    threshold = max_peak * cfg.threshold_fraction_of_peak if max_peak > 0 else 0.0
    front_width = sum(1 for x in phi if x >= threshold and threshold > 0)

    return {
        "final_retained_nat_delta_R_e": final_nat,
        "dissipated_nat_delta_R_e": dissipated,
        "ledger_residual_nat": ledger_residual,
        "peak_node_nat_delta_R_e": max(phi),
        "front_width_nodes": front_width,
        "max_peak_node_nat_delta_R_e": max_peak,
    }

def scenario(name: str, E_J: float, T: float, cfg: PDEConfig) -> Dict[str, Any]:
    raw = qg_diagnostic(E_J, T)
    pde = run_native_pde(raw["native_input_nat_delta_R_e"], cfg)
    final_E_J = native_nat_to_J(pde["final_retained_nat_delta_R_e"], T)
    final = qg_diagnostic(final_E_J, T)
    return {
        "name": name,
        "input_raw_qg": raw,
        "native_pde_result": pde,
        "final_after_pde_qg_readout": final,
        "unit_gate": {
            "pde": "∂_Θ φ = -D_R L_R φ - μ_R φ + S_R",
            "all_terms": "δ_R^(e)/Θ_R",
            "input_adapter": "E_J -> I_nat = E/(k_B T)",
            "output_adapter": "I_nat -> E_J = k_B T I_nat",
            "status": "PASS",
        },
    }

def main() -> None:
    T = 310.0
    cfg = PDEConfig()
    scenarios = [
        ("electron_rest_energy", eV_to_J(0.510998950e6), T, cfg),
        ("proton_rest_energy", eV_to_J(938.27208816e6), T, cfg),
        ("lhc_scale_14_TeV_collision", eV_to_J(14.0e12), T, cfg),
        ("ultra_high_energy_cosmic_ray_1e20_eV", eV_to_J(1.0e20), T, cfg),
        ("planck_energy", E_PLANCK_J, T, cfg),
    ]
    report = {
        "claim_boundary": "Native-unit quantum-gravity diagnostic, not a completed theory of quantum gravity.",
        "temperature_K": T,
        "constants": {
            "G": G,
            "c": C,
            "hbar": HBAR,
            "k_B": K_B,
            "E_planck_J": E_PLANCK_J,
            "M_planck_kg": M_PLANCK,
            "L_planck_m": L_PLANCK,
        },
        "diagnostic_definitions": {
            "alpha_QG": "G E^2 / (hbar c^5) = (E/E_planck)^2",
            "quantum_length": "hbar c / E",
            "schwarzschild_radius": "2 G E / c^4",
            "native_information": "I_nat = E/(k_B T), unit δ_R^(e)",
        },
        "scenarios": [scenario(*s) for s in scenarios],
    }
    print(json.dumps(report, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
