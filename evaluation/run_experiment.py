"""CLI for the synthetic network-support privacy context-ablation experiment."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

from .privacy_harness import run_experiment


def _litellm_responder(model_name: str, messages: list[dict[str, str]]) -> str:
    try:
        from litellm import completion
    except ImportError as exc:
        raise RuntimeError(
            "LiteLLM is required for live model calls. Install requirements-evaluation.txt."
        ) from exc

    result = completion(model=model_name, messages=messages, temperature=0)
    content = result.choices[0].message.content
    if content is None:
        return ""
    return content if isinstance(content, str) else str(content)


def load_cases(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("The cases file must contain a JSON array")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a paired full/redacted/minimal context privacy evaluation."
    )
    parser.add_argument("--cases", type=Path, default=Path("evaluation/sample_cases.json"))
    parser.add_argument(
        "--model", default=os.getenv("LITELLM_MODEL", "openai/gpt-4o-mini"),
        help="LiteLLM model identifier; provider credentials must be in environment variables.",
    )
    parser.add_argument(
        "--output", type=Path,
        default=Path("artifacts/network-privacy-evaluation.json"),
        help="Path for the JSON results file.",
    )
    parser.add_argument("--repetitions", type=int, default=1)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument(
        "--store-responses", action="store_true",
        help="Store raw model responses in the output. Use only with synthetic data.",
    )
    args = parser.parse_args()

    cases = load_cases(args.cases)
    result = run_experiment(
        cases,
        _litellm_responder,
        args.model,
        repetitions=args.repetitions,
        seed=args.seed,
        store_responses=args.store_responses,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Wrote {len(result['records'])} run records to {args.output}")
    for condition, metrics in result["summary"].items():
        exposure = metrics["literal_exposure_rate"]
        coverage = metrics["mean_helpful_signal_coverage"]
        exposure_text = "n/a" if exposure is None else f"{exposure:.1%}"
        coverage_text = "n/a" if coverage is None else f"{coverage:.1%}"
        print(
            f"{condition:>8}: exposure={exposure_text}, "
            f"helpful-signal coverage={coverage_text}, errors={metrics['errors']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
