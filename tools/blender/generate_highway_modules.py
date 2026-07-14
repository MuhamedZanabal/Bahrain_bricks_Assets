"""Generate deterministic mobile highway modules for Bahrain Brick.

Run with Blender 4.x:
  blender --background --python generate_highway_modules.py -- --output-dir build/generated/roads
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path
import sys

import bpy

VARIANTS = ("straight", "curve", "slip_road", "exit")


def cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="build/generated/roads")
    parser.add_argument("--variant", choices=("all",) + VARIANTS, default="all")
    argv = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    return parser.parse_args(argv)


def reset_scene() -> None:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for datablocks in (bpy.data.meshes, bpy.data.curves, bpy.data.materials):
        for block in list(datablocks):
            if block.users == 0:
                datablocks.remove(block)
    bpy.context.scene.unit_settings.system = "METRIC"
    bpy.context.scene.unit_settings.scale_length = 1.0


def material(name: str, rgba: tuple[float, float, float, float], roughness: float = 0.8) -> bpy.types.Material:
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.diffuse_color = rgba
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = rgba
        bsdf.inputs["Roughness"].default_value = roughness
    return mat


def box(name: str, size: tuple[float, float, float], location: tuple[float, float, float], mat=None) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if mat:
        obj.data.materials.append(mat)
    return obj


def collision_box(name: str, size: tuple[float, float, float], location: tuple[float, float, float]) -> bpy.types.Object:
    obj = box(f"col_{name}", size, location)
    obj.display_type = "WIRE"
    obj.hide_render = True
    obj["collision_proxy"] = True
    return obj


def road_markings(length: float, width: float, z: float, marking_mat) -> None:
    for x in (-width / 6.0, width / 6.0):
        for i in range(-4, 5):
            box(f"mark_lane_{x:+.1f}_{i:+d}", (0.12, 2.5, 0.02), (x, i * 4.2, z), marking_mat)
    for x in (-width / 2.0 + 0.35, width / 2.0 - 0.35):
        box(f"mark_edge_{x:+.1f}", (0.16, length - 1.0, 0.02), (x, 0.0, z), marking_mat)


def ring_segment(name: str, inner_r: float, outer_r: float, angle_deg: float, height: float, mat) -> bpy.types.Object:
    steps = 20
    start = -angle_deg / 2.0
    vertices = []
    faces = []
    for z in (-height / 2.0, height / 2.0):
        for i in range(steps + 1):
            a = math.radians(start + angle_deg * i / steps)
            for radius in (inner_r, outer_r):
                vertices.append((math.cos(a) * radius, math.sin(a) * radius, z))
    layer = (steps + 1) * 2
    for i in range(steps):
        a, b = i * 2, i * 2 + 1
        c, d = (i + 1) * 2, (i + 1) * 2 + 1
        faces.append((a, c, d, b))
        faces.append((a + layer, b + layer, d + layer, c + layer))
        faces.append((a, b, b + layer, a + layer))
        faces.append((c, c + layer, d + layer, d))
    faces.extend([
        (0, layer, layer + 1, 1),
        (steps * 2, steps * 2 + 1, layer + steps * 2 + 1, layer + steps * 2),
    ])
    mesh = bpy.data.meshes.new(f"{name}_mesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    obj.data.materials.append(mat)
    return obj


def build_straight(asphalt, marking) -> str:
    name = "bh_road_highway_six_lane_straight_40m_01"
    box(name, (18.0, 40.0, 0.24), (0.0, 0.0, 0.0), asphalt)
    road_markings(40.0, 18.0, 0.13, marking)
    collision_box(name, (18.0, 40.0, 0.24), (0.0, 0.0, 0.0))
    return name


def build_curve(asphalt, marking) -> str:
    name = "bh_road_highway_curve_40m_01"
    ring_segment(name, 18.0, 36.0, 64.0, 0.24, asphalt)
    # Collision is deliberately coarse for mobile: three boxes approximate the arc.
    for i, angle in enumerate((-22.0, 0.0, 22.0)):
        radius = 27.0
        a = math.radians(angle)
        obj = collision_box(f"{name}_{i}", (18.0, 13.5, 0.28), (math.cos(a) * radius, math.sin(a) * radius, 0.0))
        obj.rotation_euler[2] = a + math.pi / 2.0
    return name


def build_slip_road(asphalt, marking) -> str:
    name = "bh_road_highway_slip_road_30m_01"
    box(name, (18.0, 30.0, 0.24), (0.0, 0.0, 0.0), asphalt)
    ramp = box(f"{name}_merge_lane", (5.0, 24.0, 0.22), (8.0, 2.0, 0.01), asphalt)
    ramp.rotation_euler[2] = math.radians(-12.0)
    box(f"{name}_gore_mark", (0.18, 20.0, 0.02), (5.8, 0.0, 0.14), marking)
    collision_box(name, (18.0, 30.0, 0.24), (0.0, 0.0, 0.0))
    proxy = collision_box(f"{name}_merge_lane", (5.0, 24.0, 0.24), (8.0, 2.0, 0.0))
    proxy.rotation_euler[2] = math.radians(-12.0)
    return name


def build_exit(asphalt, marking) -> str:
    name = "bh_road_highway_exit_40m_01"
    box(name, (18.0, 40.0, 0.24), (0.0, 0.0, 0.0), asphalt)
    exit_lane = box(f"{name}_diverge_lane", (4.5, 30.0, 0.22), (9.2, 3.0, 0.01), asphalt)
    exit_lane.rotation_euler[2] = math.radians(15.0)
    box(f"{name}_gore", (0.18, 18.0, 0.02), (6.3, -2.0, 0.14), marking)
    collision_box(name, (18.0, 40.0, 0.24), (0.0, 0.0, 0.0))
    proxy = collision_box(f"{name}_diverge_lane", (4.5, 30.0, 0.24), (9.2, 3.0, 0.0))
    proxy.rotation_euler[2] = math.radians(15.0)
    return name


def export_glb(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=str(path), export_format="GLB", export_apply=True,
        export_yup=True, export_materials="EXPORT", export_cameras=False, export_lights=False,
    )


def main() -> None:
    args = cli_args()
    builders = {
        "straight": build_straight,
        "curve": build_curve,
        "slip_road": build_slip_road,
        "exit": build_exit,
    }
    selected = VARIANTS if args.variant == "all" else (args.variant,)
    for variant in selected:
        reset_scene()
        asphalt = material("bh_mat_asphalt_highway_a", (0.065, 0.07, 0.075, 1.0), 0.92)
        marking = material("bh_mat_road_marking_white_a", (0.9, 0.88, 0.78, 1.0), 0.7)
        asset_id = builders[variant](asphalt, marking)
        export_glb(Path(args.output_dir) / f"{asset_id}.glb")


if __name__ == "__main__":
    main()
