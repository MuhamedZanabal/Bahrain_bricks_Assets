.PHONY: validate test checksums verify-checksums

validate: verify-checksums
	python3 tools/validate_manifests.py
	python3 -m unittest discover -s tests -v
	python3 -m py_compile tools/*.py tools/blender/*.py tests/*.py


test: validate


checksums:
	python3 tools/source_integrity.py generate --root . --ledger SHA256SUMS


verify-checksums:
	python3 tools/source_integrity.py verify --root . --ledger SHA256SUMS
