# TODO: พัฒนา readout_genesis Standard Model domain โดยใช้ information-discrete-math (idm)

> **31 รายการ**, จัดกลุ่มตามลำดับความสำคัญ: P0=4 (#1-4), P1=9 (#5-12, #30), P2=9 (#13-20, #29), P3=9
> (#21-28, #31) — ดูหัวข้อ "รายการเพิ่มเติม 29-31" สำหรับ 3 รายการท้ายที่มี target SM item ต่างจากรายการ
> ใกล้เคียงในลิสต์หลัก

---

## P0 — บล็อกเกอร์หลัก / ความเสี่ยงสูงสุด

### 1. ใช้ semiring matrix machinery ทั่วไปของ idm (Th_coqc) เป็นฐานความถูกต้อง + ฐานโค้ดของ mu4 trellis weight-enumerator DP

- **เป้าหมาย:** Item 35 (mu_4^admissible ผ่าน GF(3) linear code / trellis weight enumerator)
- **แหล่งอ้างอิง idm:** `tools/aggregate.py` — คลาส `Semiring` ทั่วไป (`oplus`/`otimes`), semiring สำเร็จรูป 6 ตัว (MIN_PLUS, MAX_PLUS, BOTTLENECK, MINIMAX, REACH, COUNT), ฟังก์ชัน `mat_mul(A,B,sr)`, `walk_count(A)`, `all_pairs(W,sr)`; กฎ distributivity ของ (⊕,⊗) ถูก machine-check ไว้ใน `formal/IDM_Tropical.v` (`tmin_assoc`/`tmin_comm`/`tmin_idem`, `minplus_distrib`, `maxplus_distrib`, `bottleneck_distrib` — Th_coqc, axiom-free, ยืนยันด้วย `coqc -q` + `Print Assumptions` แล้ว)
- **ขั้นตอนถัดไป:** สร้าง semiring แบบ polynomial-tracking (element = dict ของสัมประสิทธิ์ตาม weight, ⊕=บวกทีละพจน์, ⊗=convolution/shift weight) ให้เข้ากับ interface ของ `aggregate.py`; ปรับ `mu4_trellis_weight_enum.py` ให้แต่ละ layer เรียก `aggregate.mat_mul` แทน DP มือเขียน; อ้าง (หรือพิสูจน์ใหม่) polynomial-semiring distributivity lemma เป็นฐานความถูกต้องแทนการ "match brute force" เพียงอย่างเดียว
- **ความเสี่ยง/ข้อควรระวัง:** `IDM_Tropical.v` พิสูจน์ distributivity เฉพาะ min-plus/max-plus/bottleneck **เท่านั้น** — ยังไม่มีทฤษฎีบทสำหรับ COUNT/polynomial semiring — ต้องพิสูจน์ lemma ใหม่ก่อนอ้างว่า idm "รองรับอยู่แล้ว" (โค้ด `aggregate.py` reusable จริง แต่ formal backing ของกรณี polynomial ยังไม่มี)

### 2. ใช้ IDM_ReadoutMinimality.v เป็น "เช็คลิสต์เงื่อนไขบังคับ" (ไม่ใช่คำตอบ) สำหรับข้อโต้แย้งจำนวนเจเนอเรชัน

- **เป้าหมาย:** Item 2 (generation multiplicity — ทำไมต้องเป็น 3 พอดี, ต้องเริ่มจากศูนย์ ห้ามป้อนคำตอบ)
- **แหล่งอ้างอิง idm:** `formal/IDM_ReadoutMinimality.v` — `Theorem minimal_three_values`, `third_value_is_neutral`: total, involution-equivariant, non-degenerate sign readout ไม่สามารถแก้ได้ด้วยค่าที่แตกต่างกันน้อยกว่า 3 ค่า (Th_coqc, นามธรรมล้วน ไม่มีเนื้อหาฟิสิกส์, Qed, ไม่พบ Admitted/Axiom)
- **ขั้นตอนถัดไป:** สำหรับข้อเสนอ item-2 ใดๆ: (ก) เขียนกลุ่มสมมาตร G ที่กระทำบนโครงสร้าง branch/tape ที่เสนอ และ readout map r ให้ชัดก่อน; (ข) ตรวจว่า r เป็น total, G-equivariant, non-degenerate ตามเงื่อนไขของทฤษฎีบท **ก่อน** นับจำนวนค่าที่ถูกบังคับ ถ้าเงื่อนไขข้อใดไม่ผ่านให้ถือว่าไม่มีขอบเขตล่างที่บังคับจากกลไกนี้
- **ความเสี่ยง/ข้อควรระวัง:** ความเสี่ยง CRRC (Cross-Role Readout Contamination) **สูงมาก** — ย้าย proof PATTERN เท่านั้น ห้ามอ้าง "idm พิสูจน์ ≥3 ค่า" เป็นหลักฐาน "3 เจเนอเรชัน" โดยไม่สร้าง group/readout ของ SM ใหม่เองก่อน สูตร cardinality ทั่วไป (ดูรายการ #9-10) ยังเป็น conjecture ที่ยังไม่พิสูจน์ — กลไกนี้ให้ได้แค่ necessary-condition/lower-bound เท่านั้น ไม่ใช่ from-scratch proof ว่า =3 พอดี

### 3. ใช้ Retained Burden Algebra ของ RCP-Energy (⊗/⊕/lexmin) เป็นแม่แบบเชิงพีชคณิตสำหรับสืบทอด κ_ord/κ_inc/κ_rel/κ_cut (และ g_j/Δ_j/κ_j) จาก S_UF

- **เป้าหมาย:** Item 15 (primitive cost ratios ของ v1.10-v1.11 isotropic fixed point) และ Item 1 (g_j/Δ_j/κ_j จาก tape/intertwiner grammar จริง — บล็อกเกอร์เดียวกัน, ผ่าน 4 ความพยายามพิสูจน์ก่อนหน้าที่ถูก adversarially refute แล้ว)
- **แหล่งอ้างอิง idm:** `tools/retained_burden_algebra.py` — `BurdenOrder`, `RetainedBurden` (Fraction exact ล้วน ไม่มี float), `.extend()` (⊗), `retain_lesser()` (⊕=lexmin); `RCP_ENERGY_ARCHITECTURE.md` §4 (นิยาม burden 6 แกน) และ §7 (finite-minimality induction argument, base+step เหนือ tick-indexed histories, ยืนยันด้วย full enumeration 9,324/46,656 admissible 6-tick histories และ 96-tick independent-order replay ใน §8, tier **Th_coqc-elig ยังไม่พิสูจน์**)
- **ขั้นตอนถัดไป:** จำลอง 4 แกนต้นทุน (หรือ g_j/Δ_j/κ_j) เป็นแกนของ `RetainedBurden` แสดงว่า isotropic fixed point (v1.10-v1.11, largest root ของ polynomial ดีกรี 6) เป็นจุด lexmin-optimal ของ burden algebra ที่สร้างจาก S_UF เอง แล้วตรวจว่า finite-minimality induction argument ของ §7 ย้ายมาใช้พิสูจน์ "forced ไม่ใช่ choice" ได้หรือไม่
- **ความเสี่ยง/ข้อควรระวัง:** finite-minimality induction ยังไม่ Coq-proved (RCP_ENERGY_ARCHITECTURE.md §9 ระบุตรงๆ) — ให้เพียง template/finite_diagnostic ไม่ใช่ derivation แกน 6 ของ RCP-Energy สร้างมาสำหรับ energy scheduling ไม่ใช่ S_UF's rewrite-cost structure — transfer ได้แค่ container/เทคนิค ไม่ใช่ผลลัพธ์ และไม่ได้แก้สาเหตุที่ 4 ความพยายามก่อนหน้าถูก refute

### 4. ⚠️ ธง CRRC: IDM_Harvest.v มีทฤษฎีบท "k=3 จาก cyclic start-independence" ซึ่งเป็น**การ re-prove ในเครื่อง (local re-proof) ของข้อโต้แย้งสี (color) ที่ harvest มาจาก readout_genesis เอง** — คือกับดัก Cross-Role Readout Contamination ที่ `HANDOFF_NEXT_SESSION.md` ในโดเมนนี้ระบุไว้ตรงๆ

- **เป้าหมาย:** Item 2 (generation multiplicity)
- **แหล่งอ้างอิง idm:** `formal/IDM_Harvest.v` — `Theorem odd_from_cyclic_closure`, `Theorem least_nontrivial_odd_is_three` (บรรทัด ~26-36, Th_coqc, axiom-free, พิสูจน์ด้วย `lia` สั้นๆ) หัวไฟล์ระบุตรงๆ ว่า "⇒ the color number 3 / SU(3)" **และ**หัวไฟล์ (บรรทัด 2-3) ระบุด้วยว่าผลลัพธ์เหล่านี้ **"harvested from readout_genesis and re-proved locally"** — กล่าวคือนี่**ไม่ใช่**ข้อค้นพบที่เกิดขึ้นเอง/อิสระในอีก repo แต่เป็นสำเนาที่ถูกดึงมาจาก readout_genesis แล้ว re-prove ซ้ำในเครื่องของ idm เอง (ตามคำของไฟล์เอง ไม่ใช่การตีความ)
- **ขั้นตอนถัดไป:** **ห้ามอ้างผลสรุป k=3 กับ item 2 โดยตรงเด็ดขาด** (เพราะเป็นสำเนาของ argument ที่ readout_genesis ผลิตไว้เองอยู่แล้ว ไม่ใช่หลักฐานใหม่จากภายนอก) ใช้เฉพาะเป็นแม่แบบของ**ขั้นตอนที่ต้องทำอิสระ**: ตรวจว่า generation-index structure มีแนวคิด "cyclic closure" ของตัวเองที่แตกต่างออกไปหรือไม่ ถ้ามีให้สร้างข้อโต้แย้งใหม่ที่ตรวจ Retained-Degree Insufficiency ก่อนถือว่าเกี่ยวข้องกับ generations
- **ความเสี่ยง/ข้อควรระวัง:** ความเสี่ยงสูงสุดในลิสต์นี้เพราะล่อใจที่สุด — ตัวเลขเดียวกัน (3), machine-checked, อยู่ในชื่อทฤษฎีบทกลางๆ (H2) ไม่ติดป้าย "color argument" ตรงๆ แม้หัวไฟล์จะเปิดเผยที่มา/ความเชื่อมโยงกับ SU(3) ไว้แล้วก็ตาม ผู้อ่านที่ไล่ดูไฟล์นี้โดยไม่เห็นบริบทข้างต้นมีความเสี่ยงทำ CRRC ตามที่ `HANDOFF_NEXT_SESSION.md` เตือนไว้พอดี บันทึกไว้เพื่อ**เตือน ไม่ใช่แนะนำให้ใช้**

---

## P1 — สำคัญ ควรทำถัดไป

### 5. แทนที่เลขคณิต GF(3) มือเขียนใน mu4_kernel_code.py ด้วย GFRing(3) ของ idm

- **เป้าหมาย:** Item 35 (R=1 boundary matrix ที่ตรวจแล้วถูกต้อง และ R=2 kernel-basis dim=80)
- **แหล่งอ้างอิง idm:** `idm/kernel/poly/coeffring.py` class `GFRing` (บรรทัด ~82-118) — exact GF(p) = ℤ/pℤ, fail-closed primality check ตอน construct (ปฏิเสธ p ที่ไม่ใช่จำนวนเฉพาะ), หาร inverse ด้วย Fermat's little theorem (`pow(b, p-2, p)`) ไม่ใช่ float หรือ ad hoc mod
- **ขั้นตอนถัดไป:** แทน numpy `%3` + hardcoded inverse dict `{1:1,2:2}` ใน `gf3_rank_and_kernel_basis`/`build_boundary_matrix` (ยืนยันแล้วว่าอยู่จริงใน `mu4_kernel_code.py`, ไม่มีการ import idm เลย) ด้วยเรียกผ่าน `GFRing(3)` object แล้วรัน R=1 (2187 codewords, weight distribution ที่ตรวจแล้ว) เป็น regression oracle ก่อน retry R=2
- **ความเสี่ยง/ข้อควรระวัง:** เป็นแค่ correctness-hygiene ไม่แก้บล็อกเกอร์จริงของ R=2 (memory near-miss จาก basis-vector ordering) — `GFRing` ปัจจุบันเชื่อมกับ univariate polynomial subsystem ของ idm เท่านั้น (0 consumer อื่นจากการ grep) เป็นการ port มือ ไม่ใช่ integration ระดับ matrix ที่มีอยู่แล้ว

### 6. ขยาย rref/null_space ของ idm ให้ ring-generic เพื่อใช้กับ GFRing(3) สำหรับ Ker(∂2) ของ item 35 (⚠️ ข้อแก้ไข: ปัจจุบัน hardcode Fraction ทั้งหมด ไม่ใช่ ring-generic แล้ว)

- **เป้าหมาย:** Item 35 (R=2 retry, บล็อกจาก kernel-basis ordering; kernel dim 80, 648 edges ตาม MU4_INVESTIGATION_LOG.md)
- **แหล่งอ้างอิง idm:** `idm/exact.py` (`def rref` บรรทัด 363, `def null_space` บรรทัด 448); `idm/kernel/poly/linsolve.py` (`def rref` บรรทัด 59); `idm/_solve_domains/d10_matrix_extended.py` (kind `'rref'`/`'matrix_rank'`, Th_coqc-tagged แต่เป็นแค่ thin wrapper ที่เรียก `idm.exact.rref`/`matrix_rank` ตัวเดียวกัน — ยืนยันจากการอ่านไฟล์ตรง)
- **⚠️ ข้อแก้ไข:** ทั้ง `idm/exact.py::rref` และ `idm/kernel/poly/linsolve.py::rref` import `fractions.Fraction` ที่ module level ตรงๆ ไม่มี ring-interface parameter เลย ไม่เคย import `coeffring` (QRing/ZRing/GFRing) — คำกล่าวอ้างเดิมที่ว่า "อัลกอริทึมน่าจะ ring-generic อยู่แล้ว" **ผิด**: ต้องเขียน arithmetic operator ใหม่ทั้งหมด ไม่ใช่แค่ rewire ring parameter
- **ขั้นตอนถัดไป:** เพิ่ม `ring=QRing` parameter ให้ `idm/kernel/poly/linsolve.rref` (และ `idm/exact.py`'s rref/null_space), ปรับ pivot selection/division ให้เรียกผ่าน ring object, เพิ่ม `null_space_over(ring)` helper; ตรวจกับ GFRing(3) บนผลลัพธ์ R=1 ที่ verify แล้ว (dim 7, 2187 codewords) ก่อนลอง R=2
- **ความเสี่ยง/ข้อควรระวัง:** เป็นงานพัฒนาใหม่ทั้งหมด — idm ไม่มี Cuthill-McKee/bandwidth-reduction เลย (grep ยืนยัน 0 hits) ซึ่งเป็นบล็อกเกอร์จริงของ R=2 (ordering-driven memory near-miss) — งานนี้ให้แค่ฐาน exact-arithmetic ที่เชื่อถือได้ ไม่แก้ ordering เอง `d10_matrix_extended.py` ยืนยันแล้วว่าเป็นแค่ wrapper ที่เรียกฟังก์ชันเดียวกับ `linsolve.py`/`exact.py` โดยตรง จึงรวมเป็นรายการเดียวและเก็บไฟล์อ้างอิงทั้งหมดไว้ครบ

### 7. ใช้ทฤษฎีบท PSD/Laplacian ของ IDM_Keystone.v + IDM_Matrix.v เป็น structural lemma สำหรับ block kernel K_b

- **เป้าหมาย:** Item 10 (K_b, 4D correlation defect ε_t(b), เป้าหมายหลัก), Item 11 (σ_phys) และ Item 16 (spectral gap) — สองข้อหลังเป็นเป้าหมายรอง ขึ้นกับว่า K_b ตรงรูปแบบ Laplacian ทั่วไปจริงหรือไม่
- **แหล่งอ้างอิง idm:** `formal/IDM_Keystone.v` — `Theorem keystone_B_eq_I` (ΦᵀL_RΦ = Σw(Φi−Φj)², การประกอบ edge = พลังงาน weighted-Laplacian), `keystone_nonneg` (PSD-ness, บรรทัด 87); `formal/IDM_Matrix.v` §Laplacian (บรรทัด 93-139) — `laplacian_symmetric`, `laplacian_rowsum_zero`, `laplacian_ones_in_kernel` (ทั้งหมด Th_coqc, เหนือ Q, axiom-free, สร้างจาก L_R=D_W−W ตัวเดียวกับที่ READOUT_GENESIS_CORE.md E00.7 ใช้)
- **ขั้นตอนถัดไป:** ตรวจว่านิยามปัจจุบันของ K_b (ใน `full_block_closure_v0_7.py`/`InfoBlockCorrelation.v`) เป็น weighted graph Laplacian D_W−W บน block-adjacency ที่ประกาศไว้จริงหรือไม่ (ยังไม่ได้ตรวจอิสระในรอบนี้) ถ้าใช่ให้อ้างทฤษฎีบทเหล่านี้ตรงๆ แทนพิสูจน์ PSD/zero-mode ใหม่
- **ความเสี่ยง/ข้อควรระวัง:** พิสูจน์แค่ symmetric/PSD/zero-mode ทั่วไป **ไม่พิสูจน์ nonzero/uniform gap** (เนื้อหาเปิดจริงของ item 16) และไม่พิสูจน์ว่า string tension ไม่เป็นศูนย์จริงทางฟิสิกส์ (item 11) — สองอย่างนี้ต้องการ calibration/limit argument ที่ idm ไม่มีให้ เงื่อนไขการใช้ทั้งหมดขึ้นกับว่า K_b ตรงรูปแบบ Laplacian จริง ซึ่งยังไม่ได้ตรวจอิสระ

### 8. ใช้ twirl (Reynolds/isotropy projector) ของ IDM_Matrix.v เป็นกลไก collapse-to-scalar สำหรับ item 15/1

- **เป้าหมาย:** Item 15 (primitive cost ratios κ_ord/κ_inc/κ_rel/κ_cut จาก v1.10-v1.11 isotropic fixed point) — ป้อนกลับเข้าบล็อกเกอร์ของ item 1 ด้วย
- **แหล่งอ้างอิง idm:** `formal/IDM_Matrix.v` — `Definition twirl` (บรรทัด 152: `twirl n A := scalarM (trace n A / inject_Z (Z.of_nat n))`), `Theorem twirl_image_scalar` (บรรทัด 159-161: image เป็น scalar matrix c·I เสมอ), `trace_twirl` (บรรทัด 193) — Th_coqc, axiom-free, ไม่พบ Admitted/Axiom
- **ขั้นตอนถัดไป:** แสดง frame-mixing weight structure ของ SM เป็น n×n Mat ภายใต้ isotropy group ที่ประกาศไว้ แล้วอ้าง `twirl_image_scalar` เป็นทฤษฎีบทรับรองขั้นตอน collapse-to-scalar แทนการพิสูจน์ ad hoc ทีละอัตราส่วน
- **ความเสี่ยง/ข้อควรระวัง:** twirl บอกแค่ "ทำไม collapse ถึงเกิด" (ทำไม average ของ isotropy group ถึงยุบเหลือ scalar เดียว) **ไม่บอกว่าค่า scalar นั้นคือเท่าไร** — จะไม่ช่วยหาค่าตัวเลขจริงของ κ_ord/κ_inc/κ_rel/κ_cut เอง ให้แค่ formalize กลไกที่ใช้อย่างไม่เป็นทางการอยู่แล้ว

### 9. [คืนค่าที่หายไป] IDM_EquivariantReadout.v มี conjecture คาร์ดินัลลิตี้ทั่วไป (|V|_min = Σ[G:H]) ที่ยังไม่พิสูจน์ — โอกาสพัฒนาร่วมสองทางกับงาน item 2

- **เป้าหมาย:** Item 2 (generation multiplicity)
- **แหล่งอ้างอิง idm:** `formal/IDM_EquivariantReadout.v` — `equivariant_stabilizer_containment` (general G, Th_coqc, พิสูจน์แล้ว) และ `faithful_stabilizer_equality` (กรณี faithful action, Th_coqc, พิสูจน์แล้ว) แต่สูตรทั่วไป |V|_min=Σ[G:H] ถูกระบุตรงๆ ในคอมเมนต์ท้ายไฟล์ว่าเป็น **"Conjecture P1 (NOT proved here)"**
- **ขั้นตอนถัดไป:** เมื่อจะ formalize ข้อเสนอ item-2 ใดๆ ให้จำแนกก่อนว่ากลุ่มการกระทำ (group action) ที่ได้เป็น faithful หรือไม่ ถ้าใช่ ให้อ้าง `faithful_stabilizer_equality` ตรงๆ ถ้าไม่ใช่ ให้ธงว่าสูตรทั่วไปยัง "ต้องใช้แต่ยังไม่พิสูจน์" ในทั้งสอง repo — เป็นโอกาสสองทาง: ถ้าโครงสร้างของ SM (item 2) กลายเป็น non-faithful case ที่ต้องการสูตรทั่วไปจริง อาจเป็นแรงจูงใจให้ปิด conjecture ของ idm เองไปพร้อมกัน
- **ความเสี่ยง/ข้อควรระวัง:** สูตรทั่วไปเป็น conjecture ที่เปิดอยู่ในตัว idm เอง ไม่ใช่ผลลัพธ์ที่อ้างอิงได้ปิด — การใช้เกินกรณี faithful-action เดี่ยวๆ จะเป็นการ overclaim เอง (กลไกนี้แยกจากรายการ #2 เพราะมี concrete_next_action และ risk profile ต่างกัน — #2 คือ precondition checklist, รายการนี้คือ open conjecture ของ idm เองที่เป็นโอกาสประสานงานปิดร่วมกัน)

### 10. [คืนค่าที่หายไป] ใช้กลไก necessary-condition (NC1-NC3 + minimal_three_values) ของ idm เป็น lower-bound probe สำหรับ generation multiplicity พร้อมธง CRRC ชัดเจน

- **เป้าหมาย:** Item 2 (generation multiplicity — ต้องทำจากศูนย์ ห้ามป้อนคำตอบ)
- **แหล่งอ้างอิง idm:** `formal/IDM_EquivariantReadout.v` (บรรทัด ~55-90) — `equivariant_stabilizer_containment`/`faithful_stabilizer_equality`/`nondegenerate_value_moves` (NC1-NC3, ทั่วไปเต็มรูปแบบ ไม่มีสมมติฐาน finiteness); `formal/IDM_ReadoutMinimality.v` — `minimal_three_values` (กรณีฐาน Z2)
- **ขั้นตอนถัดไป:** สร้างกลุ่ม G ของ admissible re-description ที่กระทำบน generation slot **ขึ้นเองจากศูนย์** (ตามข้อกำหนด item 2 ที่ห้ามใช้งานบางส่วนก่อนหน้า) และคำนวณ Stab_X(x) สำหรับ generation-tape object ตัวแทน แล้วใช้ `faithful_stabilizer_equality` หาขอบเขตล่าง [G:Stab_X(x)] เป็นผู้สมัคร จากนั้นตรวจผ่าน Retained-Degree-Insufficiency diagnostic ของ SM domain เอง
- **ความเสี่ยง/ข้อควรระวัง:** ธง CRRC ชัดเจน — ห้ามนำไปใช้เป็นคำตอบ "ทำไม 3 เจเนอเรชัน" โดยไม่สร้าง admissibility square ของ group/object คู่นี้เองก่อน สูตร cardinality ทั่วไปของ idm (Σ[G:H_type]) ยังเป็น conjecture — กลไกนี้ (ทิศทาง necessary-condition, NC1-NC3) เป็น Th_coqc จริง แต่ให้ได้แค่ lower-bound/consistency check ไม่ใช่ from-scratch proof ว่า =3 (นี่เป็นกลไกที่**ต่างจากข้อ #4 อย่างมีนัยสำคัญ** — ทฤษฎีบทคนละตัว เส้นทางพิสูจน์คนละเส้น จึงไม่ใช่ CRRC ประเภทเดียวกับ IDM_Harvest.v โดยอัตโนมัติ แต่ยังต้องระวัง mis-transfer เท่ากัน)

### 11. ใช้ Orient predicate (IDM_Geometry.v) เป็นฐาน discrete substrate สำหรับเครื่องหมาย oriented determinant/Jacobian ของ chiral gauge measure

- **เป้าหมาย:** Item 14 (anomaly coefficients จาก oriented determinant/Jacobian จริง ไม่ใช่ calibrated)
- **แหล่งอ้างอิง idm:** `formal/IDM_Geometry.v` — `Orient(ax,ay,bx,by,cx,cy)` determinant + 8 กฎ (antisymmetry ภายใต้ vertex/basis swap, cyclic invariance, translation frame-independence, scale sign-preservation, coincident-vertex degenerate=0) — Th_coqc, axiom-free; `idm/_solve_domains/d04_exact_linear_algebra.py` (`@kind('matrix_determinant','Th_coqc')`, fraction-free Gaussian elimination สำหรับ n มิติทั่วไป)
- **ขั้นตอนถัดไป:** สร้างสะพานทดลอง — แปลง gauge orbit basis change สำหรับ rep content ขั้นต่ำ ({1,3,3bar}×{1,2}) เป็น rational matrix เรียก `matrix_determinant` ตรวจว่าเครื่องหมายเปลี่ยนตามกฎ swap/cyclic ของ Orient จริงหรือไม่ ก่อนพยายาม derive ทั่วไป
- **ความเสี่ยง/ข้อควรระวัง:** เป็น orientation predicate 2 มิติ (พื้นที่สามเหลี่ยมมีเครื่องหมาย × 2) **ไม่ใช่** fermion-determinant/Pfaffian จริง — เปรียบเทียบเชิงโครงสร้างเท่านั้น เสี่ยง CRRC สูงถ้าตีความ "orientation" ทางเรขาคณิตทับความหมายฟิสิกส์โดยไม่ระวัง

### 12. ใช้ Retained Readout Pullback (RRP) axis-moment/gradient identities คำนวณ ⟨Ξ⟩ เป็นค่าคาดหวังจาก partition function

- **เป้าหมาย:** Item 13 (⟨Ξ⟩ ≠ 0 จาก unified action, ไม่ใช่สมมติไว้)
- **แหล่งอ้างอิง idm:** `RCP_RETAINED_READOUT_PULLBACK_STANDALONE.md` §1, §6-7 — เอกลักษณ์ ∂log Z/∂θ=−E[T] แบบ finite exponential-family, retained-closure pass เดียว ไม่ใช้ autodiff tape/junction tree, cross-verified กับ finite-difference (worst |Δ|≈1.9e-10, verdict ACCEPT — committed check) และเทียบเพิ่มเติมกับ opt_einsum+Autograd (agreement ถึง 8.89e-16) ซึ่งเอกสารต้นทางระบุเองว่าเป็นการรันแยกต่างหากที่ **ยังไม่ commit เข้า CI** (ต้องมี `autograd`/`opt_einsum` เป็น optional dependency)
- **ขั้นตอนถัดไป:** แสดง finite truncation ของ S_UF (ตัวที่ใช้แล้วสำหรับ isotropic fixed point v1.10-v1.11) เป็น RRP-compatible finite exponential-family factor graph เรียก pullback อ่านค่า axis moment ของ Ξ โดยตรง เทียบกับ native readout เดิม (curvature/τ_c-based) ของ item 1 เป็น consistency check
- **ความเสี่ยง/ข้อควรระวัง:** เอกลักษณ์เชิงพีชคณิตของ RRP เป็น tier **Th_coqc-elig (ยังไม่ machine-checked)** และการตีความฟิสิกส์ติดป้าย **Dr (interpretive)** — ให้แค่ finite_diagnostic-tier numeric readout ภายใต้ truncation ที่ประกาศไว้ ไม่ใช่การพิสูจน์ว่า ⟨Ξ⟩≠0 ถูก**บังคับ** และสืบทอดความเสี่ยง physics-match เดียวกับที่เปิดเผยไว้แล้วสำหรับ item 1's M_n chain ถ้า weight ของ S_UF ยังไม่ถูก root-derive เองก่อน

---

## P2 — มีประโยชน์ ควรทำในลำดับถัดมา

### 13. ใช้ exact_eigenvalues / spectral_decomposition ของ idm เป็นขั้นก่อนหน้าเชิง finite-volume แบบเข้มงวดสำหรับข้ออ้าง spectral gap

- **เป้าหมาย:** Item 16 (uniform spectral gap เมื่อ volume/block-scale → infinity)
- **แหล่งอ้างอิง idm:** `idm/_solve_domains/d04_exact_linear_algebra.py` (kind `exact_eigenvalues` — Faddeev-LeVerrier characteristic polynomial + Sturm isolation, ค่า eigenvalue จริงเป็น algebraic object ไม่ใช่ float, HOLD แทนที่จะ approximate ถ้าเกิน budget); `idm/hilbert.py` Phase H1 `spectral_decomposition` (finite-dim Hermitian, tier finite_diagnostic/Th_coqc-eligible)
- **ขั้นตอนถัดไป:** สำหรับ K_b (item 10) ที่ instantiate ที่ volume จำกัดขนาดเล็ก สร้าง matrix ที่สอดคล้องกันแล้วเรียก `idm.solve('exact_eigenvalues', ...)` ให้ได้ spectral gap แบบ exact algebraic เป็นจุดข้อมูลหนึ่งในลำดับที่ศึกษาแนวโน้มว่า gap คงอยู่ห่างจากศูนย์เมื่อ volume โตขึ้นหรือไม่ — **ไม่ใช่** การพิสูจน์ infinite-volume limit
- **ความเสี่ยง/ข้อควรระวัง:** ให้ได้แค่จุดข้อมูล finite-volume exact เท่านั้น ไม่เคยให้ statement ระดับ infinite-volume ที่ item 16 ต้องการจริง (idm เอง fence เรื่องนี้เป็น +R-Open ถาวรใน HILBERT_PLUS_R_FRONTIER.md) ยังไม่ยืนยันว่า K_b แสดงเป็น matrix ขนาดที่ Faddeev-LeVerrier รับมือได้จริงหรือไม่

### 14. ใช้ IDM_Apriori.v เป็นแม่แบบ proof-pattern (ไม่ใช่ทฤษฎีบทที่อ้างได้ตรง) สำหรับ uniform spectral-gap sequence

- **เป้าหมาย:** Item 16 (uniform spectral gap)
- **แหล่งอ้างอิง idm:** `formal/IDM_Apriori.v` — `apriori_geometric_contracts`/`apriori_stable`/`richardson_apriori_stable` (Th_coqc, axiom-free): ถ้าลำดับมี ratio structure แบบ geometric ที่รู้ล่วงหน้า จะหด (contract) และ bound ได้โดยไม่ต้องสังเกตการหดจริงก่อน
- **ขั้นตอนถัดไป:** ตรวจก่อนว่าลำดับ spectral-gap-vs-volume ของ item 16 มี (หรือแสดงได้ว่ามี) รูปแบบ geometric/multiplicative โดยโครงสร้างหรือไม่ ถ้าใช่เท่านั้นจึงศึกษาโครงสร้างการพิสูจน์ (ไม่ใช่ตัว statement) ของ `IDM_Apriori.v` เป็นแม่แบบสำหรับ lemma ใหม่เฉพาะ SM
- **ความเสี่ยง/ข้อควรระวัง:** **นี่คือ CRRC-pattern อีกแบบหนึ่ง**: ทฤษฎีบทเหล่านี้เป็นเรื่อง numerical-refinement gap (Richardson extrapolation) ไม่ใช่ physical spectral gap — มีคำว่า "gap" ร่วมกันเท่านั้น หัวไฟล์เองก็ไม่ได้อ้างว่าใช้ข้ามโดเมนได้ ใช้ได้แค่แรงบันดาลใจของ proof-pattern เท่านั้น ต้องธงไว้ชัดเจนก่อนใช้

### 15. [คืนค่าที่หายไป] ใช้ Reynolds/twirl idempotent projector เป็น discrete Haar-measure stand-in สำหรับ gauge-invariant subspace ของ item 14/20

- **เป้าหมาย:** Item 14 (interacting chiral gauge measure) และรอง Item 20 (root-native chiral A_f)
- **แหล่งอ้างอิง idm:** `formal/IDM_Matrix.v` §13.4 — `twirl(n,A) := (tr A/n)·I` (isotropy Reynolds-operator projector), `twirl_idempotent` (idempotent, พิสูจน์แล้ว), `trace_twirl` (trace-preserving), `twirl_image_scalar` (image เป็น scalar line เป๊ะ) — ทั้งหมด Th_coqc, axiom-free
- **ขั้นตอนถัดไป:** generalize `twirl` จากกรณี full-symmetric-group/scalar ไปเป็น finite gauge group ที่เกี่ยวข้องกับ rep content ที่ประกาศไว้ (เช่น Z6/Z3 quotient) แล้วตรวจว่า idempotence/trace-preservation ยังคงอยู่สำหรับ averaging operator ที่ generalize แล้ว — เป็นข้อพิสูจน์ขั้นต่ำสุดก่อนเรียกผลลัพธ์ว่า "gauge measure" ได้
- **ความเสี่ยง/ข้อควรระวัง:** `twirl` ใน IDM_Matrix.v average เหนือ full symmetric/isotropy group ไปสู่ scalar เท่านั้น — **ยังไม่ใช่** group-average เหนือ finite gauge group G ใดๆ ไปสู่ G-invariant subspace ที่ไม่จำเป็นต้องเป็น scalar การ generalize เป็นงานใหม่ทั้งหมด มีแค่ proof pattern ของ idempotence/trace-preservation ที่ย้ายมาได้ตรงๆ (รายการนี้เป็นกลไกคนละตัวกับรายการ #8 — เป้าหมาย SM คนละข้อ: #8 คือ item 15/1, รายการนี้คือ item 14/20 — 2 โอกาสแยกกัน แม้ทั้งคู่อ้าง `twirl` เป็นกลไกร่วม)

### 16. ใช้ tropical (min-plus) all-pairs shortest-path semiring เป็นตัวแทน discrete minimal-area/Wilson-loop สำหรับ string tension

- **เป้าหมาย:** Item 11 (nonzero continuum string tension σ_phys)
- **แหล่งอ้างอิง idm:** `formal/IDM_Tropical.v` (`tmin_assoc`/`tmin_comm`/`tmin_idem`, `minplus_distrib` — Th_coqc, axiom-free, ยืนยันด้วย `coqc -q` + `Print Assumptions` แล้ว: "Closed under the global context"); `tools/aggregate.py` (`Semiring` class, `MIN_PLUS` constant, `all_pairs`, `mat_mul`, ใช้จริงในไฟล์)
- **ขั้นตอนถัดไป:** สร้าง weight matrix W บน finite lattice ที่เข้ารหัส plaquette/edge action cost สำหรับ Wilson-loop boundary ขนาดเล็ก (ใช้ lattice construction เดียวกับ mu4 exploration) เรียก `all_pairs(W, MIN_PLUS)` หา minimal-area surface ที่ขอบเขตนั้นแบบ exact ที่หลายขนาด loop แล้วตรวจว่า area/perimeter มีแนวโน้มเชิงเส้น (area-law signature) เมื่อ loop โตขึ้นหรือไม่
- **ความเสี่ยง/ข้อควรระวัง:** เป็น minimal-area combinatorial functional บน finite lattice เท่านั้น **ไม่ใช่** Wilson-loop expectation value จริงของ gauge theory (ซึ่งต้อง sum/average เหนือ configuration ที่ถ่วงน้ำหนักด้วย action ไม่ใช่แค่เส้นทาง cost ต่ำสุด) — เป็นแค่ T=0/saddle-point proxy ระดับ finite_diagnostic sanity check ไม่ใช่การพิสูจน์ σ_phys≠0

### 17. ใช้ Bellman-induction argument (§7-8 RCP-Energy) เป็นแม่แบบเชิงเทคนิคว่า ⟨Ξ⟩≠0 ถูก "บังคับ" ไม่ใช่แค่คำนวณได้

- **เป้าหมาย:** Item 13 (⟨Ξ⟩ ≠ 0 จาก unified action — derived ไม่ใช่ computed)
- **แหล่งอ้างอิง idm:** `RCP_ENERGY_ARCHITECTURE.md` §7 (บรรทัด 216-236, base-case + inductive-step เหนือ finite tick-indexed histories, tier Th_coqc-elig) และ §8 (บรรทัด 238-247, ยืนยันด้วย full enumeration 9,324/46,656 admissible 6-tick histories และ 96-tick independent-order replay ให้ผลตรงกัน)
- **ขั้นตอนถัดไป:** ลองแปลง "⟨Ξ⟩≠0" เป็นข้อเสนอ minimality/extremality เหนือ finite admissible-history space เดียวกับที่ใช้ derive isotropic fixed point v1.10-v1.11 แล้วตรวจว่า argument แบบ base-case+inductive-step คล้าย §7 พิสูจน์ว่า Ξ ห่างจากศูนย์เสมอสำหรับทุก admissible history ได้หรือไม่
- **ความเสี่ยง/ข้อควรระวัง:** เป็นการย้าย proof-TECHNIQUE เท่านั้น (finite induction เหนือ admissible histories) — argument ของ RCP-Energy เป็นเรื่อง burden-cost minimality ในโดเมน energy scheduling ไม่เกี่ยวข้องเชิงโครงสร้างกับ gauge-theory order parameter นอกจากรูปแบบ "finite induction เหนือ admissible histories" ที่ใช้ร่วมกัน argument เองยังเป็น Th_coqc-elig เท่านั้น (ยังไม่ Coq-proved)

### 18. อ้าง zero-fibre Dirichlet-energy iff-identity (ผ่าน external companion repo `zero-readout-certifies`) เป็นเงื่อนไข necessary-and-sufficient สำหรับ order parameter ที่ไม่เป็นศูนย์

- **เป้าหมาย:** Item 13 (⟨Ξ⟩≠0 derived from unified action, not assumed)
- **แหล่งอ้างอิง idm:** `docs/FORMAL_COMPANIONS.md` ส่วน "1. The zero fibre" (บรรทัด 34-77) — ทฤษฎีบทหลักจริงๆ อยู่ใน **external companion repo `zero-readout-certifies`** (DOI 10.5281/zenodo.21665100) **ไม่ใช่**ใน `formal/` ของ repo นี้เอง — ระบุเอกลักษณ์ I_g(Φ)=0 ⟺ Φ คงที่บนทุก connected component
- **ขั้นตอนถัดไป:** ตรวจว่า order parameter Ξ ของ SM ใน S_UF แสดงเป็น (หรือ reduce เป็น) quadratic form แบบ Dirichlet-energy บนโครงสร้าง graph/tape ที่ตรงกับนิยาม I_g(Φ) ได้หรือไม่ ถ้าได้ ใช้เงื่อนไข iff นี้ลดปัญหาเป็น "แสดงว่า Φ ไม่คงที่บน component ใดๆ" แทนการ derive แบบเปิดกว้าง
- **ความเสี่ยง/ข้อควรระวัง:** ทฤษฎีบทที่ต้องพึ่งพาอยู่ใน **repo ภายนอกที่ยังไม่ได้เปิดตรวจจริงในรอบนี้** — ต้องถือว่าเป็นแค่ pointer ที่ยังไม่ verify จนกว่าจะเปิด repo นั้นตรวจเอง เก็งกำไรด้วยว่า Ξ จะ reduce เป็นรูปแบบ quadratic-form นี้ได้จริงหรือไม่ ยังไม่ได้ลองแปลง

### 19. รับรอง numeric chain λ_j=e^(−Δ_j^eff)/Π0 ด้วย certified exp/geometric-series ของ idm (⚠️ ข้อแก้ไข: ชื่อทฤษฎีบทอ้างผิด 2 ใน 4)

- **เป้าหมาย:** Item 1 (order-spectrum audit numeric chain: M_n → Π0 → ORDERED_READY → r_star → v_native)
- **แหล่งอ้างอิง idm:** `idm/certified.py` (re-export `exp_certified`/`geom_series_certified` จาก `tools/certified_readout.py`, สัญญา `Readout(q, bound, status, reason)`: CERTIFIED เมื่อมี bound ที่พิสูจน์แล้ว หรือ HOLD ถ้าเงื่อนไขไม่ผ่าน ไม่เดา); backed by `formal/IDM_Certified.v`
- **⚠️ ข้อแก้ไข:** ชื่อที่ถูกต้องคือ `geom_certified_identity` (Theorem, บรรทัด 31) และ `geom_certified_defect` (Corollary ที่ derive จาก `geom_certified_identity` โดยตรง, บรรทัด 44) — **ไม่ใช่** `geom_series_certified_identity`/`geom_series_certified_defect` ตามที่เคยอ้าง (คำว่า "series" ไม่มีอยู่ในชื่อจริง แต่ทั้งคู่มี counterpart ที่ถูกต้องในไฟล์ ไม่ใช่ไม่มีอยู่เลย) `geom_majorant_tail` (บรรทัด 64) เป็นทฤษฎีบทอีกตัวที่เกี่ยวข้อง (tail-bound แยกจาก identity/defect) ส่วน `exp_tail_certified` (บรรทัด 142) และ `exp_term_ratio` (บรรทัด 132) ถูกต้องตามที่อ้างไว้เดิม
- **ขั้นตอนถัดไป:** ตรงจุดที่ M_n/Π0 pipeline คำนวณ exponential decay rate หรือ geometric-series-shaped aggregation ให้เรียก `idm.certified.exp(Delta_j_eff, eps)` (หรือ `geom_series`) พร้อมพก bound ที่ได้ไปด้วยในเอกสารประกอบ chain โดยใช้ชื่อทฤษฎีบทที่ถูกต้อง
- **ความเสี่ยง/ข้อควรระวัง:** ไม่ช่วย derive Δ_j หรือ M_n เอง (บล็อกเกอร์ P0 จริงของ item 1) — ยกระดับแค่ numeric-honesty tier ของการคำนวณที่สร้างจาก input ที่ CALIBRATED ไม่ใช่ root-derived อยู่แล้ว ความล้มเหลวเชิงฟิสิกส์ที่เปิดเผยไว้ 3 จุด (74%/74%/94% deviation) ยังไม่ถูกแก้ เพราะเป็นเรื่อง physical correctness ไม่ใช่ numeric-bound tightness

### 20. ใช้ resolved_count_below/count_below_banded เป็นหลักฐาน finite-volume สำหรับแนวโน้ม spectral gap (⚠️ ข้อแก้ไข: overclaim ระดับ Th_coqc backing)

- **เป้าหมาย:** Item 16 (uniform spectral gap)
- **แหล่งอ้างอิง idm:** `retained_spectral/inertia.py` (`count_below_banded`/`resolved_count_below`, Sylvester-inertia sign-count ผ่าน banded LDLᵀ); `formal/IDM_Schur.v` (`schur_congruence_00..11`, `diag_inertia_additive`)
- **⚠️ ข้อแก้ไข:** `IDM_Schur.v` machine-check congruence เฉพาะกรณี **2×2 node เดียว** เท่านั้น (หัวไฟล์เองระบุว่า general n-block/banded case เป็น "declared next step" ยังไม่ทำ) และ **Sylvester's law of inertia** (ที่ congruence รักษา sign-count ไว้จริง) **ยังไม่พิสูจน์**ในไฟล์นี้ — ไฟล์เองติดป้าย "+R-Open, cited not proved" ไว้ตรงๆ ส่วน `inertia.py` เองก็ประกาศ tier **finite_diagnostic** ไม่ใช่ Th_coqc เต็มรูปแบบตามที่เคยอ้าง
- **ขั้นตอนถัดไป:** ถ้า K_b ของ SM จัดเป็น banded form ได้ที่ block size ที่เพิ่มขึ้นเรื่อยๆ รัน `resolved_count_below` ที่ threshold gap ผู้สมัคร ข้าม volume sequence แล้วบันทึกช่วง certain/unresolved ที่แต่ละ volume เป็นหลักฐาน finite_diagnostic ของความเสถียร/การเลื่อนของ gap
- **ความเสี่ยง/ข้อควรระวัง:** ให้ได้แค่หลักฐานแนวโน้มเชิงตัวเลขระดับ finite-volume เท่านั้น ไม่มีวันปิด item 16 ได้ (idm fence infinite-dimensional spectral theory เป็น +R-Open ถาวร) ยังต้องตรวจว่า K_b เป็น banded/reorderable ได้จริงหรือไม่ด้วย

---

## P3 — มีศักยภาพแต่เก็งกำไรสูง / ไม่ actionable ทันที

### 21. RCP (resource preflight + lineage digest) สำหรับ oriented determinant/Jacobian contraction

- **เป้าหมาย:** Item 14 — **แหล่งอ้างอิง idm:** `tools/retained_contraction_protocol.py`, `RETAINED_CONTRACTION_PROTOCOL.md` (สัญญา DECLARE/MAP/ADMIT/PREFLIGHT/EXECUTE/CERTIFY/VERDICT/TIER, SHA-256 lineage digest) — เก็งกำไรสูง RCP เองประกาศ tier `finite_diagnostic` ไม่ใช่ correctness proof ของ contraction ที่ wrap; ไม่มีอะไรในไฟล์อ้างถึง item 14 โดยตรง เป็นแค่การ application ที่เสนอ

### 22. exact_eigenvalues/characteristic_polynomial สำหรับ anomaly coefficient แบบ exact

- **เป้าหมาย:** Item 14 — **แหล่งอ้างอิง idm:** `idm/kernel/poly/eigen.py` (`characteristic_polynomial` บรรทัด 39 ผ่าน Faddeev-LeVerrier, `real_eigenvalues` บรรทัด 58 ผ่าน Sturm bisection, Fraction ล้วนไม่มี float); wired ผ่าน CHANGELOG.md WP13 Increment 1 — เป็นแค่ numerical-hygiene upgrade ไม่แก้เนื้อหาเปิดจริงของ item 14 (derive chiral measure/Jacobian เอง)

### 23. idm.continuum.Continuum เป็นสัญญา tier-honest สำหรับ regulator-independence

- **เป้าหมาย:** Item 26 (P2 ใน SM backlog เอง, deferred อยู่แล้ว) — **แหล่งอ้างอิง idm:** CHANGELOG.md [1.4.x] entry `idm.continuum.Continuum` (บรรทัด 334-355), `formal/IDM_Continuum.v` (`gap_subadditive`, `const_gap_zero`, Th_coqc, axiom-free) — ยืมวินัยการรายงาน (CERTIFIED/finite_diagnostic/HOLD) ไม่ใช่ derivation จะรายงาน HOLD จนกว่า SM domain จะพิสูจน์ tail bound ของ regulator sequence เอง

### 24. refine_stable เป็นแม่แบบ certificate เสถียรภาพ (⚠️ ข้อแก้ไข: ไม่ใช่ `integral_nd` — `integral_nd` อยู่ใน `tools/certified_readout.py`/THEOREM.md §7 ไม่ใช่ `IDM_Certified.v`)

- **เป้าหมาย:** Item 26 (P3-deferred อยู่แล้วใน SM backlog เอง) — **แหล่งอ้างอิง idm:** `formal/IDM_Certified.v::refine_stable` (บรรทัด 289, Th_coqc, axiom-free: (1-ρ)·|tailsum s N M| ≤ |s N|) — grep ยืนยันว่า `integral_nd`/n-D/tensor **ไม่ปรากฏเลย**ใน `IDM_Certified.v` ต้องอ้าง `tools/certified_readout.py`/THEOREM.md §7 สำหรับ wrapper มิติ n จริงๆ ไม่ใช่ไฟล์นี้ พิสูจน์แค่ stability ของ refinement sequence ไม่ใช่ regulator-independence ของทฤษฎีที่ได้

### 25. Schur/boundary-congruence sign-count เป็นตัวตรวจ basis-invariance ของ anomaly coefficient

- **เป้าหมาย:** Item 14 — **แหล่งอ้างอิง idm:** `formal/IDM_Schur.v` (บรรทัด 24-91, `schur_congruence_00..11` เหนือ Q, Th_coqc) — ทฤษฎีบทหลัก (Sylvester's law of inertia) **ยังไม่พิสูจน์**ในไฟล์ (ติดป้าย "+R-Open, cited not proved" เอง) ใช้ได้แค่ sanity check ของเล่นระดับ 2×2 ไม่ใช่การพิสูจน์ basis-invariance ทั่วไป

### 26. Balanced Retained-Cut Fusion (RCF) scaling benchmark เป็น infrastructure probe

- **เป้าหมาย:** Item 16 — **แหล่งอ้างอิง idm:** `RCP_NATIVE_RETAINED_FOLD_ARCHITECTURE.md` §5.7 (บรรทัด 326-429, d=9,w=8: native RCF 3.982ms เทียบ cached-plan JT 12.088ms/cold-plan JT 12.307ms, tier finite_diagnostic benchmark, FTCC core Th_coqc) — ล้วนเป็นเรื่อง computational scaling ไม่บอกอะไรเรื่องว่า gap สม่ำเสมอหรือหายไปเมื่อ volume โต

### 27. "permanent +R-Open fencing" discipline ของ Hilbert work เป็นรูปแบบความซื่อสัตย์ที่จำเป็นสำหรับ item 17

- **เป้าหมาย:** Item 17 (full interacting Lorentz continuum) — **แหล่งอ้างอิง idm:** `HILBERT_PLUS_R_FRONTIER.md` (frontier table + permanence clause), `HILBERT_MATHEMATICAL_CORE_ROADMAP.md` §2 (infinite-dim spectral theorem ประกาศเป็น +R-Open **ถาวร** ไม่ใช่เป้าหมายอนาคต) — ย้าย discipline เอกสารเท่านั้น ไม่ใช่เครื่องมือ/เทคนิคคำนวณ ไม่นับเป็น "ความคืบหน้า" ของ item 17 เอง

### 28. WP13 backlog ของ idm (exact eigenspace/Jordan form ยังไม่มี) สะท้อนช่องว่างเดียวกับ item 16

- **เป้าหมาย:** Item 16 — **แหล่งอ้างอิง idm:** `BACKLOG.md` บรรทัด 245-251 (WP13: exact eigenspaces, generalized eigenspaces, Jordan normal form, spectral decomposition ที่คืน exact object จริง — ทั้งหมดยังเป็น TODO) — จุดร่วมสำหรับ joint-prioritization ไม่ใช่เครื่องมือสำเร็จรูป (สะท้อน Scalar-Eigenmode Reduction Error ที่ READOUT_GENESIS_CORE.md เตือนไว้จากฝั่งคณิตศาสตร์ของ idm เอง)

---

## รายการเพิ่มเติม 29-31

รายการเหล่านี้ผ่านการตรวจสอบไฟล์ต้นทางโดยตรงเช่นเดียวกับรายการอื่น แต่มี target SM item ที่ต่างจากรายการ
ใกล้เคียงในลิสต์หลักอย่างมีนัยสำคัญ จึงแยกเป็นรายการของตัวเอง (#21 ผูกกับ item 14 แต่ #30 นี้ผูกกับ item 35
โดยตรง ซึ่งเป็นคนละ blocker; #27 ผูกกับ item 17 แต่ #31 ผูกกับ item 13/15 ซึ่งเป็นคนละเป้าหมาย)

### 29. ใช้ `groebner_basis` kind ของ idm (exact-CAS) ค้นหาคำตอบทั้งหมดของระบบข้อจำกัด anomaly-cancellation/rep-content

- **เป้าหมาย:** Item 12 (P1) — uniqueness ของ matter skeleton บน representation ที่รับได้ทั้งหมด ไม่ใช่แค่ alphabet ขั้นต่ำที่ประกาศไว้ `{1,3,3bar}×{1,2}`
- **แหล่งอ้างอิง idm:** `idm/_solve_domains/d04_exact_linear_algebra.py`, `@kind("groebner_basis", "exact")` (บรรทัด 66, function `_gb`) — Buchberger-algorithm Gröbner basis computation เหนือ ℚ, HOLD บน parse error/budget-exceeded — ยืนยันจากการอ่านไฟล์จริง: "real Buchberger-algorithm Gröbner basis computation... parses input polynomials over ℚ, computes reduced_groebner"
- **ขั้นตอนถัดไป:** จัดสูตร anomaly-cancellation + admissibility conditions ที่ใช้ใน v1.5 hypercharge derivation เป็น polynomial system ในตัวแปรไม่รู้ค่า (rep multiplicities, charges) แล้วรัน `idm.solve({'kind': 'groebner_basis', ...})` เพื่อได้คำอธิบาย exact ของ solution set ทั้งหมด ตรวจว่า declared minimal alphabet เป็นคำตอบเดียวหรือไม่
- **ความเสี่ยง/ข้อควรระวัง:** ยังไม่ยืนยันว่า groebner_basis รองรับ inequality/positivity side-conditions บน charges (รองรับแค่ polynomial equality โดยธรรมชาติ) tier คือ 'exact' ตาม tag ของ idm เอง ไม่ใช่ Th_coqc — การตรวจสอบพบว่า "การพิสูจน์ว่าปัญหานี้ formalize เป็น polynomial ideal จำกัดตัวแปรได้จริงและ Buchberger จะ terminate/tractable ยังไม่ได้ตรวจสอบจากไฟล์นี้อย่างเดียว"

### 30. ใช้วินัย PREFLIGHT resource-certificate ของ RCP ผูกตรงกับปัญหา near-miss หน่วยความจำของ mu4 R=2 trellis (ไม่ใช่ item 14 ตามรายการ #21)

- **เป้าหมาย:** Item 35 — R=2 retry (486 plaquettes, kernel dim=80) ที่ถูกบล็อกด้วย RSS near-miss 2,132MB โดยไม่มี rigorous pre-execution memory bound (นี่คือรายการเดียวในลิสต์ทั้งหมดที่ผูกตรงกับ blocker จริงของ item 35 — ต่างจากรายการ #21 ซึ่งผูกกับ item 14)
- **แหล่งอ้างอิง idm:** `tools/retained_contraction_protocol.py` — `RCPDeclaration` (max_work_tokens, max_peak_elements), `plan_contraction()`, `preflight_contraction()` (บรรทัด 314-384) — ยืนยันจากการอ่านไฟล์จริง: "docstring literally says 'Fail closed before tick 0 if path or dominant resources are inadmissible'... `preflight_contraction()` returns `Verdict(BLOCK, ...)` with explicit reason if bound exceeded, BEFORE any execution"
- **ขั้นตอนถัดไป:** ก่อน retry R=2 (หลัง Cuthill-McKee basis reordering ตามแผนเดิมของ mu4 investigation log) ห่อขั้นตอน trellis DP state-generation ด้วย RCP-style preflight: คำนวณ predicted peak retained-state count จาก reordered basis-vector overlap graph's bandwidth เทียบกับ declared memory budget แล้ว BLOCK พร้อม diagnostic ถ้าเกิน bound
- **ความเสี่ยง/ข้อควรระวัง:** การตรวจสอบยืนยันแค่ว่ากลไก PREFLIGHT ของไฟล์เองทำงานตามที่อธิบาย ("verified-by-reading confirmation of the module's mechanism as written") — ไม่ได้ทดสอบว่า apply กับ mu4 R=2 trellis จริงจะป้องกัน near-miss ได้จริงหรือไม่ (เป็น downstream application claim แยกต่างหาก) preflight bounds เองเป็น tier finite_diagnostic ไม่ใช่ Th_coqc-proved

### 31. อ้างอิง backlog การ formalize admissible-elimination-path ของ `RCP_ARCHITECTURE.md` §8 เป็น methodology template สำหรับ item 13/15 (ไม่ใช่ item 17 ตามรายการ #27)

- **เป้าหมาย:** Item 13 (⟨Ξ⟩≠0 derived from unified action) และ Item 15 (primitive cost ratios จาก S_UF) — ทั้งคู่ต้องการแนวคิด "rewrite-cost ที่คำนวณตาม path ต่างกันแต่ยัง admissible ต้องให้ผลตรงกัน" (order-invariance) ซึ่งเป็นคนละ target จากรายการ #27 ที่ผูกกับ item 17 (Lorentz continuum)
- **แหล่งอ้างอิง idm:** `RCP_ARCHITECTURE.md` §8 "Next mathematical layer" (บรรทัด 399-411) — backlog 6 ขั้นตอนที่ยังไม่ทำ: define finite factors/scopes ใน Coq, พิสูจน์ว่า admissible elimination step หนึ่งขั้นรักษา boundary readout, พิสูจน์การรักษาไว้ด้วย induction ตลอด admissible path, define reverse program, พิสูจน์ unary-adjoint moment identity, bind Python lineage serialization — ยืนยันจากการอ่านไฟล์จริง: "contains exactly the quoted 6-step declared-not-yet-done backlog verbatim... explicitly frames this as not-yet-done"
- **ขั้นตอนถัดไป:** เมื่อ formalize cost-ratio derivation ของ item 15 ให้จัดโครง proof obligation เป็น "boundary-readout invariance under admissible elimination order" แบบเดียวกับที่ §8 อธิบาย พิจารณาว่าการปิดจบ backlog นี้ก่อนใน idm จะให้ Coq lemma shape ที่ transfer มาใช้กับ SM domain ได้โดยตรงหรือไม่
- **ความเสี่ยง/ข้อควรระวัง:** ทั้งสองฝั่งยังไม่ปิดจบ (backlog เปิดอยู่ในตัว idm เอง) — เป็นโอกาส "ทำงานเปิดชิ้นเดียวกันครั้งเดียวแล้วแบ่งปันกัน" ไม่ใช่ "ใช้ผลลัพธ์ที่มีอยู่แล้ว" ความเชื่อมั่นในการ transfer ได้จริงต่ำจนกว่าฝั่งใดฝั่งหนึ่งจะปิดจบจริง

---

## ตัดออก (dropped)

ไม่มีรายการที่ถูกตัดออกเพราะไฟล์ที่อ้างถึงไม่มีอยู่จริง — ทุกไฟล์/ทฤษฎีบท/ฟังก์ชันของ idm ที่อ้างในเอกสารนี้
ตรวจสอบแล้วว่ามีอยู่จริงในการอ่านไฟล์ตรง **ยกเว้นรายการ #18** ซึ่งทฤษฎีบทหลักอยู่ใน external companion
repo (`zero-readout-certifies`) ที่ยังไม่ได้เปิดตรวจในรอบนี้ — ระบุไว้ชัดเจนในรายการนั้นเองว่าเป็น pointer
ที่ยังไม่ verify ไม่ใช่ผลที่ยืนยันแล้ว

## หมายเหตุระเบียบวิธี

ทุกรายการในเอกสารนี้อ้างอิงไฟล์ต้นทางใน `information-discrete-math` ที่ตรวจสอบแล้วว่ามีอยู่จริงและทำงาน
ตามที่อธิบาย (อ่านไฟล์โดยตรง ไม่ใช่จากคำอธิบาย/สรุปเพียงอย่างเดียว) 4 รายการ (#6, #19, #20, #24) มีการแก้ไข
คำกล่าวอ้างให้ตรงกับไฟล์จริง (ชื่อทฤษฎีบทผิด, ที่มาไฟล์ผิด, หรือ overclaim ระดับ Th_coqc backing) รายการ #4
(IDM_Harvest.v) ระบุ provenance ตรงตามหัวไฟล์ต้นทาง: เป็น local re-proof ที่ harvest มาจาก readout_genesis
เอง ไม่ใช่ข้อค้นพบอิสระในอีก repo — ระดับความเสี่ยง (P0, ห้ามอ้าง k=3 กับ item 2) คงเดิม
