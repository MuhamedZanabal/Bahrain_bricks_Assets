# Bahrain Brick Asset System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans task-by-task.

**Goal:** Establish the controlled asset foundation and first four architecture kits for Bahrain Brick.

**Architecture:** Separate evidence, manifests, production references, generators and promotion tests. The game repository is read-only; asset promotion occurs only after independent acceptance.

**Tech Stack:** Git, CSV/JSON, Python 3.11+, Blender Python API, Godot 4.3 GDScript, SVG, GitHub Actions.

## Global Constraints

- Official title: Bahrain Brick.
- Engine compatibility target: Godot 4.3.
- Renderer target: `gl_compatibility` mobile path.
- Primary platform: Android landscape.
- Lowercase snake_case asset names with `bh_` prefix.
- No unverified third-party binaries.
- No protected controls or signing material.

---

### Task 1: Authority and provenance audit

**Files:** `docs/assets/SOURCE_AUTHORITY_AUDIT.md`, `docs/assets/ASSET_GAP_AUDIT.md`, `docs/assets/LICENSES.md`

- [x] Record source repository, baseline commits, current premium head and superseded handover commit.
- [x] Record renderer, project-title, package-label and signing inconsistencies.
- [x] Quarantine all existing external asset groups lacking complete source evidence.
- [x] Commit the audit.

### Task 2: Standards and manifests

**Files:** `docs/assets/*.md`, `docs/assets/*.csv`, `docs/assets/ASSET_STATUS.json`

- [x] Create art bible, Android budgets, Blender export, Godot import and pipeline standards.
- [x] Create exact manifest headers and seeded production rows.
- [x] Add validation tests.
- [x] Commit the standards.

### Task 3: First architecture production batch

**Files:** `docs/assets/specs/*.md`, `docs/assets/concepts/*.svg`

- [x] Produce villa, traditional, souq and waterfront technical specifications.
- [x] Produce original orthographic/exploded SVG sheets.
- [x] Register every module in the master manifest and district matrix.
- [x] Commit the batch.

### Task 4: Procedural and gallery scaffolding

**Files:** `tools/`, `godot/asset_gallery/`, `.github/workflows/validate-assets.yml`

- [x] Add deterministic Blender generators for representative modules.
- [x] Add naming, CSV, hash and texture validation tooling.
- [x] Add Godot 4.3 gallery and benchmark scaffolding.
- [x] Run Python unit and manifest validation.
- [ ] Run Blender and Godot import tests when executables become available.
- [ ] Run physical Android benchmark and capture profiler evidence.
