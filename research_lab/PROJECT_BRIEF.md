# Faculty research collaboration brief

## Purpose

This repository provides a small, reproducible software environment for discussing three possible supervised research directions. It is a starting point for technical review, not a claim of a completed university project or a request for an endorsement.

## Direction A — Robot demonstration data and imitation learning

**Question:** How can the quality of robot demonstrations be characterised before they are used for policy learning?

**Current artifact:** A deterministic, synthetic 2-D trajectory generator and basic path/turning metrics.

**Possible 10–12 week contribution under a host supervisor:**
1. Select one existing task and dataset approved by the host lab.
2. Define data-quality criteria with the lab.
3. Reproduce baseline preprocessing and trajectory visualisation.
4. Compare one or two demonstration-quality measures against the lab's own evaluation protocol.
5. Deliver tested code, experiment notes and a short report.

**Boundary:** This workspace does not contain physical-robot recordings. The example trajectories are synthetic.

## Direction B — Trustworthy AI scenario evaluation

**Question:** Can a compact, explicit scenario suite make failure modes and control coverage easier to reproduce?

**Current artifact:** A deterministic checklist evaluator for instruction injection, sensitive disclosure and tool misuse.

**Possible 10–12 week contribution under a host supervisor:**
1. Agree on threat model and safe, approved test scenarios.
2. Define expected controls and reproducible test cases.
3. Implement a repeatable evaluation harness and reporting.
4. Analyse false positives, false negatives and scenario coverage.
5. Deliver tests, a data dictionary and a reproducibility note.

**Boundary:** The current demonstration does not query a model and is not evidence that a model is secure.

## Direction C — Scientific machine-learning baselines

**Question:** Does a simple learned surrogate improve on a transparent baseline under a controlled held-out evaluation?

**Current artifact:** A toy synthetic response curve with a constant baseline and a linear surrogate.

**Possible 10–12 week contribution under a host supervisor:**
1. Obtain an approved simulation or open dataset from the host.
2. Reproduce a transparent baseline and preprocessing procedure.
3. Evaluate a simple surrogate on a fixed train/test protocol.
4. Inspect error by data regime and conduct a small ablation.
5. Deliver reproducible code and a concise technical report.

**Boundary:** The toy data here are synthetic, not CERN, CMS, detector or experimental measurements.

## Researcher context

Prakash Chand Jain is a third-year B.Tech Information Technology student at Bharati Vidyapeeth (Deemed to be University), College of Engineering, Pune, India. Expected graduation: June 2028. The researcher is seeking a faculty-supervised Summer 2027 project and is open to narrowing the work to a host lab's actual research needs.

A separate selected research placement at IDSIA/SUPSI is upcoming and has not yet started. It is not presented here as completed work.
