.PHONY: validate test checksums
validate:
	python3 tools/validate_manifests.py
	python3 -m unittest discover -s tests -v
	python3 -m py_compile tools/*.py tools/blender/*.py tests/*.py

test: validate

checksums:
	find docs tools godot tests -type f -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS
