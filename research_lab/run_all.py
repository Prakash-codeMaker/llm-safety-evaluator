"""Run all three research demonstrations and print machine-readable results."""
from __future__ import annotations

import json

from research_lab.robotics.trajectory import run_demo as run_robotics
from research_lab.trustworthy_ai.coverage import run_demo as run_trustworthy
from research_lab.scientific_ml.benchmark import benchmark_surrogate


def main() -> None:
    results = {
        "robotics": run_robotics("nominal"),
        "trustworthy_ai": run_trustworthy(),
        "scientific_ml": benchmark_surrogate(),
        "disclaimer": "Demonstrations use synthetic or hand-authored illustrative data; they are not completed laboratory experiments.",
    }
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
