# Bahrain Brick Godot Asset Lab

## Authority and isolation

`godot_asset_lab/` is a standalone **Godot 4.3** GL Compatibility project used only for asset import review and Android benchmark preparation. It does not import, modify or duplicate protected player-control, joystick, touch-routing, HUD-input, camera-authority or movement files from `brick-bahrain-open-world`.

## Asset-gallery workflow

1. Run the approved Blender generators externally.
2. Copy generated `.glb`, `.gltf` or controlled `.tscn` files under `godot_asset_lab/assets/generated/` using the Bahrain Brick naming standard.
3. Open `godot_asset_lab/project.godot` with Godot 4.3.
4. Run `scenes/asset_gallery.tscn`.
5. Inspect scale, pivot, material replacement, normals, collision-proxy naming, seams and silhouette.
6. Record screenshots and import warnings under `docs/assets/evidence/`.

The gallery discovers only `res://assets/generated`. It does not scan the production game repository.

## Mobile benchmark scaffold

Run `scenes/mobile_benchmark.tscn` after generated assets have passed visual inspection. The script creates a controlled grid and records:

- FPS.
- process and physics frame time.
- draw calls.
- visible objects.
- static memory.
- Godot and renderer information.

The report is written at runtime to `user://bahrain_brick_asset_benchmark.json`.

## Android acceptance

A benchmark result is valid only when the project is exported with Godot 4.3 GL Compatibility and executed on a physical Android device. Capture device model, Android version, graphics quality, thermal state, instance count, load time, crash status, screenshot and profiler evidence. Emulator-only evidence must be labelled separately.

## Current validation status

- Project structure: specified and structurally tested.
- Godot parser/import execution: **not run**.
- GLB import: **not run**.
- Android export: **not run**.
- Physical-device benchmark: **not run**.
