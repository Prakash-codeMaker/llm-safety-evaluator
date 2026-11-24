# Joining a live research review

This repository is configured for GitHub Codespaces and Visual Studio Live Share.

## Option 1 — Inspect or run independently

1. Open the public repository branch `faculty-collaboration-lab`.
2. Select **Code → Codespaces → Create codespace on faculty-collaboration-lab**, or use the Codespaces link in the repository README.
3. The dev container installs the lightweight research dependencies.
4. Run `make all` to execute the tests and all three demonstrations.
5. A professor can change the synthetic inputs, inspect the implementation, or fork the repository to experiment independently.

Each person who creates their own Codespace owns and pays for that Codespace under their GitHub account and usage allowance.

## Option 2 — Join a live, supervised session

1. The researcher opens this branch in their own Codespace.
2. Confirm that the **Live Share** extension is installed and enabled.
3. Start a Live Share session from the VS Code status bar or Live Share panel.
4. Begin in **read-only** mode and approve only the named professor who is joining.
5. Share the generated invitation link privately.
6. The host can optionally share a terminal read-only so the professor can inspect experiment output. If the professor needs to run commands collaboratively, the host may explicitly share a read/write terminal while present.
7. Stop sharing and end the session after the review.

A shared read/write terminal permits the guest to execute commands with the host's current user permissions. In this Codespace that user is `vscode`, not root. Only use it with a trusted, identified collaborator, with no personal secrets or API keys in the environment.

Live Share is the collaboration layer. It does not give guests the researcher's GitHub credentials or SSH private key.

## SSH and privilege model

- The Codespace owner can open their own terminal and use `gh codespace ssh -c <codespace-name>` from a separately authenticated local terminal.
- The development container runs as the non-root `vscode` user.
- Do not add a shared root password, publish port 22, share an SSH private key, or place GitHub tokens/API keys in this repository.
- A professor can create their own Codespace from this public branch. For a live joint session in the researcher's environment, use an explicitly invited Live Share session rather than sharing SSH credentials.
- Any Live Share link should be sent privately to a named invitee, not posted publicly.

## Safety and cost

- The workspace contains no credentials or private university data.
- The examples are local, deterministic and use synthetic/hand-authored data.
- The optional Jupyter port is private by default.
- Codespaces usage is chargeable after the account's included monthly allowance. Check usage and budget limits before extended sessions.
