"""Generate reusable pedestrian crossing decal geometry."""
from __future__ import annotations
import argparse,sys
from pathlib import Path
from _common import reset_scene,create_material,add_box,export_glb

def build(output: Path)->None:
    reset_scene(); white=create_material('bh_mat_road_marking_white',(0.92,0.91,0.82,1),roughness=0.65)
    for i in range(8):
        add_box(f'bh_road_crossing_zebra_8m_01_stripe_{i+1:02d}',(0.34,0.006,3.8),(-3.15+i*0.9,0.006,0),white)
    export_glb(output/'bh_road_crossing_zebra_8m_01.glb')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='build/generated/roads')
    a=p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []);build(Path(a.output))
