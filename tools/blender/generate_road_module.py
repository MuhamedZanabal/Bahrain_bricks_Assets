"""Generate deterministic Bahrain Brick road modules in Blender.
Run: blender --background --python tools/blender/generate_road_module.py -- --output <dir>
"""
from __future__ import annotations
import argparse, sys
from pathlib import Path
import bpy
from _common import reset_scene, create_material, add_box, add_collision_box, export_glb


def build(output: Path) -> None:
    reset_scene()
    asphalt = create_material("bh_mat_asphalt_worn", (0.10, 0.105, 0.11, 1.0), roughness=0.92)
    marking = create_material("bh_mat_road_marking_white", (0.92, 0.91, 0.82, 1.0), roughness=0.65)
    road = add_box("bh_road_two_lane_straight_20m_01", (10.0, 0.10, 4.0), (0, 0, 0), asphalt)
    for x in (-7.5, -2.5, 2.5, 7.5):
        add_box(f"bh_road_marking_center_{int(x*10):+04d}", (1.4, 0.012, 0.06), (x, 0.112, 0), marking)
    add_collision_box(road, "bh_col_road_two_lane_straight_20m_01", (10.0, 0.12, 4.0), (0, 0, 0))
    export_glb(output / "bh_road_two_lane_straight_20m_01.glb")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="build/generated/roads")
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    build(Path(args.output))
