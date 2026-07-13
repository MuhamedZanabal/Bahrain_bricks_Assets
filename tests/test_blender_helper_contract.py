import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLENDER = ROOT / 'tools' / 'blender'


def _defined_names(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding='utf-8'))
    return {node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}


def test_all_common_imports_exist():
    available = _defined_names(BLENDER / '_common.py')
    missing: dict[str, list[str]] = {}
    for path in BLENDER.glob('generate_*.py'):
        tree = ast.parse(path.read_text(encoding='utf-8'))
        requested = []
        for node in tree.body:
            if isinstance(node, ast.ImportFrom) and node.module == '_common':
                requested.extend(alias.name for alias in node.names)
        absent = sorted(set(requested) - available)
        if absent:
            missing[path.name] = absent
    assert not missing, f'Undefined _common imports: {missing}'
