# Blender Export Standard

## Coordinate and scale

- Units: Metric, unit scale 1.0.
- 1 Blender unit = 1 metre.
- Apply location/rotation/scale before export.
- Godot forward: negative Z; up: positive Y after glTF import.
- Static-asset origin: ground centre unless a hinge/pivot is functionally required.
- Modular origins lie on the construction grid and mating edge.

## Mesh rules

- No non-manifold geometry unless explicitly justified.
- No duplicate faces, zero-area faces or unapplied negative scale.
- Triangulate on export or validate deterministic triangulation.
- Use hard edges/auto smooth intentionally; avoid accidental shading seams.
- UV0 required for all textured assets; UV1 only when baked lighting is approved.
- Keep separate objects only for functional pivots, material separation or LOD/collision.

## Naming

- Mesh: `<asset_id>_mesh_lod0`.
- LODs: `_lod0`, `_lod1`, `_lod2`.
- Collision: `<asset_id>_col_box_01`, `_col_convex_01`, or `_col_mesh_01`.
- Sockets/markers: `<asset_id>_socket_<purpose>`.
- Materials: `bh_mat_<family>_<variant>`.

## Export

- glTF 2.0 binary `.glb`.
- Export selected objects only.
- Include custom properties when used for sockets/metadata.
- Do not embed unrelated images or animations.
- Compression is a downstream, separately validated step.
- Output under `dist/glb/<category>/` and never directly into the game repository.
