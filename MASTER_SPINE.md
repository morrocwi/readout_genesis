# Master Spine — root to Clay, one line, no branches

> Tier: `Dr` (architectural map, not a proof). This is a **pointer document**: it names where each
> stage already lives (or doesn't yet) across `toledo`, `information-discrete-math`, and this repo.
> It restates no proof and asserts no Clay result. Readout-not-truth applies here like everywhere
> else in this repo: this map is itself a finite, dated readout of a moving codebase, not a fixed
> truth — see the "Last synced against" line before trusting any row.

## Why this file exists

The programme accumulated Toledo codes, Genesis sections, and Coq proofs across several repos with
no single place showing how they chain together end to end. This file is that place. It is
authoritative for the *shape* of the chain; each repo it points at stays authoritative for its own
content.

**Founder's architectural ruling (binding on every Clay-lane repo):** P vs NP, Navier-Stokes,
Yang-Mills, and every other Clay-adjacent lane are **leaf nodes** that plug in only after
`Domain-Specific Bridge`. No lane may grow its own separate root. A lane's job is to instantiate
this spine's generic objects (`F`, `Q`, `E_Q`, `ρ`, the bottleneck `B_i/A_i`, `W_Q`) concretely for
that domain, then connect through the *same* capacity/RDLB/weld-defect machinery already on this
spine — never invent parallel machinery. Before starting new Clay-lane work, check which spine node
it instantiates; if it doesn't instantiate one, it is scope creep on this architecture, not a new
foundation.

## The spine, three renderings

**Full technical form:**

Difference → Order/History → Retention → Retained Structure → Admissible Dynamics `F` →
Question `Q` → Reader/Experiment `E_Q` → Future Distinguishability → Reader Equivalence `~_Q` →
Domain Quotient `D_Q = S/~_Q` → Quotient Dynamics `F_Q^#` → Candidate Representation `ρ` →
Sufficiency (`ker ρ ⊆ ~_Q`) → Constructive/Semantic Firewall → Finite Resource Model →
Finite Bottleneck (`ΔO_i = B_iA_i`) → Blind Space (`K_N = ⋂_i ker A_i`) → Accumulated Capacity
Bound → Reader–Domain Lower Bound → Early Collapse / Weld Defect → Domain-Specific Bridge →
Clay Problem Target → Global Closure / Refutation.

**Genesis-language compression:**

Difference → History → Retention → Structure → Dynamics → Question → Readout → Equivalence →
Quotient → Domain → Sufficiency → Capacity → Lower Bound → Defect → Clay.

**Symbol-only DAG:**

`δ → F → Q → R_Q → ~_Q → D_Q → ρ → Suff → Bottleneck → RDLB → Defect → Clay`

## Anchor equations riding on the spine

| Node | Equation |
|---|---|
| Difference | `a ≠ b` |
| Admissible Dynamics `F` | `S_{n+1} = F(S_n, u_n, ...)` |
| Reader Equivalence `~_Q` | `s ~_Q t ⟺ ∀E∈E_Q: E(s)=E(t)` |
| Domain Quotient | `D_Q = S/~_Q` |
| Quotient Dynamics | `q_Q∘F = F_Q^#∘q_Q` (informal reading — see connection table for the exact formal statement) |
| Sufficiency | `ker ρ ⊆ ~_Q` |
| Constructive/Semantic Firewall | `A_con ⊆ A_sem` |
| Finite Bottleneck | `ΔO_i = B_iA_i` |
| Blind Space | `K_N = ⋂_{i=1}^N ker A_i` |
| Accumulated Capacity Bound | `codim K_N ≤ Σ_i m_i` |
| Reader–Domain Lower Bound | `K_N ∩ W_Q = {0} ⟹ dim W_Q ≤ Σ_i m_i` |
| Early Collapse / Weld Defect | `available capacity < required domain distinction ⟹ insufficient reader ⟹ weld defect` |

## Connection table (last verified 2026-09-13)

Pointers only — read the cited object for the real statement, never trust this row alone.

| Spine node | Object | File : identifier | Tier / status |
|---|---|---|---|
| Difference | Genesis root primitive | `toledo` `registry/genesis_root.json`, code `EQ-001` | root |
| Admissible Dynamics `F` | MQ.08 stepper | `readout_genesis/READOUT_GENESIS_CORE.md` (Part II.1; `F (MQ.08 stepper) ≡ {q_D : q_D∘F=F#_D∘q_D}`) | `Th_coqc` (δ_R⊢L_R) / `Dr` (F) |
| Reader Equivalence `~_Q` | **CAN-007** / `weld/M.03.v1` | `toledo` `registry/CANONICAL.json` | `Definition` / `current` |
| Quotient Dynamics `F_Q^#` | **CAN-006** / `weld/M.02.v1`; concretely realized as `T4b_quotient_commuting_square` | `information-discrete-math/formal/IDM_ReaderDomainFoundation.v` | Toledo: `Definition`; T4b: `Th_coqc`, axiom-free |
| Candidate Representation `ρ` / Sufficiency | `T5_sufficiency_kernel_inclusion` | `information-discrete-math/formal/IDM_ReaderDomainFoundation.v` | `Th_coqc` |
| Sufficiency (Toledo side, no-early-collapse) | **CAN-034** / `weld/E.06.v1` | `toledo` `registry/CANONICAL.json` | `Definition` / `current` |
| (factorization companion) | **CAN-165** / `EQ-002/M.01.v1` | `toledo` `registry/CANONICAL.json` | `Definition` / `current` |
| Constructive/Semantic Firewall | `A_con_subseteq_A_sem`, `constructive_closure_invariant` | `information-discrete-math/formal/IDM_ReaderDomainFoundation.v` | `Th_coqc` |
| Finite Bottleneck `ΔO_i=B_iA_i` | **CAN-054** / `EQ-015/H.06.v1` | `toledo` `registry/CANONICAL.json` | `Definition` / `unverified` (rank-bound sub-claim, PR #41) |
| Blind Space, Accumulated Capacity, RDLB, Early Collapse | **in progress** — abstract skeleton merged (`RDLB_T1_accumulation_bound`, `RDLB_T2_round_bound`, `RDLB_W_capacity_deficit_witness`); the finite-bottleneck instantiation (`K_N`, kernels, codimension bound) not yet merged | `information-discrete-math/formal/IDM_ReaderDomainFoundation.v` | `Th_coqc` (abstract layer only) |
| Early Collapse / Weld Defect | **CAN-065** / `weld/H.06.v1` | `toledo` `registry/CANONICAL.json` | `Definition` / `current` (a definition of defect, not yet a theorem computing when it's nonzero) |
| Domain-Specific Bridge, Clay Problem Target | none — by design, not yet built for any lane | — | — |

**Known open joins** (architecturally intended, not yet literally connected in Coq — closing these
is tracked as the Foundation's own six-gap list, see
`information-discrete-math`'s `docs/READER_DOMAIN_FOUNDATION_V1.md`):
- `EqOf`-family reader algebra and `FutureEq`/quotient-dynamics are the same idea by design but no
  theorem in `IDM_ReaderDomainFoundation.v` yet states `EqOf(generated future experiments) ⟺ FutureEq`.
- `T5`'s abstract representation `ρ` is never literally unified with `FutureEq`/`~_Q` from the
  earlier section of the same file.
- `T4b_quotient_commuting_square` proves a pointwise `iff` on class membership, not a literal
  function equality `q∘F=F#∘q` — the informal spine equation above is the reading, not the formal
  statement; see the file's own precision note.

## Not a Toledo code, not (yet) a Coq theorem

This spine is a composition map over objects that mostly already exist (or are in progress) — it is
not itself a single equation Toledo's schema is built to register, and several of its joins are not
yet even connected inside the objects that exist (see "Known open joins" above). Registering it as
a Toledo code now would register a claim about connections that don't yet hold formally.

There is a genuine future formalization task hiding in it: an actual Coq "spine assembly" corollary
that composes the already-proved pieces into one literal end-to-end statement once they exist and
are unified at each join. That is downstream of, not separate from, closing the Foundation's six
open gaps and completing the finite-bottleneck RDLB section — treat them as the same task, not two.

## Last synced against

- `toledo` @ `db68a778e3eb94565cb5cff36b0c1fc0078a54f7`
- `information-discrete-math` @ `f56e73f512598587d2db9cea920af135558c35bc`
- `readout_genesis` (this repo) @ `ec2b1d1463b4692a0dee6afaace6ec63384e25dc`

Re-check the connection table whenever any of these move, especially when the finite-bottleneck
RDLB section or any of the six Foundation gaps land.
