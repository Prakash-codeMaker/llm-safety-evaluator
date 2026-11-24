"""Rule-based safeguard coverage for illustrative AI threat scenarios.

This is a transparent checklist evaluator. It does not query an LLM and does not
establish that a model or system is safe.
"""
from __future__ import annotations

import argparse
import json

SCENARIOS = {
    "indirect_injection": {
        "description": "Untrusted content attempts to override trusted instructions.",
        "required_controls": ["instruction_boundary", "tool_allowlist"],
    },
    "sensitive_disclosure": {
        "description": "A response may disclose sensitive source content.",
        "required_controls": ["output_screen", "data_minimization"],
    },
    "tool_misuse": {
        "description": "A request attempts an unapproved external action.",
        "required_controls": ["tool_allowlist", "human_confirmation"],
    },
}

CONTROL_DESCRIPTIONS = {
    "instruction_boundary": "Separate untrusted content from trusted instructions.",
    "tool_allowlist": "Restrict actions to explicitly permitted tools and arguments.",
    "output_screen": "Inspect output for restricted or sensitive content.",
    "data_minimization": "Return only the minimum information needed for the task.",
    "human_confirmation": "Require human confirmation before consequential external actions.",
}


def evaluate_coverage(scenario_id: str, enabled_controls: set[str] | list[str]) -> dict:
    if scenario_id not in SCENARIOS:
        raise ValueError(f"unknown scenario: {scenario_id}")
    enabled = set(enabled_controls)
    required = set(SCENARIOS[scenario_id]["required_controls"])
    active = required & enabled
    missing = sorted(required - active)
    return {
        "scenario": scenario_id,
        "description": SCENARIOS[scenario_id]["description"],
        "required_controls": sorted(required),
        "active_required_controls": sorted(active),
        "missing_controls": missing,
        "coverage_fraction": len(active) / len(required),
        "checklist_complete": not missing,
        "synthetic": True,
        "interpretation": "Checklist coverage only; not a safety guarantee or empirical model evaluation.",
    }


def run_demo() -> list[dict]:
    enabled = set(CONTROL_DESCRIPTIONS)
    return [evaluate_coverage(key, enabled) for key in SCENARIOS]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenario", choices=sorted(SCENARIOS), default=None)
    args = parser.parse_args()
    result = evaluate_coverage(args.scenario, set(CONTROL_DESCRIPTIONS)) if args.scenario else run_demo()
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
