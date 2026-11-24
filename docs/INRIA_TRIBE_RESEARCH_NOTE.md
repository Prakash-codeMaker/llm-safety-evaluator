# Research note for Inria TRIBE: information leakage in network-support LLMs

**Status:** Proposed research direction and preliminary software artefact. This note does not claim a completed experiment or a host commitment.

## Motivation

A network-support assistant may receive operational context that mixes information needed to diagnose a fault with subscriber identifiers, contact details, addresses, device metadata, or secrets. Supplying the entire context can create unnecessary exposure. Removing too much context, however, may reduce the quality of troubleshooting. This motivates a measurable privacy–utility trade-off rather than a binary claim that a prompt is simply safe or unsafe.

## Research question

For network-support workflows, how do full-context prompting, deterministic field redaction, and task-scoped context minimisation affect information disclosure and task utility, including under untrusted text embedded in support records?

## Current artefact

The public branch \`research-grade-evaluation\` adds a Python harness that:
- constructs paired full, redacted, and minimal context conditions;
- uses synthetic subscriber canaries rather than real customer data;
- randomises the complete case/condition call schedule with a recorded seed;
- measures exact canary-string matches, lexical helpful-signal coverage, latency, and provider errors;
- reports descriptive paired differences only when all conditions for a case/repetition succeed;
- omits raw model responses by default and tests that provider failures are not silently scored as safe.

The pilot corpus has 12 hand-authored scenarios, including connectivity failures, DNS, Wi-Fi, modem provisioning, filtering, congestion, and an untrusted ticket-note injection attempt. Six-plus offline unit tests are run in GitHub Actions (the repository test count may grow as the implementation evolves).

## Proposed experimental progression

1. **Threat model and information-flow map.** Identify user, support agent, LLM, orchestration layer, network-management tools, logs, and external provider as trust boundaries. Classify data fields by sensitivity and operational necessity.
2. **Baselines.** Compare full context, deterministic redaction, and task-scoped allowlisting under the same task and system instructions.
3. **Leakage evaluation.** Begin with synthetic canaries and exact/normalised matching; then add partial, transformed, and semantic leakage checks with human-reviewed labels.
4. **Utility evaluation.** Move beyond literal keywords to a task rubric covering diagnostic correctness, actionability, unsupported claims, and appropriate requests for missing information.
5. **Adversarial evaluation.** Test indirect prompt injection and malicious content in ticket notes or device metadata, while preserving a controlled and documented test corpus.
6. **Analysis.** Use paired case-level analysis, report denominators and provider errors, and quantify uncertainty only once the corpus and annotation design support it.

## Candidate deliverables for a short research placement

- A documented threat model and field-level information-flow inventory for a selected network-support workflow.
- A reproducible Python evaluation harness and synthetic scenario schema.
- An evaluated comparison of context minimisation strategies, with leakage and task-utility measures and a documented error analysis.
- A concise technical report describing what worked, what failed, and where formal or system-level mitigations would be appropriate.

## Present limitations and honesty boundary

The current artefact is an engineering pilot, not a formal information-flow analysis. It does not implement differential privacy, prove non-interference, or establish a general privacy guarantee. The 12 scenarios are hand-authored and not representative. Exact string matching misses paraphrase and semantic disclosure; lexical helpful-signal coverage is not task-success evaluation. No live provider run or human annotation is included yet.

The next empirical step is a small live run using synthetic data, followed by inspection of false positives/false negatives and refinement of the metric suite. A stronger evaluation should be designed with the host researchers so that the threat model, data assumptions, and metrics match their application domain.
