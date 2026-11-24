# Joining a live research review

This repository is configured for GitHub Codespaces and Visual Studio Live Share.

## Option 1 — Inspect or run independently

1. Open the public repository branch `faculty-collaboration-lab`.
2. Select **Code → Codespaces → Create codespace on faculty-collaboration-lab**, or use the Codespaces link in the repository README.
3. The dev container installs the lightweight research dependencies.
4. Run `make all` to execute the tests and all three demonstrations.
5. A professor can change the synthetic inputs, inspect the implementation, or fork the repository to experiment independently.

Each person who creates their own Codespace owns and pays for that Codespace under their GitHub account and usage allowance.

## Option 2 — Join a live session with the researcher

1. The researcher opens this branch in their own Codespace.
2. Confirm that the **Live Share** extension is installed and enabled.
3. Start a Live Share session from the VS Code status bar or Live Share panel.
4. Choose **read-only** for an initial faculty review. Do not grant terminal/write access unless the professor specifically asks for it and the researcher is comfortable with the scope.
5. Share the generated invitation link directly with the invited professor.
6. Stay present during the review. Stop the Live Share session when finished.

Live Share is the collaboration layer. It does not give guests the researcher's GitHub credentials or SSH private key.

## SSH and privilege model

- The Codespace owner can open their own terminal and use `gh codespace ssh -c <codespace-name>` from a separately authenticated local terminal.
- The development container runs as the non-root `vscode` user.
- Do not add a shared root password, publish port 22, share an SSH private key, or place GitHub tokens/API keys in this repository.
- GitHub Codespaces does not let another person SSH directly into the owner's Codespace. Use Live Share for an invited joint session, or let the professor create their own Codespace from the public repository.
- Any Live Share link should be sent privately to a named invitee, not posted publicly.

## Safety and cost

- The workspace contains no credentials or private university data.
- The examples are local, deterministic and use synthetic/hand-authored data.
- The optional Jupyter port is private by default.
- Codespaces usage is chargeable after the account's included monthly allowance. Check usage and budget limits before extended sessions.
