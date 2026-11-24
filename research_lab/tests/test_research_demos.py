from research_lab.robotics.trajectory import generate_trajectory, measure_trajectory
from research_lab.trustworthy_ai.coverage import evaluate_coverage
from research_lab.scientific_ml.benchmark import benchmark_surrogate


def test_robot_trace_is_deterministic_and_measurable():
    first = generate_trajectory("noise", seed=4)
    second = generate_trajectory("noise", seed=4)
    assert (first == second).all()
    metrics = measure_trajectory(first, "noise")
    assert metrics.waypoints == 48
    assert metrics.path_length > 0
    assert metrics.total_turning >= 0


def test_gap_condition_reduces_waypoint_count():
    nominal = generate_trajectory("nominal", n=48)
    gaps = generate_trajectory("gaps", n=48)
    assert len(gaps) < len(nominal)


def test_trustworthy_ai_checklist_reports_missing_controls():
    result = evaluate_coverage("indirect_injection", {"instruction_boundary"})
    assert result["checklist_complete"] is False
    assert result["missing_controls"] == ["tool_allowlist"]


def test_trustworthy_ai_complete_checklist_is_not_claimed_as_safety_proof():
    result = evaluate_coverage("tool_misuse", {"tool_allowlist", "human_confirmation"})
    assert result["checklist_complete"] is True
    assert "not a safety guarantee" in result["interpretation"]


def test_scientific_ml_uses_held_out_data_and_is_deterministic():
    first = benchmark_surrogate(seed=11)
    second = benchmark_surrogate(seed=11)
    assert first == second
    assert first["training_samples"] + first["test_samples"] == first["samples"]
    assert first["test_samples"] > 0
    assert first["constant_baseline_rmse"] >= 0
    assert first["linear_surrogate_rmse"] >= 0
    assert first["synthetic"] is True
