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

I have a few interests in specific areas of AI that led me here.

**Open-weights models (60 seconds)**

First is an interest in open-weights models. These are models like Kimi, GLM and Deepseek that freely release the runnable, retrainable model. This makes them really cheap to run.

Many of these focus on architecture and generate training data with Opus, GPT, etc. This is distillation. The finished model is typically competitive with the model it was distilled from.

But because the tokens are so cheap, I can almost use them like they're free. That's really transformative.

**Agentic tooling (45 seconds)**

Claude is a really powerful, really polished tool. I use it to automate a ton of day-to-day work tasks.

And it hides most of it's thinking from you because it's embarassing. It fumbles around like it's never ever used a browser unless you create a skill. Every agentic tool does this. Hermes is probably the best at self-correction.

Watching them think and use tools gives you important insights into how they're working and why they're not doing what you expect.

**Embeddings (30 seconds)**

Embeddings are part of how an LLM understands language. They're also lightweight enough that you can usually run them locally. I'm a little underwater on the math here, but I'll explain a bit more later.

---

## Slide 3: Managing Interns — "The Metaphor" (03)

**STORY SETUP (60 seconds)**

Ten years ago I had this group of eight interns. In their first week I told them to pick a team name. Anything they wanted. And this is what I walked into the next morning.

That's Hao Lin. She's been at Microsoft for the last nine years. And Shayna is a Tech Lead at the same company we worked at here for as long.

One of the rules of the intern program was that we didn't put them on anything mission-critical. There were lots of proofs of concepts.

And that way I didn't have to give them a lot of guidance. We'd check in often and steer but I wanted them to feel like they had all the freedom they liked.

I gave them tasks that weren't mission-critical without too much guidance. The unspoken rule was that we couldn't give them anything mission-critical. It was more important to see what they could do on their own, where they were comfortable experimenting, and where they needed limits.

Often they'd take something in a completely unexpected way, and the results were either delightful or ridiculous. This was both.

**The three cards — point to each (75 seconds)**

They came up with interesting and weird solutions because they had room to surprise me.

Most of those weren't good, but they were interesting. They were lessons. One of them wrote a stored SQL procedure for what should have been a really simple Rails controller.

I grew a lot as a manager, too. This was also the first time I had to send an email about odors in shared spaces, and the first time I had to let someone go.

**The callout (15 seconds)**

And the thing is — these aren't competence problems. They're *lessons*. Whatever they produced during their internship didn't matter. The mistakes were just as helpful as the successes.

---

## Slide 4: Agents as Interns — "The Parallel" (04)

**TRANSITION (15 seconds)**

And coding agents have a lot of the same gaps.

**Walk the list (90 seconds)**

- **Overengineering** — It'll write a tangle of regex like it just learned about them in class. It doesn't understand your projects scale or how people will use it.
- **Reinvents the wheel** — Won't reach for a library or third-party solution without being told to look. I had to word this very strongly in my prompt.
- **Needs reminders for the obvious** — Won't check the build, run tests, or push unless you say so explicitly.
- **No instinct for what's sensitive** — They will commit secrets to your git repo, in front of God and everybody.
- **Won't tell you you're wrong** — If the solution means forking systemd, it'll do that. It won't push back and say "this is insane." It'll just quietly execute the terrible plan.

**The key line (15 seconds)**

Every single one of these is a **judgment gap**, not a capability gap. Agents *can* do these things — they just don't know they should.

---

## Slide 5: Tool Ecosystem — "Tools" (05)

**SETUP (30 seconds)**

The ecosystem matters. Different models are good at different things.

**OpenCode (45 seconds)**

This is my primary coding agent. Low-level guardrails — real planning and execution. Shows you its thinking, asks permission only when it matters. "Fix your prompt" is usually enough for it to take the right action.

**OpenClaw (30 seconds)**

Interesting and really powerful but lots of maintenance. In theory it controls its own memories, but it rewrites them into nonsense if you don't watch it.

**Hermes Agent (30 seconds)**

"Just works" for structured tasks. Task orchestration, system integration, workflow design. Kanban! It's great for things like "what tests should we add for monitoring my home server?" It plans and orchestrates, then uses opencode for most of the actual coding.

**agent-browser (20 seconds)**

CLI-friendly browser control. Have your agents write deterministic browser code and reuse it. Sometimes needs a custom skill, but this is a really easey way to make your agents see the web the way you do.

---

## Slide 6: Token Economics — "Economics" (06)

**SETUP (15 seconds)**

Let's talk about cost, because that's what's really transformative about this. Using the AI freely for whatever talacha you don't want to deal with is the difference. Claude does a great job, but I always feel like I'm on a diet.

**Ollama Pro (45 seconds)**

$20 a month. I've finally built some workflows that exhaust this regularly, but it's a lot for just coding. It does get slow during peak periods, but for async agent work that doesn't matter. The kanban board in hermes is my favorite way to work around this.

**OpenRouter for embeddings (30 seconds)**

OpenRouter because Ollama Pro doesn't have cloud embedding or reranking models. You can totally run Qwen 8B on a MacBook actually, or a smaller version on CPU that's almost as good. But embedding all my notes ever was like a penny or two in openrouter credits.

**The total (15 seconds)**

~$20 a month. For models that are typically more capable than Sonnet.

---

## Slide 7: Guardrails — "The Fix" (06)

**SETUP (30 seconds)**

Watch your agents think and use tools. They will find silent workarounds to failing tool calls. Stop this.

**Walk the pairs — read each thinking line, then the rule (90 seconds)**

"I will do step A, then step B, then step C." → **You MUST parallelize any tasks that can be completed independently.**

"Code's done, I'm done." → **Run the entire test suite. Commit and push once they're passing.**

"This works and is so obvious it doesn't need comments." → **Include thorough tests in your plan. Suggest regression tests as we go.**

"This test is unrelated, so I'll commit and push." → **Never push a build with failing tests.**

"User is vibe coding and won't read this." → **Use type safety where supported. Adhere to language-specific style guidelines.**

"Perfect, just 500 lines of slop with no dependencies!" → **Use mature, well-tested third-party libraries wherever possible.**

---

## Slide 8: Embeddings — "The Idea" (07)

**SETUP (15 seconds)**

I said I'd talk about embeddings a little more. Embeddings are cartesian coordinates in more dimensions. Rather than x y an z, there's typically 256 to 4096 dimensions.

The graph on the right shows the most significant 3 dimensions across these words. The "difference" between two words is basically the angle between them. What's interesting is that the words for aunt and uncle have similar relationships across languages. Four different words for rice and four different words for train end up in clusters.

This is a less honest projection, but forces some relationships in 3-space that you wouldn't see otherwise.

---

## Slide 9: Mnestic Demo — "The Payoff" (08)

**SETUP (30 seconds)**

What I actually wanted was a way to help agents navigate my notes and generate them consistently. Before this I copy-pasted stuff from Zoom into Gemini and then into a Google Doc. Now I just have another agent do the whole thing end-to-end. Claude suggested more tools and I had opencode build them.

**

So this is what I built. You can search by cosine distance from your query and get some data about the results. This is not a particularly meaningful search.

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
