import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SCRIPTS = {
    'tools/blender/generate_highway_modules.py',
    'tools/blender/generate_sidewalk_modules.py',
    'tools/blender/generate_drainage_channel.py',
    'tools/blender/generate_direction_sign_frame.py',
    'tools/blender/generate_supermarket_checkout.py',
}
EXPECTED_ASSET_IDS = {
    'bh_road_highway_six_lane_straight_40m_01',
    'bh_road_highway_curve_40m_01',
    'bh_road_highway_slip_road_30m_01',
    'bh_road_highway_exit_40m_01',
    'bh_sidewalk_commercial_straight_4m_01',
    'bh_sidewalk_driveway_cut_4m_01',
    'bh_drainage_channel_straight_4m_01',
    'bh_prop_direction_sign_frame_a_01',
    'bh_prop_supermarket_checkout_a_01',
}

class Phase4Batch3AssetTests(unittest.TestCase):
    def test_scripts_exist_and_use_deterministic_cli(self):
        for rel in sorted(EXPECTED_SCRIPTS):
            path = ROOT / rel
            self.assertTrue(path.is_file(), rel)
            text = path.read_text(encoding='utf-8')
            self.assertIn('argparse.ArgumentParser', text, rel)
            self.assertIn('bpy.ops.export_scene.gltf', text, rel)
            self.assertNotIn('random.', text, rel)

    def test_master_manifest_contains_batch3_ids(self):
        path = ROOT / 'docs/assets/ASSET_MASTER_MANIFEST.csv'
        with path.open(newline='', encoding='utf-8') as handle:
            ids = {row['asset_id'] for row in csv.DictReader(handle)}
        self.assertTrue(EXPECTED_ASSET_IDS.issubset(ids), sorted(EXPECTED_ASSET_IDS - ids))

    def test_specs_define_collision_lod_and_android_gate(self):
        for rel in [
            'docs/assets/specs/highway_sidewalk_kit.md',
            'docs/assets/specs/supermarket_checkout_module.md',
        ]:
            text = (ROOT / rel).read_text(encoding='utf-8').lower()
            for term in ('collision', 'lod', 'android', 'godot 4.3'):
                self.assertIn(term, text, f'{rel}: {term}')

if __name__ == '__main__':
    unittest.main()
