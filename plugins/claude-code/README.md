# Agent Supra for Claude Code

Supervision for Claude Code sessions. With this plugin, [Agent Supra](https://agentsupra.in):

- **pauses a session that is stuck**: the same tests failing attempt after attempt, edits flipping
  between two versions, or a tool failing the same way, and shows you the evidence and a suggested
  fix so you can continue, fix or stop it;
- **blocks risky commands before they run**: force pushes, recursive deletes, production database
  commands, `curl | sh` and edits to secrets files, or holds a command (a deploy, say) until a person
  approves it once;
- **nudges Claude** with what it is stuck on, instead of pausing, if you prefer;
- **tracks estimated model spend** per session, person and repository.

## What it needs

The plugin is a thin connector. Every hook runs `hooks/run.sh`, which passes the hook's input to the
`agent-supra` command and returns its answer unchanged. Install that command separately, once:

```sh
curl -fsSL https://agentsupra.in/install.sh | sh        # macOS and Linux
irm https://agentsupra.in/install.ps1 | iex              # Windows PowerShell
```

The installer also adds this plugin, so most people never install it by hand. `agent-supra` is
published on PyPI under the MIT license as [`agent-supra`](https://pypi.org/project/agent-supra/). Without it, the
plugin does nothing except show the install command when a session starts. The plugin itself never
downloads or installs anything.

## What runs, what is sent, and where

`agent-supra` runs on your computer with your user permissions, at these Claude Code events: session
start and end, before and after tool calls (shell commands and file edits), subagent start and stop,
and stop.

**Checked on your computer only, never sent:** the text of shell commands and file paths, which are
matched against guard rules locally. Only the name of a guard that matched (for example
`force_push`) is reported.

**Sent to the Agent Supra service you log in to** (`https://agentsupra.in` by default, or your own
server if you self-host), over HTTPS with your API key:

- the model name and token counts of each model call, read from Claude Code's session transcript
  (only those fields: never prompts or replies);
- test results: test IDs and which failed, as keyed hashes when they come from report files, and a
  code revision ID (a git commit hash);
- tool names, whether each call succeeded, and keyed fingerprints of their arguments and errors, which
  show that two calls were the same without revealing what they said;
- the agent's name (`claude`) and the name of the project folder (not its path or contents), so spend
  can be grouped by repository.

**Fetched from the service:** your team's shared policy (guard rules) at session start, and before
steps whether the session may continue, including any advice for Claude and answers to held commands.

**Never sent:** your prompts, Claude's replies, source code, file contents, command text, or your model
provider API keys.

**Stored locally** in `~/.agent-supra`: your saved login and session state. When test results arrive,
the hook also records a snapshot of the project with `git stash create`, which adds a git object to
the repository without changing your files, branches or stash list; `agent-supra rollback` uses these.
They stay on your computer.

The service keeps run data for 30 days. Details: [privacy](https://agentsupra.in/privacy) and
[security](https://agentsupra.in/security).

## Turning it off

`claude plugin disable agent-supra@agent-supra` turns the plugin off; `agent-supra uninstall` removes
the plugin, the program, its hooks in other agents and this computer's login.

## License

MIT. Source: [voidpusher/agent-supra-plugin](https://github.com/voidpusher/agent-supra-plugin).
Questions: <https://agentsupra.in> or the contact address on the site.
