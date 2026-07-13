"""Generate a low-poly Bahrain Brick promenade street lamp."""
from __future__ import annotations
import argparse, sys
from pathlib import Path
import bpy
from _common import reset_scene, create_material, add_box, add_collision_box, export_glb


def build(output: Path) -> None:
    reset_scene()
    metal = create_material("bh_mat_painted_metal_charcoal", (0.07, 0.08, 0.09, 1.0), roughness=0.42)
    emissive = create_material("bh_mat_lamp_warm", (1.0, 0.72, 0.35, 1.0), roughness=0.25)
    pole = add_box("bh_prop_streetlamp_prom_a_pole", (0.07, 2.4, 0.07), (0, 2.4, 0), metal)
    add_box("bh_prop_streetlamp_prom_a_arm", (0.45, 0.06, 0.06), (0.38, 4.65, 0), metal)
    add_box("bh_prop_streetlamp_prom_a_lamp", (0.24, 0.12, 0.16), (0.78, 4.5, 0), emissive)
    add_collision_box(pole, "bh_col_prop_streetlamp_prom_a_01", (0.10, 2.4, 0.10), (0, 2.4, 0))
    export_glb(output / "bh_prop_streetlamp_prom_a_01.glb")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--output", default="build/generated/street")
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    build(Path(args.output))
