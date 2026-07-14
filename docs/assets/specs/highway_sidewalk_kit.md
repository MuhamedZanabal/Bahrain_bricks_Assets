# Bahrain Brick Highway, Sidewalk and Drainage Kit — Phase 4 Batch 3

## Scope

This kit defines original, fictionalized Bahrain-inspired highway and pedestrian infrastructure for **Godot 4.3 Android**. It does not reproduce an exact road, interchange, sign face or restricted transport drawing.

## Controlled modules

| Asset ID | Nominal dimensions | Triangle target | Materials | Texture ceiling |
|---|---:|---:|---:|---:|
| `bh_road_highway_six_lane_straight_40m_01` | 18 × 40 m | 600–1,800 | 2 | 1024 px shared atlas |
| `bh_road_highway_curve_40m_01` | 18 m carriageway, 64° arc | 1,000–2,500 | 2 | 1024 px shared atlas |
| `bh_road_highway_slip_road_30m_01` | 18 × 30 m plus merge lane | 700–2,000 | 2 | 1024 px shared atlas |
| `bh_road_highway_exit_40m_01` | 18 × 40 m plus diverge lane | 700–2,000 | 2 | 1024 px shared atlas |
| `bh_sidewalk_commercial_straight_4m_01` | 3 × 4 m | 80–300 | 2 | 512 px atlas |
| `bh_sidewalk_driveway_cut_4m_01` | 3 × 4 m | 100–400 | 2 | 512 px atlas |
| `bh_drainage_channel_straight_4m_01` | 0.94 × 4 m | 80–250 | 1 | 512 px atlas |
| `bh_prop_direction_sign_frame_a_01` | 7 × 0.3 × 5.4 m | 250–800 | 2 | 512 px atlas plus verified sign-face texture |

## Modular construction

- Metric scale; one Blender unit equals one metre.
- Road origins sit at module ground centre. Forward is negative Z after Godot import; module length is represented on Blender Y before glTF conversion.
- Road ends must terminate on exact 0.5 m grid increments.
- Sign panels remain blank in source geometry. Arabic and English sign-face textures require spelling review before integration.
- Materials use shared asphalt, marking, pavement, kerb, concrete-drain and painted-metal definitions.

## Collision

- Straight carriageways use one box proxy.
- Curves use three to five coarse rotated boxes; no trimesh collision on mobile.
- Slip roads and exits use one main box and one rotated branch box.
- Sidewalk and drainage collision excludes decorative recesses.
- Sign collision is limited to support poles; panels are non-colliding unless gameplay proves otherwise.

## LOD and distance strategy

- `LOD0`: full markings and all support geometry.
- `LOD1`: remove small markings and reduce curved-road radial segments by approximately 50%.
- Distant: shared flat asphalt strip or district road impostor; sign text disabled beyond readability distance.
- Disable decorative road reflectors and drain detail beyond 35 m on medium Android quality.

## Godot 4.3 import

1. Import GLB with generated tangents and material extraction disabled by default.
2. Replace embedded materials with controlled `.tres` resources.
3. Convert `col_` objects into `StaticBody3D` collision children in the asset-gallery scene.
4. Verify module seam tolerance under 2 mm.
5. Keep these assets isolated from protected player, joystick, touch-routing and camera-authority files.

## Android acceptance requirement

The module is not approved until the asset-gallery benchmark confirms correct scale, no visible seams, collision stability at driving speed, no shader warnings, and acceptable draw-call impact on a physical Android device. Current status: **not run**.
