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
