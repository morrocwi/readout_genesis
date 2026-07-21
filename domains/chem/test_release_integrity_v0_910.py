import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parent
class TestIntegrity(unittest.TestCase):
    def test_claim(self):
        c=json.loads((ROOT/'CLAIM_BOUNDARY_v0_910.json').read_text()); self.assertEqual(c['tier'],'FORMAL_COMPOSITION_QUOTIENT_ONLY')
    def test_source_locks(self):
        locks=json.loads((ROOT/'SOURCE_LOCKS_v0_910.json').read_text())
        for rel,expected in locks['files'].items():
            h=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(); self.assertEqual(h,expected,rel)
    def test_checksums(self):
        for line in (ROOT/'CHECKSUMS_SHA256_v0_910.txt').read_text().splitlines():
            if not line.strip():continue
            expected,rel=line.split('  ',1); self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),expected,rel)
    def test_standalone(self):
        m=json.loads((ROOT/'STANDALONE_MANIFEST_v0_910.json').read_text()); self.assertTrue(m['standalone']); self.assertFalse(m['network_required'])
if __name__=='__main__':unittest.main()
