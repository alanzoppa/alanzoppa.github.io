# Speaker Notes: Architect Vibes.

CDMX May 28, 2026 — 10 slides

---

## Slide 1: Title

*(Title slide — "Architect Vibes." / "Managing agents like a team of interns." / del Toro: "Making a film is orchestrating an accident.")*

**OPENING (60 seconds)**

I'm going to talk about a deep dive in managing AI agents like a team of interns. It's fair to call this vibe coding, and to be clear — I wouldn't suggest getting this far from your code in production.

---

## Slide 2: Three Questions — "The Premise" (01)

**TRANSITION (15 seconds)**

A few of my personal interests led to this.

**Open-weights models (60 seconds)**

First is open-weights models. These are models like Kimi, GLM and Deepseek that freely release the runnable, retrainable model.

Most of these generate training data with Opus, GPT, etc. This is called distillation. The finished model is typically competitive with the model it was distilled from.

And because the tokens are so cheap, you can almost use them like they're free. That's what's really transformative.

**Agentic tooling (45 seconds)**

I wanted to dive into open-source coding agents. Claude is a really powerful, really polished tool. I use it to automate a ton of day-to-day work tasks.

But it hides most of it's thinking from you, probably because it's embarassing. It fumbles around like it's never ever used a browser every time.

And watching agents think and use tools gives you important insights into how they're working and why they're not doing what you expect.

**Embeddings (30 seconds)**

Last, embeddings are part of how an LLM understands language. They're also lightweight enough that you can run them locally. I'm a little underwater on the math here, but I'll explain more in a bit.

---

## Slide 3: Managing Interns — "The Metaphor" (03)

**STORY SETUP (60 seconds)**

Ten years ago I had this group of eight interns. In their first week I told them to pick a team name. Anything they wanted. And this is what I walked into the next morning.

I tried _not_ to give them a lot of guidance. We'd check in often and steer but I wanted them to feel like they had all the freedom they liked.

The unspoken rule was that we couldn't give them anything mission-critical. It was more important to see what they could do on their own and where they needed limits.

Often they'd take something in a completely unexpected way, and the results were either delightful or ridiculous. This was both.

**The three cards — point to each (75 seconds)**

Because they had room to surprise me, they came up with interesting and weird solutions 

Most of those solutions weren't _good_, but they were interesting. They were lessons. One of them wrote a stored SQL procedure for what should have been a 12-line Rails controller. One named a bunch of variables after ex-girlfriends.

I grew a lot as a manager, too. This was also the first time I had to send an email about office hygiene, and for unrelated reasons the first time I had to fire someone.

---

## Slide 4: Agents as Interns — "The Parallel" (04)

**TRANSITION (15 seconds)**

And coding agents have a lot of the same gaps.

**Walk the list (90 seconds)**

- **They overengineer** — They'll write a tangle of regex like they just learned about them in class. They don't understand your projects scale or how people will use it.
- **They reinvent the wheel** — Won't reach for a library or third-party solution without being told to look.
- Won't check the build, run tests, or push unless you say so explicitly.
- They will commit secrets to your git repo in front of God and everybody.
- **And they Won't tell you you're wrong** — If the solution means forking systemd, it'll quietly start doing that.

---

## Slide 5: Tool Ecosystem — "Tools" (05)

**SETUP (30 seconds)**

Here are the tools I relied on throughout.

**OpenCode (45 seconds)**

This is my primary coding agent. Low-level guardrails — real planning and execution. Shows you its thinking, asks permission only when it matters. "Fix your prompt" is usually enough for it to take the right action.

**OpenClaw (30 seconds)**

Interesting and really powerful but lots of maintenance. In theory it controls its own memories, but it rewrites them into nonsense if you don't keep track.

**Hermes Agent (30 seconds)**

"Just works" for structured tasks. Task orchestration, system integration, workflow design. Built in kanban!

**agent-browser (20 seconds)**

Not AI, it's like a CLI interface for chromium. This is a really easy way to let agents use the web the way you do. For example there's no Yahoo Finance API, so I built a skill to just log in and scrape the HTML.

---

## Slide 6: Token Economics — "Economics" (06)

**SETUP (15 seconds)**

Let's talk about cost. Using the AI freely for whatever talacha you don't want to deal with is the difference. Claude does a great job, but I always feel like I'm on a diet.

**Ollama Pro (45 seconds)**

$20 a month. I've finally built some workflows that exhaust this regularly, but it's a lot for just coding.

**OpenRouter for embeddings (30 seconds)**

OpenRouter because Ollama Pro doesn't have cloud embedding or reranking models. You can totally run Qwen 8B on a MacBook actually, or a smaller version on CPU that's almost as good. But embedding all my notes ever was like a penny or two and much faster.

**The total (15 seconds)**

~$20 a month. For models that are typically more capable than Sonnet.

---

## Slide 7: Guardrails — "The Fix" (06)

**SETUP (30 seconds)**

If you take nothing else away from this, watch how your agents think and use tools. They will find silent workarounds to failing tool calls. They'll go deep on a misunderstanding of your prompt. Catch them and stop them.

You have to convince them to parallelize by default. They really want to do everything in sequence.

They want to stop when the code's done. You have to tell them how and when to run your tests.

You'll have to tell them to write docs.

You'll have to tell them you don't care if the failing test is unrelated.

---

## Slide 8: Embeddings — "The Idea" (07)

**SETUP (15 seconds)**

I said I'd talk about embeddings a little more. Embeddings are cartesian coordinates in more dimensions. Rather than x y and zed, there's typically 256 or more, 4,096 in this case.

The graph shows the most significant 3 dimensions across the same words in four languages. It's kind of a 3D shadow of 4k-space coordinates. The "difference" between two words is the angle between them.

You'll notice that "man" and "woman" have about the same angular relationship as "hombre" and "mujer." The diff between uncle and aunt is about the same.

All the words for "rice" and "train" cluster togehter. It's interesting to me that the Mandarin version is a little askew. They're likely closer in 4k-space, but there are real differences. Like 火车 is literally "fire car" in Chinese, wheras the others are just loan words from English.

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