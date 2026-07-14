@tool
extends Node3D
## Isolated asset-gallery scene for Bahrain Brick procedural and processed GLBs.
## It never reads from or mutates the production game repository.

const GENERATED_ROOT := "res://assets/generated"
const SUPPORTED_EXTENSIONS := PackedStringArray(["glb", "gltf", "tscn"])

@export_range(1, 12, 1) var grid_columns: int = 5
@export_range(2.0, 30.0, 0.5) var grid_spacing: float = 8.0
@export var rebuild_gallery: bool = false:
	set(value):
		rebuild_gallery = false
		if value and is_inside_tree():
			build_gallery()

var _asset_root: Node3D

func _ready() -> void:
	_build_stage()
	build_gallery()

func _build_stage() -> void:
	if get_node_or_null("GeneratedAssets") == null:
		_asset_root = Node3D.new()
		_asset_root.name = "GeneratedAssets"
		add_child(_asset_root)
	else:
		_asset_root = get_node("GeneratedAssets") as Node3D

	if get_node_or_null("GalleryFloor") == null:
		var floor := MeshInstance3D.new()
		floor.name = "GalleryFloor"
		var floor_mesh := BoxMesh.new()
		floor_mesh.size = Vector3(80.0, 0.2, 80.0)
		floor.mesh = floor_mesh
		floor.position.y = -0.1
		add_child(floor)

	if get_node_or_null("Sun") == null:
		var sun := DirectionalLight3D.new()
		sun.name = "Sun"
		sun.rotation_degrees = Vector3(-48.0, -32.0, 0.0)
		sun.light_energy = 1.1
		sun.shadow_enabled = true
		add_child(sun)

	if get_node_or_null("Camera") == null:
		var camera := Camera3D.new()
		camera.name = "Camera"
		camera.position = Vector3(24.0, 20.0, 30.0)
		camera.look_at_from_position(camera.position, Vector3.ZERO, Vector3.UP)
		camera.current = true
		add_child(camera)

func build_gallery() -> void:
	if _asset_root == null:
		_build_stage()
	for child in _asset_root.get_children():
		child.queue_free()

	var scene_paths := _collect_scene_paths(GENERATED_ROOT)
	scene_paths.sort()
	for index in scene_paths.size():
		var path := scene_paths[index]
		if not ResourceLoader.exists(path, "PackedScene"):
			push_warning("Asset gallery skipped unreadable scene: %s" % path)
			continue
		var packed := ResourceLoader.load(path, "PackedScene") as PackedScene
		if packed == null:
			push_warning("Asset gallery failed to load: %s" % path)
			continue
		var instance := packed.instantiate()
		instance.name = path.get_file().get_basename()
		var column := index % grid_columns
		var row := index / grid_columns
		if instance is Node3D:
			(instance as Node3D).position = Vector3(column * grid_spacing, 0.0, row * grid_spacing)
		_asset_root.add_child(instance)

	print("Bahrain Brick asset gallery loaded %d scene(s)." % scene_paths.size())

func _collect_scene_paths(root_path: String) -> Array[String]:
	var results: Array[String] = []
	var directory := DirAccess.open(root_path)
	if directory == null:
		push_warning("Generated asset directory is unavailable: %s" % root_path)
		return results

	directory.list_dir_begin()
	var entry := directory.get_next()
	while entry != "":
		if entry.begins_with("."):
			entry = directory.get_next()
			continue
		var full_path := root_path.path_join(entry)
		if directory.current_is_dir():
			results.append_array(_collect_scene_paths(full_path))
		elif entry.get_extension().to_lower() in SUPPORTED_EXTENSIONS:
			results.append(full_path)
		entry = directory.get_next()
	directory.list_dir_end()
	return results
