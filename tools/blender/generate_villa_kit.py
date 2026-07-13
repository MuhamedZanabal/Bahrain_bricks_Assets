#!/usr/bin/env python3
import argparse, math, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from _common import reset_scene,mat,cube,add_box_collision,export_glb

def build(output):
    reset_scene()
    plaster=mat('bh_mat_plaster_warm_white',(0.88,0.82,0.72),0.82)
    wood=mat('bh_mat_wood_warm',(0.27,0.13,0.07),0.65)
    glass=mat('bh_mat_glass_dark',(0.05,0.18,0.23),0.25)
    parts=[]
    parts.append(cube('bh_villa_wall_solid_01_mesh_lod0',(0,0,1.6),(3,0.25,3.2),plaster))
    left=cube('bh_villa_wall_window_01_left',(-1.15,4,1.6),(0.7,0.25,3.2),plaster)
    right=cube('bh_villa_wall_window_01_right',(1.15,4,1.6),(0.7,0.25,3.2),plaster)
    top=cube('bh_villa_wall_window_01_top',(0,4,2.75),(1.6,0.25,0.9),plaster)
    sill=cube('bh_villa_wall_window_01_sill',(0,4,0.45),(1.6,0.25,0.9),plaster)
    window=cube('bh_villa_wall_window_01_glass',(0,3.97,1.6),(1.5,0.04,1.4),glass)
    gate=cube('bh_villa_gate_vehicle_01_mesh_lod0',(0,8,1.3),(4,0.16,2.6),wood)
    boundary=cube('bh_villa_boundary_wall_01_mesh_lod0',(0,12,1.1),(4,0.25,2.2),plaster)
    for p in [parts[0],left,right,top,sill,gate,boundary]: add_box_collision(p)
    export_glb(output)
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--output',default='dist/glb/villas/bh_villa_modular_starter.glb'); a=ap.parse_args(); build(a.output)
