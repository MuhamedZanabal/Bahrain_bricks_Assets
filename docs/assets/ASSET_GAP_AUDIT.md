# Ruthless Asset-Gap Audit

## Current usable inventory

**Accepted production binaries: zero.**

The game repository contains or references generic models and shaders, but the binary asset groups lack sufficient per-archive provenance, creator, source revision, archive checksum and acceptance evidence for promotion into the controlled asset repository.

## Critical gaps

1. No Bahrain-specific modular architecture kits.
2. No controlled road/intersection/kerb/sign system.
3. No consistent fictional vehicle family with pivots, seats, anchors, LODs and collisions.
4. No shared-rig multicultural NPC family or canonical animation library.
5. No controlled material/trim/atlas library.
6. No verified source/attribution ledger for existing external GLBs.
7. No isolated asset gallery or controlled Android benchmark scene.
8. No repeatable Blender export and Godot import contract.
9. No district-to-asset coverage matrix.
10. No acceptance gate tying licensing, geometry, materials, textures, collision, LOD and Android evidence together.

## High-risk inherited conditions

- Stale title and package labels in the root project tree.
- Debug signing material and passwords in versioned export configuration.
- Overlay/payload-based premium authority rather than a clean reconstructed source tree.
- Full-scene material overrides may erase authored PBR distinctions and increase shader/material churn.
- Outline second passes can approximately double affected draw submissions.
- Broad `export_filter="all_resources"` risks shipping unused assets.
- x86_64 Android architecture increases APK size unless explicitly required for emulator QA.

## Production priority

1. License/provenance control plane.
2. Four architecture kits and shared materials.
3. Road kit and street props.
4. Vehicle family.
5. NPC rig and animation set.
6. Coastal/desert vegetation and water.
7. UI/audio/branding.
8. One vertical-slice asset package and Android benchmark.
