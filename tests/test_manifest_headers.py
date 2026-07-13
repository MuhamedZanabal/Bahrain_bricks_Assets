import csv, unittest
from pathlib import Path
class ManifestTests(unittest.TestCase):
    def test_master_has_rows_and_unique_ids(self):
        p=Path(__file__).resolve().parents[1]/'docs/assets/ASSET_MASTER_MANIFEST.csv'
        with p.open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
        self.assertGreater(len(rows),50)
        ids=[r['asset_id'] for r in rows]
        self.assertEqual(len(ids),len(set(ids)))
    def test_inherited_are_quarantined(self):
        p=Path(__file__).resolve().parents[1]/'docs/assets/ASSET_MASTER_MANIFEST.csv'
        with p.open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
        for r in rows:
            if r['source_type']=='inherited_unverified': self.assertEqual(r['integration_status'],'quarantined')
if __name__=='__main__': unittest.main()
