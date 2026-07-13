from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.check_signing_material import find_violations


class SigningMaterialTests(unittest.TestCase):
    def test_documentation_may_describe_historical_issue(self):
        with TemporaryDirectory() as td:
            root = Path(td)
            (root / "docs").mkdir()
            (root / "docs" / "audit.md").write_text(
                'keystore/release_password="historical-example"\n', encoding="utf-8"
            )
            self.assertEqual(find_violations(root), [])

    def test_rejects_keystore_binary_by_extension(self):
        with TemporaryDirectory() as td:
            root = Path(td)
            (root / "debug.keystore").write_bytes(b"not-a-real-key")
            self.assertEqual(
                find_violations(root), ["forbidden signing file: debug.keystore"]
            )

    def test_rejects_password_assignment_in_export_config(self):
        with TemporaryDirectory() as td:
            root = Path(td)
            (root / "export_presets.cfg").write_text(
                'keystore/release_password="secret"\n', encoding="utf-8"
            )
            self.assertEqual(
                find_violations(root),
                ["signing password assignment: export_presets.cfg:1"],
            )


if __name__ == "__main__":
    unittest.main()
