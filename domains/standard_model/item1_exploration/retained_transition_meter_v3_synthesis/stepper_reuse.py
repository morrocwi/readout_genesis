#!/usr/bin/env python3
"""
RTM v1 -- stepper_reuse.py: thin import shim, NO copy-pasted physics.

Reuses the EXACT Reader/Record stepper functions, gradV/grad2V, and (M, D, K) parameters from
`domains/standard_model/matter_antimatter_exploration/attempt1_bateman_doubling_hypothesis_v1.py`
by loading that file as a module via `importlib.util` (it has no `__init__.py`/package -- it is a
script, not an importable module in the normal sense). This file re-exports the reused objects
UNMODIFIED. It does not redefine `gradV`, `grad2V`, `step_reader`, or `step_record` anywhere --
per the System position paper, a second hand-copy of that math is the #1 silent-fork risk this
file exists to avoid.

SIDE EFFECT DISCLOSURE: attempt1_bateman_doubling_hypothesis_v1.py is a SCRIPT, not a library --
importing it by path executes its entire body, including its own 2000-step simulation, its own
`ck()` checks, and its own prints/HONEST FENCE. That is attempt1's own already-reviewed, already-
passing diagnostic run (matter/antimatter Dr-tier hypothesis, unrelated to RTM) -- re-running it
here is an unavoidable consequence of "no copy-paste, reuse the real functions," not a new claim.
Its stdout is captured and discarded (not silently hidden from the record: printed once here,
clearly labeled, so nothing is suppressed without disclosure) rather than left to interleave with
RTM's own output.

Tier: this file makes NO physics claim itself -- pure plumbing. N/A for tier purposes.
"""
import importlib.util
import io
import os
import contextlib

_ATTEMPT1_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "matter_antimatter_exploration",
    "attempt1_bateman_doubling_hypothesis_v1.py",
)
_ATTEMPT1_PATH = os.path.normpath(_ATTEMPT1_PATH)

if not os.path.exists(_ATTEMPT1_PATH):
    raise FileNotFoundError(
        f"stepper_reuse.py requires the existing stepper at {_ATTEMPT1_PATH} -- "
        "RTM does not implement a fallback copy of the stepper math."
    )

_spec = importlib.util.spec_from_file_location("attempt1_bateman_doubling_hypothesis_v1", _ATTEMPT1_PATH)
_stepper_module = importlib.util.module_from_spec(_spec)

_captured_stdout = io.StringIO()
with contextlib.redirect_stdout(_captured_stdout):
    _spec.loader.exec_module(_stepper_module)

ATTEMPT1_IMPORT_STDOUT = _captured_stdout.getvalue()
ATTEMPT1_IMPORT_FAILS = list(_stepper_module.FAILS)  # attempt1's OWN ck() failures, if any (disclosed below)

# Re-exports -- UNMODIFIED, same objects, no second copy of the math.
step_reader = _stepper_module.step_reader
step_record = _stepper_module.step_record
gradV = _stepper_module.gradV
grad2V = _stepper_module.grad2V
M = _stepper_module.M
D = _stepper_module.D
K = _stepper_module.K
dt = _stepper_module.dt


def disclose_reuse():
    """Print a short, honest disclosure of what was reused and what happened on import.
    Call this explicitly from RTM's own orchestrator (not at import time) so RTM's own
    stdout stays in RTM's control, while the reuse is never hidden."""
    print(f"  [REUSE] loaded stepper from: {_ATTEMPT1_PATH}")
    print(f"  [REUSE] reused unmodified: step_reader, step_record, gradV, grad2V, M={M}, D={D}, K={K}, dt={dt}")
    print(f"  [REUSE] attempt1's own import-time simulation ran and was captured "
          f"({len(ATTEMPT1_IMPORT_STDOUT.splitlines())} lines of its own stdout, discarded -- "
          f"that is attempt1's own already-reviewed matter/antimatter run, unrelated to RTM)")
    if ATTEMPT1_IMPORT_FAILS:
        print(f"  [REUSE] WARNING: attempt1's own ck() checks reported {len(ATTEMPT1_IMPORT_FAILS)} "
              f"FAIL(S) on import: {ATTEMPT1_IMPORT_FAILS} -- inspecting the reused functions for "
              f"correctness before trusting RTM's own fit is recommended")
    else:
        print(f"  [REUSE] attempt1's own ck() checks: all PASS on this import (no known-broken reused code)")
