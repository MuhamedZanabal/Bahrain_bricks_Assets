extends Node3D

const GRID_COLUMNS := 6
const CELL_SIZE := 8.0

func _ready() -> void:
    _build_reference_grid()
    print("BAHRAIN BRICK ASSET GALLERY READY")

func _build_reference_grid() -> void:
    var floor_mesh := PlaneMesh.new()
    floor_mesh.size = Vector2(64.0, 64.0)
    var floor := MeshInstance3D.new()
    floor.name = "ReferenceFloor"
    floor.mesh = floor_mesh
    var material := StandardMaterial3D.new()
    material.albedo_color = Color("d9d1c2")
    material.roughness = 0.9
    floor.material_override = material
    add_child(floor)

func place_asset(scene: PackedScene, index: int, asset_id: String) -> Node3D:
    var instance := scene.instantiate() as Node3D
    instance.name = asset_id
    var row := index / GRID_COLUMNS
    var column := index % GRID_COLUMNS
    instance.position = Vector3(column * CELL_SIZE, 0.0, row * CELL_SIZE)
    add_child(instance)
    return instance
