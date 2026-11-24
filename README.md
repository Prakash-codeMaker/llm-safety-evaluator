# LLM Safety Evaluator

A small research prototype for examining LLM responses to adversarial prompts and, in the new evaluation path, measuring **literal disclosure of synthetic sensitive data under context minimisation** in network-support scenarios.

> **Research status:** The privacy experiment is a runnable pilot protocol, not a completed benchmark. This update adds the harness and tests; it does not claim live-model results. The existing Streamlit/FastAPI app includes a simulated demo mode and should not be interpreted as evidence of model performance.

## What is here

| Component | Purpose | Evidence status |
|---|---|---|
| backend/ and frontend/ | Original LiteLLM, FastAPI and Streamlit prototype | Earlier exploratory implementation; demo responses are simulated |
| evaluation/ | Paired full / redacted / minimal context evaluation for synthetic network-support cases | New, unit-tested harness; live provider runs are the researcher's responsibility |
| tests/ | Offline tests for context construction, scoring, aggregation and error handling | Runs without an API key |
| docs/EXPERIMENT_PROTOCOL.md | Research question, hypotheses, metrics, reproduction steps and limitations | Protocol only; no results claimed |

## Research direction

The new experiment asks whether reducing the context supplied to a network-support assistant lowers exposure of planted sensitive values while retaining useful troubleshooting signals. It compares three paired conditions for each case:

- **Full context:** every synthetic context field is supplied.
- **Redacted context:** fields declared sensitive are replaced with [REDACTED].
- **Minimal context:** only the case's task-relevant fields are supplied.

The primary metric is exact, case-insensitive canary-string exposure. The secondary metric is lexical coverage of predeclared helpful signals. These are intentionally simple pilot measures: exact matching misses paraphrased or inferred leakage, and lexical coverage is not semantic task quality. Read the full protocol at docs/EXPERIMENT_PROTOCOL.md before interpreting results.

## Run the offline tests

Python 3.10 or later is recommended. The test suite uses only the Python standard library:

    python -m unittest discover -s tests -v

## Run a live privacy experiment

1. Create and activate a virtual environment.
2. Install the evaluation dependency:

       python -m pip install -r requirements-evaluation.txt

3. Configure the credential for your selected LiteLLM provider in the environment. For example, for an OpenAI model:

       export OPENAI_API_KEY="your-key"

   Do not paste keys into source files, notebooks, issue comments, or commits.

4. Run the synthetic pilot:

       python -m evaluation.run_experiment \
         --model openai/gpt-4o-mini \
         --cases evaluation/sample_cases.json \
         --repetitions 1 \
         --seed 2026 \
         --output artifacts/network-privacy-evaluation.json

   The default run makes **9 model calls** (3 cases × 3 conditions). Increase --repetitions only when you are comfortable with the additional API cost.

5. Inspect the JSON output. Failed provider calls are marked error and excluded from metric denominators; they are not treated as safe. Raw model responses are omitted by default. Add --store-responses only when working with synthetic test data and when retaining outputs is appropriate.

The model identifier and API provider configuration should be recorded when sharing any result. A model name alone may not uniquely identify a hosted snapshot. The output includes descriptive paired differences versus the full-context condition, computed only for case/repetition groups in which all three conditions succeeded; these are not statistical significance tests.

## Existing interactive prototype

The original app is retained for continuity. Its demo mode uses keyword triggers and randomised simulated outcomes; it is a UI demonstration, **not a model evaluation**. The original app's API-based evaluation path has not been revalidated as part of the new privacy harness. Do not use its displayed score or demo output as a benchmark claim.

The original dependencies are listed separately in backend/requirement.txt and frontend/requirement.txt. The new research harness does not depend on the Streamlit UI or the original backend.

## Reproducibility and responsible use

- The included cases use synthetic identifiers, reserved .test emails and documentation-range IP addresses. They contain no real subscriber records.
- Never run the harness on real customer information without the required authorisation, data-protection review, and a secure data-handling plan.
- Do not interpret a zero literal-exposure rate as proof of privacy.
- Do not present the three-case pilot as a representative benchmark, a general safety score, or evidence that one model is safer than another.
- For a stronger study, expand and review the scenario set, add semantic and partial-match detectors, conduct blinded human annotation, report agreement and uncertainty, and preserve the paired-by-case design.

## Project links

- Repository: https://github.com/Prakash-codeMaker/llm-safety-evaluator
- Maintainer: https://github.com/Prakash-codeMaker
