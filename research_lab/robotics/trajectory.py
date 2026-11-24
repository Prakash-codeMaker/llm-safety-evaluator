"""Synthetic robot-demonstration trajectory quality checks.

All data generated here are synthetic 2-D traces, not physical-robot telemetry.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np


@dataclass(frozen=True)
class TrajectoryMetrics:
    waypoints: int
    path_length: float
    total_turning: float
    mean_step: float
    condition: str


def generate_trajectory(condition: str = "nominal", n: int = 48, seed: int = 7) -> np.ndarray:
    if condition not in {"nominal", "noise", "drift", "gaps"}:
        raise ValueError("condition must be nominal, noise, drift, or gaps")
    if n < 8:
        raise ValueError("n must be at least 8")

    t = np.linspace(0.0, 1.0, n)
    points = np.column_stack((100.0 * t, 50.0 + 18.0 * np.sin(2.0 * np.pi * t)))
    rng = np.random.default_rng(seed)

    if condition == "noise":
        points += rng.normal(0.0, 1.25, size=points.shape)
    elif condition == "drift":
        points[:, 1] += 17.0 * t
    elif condition == "gaps":
        keep = np.ones(n, dtype=bool)
        keep[max(2, n // 4):max(4, n // 4 + 3)] = False
        points = points[keep]

    return points.astype(float)


def measure_trajectory(points: np.ndarray, condition: str = "nominal") -> TrajectoryMetrics:
    arr = np.asarray(points, dtype=float)
    if arr.ndim != 2 or arr.shape[1] != 2 or len(arr) < 2:
        raise ValueError("points must be an (N, 2) array with N >= 2")
    steps = np.diff(arr, axis=0)
    lengths = np.linalg.norm(steps, axis=1)
    headings = np.arctan2(steps[:, 1], steps[:, 0])
    delta = np.diff(headings)
    wrapped = np.arctan2(np.sin(delta), np.cos(delta))
    return TrajectoryMetrics(
        waypoints=int(len(arr)),
        path_length=float(lengths.sum()),
        total_turning=float(np.abs(wrapped).sum()),
        mean_step=float(lengths.mean()),
        condition=condition,
    )


def run_demo(condition: str = "nominal", n: int = 48, seed: int = 7) -> dict:
    points = generate_trajectory(condition=condition, n=n, seed=seed)
    return {"metrics": asdict(measure_trajectory(points, condition)), "synthetic": True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--condition", choices=["nominal", "noise", "drift", "gaps"], default="nominal")
    parser.add_argument("--points", type=int, default=48)
    parser.add_argument("--seed", type=int, default=7)
    args = parser.parse_args()
    print(json.dumps(run_demo(args.condition, args.points, args.seed), indent=2))


if __name__ == "__main__":
    main()
