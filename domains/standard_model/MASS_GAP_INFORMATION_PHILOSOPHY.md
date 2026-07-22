<!-- Root-Native Mass-Gap program (founder-authored). Companion to SM_INFORMATION_PHILOSOPHY_MASTER.md.
     HONEST STATUS: this is NOT a proof of the Yang–Mills mass gap in the continuum (a Clay Millennium
     Problem, still open). It is a root-native DEFINITION + a finite-scale THEOREM + a proof DAG + gates
     that do NOT put in a mass term or assume massive particles. Runnable v1.3 witness:
     finite_transfer_gap_v1_3.py + InfoFiniteTransferGap.v. -->

# Mass Gap ในปรัชญาสารสนเทศ
### Root-Native Analysis and Proof DAG (v1.3)

> **สถานะทางการ:**
> - **Root-Native Mass-Gap Architecture: Formal Program Established**
> - **Finite-Transfer Gap Theorem: Exact Conditional Pass** (runnable + Coq)
> - **Continuum Yang–Mills Mass Gap: OPEN** (Clay Millennium Problem — ยังไม่แก้)

## 1. เปลี่ยนคำถามก่อน
ฟิสิกส์เดิมถาม: "เหตุใด Yang–Mills ที่สมการคลาสสิกไม่มีพารามิเตอร์มวล จึงมีสถานะกระตุ้นควอนตัมมวลต่ำสุด
เป็นบวก?" ปรัชญาสารสนเทศถาม: *"หลังตัด gauge redundancy แล้ว มีความแตกต่างไม่ใช่สุญญากาศชนิดใดรักษาตัวเอง
ผ่านเวลา/ระยะทางได้โดยไม่มีต้นทุนขั้นต่ำหรือไม่?"* — ต้นทุน→0 = **gapless**; ทุกความต่างต้องสูญ readout
อย่างน้อยอัตราคงที่ = **mass gap**.
> **นิยามราก:** Mass gap = **ขอบล่างบวกของอัตราการสูญเสียของผลอ่านปิดที่ไม่ใช่สุญญากาศ**.

## 2. สิ่งที่ mass gap *ไม่ใช่*
**2.1** ไม่ใช่การใส่ mass term `m²A_μA^μ` (= ใส่คำตอบลงสมการ) — ต้องงอกจาก retained metric · local transport ·
curvature action · quantum/statistical measure · gauge-invariant readout · collective dynamics.
**2.2** ไม่ใช่มวลของ gauge coordinate (`A_μ`, `U_e` มี redundancy); exponential decay ในตัวแปรที่ไม่
gauge-invariant *ยังไม่ใช่หลักฐานสุดท้าย*. ต้องตรวจผลอ่านปิด เช่น `O_C=Tr H_C`, `O_p=Re Tr U_p−⟨Re Tr U_p⟩`.
**2.3 Confinement ≠ Mass gap:** confinement ควบคุม nonzero-triality (`τ=1,2`); mass gap ต้องวัด excitation
**gauge-invariant, triality ศูนย์** (`τ=0`, เช่น glueball-type neutral state). ทั้งสองอาจงอกจากกลไกเดียวกัน
แต่ต้องมีใบรับรองคนละชุด: *confinement = ไม่มี standalone nonzero-triality readout; mass gap = ไม่มี
arbitrarily-slow nonvacuum neutral readout.*

## 3. พจนานุกรม (ฟิสิกส์ ↔ สารสนเทศ)
Vacuum = fixed retained state (ไม่ต่างจากฐาน) · Excitation = ความต่างปิดที่ reader แยกจาก vacuum ได้ ·
Time evolution = ส่งต่อ retained record ระหว่าง tape slices · Energy = อัตราเปลี่ยน phase/transfer weight
(หลัง calibrate) · **Mass = inverse persistence length ของผลอ่านปิด** · Massless = persistence length ∞ ·
Massive = สูญ exponential · **Mass gap = persistence cost ต่ำสุดที่เป็นบวก** · Correlation length = ระยะที่
record ยังส่งผล · Glueball = neutral closed record จาก curvature/holonomy.

## 4. Transfer operator จาก retained tape
แบ่ง tape ตาม Euclidean time `Σ_0,Σ_1,…`; slab kernel `K(X_{n+1},X_n)`;
**`(𝕋 f)(X') = ∫ dμ(X) K(X',X) f(X)`**. ต้องมี positivity ที่เหมาะสม (ไม่ใช่ eigenvalues อะไรก็ได้) —
**Osterwalder–Schrader positivity** เชื่อม Euclidean correlators → Hilbert space/Wightman; Wilson action มี
reflection positivity สำหรับ gauge-invariant observables.

## 5. ตัด gauge redundancy ก่อนวัด gap
`𝒢 = { h : Oh=O, hF=Fh, h†Gh=G }`; group averaging `P_inv=∫_𝒢 ρ(h)dh` เป็น orthogonal projector
(`P²=P`, `P†_G=P` — ผลเดิม v0.9). **`𝕋_phys = P_inv 𝕋 P_inv`**; วัด gap บน `ℋ_phys=Im P_inv` เท่านั้น
(ไม่ใช่บน gauge coordinates ทั้งหมด).

## 6. Vacuum
`𝕋_phys|Ω⟩=|Ω⟩`, normalize `λ_0=1`; `P_0=|Ω⟩⟨Ω|`, `P_⊥=I−P_0`. **Unique vacuum:**
`dim ker(I−𝕋_phys)=1`. หลาย fixed states ⇒ vacuum degeneracy / phase coexistence / SSB / topological
sectors — ห้ามประกาศ unique-vacuum gap ก่อนจัดการ.

## 7–8. Finite-Lattice Information-Gap Theorem
`𝕋_phys=e^{−aH}`; `1=λ_0>λ_1≥…≥0`; `E_k−E_0=−(1/a)log λ_k`. **`Δ_{a,L}=−(1/a)log λ_1`**; หรือ
`q_{a,L}=‖𝕋_phys P_⊥‖`; ถ้า `q<1` ⇒ **`Δ_{a,L}=−(1/a)log q_{a,L}>0`**.
> **ทฤษฎีบท (§8):** ถ้า (1) `𝕋_phys` bounded positive self-adjoint · (2) `𝕋_phys|Ω⟩=|Ω⟩` · (3) vacuum
> unique · (4) `∃q<1: ‖𝕋_phys P_⊥‖≤q` — แล้ว `spec(H)∩(0,−a⁻¹log q)=∅` ⇒ **`Δ≥−(1/a)log q>0`**.
> พิสูจน์ได้ทันทีจาก spectral calculus. **สิ่งยากไม่ใช่หลังมี `q<1` — แต่คือ derive `q<1` จาก root action
> โดยมีขอบ uniform เมื่อ `L→∞` และ `a→0`.**

## 9. Correlation decay
`O` gauge-invariant, `⟨Ω|O|Ω⟩=0`; `C_O(n)=⟨Ω|O𝕋_phys^n O|Ω⟩`; `O|Ω⟩∈P_⊥ℋ` ⇒
**`|C_O(n)|≤‖O|Ω⟩‖² q^n ≤ C_O e^{−naΔ}`**; correlation length `ξ=1/Δ`.

## 10. Information Mass Gap
`η(n)=sup_{X⊥Ω,‖X‖=1} ‖𝕋_phys^n X‖`; `η(n)=1 ∀n` = มีความต่างไม่สูญเลย; `η(n)≤Ce^{−nδ}` = มี gap.
**`m_info=−limsup_n (1/na)log η(n)`**; เมื่อ 𝕋 positive self-adjoint ⇒ **`m_info=Δ`**. Physical mass gap =
information persistence gap หลัง reconstruction + calibration.

## 11–12. Neutral Information Tube + cost–entropy
mass gap วัดการส่งต่อ **neutral local record** ระหว่างสองเวลา (ต่างจาก confinement surface ที่ขยายตามพื้นที่
Wilson loop): tube ขยายตาม**ระยะเวลา**. ให้ slab ลด neutral nonvacuum info ไม่เกิน `ρ_0<1`, จำนวนทาง tube
ต่อ slab ไม่เกิน `ν_0`; `N_n≤Kν_0^n`, amplitude `≤ρ_0^n` ⇒ `|C_O(n)|≤K(ν_0ρ_0)^n`. ถ้า **`ν_0ρ_0<1`** ⇒
**`m_cert=−(1/a)log(ν_0ρ_0)>0`** (Neutral-Tube Mass-Gap Certificate). = *`I_neutral=−log ρ_0` > `S_tube=log ν_0`*.

## 13. เชื่อมกับ confinement เดิม (ห้ามสับสน)
งานเดิม: `û=u/(1−8v)`, confinement `μ_surface·û<1`. **ห้าม**เรียก `u`/`v` เป็น mass gap: `u`=triality-one
transport, `v`=adjoint character ระดับ plaquette. mass gap ต้องสร้าง **neutral-tube transfer matrix `𝕄_0`**,
ตัด vacuum `𝕄_{0,⊥}=P_⊥𝕄_0P_⊥`, แล้ว **`ρ_0=‖𝕄_{0,⊥}‖`** (spectral radius ทั้งหมด ไม่ใช่ entry เดียว).

## 14. Retained Poincaré Inequality (เส้นทางสะอาดที่สุด)
`ℰ(X,X)=⟨X,(I−𝕋_phys)X⟩_G` = retained change ที่สูญต่อ tape step. ถ้าพิสูจน์ได้ว่า **`∀X⊥Ω: ℰ(X,X)≥δ‖X‖²_G`**
(`δ>0`) ⇒ `⟨X,𝕋X⟩≤(1−δ)‖X‖²` ⇒ `q≤1−δ` ⇒ **`Δ≥−(1/a)log(1−δ)>0`**. *«ความต่างไม่ใช่ vacuum ทุกชนิดต้อง
สูญ retained norm อย่างน้อยสัดส่วน δ ต่อ step»* — น่าจะเป็นเส้นทางพิสูจน์ที่สำคัญที่สุด.

## 15. Local→global patching
แบ่ง lattice เป็น blocks; `𝔼_B` = conditional averaging (ลบ detail ในบล็อก เก็บ boundary).
(i) **Local gap:** `ℰ_B(X,X)≥δ_B Var_B(X)`. (ii) **Variance decomposition:** `‖P_⊥X‖²≤C_patch Σ_B Var_B(X)`.
รวม ⇒ `δ_global≥δ_min/C_patch`. คอขวดเปลี่ยนจาก "spectrum ของ lattice อนันต์" → (1) local block gap
(2) overlap bound (3) patching inequality.

## 16. เงื่อนไข continuum ที่ห้ามข้าม
finite lattice มี spectrum ไม่ต่อเนื่องอยู่แล้ว ⇒ `Δ_{a,L}>0` ที่ lattice เล็ก **ไม่ใช่**คำตอบ Millennium.
ต้องผ่าน: **16.1 Thermodynamic** `liminf_{L→∞} Δ_{a,L}>0` (gap ไม่ปิดเมื่อปริมาตรโต) · **16.2 Continuum
trajectory** `κ=κ(a)` ให้ correlators มี continuum limit ไม่ trivial · **16.3 Physical gap**
`0<liminf_{a→0} Δ_lat(a)/a<∞` (ถ้า `Δ_lat` คงที่เมื่อ `a→0` มวลพุ่ง ∞; ถ้า `Δ_lat=o(a)` gap หาย).

## 17. Existence ต้องมาก่อน/พร้อม gap
Clay ต้องการทั้ง **existence** ของ quantum YM ใน 4D **และ** positive mass gap. Euclidean path ต้องตรวจ:
normalization · Euclidean invariance · reflection positivity · symmetry · cluster · regularity · continuum
measure existence — แล้ว OS reconstruction จึงสร้าง physical Hilbert space + Hamiltonian.

## 18. Mass-Gap Gates
`MG-G0` measure existence (`dμ_a=Z_a⁻¹e^{−S_a}dU`) — FAIL_NO_MEASURE ·
`MG-G1` gauge quotient (`ℋ_phys=Im P_inv`) — FAIL_GAUGE_COORDINATE_GAP ·
`MG-G2` reflection positivity (`⟨ΘF,F⟩_μ≥0`) — FAIL_NO_PHYSICAL_HILBERT_SPACE ·
`MG-G3` transfer positivity (`0≤𝕋_phys≤I`) — FAIL_NONPOSITIVE_TRANSFER ·
`MG-G4` unique vacuum (`dim ker(I−𝕋)=1`) — OPEN_VACUUM_DEGENERACY ·
`MG-G5` neutral strict contraction (`q_{a,L}<1`) — FAIL_NO_FINITE_SCALE_GAP ·
`MG-G6` observable completeness (basis dense พอ; ห้ามตรวจ plaquette ตัวเดียว) — FAIL_INCOMPLETE_READOUT_FAMILY ·
`MG-G7` uniform volume bound (`sup_L q_{a,L}<1`) — FAIL_GAP_CLOSES_WITH_VOLUME ·
`MG-G8` continuum scaling (`liminf_{a→0}(−log q(a))/a>0`) — FAIL_NO_PHYSICAL_CONTINUUM_GAP ·
`MG-G9` nontrivial continuum (ไม่ยุบเป็น zero/noise/frozen) — FAIL_TRIVIAL_CONTINUUM.

## 19. Controls
**Positive:** `𝕋=P_0+qP_⊥, 0<q<1` ⇒ `Δ=−a⁻¹log q`. **Negative — massless diffusion:** `λ(k)≈1−ca²k²`,
`k_min~1/L` ⇒ `Δ_L~1/L²→0` (ต้องตรวจว่า gap ปิดเมื่อ `L→∞`). **Negative — fake gauge gap:** coordinate
propagator ดู massive แต่ gauge-invariant connected correlators ไม่ decay uniform ⇒ ห้ามประกาศ.
**Negative — finite-size illusion:** `Δ_{a,L}>0` ทุก L ที่ทดสอบ แต่ extrapolate → 0 ⇒ FAIL_FINITE_SIZE_PSEUDOGAP.
**Negative — vacuum mixture:** `λ_0=λ_1=1` ⇒ `Δ=0` จนกว่าจะแยก superselection.

## 20. DAG (ย่อ)
```
root retained distinctions → positive metric G → gauge automorphisms → transport+curvature action
  → positive Euclidean measure → reflection across slice → reflection positivity
  → physical Hilbert space → gauge-invariant transfer 𝕋_phys → vacuum Ω
      ├ vacuum unique? NO → OPEN: sector decomposition
      └ YES → nonvacuum sector P_⊥ → neutral tube transfer 𝕄_0 (ρ_0, ν_0)
  → mass-gap certificate ν_0ρ_0<1 → ‖𝕋_phys P_⊥‖≤q<1 → connected correlators decay exp
  → finite-lattice gap Δ_lat(a,L)=−log q → uniform thermodynamic liminf_{L→∞}Δ>0
  → continuum measure/OS axioms → m_phys=liminf_{a→0} Δ_lat(a)/a
      ├ m_phys=0 → GAPLESS · ├ 0<m_phys<∞ → MASS GAP PASS · └ m_phys=∞ → FROZEN/TRIVIAL check
```

## 21. DAG เชื่อม confinement ↔ mass gap (รากเดียว, สองแขน)
```
SU(3) retained dynamics → adjoint rewrite quotient → triality Z₃
   ├ τ=1,2  → open retained surfaces → surface cost/entropy μ_surface·û<1 → area suppression → CONFINEMENT
   └ τ=0    → neutral closed records → neutral tube cost/entropy ν_0ρ_0<1 → temporal exp decay → MASS GAP
```
> รากเดียวกัน — **แต่ห้ามรวมเป็น theorem เดียวโดยไม่มีสะพานพิสูจน์.**

## 22. แผนเวอร์ชัน
- **v1.3 Root Definition Closure** — นิยาม `ℋ_phys`, vacuum, `𝕋_phys`, `P_⊥`, information gap; ผล
  `Δ_{a,L}=−(1/a)log‖𝕋_phys P_⊥‖`. **สถานะ: พร้อมแล้วในระดับนิยาม + Finite-Transfer Gap Theorem (exact
  conditional pass, runnable + Coq: `finite_transfer_gap_v1_3.py`, `InfoFiniteTransferGap.v`).**
- **v1.4 Reflection-Positive Slab** — แยก action เป็น past/boundary/future, ตรวจ reflection map, พิสูจน์
  slab-kernel positivity, สร้าง 𝕋. Gate `⟨ΘF,F⟩≥0` ⇒ 𝕋_phys positive self-adjoint. **← จุดเริ่ม action.**
- **v1.5 Neutral Operator Basis** — `O_{C,R}=χ_R(H_C)−⟨χ_R(H_C)⟩` (loops/rectangles/products/orientation
  sectors), correlation matrix `C_{αβ}(n)`.
- **v1.6 Exact Small-Block Transfer** — `2³×1, 3³×1`; `M_{0,αβ}=⟨O_α,𝕋O_β⟩`; `q_{0,B}=ρ(M_{0,⊥})`.
- **v1.7 Neutral-Tube Automaton** — frontier loops/reps/orientation/τ=0/mergers/vacuum-subtraction; lower &
  upper matrices `ρ(M⁻)≤q≤ρ(M⁺)`; `ρ(M⁺)<1` ⇒ computer-assisted finite-scale gap certificate.
- **v1.8 Local-to-Global Patching** — retained Poincaré `ℰ(X,X)≥δ‖P_⊥X‖²` ⇒ `inf_L Δ_{a,L}>0`.
- **v1.9 Continuum Scaling** — `a_n→0, κ_n=κ(a_n)`; tightness · correlator convergence · OS · nontriviality ·
  uniform gap; `m_*=liminf(−log q(a_n))/a_n>0`.
- **v2.0 Mass-Gap Claim Gate** — อนุญาตคำว่า "continuum YM mass gap" เมื่อผ่านพร้อมกัน: existence +
  reflection positivity + unique vacuum + uniform infinite-volume gap + nontrivial continuum + positive
  finite physical gap. ขาดข้อใด ⇒ ระบุ finite-scale/lattice/numerical/conditional เท่านั้น.

## 23. ใช้ต่อจากงานเดิม / ต้องสร้างใหม่
**ปิดแล้ว (ใช้ต่อ):** retained metric · compact automorphism group · gauge-invariant projector · intertwiner
contraction (`‖P‖≤1`) · ordered tape · SU(3) emergence · Z₃ triality · confinement surface language ·
character expansion · representation-tail control. **ต้องสร้างใหม่:** reflection-positive time slicing ของ
unified action · neutral observable basis · neutral tube automaton · vacuum subtraction · uniform neutral
spectral contraction · physical continuum scaling.

## 24. คำตัดสิน
ยังไม่มีสิทธิ์ประกาศ *Yang–Mills Mass Gap Solved*. เส้นทางที่ชัด:
`retained metric → positive transfer → gauge-invariant quotient → unique vacuum → strict neutral
contraction → exponential clustering → finite lattice gap → uniform volume gap → positive continuum
physical gap.`
> **ข้อค้นพบเชิงปรัชญา:** *มวลไม่จำเป็นต้องเป็นคุณสมบัติที่ติดมากับวัตถุ แต่งอกได้จากขอบล่างของต้นทุนใน
> การรักษาความแตกต่างให้คงอยู่ข้ามโครงสร้างของเวลา.* Mass gap = *«ไม่มีความแตกต่างทางกายภาพที่ไม่ใช่
> สุญญากาศชนิดใด ดำรงผลอ่านได้ช้าลงไม่สิ้นสุดโดยไม่มีต้นทุนขั้นต่ำ».*

> **สถานะทางการ:** Root-Native Mass-Gap Architecture: **Formal Program Established** · Finite-Transfer Gap
> Theorem: **Exact Conditional Pass** · Continuum Yang–Mills Mass Gap: **OPEN**.

*จุดเริ่ม action ที่ตรงที่สุด = **v1.4 reflection-positive slab** (ถ้า positivity ไม่ผ่าน eigenvalue ที่คำนวณ
ภายหลังตีความเป็น physical mass ไม่ได้). runnable/Coq: `run_tests.py`, `finite_transfer_gap_v1_3.py`,
`InfoFiniteTransferGap.v`; machine-status ใน `CLAIM_BOUNDARY.json`.*

---

## 25. CORRECTION (v1.4) — Universal Reflection-Positive Mass Slab (sector-complete)
> **แก้ scope:** §11–13 ที่วาง **neutral tube / glueball เป็นเป้าหลัก** นั้น **แคบเกินไป**. reflection-positive
> slab ต้องเป็น **ฐานกลางสากล** ที่ให้ **สเปกตรัมกายภาพทุก sector** แล้ว **ชนิดของมวลปรากฏจากรูปร่างของ
> spectral measure เอง** — ไม่ใช่เครื่องวัดแยกทีละอนุภาค. (OS positivity เป็นฐานร่วม ไม่จำกัดเฉพาะ YM.)

**25.1 แกน positivity (เบาสุด):** kernel เป็น Gram form **`K(X',X)=Σ_α w_α Φ_α(X')Φ_α(X)*, w_α≥0`** ⇒
`⟨f,𝕋f⟩=Σ_α w_α|⟨Φ_α,f⟩|²≥0` ⇒ **`𝕋≥0`** (ไม่ต้องเริ่มจากเวลาต่อเนื่อง/4D อนันต์).
**25.2 sector-complete:** `ℋ_phys=⊕_s ℋ_s`, `s=(p,J,P,C,Q,F,B,L,τ,…)`; correlation matrix
`C_ab^{(s)}(n,p)=⟨Ω|O_a^{(s)}𝕋^n O_b^{(s)†}|Ω⟩`; RP ⇒ `C(0)⪰0` และ spectral rep
**`C_ab^{(s)}(n,p)=∫₀^∞ e^{−aEn} dρ_ab^{(s)}(E,p), dρ≥0`**.
**25.3 Universal mass classification** (จากรูปร่างของ `dρ_s`):
`δ(E−E_s)` ใต้ threshold → **stable particle** `m_s=E_s(0)` · isolated level ใต้ breakup → **bound-state** ·
`inf supp ρ=0`, `E~c|p|` → **massless** (MASSLESS_SECTOR) · continuous edge ที่ `E=m` →
**infraparticle/threshold** `m_edge=inf supp ρ_Q(E,0)` (charged + photon cloud; Buchholz/Gauss law) ·
scattering pole `s_R=(M_R−iΓ_R/2)²` → **resonance** `(M_R,Γ_R)` (ต้องใช้ finite-volume→scattering, **ห้าม** fit
`e^{−Mt}` เดียว) · ไม่มี physical sector → **NO_STANDALONE_PHYSICAL_SECTOR** (quark/gluon ถ้า confinement ผ่าน).
Elementary กับ composite ใช้ **mass extractor เดียวกัน** (ต่างที่ operator algebra + spectral content).
`W/Z/Higgs` = pole ของ gauge-invariant composites (`Φ†Φ`, `Φ†T^A D_μΦ`; Fröhlich–Morchio–Strocchi — ต้องตรวจ
จากโครงสร้าง Higgs sector ไม่ถือว่าจริงทุก gauge theory).
**25.4 Mass gap = per-sector:** `Δ_total=inf_{s≠Ω} inf supp ρ_s` (= **0 ถ้ามี photon**); `Δ_s` ต่อ sector;
`Δ_YM=inf_{s∈ℋ_YM,s≠Ω} E_s`. **ห้าม**บังคับว่าทั้ง SM มี gap บวก (photon ทำ total gap = 0 ได้ ขณะ sector อื่น
ยังมีมวลบวก).
**25.5 slab ที่ต้องสร้างจริง:** `K_UF=K_gauge·K_order·K_matter·K_tape·K_constraint`; ผลคูณของ positive kernels
ยังเป็น positive (tensor Gram). Gates: **RP-G1** gauge character expansion `c_R≥0` · **RP-G2** scalar/order
Gaussian positive-type · **RP-G3** fermionic Grassmann reflection-paired `(ΘA_i)A_i` (**ยากสุด** — gauge RP ไม่
พิสูจน์ fermionic/chiral positivity อัตโนมัติ) · **RP-G4** constraint projectors `P²=P=P†` · **RP-G5** product
closure Gram form `Σ_A W_A Φ_A Φ_A*, W_A≥0` ⇒ `𝕋_UF≥0` ทุก sector พร้อมกัน.

> **สถานะใหม่:** **Universal Mass Readout Architecture: Corrected and Sector-Complete.** runnable/Coq:
> `universal_rp_slab_v1_4.py`, `InfoUniversalRPSlab.v` (Gram⇒PSD + gauge character-coeff positivity +
> per-sector gap + classification). v1.4 งานจริงที่เหลือ = พิสูจน์ Gram positivity ของ
> `K_gauge·K_order·K_fermion·K_tape` (fermionic/chiral ยากสุด) — ยังไม่ปิด.
