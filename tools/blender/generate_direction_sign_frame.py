"""Generate an unbranded bilingual-ready highway direction-sign frame."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
import bpy

def cli():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output-dir',default='build/generated/props/street')
    return p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
def cube(name,dims,loc,mat=None,collision=False):
    bpy.ops.mesh.primitive_cube_add(location=loc);o=bpy.context.object;o.name=name;o.dimensions=dims
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if mat:o.data.materials.append(mat)
    if collision:o.display_type='WIRE';o.hide_render=True;o['collision_proxy']=True
    return o
def main():
    a=cli();bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
    bpy.context.scene.unit_settings.system='METRIC';bpy.context.scene.unit_settings.scale_length=1.0
    aid='bh_prop_direction_sign_frame_a_01'
    metal=bpy.data.materials.new('bh_mat_sign_metal_a');metal.diffuse_color=(0.18,0.20,0.21,1)
    panel=bpy.data.materials.new('bh_mat_sign_panel_teal_a');panel.diffuse_color=(0.02,0.28,0.29,1)
    for x in (-3.2,3.2): cube(f'{aid}_pole_{x:+.1f}',(0.22,0.22,5.4),(x,0,2.7),metal)
    cube(f'{aid}_beam',(7.0,0.22,0.22),(0,0,5.15),metal)
    cube(f'{aid}_panel_left',(3.0,0.10,1.45),(-1.65,-0.12,4.25),panel)
    cube(f'{aid}_panel_right',(3.0,0.10,1.45),(1.65,-0.12,4.25),panel)
    # Blank panels intentionally contain no Arabic or English text; text is supplied by verified Godot textures.
    for x in (-3.2,3.2): cube(f'col_{aid}_pole_{x:+.1f}',(0.3,0.3,5.4),(x,0,2.7),collision=True)
    out=Path(a.output_dir)/f'{aid}.glb';out.parent.mkdir(parents=True,exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=str(out),export_format='GLB',export_apply=True,export_yup=True)
if __name__=='__main__':main()
