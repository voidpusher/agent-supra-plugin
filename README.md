# Agent Supra plugin

The Claude Code plugin for [Agent Supra](https://agentsupra.in), supervision for AI coding agents.
With it, Claude Code sessions:

- **pause when stuck**: the same tests failing attempt after attempt, edits flipping back and forth,
  or a tool failing the same way. Supra shows the evidence and a suggested fix; you continue, fix or stop.
- **can't run risky commands**: force pushes, recursive deletes, production databases, `curl | sh`
  and secrets files are blocked before they run. Your own rules in a `supra.yaml` can hold a
  command (a deploy, say) until someone approves it, once.
- **get nudged** with what they are stuck on, instead of being paused, if you prefer.
- **show estimated spend** per session, person and repository, and appear in your team's fleet view.

Guards run on your machine and report only the guard's name. Prompts, code and command text
never leave it.

```sh
pip install --upgrade "agent-supra>=1.15.0"
claude plugin marketplace add voidpusher/agent-supra-plugin
claude plugin install agent-supra@agent-supra
agent-supra login
claude
```

Full setup is in the [Claude Code guide](https://agentsupra.in/docs/claude-code). Other agents
and frameworks are listed in the [quickstart](https://agentsupra.in/docs/quickstart).

- `plugins/claude-code` is the plugin. It only runs the `agent-supra claude-hook` command.
- `practice-project` is a tiny project with one failing test, for
  [trying Agent Supra](https://agentsupra.in/docs/practice-project).

Found a problem? [Open an issue](https://github.com/voidpusher/agent-supra-plugin/issues).

This repository is generated from Agent Supra's private source. Licensed under MIT.
