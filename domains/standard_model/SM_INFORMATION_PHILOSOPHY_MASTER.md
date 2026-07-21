<!-- CANONICAL SYNTHESIS (ฉบับแม่). Founder-authored master reference for the Standard-Model /
     color / confinement work in the information-philosophy framework. Use this as the PRIMARY
     reference to prevent drift back to importing external physics laws as premises without
     declaring their tier. It separates: closed (§21) · conditional/numerical (§22) · not-yet-
     derived (§23). Every runnable witness lives in this folder (see INDEX / run_tests.py);
     every claim's machine-status is in CLAIM_BOUNDARY.json and STANDARD_MODEL_CLOSURE.md. -->

# Standard Model ในภาษาปรัชญาสารสนเทศ
### ฉบับสังเคราะห์ตั้งแต่รากจนถึงโครงสร้างแรงและ confinement (ฉบับแม่ · canonical reference)

> **สถานะรวม:** *Root-Native Standard-Model Architecture — **Substantial Partial Closure*** (ไม่ใช่
> *Complete Standard Model Derivation*). ทุกผลในเอกสารนี้มี tier กำกับ; ผลที่ปิดแล้วมี verifier (PASS)
> + Coq witness (`Print Assumptions` Closed) ในโฟลเดอร์นี้ (`run_tests.py`, `CLAIM_BOUNDARY.json`,
> `STANDARD_MODEL_CLOSURE.md`).

## บทนำ — เรากำลังทำอะไร
เป้าหมายไม่ใช่การนำ Standard Model ที่รู้คำตอบอยู่แล้วมาเปลี่ยนชื่อเป็นภาษาสารสนเทศ แต่คือการเริ่มจาก
รากที่เล็กที่สุด — ความแตกต่างที่ระบบรักษาไว้, การอ่านผล, ความทรงจำ/ลำดับของเหตุการณ์, การเปลี่ยนชื่อ
ภายในที่ไม่ทำให้ผลอ่านเปลี่ยน, การเชื่อมข้อมูลหลายตำแหน่ง, และเงื่อนไขที่ข้อมูลปิดเป็นผลอ่านสมบูรณ์ได้ —
แล้วถามว่าโครงสร้างที่ภายหลังเรียกว่า `U(1)`, `SU(2)`, `SU(3)` งอกจากรากได้หรือไม่

> **หลักบังคับ:** *ชื่อทางฟิสิกส์ต้องมาในภายหลัง ไม่ใช่เป็น premise ที่ใส่ไว้ตั้งแต่ต้น.* "สี", "ประจุ",
> "แรง", "ควาร์ก", "กลูออน", "เกจ" = ความหมายที่มอบให้โครงสร้าง**หลัง**ค้นพบ ไม่ใช่วัตถุตั้งต้น

---

## ส่วนที่ 1 — รากของภววิทยาสารสนเทศ

**1.1 สิ่งพื้นฐานที่สุดคือความแตกต่างที่ยังถูกรักษาไว้.** สถานะ retained ลำดับ `n`:
`Z_n = (Φ_n, Ψ_n, Θ_n, U_n, Σ_n, 𝒯_n, Λ_n)` — บทบาทเชิงสารสนเทศ (ข้อเสนอ · สิ่งที่มีผลต่อการอ่าน ·
โครงสร้างการแปล · กฎขนส่งความต่าง · ร่องรอยสะสม · tape/ลำดับ · เงื่อนไขปิด). แก่น: *สิ่งที่ไม่มีผลต่อ
การอ่านใดเลย ไม่ควรถูกนับเป็นความแตกต่างทางกายภาพ.*

**1.2 Reader–record relation.** ผลอ่าน `r=O(X)`; ถ้า `O(hX)=O(X)` ทุกสถานะ → `h` คือการเปลี่ยนชื่อ
ภายใน. นิยาม `X∼X' ⟺ O(X)=O(X')`; physical state = equivalence class `[X]`. **นี่คือรากของ gauge redundancy.**

**1.3 Retained metric.** `⟨x,y⟩_G = x†Gy, G>0` ⇒ retained load `‖x‖²_G = x†Gx ≥ 0`. ยังไม่ใช่ "พลังงาน"
จนกว่าจะ calibrate.

---

## ส่วนที่ 2 — Ordered tape และการกำเนิดลำดับ

**2.1** tape ต้องรักษาลำดับ (แยก `A→B` จาก `B→A`). สลับติดกัน: `Ω(…x_i,x_{i+1}…)=r·Ω(…x_{i+1},x_i…)`,
`r²=1 ⇒ r=±1`. ต้องแยกลำดับจริง ⇒ **`r=−1`** ⇒ primitive witness เป็น **antisymmetric**.

**2.2** วงปิดไม่มีจุดเริ่มพิเศษ: `Ω(x_1…x_k)=Ω(x_2…x_k,x_1)`; ย้าย `x_1` ไปท้าย = สลับ `k−1` ครั้ง ⇒
เครื่องหมาย `(−1)^{k−1}`. cyclic-invariant + nonzero ⇒ **`(−1)^{k−1}=1` ⇒ `k` เป็นเลขคี่**. `k>1` ต่ำสุด
⇒ **`k=3`** (Three-Channel Necessity).

---

## ส่วนที่ 3 — จากสามช่องไปสู่ SU(3)

**3.1** alternating trilinear `Ω(x,y,z)` = 0 เสมอ ถ้า `dim V<3` ⇒ `dim V≥3`; minimal non-spectator carrier
⇒ **`dim V=3`**, `V≅ℂ³`.
**3.2** รักษา metric: `U†GU=G`, basis `G=I` ⇒ `U†U=I` ⇒ กลุ่มอยู่ใน `U(3)`.
**3.3** triple witness: `Ω(Ux,Uy,Uz)=det(U)·Ω(x,y,z)`; รักษา ⇒ `det U=1` ⇒
> **`SU(3) = {U∈U(3): det U=1}`**

สายการงอก: `ordered tape → odd cyclic closure → 3 channels → metric+volume preservation → SU(3)`.
**3.4** ตัวแปลงบนสามช่อง `3×3=9`; ตัด common trace (`Tr X=0`) ออก 1 ⇒ **`9−1=8 = dim su(3)`** (แปดตัวพา
แรงไม่ได้ถูกป้อน).

---

## ส่วนที่ 4 — รากของ gauge structure

**4.1 Automorphisms ที่อ่านไม่ออก:** `𝒜 = { h : Oh=O, hF=Fh, h†Gh=G }`. แต่ละตำแหน่งเลือก basis ต่างกัน
⇒ ตัวขนส่ง `U_{j←i}` แปลงเป็น **`U'_{j←i} = h_j U_{j←i} h_i⁻¹`** (local gauge transformation จากข้อเท็จจริงว่า
reader ต่างตำแหน่งตั้งชื่อพิกัดภายในต่างกันได้).
**4.2 Holonomy/curvature:** `H_C = ∏_{e∈C} U_e`, `H_C' = h H_C h⁻¹` ⇒ อ่านได้เฉพาะ conjugation-invariant
(เช่น `Tr H_C`); **`𝒦_C = H_C − I`** = ความไม่สอดคล้องของการแปลรอบวง.
**4.3 แรง = projection:** `𝓕_all = 𝓕_G+𝓕_EM+𝓕_W+𝓕_S+𝓕_res`; completeness `χ4 = 1 − ‖𝓕_res‖²/‖𝓕_all‖²`.
`χ4≈1` = สี่ sector อธิบายเกือบครบ; residual ใหญ่ = ห้ามประกาศว่ามีแค่สี่แรง.

---

## ส่วนที่ 5 — การค้นพบ algebra ของ Standard Model
Blind pipeline (ไม่ป้อนชื่อ): พบ `dim Z(𝔤)=1` + simple ideals `(dim,rank)=(3,1)` และ `(8,2)` ⇒ semantic
label `𝔤 ≅ u(1)⊕su(2)⊕su(3)`, `dim = 1+3+8 = 12`. **ซื่อสัตย์:** pipeline แยก algebra นี้ได้ใน fixtures —
*ยังไม่ใช่*การพิสูจน์ว่า axioms รากบังคับให้ทั้งสามก้อนนี้เป็นคำตอบเดียวในทุกระบบ.

---

## ส่วนที่ 6 — ความหมายของสาม sector
**6.1 U(1)** = freedom ของ common phase `x↦e^{iα}x` ที่ retained load ไม่เปลี่ยน; อ่านได้เฉพาะความต่างเฟส/
holonomy. **ยังไม่ปิด:** central direction = hypercharge จริงไหม (charge spectrum, normalization, anomaly,
global quotient).
**6.2 SU(2)** = simple ideal `(3,1)` = algebra นอน-abelian เล็กสุดบน binary doublet; **weak-sector
identification ยังมีเงื่อนไข** (chiral, doublet/singlet, charges, เชื่อม U(1)).
**6.3 SU(3)** = รากแข็งสุด: `ordered tape → 3-cycle → ℂ³ → SU(3)` (สามช่องที่เดี่ยวปิดไม่ได้ แต่สามชนิด
สร้าง alternating closure สมบูรณ์ได้).

---

## ส่วนที่ 7 — สสารคืออะไร
**7.1** representation = ชนิดของความแตกต่างที่ตอบสนองต่อ internal relabeling `x↦ρ_R(g)x` แบบหนึ่ง (ไม่ได้
เริ่มจากจุดมวล). **7.2** Casimir `C_2(R)` = ฉลาก basis-independent จำแนก representation (pipeline: blind
algebra → joint Casimirs → eigenspaces → irreps → intertwiners → anomaly). **7.3 Interaction = invariant
intertwiner** `𝓘 : R_1⊗…⊗R_n → 1`; ไม่มี singlet channel = coupling ปิดไม่ได้. Yukawa = intertwiner
(left⊗right⊗scalar); *ค่ามวล/coupling จริงยังไม่ derive.*

---

## ส่วนที่ 8 — Pair–triple grammar
`3⊗3̄ → 1+…` (ข้อมูล+ข้อมูลตรงข้าม → neutral); `3⊗3⊗3 → 1+…` ผ่าน `ε_{abc}x^a y^b z^c`; **ไม่มี** `3→1`
(singleton ปิดไม่ได้) — จุดเริ่มของ confinement.

---

## ส่วนที่ 9 — จาก SU(3) เต็มไปสู่ retained Z₃
**9.1** โจทย์ที่ถูก *ไม่ใช่* "ฉาย SU(3)→Z₃ ด้วยมือ" แต่คือ: หลัง adjoint dynamics เขียนทับ representation
detail ข้อมูลใดเหลือ. weight lattice `P`, root lattice `Q`; adjoint เปลี่ยน weight ด้วย `Q` ⇒ retained
quotient **`P/Q ≅ Z₃`**.
**9.2 Triality** `τ(p,q) = p+2q (mod 3)`: `τ(3)=1, τ(3̄)=2, τ(8)=0`; adjoint `τ=0` ⇒ `τ(R⊗8)=τ(R)` (local
dynamics เปลี่ยน detail ได้ แต่เปลี่ยน triality ไม่ได้).
**9.3** `1+2=0`, `1+1+1=0`, แต่ `1,2≠0 (mod 3)` ⇒ pair + triple ปิด, singleton ไม่ปิด. **ordered-tape
derivation กับ representation quotient บรรจบที่ `Z₃` เดียวกัน.**

---

## ส่วนที่ 10 — Confinement ในภาษาสารสนเทศ
**10.1 นิยามรากกว่า:** *ไม่มี asymptotic standalone readout ที่มี nonzero triality* — `ℋ_physical ⊆ ℋ_{τ=0}`.
**10.2 Exact Z₃ 2D witness:** `z_e∈Z₃`, `u_p=∏ z_e^{ε}`, `S=κΣ|u_p−1|²`, `|ω−1|²=3`, `r=e^{−3κ}` ⇒
`q(κ)=(1−r)/(1+2r)`; 2D simply-connected ⇒ **`⟨W(C)⟩=q^{A(C)}`** ⇒ area law `σ=−log q>0` (exact pass เฉพาะ
Z₃/2D). **10.3** พื้นผิว 3+1D: `n_p∈Z₃`, closure `δn=j (mod 3)` (nonzero triality หยุดกลางไม่ได้ ต้องต่อ
แผ่นหรือจบที่ source triality ตรงกัน). **10.4 Cost–entropy:** `ρ<1` ต่อ plaquette, `N_A≲μ^A` ⇒ `Σ N_A ρ^A ≲
Σ(μρ)^A`; sufficient **`μρ<1`** ⟺ `I_retain=−log ρ > S_surface=log μ`.

---

## ส่วนที่ 11 — Full SU(3) action & character coefficients
`S_p(U)=κ‖U−I‖²_F`, `‖U−I‖²=6−2Re Tr U` ⇒ `K_κ(U)=exp[κ(χ_3+χ_3̄)]=Σ_R c_R(κ)χ_R`,
`c_R(κ)=∫_{SU(3)} K_κ χ_R^*`. **All-order recursion:** `dK/dκ=(χ_3+χ_3̄)K ⇒
c_R'(κ)=Σ_S(N_{3S}^R+N_{3̄S}^R)c_S`, `c_R(0)=δ_{R0}` (coefficients ทุกลำดับจาก fusion grammar).
`u=c_3/3c_0` (fundamental triality retention), `v=c_8/8c_0` (adjoint dressing).

---

## ส่วนที่ 12 — Intertwiners ขยายข้อมูลไม่ได้
`h†Gh=G` (G>0) ⇒ กลุ่มเป็น compact. link projector **`P_e=∫_𝒢 ρ_e(h)dμ(h)`**: `P²=P`, `P†_G=P`
(orthogonal projector) ⇒ **`‖P_e T‖_G ≤ ‖T‖_G`** — จุดเชื่อมภายในเลือกข้อมูลที่ปิดร่วมได้เท่านั้น
*สร้าง/ขยาย signal ไม่ได้* (internal exact).

---

## ส่วนที่ 13 — Infinite representation tail
`3⊗8 = 3⊕6̄⊕15` (แตกไม่สิ้นสุด แต่รักษา triality). `‖N_8‖_∞≤8`; `Σ_m(vN_8)^m` ลู่เข้าเมื่อ **`8v<1`** ⇒
**`û ≤ u/(1−8v)`** (ไม่ต้องตรวจ representation ทีละตัว หาก resolvent ผ่าน).

---

## ส่วนที่ 14 — Surface entropy automaton
**14.1 Frontier state** `b_s∈C_1(Σ_s;Z₃)`; transition `∂q_s+b_s−b_{s+1}=j_s (mod 3)` ⇒ surface counting =
finite-state process. **14.2 Restricted lower:** single-height shortest connector ⇒
**`μ_shortest=3.875129794…`** (lower bound). **14.3 Local branching upper:** edge 4D แตะ 6 plaquettes,
เหลือ 5 ช่อง; assignments รักษา Z₃ closure แยกตาม `r` = `5,10,30,25,11` ⇒ **`B(z)=5z+10z²+30z³+25z⁴+11z⁵`**;
`B(z_+)=1 ⇒ z_+≈0.14116126 ⇒ μ_local^+≈7.08409660`. ⇒ **bracket `3.87513 ≤ μ_4^admissible ≤ 7.08410`**
(ขอบบนมีเงื่อนไข first-discovery encoding).

---

## ส่วนที่ 15 — Confinement certificate ปัจจุบัน
**`𝔠(κ) = μ_4^admissible · u(κ)/(1−8v(κ))`**; PASS เมื่อ `𝔠<1` ⇒ `|⟨W(C)⟩| ≲ e^{−σ_cert A_min}`,
`σ_cert=−log 𝔠>0`. ใช้ `μ^+=7.08409660` + all-order Haar integrals ⇒ threshold **`κ_*≈0.321686625`**.
สถานะ: ***conditional high-precision certificate*** (ไม่ใช่ proof ของ continuum QCD).

---

## ส่วนที่ 16 — String breaking
ไม่มี matter: `V(R)~σR`. มี matter triality 1/2: สร้างคู่มาปิดปลายได้ ⇒
**`V_eff(R) ≈ min(σR, 2M_scr)`**, `R_break = 2M_scr/σ`. *ไม่ละเมิด triality conservation* — ข้อมูลไม่หาย
แต่ย้ายไป endpoints ใหม่จนผลรวมเป็นกลาง.

---

## ส่วนที่ 17 — Chirality (กำแพงหลัก)
chirality ต้องงอกจาก ordered orientation ของ tape: `Γ_𝒯`, `V=V_L⊕V_R`, `P_{L,R}=(1∓Γ_𝒯)/2` แล้วพิสูจน์ว่า
SU(2) กระทำไม่เท่ากันบนสอง sector. **ยังไม่ derive:** orientation operator จากรากโดยไม่ป้อน Dirac algebra,
spectrum, เชื่อม Lorentz/spin, chiral anomaly ที่ถูก ⇒ **chirality ยังเป็นกำแพงหลัก**.

---

## ส่วนที่ 18 — Radiative corrections
`Γ^{(1)} = ½log det'𝓗_B − ½log det'(𝓗_F†𝓗_F) − log det'𝓜_orb` (bosonic Hessian · fermionic/chiral ·
orbit subtraction). *ไม่ป้อน* textbook `11/3, 2/3, 1/3` — coefficients ต้องเกิดจาก spectrum/multiplicity/
representation/orbit/statistics. สถานะ: **log-det engine กำหนดแล้ว, physical coefficients ยังไม่ derive ครบ**.

---

## ส่วนที่ 19 — Unified action candidate
**`S_UF = S_DRL + S_geo + S_int + S_Σ + S_cut + S_tape`**, `δS_UF/δZ_n = 0`. เป็น **architecture** ไม่ใช่
physical final action ที่สอบเทียบเสร็จ.

---

## ส่วนที่ 20 — DAG ฉบับแม่
```
retained distinctions → reader–record equivalence → positive retained metric
   → automorphisms reader can't separate → local basis freedom → transport U_{j←i}
   → holonomy & curvature → internal transformation algebra
        ├── center dim 1        → U(1)-type sector
        ├── simple ideal (3,1)  → SU(2)-type sector
        └── ordered tape → antisymmetric cyclic closure → three channels
              → metric + triple-form preservation → SU(3)
   → representations & intertwiners → adjoint rewrite equivalence → P/Q ≅ Z₃ → triality
        ├── pair closure   ┐
        └── triple closure ┘ → no singleton neutral readout
   → retained Z₃ surfaces → surface closure δn=j → character retention u,v
   → tail resolvent û≤u/(1−8v) → surface entropy μ → μû<1 certificate → area suppression
        ├── pure carrier: V(R)≈σR
        └── dynamical matter: string breaking → asymptotic triality neutrality
```

---

## ส่วนที่ 21 — สิ่งที่ถือว่าปิดแล้ว (exact / exact-under-declared-axioms)
1. Reader-equivalence ⇒ gauge-type redundancy · 2. Metric-preserving automorphisms ⇒ compact group ·
3. Local relabeling ⇒ transport law · 4. Holonomy แปลงด้วย conjugation · 5. Ordered cyclic antisymmetric
minimal closure ⇒ `k=3` · 6. Minimal carrier ⇒ dim 3 · 7. รักษา Hermitian metric + trilinear volume ⇒
SU(3) · 8. `dim su(3)=8` · 9. `P/Q≅Z₃` · 10. Triality คงที่ใต้ adjoint rewrites · 11. Link group averaging
= orthogonal projector · 12. Intertwiners ไม่ขยาย retained norm · 13. Exact Z₃ 2D area law · 14. All-order
character coefficient integral นิยามครบ · 15. Infinite adjoint tail มี resolvent bound เมื่อ `8v<1`.

## ส่วนที่ 22 — สิ่งที่มีเงื่อนไข / numerical closure
1. ระบุ blind algebra ว่าเป็น SM algebra จาก fixtures · 2. uniqueness ของ `u(1)⊕su(2)⊕su(3)` ·
3. surface entropy upper bound `7.0841` · 4. 4D confinement certificate · 5. threshold `κ_*≈0.321686625` ·
6. เชื่อม finite-lattice certificate → continuum · 7. ตีความ `κ` เป็น physical coupling · 8. linear potential
ก่อน string breaking · 9. representation-tail multiplicity bound ในทุก effective interaction.

## ส่วนที่ 23 — สิ่งที่ยังไม่ได้ derive
**กลุ่ม:** uniqueness ของ gauge algebra · global quotient (เชื่อม centers) · hypercharge normalization.
**สสาร:** matter multiplets ครบ · จำนวน generation = 3 · quark/lepton assignment · neutrino · particle–
antiparticle จากราก. **Chirality/spacetime:** Lorentz · spin · spin–statistics · exclusion · left–right
asymmetry · chiral anomaly. **Scalar/มวล:** Higgs-like order parameter · SSB · vev · Yukawa · mass
hierarchy · CKM/PMNS · CP violation. **Dynamics:** physical β-functions · asymptotic freedom จาก root-native
determinant · continuum limit · nonzero physical mass gap · physical string tension · matching กับ QCD.
**การทดลอง:** couplings · masses · decay rates · cross sections · precision electroweak.

---

## ส่วนที่ 24 — ข้อค้นพบเชิงปรัชญาหลัก
**24.1** gauge symmetry = ข้อจำกัดของการตั้งชื่อ (ไม่ใช่สมมาตรของวัตถุ); gauge field = สิ่งที่ทำให้คำแปล
ระหว่าง reader ต่างตำแหน่งสอดคล้อง. **24.2** อนุภาค = ชนิดของความแตกต่างที่ขนส่งได้. **24.3** แรง = ราคา
ของความไม่สอดคล้องในการแปล (curvature). **24.4** สี = retained quotient (triality `0,1,2`) ไม่ใช่สามสีตาม
ตัวอักษร. **24.5** confinement = ความเป็นไปไม่ได้ของผลอ่านเดี่ยวที่มี nonzero triality (ไม่มี invariant
standalone reader). **24.6** renormalization = การไหลของความสามารถในการแยกความแตกต่าง (`ρ_t(b)`) ไม่ใช่แค่
การวิ่งของ coupling.

---

## ส่วนที่ 25 — สรุปสุดท้าย
```
retained distinctions → reader equivalence → internal automorphisms
   → local transport and curvature → u(1)⊕su(2)⊕su(3) → representation information
   → invariant couplings → Z₃ triality quotient → closed retained surfaces
   → cost–entropy competition → confinement or string breaking → asymptotic neutral readout
```
> «Standard Model ในกรอบนี้ไม่ใช่รายการอนุภาคและแรงที่ถูกใส่ไว้ก่อน แต่เป็น**สถาปัตยกรรมของความแตกต่างที่
> ถูกขนส่ง เปลี่ยนชื่อ รวม ปิด และรักษาไว้ภายใต้ข้อจำกัดของผู้อ่าน**»

**ข้อสรุปที่แข็งแรงสุดปัจจุบัน:**
`ordered retained information ⇒ three-channel closure ⇒ SU(3) ⇒ Z₃ retained triality ⇒
information-theoretic confinement mechanism.`

**ยังต้องปิด:** chirality + matter spectrum + hypercharge + mass generation + continuum dynamics.

> **คำตัดสินซื่อสัตย์:** **Root-Native Standard-Model Architecture: Substantial Partial Closure** —
> *ไม่ใช่* Complete Standard Model Derivation.

---
*เอกสารนี้เป็นฐานอ้างอิงหลัก (canonical) เพื่อกันการดริฟกลับไปนำกฎฟิสิกส์ภายนอกมาเป็น premise โดยไม่ประกาศ
สถานะ. runnable witnesses + machine-status: `run_tests.py`, `CLAIM_BOUNDARY.json`, `STANDARD_MODEL_CLOSURE.md`,
`INDEX.md` (ในโฟลเดอร์เดียวกัน).*
