# NS application note — EPSC-38 sample interpolation conditioning

Status: external Navier--Stokes application map only. This note does not promote a domain-specific result into the Readout Genesis root canon.

The finite-observability programme now distinguishes two derivative-free sampling statements.

`PROP-EPSC-37` is structural: for the fixed `N=1` shell-energy case, 49 finite-time shell-energy samples form a local quotient chart for sufficiently small nonzero spacing because the sample Jacobian has a nonzero leading determinant coefficient.

`PROP-EPSC-38` is quantitative but narrower: if those samples are first interpolated back into the existing high-order scaled Taylor chart, the exact finite interpolation operator has induced infinity norm

\[
\boxed{
\kappa_\infty(h)
=
\|S D_h^{-1}V^{-1}\|_\infty
=
\max_n |s_n||h|^{-n}\sum_j |(V^{-1})_{nj}|.
}
\]

For the current `N=1` application, `s_n=600^n n!` and the two primary shell channels use nodes `0,...,23`. Exact rational reproduction shows very large amplification even before physical sensor or model errors are introduced:

\[
10^{70}\le\kappa_\infty(1)<10^{71},
\qquad
10^{93}\le\kappa_\infty(10^{-1})<10^{94},
\]

\[
10^{116}\le\kappa_\infty(10^{-2})<10^{117},
\qquad
10^{134}\le\kappa_\infty(1/600)<10^{135}.
\]

The application-level interpretation is therefore not that finite-time sampling fails. It is that the intermediate representation

\[
\text{samples}
\to
\text{high-order Taylor/derivative chart}
\to
\text{retained inverse}
\]

can be badly conditioned even when the direct finite sample map is structurally invertible. The next useful application target is to invert the direct sample map itself with an explicit spacing and a certified local preconditioner:

\[
q_h=\sup_{x\in B}\|I-A_hD\mathcal S_h(x)\|_\infty<1.
\]

That would allow sample-space uncertainty to propagate directly to a retained-state radius `rho_1` without reconstructing derivatives through order 23.

The result remains owned by the finite-math and Navier--Stokes repositories. `PROP-EPSC-36` and full `PROP-EPSC-19` remain open for validated flow/tangent remainder, direct sample-map conditioning, branch capture, sensor/model uncertainty and end-to-end composition. Arbitrary-finite-`N` inversion, outer continuum completion, physical turbulence adequacy, continuum Navier--Stokes regularity and the Clay Millennium problem remain separate and unproved.
