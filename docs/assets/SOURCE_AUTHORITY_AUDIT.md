# Source Authority Audit — Read Only

Audit date: 2026-07-13

## Repository

- Source: `MuhamedZanabal/brick-bahrain-open-world`
- Default branch: `main`
- Default branch commit: `08378d1383eb7aeb1ae91b9eeb8994b79a96f1de`
- Default branch classification: original Godot 4.3 v12 source, not current premium authority.

## Authority hierarchy verified during this session

- Functional graphics baseline: `464a8811a818bd6bb9e102566e0a525396b11515`
- Frozen controls authority: `c5548465627942a2889a0bd09f8979c3a29fbcdd`
- Premium branch: `work/bahrain-brick-premium-visual-v14`
- Current premium branch head exposed by draft PR #14: `00a6ccc50caa9b23a70398da6854218fa7f2ebde`
- Earlier handover commit `31a21eff586f9b83ab1b0f6e900d55412dc77259` exists but is superseded by the current branch head.

## Important topology finding

The premium branch is not a clean directly checked-in reconstructed game tree. Its authority includes checksum-locked payload fragments and scripts that apply presentation/world overlays to a recovered project during CI. Consequently, root files such as `project.godot` and `export_presets.cfg` still expose stale v12 product values even at the premium branch head.

## Project configuration evidence

- Godot feature floor: 4.3.
- Root project feature string includes `Forward Plus`, but explicit renderer settings are `gl_compatibility` for desktop and mobile.
- Viewport: 1920 × 1080.
- Handheld orientation enum: 1.
- ETC2/ASTC import enabled.
- Root project name remains `Brick Bahrain: Open World`, not the official title.
- Root Android package label remains `Zanabal Gaming`.
- Root export preset stores debug/release keystore paths and passwords and points both profiles to the same debug keystore.

## Existing asset surface

The source `AssetLoader` declares:

- 14 generic buildings
- 4 skyscrapers
- 10 civilian/emergency vehicle meshes
- 6 palm variants
- 4 generic trees
- 4 nature props
- 3 road modules
- Flexible Toon and outline shaders

The loader comments describe the GLBs as Kenney CC0 assets, but the repository audit found no complete third-party notice evidence for the imported asset tree. That comment is not sufficient provenance.

## Existing license evidence

- Source-tree audit: 846 files scanned; 4 P0 and 3 P1 findings.
- Asset-license summary: 321 rows; 11 blocked; 310 require project provenance.
- Flexible Toon Shader upstream identity and MIT license were verified against `CaptainProton42/FlexibleToonShaderGD` at commit `dacf9a41d697a26360af96cdbf6332589cd97ab7`.
- Exact provenance of the bundled Godot 4 port remains unverified.
- Root project license was missing in the audited source.

## Mutation statement

No branch, file, commit, pull request, workflow, release or setting in `MuhamedZanabal/brick-bahrain-open-world` was modified by this asset-production phase.
