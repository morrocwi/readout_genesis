# Root DAG Master v0.901

**Status:** frozen for every descendant release.  A later release may add nodes only through an explicit delta; it may not delete, silently rename, or retype these nodes.

```mermaid
flowchart TD
    R0["R0 ROOT: retained distinction"] --> R1["R1 identity/history/lineage/context"]
    R1 --> R2["R2 typed retained state + boundary"]
    R2 --> R3["R3 quotient sufficiency/refinement"]
    R2 --> R4["R4 ledger map L(n)=A n"]
    R4 --> R5["R5 closed-boundary conservation"]
    R5 --> R6["R6 kernel of preserving changes"]
    R6 --> R7["R7 extent coordinates"]
    R7 --> R8["R8 positivity/capacity region"]
    R2 --> R9["R9 conditional additive-readout theorem"]
    R3 --> R10["R10 observational stationarity hierarchy"]

    T0["T0 empirical tape"] --> D0["D0 candidate-law discovery"]
    P0["P0 discovery grammar"] --> D0
    P1["P1 complexity/tie protocol"] --> D0
    R3 --> D0
    D0 --> D1["D1 holdout/intervention/transport gates"]
    D1 --> O0["O0 calibrated readout"]
    D1 --> N0["N0 certified numerical procedure"]
    R8 --> N0
    R9 --> O0
    O0 --> C0["C0 bounded claim gate"]
    N0 --> C0
    R10 --> C0
```

## Mandatory path labels

- **R:** root primitive or root theorem
- **P:** protocol chosen by the project, never called a law of nature
- **T:** empirical tape
- **D:** discovered domain law after independent gates
- **O:** calibrated readout
- **N:** numerical procedure

The forbidden shortcut is:

\[
R_0 \not\Rightarrow \text{a specific chemistry law without }T_0.
\]
