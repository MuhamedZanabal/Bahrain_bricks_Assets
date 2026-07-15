from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.source_integrity import generate_ledger, verify_ledger


class SourceIntegrityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.name", "Test"], check=True)
        subprocess.run(["git", "-C", str(self.root), "config", "user.email", "test@example.invalid"], check=True)
        (self.root / ".gitignore").write_text("__pycache__/\n*.pyc\n", encoding="utf-8")
        (self.root / "a.txt").write_text("authority\n", encoding="utf-8")
        (self.root / "nested").mkdir()
        (self.root / "nested" / "b.txt").write_text("production\n", encoding="utf-8")
        (self.root / "SHA256SUMS").write_text("", encoding="utf-8")
        subprocess.run(
            ["git", "-C", str(self.root), "add", ".gitignore", "a.txt", "nested/b.txt", "SHA256SUMS"],
            check=True,
        )
        self.ledger = self.root / "SHA256SUMS"

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_modified_tracked_file_fails_verification(self) -> None:
        generate_ledger(self.root, self.ledger)
        (self.root / "a.txt").write_text("modified\n", encoding="utf-8")

        result = verify_ledger(self.root, self.ledger)

        self.assertFalse(result.passed)
        self.assertEqual(result.modified_files, ("a.txt",))

    def test_missing_tracked_file_fails_verification(self) -> None:
        generate_ledger(self.root, self.ledger)
        (self.root / "nested" / "b.txt").unlink()

        result = verify_ledger(self.root, self.ledger)

        self.assertFalse(result.passed)
        self.assertEqual(result.missing_files, ("nested/b.txt",))

    def test_ignored_bytecode_does_not_enter_ledger(self) -> None:
        cache = self.root / "tools" / "__pycache__"
        cache.mkdir(parents=True)
        bytecode = cache / "generated.cpython-311.pyc"
        bytecode.write_bytes(b"generated-bytecode")
        subprocess.run(
            ["git", "-C", str(self.root), "add", "-f", "tools/__pycache__/generated.cpython-311.pyc"],
            check=True,
        )

        generate_ledger(self.root, self.ledger)

        text = self.ledger.read_text(encoding="utf-8")
        self.assertNotIn("__pycache__", text)
        self.assertNotIn(".pyc", text)

    def test_repeated_generation_is_deterministic(self) -> None:
        generate_ledger(self.root, self.ledger)
        first = self.ledger.read_bytes()

        generate_ledger(self.root, self.ledger)
        second = self.ledger.read_bytes()

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
