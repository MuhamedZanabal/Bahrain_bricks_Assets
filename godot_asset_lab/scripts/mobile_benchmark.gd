extends Node3D
## Controlled mobile benchmark scaffold for Bahrain Brick assets.
## Runtime measurements are valid only when executed in Godot 4.3 on target Android hardware.

const GENERATED_ROOT := "res://assets/generated"
const REPORT_PATH := "user://bahrain_brick_asset_benchmark.json"

@export_range(1, 200, 1) var target_instances: int = 40
@export_range(5.0, 120.0, 1.0) var sample_duration_seconds: float = 20.0
@export_range(1, 20, 1) var grid_columns: int = 8
@export_range(2.0, 30.0, 0.5) var grid_spacing: float = 7.0

var _started_at_msec: int
var _samples: Array[Dictionary] = []
var _available_scenes: Array[String] = []

func _ready() -> void:
	_build_stage()
	_available_scenes = _collect_scene_paths(GENERATED_ROOT)
	_spawn_controlled_instances()
	_started_at_msec = Time.get_ticks_msec()

func _process(_delta: float) -> void:
	var elapsed := (Time.get_ticks_msec() - _started_at_msec) / 1000.0
	_samples.append({
		"elapsed_seconds": elapsed,
		"fps": Performance.get_monitor(Performance.TIME_FPS),
		"process_seconds": Performance.get_monitor(Performance.TIME_PROCESS),
		"physics_process_seconds": Performance.get_monitor(Performance.TIME_PHYSICS_PROCESS),
		"draw_calls": Performance.get_monitor(Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME),
		"objects_in_frame": Performance.get_monitor(Performance.RENDER_TOTAL_OBJECTS_IN_FRAME),
		"static_memory_bytes": Performance.get_monitor(Performance.MEMORY_STATIC),
	})
	if elapsed >= sample_duration_seconds:
		_write_report()
		set_process(false)

func _build_stage() -> void:
	var floor := MeshInstance3D.new()
	var floor_mesh := BoxMesh.new()
	floor_mesh.size = Vector3(100.0, 0.2, 100.0)
	floor.mesh = floor_mesh
	floor.position.y = -0.1
	add_child(floor)

	var sun := DirectionalLight3D.new()
	sun.rotation_degrees = Vector3(-50.0, -35.0, 0.0)
	sun.light_energy = 1.0
	sun.shadow_enabled = true
	add_child(sun)

	var camera := Camera3D.new()
	camera.position = Vector3(30.0, 24.0, 36.0)
	camera.look_at_from_position(camera.position, Vector3.ZERO, Vector3.UP)
	camera.current = true
	add_child(camera)

func _spawn_controlled_instances() -> void:
	if _available_scenes.is_empty():
		push_warning("Benchmark has no generated GLB or TSCN assets to instantiate.")
		return
	for index in target_instances:
		var path := _available_scenes[index % _available_scenes.size()]
		if not ResourceLoader.exists(path, "PackedScene"):
			continue
		var packed := ResourceLoader.load(path, "PackedScene") as PackedScene
		if packed == null:
			continue
		var instance := packed.instantiate()
		var column := index % grid_columns
		var row := index / grid_columns
		if instance is Node3D:
			(instance as Node3D).position = Vector3(column * grid_spacing, 0.0, row * grid_spacing)
		add_child(instance)

func _write_report() -> void:
	var report := {
		"project": "Bahrain Brick Asset Lab",
		"godot_version": Engine.get_version_info(),
		"renderer": RenderingServer.get_video_adapter_name(),
		"target_instances": target_instances,
		"available_asset_scenes": _available_scenes.size(),
		"sample_duration_seconds": sample_duration_seconds,
		"samples": _samples,
		"status": "runtime_measurement",
	}
	var file := FileAccess.open(REPORT_PATH, FileAccess.WRITE)
	if file == null:
		push_error("Unable to write benchmark report: %s" % REPORT_PATH)
		return
	file.store_string(JSON.stringify(report, "\t"))
	file.close()
	print("Bahrain Brick benchmark report written: %s" % REPORT_PATH)

func _collect_scene_paths(root_path: String) -> Array[String]:
	var results: Array[String] = []
	var directory := DirAccess.open(root_path)
	if directory == null:
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
		elif entry.get_extension().to_lower() in PackedStringArray(["glb", "gltf", "tscn"]):
			results.append(full_path)
		entry = directory.get_next()
	directory.list_dir_end()
	return results
