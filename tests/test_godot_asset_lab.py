from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / 'godot_asset_lab'

class GodotAssetLabTests(unittest.TestCase):
    def test_project_is_godot_43_mobile_gl_compatibility(self):
        text = (LAB / 'project.godot').read_text(encoding='utf-8')
        self.assertIn('config/features=PackedStringArray("4.3", "GL Compatibility")', text)
        self.assertIn('renderer/rendering_method="gl_compatibility"', text)
        self.assertIn('renderer/rendering_method.mobile="gl_compatibility"', text)
        self.assertIn('window/size/viewport_width=1280', text)
        self.assertIn('window/size/viewport_height=720', text)

    def test_gallery_scans_only_isolated_generated_assets(self):
        text = (LAB / 'scripts/asset_gallery.gd').read_text(encoding='utf-8')
        self.assertIn('res://assets/generated', text)
        self.assertIn('DirAccess.open', text)
        self.assertIn('ResourceLoader.exists', text)
        self.assertNotIn('player_controller', text)
        self.assertNotIn('joystick', text)
        self.assertNotIn('brick-bahrain-open-world', text)

    def test_benchmark_records_mobile_metrics(self):
        text = (LAB / 'scripts/mobile_benchmark.gd').read_text(encoding='utf-8')
        for monitor in (
            'Performance.TIME_FPS',
            'Performance.TIME_PROCESS',
            'Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME',
            'Performance.MEMORY_STATIC',
        ):
            self.assertIn(monitor, text)
        self.assertIn('user://bahrain_brick_asset_benchmark.json', text)

    def test_required_scenes_and_documentation_exist(self):
        for rel in (
            'scenes/asset_gallery.tscn',
            'scenes/mobile_benchmark.tscn',
            'assets/generated/.gitkeep',
        ):
            self.assertTrue((LAB / rel).is_file(), rel)
        doc=(ROOT/'docs/assets/GODOT_ASSET_LAB.md').read_text(encoding='utf-8').lower()
        self.assertIn('godot 4.3',doc)
        self.assertIn('android',doc)
        self.assertIn('not run',doc)

if __name__ == '__main__':
    unittest.main()
