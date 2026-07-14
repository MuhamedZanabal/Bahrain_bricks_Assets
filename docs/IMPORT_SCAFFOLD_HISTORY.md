# Import Scaffolding History

The original import-scaffolding commits remain in the immutable `main` history. Their workflow files were removed from the current tree because they contained force-push operations against `main`, which are prohibited by the accepted publication decision.

Preserved commits:

- `1e39bd47afd4947212916f5cb6acbb7fb1984886` — first verified-history importer.
- `9aba3b07bb4f8a33a02a88811d6a95db7a5934a2` — Phase 4 Batch 3 importer.
- `1a9a087c69080a940f89f2797f3746663a23cdd0` — Phase 5 importer.
- `cb7f1e7500d1793872dd663f32101e4a7205285f` — Phase 5 importer v2.
- `7a46e3fc8a9b3ff4cbe9496977ec7f88307652cd` — exact Drive-bundle importer containing the prohibited force update.

The current workflow verifies bundle SHA-256, byte size, bundle integrity, target ref, and exact commit, then creates only the non-protected archival branch using a non-force push.
