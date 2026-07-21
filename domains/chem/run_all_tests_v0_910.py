from __future__ import annotations
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
steps=[]
def run(name,cmd):
    p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
    steps.append({'name':name,'returncode':p.returncode})
    if p.returncode:
        print(p.stdout); print(p.stderr,file=sys.stderr)
run('drift_audit',[sys.executable,'drift_validator_v0_910.py'])
run('proof_receipt',[sys.executable,'make_proof_receipt_v0_910.py'])
run('checker',[sys.executable,'checker_v0_910.py'])
run('unit_tests',[sys.executable,'-m','unittest','-v','test_composition_kernel_v0_910.py','test_drift_contract_v0_910.py','test_release_integrity_v0_910.py'])
result={'version':'0.910','steps':steps,'decision':'PASS' if all(s['returncode']==0 for s in steps) else 'FAIL'}
(ROOT/'TEST_REPORT_v0_910.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2,sort_keys=True))
raise SystemExit(0 if result['decision']=='PASS' else 1)
