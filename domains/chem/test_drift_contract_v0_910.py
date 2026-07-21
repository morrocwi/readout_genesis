import json, unittest
from pathlib import Path
from drift_validator_v0_910 import run_drift_audit
ROOT=Path(__file__).resolve().parent
class TestDrift(unittest.TestCase):
    def test_drift(self): self.assertEqual(run_drift_audit()['decision'],'PASS')
    def test_delta_no_destructive_change(self):
        d=json.loads((ROOT/'ROOT_DAG_DELTA_v0_910.json').read_text())
        self.assertEqual(d['removed_nodes'],[]); self.assertEqual(d['retyped_nodes'],[]); self.assertEqual(d['renamed_nodes'],[])
    def test_recursive_anchor(self): self.assertTrue((ROOT/'anchor_v0_901/run_all_tests_v0_901.py').is_file())
if __name__=='__main__':unittest.main()
