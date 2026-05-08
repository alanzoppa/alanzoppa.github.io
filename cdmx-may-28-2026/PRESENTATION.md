I’m going to talk about a personal experiment in writing code like an architect. It’s fair to call this vibe coding, and to be clear I wouldn’t recommend getting this far from your code when there are production consequences.

But I was interested in how far I could push agency with open models. You can get a shocking number of LLM tokens for $20/month now. Ollama Pro is so generous I can’t use it up, and let smarter models than I technically need do the dirty work.

So I'm going to tell you about what I built, what problems it solves for me, and mostly how I let the AIs do most of the work without delivering slop.o

First, let's talk about open-weights models. Chinese companies are delivering a lot of great work.

GLM 5.1 and Kimi k2.6 are 

Plan then execute is a common workflow. Most agentic coding tools are built this way, and optimize for using a larger model to plan and a smaller model to execute. We can carry this further. Here's a few of my standard instructions. Here's the high points and why it's so effective.

1. Global Config (~/.config/opencode/AGENTS.md) — The Powerhouse
This is a detailed orchestration manual for AI coding agents. What makes it effective:
a) Clear hierarchy of model assignment. It defines a Decision Matrix mapping task types to specific models:
> | Task Type | Subagent | Model | Why |
> |---|---|---|---|
> | Exploring many files, batch metadata edits, pattern-based find-and-replace | @flash | ollama-cloud/deepseek-v4-flash | Token-efficient, fast on large sets |
> | Writing standalone files, tests, configs, migrations, data transforms | @hurry | ollama-cloud/minimax-m2.7 | Fast for well-defined, self-contained work |
> | Architectural changes, refactoring, complex feature implementation | @kimi | ollama-cloud/kimi-k2.6 | Smarter model for tasks requiring judgment |
b) Aggressive parallelization mandate. It doesn't suggest — it requires delegation:
> "MUST parallelize with subagents — Default to dispatching subagents. Doing everything yourself is the exception, not the rule."
And a concrete self-check rule:
> "Before executing multi-step work, explicitly ask: 'Can any of these steps be dispatched to a subagent?' If yes, dispatch them. When your todo list has 3+ items, at least half should be dispatched to subagents where possible."
c) Acknowledges tool limitations explicitly. The MCP limitation section prevents silent failures:
> "MCP servers (notes-browser, Linear, Notion, GitHub) are enabled in opencode.json but subagents dispatched via the Task tool cannot access them."
d) Git discipline baked in. Push-after-green, track AGENTS.md changes, and keep skills in sync with repos.
e) Terseness as a value. Code style enforces the same brevity the system instructions demand:
> "Comments are terse omit if code is self-explanatory, use sparingly, keep short."

From the Code Style section of ~/.config/opencode/AGENTS.md:
> "Don't reinvent the wheel - If a robust library is available, prefer this over implementing something from scratch. Use standard or existing package management solutions. Don't re-test library functionality."
The mandate is threefold: prefer existing robust libraries, use standard package managers (don't ad-hoc install), and don't write tests that re-verify what a library already guarantees.
