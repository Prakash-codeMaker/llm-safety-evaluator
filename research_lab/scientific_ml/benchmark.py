"""Synthetic toy response curve with held-out baseline comparison.

The generated samples are illustrative only and are not CERN/CMS or other
experimental detector measurements.
"""
from __future__ import annotations

import argparse
import json

import numpy as np


def generate_samples(n: int = 60, noise_fraction: float = 0.08, seed: int = 23):
    if n < 12:
        raise ValueError("n must be at least 12")
    if not 0.0 <= noise_fraction <= 0.5:
        raise ValueError("noise_fraction must be between 0 and 0.5")
    rng = np.random.default_rng(seed)
    x = np.linspace(1.0, 100.0, n)
    signal = 1.8 * np.sqrt(x) + 0.055 * x
    scale = max(float(signal.max()), 1.0)
    y = signal + rng.normal(0.0, noise_fraction * scale, size=n)
    return x, y


def benchmark_surrogate(n: int = 60, noise_fraction: float = 0.08, seed: int = 23) -> dict:
    x, y = generate_samples(n, noise_fraction, seed)
    rng = np.random.default_rng(seed + 1)
    order = rng.permutation(n)
    split = int(round(n * 0.7))
    train_idx, test_idx = order[:split], order[split:]
    x_train, y_train = x[train_idx], y[train_idx]
    x_test, y_test = x[test_idx], y[test_idx]

    constant = float(y_train.mean())
    slope, intercept = np.polyfit(x_train, y_train, deg=1)
    pred_constant = np.full_like(y_test, constant)
    pred_linear = slope * x_test + intercept

    def rmse(pred):
        return float(np.sqrt(np.mean((y_test - pred) ** 2)))

    return {
        "samples": n,
        "training_samples": int(len(train_idx)),
        "test_samples": int(len(test_idx)),
        "constant_baseline_rmse": rmse(pred_constant),
        "linear_surrogate_rmse": rmse(pred_linear),
        "linear_coefficients": {"slope": float(slope), "intercept": float(intercept)},
        "seed": seed,
        "noise_fraction": noise_fraction,
        "synthetic": True,
        "data_note": "Synthetic toy curve only; not real particle-physics, CERN, CMS, or detector data.",
        "split_note": "Random train/test split with a fixed seed; all reported RMSE values use held-out samples.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--samples", type=int, default=60)
    parser.add_argument("--noise", type=float, default=0.08)
    parser.add_argument("--seed", type=int, default=23)
    args = parser.parse_args()
    print(json.dumps(benchmark_surrogate(args.samples, args.noise, args.seed), indent=2))


if __name__ == "__main__":
    main()
