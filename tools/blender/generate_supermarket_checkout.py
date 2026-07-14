"""Generate a mobile-safe fictional supermarket checkout module."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
import bpy

def cli():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output-dir',default='build/generated/architecture/supermarket')
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
    aid='bh_prop_supermarket_checkout_a_01'
    body=bpy.data.materials.new('bh_mat_checkout_body_a');body.diffuse_color=(0.80,0.74,0.58,1)
    belt=bpy.data.materials.new('bh_mat_checkout_belt_a');belt.diffuse_color=(0.08,0.09,0.10,1)
    accent=bpy.data.materials.new('bh_mat_checkout_accent_a');accent.diffuse_color=(0.70,0.10,0.12,1)
    cube(aid,(2.6,0.85,0.78),(0,0,0.39),body)
    cube(f'{aid}_belt',(1.45,0.66,0.06),(-0.35,0,0.81),belt)
    cube(f'{aid}_scanner',(0.36,0.50,0.18),(0.68,0,0.90),accent)
    cube(f'{aid}_bag_well',(0.58,0.72,0.42),(1.02,0,0.99),body)
    cube(f'col_{aid}',(2.6,0.85,0.82),(0,0,0.41),collision=True)
    out=Path(a.output_dir)/f'{aid}.glb';out.parent.mkdir(parents=True,exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=str(out),export_format='GLB',export_apply=True,export_yup=True)
if __name__=='__main__':main()
