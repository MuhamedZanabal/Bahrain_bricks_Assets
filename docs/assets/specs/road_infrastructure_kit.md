# Road Infrastructure Kit — Production Specification

## Scope
A metric modular road family for Godot 4.3 mobile: 20 m straight segments, junctions, roundabouts, highway pieces, service roads, kerbs, sidewalks, crossings, drainage, signs, barriers and decals.

## Grid and orientation
- Module length: 20 m primary, 10 m secondary adapters.
- Godot forward: negative Z.
- Road crown: 1.5–2.0% visual slope only where drainage readability requires it.
- Two-lane carriageway: 8 m total; four-lane divided: 16 m plus median; six-lane: 24 m plus median.
- Kerb height: 0.15 m; sidewalk width: 1.8 m residential, 3.0–6.0 m commercial/waterfront.

## Required modules
Straight two-lane, four-lane and six-lane; T-junction; four-way intersection; roundabout; slip road; highway exit; bridge deck; tunnel portal; ramp; parking lane; service road; coastal road; desert road; dirt track; pedestrian crossing; bus bay; taxi bay; driveway cut.

## Budgets
- Road mesh: 300–2,500 triangles per 20 m module.
- Junction: 1,500–6,000 triangles.
- Materials: 1 atlas plus optional decal material.
- Texture: 1024 atlas maximum; decals 512–1024.
- Collision: one static concave road mesh only where required; otherwise boxes/prisms.
- LOD: LOD0, LOD1 at 40–55%, distant flat silhouette or merged sector.

## Godot integration
Each GLB becomes a reusable PackedScene with MeshInstance3D, StaticBody3D collision, navigation exclusion metadata, lane sockets, sidewalk sockets and district palette metadata. Repeated road props use MultiMeshInstance3D.
