# Speaker Notes: Architect Vibes.

CDMX May 28, 2026 — 10 slides

---

## Slide 1: Title

*(Title slide — "Architect Vibes." / "Managing agents like a team of interns." / del Toro: "Making a film is orchestrating an accident.")*

**OPENING (60 seconds)**

I'm going to talk about a personal experiment in managing AI agents like a team of interns. It's fair to call this vibe coding, and to be clear — I wouldn't recommend getting this far from your code when there are production consequences.

But that's exactly what made this experiment interesting. When the stakes are low, you can push things much further than you'd ever dare in a production system. And what I found surprised me.

I'm going to start with the premise, then the metaphor, then the parallel, the tools, the economics, the fix, the idea, and finally the payoff.

---

## Slide 2: Three Questions — "The Premise" (01)

**TRANSITION (15 seconds)**

I was interested in three things here. Not "can AI write code" — we all know it can. Deeper questions.

**Open-weights models (60 seconds)**

How far can I push open-weights models? Everyone talks about Claude and GPT-4 — they're the gold standard. But the Chinese companies — Alibaba, Moonshot, Zhipu — are shipping genuinely competitive open models. GLM 5.1, Kimi k2.6, DeepSeek v4. These aren't toys. They're no more than 6 months behind SOTA and they're getting shockingly cheap to run. They're constantly distilling from the frontier models.

**Agentic tooling (45 seconds)**

What happens when you watch an agent work and correct it in real time? Claude Code has an enormous system prompt — pages of behavioral guardrails. When you strip that away and give an agent a raw model, what breaks first? You need visibility into what it's thinking.

**Embeddings (30 seconds)**

How can I use embeddings to navigate my own data? I'll be honest — I only understand enough to be dangerous. I know what goes in and what comes out. The 4,096 dimensions? I wanted to get my hands dirty and see what they actually enable.

---

## Slide 3: Managing Interns — "The Metaphor" (03)

**STORY SETUP (60 seconds)**

Ten years ago I had this group of eight interns. And working with AI agents feels a lot like managing them. Let me explain.

I gave them tasks that weren't mission-critical without too much guidance. It was more important to see what they could do on their own, where they were comfortable experimenting, and where they needed unambiguous limits.

Often they'd take something in a completely unexpected way, and the results were either delightful or ridiculous.

**The three cards — point to each (75 seconds)**

*(Point to the photo)* In their first week I told them to pick a team name. I didn't give them any constraints. They came back with something weird and memorable. They used it as a chance to make fun of me because I didn't give them any limits. That's the delight of giving smart people room to surprise you.

But I'd also have to remind them of things that were obvious. One of them tried to write a stored SQL procedure for what should have been a 12-line Rails controller — massive overengineering.

Another stored his sweaty gym clothes in a small, shared office. Another didn't show up for meetings. No tests. Things you didn't think you'd have to say.

**The callout (15 seconds)**

And the thing is — these aren't competence problems. They're *lessons*. Knowing what matters and what doesn't.

---

## Slide 4: Agents as Interns — "The Parallel" (04)

**TRANSITION (15 seconds)**

And coding agents have a lot of the same gaps. Let me show you the parallels.

**Walk the list (90 seconds)**

- **Overengineering** — Reaching for a clever solution when a boring one was right there. The agent will write 200 lines of regex when a library exists.
- **Reinvents the wheel** — Won't reach for a library or third-party solution without being told to look. If the intern thinks it's a good idea to fork systemd, the agent will think it's a good idea to fork systemd.
- **Needs reminders for the obvious** — Won't check the build, run tests, or push unless you say so explicitly. The intern who doesn't show up to meetings? Same energy.
- **No instinct for what's sensitive** — Credentials, secrets, private data — not on the radar without a rule. They will commit secrets to your git repo, in front of God and everybody.
- **Won't tell you you're wrong** — If the solution means forking systemd, it'll do that. It won't push back and say "this is insane." It'll just quietly execute the terrible plan.

**The key line (15 seconds)**

Every single one of these is a **judgment gap**, not a capability gap. Agents *can* do these things — they just don't know they should.

---

## Slide 5: Tool Ecosystem — "Tools" (05)

**SETUP (30 seconds)**

The ecosystem matters. Each tool has a distinct personality. Different models are good at different things. Knowing which one to reach for is half the battle.

**OpenCode (45 seconds)**

This is my primary coding agent. Low-level guardrails — real planning and execution. Shows you its thinking, asks permission only when it matters. And one of my favorite rules: "User does not give a fuck if the test failure appears unrelated, you never push a red build." That's the energy you need.

**OpenClaw (30 seconds)**

Interesting and really powerful but lots of maintenance. Flexible but high-maintenance agent. It's learned how to use things just the way I like, but it tends to write spaghetti code. And it knows too much about me — that's actually a liability for focused coding.

**Hermes Agent (30 seconds)**

"Just works" for structured tasks. Task orchestration, system integration, workflow design. Kanban! It's great for things like "what tests should we add for monitoring my home server?" I don't ask it to write application code — that's not its strength.

**agent-browser (20 seconds)**

CLI-friendly browser control. Have your agents write deterministic browser code and reuse it. The rule: "Look at the site before you tell me there are no JS errors." Agents don't get lost with a simple CLI tool.

---

## Slide 6: Token Economics — "Economics" (06)

**SETUP (15 seconds)**

Let's talk about cost, because that's what makes all of this viable.

**Ollama Pro (45 seconds)**

$20 a month. Ollama Pro is very difficult to exhaust. I've thrown everything at it — DeepSeek v4, Kimi k2.6, GLM 5.1, the big models — and I can't burn through the quota. It does get slow during peak periods, but for async agent work that doesn't matter.

**OpenRouter for embeddings (30 seconds)**

OpenRouter because Ollama Pro doesn't have cloud embedding or reranking models. But here's the thing — embedding the whole set of about 1,600 documents cost roughly one cent. $0.01. With Qwen 8B Embedding, which is honestly overkill for this. Embedding models are incredibly cheap.

**The total (15 seconds)**

~$20 a month. That's a coding agent that runs all day. Very capable open-weights models at race-to-the-bottom prices.

---

## Slide 7: Guardrails — "The Fix" (06)

**SETUP (30 seconds)**

Watch your agents think and use tools. They will find silent workarounds to failing tool calls. Stop this.

**Walk the pairs — read each thinking line, then the rule (90 seconds)**

*(This slide shows agent thinking on the left, your guardrail on the right. Read each pair.)*

"I will do step A, then step B, then step C." → **You MUST parallelize any tasks that can be completed independently.**

"Code's done, I'm done." → **Run the entire test suite. Commit and push once they're passing.**

"This works and is so obvious it doesn't need comments." → **Include thorough tests in your plan. Suggest regression tests as we go.**

"This test is unrelated, so I'll commit and push." → **Never push a build with failing tests.**

"User is vibe coding and won't read this." → **Use type safety where supported. Adhere to language-specific style guidelines.**

"Perfect, just 500 lines of slop with no dependencies!" → **Use mature, well-tested third-party libraries wherever possible.**

**Why this works (30 seconds)**

These aren't suggestions. They're mandates. The power is that you're preempting the agent's worst instincts — the thoughts you can't see — with rules that close the judgment gap before it opens.

---

## Slide 8: Embeddings — "The Idea" (07)

**SETUP (15 seconds)**

Let me try to explain embeddings the way I wish someone had explained them to me. In only three dimensions.

**The concept (45 seconds)**

*(Point to the plot)* An embedding is just a coordinate. Every word, sentence, or document gets a position in a high-dimensional space — and similar meanings land near each other.

The angle between two vectors — cosine distance — *is* their semantic distance. Near 0° means same meaning. Near 180° means opposite.

**The equation (15 seconds)**

*(Point to the equation)* uncle − man + woman ≈ aunt. This isn't a gimmick. The vector arithmetic actually works — the direction from "man" to "woman" captures gender, and adding it to "uncle" lands near "aunt."

**The insight (15 seconds)**

"Sad" is close to "unhappy" even though they share no letters. You're matching **meaning**, not keywords. That's what makes semantic search work.

**PCA vs UMAP — toggle it (45 seconds)**

*(Toggle between PCA and UMAP)*

I've got two projections here. PCA on the left — linear, global. Finds the three orthogonal axes of greatest variance. 51.3% of the variance is retained. What you see is what is there.

Now toggle to UMAP — nonlinear. It builds a graph of nearest neighbors, then unfolds it into 3D. Tight clusters get tighter. The stress is much lower — 0.084 vs 0.238. But absolute distances between clusters aren't reliable. What you gain in cluster clarity you lose in global faithfulness.

**The practical takeaway (15 seconds)**

Drag the plot, rotate it, toggle between them. This is what your data looks like when you compress 4,096 dimensions into three. It's a lossy view — but a useful one.

---

## Slide 9: Mnestic Demo — "The Payoff" (08)

**SETUP (30 seconds)**

So what did I actually build with all of this? Something I'd never have bothered to write by hand.

I had extensive notes over years and years — different formats, different tools, different levels of quality. I wanted to organize them and find connections between them. I wanted my agents to have deep access to context about my workday.

**Play the video (3-4 minutes)**

*(Click to play the YouTube embed — it's a screen recording of Mnestic in action. Narrate over it.)*

While this plays, here's what you're seeing. Mnestic is a personal knowledge base with semantic search. Notes come in — Zoom transcripts processed by Claude, manual notes I write, work logs — and they get embedded into a 4,096-dimensional space using qwen3-embedding-8b.

Any agent that speaks MCP can query my entire note history. Hermes, OpenCode, Openclaw — they all use the same MCP tools to search, browse, and recall. Semantic search means "sad" finds "unhappy" even though they share no letters.

And the similarity cloud — notes with high cosine similarity cluster together. The clusters are meaningful. You can see note series, related topics, and connections you'd never find by searching keywords.

The whole point: cross-session memory. In the next session, an agent can follow threads like "Alan promised to send Ale an email, did he remember?" — that kind of recall is what makes this worth building.

---

## Slide 10: Takeaways — "Closing" (09)

**WRAP-UP (90 seconds)**

Five takeaways.

**One:** $20 a month gets you a shocking number of tokens. Ollama Pro is generous for a single developer. You can let smarter models than you technically need do the dirty work.

**Two:** Open-weights models are competitive. GLM 5.1, Kimi k2.6, DeepSeek v4 — the Chinese labs are shipping, and they're distilling from the frontier.

**Three:** Plan-then-execute works at scale. Big model plans, smaller models execute, explicit task-to-model mapping. You don't have to use the expensive model for everything.

**Four:** Guardrails matter more than intelligence. Clear mandates — not suggestions — close the judgment gap. The model doesn't need to be smarter. It needs better rules.

**Five:** I built something I wouldn't have written by hand. Mnestic took me from scattered notes across years to a queryable agent knowledge base. The code was written by agents. The architecture was directed by me.

**Close with del Toro (15 seconds)**

To me, the director as dictator makes no sense. The director as prophet makes sense. That's writing code like an architect. You don't lay every brick. You set the vision, you set the guardrails, and you let the interns do the work.

*(Open for questions)*

---

## Q&A Preparation

**Likely questions and prepared responses:**

**Q: What's the biggest risk of this approach?**
A: The same as any delegation — you can't verify everything. If an agent introduces a subtle bug and the tests don't catch it, you might not find it until much later. That's why I said upfront: don't do this for production-critical code.

**Q: How do you decide what to delegate vs. write yourself?**
A: If it's novel — something I've never done before — I write it. If it's a pattern I've seen a hundred times, I delegate. Agents are great at known patterns, terrible at genuine novelty.

**Q: What happens when the agents disagree with each other?**
A: They don't talk to each other directly — that's by design. Each subagent gets a self-contained task. The orchestrator resolves conflicts. If two agents produce different implementations, I pick one or merge them.

**Q: How do you handle model-specific quirks?**
A: Task-to-model mapping. DeepSeek v4 Flash for exploration — fast and token-efficient. Kimi k2.6 for architecture — better judgment. GLM 5.1 for routine work. The matrix prevents the "wrong tool for the job" problem. This is all in my AGENTS.md — it's algorithmic, not guesswork.

**Q: Do you worry about model providers going away?**
A: Yes. That's partly why I use open-weights models — they can run anywhere. If Ollama Pro disappeared tomorrow, I could run the same models locally or on another provider. The tooling (OpenCode) doesn't care which backend you use.

---

## Timing Guide

| Slide | Section | Target Time |
|---|---|---|
| 1 | Title / Opening | 1 min |
| 2 | Three Questions | 2.5 min |
| 3 | Managing Interns | 2.5 min |
| 4 | Agents as Interns | 2 min |
| 5 | Tool Ecosystem | 2.5 min |
| 6 | Token Economics | 1.5 min |
| 7 | Guardrails | 2 min |
| 8 | Embeddings | 2.5 min |
| 9 | Mnestic Demo (video) | 3-4 min |
| 10 | Takeaways / Closing | 2 min |
| | **Total** | **~22-24 min** |

*Buffer: 5-8 minutes for transitions, demo video, and Q&A setup. The video does the heavy lifting on the demo slide — let it play and narrate over it.*
