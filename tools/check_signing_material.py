#!/usr/bin/env python3
"""Fail closed when repository content includes Android signing credentials.

Documentation may describe historical signing defects. This scanner only treats
credential-file extensions and password assignments in executable/configuration
surfaces as violations.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable

FORBIDDEN_SUFFIXES = {".keystore", ".jks", ".p12", ".pfx"}
CONFIG_SUFFIXES = {
    ".cfg", ".conf", ".env", ".godot", ".gradle", ".ini", ".json",
    ".properties", ".toml", ".yaml", ".yml",
}
PASSWORD_ASSIGNMENT = re.compile(
    r"^\s*keystore/(?:debug|release)_password\s*=\s*.+$", re.IGNORECASE
)
EXCLUDED_DIRS = {".git", "docs", "evidence", "__pycache__"}


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.relative_to(root).parts[:-1]):
            continue
        yield path


def find_violations(root: Path) -> list[str]:
    violations: list[str] = []
    for path in iter_files(root):
        rel = path.relative_to(root).as_posix()
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            violations.append(f"forbidden signing file: {rel}")
            continue
        if path.suffix.lower() not in CONFIG_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            if PASSWORD_ASSIGNMENT.match(line):
                violations.append(f"signing password assignment: {rel}:{line_no}")
    return violations


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    violations = find_violations(root)
    if violations:
        print("Signing-material validation failed:")
        for item in violations:
            print(f"- {item}")
        return 1
    print("Signing-material validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
