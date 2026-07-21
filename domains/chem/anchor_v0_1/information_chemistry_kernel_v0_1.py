#!/usr/bin/env python3
"""Information Chemistry v0.1 — self-contained computational kernel.

This file deliberately uses only the Python standard library.  It implements
four root operations:

1. infer finite interaction capacity from admission/obstruction tape;
2. quotient saturated connection graphs into structural normal forms;
3. derive stoichiometric coefficients from a retained-type null ledger;
4. construct two incompatible chemistries that satisfy the same retention law,
   proving that retention alone cannot select empirical compatibility.

It is a foundations kernel, not an electronic-structure or laboratory model.
"""

from __future__ import annotations

import itertools
import json
import math
import re
from collections import Counter, deque
from fractions import Fraction
from functools import reduce
from pathlib import Path


FORMULA_TOKEN = re.compile(r"([A-Z][a-z]?)([0-9]*)")


def parse_formula(formula: str) -> Counter[str]:
    """Read a simple molecular formula as a retained-type occupation vector."""
    position = 0
    result: Counter[str] = Counter()
    for match in FORMULA_TOKEN.finditer(formula):
        if match.start() != position:
            raise ValueError(f"unsupported formula: {formula}")
        kind, digits = match.groups()
        result[kind] += int(digits or "1")
        position = match.end()
    if position != len(formula) or not result:
        raise ValueError(f"unsupported formula: {formula}")
    return result


def discover_capacity(record: dict) -> int:
    admitted = sorted(set(record["admitted_incident_counts"]))
    obstructed = sorted(set(record["obstructed_incident_counts"]))
    if not admitted or admitted != list(range(admitted[-1] + 1)):
        raise ValueError("admission tape is not gap-free")
    capacity = admitted[-1]
    if not obstructed or obstructed[0] != capacity + 1:
        raise ValueError("obstruction tape does not close the capacity boundary")
    return capacity


def lcm(a: int, b: int) -> int:
    return abs(a * b) // math.gcd(a, b)


def primitive_positive_null_vector(matrix: list[list[int]]) -> list[int]:
    """Exact rational RREF for a one-dimensional positive nullspace."""
    a = [[Fraction(value) for value in row] for row in matrix]
    row_count, column_count = len(a), len(a[0])
    pivots: list[int] = []
    pivot_row = 0
    for column in range(column_count):
        candidate = next(
            (row for row in range(pivot_row, row_count) if a[row][column]), None
        )
        if candidate is None:
            continue
        a[pivot_row], a[candidate] = a[candidate], a[pivot_row]
        divisor = a[pivot_row][column]
        a[pivot_row] = [value / divisor for value in a[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not a[row][column]:
                continue
            factor = a[row][column]
            a[row] = [x - factor * y for x, y in zip(a[row], a[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break
    free = [column for column in range(column_count) if column not in pivots]
    if len(free) != 1:
        raise ValueError("kernel requires a one-dimensional stoichiometric nullspace")
    solution = [Fraction(0) for _ in range(column_count)]
    solution[free[0]] = Fraction(1)
    for row, pivot in reversed(list(enumerate(pivots))):
        solution[pivot] = -sum(
            a[row][column] * solution[column] for column in free
        )
    denominator = reduce(lcm, (value.denominator for value in solution), 1)
    integers = [int(value * denominator) for value in solution]
    if all(value < 0 for value in integers):
        integers = [-value for value in integers]
    if not all(value > 0 for value in integers):
        raise ValueError("declared sides have no all-positive primitive balance")
    divisor = reduce(math.gcd, integers)
    return [value // divisor for value in integers]


def balance_retained_ledger(reactants: list[str], products: list[str]) -> dict:
    species = reactants + products
    profiles = [parse_formula(formula) for formula in species]
    kinds = sorted({kind for profile in profiles for kind in profile})
    signed_matrix = [
        [
            profile[kind] if column < len(reactants) else -profile[kind]
            for column, profile in enumerate(profiles)
        ]
        for kind in kinds
    ]
    coefficients = primitive_positive_null_vector(signed_matrix)
    residual = {
        kind: sum(
            coefficients[column] * signed_matrix[row][column]
            for column in range(len(species))
        )
        for row, kind in enumerate(kinds)
    }
    return {
        "species": species,
        "retained_kinds": kinds,
        "signed_ledger_matrix": signed_matrix,
        "coefficients": dict(zip(species, coefficients)),
        "retention_residual": residual,
    }


def edge_universe(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def degree_sequence(n: int, edges: tuple[tuple[int, int], ...]) -> list[int]:
    degree = [0] * n
    for i, j in edges:
        degree[i] += 1
        degree[j] += 1
    return degree


def connected(n: int, edges: tuple[tuple[int, int], ...]) -> bool:
    if n == 1:
        return True
    adjacency = [[] for _ in range(n)]
    for i, j in edges:
        adjacency[i].append(j)
        adjacency[j].append(i)
    seen, queue = {0}, deque([0])
    while queue:
        node = queue.popleft()
        for neighbour in adjacency[node]:
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)
    return len(seen) == n


def canonical_unlabelled_key(n: int, edges: tuple[tuple[int, int], ...]) -> str:
    edge_set = {tuple(sorted(edge)) for edge in edges}
    candidates = []
    for permutation in itertools.permutations(range(n)):
        transformed = {
            tuple(sorted((permutation[i], permutation[j]))) for i, j in edge_set
        }
        candidates.append(
            "".join(
                "1" if edge in transformed else "0" for edge in edge_universe(n)
            )
        )
    return min(candidates)


def saturated_normal_forms(n_x: int, inventory_y: int, capacity_x: int) -> list[dict]:
    """Find X skeleton normal forms; monovalent Y saturates remaining ports."""
    universe = edge_universe(n_x)
    forms: dict[str, dict] = {}
    lineages: Counter[str] = Counter()
    for bits in itertools.product((0, 1), repeat=len(universe)):
        edges = tuple(edge for edge, bit in zip(universe, bits) if bit)
        if not connected(n_x, edges):
            continue
        degrees = degree_sequence(n_x, edges)
        if any(degree > capacity_x for degree in degrees):
            continue
        attached_y = [capacity_x - degree for degree in degrees]
        if sum(attached_y) != inventory_y:
            continue
        key = canonical_unlabelled_key(n_x, edges)
        lineages[key] += 1
        forms.setdefault(
            key,
            {
                "normal_form_id": key or "single-X",
                "x_degree_profile": sorted(degrees, reverse=True),
                "y_attachment_profile": sorted(attached_y, reverse=True),
                "composition": {"X": n_x, "Y": inventory_y},
            },
        )
    result = []
    for key in sorted(forms):
        form = forms[key]
        form["retained_labelled_lineages"] = lineages[key]
        result.append(form)
    return result


def perfect_matchings(nodes: tuple[int, ...]) -> list[tuple[tuple[int, int], ...]]:
    if not nodes:
        return [tuple()]
    first = nodes[0]
    result = []
    for index in range(1, len(nodes)):
        second = nodes[index]
        remainder = nodes[1:index] + nodes[index + 1 :]
        for matching in perfect_matchings(remainder):
            result.append(((first, second),) + matching)
    return result


def component_compositions(
    labels: list[str], edges: tuple[tuple[int, int], ...]
) -> tuple[str, ...]:
    adjacency = [[] for _ in labels]
    for i, j in edges:
        adjacency[i].append(j)
        adjacency[j].append(i)
    unseen = set(range(len(labels)))
    components = []
    while unseen:
        root = next(iter(unseen))
        stack, members = [root], []
        unseen.remove(root)
        while stack:
            node = stack.pop()
            members.append(node)
            for neighbour in adjacency[node]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    stack.append(neighbour)
        counts = Counter(labels[node] for node in members)
        components.append(
            "".join(kind + (str(count) if count != 1 else "") for kind, count in sorted(counts.items()))
        )
    return tuple(sorted(components))


def compatibility_countermodels() -> dict:
    """Construct two empirical chemistries with identical retained inventory."""
    labels = ["A", "A", "B", "B"]
    nodes = tuple(range(len(labels)))
    models = {
        "same_kind_only": {("A", "A"), ("B", "B")},
        "cross_kind_only": {("A", "B"), ("B", "A")},
    }
    outputs = {}
    for name, allowed in models.items():
        admitted = []
        for matching in perfect_matchings(nodes):
            if all((labels[i], labels[j]) in allowed for i, j in matching):
                admitted.append(component_compositions(labels, matching))
        outputs[name] = [list(composition) for composition in sorted(set(admitted))]
    initial = dict(Counter(labels))
    return {
        "shared_initial_inventory": initial,
        "shared_capacity": {"A": 1, "B": 1},
        "model_outputs": outputs,
        "both_preserve_retention": all(outputs.values()),
        "outputs_disagree": outputs["same_kind_only"] != outputs["cross_kind_only"],
        "conclusion": (
            "Retention and capacity do not determine compatibility: empirical "
            "interaction structure is an independent required input."
        ),
    }


def run_foundations() -> dict:
    tape = {
        "X": {
            "admitted_incident_counts": [0, 1, 2, 3, 4],
            "obstructed_incident_counts": [5],
        },
        "Y": {
            "admitted_incident_counts": [0, 1],
            "obstructed_incident_counts": [2],
        },
    }
    capacities = {kind: discover_capacity(record) for kind, record in tape.items()}
    family = []
    for n_x in range(1, 5):
        inventory_y = n_x * capacities["X"] - 2 * max(0, n_x - 1)
        forms = saturated_normal_forms(n_x, inventory_y, capacities["X"])
        family.append(
            {
                "composition": {"X": n_x, "Y": inventory_y},
                "normal_form_count": len(forms),
                "normal_forms": forms,
                "lineage_count": sum(f["retained_labelled_lineages"] for f in forms),
            }
        )
    return {
        "kernel_version": "Information-Chemistry-0.1",
        "dependencies": "Python standard library only",
        "derivation_1_capacity": {
            "interaction_tape": tape,
            "discovered_capacities": capacities,
        },
        "derivation_2_structural_identity": {
            "anonymous_saturated_family": family,
            "finding": "X4Y10 has two normal forms but sixteen labelled lineages",
        },
        "derivation_3_stoichiometry": balance_retained_ledger(
            ["CH4", "O2"], ["CO2", "H2O"]
        ),
        "theorem_1_no_free_chemistry": compatibility_countermodels(),
        "claim_boundary": {
            "established_by_kernel": [
                "capacity inference from a closed admission/obstruction tape",
                "structural quotient under node relabelling",
                "composition is insufficient for structural identity",
                "stoichiometric balance follows from retained-type conservation",
                "retention alone underdetermines empirical compatibility",
            ],
            "still_requires_empirical_or_additional_structure": [
                "real element interaction profiles",
                "bond order, geometry, electronic state and energy",
                "product selection and reaction rates",
                "thermodynamic and quantum readout calibration",
            ],
        },
    }


def main() -> None:
    result = run_foundations()
    output = Path(__file__).with_name("information_chemistry_kernel_result.json")
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
