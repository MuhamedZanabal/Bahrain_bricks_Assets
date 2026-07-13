# Manama Souq Modular Kit — Production Specification

## Purpose

Dense fictional market streets supporting retail, delivery, browsing and mission routes.

## Shop modules

Gold/jewellery, spice, tailoring, perfume, electronics, fabric, toy, grocery, café, bakery and souvenir façade variants. All names are fictional; Arabic text remains placeholder geometry until linguistically verified.

## Dimensions

- standard shop bay: 3.0 m W × 3.2 m H
- narrow bay: 2.2 m W
- double bay: 6.0 m W
- shutter: 2.4–2.8 m clear width
- awning projection: 1.2–1.8 m
- covered passage: 3.0–4.0 m clear width
- display-table footprint: 1.2 × 0.7 m
- delivery opening: 2.4 × 2.6 m

## Budget

- shop shell: 1,000–3,500 triangles
- prop dressing set per bay: 500–2,000 triangles
- material budget: façade atlas, signage atlas, glass/metal = maximum 3
- shared 1024 façade trim, 1024 signage atlas, 512 prop atlas

## Collision and interaction

Shell collision uses boxes. Shutters and doors receive separate interaction shapes. Display tables/crates use simple boxes only when they block movement. Hanging lamps/awnings do not collide.

## LOD

At 35 m, remove interior cards, small merchandise, cables and hanging lamps. At 70 m, collapse façade to one material and signage color block.
