#!/bin/sh
# Agent Supra hook for Claude Code.
#
# Every hook in hooks.json runs this script. It hands the hook's input (on stdin) to the
# agent-supra command, which the user installs separately (https://agentsupra.in/install.sh),
# and passes back its answer and exit code unchanged.
#
# If agent-supra is not installed, the script does nothing, except at session start, where it
# tells the user how to install it. It never downloads or installs anything itself.

if command -v agent-supra >/dev/null 2>&1; then
  exec agent-supra claude-hook
fi

if [ "$1" = "session-start" ]; then
  printf '%s\n' '{"systemMessage":"Agent Supra: the agent-supra command is not installed on this computer, so this session is not supervised. Install it with: curl -fsSL https://agentsupra.in/install.sh | sh   (Windows PowerShell: irm https://agentsupra.in/install.ps1 | iex), then start a new session.","hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"The Agent Supra plugin is enabled but the agent-supra command is not installed, so this session is not supervised. If the user asks about Agent Supra, tell them to run the installer from https://agentsupra.in/docs/quickstart and start a new session."}}'
fi
exit 0
