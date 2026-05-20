# Architect Vibes. — Presentation Plan

**Talk:** CDMX, May 28, 2026
**Format:** Self-contained HTML slide deck (`index.html`)
**Slides:** 10 · ~22-24 minutes + Q&A
**Speaker notes:** `SPEAKER_NOTES.md`

---

## Overview

A personal retrospective on building software through AI agents — not as a typist, but as an architect directing autonomous subagents. The through-line: open-weights models are competitive, guardrails matter more than model intelligence, and you can get a surprising amount done for ~$20/month.

Bookended by Guillermo del Toro quotes: "Making a film is orchestrating an accident" (opening) and "The director as prophet makes sense" (closing).

---

## Slide Breakdown

### Slide 1: Title
**"Architect Vibes."** — "Managing agents like a team of interns."
- Headshot (8-bit pixel art style) + Alan Zoppa · Chicago · May 28, 2026
- del Toro: "Making a film is orchestrating an accident."
- Media: `headshot-8bit.png`

### Slide 2: Three Questions (01 — The Premise)
Three numbered items:
1. **Open-weights models** — No more than 6 months behind SOTA, low prices, constantly distilling
2. **Agentic Tooling** — Watch how it works and correct it when it goes wrong
3. **Embeddings** — I only understand enough to be dangerous. How can I use them to navigate my own data?

### Slide 3: Managing Interns (03 — The Metaphor)
"Once, I managed eight interns."
- Left: `interns.jpg` — team photo
- Right: three cards
  - Give them room to surprise you (ridiculous team name)
  - They'll overengineer (stored SQL procedure for a 12-line controller)
  - They need limits that would seem obvious (gym clothes, missed meetings, no tests)
- Callout: "These aren't competence problems. They're lessons."
- Media: `interns.jpg`

### Slide 4: Agents as Interns (04 — The Parallel)
"Coding agents have a lot of the same gaps."
- Overengineering → reaching for clever when boring was right there
- Reinvents the wheel → won't use libraries without being told
- Needs reminders for the obvious → won't check build, run tests, or push
- No instinct for what's sensitive → credentials, secrets not on the radar
- Won't tell you you're wrong → will fork systemd if that's the solution
- Key line: "Every one of these is a **judgment gap**, not a capability gap."

### Slide 5: Tool Ecosystem (05 — Tools)
"Open-source tooling. Different models are good at different things."
Four cards in a 2×2 grid:
- **OpenCode** — Low-level guardrails. Real planning and execution. "User does not give a fuck if the test failure appears unrelated, you never push a red build."
- **OpenClaw** — Flexible but high-maintenance. "Why do you keep forgetting this?"
- **Hermes Agent** — "Just works" for structured tasks. Task orchestration, Kanban. "What tests should we add for monitoring my home server?"
- **agent-browser** — CLI-friendly browser control. "Look at the site before you tell me there are no JS errors."
- Media: `tools-ecosystem.png`

### Slide 6: Token Economics (06 — Economics)
"$20/month buys agents that run all day."
- Table: Ollama Pro ($20/mo → DeepSeek v4, Kimi k2.6, GLM 5.1), OpenRouter (~$0.01 → embed ~1,600 docs with Qwen 8B), Total ~$20/mo
- "Very capable open-weights models are available at race-to-the-bottom prices."

### Slide 7: Guardrails (06 — The Fix)
"Watch your agents think and use tools. They will find silent workarounds."
Six pairs — agent thinking on the left, guardrail on the right:
1. "I will do step A, then step B, then step C." → MUST parallelize
2. "Code's done, I'm done." → Run tests, commit and push when passing
3. "This works, so obvious it doesn't need comments." → Include thorough tests
4. "This test is unrelated, so I'll commit and push." → Never push a red build
5. "User is vibe coding and won't read this." → Type safety, style guidelines
6. "Perfect, 500 lines of slop with no dependencies!" → Use mature third-party libraries

### Slide 8: Embeddings (07 — The Idea)
"Embeddings in only three dimensions."
- Left: prose explanation — embedding = coordinate, cosine distance = semantic distance, "uncle − man + woman ≈ aunt", "Sad is close to unhappy even though they share no letters"
- Right: interactive 3D Plotly visualization with PCA/UMAP toggle
  - PCA: linear, global, 51.3% variance retained, stress 0.238
  - UMAP: nonlinear, neighbors 5, stress 0.084
  - Draggable, rotatable, toggle to compare
- "Drag the plot to rotate · toggle to compare"
- Media: inline word-vector data (Plotly), `word_vectors_3d.html` (standalone version)

### Slide 9: Mnestic Demo (08 — The Payoff)
"Mnestic — live"
- YouTube embed (`XCLMAZbMCr4`) — screen recording of Mnestic in action
- Click to play inline, with "Open on YouTube ↗" fallback link
- Shows: semantic search, MCP agent queries, Zoom → Claude → Mnestic pipeline, similarity cloud

### Slide 10: Takeaways (09 — Closing)
"Five takeaways"
1. $20/month gets you a shocking number of tokens — Ollama Pro is generous
2. Open-weights models are competitive — Chinese labs are shipping (and distilling)
3. Plan-then-execute works at scale — big model plans, smaller models execute
4. Guardrails matter more than intelligence — clear mandates close the judgment gap
5. I built something I wouldn't have written by hand — Mnestic
- Final quote: "The director as prophet makes sense." — Guillermo del Toro

---

## Media Assets

### In the directory
| File | Slide | Description |
|---|---|---|
| `index.html` | All | Self-contained slide deck with inline Plotly data |
| `headshot-8bit.png` | 1 | 8-bit pixel art headshot |
| `interns.jpg` | 3 | Intern team photo |
| `interns-comparison.png` | 3-4 | Intern vs agent behavior visual (backup visual) |
| `tools-ecosystem.png` | 5 | Tool ecosystem diagram |
| `word_vectors_3d.html` | 8 | Standalone 3D word vectors visualization |

### External / Embedded
| Resource | Slide | Description |
|---|---|---|
| YouTube `XCLMAZbMCr4` | 9 | Mnestic demo screen recording |
| Plotly CDN (`plotly-3.0.1.min.js`) | 8 | 3D scatter plot library (loaded from CDN) |

---

## Delivery

1. Open `index.html` in a browser — arrow keys or click zones to navigate
2. Press `?` for keyboard shortcut help
3. Press `F` for fullscreen
4. Have `SPEAKER_NOTES.md` open in a separate window for cues
5. The YouTube embed on slide 9 is click-to-play — click the play button to start the demo video
