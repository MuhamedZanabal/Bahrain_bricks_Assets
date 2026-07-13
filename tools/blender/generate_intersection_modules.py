"""Generate deterministic Bahrain Brick road intersection modules."""
from __future__ import annotations
import argparse, sys
from pathlib import Path
from _common import reset_scene, create_material, add_box, add_collision_box, export_glb


def _base(name: str, output: Path, arms: list[tuple[tuple[float,float,float], tuple[float,float,float]]]) -> None:
    reset_scene()
    asphalt=create_material('bh_mat_asphalt_worn',(0.10,0.105,0.11,1),roughness=0.92)
    white=create_material('bh_mat_road_marking_white',(0.92,0.91,0.82,1),roughness=0.65)
    slab=add_box(name,(10,0.10,10),(0,0,0),asphalt)
    for index,(half,loc) in enumerate(arms,1):
        add_box(f'{name}_mark_{index:02d}',half,loc,white)
    add_collision_box(slab,f'bh_col_{name[3:]}',(10,0.12,10),(0,0,0))
    export_glb(output/f'{name}.glb')


def build(output: Path) -> None:
    output.mkdir(parents=True,exist_ok=True)
    _base('bh_road_intersection_four_way_20m_01',output,[
        ((0.08,0.012,3.2),(0,0.112,-6.2)),((0.08,0.012,3.2),(0,0.112,6.2)),
        ((3.2,0.012,0.08),(-6.2,0.112,0)),((3.2,0.012,0.08),(6.2,0.112,0))])
    _base('bh_road_intersection_t_20m_01',output,[
        ((0.08,0.012,3.2),(0,0.112,-6.2)),((3.2,0.012,0.08),(-6.2,0.112,0)),
        ((3.2,0.012,0.08),(6.2,0.112,0))])

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--output',default='build/generated/roads')
    a=p.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
    build(Path(a.output))
