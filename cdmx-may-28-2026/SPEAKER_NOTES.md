# Speaker Notes: Writing Code Like an Architect

CDMX May 28, 2026

---

## Slide 1: Title

*(Title slide — your name, talk title, "A Personal Experiment in Vibe Coding")*

**OPENING (60 seconds)**

I'm going to talk about a personal experiment in writing code like an architect. It's fair to call this vibe coding, and to be clear — I wouldn't recommend getting this far from your code when there are production consequences.

But that's exactly what made this experiment interesting. When the stakes are low, you can push things much further than you'd ever dare in a production system. And what I found surprised me.

---

## Slide 2: The Three Questions

**TRANSITION (30 seconds)**

I was interested in three things here. Not "can AI write code" — we all know it can. Deeper questions.

**POINT 1: Open-weights models (60 seconds)**

How far can I push open-weights models? Everyone talks about Claude and GPT-4 — they're the gold standard. But the Chinese companies — Alibaba, Moonshot, Zhipu — are shipping genuinely competitive open models. GLM 5.1, Kimi k2.6, DeepSeek v4. These aren't toys. And they're getting shockingly cheap to run.

The question isn't "can they code" — it's "how far can they go when you give them real autonomy?"

**POINT 2: Default prompts (45 seconds)**

What mistakes do agents make without the default prompts baked into Claude? Claude Code has an enormous system prompt — pages and pages of behavioral guardrails. When you strip that away and give an agent a raw model, what happens? What breaks first?

**POINT 3: Embeddings (45 seconds)**

How can I use embeddings to navigate my own data? I'll be honest — I really only understand them at an interface level. I know what goes in and what comes out. But the middle part? The 4,096 dimensions? I wanted to get my hands dirty and see what they actually enable.

---

## Slide 3: Token Economics

**SETUP (30 seconds)**

Let's talk about cost, because that's what makes all of this viable.

**Ollama Pro — $20/month (45 seconds)**

Ollama Pro at $20 a month is very difficult to exhaust in a week. I've thrown everything at it — DeepSeek v4, Qwen 3, the big models — and I can't burn through the quota. It does get slow during peak periods, but for async agent work that doesn't matter.

**OpenCode Go — $10/month (30 seconds)**

OpenCode Go at $10 a month is a great deal too. It's the agent runtime — the thing that manages the subagents, the tools, the filesystem access. This plus Ollama Pro means $30/month total for an agent that can code all day.

**OpenRouter for embeddings (45 seconds)**

OpenRouter because none of the above have cloud embedding or reranking models. But here's the thing — embedding the whole set of about 1600 documents cost roughly one cent. $0.01. Embedding models are incredibly cheap.

**Local inference (30 seconds)**

Embedding and reranking run alright on a Mac with plenty of unified RAM, but the inference is cheap enough that I don't bother anymore. Qwen 0.6B Embedding is great for this kind of thing — tiny model, fast, good enough.

---

## Slide 4: Tool Ecosystem

**SETUP (45 seconds)**

The ecosystem matters. Each tool has a distinct personality and strengths. Knowing which one to reach for is half the battle.

**OpenCode (60 seconds)**

OpenCode is a great open-source alternative to Claude Code. It's not picky about what model you use or which service — Ollama, OpenRouter, local models, whatever. It's easy to switch between models and specialize per-model subagents. It already has a rich team of built-in subagents for parallelization and context-saving.

This is my primary coding agent. The one I trust with real development work.

**Openclaw (45 seconds)**

Openclaw did some of the data gathering for me. It's learned how to use GitHub Pages in just the way I like, but it tends to write spaghetti code. For anything more technical, it tends to get lost in all the personal details it has access to. It knows too much about me — that's actually a liability for focused coding.

**Hermes Agent (45 seconds)**

Hermes Agent is much less personal than Openclaw and tends to do a great job with devops-type things. It's more opinionated about the kind of help it provides. It's great for things like "figure out why Avahi or systemd or nginx aren't working." I don't ask it to write application code — that's not its strength.

**agent-browser (30 seconds)**

agent-browser is generally simpler for agents to orchestrate at the CLI compared to Playwright. Playwright has a complex API surface. agent-browser just does one thing: navigate, click, extract. Agents don't get lost.

---

## Slide 5: Managing Interns

**STORY SETUP (60 seconds)**

Ten years ago I had this group of eight interns. And working with AI agents feels a lot like managing them. Let me explain.

I gave them tasks that weren't mission-critical without too much guidance. It was more important to see what they could do on their own, where they were comfortable experimenting, and where they needed unambiguous limits.

Often they'd take something in a completely unexpected way, and the results were either delightful or ridiculous.

**The team name story (45 seconds)**

In their first week I told them to pick a team name. I didn't give them any constraints. They came back with something — *(gesture to photo)* — weird and memorable. They used it as a chance to make fun of me because I didn't give them any limits.

That's the delight of giving smart people room to surprise you. And it's the same with agents.

**The obvious things (45 seconds)**

But I'd also have to remind them of things that were obvious. One of them tried to write a stored SQL procedure for a really simple Rails controller — massive overengineering. I had to talk to another one about storing his sweaty gym clothes in a small, shared office. Another didn't show up for meetings because he figured somebody would come get him when it was time.

These aren't competence problems. They're judgment problems. Knowing what matters and what doesn't.

---

## Slide 6: Coding Agents as Interns

**TRANSITION (15 seconds)**

And coding agents are kind of like this. Let me show you the parallels.

**The overengineering parallel (45 seconds)**

They'll solve problems with a tangle of regex if you don't encourage them to install third-party libraries. They'll flail around with curl forever if you don't install agent-browser or Playwright. If the intern thinks it's a good idea to fork systemd, the agent will think it's a good idea to fork systemd.

They need the toolbelt you'd give any junior developer.

**The judgment gaps — rapid-fire (60 seconds)**

- They won't commit or push unless you tell them to.
- They won't run the tests before pushing unless you tell them to.
- They will commit secrets to your git repo, in front of God and everybody, unless you tell them not to.
- They will single-thread their way through an entire task unless you tell them to parallelize.

Every single one of these is the exact same class of problem as the intern who doesn't show up to meetings. Not a capability gap — a judgment gap. The agent CAN do these things. It just doesn't know it should.

---

## Slide 7: Guardrails

**SETUP (30 seconds)**

So the solution isn't smarter models. It's better guardrails. Here's what I've landed on.

**READ EACH GUARDRAIL, pause briefly between:**

- **MUST parallelize with subagents** — Default to dispatching subagents. Doing everything yourself is the exception, not the rule. This applies in ALL modes.

- **Push after successful complex changes** — When completing a series of related changes, commit AND push immediately. ALL tests must be green before pushing.

- **Test new functionality** — Plan and write automated tests as you go. Write regression tests where appropriate.

- **Always specify the subagent type** — When presenting a plan, say "I'll dispatch X to @build, Y to @explore."

- **Type safety is preferred** — When supported by the language.

- **Don't reinvent the wheel** — If a robust library is available, prefer it over implementing from scratch. Use standard package managers. Don't re-test library functionality.

**WHY THIS WORKS (45 seconds)**

The power is that these aren't suggestions. In my AGENTS.md, they're mandates. "MUST parallelize." "Default to dispatching." The guardrails are written like rules, not advice.

And the decision matrix — mapping specific task types to specific models — means the agent doesn't have to guess which model to use. It's algorithmic. Explore → flash model. Refactor → kimi. Tests → hurry model. This eliminates the most common failure mode: using the wrong tool for the job.

---

## Slide 8: Mnestic Architecture

**TRANSITION (30 seconds)**

So what did I actually build with all of this? Something I'd never have bothered to write by hand.

**ORIGIN (45 seconds)**

I had extensive notes over years and years — different formats, different tools, different levels of quality. I wanted to organize them and find connections between them. I wanted to apply the same process to my work notes and give my agents deep access to context about my workday.

And I wanted to understand embedding models better. This part was a little frustrating because — as I said — I honestly only get how they work at an interface level.

**ARCHITECTURE WALKTHROUGH — point to diagram (90 seconds)**

*(Show mnestic-architecture.html)*

Here's the flow. On the left, notes come from three sources: Zoom transcripts, manual notes I write, and work logs. Claude processes the Zoom transcripts — it captures the AI summaries, applies my styleguide for notes, and dumps structured markdown into the system.

That structured content goes into OpenViking, which is the ingestion engine. It uses ChromaDB with qwen3-embedding-8b — that's the 4096-dimension embedding model. Every note gets turned into a vector in that space.

On the front, there's an MCP server. That's the interface. Any agent — Hermes, OpenCode, Openclaw — can query it using standard MCP tools. Semantic search, similarity queries, browsing by tag or date.

And the similarity cloud on the right — that's the visualization. Notes with >75% cosine similarity cluster together. The clusters are meaningful. You can see note series, related topics, and connections you'd never find by searching keywords.

---

## Slide 9: Embeddings Explained

**SETUP (30 seconds)**

Let me try to explain embeddings the way I wish someone had explained them to me.

**THE ANALOGY (60 seconds)**

*(Show embedding-viz.html)*

Embeddings are sort of a part of an LLM. They take input — a word, a sentence, a document — and return a set of coordinates. In this case, coordinates in 4,096 dimensions.

These coordinates are relative to meaning. "Uncle" and "aunt" occupy positions that share a relationship — the same relationship that "man" and "woman" share. When you compress the dimensions down to just three for visualization, you can see this.

**COSINE DISTANCE (45 seconds)**

The "difference" between two embeddings is the cosine distance — the angle between the two vectors from the center. Near-zero means very similar meaning. Near-180 means very different.

This is what makes semantic search work. You're not matching keywords — you're matching meaning. "Sad" is close to "unhappy" even though they share no letters.

---

## Slide 10: Mnestic Demo

**SETUP (15 seconds)**

Let me show you what this looks like in practice.

*(Play mnestic-demo.mp4 OR do live demo)*

**DURING DEMO — narrate these points:**

1. "What you're seeing here is a cloud of notes with >75% relationship to each other. The clusters are meaningful. It finds notes from the same series very easily."

2. *(Show an agent query)* "This makes it really easy for different agents to tap into the MCP frontend and get a ton of detailed context. Any agent that speaks MCP can query my entire note history."

3. *(Show Zoom → Mnestic flow)* "My work notes are mostly generated from Zoom transcripts. Claude goes into Zoom, captures the AI summaries, and applies my styleguide for notes before dumping into Mnestic."

4. *(Show cross-session recall)* "And then in the next session, it's actually able to follow threads like 'Alan promised to send Ale an email, did he remember?' — that kind of cross-session memory is the whole point."

---

## Slide 11: Closing

**WRAP-UP (90 seconds)**

So here's what I learned.

You can get a shocking number of LLM tokens for $20 a month now. Ollama Pro is so generous I can't use it up, and I can let smarter models than I technically need do the dirty work.

Chinese companies are delivering a lot of great work in open-weights models. GLM 5.1, Kimi k2.6, DeepSeek v4 — these are competitive with the flagship models for many tasks.

Plan-then-execute is a common workflow. Most agentic coding tools are built this way — large model to plan, smaller model to execute. We can carry this further with explicit model-to-task mapping and aggressive parallelization.

The guardrails matter more than the model. Give your agents clear mandates, not suggestions. Tell them when to push, when to test, when to parallelize, and when to use a library. They'll follow the rules — they just need the rules.

And finally: I built something I wouldn't have bothered to write by hand. Mnestic took me from scattered notes across years to a queryable knowledge base that any agent can use. The code was written by agents. The architecture was directed by me.

That's writing code like an architect. You don't lay every brick. You design the system, you set the guardrails, and you let the interns do the work.

*(Open for questions)*

---

## Q&A Preparation

**Likely questions and prepared responses:**

**Q: What's the biggest risk of this approach?**
A: The same as any delegation — you can't verify everything. If an agent introduces a subtle bug and the tests don't catch it, you might not find it until much later. That's why I said upfront: don't do this for production-critical code.

**Q: How do you decide what to delegate vs. write yourself?**
A: If it's novel — something I've never done before — I write it. If it's a pattern I've seen a hundred times, I delegate. The agents are great at known patterns, terrible at genuine novelty.

**Q: What happens when the agents disagree with each other?**
A: They don't talk to each other directly — that's by design. Each subagent gets a self-contained task. The orchestrator (OpenCode) resolves conflicts. If two agents produce different implementations of the same thing, I pick one or merge them.

**Q: How do you handle model-specific quirks?**
A: The decision matrix. Different models have different strengths. DeepSeek v4 Flash for exploration — it's fast and token-efficient. Kimi k2.6 for architecture — it has better judgment. MiniMax m2.7 for tests and migrations — fast and reliable on well-defined work. The matrix prevents the "wrong tool for the job" problem.

**Q: Do you worry about model providers going away?**
A: Yes. That's partly why I use open-weights models — they can run anywhere. If Ollama Pro disappeared tomorrow, I could run the same models locally or on another provider. The tooling (OpenCode) doesn't care which backend you use.

---

## Timing Guide

| Section | Target Time |
|---|---|
| Opening + Three Questions | 4 min |
| Token Economics | 3 min |
| Tool Ecosystem | 4 min |
| Managing Interns | 3 min |
| Coding Agents as Interns | 3 min |
| Guardrails | 3 min |
| Mnestic Architecture | 3 min |
| Embeddings Explained | 3 min |
| Mnestic Demo | 4 min |
| Closing | 2 min |
| **Total** | **~32 min** |

*Buffer: 5-8 minutes for transitions, demo glitches, and Q&A setup.*
