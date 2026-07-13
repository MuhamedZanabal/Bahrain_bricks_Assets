"""Generate a mobile-safe fictional Bahrain Brick bus shelter."""
from __future__ import annotations
import argparse,sys
from pathlib import Path
from _common import reset_scene,create_material,add_box,add_collision_box,export_glb

def build(output: Path)->None:
    reset_scene(); metal=create_material('bh_mat_painted_metal_charcoal',(0.08,0.09,0.10,1),roughness=0.5); glass=create_material('bh_mat_tinted_glass',(0.12,0.22,0.28,1),roughness=0.2); seat=create_material('bh_mat_warm_wood',(0.38,0.20,0.10,1),roughness=0.72)
    frame=add_box('bh_prop_bus_shelter_a_01_roof',(2.4,0.10,0.8),(0,2.65,0),metal)
    for x in (-2.25,2.25): add_box(f'bh_prop_bus_shelter_a_01_post_{x:+.2f}',(0.06,1.3,0.06),(x,1.3,0),metal)
    add_box('bh_prop_bus_shelter_a_01_back',(2.2,1.05,0.025),(0,1.35,0.74),glass)
    add_box('bh_prop_bus_shelter_a_01_seat',(1.5,0.08,0.28),(0,0.62,0.25),seat)
    add_collision_box(frame,'bh_col_prop_bus_shelter_a_01',(2.4,1.35,0.82),(0,1.35,0))
    export_glb(output/'bh_prop_bus_shelter_a_01.glb')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='build/generated/street')
    a=p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []);build(Path(a.output))
