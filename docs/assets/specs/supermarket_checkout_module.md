# Bahrain Brick Supermarket Checkout Module

## Purpose

An original fictional checkout counter for a Bahrain-inspired neighborhood supermarket, designed for **Godot 4.3 Android** and compatible with the broader supermarket kit.

## Dimensions and budget

- Overall footprint: approximately 2.6 × 0.85 m.
- Counter height: 0.78 m; scanner surface approximately 0.90 m.
- Target: 300–1,200 visible triangles.
- Maximum three materials using a shared 512–1024 px interior-commercial atlas.
- No real retailer branding, logos, copied product packaging or price text.

## Components

- Main counter body.
- Dark conveyor belt.
- Scanner housing.
- Bagging well.
- Optional separate barcode scanner, receipt roll and payment terminal in a later prop batch.

## Collision

Use one box collision proxy around the counter body. Scanner and bagging details remain non-colliding. NPC queue and cashier interaction markers belong in the Godot scene, not the mesh.

## LOD

- `LOD0`: all listed components.
- `LOD1`: merge scanner and bagging well into the body; target 50% or less of LOD0 triangles.
- Distant interior culling: disable beyond the supermarket room portal or 30 m.

## Godot 4.3 integration

Import to the isolated supermarket gallery scene, replace embedded materials with controlled `.tres` resources, and attach cashier, customer queue, conveyor-start and payment interaction markers as separate `Marker3D` nodes.

## Android validation

Required before approval: physical-device import, collision, NPC navigation clearance, material, draw-call and memory tests. Current status: **not run**.
