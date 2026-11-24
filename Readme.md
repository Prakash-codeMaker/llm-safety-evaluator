# 🔥 LLM Safety Evaluator & Red Teaming Tool

> **Faculty collaboration workspace:** this branch also contains a reproducible research environment under `research_lab/`, with three deterministic software demonstrations and a Codespaces/Live Share setup.
>
> **[Open this branch in GitHub Codespaces](https://codespaces.new/Prakash-codeMaker/llm-safety-evaluator?ref=faculty-collaboration-lab)** · [Read the collaboration guide](COLLABORATION.md) · [Review the research brief](research_lab/PROJECT_BRIEF.md) · [Contact the researcher](mailto:p9340297@gmail.com)

A "Judge-as-a-Service" platform that automatically tests LLMs (GPT-4, Claude, DeepSeek, Gemini) for safety violations using adversarial prompts.

## Faculty collaboration workspace

The `research_lab/` package is deliberately separate from the existing LLM Safety Evaluator application. It provides three small, reproducible examples:

1. **Robotics:** synthetic trajectory generation and path-quality measurements.
2. **Trustworthy AI:** a rule-based scenario and safeguard-coverage checklist.
3. **Scientific ML:** a synthetic toy response curve with a held-out baseline comparison.

Open the branch in Codespaces, then run:

```bash
make all
```

For a live review, the researcher can start a read-only Visual Studio Live Share session and privately invite a professor. See [COLLABORATION.md](COLLABORATION.md). The Codespace runs as a non-root user. Do not share root credentials or SSH private keys.

**Research integrity:** these examples use synthetic or hand-authored test cases. They are not completed laboratory experiments, physical-robot data, real CERN/CMS data, or evidence of model safety. The proposed 10–12 week research scopes are described in [PROJECT_BRIEF.md](research_lab/PROJECT_BRIEF.md).

## Existing LLM Safety Evaluator

### Features
- **Multi-Model Support:** Tests OpenAI, Anthropic, Google, and DeepSeek models.
- **Automated Scoring:** Uses LLM-as-a-Judge to detect toxicity and jailbreaks.
- **PDF Reporting:** Generates compliance reports for stakeholders.
- **Demo Mode:** Allows testing without live API keys.

### Tech Stack
- **Frontend:** Streamlit
- **Backend:** FastAPI
- **AI Routing:** LiteLLM

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Prakash-codeMaker/llm-safety-evaluator
   cd llm-safety-evaluator
   ```
2. Install the existing application dependencies as described by its backend and frontend requirement files.

The research-workspace dependencies are separate in `requirements-research.txt`.
