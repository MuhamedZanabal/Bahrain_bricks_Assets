"""Generate a low-poly waterfront/street bollard."""
from __future__ import annotations
import argparse, sys
from pathlib import Path
import bpy
from _common import reset_scene, create_material, add_collision_box, export_glb


def build(output: Path) -> None:
    reset_scene()
    metal = create_material("bh_mat_painted_metal_charcoal", (0.08, 0.09, 0.10, 1.0), roughness=0.48)
    bpy.ops.mesh.primitive_cylinder_add(vertices=12, radius=0.10, depth=0.85, location=(0, 0.425, 0))
    obj = bpy.context.object; obj.name = "bh_prop_street_bollard_a_01"; obj.data.materials.append(metal)
    add_collision_box(obj, "bh_col_prop_street_bollard_a_01", (0.11, 0.425, 0.11), (0, 0.425, 0))
    export_glb(output / "bh_prop_street_bollard_a_01.glb")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--output", default="build/generated/street")
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    build(Path(args.output))
