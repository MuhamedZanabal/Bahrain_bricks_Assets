"""Generate commercial sidewalk and driveway-cut modules for Bahrain Brick."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
import bpy


def args():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output-dir', default='build/generated/roads')
    p.add_argument('--variant', choices=('all','straight','driveway_cut'), default='all')
    return p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])

def reset():
    bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    bpy.context.scene.unit_settings.system='METRIC'; bpy.context.scene.unit_settings.scale_length=1.0

def mat(name, color):
    m=bpy.data.materials.new(name); m.diffuse_color=color; return m

def cube(name, dims, loc, material=None, collision=False):
    bpy.ops.mesh.primitive_cube_add(location=loc); o=bpy.context.object; o.name=name; o.dimensions=dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if material: o.data.materials.append(material)
    if collision: o.display_type='WIRE'; o.hide_render=True; o['collision_proxy']=True
    return o

def export(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.export_scene.gltf(filepath=str(path), export_format='GLB', export_apply=True, export_yup=True)

def straight(output):
    reset(); concrete=mat('bh_mat_pavement_warm_a',(0.58,0.54,0.46,1)); kerb=mat('bh_mat_kerb_light_a',(0.78,0.75,0.66,1))
    aid='bh_sidewalk_commercial_straight_4m_01'
    cube(aid,(3.0,4.0,0.18),(0,0,0.09),concrete); cube(f'{aid}_kerb',(0.28,4.0,0.30),(1.36,0,0.15),kerb)
    cube(f'col_{aid}',(3.0,4.0,0.18),(0,0,0.09),collision=True)
    export(output/f'{aid}.glb')

def driveway(output):
    reset(); concrete=mat('bh_mat_pavement_warm_a',(0.58,0.54,0.46,1)); kerb=mat('bh_mat_kerb_light_a',(0.78,0.75,0.66,1))
    aid='bh_sidewalk_driveway_cut_4m_01'
    cube(aid,(3.0,4.0,0.12),(0,0,0.06),concrete)
    left=cube(f'{aid}_ramp_left',(1.2,1.1,0.18),(-0.75,0,0.14),kerb); left.rotation_euler[1]=0.10
    right=cube(f'{aid}_ramp_right',(1.2,1.1,0.18),(0.75,0,0.14),kerb); right.rotation_euler[1]=-0.10
    cube(f'col_{aid}',(3.0,4.0,0.16),(0,0,0.08),collision=True)
    export(output/f'{aid}.glb')

def main():
    a=args(); output=Path(a.output_dir)
    if a.variant in ('all','straight'): straight(output)
    if a.variant in ('all','driveway_cut'): driveway(output)
if __name__=='__main__': main()
