from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name): return json.loads((ROOT/name).read_text(encoding='utf-8'))
def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1<<20),b''): h.update(chunk)
    return h.hexdigest()

def dag_errors(dag):
    nodes={n['id']:n for n in dag['nodes']}; errors=[]; adj={x:[] for x in nodes}; indeg={x:0 for x in nodes}
    for a,b in dag['edges']:
        if a not in nodes or b not in nodes: errors.append(f'unknown edge {a}->{b}'); continue
        adj[a].append(b); indeg[b]+=1
    q=[x for x,d in indeg.items() if d==0]; seen=0
    while q:
        x=q.pop(); seen+=1
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    if seen!=len(nodes):errors.append('DAG cycle')
    return nodes,errors

def run_drift_audit():
    dag=load('ROOT_DAG_MASTER_v0_910.json'); base=load('anchor_v0_901/ROOT_DAG_MASTER_v0_901.json')
    registry=load('RULE_REGISTRY_v0_910.json'); contract=load('DRIFT_CONTRACT_v0_910.json')
    nodes,errors=dag_errors(dag)
    current={n['id']:n for n in dag['nodes']}
    for old in base['nodes']:
        if old['id'] not in current: errors.append(f"missing inherited node {old['id']}")
        elif current[old['id']]!=old: errors.append(f"drifted inherited node {old['id']}")
    edges={tuple(e) for e in dag['edges']}
    for e in base['edges']:
        if tuple(e) not in edges: errors.append(f"removed inherited edge {e}")
    allowed=set(contract['allowed_rule_classes']); ids=set(); forbidden={'EMPIRICAL_TAPE','DISCOVERED_DOMAIN_LAW','CALIBRATED_READOUT','NUMERICAL_PROCEDURE'}
    for rule in registry['rules']:
        rid=rule['rule_id']
        if rid in ids:errors.append(f'duplicate rule {rid}')
        ids.add(rid)
        if rule['class'] not in allowed:errors.append(f'bad class {rid}')
        if not rule.get('forbidden_claims'):errors.append(f'missing forbidden claims {rid}')
        for p in rule['parents']:
            if p not in nodes:errors.append(f'unknown parent {rid}:{p}')
            elif rule['class']=='ROOT_THEOREM' and nodes[p]['type'] in forbidden:errors.append(f'root theorem forbidden dependency {rid}:{p}')
    hits=[]
    for name in contract['active_files_scanned_for_imported_laws']:
        text=(ROOT/name).read_text(encoding='utf-8').lower()
        for token in contract['prohibited_active_domain_tokens']:
            if token.lower() in text:hits.append({'file':name,'token':token})
    if hits:errors.append('prohibited domain tokens in active files')
    required=load('STANDALONE_MANIFEST_v0_910.json')['required_paths']
    missing=[p for p in required if not (ROOT/p).exists()]
    if missing:errors.append('missing standalone paths')
    if load('CLAIM_BOUNDARY_v0_910.json')['tier']!='FORMAL_COMPOSITION_QUOTIENT_ONLY':errors.append('claim tier drift')
    result={'version':'0.910','errors':errors,'imported_token_hits':hits,'missing_standalone_paths':missing,
            'dag_sha256':sha(ROOT/'ROOT_DAG_MASTER_v0_910.json'),'registry_sha256':sha(ROOT/'RULE_REGISTRY_v0_910.json'),
            'decision':'PASS' if not errors else 'FAIL'}
    return result
if __name__=='__main__':
    r=run_drift_audit(); (ROOT/'DRIFT_AUDIT_v0_910.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n',encoding='utf-8'); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r['decision']=='PASS' else 1)
