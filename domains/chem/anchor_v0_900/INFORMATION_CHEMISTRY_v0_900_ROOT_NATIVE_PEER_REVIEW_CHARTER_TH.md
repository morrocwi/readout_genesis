# Information Chemistry v0.900
## Root-Native Peer-Review Charter and Curriculum DAG

**Status:** preregistration draft  
**Purpose:** define the only acceptable path from the retained-difference root to chemistry computation, and specify repeated peer-review gates from secondary-school chemistry through doctoral-level research.

---

## 1. Non-negotiable interpretation of “from the root”

The project must not claim that particular empirical chemistry laws follow from retained difference alone.

The admissible architecture is:

\[
\text{Root constraints}
+
\text{typed empirical tape}
+
\text{preregistered discovery procedure}
\rightarrow
\text{candidate domain law}
\]

A law can enter the active canon only as one of:

1. **ROOT_THEOREM** — formally derived from the project root;
2. **DISCOVERED_DOMAIN_LAW** — discovered from independent empirical tape and passed holdout/intervention tests;
3. **CALIBRATED_READOUT** — a validated map from retained/domain state to a named observable;
4. **NUMERICAL_PROCEDURE** — a computational method with no claim of being a law of nature;
5. **UNRESOLVED** — insufficient evidence or non-unique model;
6. **OBSTRUCTED** — contradiction, missing state, failed units, failed rank, or failed provenance.

No equation may be labelled simply “derived” without one of these types.

---

## 2. Repeated peer-review loop

Every module must pass the following loop:

### Step A — Root trace
List every symbol, transformation, ordering, aggregation, metric, and constraint.

For each item provide:
- parent nodes in the root DAG;
- proof or discovery receipt;
- empirical inputs;
- hidden assumptions;
- units and resolution;
- permitted claim.

### Step B — Imported-law adversary
A Checker searches for:
- textbook equations embedded in code;
- named scientific laws in active kernels;
- silent default constants;
- hand-written conservation rows;
- target-derived feature choices;
- fixed transforms such as logarithm, Euclidean norm, affine fit, or arithmetic mean that were not preregistered as candidate grammars.

### Step C — Model-nonuniqueness adversary
Construct competing models that fit the same train tape.

The module passes only if:
- holdout/intervention data separate them; or
- the result is labelled UNRESOLVED.

### Step D — State-sufficiency adversary
Search for pairs of states that are equal in the proposed quotient but yield different future transitions or readouts.

If found:
- refine the quotient;
- add a hidden/context coordinate; or
- label the module OBSTRUCTED/UNRESOLVED.

### Step E — Numerical adversary
Check:
- rank;
- conditioning;
- interval bounds;
- all-root completeness where claimed;
- sensitivity to resolution;
- deterministic regeneration;
- independent implementation.

### Step F — Curriculum challenge
Solve preregistered problems at the target educational level without reading answer keys.

### Step G — Claim audit
The final claim must be weaker than or equal to the evidence.

Any failure returns the module to design. Historical artifacts are retained and never overwritten.

---

## 3. Peer-review result for the current DAG

**Decision: MAJOR REVISION**

### Accepted root branches

The following branches are plausible root theorems once written formally:

\[
A\nu=0
\]

from retained ledgers in a closed boundary;

\[
n'-n^{(0)}\in\ker A
\]

and, for a selected basis \(N\),

\[
n'=n^{(0)}+N\xi;
\]

positivity/capacity constraints;

typed identity, lineage, provenance, quotient refinement, and three-valued admissibility.

### Branches not yet root-derived

1. **Composition quotient**  
   Counting components assumes a commutative composition operation. Permutation invariance and decomposition uniqueness still require gates.

2. **Additive readout**  
   Additivity does not follow from retention alone. It requires a demonstrated monoid homomorphism or discovery from composition tape.

3. **Quantity ratio \(n/V\)**  
   The ratio is a readout choice. Scale invariance and operational calibration must be demonstrated.

4. **Candidate grammar**  
   Linear, polynomial, rational, logarithmic, and monotone families are imported mathematical hypothesis classes. They may be permitted as preregistered search languages, but cannot be called root theorems.

5. **Complexity minimization**  
   The complexity measure and tie-breaking rule are protocol choices. They require an invariance/refinement justification and sensitivity audit.

6. **Equilibrium as fixed point**  
   A fixed point is a root-native stationarity concept, but not automatically chemical or thermodynamic equilibrium. Stability, recurrence, hidden currents, boundary flux, and resolution must be checked.

7. **Effective coordinates/activity**  
   A coordinate that compresses data is not automatically physically meaningful. Intervention and cross-context transport tests are required.

8. **pH semantics**  
   A discovered logarithmic sensor map may reproduce a report scale, but the label “pH” requires instrument and reference-state calibration.

9. **Root completeness**  
   Finite multi-start does not prove all roots were found.

10. **Empirical independence**  
    Simulated tape generated by a legacy equation can test software recovery only, not scientific discovery.

---

## 4. Required corrections before implementation

### Gate 0 — Root/Protocol separation

Create separate registries:

- `ROOT_THEOREM_REGISTRY`
- `DISCOVERY_GRAMMAR_REGISTRY`
- `EMPIRICAL_TAPE_REGISTRY`
- `READOUT_REGISTRY`
- `NUMERICAL_METHOD_REGISTRY`

No object may appear in more than one registry without an explicit bridge receipt.

### Gate 1 — Constructive quotient discovery

A chemistry quotient \(q_{\rm chem}\) must include:

\[
\epsilon_{\rm dyn}
=
d(q(F(S)),F^\#(q(S)))
\]

\[
\epsilon_{\rm read}
=
d(O(S),O^\#(q(S)))
\]

and counterexample-driven refinement.

### Gate 2 — Composition theorem

Before formula parsing is treated as physical composition, demonstrate:

- identity element;
- closure;
- associativity at the chosen resolution;
- admitted commutativity;
- decomposition stability;
- lineage preservation.

### Gate 3 — Conserved-ledger discovery

Permit two routes:

1. ledger supplied as a typed problem statement;
2. ledger basis discovered from transition tape.

Never infer reaction occurrence from a nullspace direction alone.

### Gate 4 — Readout homomorphism

A readout \(R\) is additive only after testing:

\[
R(x\oplus y)=R(x)+R(y)
\]

across train, holdout, and intervention panels.

### Gate 5 — Stationarity hierarchy

Distinguish:

- observational stationarity;
- quotient fixed point;
- stable fixed point;
- zero resolved current;
- detailed-balance-like symmetry if discovered;
- thermodynamic equilibrium only after calibrated thermodynamic readouts.

### Gate 6 — Model discovery honesty

Every discovered law must report:
- search language;
- excluded languages;
- complexity metric;
- equivalent models;
- identifiability;
- extrapolation domain.

### Gate 7 — Root certification

A solver may claim a unique physical answer only with:
- interval enclosure, algebraic certificate, monotonicity theorem, or exhaustive finite proof;
- full-rank or appropriate singular-manifold certificate;
- boundary and unit admissibility.

---

## 5. Curriculum DAG

### Tier S — Secondary school

#### S1 Matter and formula representation
- typed species identity;
- composition vectors;
- isotopes as tape;
- formula parsing;
- formula isomer warning.

#### S2 Quantitative chemistry
- molar-mass readout;
- amount/mass inverse decoder;
- exact equation balancing;
- mole ratios;
- limiting boundary;
- theoretical yield;
- percentage yield as report.

#### S3 Solutions
- amount and volume readouts;
- concentration as calibrated ratio;
- mixing under explicitly tested additive-volume context;
- dilution as retained-solute intervention.

#### S4 Acid/base and equilibrium
- discovered stationary constraints;
- calibrated hydrogen-coordinate readout;
- buffers as intervention robustness;
- titration as a sequence of state interventions.

#### S5 Gas and energy modules
These must not use imported gas or thermochemical laws.
They require separate real tapes and domain-law discovery.

**Secondary-school completion gate:**  
Solve a frozen benchmark covering all supported topics, while explicitly returning UNRESOLVED for unsupported laws.

---

### Tier U — Undergraduate

#### U1 General chemistry
- multireaction stoichiometry;
- multiprotic and coupled equilibrium;
- precipitation and phase appearance;
- electrochemical readouts;
- nonideal solution coordinates;
- temperature/context transport.

#### U2 Physical chemistry
- discovered state equations;
- kinetic-law discovery from time tapes;
- stationary vs equilibrium separation;
- energy/entropy/free-energy readouts only after calibration;
- spectroscopy as translation discovery.

#### U3 Organic chemistry
- typed molecular graphs;
- constitutional/stereo identity;
- reaction-family discovery;
- mechanism candidates as hidden-state models;
- product-distribution prediction with uncertainty.

#### U4 Analytical chemistry
- measurement models;
- calibration;
- detection limits;
- uncertainty propagation;
- inverse problems;
- instrument cross-validation.

#### U5 Inorganic/material chemistry
- coordination/state graphs;
- phase and lattice descriptors;
- redox and electronic-state readouts;
- structure-property discovery.

**Undergraduate completion gate:**  
Held-out multi-domain benchmark, real datasets, method-separated Checker, and explicit failure map.

---

### Tier M — Master’s level

- hierarchical/multiscale state representations;
- model selection under non-identifiability;
- Bayesian or alternative evidence update labelled as inference protocol;
- experimental design chosen to separate competing laws;
- causal intervention and transportability;
- uncertainty decomposition;
- domain adaptation;
- mechanistic latent-state discovery;
- reproducible preregistered research workflow.

**Master’s completion gate:**  
The system must design an informative experiment, predict outcomes before opening them, and update or reject its law set without repairing failed predictions.

---

### Tier D — Doctoral level

- open-domain law discovery;
- theorem/certificate generation;
- autonomous counterexample search;
- cross-scale commuting diagrams;
- emergent-domain validation;
- novel observable proposal;
- external laboratory collaboration;
- independent replication;
- publication-grade provenance;
- comparison against state-of-the-art domain models;
- explicit theorem, empirical law, calibrated readout, and conjecture separation.

**Doctoral completion is not “knows all chemistry.”**  
It means the architecture can make and survive a novel, independently replicated chemical claim.

---

## 6. Release sequence

| Release | Scope | Required decision |
|---|---|---|
| v0.900 | Root-law charter, DAG, registries, audit schemas | no scientific claim |
| v0.901 | Formal root theorem proofs and proof checker | ROOT_THEOREM only |
| v0.910 | Constructive composition quotient | pass commuting/refinement gates |
| v0.920 | Ledger/kernel quantitative core | secondary stoichiometry |
| v0.930 | Readout homomorphism and units | molar mass, amount, concentration |
| v0.940 | Generic state/constraint discovery | synthetic software validation only |
| v0.950 | Real-tape equilibrium discovery | secondary acid/base |
| v0.960 | Intervention sequence engine | buffer/titration |
| v0.970 | Secondary-school benchmark release | complete supported secondary tier |
| v0.980 | Undergraduate modules | domain-separated releases |
| v0.990 | Master’s research engine | experiment design and model revision |
| v1.000 | Doctoral validation milestone | novel external replicated result |

Version numbers represent evidence milestones, not marketing completeness.

---

## 7. Stop rules

The review loop must stop or return UNRESOLVED when:

- a supposed root theorem needs an empirical fact;
- multiple laws remain observationally equivalent;
- the state quotient is insufficient;
- the result depends materially on an unregistered grammar;
- a root is not certified;
- a readout lacks calibration;
- the tape is simulated but the claim is empirical;
- the same operator controls Maker and hidden target;
- a doctoral-level claim lacks external replication.

---

## 8. Immediate next artifact

Before implementing chemistry, v0.901 must formalize and attempt to prove only these propositions:

1. retained-ledger conservation under a declared closed boundary;
2. kernel characterization of admissible ledger-preserving changes;
3. extent coordinates from a chosen kernel basis;
4. positivity/capacity admissible region;
5. quotient-refinement theorem;
6. conditions under which additive readouts are justified;
7. conditions under which a fixed point is only observational stationarity.

Any proposition that cannot be proven from the root must be downgraded to a protocol or discovery target.
