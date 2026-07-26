# Discrete Mass Hierarchy (item 1) — Plan + Checklist for the next model

> Self-contained. If you are a fresh AI, this file + the two it points to
> (`SM_INFORMATION_PHILOSOPHY_MASTER.md`, `MASS_GAP_INFORMATION_PHILOSOPHY.md`) let you pick up the
> fermion-mass program from zero. Written 2026-07-26 after the previous AI (a) fell into a continuum
> detour and (b) forgot the parameter-economy ledger. Both mistakes are recorded below so you don't
> repeat them.

## 1. The goal (the success criterion — this is the whole point)

Reproduce the Standard Model's own physics via the **information-SM, DISCRETE** approach, **fitting
FEWER free values than the standard SM does.** The SM fits **19** (see §2). *You do NOT need to derive
anything from nothing* — that materialist bar is explicitly rejected. **Fitting is allowed; fitting
fewer than 19 is the win.** Founder ruling, verbatim: *"คำนวนตรงไหมก็พอ SM ก็ฟิตตั้ง 19 ค่า"* and
*"แก้โจทย์ได้ โดยฟิตค่าน้อยกว่า SM ทั่วไปก็พอ"*. Scope: **info-SM discrete only** — do NOT go solve
general open problems (continuum QG, Millennium, etc.).

## 2. Where we stand — the parameter-economy ledger (already 17/19, NOT 0)

Canonical count: `SESSION_2026_07_24_PARAMETER_ECONOMY_SUMMARY.md`. The SM's 19 = 9 fermion masses +
3 gauge couplings + 4 CKM (3 angles + 1 phase) + 2 Higgs (`v`, `λ`) + 1 `θ_QCD`.

| sector | SM | info-SM now | saved |
|---|---|---|---|
| 9 fermion masses | 9 | 9 fed in (PDG, `fit_calibrated_registry.py`) | 0 — **THE bottleneck (item 1)** |
| **4 CKM (angles+phase)** | **4** | **2** (`D_up`, `φ`, Fritzsch texture-zero) | **2 ✅ (the rotation sector — already done)** |
| 3 gauge couplings | 3 | 3 | 0 |
| Higgs `v`,`λ` | 2 | 2 (λ proven circular until item 1 closes) | 0 |
| `θ_QCD` | 1 | 1 | 0 |
| **total** | **19** | **17 fit** | **2 (~11%), fit_calibrated** |

**So "fit fewer than SM" is already partly achieved (17 < 19), entirely in the CKM/rotation sector.**

## 3. What the previous AI FORGOT / GOT WRONG (recorded so you don't)

- **FORGOT: the rotation/CKM saving already exists.** The mixing (rotation between flavor and mass
  bases) is the proof-of-concept that this framework CAN fit fewer than the SM:
  - `θ_12` (Cabibbo) = `√(m_d/m_s)` (Gatto–Sartori–Tonin 1968) — **ZERO new parameters** (uses masses
    already in the registry). `item22_exploration/cabibbo_angle_gst_v1.py`.
  - all 3 CKM angles + CP phase reproduced by the **Fritzsch extended texture** with just
    **2 params** (`D_up`, `φ`), fit jointly. `item22_exploration/fritzsch_extended_texture_v1.py`,
    `item24_exploration/cp_phase_jarlskog_v1.py`. So the rotation uses **< 2** where the SM uses 4.
  - **The discrete template to copy:** an earlier root-native mixing attempt smuggled in the continuum
    (inverse trig / "degrees" = the `I1` ℝ-completeness injection); the founder caught it
    (*"องศาคืออะไรในสารสนเทศ"*) and it was refixed as an **overlap fraction**
    `overlap(v,e_i) = |⟨v,e_i⟩_G|² / (⟨v,v⟩_G·⟨e_i,e_i⟩_G)` — a Born-rule ratio (Th_coqc, no trig, no
    π, no ℝ). `item22_exploration/mixing_angle_from_L_R_v2_overlap_fraction.py`. **The mass program
    must stay discrete the same way** (spectral/overlap ratios, never continuum angles/limits).
- **GOT WRONG (the whole 2026-07-25/26 continuum detour, now retracted):** built a **continuous-Θ 2×2
  graph-operator arc** to derive mass ratios. `cond#(G[Θ]) = (1+|Θ|)/(1−|Θ|)` is a smooth *bijection*
  Θ↔R — a **coordinate, not an observable** — so one continuous knob can never force generations. It
  was continuum contamination (against `readout-not-truth`). All of it was removed: EQ-069/070/071
  retracted from the stream, candidate code deleted. Full record + lessons:
  `item1_exploration/CONTINUUM_ARC_ERROR_NOTE.md`. **Do not rebuild any continuous-Θ mechanism.**

## 4. The bottleneck: item 1 = the 9 fermion masses

- It is the biggest single chunk (**9 of 19**).
- It **gates item 18** (Higgs `λ`, proven circular until masses close).
- The CKM saving currently **leans on real masses fed in** (the textures use mass ratios), so closing
  item 1 strengthens the rotation result too.
- Status: `SM_INFORMATION_PHILOSOPHY_MASTER.md` §23 lists "mass hierarchy / Yukawa coefficients" as
  **NOT derived**. This is the keystone open item.

## 5. The discrete approach (grounded — copy the rotation template)

Mass is already given a discrete definition by the framework; the detour ignored it:
- **Mass = inverse persistence length = `−(1/a) log λ_k`** of the **gauge-quotiented transfer operator
  `𝕋_phys`** on `ℋ_phys`, **per representation sector** (`MASS_GAP_INFORMATION_PHILOSOPHY.md` §7–8,
  §25: "the TYPE of mass appears from the SHAPE of the spectral measure itself"). A **discrete spectral
  log-eigenvalue**, read like the overlap fraction — never a continuum coordinate.
- **Hierarchy = exponential of a finite span** (`INFINITY_INJECTION_DIAGNOSIS.md` §2, H5); **masses =
  relational fixed points that run, no scale-free constant** (H2) — the dimensionless **ratios** are
  the object.
- **The reduction lever:** if the **3 generations per sector are eigenvalues of ONE small graph**
  whose topology forces its spectrum (e.g. path `P₃` → Laplacian eigenvalues `{0,1,3}`, integer,
  calibration-free), each sector needs **~1 scale param instead of 3 masses** → **9 → ~3** ⇒ beats 19.
- The **per-sector difference** (up/down/lepton) must come from the **different representations**
  (matter skeleton `Q, u^c, d^c, L, e^c`, already derived) — a computed hard target: the cross-branch
  log-slope differs (up 1.77, down 2.27, lepton 1.53), so a single shared graph rescaled is refuted;
  the sectors need distinct sub-graphs/couplings.
- This is **`Th_coqc`-able**: a fixed graph's Laplacian / transfer-operator spectrum is an exact ℚ
  object (`Print Assumptions` Closed) — unlike the continuous arc which was only `finite_diagnostic`.

## 6. Hard constraints (what NOT to do)

- **No continuum.** No continuous parameter Θ, no continuous-time ODE, no inverse trig / angles /
  limits / ℝ-completeness. If a quantity is a smooth bijection of a free knob, it is a coordinate, not
  physics. Stay in discrete spectra / overlap ratios.
- **Keep the equation stream stable.** Appendix C is at EQ-071 with EQ-069/070/071 RETRACTED; add new
  entries only at EQ-072+, tier-honest, synced across all three stream files.
- **Tier honesty & adversarial review.** Everything `fit_calibrated`/`Dr` until a discrete spectrum is
  topology-forced; independently review every claim (default REFUTE); the previous arc had 6 caught
  over-claims. Report computed-facts + tier, never "works/fails" value-words.
- **Fit is fine; fewer-than-19 is the bar.** Do not chase derive-from-nothing.

## 7. CHECKLIST (concrete, ordered — tick as you go)

- [ ] **C1. Read the ground truth.** `MASS_GAP_INFORMATION_PHILOSOPHY.md` §7–8 + §25; the master §7
      (Yukawa=intertwiner) + §23; `item22_exploration/mixing_angle_from_L_R_v2_overlap_fraction.py`
      (the discrete overlap template); `CONTINUUM_ARC_ERROR_NOTE.md` (what not to repeat).
- [ ] **C2. Inventory existing discrete machinery** — do NOT rebuild. What can `scripts/
      falsify_particle_graph.py` (`gapratio(G)`), the mass-gap v1.3/v1.4 code
      (`finite_transfer_gap_v1_3.py`, `universal_rp_slab_v1_4.py`), and the `L_R` operator already
      compute? Write a one-page map of reusable pieces.
- [ ] **C3. Pin the target numerically.** For each sector, the two consecutive-generation mass ratios
      and the log-slope (up 1.77 / down 2.27 / lepton 1.53). These are the numbers a discrete spectrum
      must hit. (Already in `CONTINUUM_ARC_ERROR_NOTE.md` §3.3.)
- [ ] **C4. Small-graph spectral search (the core experiment).** Search small graphs / product graphs
      (`P₃`-like ⊗ sector) whose Laplacian (or transfer-operator) spectral-gap ratios reproduce ONE
      sector's two mass ratios from **fewer than 2 free parameters** (ideally 1 scale). Topology forced,
      not fitted. Read the ratio as a Born-rule/spectral ratio, never an angle.
- [ ] **C5. Per-sector difference from representation.** Show the up/down/lepton log-slope difference
      arises from their different representations (distinct sub-graphs), not a per-sector free knob.
- [ ] **C6. Parameter count.** Tally: does the discrete construction fit `< 9` for the masses? Update
      the ledger in `SESSION_2026_07_24_PARAMETER_ECONOMY_SUMMARY.md` honestly (fit_calibrated).
- [ ] **C7. Tier + review.** Independent adversarial review (default REFUTE); if a spectrum is
      topology-forced (not fitted), pursue a `Th_coqc` witness (exact ℚ eigenvalues, `Print
      Assumptions` Closed). Only then does it stop being `fit_calibrated`.
- [ ] **C8. Log + stream.** Log in `item1_exploration/ITEM1_EXPLORATION_LOG.md`; if a result is solid,
      add EQ-072+ to Appendix C (all three synced files), branch+PR both repos, merge only on founder
      instruction.
- [ ] **C9. (stretch) Item 18 unlock.** Once masses have a discrete handle, revisit `λ` (item 18,
      currently proven-circular).

## 8. Pointers

- Success criterion + ledger: `SESSION_2026_07_24_PARAMETER_ECONOMY_SUMMARY.md`.
- Discrete mass definition: `MASS_GAP_INFORMATION_PHILOSOPHY.md` (§7–8, §25).
- Structure already derived: `SM_INFORMATION_PHILOSOPHY_MASTER.md` (§21 closed, §23 open).
- Rotation template (discrete, fewer-params, already done): `item22_exploration/`, `item24_exploration/`.
- What not to repeat: `item1_exploration/CONTINUUM_ARC_ERROR_NOTE.md`.
- Reusable graph-spectrum code: `scripts/falsify_particle_graph.py`, mass-gap `*_v1_3.py`/`*_v1_4.py`.
