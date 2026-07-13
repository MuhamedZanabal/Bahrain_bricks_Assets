# Bahrain Bay-Inspired Waterfront Kit — Production Specification

## Purpose

Premium fictional waterfront supporting promenade exploration, hotels, cafés, marinas and skyline composition without copying landmark geometry.

## Modules and dimensions

- straight promenade: 10 m and 20 m lengths, 6 m usable width
- curved promenade: 15°, 30° and 45° segments, 20 m design radius
- marina edge: 5 m module, 1.1 m rail, 0.45 m coping
- water stairs: 4 m W, non-enterable unless gameplay requires
- café terrace: 8 × 6 m
- planter: 2 × 2 m and 4 × 1.2 m
- bench socket every 8–12 m
- light spacing: 12–18 m
- hotel drop-off: 24 m loop module
- tower podium: 24 × 24 m and 36 × 24 m modules

## Tower language

Original clean silhouettes using tapered slabs, offset crowns, fins, rounded corners and restrained dark/blue glass. No Bahrain landmark tracing.

## Budget

- promenade module: 300–1,500 triangles
- street furniture set: 150–1,200 each
- tower LOD0: 8,000–18,000 triangles
- tower LOD1: 25–35%
- skyline silhouette: 300–1,000 triangles
- shared materials: pavement, rail/metal, glass, plaster/stone, water edge

## Collision and LOD

Promenade collision uses simple slabs/rails. Water edge uses a continuous safety barrier. Furniture uses boxes/capsules where necessary. Small props and terrace furniture cull at 45 m; tower window geometry is forbidden and represented through materials.
