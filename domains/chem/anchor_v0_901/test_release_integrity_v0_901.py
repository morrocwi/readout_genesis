import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent

class IntegrityTests(unittest.TestCase):
    def test_source_locks(self):
        locks = json.loads((ROOT/'SOURCE_LOCKS_v0_901.json').read_text())
        for item in locks['files']:
            path = ROOT/item['path']
            self.assertTrue(path.is_file(), item)
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), item['sha256'])

    def test_standalone_manifest(self):
        manifest = json.loads((ROOT/'STANDALONE_MANIFEST_v0_901.json').read_text())
        self.assertTrue(manifest['standalone'])
        self.assertEqual(manifest['runtime_dependencies'], ['Python standard library'])
        for path in manifest['required_paths']:
            self.assertTrue((ROOT/path).exists(), path)

    def test_checksums(self):
        for line in (ROOT/'CHECKSUMS_SHA256_v0_901.txt').read_text().splitlines():
            if not line.strip():
                continue
            digest, rel = line.split('  ', 1)
            self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(), digest, rel)

if __name__ == '__main__':
    unittest.main()
