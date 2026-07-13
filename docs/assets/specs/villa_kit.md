# Bahraini Villa Modular Kit — Production Specification

## Purpose

Residential kit for Riffa, Saar, Budaiya, Isa Town and suburban connectors. Original fictional designs only.

## Modules and dimensions

- wall solid: 3.0 m W × 3.2 m H × 0.25 m D
- wall window: same bay; opening 1.5 × 1.4 m, sill 0.9 m
- wall door: opening 1.1 × 2.3 m
- corner: 0.5 × 0.5 m structural return
- balcony: 3.0 × 1.25 m, 1.05 m rail
- parapet: 3.0 × 0.8 m
- gate pedestrian: 1.2 × 2.4 m
- gate vehicle: 4.0 × 2.6 m
- boundary wall: 4.0 × 2.2 m
- canopy: 5.5 × 5.5 m, 2.8 m clearance
- garage opening: 3.2 × 2.6 m
- stair: 1.2 m width, 0.17 m rise, 0.28 m going
- rooftop details: AC condenser, tank base, dish mount and service screen

## Variants

Modern white, beige plaster, sandstone accent, luxury corner and compact single-storey. Shared structure; palette/material variants do not duplicate geometry.

## Budget

- assembled villa LOD0: 6,000–12,000 visible triangles
- LOD1: 35–45%
- distant silhouette: 800–1,800 triangles
- materials: plaster trim atlas + glass + optional metal = maximum 3
- textures: one 1024 atlas; optional 512 detail/decals

## Collision

Box/prism collision per wall, slab and stair flight. Gates use separate interaction collision. AC, dish, plants and roof clutter have no collision unless gameplay requires it.

## Integration

Scene wrapper exposes `entrance_socket`, `driveway_socket`, `garage_socket`, `roof_service_socket` and optional `interior_portal`. Distance-shadow cutoff starts at 45 m; rooftop clutter culls at 35 m.
