# Godot 4.3 Import Standard

## Isolation

All assets first enter `godot/asset_gallery/`. Production world scenes are not the first import target.

## Import checks

1. Godot 4.3 editor import completes with no parser, texture, mesh or dependency errors.
2. Scale test confirms known reference dimensions within ±1%.
3. Forward/up orientation and pivot are correct.
4. Materials are consolidated to budget.
5. Mesh LODs and visibility ranges are assigned.
6. Collision is explicit; auto-generated trimesh collision is forbidden for ordinary buildings and vehicles.
7. Static assets use static bodies or scene-level collision aggregation as appropriate.
8. Repeated props expose MultiMesh-compatible meshes.
9. Source archives and design files are excluded from export.

## Recommended resource placement

- Imported GLB: `assets/<category>/<asset_id>.glb`
- Reusable scene wrapper: `scenes/assets/<category>/<asset_id>.tscn`
- Shared material: `assets/materials/master/<material_id>.tres`
- Collision wrapper: within the scene wrapper, not destructively baked into the source GLB.

## Mobile renderer controls

- StandardMaterial3D or bounded mobile shader variants.
- Minimize transparency and per-instance shader variation.
- No ordinary-asset screen-space effects.
- Disable shadows beyond reviewed visibility distance.
- Use baked/static lighting only after memory and bake-size review.
