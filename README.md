# Agent Supra plugin

The Claude Code plugin for [Agent Supra](https://agentsupra.in), which notices when an AI
coding agent is stuck by checking whether its tests actually make progress.

```sh
pip install --upgrade "agent-supra>=1.8.0"
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
