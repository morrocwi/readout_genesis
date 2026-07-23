#!/usr/bin/env python3
"""Run primary and independent Philosophy/MEMK release checks."""
from philosophy_memk_closure_v0_2_0 import run as primary
from checker_philosophy_memk import run as independent

def main():
    ok1, r1 = primary()
    ok2, r2 = independent()
    if not ok1 or not ok2:
        print("PRIMARY", r1)
        print("INDEPENDENT", r2)
        raise SystemExit("FAIL: Philosophy/MEMK release bundle")
    print("PASS: PHILOSOPHY_MEMK_STRUCTURAL_REGISTRATION")
    print("DOMAIN_CLOSURE: UNRESOLVED")
    print("EMPIRICAL_CALIBRATION: UNRESOLVED")

if __name__ == "__main__":
    main()
