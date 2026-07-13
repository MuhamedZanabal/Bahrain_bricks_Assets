extends Node3D

var start_ms := 0
var samples: Array[float] = []

func _ready() -> void:
    start_ms = Time.get_ticks_msec()
    print("BENCHMARK_START")

func _process(_delta: float) -> void:
    samples.append(Performance.get_monitor(Performance.TIME_FPS))
    if Time.get_ticks_msec() - start_ms >= 10000:
        var total := 0.0
        for value in samples: total += value
        var avg := total / max(samples.size(), 1)
        print("BENCHMARK_RESULT fps_avg=%.2f objects=%d draw_calls=%d video_mem=%d" % [avg, Performance.get_monitor(Performance.OBJECT_NODE_COUNT), Performance.get_monitor(Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME), Performance.get_monitor(Performance.RENDER_VIDEO_MEM_USED)])
        get_tree().quit(0)
