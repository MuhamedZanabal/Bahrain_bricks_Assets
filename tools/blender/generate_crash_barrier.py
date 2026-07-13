"""Generate a modular 4 m highway crash barrier."""
from __future__ import annotations
import argparse,sys
from pathlib import Path
from _common import reset_scene,create_material,add_box,add_collision_box,export_glb

def build(output: Path)->None:
    reset_scene(); metal=create_material('bh_mat_galvanized_metal',(0.42,0.44,0.45,1),roughness=0.55,metallic=0.65)
    rail=add_box('bh_prop_crash_barrier_4m_01_rail',(2.0,0.16,0.05),(0,0.65,0),metal)
    for x in (-1.7,0,1.7): add_box(f'bh_prop_crash_barrier_4m_01_post_{int((x+2)*10):02d}',(0.05,0.45,0.05),(x,0.45,0),metal)
    add_collision_box(rail,'bh_col_prop_crash_barrier_4m_01',(2.0,0.45,0.08),(0,0.45,0))
    export_glb(output/'bh_prop_crash_barrier_4m_01.glb')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='build/generated/street')
    a=p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []);build(Path(a.output))
