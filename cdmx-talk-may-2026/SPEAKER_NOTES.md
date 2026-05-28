# Speaker Notes: Architect Vibes.

CDMX May 28, 2026 — 10 slides

---

## Slide 1: Title

*(Title slide — "Architect Vibes." / "Managing agents like a team of interns." / del Toro: "Making a film is orchestrating an accident.")*

**OPENING (60 seconds)**

I'm going to talk about a deep dive in managing AI agents like a team of interns. It's fair to call this vibe coding, and to be clear — I wouldn't suggest getting this far from your code when there are production consequences.

---

## Slide 2: Three Questions — "The Premise" (01)

**TRANSITION (15 seconds)**

A few of my personal interests led to this.

**Open-weights models (60 seconds)**

First is an interest in open-weights models. These are models like Kimi, GLM and Deepseek that freely release the runnable, retrainable model.

Most of these generate training data with Opus, GPT, etc. This is called distillation. The finished model is typically competitive with the model it was distilled from.

And because the tokens are so cheap, you can almost use them like they're free. That's really transformative.

**Agentic tooling (45 seconds)**

Claude is a really powerful, really polished tool. I use it to automate a ton of day-to-day work tasks.

But it hides most of it's thinking from you because it's embarassing. It fumbles around like it's never ever used a browser every time.

Watching agents think and use tools gives you important insights into how they're working and why they're not doing what you expect.

**Embeddings (30 seconds)**

Embeddings are part of how an LLM understands language. They're also lightweight enough that you can usually run them locally. I'm a little underwater on the math here, but I'll explain more in a bit.

---

## Slide 3: Managing Interns — "The Metaphor" (03)

**STORY SETUP (60 seconds)**

Ten years ago I had this group of eight interns. In their first week I told them to pick a team name. Anything they wanted. And this is what I walked into the next morning.

I tried not to give them a lot of guidance. We'd check in often and steer but I wanted them to feel like they had all the freedom they liked.

 The unspoken rule was that we couldn't give them anything mission-critical. It was more important to see what they could do on their own, where they were comfortable experimenting, and where they needed limits.

Often they'd take something in a completely unexpected way, and the results were either delightful or ridiculous. This was both.

**The three cards — point to each (75 seconds)**

Because they had room to surprise me, they came up with interesting and weird solutions 

Most of those solutions weren't good, but they were interesting. They were lessons. One of them wrote a stored SQL procedure for what should have been a 12-line Rails controller.

I grew a lot as a manager, too. This was also the first time I had to send an email about hygiene, and the first time I had to fire someone.

---

## Slide 4: Agents as Interns — "The Parallel" (04)

**TRANSITION (15 seconds)**

And coding agents have a lot of the same gaps.

**Walk the list (90 seconds)**

- **Overengineering** — They'll write a tangle of regex like they just learned about them in class. They don't understand your projects scale or how people will use it.
- **Reinvents the wheel** — Won't reach for a library or third-party solution without being told to look.
- Won't check the build, run tests, or push unless you say so explicitly.
- They will commit secrets to your git repo in front of God and everybody.
- **Won't tell you you're wrong** — If the solution means forking systemd, it'll quietly start doing that.

---

## Slide 5: Tool Ecosystem — "Tools" (05)

**SETUP (30 seconds)**

Here are the tools I relied on throughout this.

**OpenCode (45 seconds)**

This is my primary coding agent. Low-level guardrails — real planning and execution. Shows you its thinking, asks permission only when it matters. "Fix your prompt" is usually enough for it to take the right action.

**OpenClaw (30 seconds)**

Interesting and really powerful but lots of maintenance. In theory it controls its own memories, but it rewrites them into nonsense if you don't watch it.

**Hermes Agent (30 seconds)**

"Just works" for structured tasks. Task orchestration, system integration, workflow design. Kanban!

**agent-browser (20 seconds)**

Not AI, but the perfect tool for giving your agents a command-line browser. This is a really easy way to let them see the web the way you do.

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

Watch your agents think and use tools. They will find silent workarounds to failing tool calls. Notice this and stop it.

I had to convince them to parallelize by default. They really want to do everything in sequence.

They want to stop when the code's done. You have to tell them how and when to run your tests.

You'll have to tell them to write docs.

You'll have to tell them you don't care if the failing test is unrelated.

---

## Slide 8: Embeddings — "The Idea" (07)

**SETUP (15 seconds)**

I said I'd talk about embeddings a little more. Embeddings are cartesian coordinates in more dimensions. Rather than x y an z, there's typically 256 or more.

The graph on the right shows the most significant 3 dimensions across these words. It's kind of a 3-space shadow of 4k-space coordinates. The "difference" between two words is the angle between them.

You'll notice that "man" and "woman" have about the same angular relationship as "hombre" and "mujer." The diff between uncle and aunt is about the same.

All the words for "rice" and "train" cluster togehter. It's interesting that the Mandarin version is a little askew. They're likely closer in 4k-space, but there are real differences. Like 火车 is literally "fire car" in Chinese, wheras the others are just straight loan words from English.

---

## Slide 9: Mnestic Demo — "The Payoff" (08)

**SETUP (30 seconds)**

What I actually wanted was a way to help agents navigate my notes and generate them consistently. Before this I copy-pasted stuff from Zoom into Gemini and then into a Google Doc. Now I just have another agent do the whole thing end-to-end. 

**

So this is what I built. You can search by cosine distance from your query and get some data about the results. This is not a particularly meaningful search.

This is just everything most recent. This is when I had hermes find a local HVAC contractor for me.

Tags, you know how tags work.

I don't remember what I was doing on that Feb. 17th...

And here's the fun stuff. This is everything with 75%+ cosine similarity. Kinda amazing what we can do with WebGL now.

When we crank the minimum similarity down you start to see this dense cobwebs connecting all the embeddings.

There's also a search graph. We can spin it around the same way, but this shows us the best match in red and the worst matches in blue.

That's just an excerpt from Snow Crash by Neal Stephenson.



---

## Slide 10: Takeaways — "Closing" (09)

**WRAP-UP (90 seconds)**

Five takeaways.

**One:** $20 a month gets you a shocking number of tokens. Ollama Pro is generous for a single developer. You can let DeepSeek Pro plan and let smarter models than you technically need handle implementation.

**Two:** Open-weights models are competitive. GLM 5.1, Kimi k2.6, DeepSeek v4 — the Chinese labs are distillinga and shipping every few months.

**Three:** Plan-then-execute works at scale. Big model plans, smaller models execute, explicit task-to-model mapping. You don't have to use the expensive model for everything.

**Four:** I built something I wouldn't have written by hand. Mnestic took me from scattered notes across years to a queryable agent knowledge base. The code was written by agents. The architecture was directed by me.