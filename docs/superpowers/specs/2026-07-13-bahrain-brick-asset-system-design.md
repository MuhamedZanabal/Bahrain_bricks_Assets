# Bahrain Brick Asset System Design

## Objective

Create a license-first, mobile-budgeted, Bahrain-specific asset-production repository that can feed the Godot 4.3 Android game without mutating the game repository or importing unverified binaries.

## Architecture

The repository has five isolated layers:

1. **Evidence and policy** — authority audit, art bible, budgets, licenses and acceptance rules.
2. **Manifest control plane** — CSV/JSON sources of truth for every asset, district use, review state and Android status.
3. **Production references** — original SVG technical sheets, orthographic requirements and external-generation prompts.
4. **Procedural tooling** — deterministic Blender generators, naming/hash/texture validators and a Godot gallery scaffold.
5. **Promotion gate** — no asset can move into the game until license, scale, materials, collision, LOD, import and Android checks pass.

## Data flow

Candidate → provenance record → quarantine → concept/spec approval → source generation → processing → manifest update → isolated gallery import → Android benchmark → accepted package → downstream integration pull request.

## Failure policy

- Missing or unclear license: reject or quarantine.
- Missing archive checksum: reject.
- Naming or manifest mismatch: CI failure.
- Budget violation: reject unless profiling evidence approves an exception.
- Godot import or Android test failure: reject.
- Real branding, copied landmark geometry or signing secrets: hard reject.

## Scope boundary

This phase does not claim production-ready GLB, Blend, FBX, Android validation, or physical-device evidence. It produces executable specifications, deterministic technical concept sheets, procedural starter scripts and the isolated validation framework.
