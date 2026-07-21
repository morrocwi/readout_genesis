# Root DAG Master — Relativity v0.2

**Standalone rule:** this file contains the complete DAG for the relativity domain, not a pointer
elsewhere. Every node below corresponds to a `rule_id` in `RULE_REGISTRY.json`. Root `P0`
(`a != b`) is the master retained distinction; nothing here is a new axiom — this DAG is a readout
of `source_root/READOUT_GENESIS_CORE_SNAPSHOT.md`.

Tier legend: `[RB]` ROOT_BACKBONE · `[RT]` ROOT_THEOREM · `[FD]` FINITE_DIAGNOSTIC ·
`[PIG]` PROPOSED_INTERNAL_GATE · `[PIB]` PROPOSED_INTERNAL_BRIDGE · `[DF]` DECLARED_FORMULA ·
`[OPEN]` unresolved bottleneck.

**v0.2 note:** OB-07 and OC-05, shown `[OPEN]` in v0.1, are now `[closed]` via two new internal
gates — `GC-*` (Null-Transport Factorization Gate, `[PIG]`/`[FD]`) and `GD-*` (Geometry
Stationarity Gate, `[FD]`) — added below as new DAG nodes, each with its own `rule_id` in
`RULE_REGISTRY.json`. Both gates are FINITE INTERNAL CLOSURE (algebraic), never `[Th_coqc]` and
never real physics.

```mermaid
flowchart TD
    RB_P0["RB-P0 a!=b distinguishability/asymmetry [RB]"] --> RB_P1["RB-P1 ordered transitions, retention tau_c>0 [RB]"]
    RB_P1 --> RB_P2["RB-P2 discrete ticks, finite causal graph/operator L_R, MQ.08 stepper [RB]"]
    RB_P2 --> RB_P3["RB-P3 telegraph coarse-grain, finite front speed v=sqrt(D/tau_c) [RB]"]
    RB_P3 --> RB_P4["RB-P4 finite causal cone |x|<=v*t [RB]"]

    %% ---- Observer-Cone arm (group A) ----
    RB_P4 --> OA01["OA-01 null coords n_+=v*t+x, n_-=v*t-x [FD]"]
    OA01 --> OA02["OA-02 cone product Q_v=n_+ n_- [FD]"]
    RB_P4 --> OA03["OA-03 O1 path-additivity gate => linearity [FD]"]
    OA03 --> OA04["OA-04 O2 cone-preservation gate [FD]"]
    OA04 --> OA05["OA-05 O3 orientation gate [FD]"]
    OA02 --> OA06["OA-06 O4 RD-neutrality gate [PIG]"]
    OA05 --> OA06
    OA06 --> OA07["OA-07 forced kappa null rescaling [PIB]"]
    OA07 --> OA08["OA-08 Gamma_R=(kappa+1/kappa)/2 [PIB]"]
    OA08 --> OA09["OA-09 observer transforms x',t' [PIB]"]
    OA09 --> OA10["OA-10 time dilation / length contraction [PIB]"]
    OA09 --> OA11["OA-11 relative simultaneity [PIB]"]
    OA09 --> OA12["OA-12 velocity composition [PIB]"]

    %% ---- Living-Geometry arm (group B) ----
    RB_P2 --> OB01["OB-01 operator->metric g~=1/2 Hess sigma_LR [RT / Th_coqc base, Face 8]"]
    OB01 --> OB02["OB-02 finite-basis covariance + minimal closed state Z_n [FD, PARTIAL]"]
    OB02 --> OB03["OB-03 discrete connection U_j<-i=V_j^-1 V_i [FD]"]
    OB03 --> OB04["OB-04 curvature certificate K_C=U_C-I!=0 [FD]"]
    OB03 --> OB05["OB-05 free-path obstruction minimizer [FD]"]
    OB01 --> OB06["OB-06 geometry-field feedback commuting square [FD]"]
    OB02 --> OB06
    OB03 --> OB06
    OA08 --> OB07["OB-07 observer-normalization/redshift/lapse quotient [PIG, CLOSED v0.2]"]
    OB01 --> OB07

    %% ---- Boundary / BH / QG arm (group C) ----
    RB_P3 --> OC01["OC-01 graph front-speed vs measured-speed [DF]"]
    RB_P1 --> OC02["OC-02 mass-memory declared correspondence [DF]"]
    OC02 --> OC03["OC-03 Schwarzschild r_s=2GE/c^4 [DF]"]
    RB_P1 --> OC04["OC-04 Unruh tau_c=pi c/a [DF]"]
    OC03 --> OC05["OC-05 horizon bridge + dynamic metric-source closure [FD, CLOSED v0.2]"]
    OC04 --> OC05
    OB06 --> OC05

    %% ---- Gate C: Null-Transport Factorization Gate (v0.2, observer side) ----
    OA09 --> GC01["GC-01 null coords -> B=N*diag(chi^-1,chi), lapse N=sqrt(det B) [PIG]"]
    GC01 --> GC02["GC-02 redshift nu_o=N nu_i, dtheta_o=dtheta_i/N [FD]"]
    GC01 --> GC03["GC-03 composition N_j|o=N_j|i*N_i|o, loop holonomy H_N(C) [FD]"]
    GC01 --> GC04["GC-04 horizon N=0 <=> det B=0 (finite rank-loss boundary) [PIG]"]
    GC01 --> GC05["GC-05 Unruh-fix kappa_R=Normalize_N(a_local) [DF]"]
    OC04 --> GC05
    GC02 --> OB07
    GC04 --> OC05
    GC05 --> OC05

    %% ---- Gate D: Geometry Stationarity Gate (v0.2, geometry side) ----
    OB01 --> GD01["GD-01 geometry source S_Theta=Phi^T G_a Psi [FD]"]
    OB02 --> GD01
    GD01 --> GD02["GD-02 stationarity law + explicit Theta_{n+1} stepper [FD]"]
    GD02 --> GD03["GD-03 minimal closed state Z_n + commuting square [FD]"]
    OB02 --> GD03
    GD02 --> GD04["GD-04 fail rules: PIVOT/ADMISSIBILITY/NULL_MIXING/HORIZON_BOUNDARY [FD]"]
    GC04 --> GD04
    GD02 --> OC05
    GD03 --> OC05
```

## Post-closure summary DAG (audit view)

The 24-node **Minimal Relativity DAG** used for the closure audit (`CLOSURE_AUDIT.json`) is the
coarser grouping of the graph above into three arms sharing the root cone/operator:

```mermaid
flowchart TD
    ROOT["P0..P4 root backbone (a!=b -> cone)"] --> GA["Group A: Observer/Kinematics — 12/12 closed"]
    ROOT --> GB["Group B: Living-Geometry/GR — 6/7 closed"]
    ROOT --> GCg["Group C: Boundary/BH/QG — 1/5 strict closed"]
    GA -. RD-neutrality gate OA-06 shared cone/operator .-> GB
    GA -. Null-Transport Factorization Gate GC-01 .-> GB
    GB --> OB07b["observer-normalization/redshift — CLOSED v0.2 (GC-01/GC-02)"]
    GCg --> OC05b["horizon bridge / metric-source closure — CLOSED v0.2 (GC-04/GC-05 + GD-01..GD-04)"]
```

v0.2 lift on this DAG: strict `17/24=70.8% -> 19/24=79.2%`, weighted `19.5/24=81.25% -> 21.5/24=89.6%`.
The five nodes still `partial` (OB-02, OC-01, OC-02, OC-03, OC-04) are exactly the real-physics
calibration gaps — see `CLOSURE_AUDIT.json` → `remaining_bottlenecks_for_real_physics_tier`.

## Non-drift rule

The cone product `Q_v` and every downstream observer-cone node are composed **only** from the root's
own two null edges (`n_+`, `n_-`); no Minkowski interval, Lorentz transformation, or any other named
relativity/geometry law is imported as a premise anywhere in this graph. The one exception admitted
into `[Th_coqc]` is the single operator-to-metric direction of `OB-01`, inherited verbatim from the
master core's Face 8 — the reverse direction (spectrum alone determining the metric) stays forbidden.

The `GC-*` and `GD-*` nodes added in v0.2 are built the same way: `GC-01`'s lapse `N=sqrt(det B)` is
composed only from the diagonal observer map's own determinant (no named lapse function imported);
`GD-01`'s geometry source `S_Theta=Phi^T G_a Psi` is composed only from the root's own reader/record
fields and the geometry operator's own `Theta`-derivative (no named stress-energy tensor imported).
No new node in this file is tagged `[Th_coqc]`; the only `[Th_coqc]` node in the whole DAG remains
`OB-01`'s forward direction.
