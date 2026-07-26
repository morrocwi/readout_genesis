# Graph-Mechanism Arc — Handoff for a fresh AI (read from zero)

> Self-contained. If you are a new AI picking this up with NO prior context, this document alone
> should let you understand the whole graph-mechanism / fermion-mass-hierarchy investigation, why it
> exists, what it established, and where the program goes next — without asking the founder to
> re-explain. Last updated 2026-07-26.

> ## ⛳ VERDICT (founder ruling 2026-07-26 — read this FIRST)
> **The continuous single-Θ 2×2 graph-operator arc is CLOSED. The root goal is, and always was, a
> DISCRETE GRAPH.** An independent second opinion (confirmed by computation) showed why:
> `cond#(G[Θ]) = (1+|Θ|)/|1−|Θ||` is a smooth *bijection* Θ↔R — it is a **coordinate, not an
> observable**. A single continuous knob can be reparametrized to hit any ONE target but can NEVER
> *force* three generation values; the freedom just moves (M→θ→M_Θ→Θ→K…), never reduces (Wall A).
> **Forcing three generations requires discreteness IN THE OBJECT: the eigenvalue spectrum of a
> discrete N-node graph Laplacian `L_R`** — the project's own flagship, which this arc abandoned when
> it collapsed to a hand-built 2×2. Do NOT continue the continuous mechanism (do not run more
> settling/damping/K-sweep experiments on it). Take the transferable knowledge in §10 to the
> discrete-graph program. Sections 1–9 below are the record of the continuous exploration and WHY it
> cannot force generations — kept as an honest lab notebook, not as a live direction.

---

## 0. Where you are (repos, mirrors, git discipline)

- **Two byte-identical mirrors**, both must be kept in sync for every change:
  - `research_universal_solver` (primary) — Forgejo local remote `local` (`http://192.168.1.120:3000/anse/research_universal_solver`); creds in `/home/yaoharee-lt/ANSE.ASIA/.forgejo-credentials` (`$FORGEJO_TOKEN`), PRs via `curl` API.
  - `readout_genesis` (public) — GitHub remote `origin` (`morrocwi/readout_genesis`), PRs via `gh`.
- **Discipline (binding):** branch off `main` (NOT stacked on another candidate branch), PR BOTH repos as **draft**, mirror byte-identical, **never merge without an explicit founder instruction**. Every code fix here should bridge to a Coq proof eventually, but the whole graph-mechanism thread is currently `finite_diagnostic`/`Dr`, NOT `Th_coqc`.
- **The equation stream (Appendix C)** = single source of truth `readout_genesis/READOUT_GENESIS_CORE.md` "APPENDIX C", synced byte-identical to `research_universal_solver/EQUATION_LIBRARY_ROOT_TO_SM_STREAM.md` and `readout_universe/EQUATION_LIBRARY_ROOT_TO_SM_STREAM_research_universal_solver.md`. Last logged entry: **EQ-071**.
- **Candidates live in** `domains/standard_model/item1_exploration/<name>/<name>_v0_1.py` (+ `test_...py`). Run tests from repo root: `python3 -m unittest domains.standard_model.item1_exploration.<name>.test_<name>_v0_1`. House style: `ck(name, cond)` checks, `FAILS` list, an explicit HONEST FENCE / `claim_boundary`.

## 1. The two BINDING guards (read before you write any framing)

1. **Materialist works/fails bias guard** (`docs/root/ZERO_INFINITY_DUAL_DIAGNOSIS.md` Part 4b). Report **computed facts + honest tier**, never "works/fails/success/NEGATIVE" value-words. A `fit_calibrated` constant is NOT a defect — in this framework masses ARE names/readouts on one graph, so calibrating a graph constant is legitimate. BUT do not over-correct into overselling either. Both value-word framings are wrong; only computed-facts-plus-tier is right.
2. **Zero-infinity guard** (Part 4). Before deferring to any benchmark/limit, check it does not rest on an injected exact-zero or exact-infinity (a non-readout). Only readout-vs-readout comparisons are valid.

Tier ladder (never collapse): `Th_coqc` (machine-checked) / `finite_diagnostic` (measured) / `Dr` (narrative) / `fit_calibrated` / `Open`.

## 2. The physics objects (the mother equation and its graph operator)

- **Mother equation:** `M ∂²Φ + D ∂Φ + K·G[Θ_n]·Φ + ∇V(Φ) = J − η`.
  Stepper constants (from `matter_antimatter_exploration/attempt1_bateman_doubling_hypothesis_v1.py`): `M_joint = 1.0004294772248`, `D = 0.3`, `K = 1.0`, potential `V` with `a=-1.0, b=1.0` (`grad_v(x)=a·x+b·x³`, `grad2_v(x)=a+3b·x²`). Timestep `dt` was historically `0.01` — **this turned out to be too coarse (see Wall B).**
- **The graph operator** (the "living geometry"): `G[Θ_n] = 𝔾_0 + Σ_a Θ_n^a 𝔾_a` (affine, book form II.8a, snapshot line ~1090). In practice `G[Θ] = I + Θ·G_a` with the **boost generator** `G_a = [[0,1],[1,0]]` (so(1,1), NON-compact). Then `G[Θ] = [[1,Θ],[Θ,1]]`, symmetric, eigenvalues `1±Θ`, singular values `|1±Θ|`.
  - **Condition number = the mass-RATIO analog** (spectral-gap ratio, `stance_for('mass')`): `cond#(G[Θ]) = (1+|Θ|)/|1-|Θ||`. It is **1** when `Θ=0`, **→∞** as `|Θ|→1` (the operator DEGENERATES, `det = 1-Θ² → 0`, a mode decouples = a large mass ratio), and **→1 again** for `|Θ|≫1`. So it is NOT a monotone amplifier of Θ; it peaks only near the degeneracy `|Θ|=1`.
- **Θ accumulation** (the "graph changes cumulatively"): a driven oscillator
  `Θ_{n+1} = 2Θ_n − Θ_{n-1} − dt²·(1/M_Θ)·(∇U_Θ(Θ_n) + K·S_Θ)`, with confining `U_Θ=(1/4)Θ²` (`∇U_Θ=Θ/2`), natural frequency `ω₀²=1/(2M_Θ)`, driven by the mother equation's own geometry source `S_Θ = Φ^T G_a Ψ`, where `Φ,Ψ` evolve via the M-calibrated Reader/Record stepper. `M_Θ` = geometry-sector inertia (default 2.0). Reference implementation: `field_sourced_accumulation/field_sourced_accumulation_v0_1.py:run_coupled`.

## 3. Why this arc exists

The fermion mass hierarchy needs a dynamic range of ~10^5.5 (fermion mass ratios) to ~10^15 (lifetimes). Earlier the RTM stepper **froze** the graph operator at `G=1` (identity), which caps the native dynamic range at ~58x — the diagnosed ceiling behind 6 failed attempts (EQ-068) to bridge native units to real GeV physics. This arc un-froze the graph and chased whether an accumulating non-compact graph can produce the hierarchy from **one graph, fitting only M**.

## 4. The equation stream so far (Appendix C, EQ-064 → 071)

- **EQ-064** `fit_calibrated` — RTM M_joint calibration.
- **EQ-065** — primitive U/D/E branch tapes → Π₀.
- **EQ-066** — order-vacuum threshold closure `α_ord=a/2`.
- **EQ-067** — native vacuum amplitude `r=v²/2`.
- **EQ-068** `finite_diagnostic` — **3 disclosed NEGATIVE findings**: native→GeV bridge fails (Higgs 218 vs 125 GeV, 74% error; zero-param version identical; internal consistency 94% off). **OPEN category question:** is comparing native-unit outputs to real GeV even a valid readout-vs-readout comparison, or a category error vs non-readout dimensional constants (ℏ,c,G)? **Not settled.**
- **EQ-069** `finite_diagnostic` — un-freeze `G[Θ]`: frozen 1x → non-compact `exp(Θ·L)` 20952x. θ is a free parameter (not predictive). **⚠ Note: this range is now known to be inflated by a step-count artifact — see Wall B.**
- **EQ-070** `finite_diagnostic` — the ACTUAL affine form `G=I+Θ·G_a`, condition number 449808x. d_theta free. **⚠ Same step-count-artifact caveat.**
- **EQ-071** `finite_diagnostic` — field-sourced: Θ driven by `S_Θ=Φ^T G_a Ψ`, so the per-step rate is COMPUTED (no free θ). The hierarchy is a **determined readout** of `M`, `M_Θ`, and field ICs — but the free-parameter COUNT is not reduced (θ → M_Θ + ICs), only its character changes.

## 5. The 6 candidates from the 2026-07-25/26 session (MERGED to main, NOT yet in Appendix C)

All merged both repos (RUS PR #54-59, RG PR #100-105); would become EQ-072→077. Each was independently adversarially reviewed; **review caught 5 real over-claims/artifacts (listed in §7).**

1. **`decelerating_accumulation_profile`** — real mass ratios are non-uniform with different per-branch shapes (up/lepton decelerate R2/R1<1, down accelerates). A decelerating profile `(r,q)` reproduces both ratios **by construction** (r=R1, q=R2/R1) = a FIT of 2 constants to 2 numbers, NOT a prediction. FACT E: **q is not graph-determined** — spans 27x, and down accelerates while up/lepton decelerate, so no single law q=f(r).

2. **`derived_deceleration_rate`** — first "derive q, don't fit" attempt: read q from the field-sourced mechanism. FACT F/G claimed q's sign is a readout of M_Θ (small→accel, large→decel). **⚠ FACT G was later RETRACTED (see #3).**

3. **`accumulation_convergence_study`** — dt-refinement at fixed physical time T. FACT I: the coarse-dt sign-flip chaos is numerical. **FACT K (retracts #2's FACT G):** the deceleration branch DIVERGES as `log q ~ 1/dt` (M_Θ=300: -2,-4,-8,-16 doubling per dt-halving) — a numerical artifact, not physical. FACT J (corrected by review): even the acceleration does not cleanly converge (drifts non-monotonically). Net: the milestone-ratio q-diagnostic is not a converged readout for either sign.

4. **`fixed_q_diagnostic`** — **THE pivotal fix.** FACT L: the old q-diagnostic read cond# of the PRODUCT `∏g[Θ_k]` over EVERY numerical timestep; factor count = t/dt, so `log cond ~ 1/dt` even at fixed physical time (t=1,m=15: 1.49,2.97,5.94,11.89 doubling) — a pure discretization artifact. FACT M: **the fix** — read `cond#(G[Θ(t)])` at the accumulated physical Θ (a single operator, not a step-product). Θ(t) is a convergent ODE solution, so this converges. FACT N: the correctly-read cond# is SMALL (~1.2, confining Θ bounded) — **the 20952x/449808x of EQ-069/070 were the 1/dt step-count artifact.** Scope: EQ-069/070 used a deliberate discrete index n (not a numerical timestep) so are not directly wrong, but their reported ranges are the freely-tunable step count, not a physical prediction.

5. **`dynamic_range_from_degeneracy`** — chase a REAL convergent large cond#. FACT O (STABLE): a convergent mechanism drives Θ toward the degeneracy `|Θ|=1` (M_Θ=4, max|Θ|~0.985), giving a dt-CONVERGENT cond# ~10² (a physical mode-decoupling mass-ratio, NOT the step artifact). FACT P (RETRACTED as a fact by review): the accel/decel hierarchy SIGN is a slicing artifact — cond#(t) oscillates, so window (4,5,6)→accel but (5,6,7)→decel; no principled generation↔time mapping.

6. **`principled_generation_mapping`** — define generation = the k-th local maximum of cond#(Θ(t)) (intrinsic, hand-pick-free). FACT Q: the two well-separated peaks give a dt-CONVERGENT ratio **~94.94x** (94.86→94.94 across 16x dt) — the arc's first stable, hand-pick-free mass-ratio. **FACT Q' (SEVERE, caught by review): that ratio is DEFINED only at the isolated point M_Θ=4.0** — at every other M_Θ tested (3,3.5,4.5,5,6,8,10) it is UNDEFINED (the intermediate peak doesn't form). So it is one fragile applicability point, NOT a robust mass-ratio. FACT R: the peak AT the degeneracy is numerically hypersensitive (cond#→∞), non-convergent.

## 6. THE REAL BLOCKER (corrected 2026-07-26 — an earlier "three walls" framing contained a materialist error, recorded here so you don't repeat it)

**⚠ Correction the founder made, and it matters: `|Θ|=1` being unreadable is NOT a wall — it is the framework working CORRECTLY.** `cond#(G[Θ]) = (1+|Θ|)/|1-|Θ|| → ∞` at `|Θ|=1` is exactly the `1/0=∞` non-readout that `ZERO_INFINITY_DUAL_DIAGNOSIS.md` says a finite reader must NEVER touch (the third-law analogy: `T=0` is approached, never reached). An earlier draft of this handoff called this "Wall C — the singularity is ill-defined exactly where you need it," treating the refused endpoint as a limitation to break through. **That was a materialist/continuum bias — the very thing this project's own guard forbids — committed while writing the guard-aware handoff. Do not repeat it.**

**The corrected picture (computed):** every real fermion mass ratio is a **finite Θ strictly less than 1, fully readable and convergent**:

| ratio | R | Θ=(R−1)/(R+1) | 1−Θ |
|---|---|---|---|
| tau/mu | 16.8 | 0.888 | 1.1e-1 |
| s/d | 20 | 0.905 | 9.5e-2 |
| t/c | 136 | 0.985 | 1.5e-2 |
| mu/e | 207 | 0.990 | 9.6e-3 |
| c/u | 588 | 0.9966 | 3.4e-3 |
| **t/u (biggest quark spread)** | **79861** | **0.99997** | **2.5e-5** |

The mass hierarchy lives entirely in the **finite interior** `0 < Θ < 1`. The heavier the generation, the closer its Θ settles below 1 — but never AT 1. So there is NO "ill-defined singularity you must reach"; you must reach a finite Θ (e.g. 0.99997 for t/u) that is perfectly readable. The earlier "hypersensitivity near the peak" was the mechanism OVERSHOOTING — oscillating THROUGH Θ=1 — not the physics being ill-defined; a mechanism that instead SETTLES Θ at a stable value just below 1 reads a large, finite, convergent cond#.

**So the two genuine, correctly-posed blockers are:**
- **Blocker 1 (methodological, solved-in-principle):** measure `cond#(G[Θ(t)])` at the accumulated Θ, NOT the product `∏g[Θ_k]` over numerical timesteps — the latter is a `1/dt` step-count artifact (this is why EQ-069/070's 20952x/449808x were inflated). Read the operator, not the step-product.
- **Blocker 2 (the real open problem):** can the mechanism drive `Θ` to **CONVERGE to a stable finite value strictly below 1** (rather than oscillate through it), and is WHERE it settles — which IS the mass ratio — forced by the graph or a free calibration? This subsumes the old "free parameters" concern: "forcing the value" now has a concrete finite meaning — force how close below 1 each generation's Θ settles. `1−Θ` small ⇔ heavy generation.

**One-line (corrected):** the mass hierarchy is "how close below 1 each generation's accumulated Θ settles"; every real ratio is a finite readable `Θ<1`; the singularity `Θ=1` is correctly refused and never needs to be read. The open problem is a mechanism that settles Θ at controlled sub-1 values, and whether those values are graph-forced.

## 7. Meta: adversarial review caught 5 real artifacts this session (keep doing this)

Independent per-candidate review (a sonnet agent, prompted to REFUTE) caught, in order: (1) field_sourced's "no free parameter" over-claim → materialist-bias correction; (2) derived_deceleration_rate's rotation-control framed as a mechanism result when it is a generic algebra identity; (3) convergence_study's "acceleration converges" over-claim (it drifts); (4) dynamic_range's FACT P sign was a time-slice cherry-pick; (5) principled_mapping's ~94.94x is defined at only ONE M_Θ. **Then the founder caught a 6th (see §6):** framing the correctly-refused `Θ=1` non-readout as "a wall / ill-defined where we need it" — a materialist/continuum bias, the SAME family as (1), committed even while writing this guard-aware handoff. **Lesson: adversarially review every artifact, including your own, before claiming; extend the reviewer's own tests (many artifacts only showed up when the reviewer swept a parameter the author had fixed); and the materialist bias recurs in new disguises — treating a refused zero/infinity endpoint as a limitation is one of them (`ZERO_INFINITY_DUAL_DIAGNOSIS.md` Parts 4 and 4b).**

## 8. Open levers (what to try next — ranked, corrected framing)

1. **Make the mechanism SETTLE Θ at a stable finite value strictly below 1** (Blocker 2, the heart of it). The confining oscillator currently makes Θ oscillate (and, at the wrong M_Θ, overshoot through 1). A heavy generation needs Θ to converge and STAY near — but below — 1 (e.g. 0.99997 for t/u). What in the dynamics (damping D, drive S_Θ, a different potential) makes Θ settle at a controlled `1−Θ` rather than oscillate? `1−Θ` small ⇔ heavy.
2. **Is the settling point graph-forced or free?** Once (1) gives stable sub-1 settling, ask whether WHERE it settles (= the mass ratio) is forced by the graph (a symmetry, a fixed point of the Θ dynamics, a `Th_coqc` constraint) or is a free calibration. This is the concrete, finite form of the old "free-parameter" question — no mysticism, just "what sets `1−Θ`."
3. **Get 3 generations, robustly** (fixes FACT Q' fragility) — three stable sub-1 settling points (three `1−Θ` values), robust across the graph constants, not the single isolated M_Θ=4.0 point. Do NOT chase "reading AT the singularity" — that is correctly refused; chase three finite settling points.
4. **Resolve EQ-068's category question** — is native→GeV a valid readout-vs-readout comparison at all? Note: the mass RATIOS (cond# = Θ-readouts) are dimensionless and sidestep the ℏ,c,G non-readout issue, so the ratio program may be checkable even while the absolute-GeV bridge stays open.
5. **Prove or drop n↔generation** (Attempt 13's unproven conjecture) and the whole thread's lack of any `Th_coqc` result.

**Do NOT** re-introduce a "the singularity is ill-defined where we need it" framing — see §6. `Θ=1` is a correctly-refused non-readout; the physics lives at finite `Θ<1`.

## 9. Practical pointers

- Reference mechanism (copyable): `field_sourced_accumulation/field_sourced_accumulation_v0_1.py:run_coupled` (the coupled Φ/Ψ/Θ stepper). The fixed reader: `fixed_q_diagnostic/fixed_q_diagnostic_v0_1.py` (`_evolve(..., product=False)` returns accumulated Θ; `cond_graph_operator(θ)=(1+|θ|)/|1-|θ||`). The convergence discipline: refine dt at FIXED physical time T=n·dt; a physical quantity converges, a 1/dt artifact diverges.
- Real target ratios (from `fit_calibrated_registry.PDG_MASSES_GEV`): up R1=588/R2=136, down R1=20/R2=45, lepton R1=207/R2=17 (R1=gen2/gen1, R2=gen3/gen2). log q targets: down +0.35, up −0.64, lepton −1.09.
- When you add EQ-072→077 to Appendix C, keep tiers honest (`finite_diagnostic`/`Dr`), carry each candidate's REQUIRED caveats in-entry (especially the retractions: EQ for `accumulation_convergence_study` must state it retracts `derived_deceleration_rate`'s FACT G; the `fixed_q_diagnostic` EQ must state EQ-069/070's ranges were the step-count artifact), and update all three synced files identically.

## 10. CONSOLIDATION — transferable knowledge for the DISCRETE-GRAPH program (the root goal)

The continuous arc is closed (see the VERDICT banner). Here is everything it produced that the
discrete-graph `L_R` program should carry forward — so the exploration was not wasted.

### 10.1 What forcing requires (the core lesson)
- **Mass ratio = spectral-gap ratio of `L_R`** stays correct (`stance_for('mass')`), but `L_R` MUST be
  a **discrete N-node graph Laplacian**, not a continuous 2×2 Θ-operator. On a discrete graph the
  **topology forces the eigenvalue spectrum** (integer/rational, calibration-free) — that is the only
  way to get *forced* (not fitted) generation values.
- Minimal structure for **3 generations × 3 sectors**: a **product graph** — a generation-graph ⊗ a
  sector-graph. Example landmark: the path `P₃` has Laplacian eigenvalues `{0, 1, 3}` — already
  integer-forced by topology, no tuning. The discrete program's job is to find the small graph whose
  spectrum matches the data (§10.2) with topology, not calibration, setting the numbers.
- **Do NOT** re-introduce a continuous free knob and call the hierarchy "determined once you fix it."
  That is parameter-count-conserving reparametrization (Wall A). Forcing = topology→spectrum with **no
  tunable value** left.

### 10.2 The empirical TARGET the discrete spectrum must reproduce (computed, hard constraints)
- Real consecutive-generation mass ratios (from `fit_calibrated_registry.PDG_MASSES_GEV`):
  up `(c/u, t/c) = (588, 136)`, down `(s/d, b/s) = (20, 45)`, lepton `(mu/e, tau/mu) = (207, 17)`.
- **The three sectors have DIFFERENT log-hierarchy SHAPES** — the cross-branch log-slope
  `(ln m₃ − ln m₁)/(ln m₂ − ln m₁)` is **up 1.77, down 2.27, lepton 1.53** (computed). Consequence,
  proven this session: a **single shared graph with only a per-sector scale is REFUTED** — the discrete
  structure MUST give **per-sector-distinct spectra** (different sector-subgraphs or couplings), not
  one graph rescaled. (This also killed the Froggatt–Nielsen single-graph exponent idea.)
- **Shape, not just size:** down-type ACCELERATES across generations (R₂ > R₁) while up/lepton
  DECELERATE (R₂ < R₁). The discrete spectrum must produce BOTH shapes from its topology.
- One structural near-coincidence worth remembering (not a result): the up-sector log-slope ratio
  `ln R₁/ln R₂ ≈ 1.30 ≈ 4/3` (2.6% off) — if a discrete graph naturally yields a `4:3` spectral-gap
  pattern for the up sector, that would be a genuine (topology-forced) hit rather than a fit.

### 10.3 Methodology to carry over (hard-won, mostly the honest negatives)
- **Read the operator's spectrum directly** — never a product accumulated over numerical timesteps
  (that is a `1/dt` step-count artifact, the bug that inflated EQ-069/070's 20952x/449808x). On a
  discrete graph this is automatic: diagonalize `L_R` once.
- **Refused endpoints are correct, not walls.** A degeneracy / zero / infinity is a non-readout the
  finite reader must not touch (`ZERO_INFINITY_DUAL_DIAGNOSIS.md`). A discrete spectrum has finite
  gaps by construction — the whole "singular attractor / overshoot" pathology of the continuous arc
  simply does not arise. (Founder caught a materialist bias where an earlier draft treated the refused
  singularity as a limitation — see §6.)
- **Adversarially review every artifact, including your own, and extend the reviewer's own sweeps** —
  this session, review + the founder + a second opinion caught 6+ over-claims (a 1/dt artifact, a
  cherry-picked sign, a single-M_Θ fragility, a two-hits-are-really-one deflation, and the
  coordinate-not-observable structural verdict). Assume your first framing over-claims until swept.
- **Tier honesty**: the whole continuous arc was `finite_diagnostic`/`Dr`, never `Th_coqc`. The
  discrete-graph program has a real shot at `Th_coqc` because a fixed graph's Laplacian spectrum is an
  exact, machine-checkable rational object (diagonalize over ℚ; `Print Assumptions` closed).

### 10.4 Concrete first step for the discrete program
Search small graphs / product graphs whose Laplacian spectral-gap ratios match §10.2's per-sector
targets, with the sector difference coming from **different subgraphs**, not a scale. Start from the
project's existing `L_R` machinery and `scripts/falsify_particle_graph.py` (which already reads
`gapratio(G)` of candidate graphs — it was on the right track; the continuous arc was the detour).
Success criterion: a graph family where **topology alone** fixes the three per-sector spectra to the
data — no fitted Θ, no fitted rate. Until topology forces the numbers, any match stays `fit_calibrated`.
