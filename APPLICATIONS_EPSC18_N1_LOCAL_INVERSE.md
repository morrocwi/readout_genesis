# Readout Genesis application note — EPSC-18 full N=1 local inverse milestone

Status: external Navier-Stokes application; **not a Genesis root theorem**.

The Navier-Stokes application has now moved one step beyond rank saturation. At the finite cubic cutoff `N=1`, the application constructs an explicit finite symmetry slice and an explicit square shell-energy Taylor-jet minor.

The native chain is

\[
\boxed{
52\text{ finite state coordinates}
\to
3\text{ translation gauge directions}
\to
49\text{ finite quotient coordinates}
\to
49\text{ selected finite observations}
\to
\det J\ne0
\to
\text{local finite inverse}.
}
\]

The nonzero determinant is certified by a good-prime modular witness in the Navier-Stokes reproduction ledger and lifted back to the rational/real finite chart because the prime does not divide the construction's declared denominators.

## Why this matters to the Genesis interpretation

This is a direct example of the finite-first discipline:

> do not posit a completed infinite object and then ask whether a finite representation approximates it; first ask whether the declared finite distinctions determine the finite state relevant to the reader.

The local result uses no `X_infinity` object. It concerns only a finite observation map on a finite symmetry quotient.

The result also sharpens the earlier restoration/transfer interpretation. Shell-energy evolution retains the redistribution structure hidden by total energy, and the finite energy jet can locally distinguish all finite state directions except spatial translation at the certified witness. The proof of invertibility, however, comes from the finite Navier-Stokes observation Jacobian, not from the Genesis interpretation itself.

## What remains open

The result is **local existence**, not yet a measurement-ready certificate. The application still needs an explicit finite box `B`, interval Jacobian enclosure `J(B)`, and preconditioner `A` satisfying

\[
\|I-AJ(B)\|<1,
\]

plus certified branch/symmetry containment. Only then can observation uncertainty be converted into an explicit retained-state radius `rho_1`.

This remaining quantitative step is tracked in Toledo after the local-existence milestone. The full noisy chain and all-resolution saturation remain separate questions.

## Non-collapse fence

Nothing in this result implies:

- an actually existing completed infinite Fourier state;
- global injectivity of energy observations;
- an all-`N` theorem;
- continuum regularity or absence of singularities;
- physical DNS adequacy of `N=1`;
- a Clay Millennium solution.

If a continuum `beta_N` is later used, it remains an external analytic adapter composed with the finite-native `rho_N` layer rather than the ontological foundation of the finite proof.
