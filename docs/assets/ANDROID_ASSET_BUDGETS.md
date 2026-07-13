# Android Asset Budgets

Target baseline: Godot 4.3, `gl_compatibility`, 1280×720 internal render target on mid-range Android hardware.

## Geometry

| Class | LOD0 triangles | LOD1 target | Distant strategy |
|---|---:|---:|---|
| Minor prop | 50–1,000 | optional | distance cull |
| Medium prop | 500–3,000 | 40–60% | distance cull |
| Large prop | 2,000–8,000 | 35–50% | silhouette mesh |
| Small building | 500–3,000 | 35–50% | 1 mesh/material |
| Medium building | 3,000–12,000 | 30–45% | silhouette mesh |
| Tower | 5,000–20,000 | 25–40% | impostor/silhouette |
| Traffic vehicle | 4,000–12,000 | 35–50% mandatory | 500–1,500 tris |
| Player vehicle | 10,000–30,000 | 40–55% | 1,000–3,000 tris |
| NPC | 5,000–18,000 | 35–50% | low-bone LOD |

## Materials and textures

- Ordinary modular part: 1 material.
- Building kit: one shared trim/atlas material plus optional glass.
- Traffic vehicle: maximum 3 materials.
- Player vehicle: maximum 6 materials.
- Minor props: 256–512 px.
- Buildings and vehicles: 512–1024 px.
- Hero-only: 2048 px with written exception.
- No unapproved 4K/8K textures.
- Prefer ETC2/ASTC-compatible PNG/TGA sources; runtime import settings determine compression.

## Scene budgets

- Dense mobile vertical slice target: ≤ 900 visible MeshInstance3D nodes before MultiMesh consolidation.
- Opaque materials preferred; transparent surfaces limited to glass, water and carefully bounded VFX.
- Dynamic shadow-casting lights: target 1 sun + 0–4 local lights in view.
- Repeated vegetation/props: MultiMesh mandatory after 25 identical instances per cell.
- Outline second pass: hero characters/vehicles only; never the full city.

## Memory and package controls

- Asset gallery cold-load target: < 8 s on reference phone.
- Vertical-slice texture memory target: < 512 MiB estimated residency.
- New asset package APK delta target per reviewed batch: < 150 MiB.
- Archive and source files are excluded from Android export.
- x86_64 export is QA-only unless product requirements prove otherwise.
