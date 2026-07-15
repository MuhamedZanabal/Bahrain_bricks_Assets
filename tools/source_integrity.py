#!/usr/bin/env python3
"""Generate and verify the canonical tracked-file SHA-256 ledger.

The ledger scope is the Git index, not the mutable working-tree filesystem. The
ledger file excludes itself to avoid a recursive checksum. All other tracked
files, including intentionally committed generated evidence, remain in scope.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable

_HASH_LINE = re.compile(r"^([0-9a-f]{64})  (.+)$")
_NON_AUTHORITATIVE_PARTS = frozenset({"__pycache__", ".pytest_cache", ".godot"})
_NON_AUTHORITATIVE_TOP_LEVEL = frozenset({"build", "dist", "exports"})
_NON_AUTHORITATIVE_SUFFIXES = frozenset({".pyc", ".pyo", ".tmp", ".blend1"})


@dataclass(frozen=True)
class VerificationResult:
    expected_entries: int
    ledger_entries: int
    modified_files: tuple[str, ...] = ()
    missing_files: tuple[str, ...] = ()
    missing_entries: tuple[str, ...] = ()
    unexpected_entries: tuple[str, ...] = ()
    malformed_lines: tuple[str, ...] = ()

    @property
    def passed(self) -> bool:
        return not (
            self.modified_files
            or self.missing_files
            or self.missing_entries
            or self.unexpected_entries
            or self.malformed_lines
        )


def _run_git(root: Path, *args: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def _normalise_repo_path(raw: str) -> str:
    path = PurePosixPath(raw.replace("\\", "/"))
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError(f"unsafe repository path: {raw!r}")
    return path.as_posix()


def _ledger_relative_path(root: Path, ledger_path: Path) -> str:
    root = root.resolve()
    ledger = ledger_path.resolve()
    try:
        relative = ledger.relative_to(root)
    except ValueError as error:
        raise ValueError("ledger must be inside repository root") from error
    return _normalise_repo_path(relative.as_posix())


def _is_non_authoritative_generated(relative: str) -> bool:
    path = PurePosixPath(relative)
    if any(part in _NON_AUTHORITATIVE_PARTS for part in path.parts):
        return True
    if path.parts and path.parts[0] in _NON_AUTHORITATIVE_TOP_LEVEL:
        return True
    return path.suffix.lower() in _NON_AUTHORITATIVE_SUFFIXES


def tracked_paths(root: Path, ledger_path: Path) -> tuple[str, ...]:
    """Return the deterministic canonical ledger scope from the Git index."""
    root = root.resolve()
    excluded = _ledger_relative_path(root, ledger_path)
    raw = _run_git(root, "ls-files", "-z")
    paths: set[str] = set()
    for item in raw.decode("utf-8").split("\0"):
        if not item:
            continue
        relative = _normalise_repo_path(item)
        if relative == excluded or _is_non_authoritative_generated(relative):
            continue
        paths.add(relative)
    return tuple(sorted(paths))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def generate_ledger(root: Path, ledger_path: Path) -> dict[str, str]:
    root = root.resolve()
    ledger_path = ledger_path.resolve()
    entries: dict[str, str] = {}
    for relative in tracked_paths(root, ledger_path):
        source = root / relative
        if not source.is_file():
            raise FileNotFoundError(f"tracked file is missing or not regular: {relative}")
        entries[relative] = _sha256(source)

    payload = "".join(f"{digest}  {relative}\n" for relative, digest in entries.items())
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = ledger_path.with_name(f".{ledger_path.name}.tmp")
    temporary.write_text(payload, encoding="utf-8", newline="\n")
    os.replace(temporary, ledger_path)
    return entries


def _parse_ledger(ledger_path: Path) -> tuple[dict[str, str], tuple[str, ...]]:
    entries: dict[str, str] = {}
    malformed: list[str] = []
    for line_number, line in enumerate(ledger_path.read_text(encoding="utf-8").splitlines(), 1):
        match = _HASH_LINE.fullmatch(line)
        if not match:
            malformed.append(f"{line_number}:{line}")
            continue
        digest, raw_path = match.groups()
        try:
            path = _normalise_repo_path(raw_path)
        except ValueError:
            malformed.append(f"{line_number}:{line}")
            continue
        if path in entries:
            malformed.append(f"{line_number}:duplicate:{path}")
            continue
        entries[path] = digest
    return entries, tuple(malformed)


def verify_ledger(root: Path, ledger_path: Path) -> VerificationResult:
    root = root.resolve()
    ledger_path = ledger_path.resolve()
    expected = set(tracked_paths(root, ledger_path))
    entries, malformed = _parse_ledger(ledger_path)
    actual_paths = set(entries)

    missing_entries = tuple(sorted(expected - actual_paths))
    unexpected_entries = tuple(sorted(actual_paths - expected))
    missing_files: list[str] = []
    modified_files: list[str] = []
    for relative in sorted(expected & actual_paths):
        source = root / relative
        if not source.is_file():
            missing_files.append(relative)
        elif _sha256(source) != entries[relative]:
            modified_files.append(relative)

    return VerificationResult(
        expected_entries=len(expected),
        ledger_entries=len(entries),
        modified_files=tuple(modified_files),
        missing_files=tuple(missing_files),
        missing_entries=missing_entries,
        unexpected_entries=unexpected_entries,
        malformed_lines=malformed,
    )


def _result_payload(result: VerificationResult) -> dict[str, object]:
    payload: dict[str, object] = asdict(result)
    payload["passed"] = result.passed
    payload["failure_count"] = sum(
        len(items)
        for items in (
            result.modified_files,
            result.missing_files,
            result.missing_entries,
            result.unexpected_entries,
            result.malformed_lines,
        )
    )
    return payload


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("generate", "verify"))
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--ledger", type=Path, default=Path("SHA256SUMS"))
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    root = args.root.resolve()
    ledger = args.ledger if args.ledger.is_absolute() else root / args.ledger
    if args.action == "generate":
        entries = generate_ledger(root, ledger)
        print(json.dumps({"generated_entries": len(entries), "ledger": str(ledger)}, indent=2))
        return 0

    result = verify_ledger(root, ledger)
    print(json.dumps(_result_payload(result), indent=2))
    return 0 if result.passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
