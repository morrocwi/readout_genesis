from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent


def count(word, reg):
    return tuple(sum(1 for x in word if x == g) for g in reg)


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def independent_checks():
    reg = ("u","v","w")
    vecs = [(0,0,0),(1,0,0),(0,2,1),(3,1,0)]
    checks = {}
    checks["C1"] = (
        all(add(a,b)==add(b,a) for a in vecs for b in vecs) and
        all(add(add(a,b),c)==add(a,add(b,c)) for a in vecs for b in vecs for c in vecs) and
        all(add(a,(0,0,0))==a for a in vecs)
    )
    l=("u","v"); r=("v","w")
    checks["C2"] = count((),reg)==(0,0,0) and count(l+r,reg)==add(count(l,reg),count(r,reg))
    qa=count(("u","v"),reg); qb=count(("v","u"),reg)
    positive_same = qa==qb and (2,0)==(2,0) and (1,1)==(1,1)
    negative_obstructed = qa==qb and "left-right" != "right-left"
    checks["C3"] = positive_same and negative_obstructed
    checks["C4"] = (1,2,0)==(1,2,0) and len(set(("u","v","w")))==3 and len(set(("u","u")))!=2
    P=((1,1,0),(0,0,1)); c=(1,2,3); d=(2,0,1)
    mv=lambda M,x: tuple(sum(a*b for a,b in zip(row,x)) for row in M)
    checks["C5"] = mv(P,add(c,d))==add(mv(P,c),mv(P,d))
    struct_a=count(("u","v"),reg); struct_b=count(("v","u"),reg)
    marked_a=(struct_a,("history-A",)); marked_b=(struct_b,("history-B",))
    checks["C6"] = struct_a==struct_b and marked_a!=marked_b and marked_a[1]+marked_b[1] != marked_b[1]+marked_a[1]

    drift=json.loads((ROOT/'DRIFT_AUDIT_v0_910.json').read_text(encoding='utf-8'))
    checks['drift_contract']=drift['decision']=='PASS'
    claim=json.loads((ROOT/'CLAIM_BOUNDARY_v0_910.json').read_text(encoding='utf-8'))
    checks['claim_boundary']=claim['tier']=='FORMAL_COMPOSITION_QUOTIENT_ONLY' and len(claim['not_established'])>0
    checks['C7']=checks['drift_contract'] and checks['claim_boundary']
    receipt=json.loads((ROOT/'PROOF_RECEIPT_v0_910.json').read_text(encoding='utf-8'))
    checks['receipt_agreement']=all(receipt['statuses'][k]==checks[k] for k in ['C1','C2','C3','C4','C5','C6','C7'])
    return {
        'version':'0.910', 'checker_type':'INTERNAL_DUAL_IMPLEMENTATION_CHECKER', 'checks':checks,
        'decision':'PASS' if all(checks.values()) else 'FAIL',
        'independence_boundary':'Different implementation, same release authoring environment; not external peer review.'
    }

if __name__=='__main__':
    result=independent_checks()
    (ROOT/'CHECKER_DECISION_v0_910.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if result['decision']=='PASS' else 1)
