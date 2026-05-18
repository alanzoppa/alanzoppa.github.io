I’m going to talk about a personal experiment in writing code like an architect.
It’s fair to call this vibe coding, and to be clear I wouldn’t recommend getting
this far from your code when there are production consequences.

----

I was interested in a few different things here.

1. How far I can push open-weights models? How do these compare to the flagship
   models?
2. What mistakes do agents make without the default prompts baked into Claude?
3. How can I use embeddings to navigate my own data? I really only understand
   them at an interface level.


----

## Tokens

1. Ollama Pro @ 20USD/mo. is very difficult to exhaust in a week. Sometimes slow
   during peak periods.
2. OpenCode Go at $10/mo. is a great deal too.
3. OpenRouter because none of the above have cloud embedding or reranking
   models, but embedding the whole set of ~1600 documents cost ~0.01 USD.
4. Embedding and reranking run alright on a Mac with plenty of unified RAM but
   the inference is cheap enough that I don't bother anymore. Qwen 0.6B
   Embedding is great for this kind of thing though.


----

## Tools

1. Opencode is a great open-source alternative to Claude Code. It's not picky
   about what model you use or which service. It's easy to switch between models
   and specialize per-model subagents. It already has a rich team of built-in
   subagents for parallelization and context-saving.
2. Openclaw did some of the data gathering for me. It's learned how to use
   github pages in just the way I like, but it tends to write spaghetti code.
   For anything more technical, it tends to get lost in all the personal details
   it has access to.
3. Hermes Agent is much less personal than Openclaw and tends to do a great job
   with devops type things. It's more opinionated about the kind of help it
   provides. It's great for things like "figure out why Avahi or systemd or
   nginx, etc. aren't working."
4. agent-browser is generally simpler for agents to orchestrate at the CLI
   compared to playwright.



----

## Managing Interns

1. Ten years ago I had this group of eight interns, and this feels a lot like
   managin them.
2. I gave them tasks that aren't mission-critical without too much guidance. It
   was more important to see what they coudl do on their own, where they were
   comfortable experimenting, and where they needed unambiguous limits.
3. Often they'd take somethign in a completely unexpected way and the results
   were often either delightful or ridiculous.
4. In their first week I told them to pick a team name and they did this. They
   did something weird and memorable and used it as a chance to make fun of me
   because I didn't give them any limits.
5. But I'd also have to remind them of things that were obvious. One of them
   tried to right a stored SQL procedure for a really simple Rails Controller.
   I had to talk to another one about storing his sweaty gym clothes in a small,
   shared office. Another didn't show up for meetings because he figured
   somebody would come get him when it was time.


----

## Coding Agents as Interns

1. And coding agents are kind of like this. They'll solve problems with a tangle
   of regex if you don't encourage them to install third-party libraries.
   They'll flail around with curl forever if you don't install agent-browser or
   playwright. If the intern thinks its a good idea to form systemd, the agent
   will think it's a good idea to fork systemd.
2. They won't commit or push unless you tell them to.
3. They won't run the tests before pushing unless you tell them to.
4. They will commit secrets to your git repo, in front of God and everybody,
   unless you tell them not to.
5. They will single-thread their way through an entire task unless you tell them
   to parallelize.

----

## Guardrails

- **MUST parallelize with subagents** — Default to dispatching subagents. Doing everything yourself is the exception, not the rule. This applies in ALL modes (Plan and Build).
- **Push after successful complex changes** - When completing a series of related changes (model + migration + command updates + tests passing), commit AND push immediately. Unless told otherwise, ensure that ALL tests are green before pushing.
- **Test new functionality** plan and write automated tests as you go. Write regression tests where appropriate.
- **Always specify the subagent type** when presenting a plan. Say "I'll dispatch X to `@build`, Y to `@explore`".
- **Type safety is preferred** when supported by the language.
- **Don't reinvent the wheel** - If a robust library is available, prefer this over implementing something from scratch. Use standard or existing package management solutions. Don't re-test library functionality.


----

## Code I wouldn't have bothered to write.

1. I built this thing (I'll add a video later).
2. I had extensive notes over years and years in different formats. I wanted to
   organize them and find connections between them.
3. I wanted to apply the same process to my work notes and give my agents deep
   access to context about my workday.
4. I wanted to understand embedding models better. This part was a little
   frustrating because I honestly only get how they work at an interface level.



----

## Embedding how-to

1. These are sort of a part of an LLM. They'll take input and return (for
   example) a set of coordinates in 4,096 dimensions.
2. These coordiantes are relative to the meaning of the word.
3. Take a look at the example. Here the embeddings are compressed into their
   most significant three dimensions, and you can see that "uncle" bears about
   the same relationship to "aunt" as "man" does to "woman."
4. The "difference" between two embeddings is the cosine distance between the
   two embeddings relative to the cartesian center.


----

## That's what I wanted from Mnestic.

[live or recorded demo]

1. What you're seeing here is a cloud of notes with >75% relationship to each
   other. The clusters are meaningful. It finds notes from the same series very
   easily.
2. This makes it really easy for different agents to tap into the MCP frontend
   and get a ton of detailed context.
3. My work notes are mostly generated from the Zoom transcripts. Typically
   Claude goes into Zoom, captures the AI summaries, and applies my styleguide
   for notes before dumping into Mnestic.
4. And then in the next session, it's actually able to follow threads like "Alan
   promised to send Ale an email, did he remember?"
















But I was interested in how far I could push agency with open models. You can
get a shocking number of LLM tokens for $20/month now. Ollama Pro is so generous
I can’t use it up, and let smarter models than I technically need do the dirty
work.

So I'm going to tell you about what I built, what problems it solves for me, and
mostly how I let the AIs do most of the work without delivering slop.o

First, let's talk about open-weights models. Chinese companies are delivering a
lot of great work.

GLM 5.1 and Kimi k2.6 are 

Plan then execute is a common workflow. Most agentic coding tools are built this
way, and optimize for using a larger model to plan and a smaller model to
execute. We can carry this further. Here's a few of my standard instructions.
Here's the high points and why it's so effective.

1. Global Config (~/.config/opencode/AGENTS.md) — The Powerhouse This is a
   detailed orchestration manual for AI coding agents. What makes it effective:
   a) Clear hierarchy of model assignment. It defines a Decision Matrix mapping
   task types to specific models:
> | Task Type | Subagent | Model | Why | |---|---|---|---| | Exploring many
> files, batch metadata edits, pattern-based find-and-replace | @flash |
> ollama-cloud/deepseek-v4-flash | Token-efficient, fast on large sets | |
> Writing standalone files, tests, configs, migrations, data transforms | @hurry
> | ollama-cloud/minimax-m2.7 | Fast for well-defined, self-contained work | |
> Architectural changes, refactoring, complex feature implementation | @kimi |
> ollama-cloud/kimi-k2.6 | Smarter model for tasks requiring judgment |
b) Aggressive parallelization mandate. It doesn't suggest — it requires
delegation:
> "MUST parallelize with subagents — Default to dispatching subagents. Doing
> everything yourself is the exception, not the rule."
And a concrete self-check rule:
> "Before executing multi-step work, explicitly ask: 'Can any of these steps be
> dispatched to a subagent?' If yes, dispatch them. When your todo list has 3+
> items, at least half should be dispatched to subagents where possible."
c) Acknowledges tool limitations explicitly. The MCP limitation section prevents
silent failures:
> "MCP servers (notes-browser, Linear, Notion, GitHub) are enabled in
> opencode.json but subagents dispatched via the Task tool cannot access them."
d) Git discipline baked in. Push-after-green, track AGENTS.md changes, and keep
skills in sync with repos.  e) Terseness as a value. Code style enforces the
same brevity the system instructions demand:
> "Comments are terse omit if code is self-explanatory, use sparingly, keep
> short."

From the Code Style section of ~/.config/opencode/AGENTS.md:
> "Don't reinvent the wheel - If a robust library is available, prefer this over
> implementing something from scratch. Use standard or existing package
> management solutions. Don't re-test library functionality."
The mandate is threefold: prefer existing robust libraries, use standard package
managers (don't ad-hoc install), and don't write tests that re-verify what a
library already guarantees.
