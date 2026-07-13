#!/usr/bin/env python3
import argparse, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from _common import reset_scene,mat,cube,add_box_collision,export_glb

def build(output):
    reset_scene(); paving=mat('bh_mat_promenade_paving',(0.64,0.60,0.52),0.8); metal=mat('bh_mat_railing_brushed',(0.15,0.18,0.20),0.35,0.65); wateredge=mat('bh_mat_wateredge_stone',(0.52,0.49,0.44),0.85)
    deck=cube('bh_waterfront_promenade_10m_01_mesh_lod0',(0,0,0),(10,6,0.3),paving); edge=cube('bh_waterfront_marina_edge_01_mesh_lod0',(0,-3,0.4),(10,0.5,0.8),wateredge)
    add_box_collision(deck); add_box_collision(edge)
    for x in [-4.5,-1.5,1.5,4.5]:
        cube(f'bh_waterfront_railing_post_{x:+.1f}',(x,-2.75,1.0),(0.08,0.08,1.2),metal)
    cube('bh_waterfront_railing_top',(0,-2.75,1.55),(10,0.08,0.08),metal)
    export_glb(output)
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--output',default='dist/glb/waterfront/bh_waterfront_promenade_starter.glb'); a=ap.parse_args(); build(a.output)
