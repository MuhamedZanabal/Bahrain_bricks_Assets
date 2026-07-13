"""Generate a deterministic 4 m kerb and sidewalk edge module."""
from __future__ import annotations
import argparse, sys
from pathlib import Path
import bpy
from _common import reset_scene, create_material, add_box, add_collision_box, export_glb


def build(output: Path) -> None:
    reset_scene()
    concrete = create_material("bh_mat_concrete_light", (0.62, 0.60, 0.55, 1.0), roughness=0.88)
    kerb = add_box("bh_kerb_standard_straight_4m_01", (2.0, 0.15, 0.15), (0, 0.15, 0), concrete)
    add_collision_box(kerb, "bh_col_kerb_standard_straight_4m_01", (2.0, 0.15, 0.15), (0, 0.15, 0))
    export_glb(output / "bh_kerb_standard_straight_4m_01.glb")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--output", default="build/generated/roads")
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    build(Path(args.output))
