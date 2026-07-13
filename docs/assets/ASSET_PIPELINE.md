# Asset Pipeline

## States

`idea → specified → concept_approved → source_created → processed → gallery_imported → desktop_pass → android_pass → accepted → promoted`

`quarantined` and `rejected` are terminal until new evidence is supplied.

## Intake contract

Every candidate receives an `ASSET_MASTER_MANIFEST.csv` row before its binary is copied into the repository. Third-party candidates additionally require source URL, creator, license URL, source revision, download date and archive SHA-256.

## Processing sequence

1. Preserve original archive in `_source_archives` outside Android export.
2. Record SHA-256 before extraction.
3. Scan archive for license and unexpected executables/secrets.
4. Normalize names and metric scale.
5. Reduce materials and textures.
6. Build explicit collision and LODs.
7. Export GLB.
8. Import into isolated Godot gallery.
9. Run acceptance scripts and visual review.
10. Run Android benchmark.
11. Mark accepted only when every mandatory field passes.

## Promotion package

A promoted package contains processed GLB/PNG/OGG/SVG resources, scene wrappers, material resources, license notice, manifest subset, checksums and benchmark evidence. Source Blend files and archives remain in the asset repository or large-file storage, never silently mixed into the game tree.
