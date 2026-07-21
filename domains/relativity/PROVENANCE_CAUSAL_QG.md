<!-- Verified upgrades pulled from the causal-quantum-gravity Coq corpus (best-version audit). -->

# Provenance — causal-quantum-gravity Coq upgrades (2026-07-21)

The founder's derivation gave this domain its *finite internal closure* witnesses (exact-rational,
`relativity_closure_v0_*.py`). Several nodes have a **stronger, machine-checked** backing already in
the sibling repo `causal-quantum-gravity/` (public curated export, `make verify` CI-green, PR #31 —
81 formal files). Those are folded in here as **tier upgrades** — but only after each cited `.v` was
**re-verified locally** (compiled with `coqc -q -R . DQG`, and grep-clean of `Admitted`/`admit`/
`Axiom`/`Parameter`). Nothing is tagged `Th_coqc` on the strength of a filename or a claimed tag.

**Status taxonomy** (per founder, 2026-07-21):
`green` = Coq/formal closed · `yellow` = theorem closed but the *physical/semantic* bridge is partial
(FORMAL-CLOSED / BRIDGE-PARTIAL) · `red` = open · `gray` = measured/calibration adapter.

## Verified GREEN (compiled clean + axiom-grep clean here, 2026-07-21) — usable as `Th_coqc`

| relativity node | causal-quantum-gravity file | key theorem(s) | what it earns |
|---|---|---|---|
| operator→metric (OB-01) | `formal/RDL_MetricReadout.v` | `metric_form_readout` | already `Th_coqc` (core Face 8) — confirmed, one of the 2/8 cards that survived the hollow-card audit |
| operator→metric BROADENING (OB-01) | `formal/InfoMetricIsEnergyReadout.v` | metric-Hessian readout = mother-equation energy form | **green broadening**: closes the named "isolated islands" gap (`RDL_GammaSpectral.energy` ↔ `RDL_MetricReadout.qform`) — axiom-free, root-native (weighted-graph Dirichlet form + `L_R` Hessian only) |
| discrete connection (OB-03) | `formal/InfoConnectionFromFrame_attempt.v` | `coboundary_telescopes`, `closed_loop_pure_gauge_flat`, `genuine_curvature_is_non_coboundary` | **FD → `Th_coqc`**: connection from a frame field, pure-gauge-is-flat, genuine non-coboundary curvature — no continuum/manifold import |
| curvature certificate (OB-04) | `formal/InfoDiscreteRiemannCurvature_attempt.v` | `riemann_is_second_difference`, `curvature_nonzero_witness` | **FD → `Th_coqc`**: discrete Riemann = second finite difference, with a nonzero witness |
| curvature chain (OB-04 extended) | `InfoMetricCompatibleCurvature_attempt.v`, `InfoDiscreteSecondBianchi_attempt.v`, `InfoDiscreteGaussBonnet_attempt.v`, `InfoRiemannPairSymmetry_attempt.v`, `InfoRationalSO3Curvature_attempt.v` | metric-compatible curvature, 2nd Bianchi, Gauss–Bonnet, Riemann pair symmetry, rational SO(3) curvature | **green** supporting theorems for the discrete geometry chain |
| causal cone (OA-01/02) | `formal/InfoConeInheritance.v` | `shift_blind_step`, `step_domain_of_dependence`, `step_path_local_stencil` | strengthening (already ROOT_BACKBONE): axiom-free one-step domain-of-dependence, arbitrary edges/coefficients |
| Lorentzian signature FOUNDATION under RD-neutrality (OA-06) | `formal/InfoLorentz.v` | signature-from-causal-order (`≺`) | **green** for the *signature foundation only*. Does NOT upgrade `Γ_R`/the transforms (OA-07…OA-12) — those stay `[Proposed internal bridge]`. |
| geometry back-reaction joint (GD-01/GD-03) | `formal/InfoBackReaction.v` | `edge_strain_expansion_exact`, `budget_consumed_exact`, `retention_shift_iff` | **green, PARTIAL** — closes ONE joint of the feedback (strain/edge budget), root-native, no stress-energy import; does not close the full metric–source law |
| spine crossover discriminant (NOT node-8 lapse/redshift) | `formal/InfoTelegraphHorizonUnification_attempt.v`, `formal/InfoTelegraphCrossover_attempt.v` | `disc_is_spine_discr`, `lam_c_is_spine_lambda_c`, `quantum_iff_above_horizon` | **green**, but proves a **DISTINCT** object: the spine's OWN classical/quantum crossover discriminant `λ_c=D²/4MK`. It does **NOT** cover node-8's lapse `N=√detB` / redshift `ν_o=Nν_i` — do not relabel it as closing the observer-normalization/horizon node. (Belongs more to the quantum oscillatory-split node.) |

Also verified green and relevant to the sibling **quantum** domain (recorded here for cross-use):
`InfoRetainedDistinctionForcesLaplacian_attempt.v` (retained-distinction axioms **force** the `L_R`
form — not merely posit it), `InfoAsymmetricSeedTrifurcation.v` (`R_0 = DiagPart + SymOff + SkewOff`),
`InfoSeedTorsionIsSkewOff.v` / `InfoSeedTorsionGroupAndRankN.v` / `InfoSeedTorsionGenuineMixing.v`
(torsion/circulation branch), `InfoMemoryBeforeMass.v` (retained memory → inertial/mass readout,
discrete algebra). **CAVEAT on the QM/SR "unification":** `InfoQuantumRelativityUnification.v`
(`box_quad_is_spine_residual`, `spine_dispersion_iff_box_quad_vanishes`) compiles axiom-free, but its
`box_quad` **inherits the imported Minkowski signature** from `InfoLorentzInvariance.box_quad` — so it
is a **bounded ALGEBRAIC identity between two independently-posited constructions**, NOT a root-native
derivation of QM/SR. The repo's own `completeness-and-claims.md` states this verbatim. Cite it (and
`InfoSeedFeedsQuantumRelativity_attempt.v`) only as an algebraic identity — never as "QM and SR
derived from one root."

**Tier footnote:** two files here are `+reals` (Coq's standard-library Reals axioms
`sig_forall_dec` + `functional_extensionality_dep`, disclosed by the repo, NOT a hidden import):
`InfoLorentzContinuum.v` and `InfoQuantumGravityRootBridge.v`. `+reals` is honestly weaker than
axiom-free `Th_coqc`; neither is pulled in here.

## REFUSED — checked and NOT pulled in (would repeat the hollow-card mistake)

| file | why refused |
|---|---|
| `formal/InfoLorentzInvariance.v` and `URCF_RD_All.v` module `InfoGR2.GW` | Compiles `Th_coqc`/axiom-free, **but** imports the Minkowski `interval` and the boost constraint `γ²(1−v²)=1` as `Definition`s/hypotheses — **NOT forced by the graph root**. The repo's own `supplement/completeness-and-claims.md` (L28-32) says "POSITED, not forced by the graph root." Pulling it in as "derives `Γ_R`" would be exactly the secret-import hollow card the founder warned against. `Γ_R` therefore stays `[Proposed internal bridge]`. |
| `formal/InfoAnalysisLift.v` | Imports the Schwarzschild metric as a `Definition`, not derived — consistent with Schwarzschild staying `[DeclaredFormula]`. |
| `formal/InfoQuantumGravityRootBridge_attempt.v` | Imports the GR field-equation conclusion (`[Dr]`/import), not root-derived. Not usable as a root-native upgrade. |

## Discipline note

Every upgrade above is `green` = the **algebraic/structural** claim is machine-checked and root-native.
None of them promotes the domain past `FINITE_INTERNAL_CLOSURE`: the `yellow` (physical bridge) and
`red` (open) statuses of Born-less measurement, real `c`, real surface gravity, real stress-energy,
full nonlinear GR and QFT are unchanged. Machine-checked structure ≠ real physics.
