# Road Intersections and Transit Kit

## Scope

Original modular road infrastructure for Bahrain Brick: four-way intersection, T-junction, compact roundabout, zebra crossing, traffic signal, crash barrier, and bus shelter. No real authority branding or copied sign layouts.

## Grid and scale

- Metric units; Godot forward is negative Z.
- Road modules use 20 m or 24 m square footprints and snap to a 1 m grid.
- Carriageway width: 8 m for standard two-lane streets.
- Sidewalk interface height: 0.15 m.
- Pivot: ground centre for road modules; ground-centred on props.

## Budgets

| Asset | LOD0 triangles | Materials | Texture maximum | Collision |
|---|---:|---:|---:|---|
| Intersection | 300–3,000 | 1–2 | 1024 | one static slab |
| Roundabout | 500–4,000 | 1–3 | 1024 | slab plus island cylinder |
| Crossing | 32–256 | 1 | 512 | none |
| Traffic signal | 250–1,200 | 2–4 | 512 | pole box |
| Crash barrier | 100–700 | 1 | 512 | single box |
| Bus shelter | 400–2,000 | 2–3 | 512 | simplified envelope |

## LOD and distance

- Road modules: LOD1 removes raised marking geometry; distant roads use atlas/decal treatment.
- Signals and shelters: LOD1 at 35–45% triangles; hide under 8 projected pixels.
- Crossing geometry disables beyond 80 m and is replaced by road-atlas markings.

## Android gate

Benchmark at least four intersections, one roundabout, eight signals, 16 barriers, two shelters, and 12 crossing modules in view. Record draw calls, frame time, visible objects, and memory before acceptance.
