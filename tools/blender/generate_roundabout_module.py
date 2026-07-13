"""Generate a compact low-poly roundabout module."""
from __future__ import annotations
import argparse,sys
from pathlib import Path
import bpy
from _common import reset_scene,create_material,add_box,add_collision_box,export_glb

def build(output: Path)->None:
    reset_scene()
    asphalt=create_material('bh_mat_asphalt_worn',(0.10,0.105,0.11,1),roughness=0.92)
    concrete=create_material('bh_mat_concrete_light',(0.62,0.60,0.55,1),roughness=0.88)
    slab=add_box('bh_road_roundabout_compact_24m_01',(12,0.10,12),(0,0,0),asphalt)
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=4.2,depth=0.32,location=(0,0.16,0))
    island=bpy.context.object; island.name='bh_road_roundabout_compact_24m_01_island'; island.data.materials.append(concrete)
    add_collision_box(slab,'bh_col_road_roundabout_compact_24m_01',(12,0.12,12),(0,0,0))
    export_glb(output/'bh_road_roundabout_compact_24m_01.glb')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='build/generated/roads')
    a=p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []);build(Path(a.output))
