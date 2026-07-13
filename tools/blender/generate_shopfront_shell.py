#!/usr/bin/env python3
import argparse, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from _common import reset_scene,mat,cube,add_box_collision,export_glb

def build(output):
    reset_scene(); plaster=mat('bh_mat_plaster_beige',(0.78,0.67,0.51)); metal=mat('bh_mat_metal_shutter',(0.32,0.35,0.36),0.55,0.2); awning=mat('bh_mat_awning_red',(0.55,0.08,0.07),0.75)
    left=cube('bh_souq_shop_shell_left',(-1.3,0,1.6),(0.4,0.35,3.2),plaster); right=cube('bh_souq_shop_shell_right',(1.3,0,1.6),(0.4,0.35,3.2),plaster); top=cube('bh_souq_shop_shell_top',(0,0,2.9),(2.2,0.35,0.6),plaster)
    shutter=cube('bh_souq_shutter_01_mesh_lod0',(0,-0.04,1.35),(2.35,0.12,2.7),metal); canopy=cube('bh_souq_awning_01_mesh_lod0',(0,-0.8,2.65),(2.8,1.45,0.12),awning)
    for p in [left,right,top,shutter]: add_box_collision(p)
    export_glb(output)
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--output',default='dist/glb/souq/bh_souq_shopfront_starter.glb'); a=ap.parse_args(); build(a.output)
