# Root DAG Master — Quantum v0.1

**Standalone rule:** this file contains the complete 32-node Quantum DAG, not a pointer elsewhere.
Every node below corresponds to a `rule_id` in `RULE_REGISTRY.json`. Root `Q-R0` (`a != b`) is the
master retained distinction — the SAME root as `relativity/`, nothing here is a new axiom. This DAG
is a readout of `source_root/READOUT_GENESIS_CORE_SNAPSHOT.md`.

**The overriding discipline (do not blur this):** *"oscillation is NOT yet quantum."* None of
`{i, psi, Hilbert space H, Born rule p=|psi|^2, tensor product ⊗, [A,B]=i*hbar, spin, particles,
creation/annihilation, vacuum, coupling constants}` is a premise anywhere in this graph — each is a
**destination** reached only by passing its own gate (see `RULE_REGISTRY.json` → `gates`). The word
"quantum" is licensed only when state + norm + composition + channel + measurement close **together**
— they do not, here. This DAG is 43.75% strict green / 53.1% weighted of *this 32-node DAG only*.

Tier legend: `green` Coq/formal-closed (`Th_coqc` or exact-rational finite witness) ·
`yellow` formal-closed / bridge-partial · `red` open · `gray` measured/calibration adapter (none
active in this domain yet).

```mermaid
flowchart TD
    R0["Q-R0 a!=b retained distinction (shared root) [green]"] --> R1["Q-R1 ordered transitions, retention tau_c>0 [green]"]
    R1 --> R2["Q-R2 discrete ticks, finite causal graph [green]"]
    R2 --> R3["Q-R3 retained-distinction axioms FORCE L_R form [green, Th_coqc]"]
    R3 --> R4["Q-R4 telegraph coarse-grain / spine PDE M-d2+D-d+K [green]"]
    R4 --> R5["Q-R5 spine characteristic eq M*s^2+D*s+K*lambda=0 [green]"]

    %% ---- Oscillatory split (spine dispersion) ----
    R5 --> OS1["Q-OS1 oscillatory-regime split lambda_c=D^2/4MK [green, exact witness]"]

    %% ---- Asymmetric-seed / torsion branch ----
    R2 --> S1["Q-S1 seed trifurcation R0=Diag+SymOff+SkewOff [green, Th_coqc]"]
    S1 --> S2["Q-S2 seed torsion=SkewOff, group+rank-N [green, Th_coqc]"]
    S2 --> S3["Q-S3 seed torsion genuine mixing [green, Th_coqc]"]
    S3 --> X11["Q-X11 spin / spin-statistics [red, OPEN -- SkewOff is NOT spin]"]

    %% ---- Complexification / norm / evolution ----
    R2 --> C1["Q-C1 complexification gate: J^2=-I, G-skew (+failing control) [green]"]
    C1 --> N1["Q-N1 positive quantum norm N_Q>=0 [green, exact witness]"]
    N1 --> N2["Q-N2 reversible G-orthogonal evolution [green, exact witness]"]
    C1 --> X1["Q-X1 general root-derived complex psi [red, OPEN]"]
    N1 --> X1
    C1 --> X13["Q-X13 superposition gate, fixed-operator-only [red, OPEN beyond narrow case]"]
    N1 --> X13

    %% ---- Metric/curvature (folded from relativity) ----
    R2 --> G1["Q-G1 discrete metric/curvature chain (folded, relativity/OB-03,OB-04) [green, Th_coqc]"]

    %% ---- Yellow bridges ----
    R4 --> Y1["Q-Y1 QM/SR bounded algebraic identity (imported Minkowski) [yellow]"]
    R5 --> Y2["Q-Y2 telegraph crossover discriminant (spine's own) [yellow]"]
    OS1 --> Y3["Q-Y3 v^2=K/M conditional oscillator-parameter ID [yellow]"]
    G1 --> Y4["Q-Y4 metric/curvature-to-quantum-regime bridge [yellow]"]
    R1 --> M1["Q-M1 memory-before-mass, formal algebra [green, Th_coqc, folded into Y5]"]
    M1 --> Y5["Q-Y5 memory-before-mass physical/semantic bridge [yellow]"]
    N1 --> Y6["Q-Y6 channel/CPTP formal card, bridge-from-root open [yellow]"]
    N2 --> Y6

    %% ---- Open frontier (RED) ----
    C1 --> X2["Q-X2 quantum quotient q_Q (commuting square NOT proven) [red, OPEN -- central bottleneck]"]
    N1 --> X2
    N2 --> X2
    X2 --> X3["Q-X3 mixed-state from hidden lineage [red, OPEN]"]
    X2 --> X4["Q-X4 subsystem composition (x)_kappa [red, OPEN]"]
    X4 --> X9["Q-X9 correlation / CHSH / Tsirelson bound [red, OPEN]"]
    N1 --> X6["Q-X6 measurement / Born-rule uniqueness (TARGET) [red, OPEN]"]
    X6 --> X7["Q-X7 conditional update / collapse [red, OPEN]"]
    C1 --> X8["Q-X8 uncertainty relation (formal guard, not root-derivation) [red, OPEN]"]
    Y5 --> X10["Q-X10 mass / particle layer [red, OPEN]"]
    X2 --> X12["Q-X12 QFT (needs q_Q + q_relativity + q_geometry joint) [red, OPEN]"]
```

## The 32-node closure count (matches `quantum_closure_v0_1.py` exactly)

| Tier | Count | Nodes |
|---|---|---|
| **green** | 14 | Q-R0, Q-R1, Q-R2, Q-R3, Q-R4, Q-R5, Q-OS1, Q-S1, Q-S2, Q-S3, Q-C1, Q-N1, Q-N2, Q-G1 |
| **yellow** | 6 | Q-Y1, Q-Y2, Q-Y3, Q-Y4, Q-Y5, Q-Y6 |
| **red (open)** | 12 | Q-X1, Q-X2, Q-X3, Q-X4, Q-X6, Q-X7, Q-X8, Q-X9, Q-X10, Q-X11, Q-X12, Q-X13 |
| **total** | **32** | strict green `14/32=43.75%` · weighted `(14+6/2)/32=17/32=53.1%` |

`Q-M1` (memory-before-mass, formal) is cited but **not** counted as an independent 33rd node — it is
the supporting Coq witness folded into `Q-Y5`'s yellow accounting (its physical-mass bridge is what
stays open/declared, matching the verifier's own inline accounting).

## Corrected unified causal-QG DAG (retained distinction → quantum completion)

The second view below is the founder's corrected unified DAG showing how the *same* root that feeds
`relativity/` also feeds the quantum branch, through the shared asymmetric-seed trifurcation and
forced-operator machinery — ending at the still-open relativistic-quantum-field node.

```mermaid
flowchart TD
    RD["retained distinction δ_R (a!=b)"] --> SEED["asymmetric seed R0"]
    SEED --> DIAG["Diag part"]
    SEED --> SYM["SymOff part"]
    SEED --> SKEW["SkewOff part (torsion/circulation)"]
    DIAG --> FORCEDD["forced D (dissipative/diffusive coefficient)"]
    SYM --> FORCEDLR["forced L_R operator (InfoRetainedDistinctionForcesLaplacian)"]
    SKEW --> TORSION["torsion branch: group + rank-N + genuine mixing"]
    FORCEDLR --> FULLOP["full causal operator (spine M-d2+D-d+K)"]
    FORCEDD --> FULLOP
    FULLOP --> SPECTRAL["spectral / metric readout (Face 8, shared with relativity/OB-01)"]
    FULLOP --> TELEGRAPH["telegraph coarse-grain, crossover discriminant lambda_c"]
    SPECTRAL --> CURV["discrete curvature chain (Q-G1)"]
    TELEGRAPH --> OSC["oscillatory-regime split (Q-OS1) -- oscillation is NOT yet quantum"]
    OSC --> COMPLEX["complexification gate (Q-C1): i as a readout"]
    TORSION -.->|"NOT spin -- open bridge"| SPINOPEN["spin/statistics [red, OPEN]"]
    COMPLEX --> NORM["positive norm + reversible evolution (Q-N1/N2)"]
    NORM --> QQUOT["quantum quotient q_Q [red, OPEN -- central bottleneck]"]
    QQUOT --> MIXED["mixed state [red, OPEN]"]
    QQUOT --> COMPOSE["composition (x)_kappa [red, OPEN]"]
    NORM --> CHANNEL["channel/CPTP [yellow, bridge-from-root open]"]
    NORM --> MEASURE["measurement/Born [red, OPEN -- TARGET only]"]
    QQUOT -.->|"joint with relativity/q_g + geometry q_geometry, all still partial/open"| RQF["relativistic quantum field [red, OPEN -- QFT completion]"]
    CURV -.-> RQF
```

## Non-drift rule

Every node above is composed **only** from the root's own retained-distinction structure (`Q-R0`
through `Q-R5`), the asymmetric-seed trifurcation (`Q-S1..S3`), and the complexification/norm gates
(`Q-C1/N1/N2`) — no `i`, `psi`, Hilbert space, Born rule, tensor product, canonical commutator, spin,
particle, creation/annihilation operator, vacuum, or coupling constant is imported as a premise
anywhere in this graph; each appears only as a still-`red`/`OPEN` destination node or an explicitly
`yellow` bridge-partial connective. The one node folded in from `relativity/` (`Q-G1`, discrete
metric/curvature chain) is cited, not re-derived — it shares the same underlying `L_R` operator.

The `Q-Y1` (QM/SR bounded identity) node is explicitly never promoted past `yellow`: it inherits an
imported Minkowski signature from `relativity/`'s refused `InfoLorentzInvariance.v` chain (see
`PROVENANCE_CAUSAL_QG.md`) and must never be cited as "QM derived from one root."
