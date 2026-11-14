# Practice project: one failing test

Use this project to try Agent Supra if you don't have a disposable Python project with
pytest. It is a tiny invoice calculator with one real bug: the bulk discount is supposed to
start at 10 items. Running pytest gives 4 passing tests and 1 failing. It needs no API keys
or network access. The only thing it installs is pytest.

## Set it up

Copy it out of the download and make it its own Git repository. Supra records code revisions
from Git, so it needs a first commit.

macOS/Linux:

```sh
git clone https://github.com/voidpusher/agent-supra-plugin
cp -r agent-supra-plugin/practice-project ~/supra-practice
cd ~/supra-practice
git init -q && git add . && git -c user.name=Practice -c user.email=practice@example.com commit -qm "Practice project"
python -m venv .venv && source .venv/bin/activate
python -m pip install pytest "agent-supra>=1.8.0"
python -m pytest -q        # expect: 1 failed, 4 passed
```

Windows PowerShell:

```powershell
git clone https://github.com/voidpusher/agent-supra-plugin
Copy-Item -Recurse agent-supra-plugin\practice-project $HOME\supra-practice
cd $HOME\supra-practice
git init -q; git add .; git -c user.name=Practice -c user.email=practice@example.com commit -qm "Practice project"
python -m venv .venv; .\.venv\Scripts\Activate.ps1
python -m pip install pytest "agent-supra>=1.8.0"
python -m pytest -q        # expect: 1 failed, 4 passed
```

## Try it with Claude Code

Follow [Claude Code setup](https://agentsupra.in/docs/claude-code) in observation mode: run `agent-supra login` once,
then start `claude` from this folder. Ask:

> Run the tests, then fix the failing test.

Claude runs pytest, finds the bug and fixes it. Your dashboard shows a **Claude Code session**
with its test reports. The failing count should go from 1 to 0.

To see Supra catch a stuck agent, restore the bug with `git checkout invoice.py` and ask:

> Run the tests four times without changing any code.

In observation mode the run is flagged and Claude carries on.
