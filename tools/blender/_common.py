import bpy
from pathlib import Path

def reset_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def mat(name, color, roughness=0.7, metallic=0.0):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.diffuse_color=(*color,1.0); m.roughness=roughness; m.metallic=metallic
    return m

def cube(name, location, dimensions, material=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    o=bpy.context.object; o.name=name; o.dimensions=dimensions
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if material: o.data.materials.append(material)
    return o

def add_box_collision(source, suffix='col_box_01'):
    c=cube(f'{source.name}_{suffix}',source.location,source.dimensions,None)
    c.display_type='WIRE'; c.hide_render=True; c['collision_proxy']=True
    return c

def export_glb(path):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=str(path),export_format='GLB',use_selection=False,export_apply=True)

# Phase 4 canonical helper API. `half_extents` follows Godot BoxShape3D
# semantics and avoids ambiguity in procedural specifications.
def create_material(name, color, roughness=0.7, metallic=0.0):
    rgba = tuple(color)
    rgb = rgba[:3]
    return mat(name, rgb, roughness=roughness, metallic=metallic)


def add_box(name, half_extents, location=(0, 0, 0), material=None):
    dimensions = tuple(float(v) * 2.0 for v in half_extents)
    return cube(name, location, dimensions, material)


def add_collision_box(source, name, half_extents, location=(0, 0, 0)):
    dimensions = tuple(float(v) * 2.0 for v in half_extents)
    collision = cube(name, location, dimensions, None)
    collision.display_type = 'WIRE'
    collision.hide_render = True
    collision['collision_proxy'] = True
    collision['source_object'] = source.name
    return collision
