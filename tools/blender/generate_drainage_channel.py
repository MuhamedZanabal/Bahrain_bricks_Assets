"""Generate a 4 m roadside drainage-channel module for Bahrain Brick."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
import bpy

def cli():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--output-dir',default='build/generated/roads')
    return p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
def cube(name,dims,loc,mat=None,collision=False):
    bpy.ops.mesh.primitive_cube_add(location=loc); o=bpy.context.object; o.name=name; o.dimensions=dims
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if mat:o.data.materials.append(mat)
    if collision:o.display_type='WIRE';o.hide_render=True;o['collision_proxy']=True
    return o
def main():
    a=cli(); bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    bpy.context.scene.unit_settings.system='METRIC'; bpy.context.scene.unit_settings.scale_length=1.0
    aid='bh_drainage_channel_straight_4m_01'; m=bpy.data.materials.new('bh_mat_drain_concrete_a');m.diffuse_color=(0.42,0.40,0.36,1)
    cube(aid,(0.7,4.0,0.10),(0,0,0.05),m); cube(f'{aid}_edge_l',(0.12,4.0,0.24),(-0.35,0,0.12),m);cube(f'{aid}_edge_r',(0.12,4.0,0.24),(0.35,0,0.12),m)
    cube(f'col_{aid}',(0.94,4.0,0.24),(0,0,0.12),collision=True)
    out=Path(a.output_dir)/f'{aid}.glb';out.parent.mkdir(parents=True,exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=str(out),export_format='GLB',export_apply=True,export_yup=True)
if __name__=='__main__':main()
