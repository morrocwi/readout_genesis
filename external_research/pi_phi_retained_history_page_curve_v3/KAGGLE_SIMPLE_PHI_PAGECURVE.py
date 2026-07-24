# Kaggle one-cell code: simple phi-schedule Page-curve test
# Finite-qubit simulation only; not a black-hole or quantum-gravity result.

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

MASTER_SEED = 20260724
BLACK_HOLE_QUBITS = 5
SCRAMBLE_DEPTH = 3
N_CIRCUITS = 8
SETTING_PAIRS_PER_POINT = 600
PHI = (1.0 + math.sqrt(5.0)) / 2.0
GOLDEN_FRACTION = 1.0 / (PHI * PHI)

I2 = np.array([[1, 0], [0, 1]], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULIS = np.stack([I2, X, Y, Z])
PAULI_FORWARD = np.zeros((4, 4), dtype=complex)
for p, matrix in enumerate(PAULIS):
    for i in range(2):
        for j in range(2):
            PAULI_FORWARD[p, 2 * i + j] = matrix[j, i]


def random_unitary(dimension, rng):
    matrix = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    q, r = np.linalg.qr(matrix)
    diagonal = np.diag(r)
    phases = np.where(np.abs(diagonal) > 0, diagonal / np.abs(diagonal), 1.0)
    return q * phases.conj()


def apply_gate(state, gate, targets, n_qubits):
    targets = list(targets)
    rest = [q for q in range(n_qubits) if q not in targets]
    permutation = targets + rest
    inverse = np.argsort(permutation)
    tensor = state.reshape([2] * n_qubits).transpose(permutation).reshape(2 ** len(targets), -1)
    tensor = gate @ tensor
    return tensor.reshape([2] * n_qubits).transpose(inverse).reshape(-1)


def swap_qubits(state, q1, q2, n_qubits):
    return state.reshape([2] * n_qubits).swapaxes(q1, q2).reshape(-1)


def reduced_density_matrix(state, keep_qubits, n_qubits):
    keep_qubits = list(keep_qubits)
    rest = [q for q in range(n_qubits) if q not in keep_qubits]
    matrix = state.reshape([2] * n_qubits).transpose(keep_qubits + rest).reshape(2 ** len(keep_qubits), -1)
    rho = matrix @ matrix.conj().T
    return 0.5 * (rho + rho.conj().T)


def apply_local_transform(tensor, matrix, axis):
    transformed = np.tensordot(matrix, tensor, axes=(1, axis))
    return np.moveaxis(transformed, 0, axis)


def rho_to_pauli_coefficients(rho):
    dimension = rho.shape[0]
    n_qubits = int(round(math.log2(dimension)))
    if n_qubits == 0:
        return np.array([1.0])
    tensor = rho.reshape([2] * n_qubits + [2] * n_qubits)
    interleaved_axes = []
    for q in range(n_qubits):
        interleaved_axes.extend([q, n_qubits + q])
    tensor = tensor.transpose(interleaved_axes).reshape([4] * n_qubits)
    for axis in range(n_qubits):
        tensor = apply_local_transform(tensor, PAULI_FORWARD, axis)
    return np.real_if_close(tensor, tol=1000).real.reshape(-1)


def simulate_evaporation(seed):
    rng = np.random.default_rng(seed)
    n_black_hole = BLACK_HOLE_QUBITS
    n_total = 2 * n_black_hole
    state = np.zeros(2 ** n_total, dtype=complex)
    state[0] = 1.0
    active_black_hole = list(range(n_black_hole))
    radiation_states = []
    for step in range(n_black_hole + 1):
        radiation_qubits = list(range(n_black_hole, n_black_hole + step))
        radiation_states.append(reduced_density_matrix(state, radiation_qubits, n_total))
        if step == n_black_hole:
            break
        for _ in range(SCRAMBLE_DEPTH):
            shuffled = list(rng.permutation(active_black_hole))
            for i in range(0, len(shuffled) - 1, 2):
                state = apply_gate(state, random_unitary(4, rng), [int(shuffled[i]), int(shuffled[i + 1])], n_total)
            if len(shuffled) % 2 == 1:
                state = apply_gate(state, random_unitary(2, rng), [int(shuffled[-1])], n_total)
        emitted = active_black_hole.pop()
        radiation_target = n_black_hole + step
        state = swap_qubits(state, emitted, radiation_target, n_total)
    return radiation_states


def schedule_indices(schedule_name, n_settings, n_samples, rng):
    if schedule_name == "random":
        return rng.integers(0, n_settings, size=n_samples)
    if schedule_name == "cyclic":
        return np.arange(n_samples) % n_settings
    if schedule_name == "golden":
        k = np.arange(n_samples, dtype=float)
        points = ((k + 0.5) * GOLDEN_FRACTION) % 1.0
        return np.floor(points * n_settings).astype(int)
    raise ValueError(f"Unknown schedule: {schedule_name}")


def signed_purity_estimate(pauli_coefficients, schedule_name, n_setting_pairs, rng):
    n_settings = len(pauli_coefficients)
    dimension = int(round(math.sqrt(n_settings)))
    indices = schedule_indices(schedule_name, n_settings, n_setting_pairs, rng)
    expectations = np.clip(pauli_coefficients[indices], -1.0, 1.0)
    probabilities = (1.0 + expectations) / 2.0
    outcome_a = np.where(rng.random(n_setting_pairs) < probabilities, 1.0, -1.0)
    outcome_b = np.where(rng.random(n_setting_pairs) < probabilities, 1.0, -1.0)
    return float(dimension * np.mean(outcome_a * outcome_b))


def main():
    rows = []
    schedules = ["random", "cyclic", "golden"]
    for circuit in range(N_CIRCUITS):
        radiation_states = simulate_evaporation(MASTER_SEED + circuit)
        for step, rho in enumerate(radiation_states):
            ideal_purity = float(np.trace(rho @ rho).real)
            coefficients = rho_to_pauli_coefficients(rho)
            physical_floor = 1.0 if step == 0 else 1.0 / (2 ** step)
            for schedule_number, schedule_name in enumerate(schedules):
                local_rng = np.random.default_rng(MASTER_SEED + 100000 * circuit + 1000 * step + schedule_number)
                estimate = signed_purity_estimate(coefficients, schedule_name, SETTING_PAIRS_PER_POINT, local_rng)
                physical = physical_floor <= estimate <= 1.0
                rows.append({
                    "circuit": circuit,
                    "step": step,
                    "radiation_qubits": step,
                    "schedule": schedule_name,
                    "ideal_purity": ideal_purity,
                    "signed_purity_estimate": estimate,
                    "absolute_error": abs(estimate - ideal_purity),
                    "physical_floor": physical_floor,
                    "physical_translation_pass": physical,
                    "translated_renyi2": -math.log(estimate) if physical else np.nan,
                })
    results = pd.DataFrame(rows)
    summary_rows = []
    for schedule_name in schedules:
        part = results[results["schedule"] == schedule_name]
        summary_rows.append({
            "schedule": schedule_name,
            "purity_rmse": float(np.sqrt(np.mean((part["signed_purity_estimate"] - part["ideal_purity"]) ** 2))),
            "physical_translation_rate": float(part["physical_translation_pass"].mean()),
            "negative_readout_rate": float((part["signed_purity_estimate"] < 0).mean()),
        })
    summary = pd.DataFrame(summary_rows).sort_values("purity_rmse")
    random_rmse = float(summary.loc[summary["schedule"] == "random", "purity_rmse"].iloc[0])
    golden_rmse = float(summary.loc[summary["schedule"] == "golden", "purity_rmse"].iloc[0])
    improvement = 100.0 * (random_rmse - golden_rmse) / random_rmse
    print("\nSIMPLE PHI-SCHEDULE PAGE-CURVE TEST")
    print("=" * 60)
    print(summary.to_string(index=False))
    print(f"\nGolden vs random purity-RMSE improvement: {improvement:.2f}%")
    print("Important: negative estimates are retained as signed readouts and are not converted into entropy.")
    output_dir = Path("/kaggle/working")
    if not output_dir.exists():
        output_dir = Path.cwd()
    results.to_csv(output_dir / "simple_phi_pagecurve_results.csv", index=False)
    summary.to_csv(output_dir / "simple_phi_pagecurve_summary.csv", index=False)
    plot_table = results.groupby(["step", "schedule"])["absolute_error"].mean().unstack()
    plt.figure(figsize=(8, 5))
    for schedule_name in schedules:
        plt.plot(plot_table.index, plot_table[schedule_name], marker="o", label=schedule_name)
    plt.xlabel("Emitted radiation qubits")
    plt.ylabel("Mean absolute purity error")
    plt.title("Random, cyclic, and golden-ratio schedules")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "simple_phi_pagecurve.png", dpi=180)
    print("\nSaved:", output_dir / "simple_phi_pagecurve_results.csv", output_dir / "simple_phi_pagecurve_summary.csv", sep="\n")


if __name__ == "__main__":
    main()
