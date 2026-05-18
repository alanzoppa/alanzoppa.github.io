# Presentation Plan: Writing Code Like an Architect

A Personal Experiment in Vibe Coding

**Talk:** CDMX, May 28, 2026
**Duration:** ~15 minutes + Q&A
**Format:** Marp slide deck (SLIDES.md) with speaker notes (SPEAKER_NOTES.md)

---

## Overview

This talk is a personal retrospective on building software through AI agents — not as a typist, but as an architect directing autonomous subagents. The through-line: open-weights models are competitive, guardrails matter more than model intelligence, and you can get a shocking amount done for $30/month.

**Three research questions anchor the talk:**

1. How far can I push open-weights models vs. flagship models?
2. What mistakes do agents make without Claude's default system prompts?
3. How can I use embeddings to navigate my own data?

**The project that ties it together:** Mnestic — a personal knowledge base with semantic search, built almost entirely by AI agents, now queryable by any agent via MCP.

---

## Slide Breakdown

### Slide 1: Title

**Content:** Talk title, name, subtitle "A Personal Experiment in Vibe Coding." Dark theme, minimalist.

**Media:** None (text-only title slide)

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 1 — Opening hook (60s)

---

### Slide 2: The Three Questions

**Content:** Three numbered research questions displayed as a list. Each question gets a one-line expansion. Visual: simple numbered list with icons or bold numbers.

1. **Open-weights models** — How far can they go with real autonomy?
2. **Open-source tools** — What degrees of freedom are available?
3. **Embeddings** — How can I use them to navigate my own data?

**Media:** None

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 2 — Three questions expanded (3 min)

---

### Slide 3: Token Economics

**Content:** Cost breakdown as a visual table or card layout. Four items with dollar amounts and key stats:

| Service | Cost | What You Get |
|---|---|---|
| Ollama Pro | $20/mo | Nearly inexhaustible tokens, DeepSeek v4, Qwen 3 |
| OpenRouter | ~$0.01 | Embed ~1600 documents (Qwen 8B Embedding) |
| **Total** | **~$20/mo** | A coding agent that runs all day |

Optional callout: "Embedding 1600 documents cost one cent."

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 3 — Cost narrative (3 min)

---

### Slide 4: Tool Ecosystem

**Content:** Four-tool comparison showing distinct personalities and strengths. Visual: four cards or quadrants.

| Tool | Role | Best For |
|---|---|---|
| **OpenCode** | Primary coding agent | Real dev work, subagent orchestration |
| **Hermes Agent** | Agentic assistant | System debugging (Avahi, systemd, nginx) |
| **agent-browser** | Web automation | CLI-friendly browser control for agents |

Key message: knowing which tool to reach for is half the battle.

**Media:** `tools-ecosystem.png` — visual showing tool ecosystem and connections

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 4 — Tool walkthrough (4 min)

---

### Slide 5: Managing Interns

**Content:** Split layout. Left side: the intern photo (`interns.jpg`). Right side: three bullet points from the story:

- **Give them room to surprise you** — they picked a ridiculous team name and made fun of me
- **They'll overengineer** — stored SQL procedure for a simple Rails controller
- **They need obvious limits** — gym clothes in the office, skipped meetings

Transition line: "These aren't competence problems. They're judgment problems."

**Media:**
- `interns.jpg` — photo of the intern team (primary visual for this slide)
- `interns-comparison.png` — side-by-side intern vs. agent behaviors (can be Slide 6 or a second visual here)

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 5 — Intern story (3 min)

---

### Slide 6: Coding Agents as Interns

**Content:** Parallel behaviors — intern on the left, agent on the right. Five rows:

| Intern Behavior | Agent Behavior |
|---|---|
| Overengineers a simple task | Solves problems with regex tangles |
| Needs to be told to show up | Won't commit or push unless told |
| Needs to be reminded of basics | Won't run tests before pushing |
| No sense of what's sensitive | Commits secrets to git |
| Does one thing at a time | Single-threads through tasks |

Key message: every one of these is a judgment gap, not a capability gap. Agents CAN do these things — they just don't know they should.

**Media:** `interns-comparison.png` — the side-by-side visual (primary for this slide)

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 6 — Agent parallels (3 min)

---

### Slide 7: Guardrails

**Content:** Six guardrail rules displayed as a checklist or card grid. Title: "The Solution Isn't Smarter Models — It's Better Guardrails."

- **MUST parallelize with subagents** — Dispatching is the default; solo work is the exception
- **Push after successful complex changes** — Commit AND push; all tests green first
- **Test new functionality** — Write automated tests as you go; regression tests where needed
- **Always specify the subagent type** — "I'll dispatch X to @build, Y to @explore"
- **Type safety is preferred** — When supported by the language
- **Don't reinvent the wheel** — Prefer robust libraries; don't re-test library functionality

**Media:**
- `guardrails-checklist.png` — visual checklist rendering
- `guardrails-in-action.gif` — 30-second demo of guardrails working (auto-test, auto-push, library preference)

**Decision matrix callout:** Add a smaller inset or transition note showing the model-to-task mapping (Slide 7b or a reveal):
> Explore → @flash / DeepSeek v4 Flash · Refactor → @kimi / Kimi k2.6 · Tests → @hurry / MiniMax m2.7

**Media:** `model-decision-matrix.png` — the model assignment table as a styled card

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 7 — Guardrails walkthrough + decision matrix (3 min)

---

### Slide 8: Mnestic Architecture

**Content:** Architecture diagram showing the full pipeline. Left to right flow:

```
[Zoom Transcripts] ──┐
[Manual Notes]     ──┤
[Work Logs]        ──┘
        │
        ▼
  [Claude Processing]
  transcript → styleguide → structured markdown
        │
        ▼
  [OpenViking Ingestion]
  ChromaDB + qwen3-embedding-8b (4096-dim)
        │
        ▼
  [MCP Server Frontend]
        │
        ├──→ [Hermes Agent]
        ├──→ [OpenCode]
        └──→ [Openclaw]
        │
        ▼
  [Similarity Cloud]
  Notes clustered by >75% cosine similarity
```

**Media:** `mnestic-architecture.html` — dark-themed SVG architecture diagram (primary visual)

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 8 — Architecture walkthrough (3 min)

---

### Slide 9: Embeddings Explained

**Content:** Intuitive, non-mathematical explanation of embeddings. Two visual concepts:

1. **The word relationship:** "uncle" is to "aunt" as "man" is to "woman" — shown as arrows in a reduced 3D space
2. **Cosine distance:** angle between two vectors = semantic difference. Near-zero = similar meaning. Near-180 = very different.

Key insight: "Sad is close to unhappy even though they share no letters. You're matching meaning, not keywords."

**Media:** `embedding-viz.html` — interactive 3D visualization of word relationships and cosine distance

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 9 — Embeddings explained (3 min)

---

### Slide 10: Mnestic Demo

**Content:** Placeholder slide for the live or recorded demo. Shows:

- The Mnestic web UI with note similarity cloud
- An agent querying via MCP (Hermes or OpenCode using `mcp_mnestic_*` tools)
- Zoom transcript → Claude → Mnestic pipeline result
- Cross-session memory: "Alan promised to send Ale an email, did he remember?"

**Media:** `mnestic-demo.mp4` — 2-3 minute screen recording (primary; or live demo)

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 10 — Demo narration cues (4 min)

---

### Slide 11: Closing

**Content:** Five takeaways displayed as a summary list:

1. **$20/month gets you a shocking number of tokens** — Ollama Pro is nearly inexhaustible
2. **Open-weights models are competitive** — GLM 5.1, Kimi k2.6, DeepSeek v4 from Chinese labs
3. **Plan-then-execute works at scale** — Large model plans, smaller models execute, explicit task-to-model mapping
4. **Guardrails matter more than model intelligence** — Clear mandates, not suggestions
5. **I built something I wouldn't have bothered to write by hand** — Mnestic: scattered notes → queryable agent knowledge base

Final line: "That's writing code like an architect. You don't lay every brick. You design the system, you set the guardrails, and you let the interns do the work."

**Media:** None (text-only)

**Speaker notes reference:** SPEAKER_NOTES.md §Slide 11 — Closing + Q&A prep (2 min + buffer)

---

## Media Punch List

All media assets needed for the presentation. See `PUNCHLIST.md` for detailed creation instructions.

### Screen Recordings & GIFs

| # | Asset | Filename | Slides | Description |
|---|---|---|---|---|
| 1 | Mnestic demo | `mnestic-demo.mp4` | 10 | 2-3 min: UI cloud, MCP query, Zoom→Mnestic pipeline, cross-session recall |
| 2 | Agent parallelization | `agent-parallelization.gif` | 7 | 30-60s: OpenCode dispatching subagents, decision matrix in action |
| 3 | Guardrails in action | `guardrails-in-action.gif` | 7 | 30s: auto-test, auto-push, library-over-regex preference |
| 4 | Token cost demo | `token-cost-demo.mp4` | 3 | (Optional) 1 min: Ollama Pro dashboard, OpenRouter billing, subscription pages |

### Diagrams & Visuals

| # | Asset | Filename | Slides | Description |
|---|---|---|---|---|
| 5 | Mnestic architecture | `mnestic-architecture.html` | 8 | Dark SVG: note sources → Claude → ChromaDB → MCP → agents → similarity cloud |
| 6 | Embedding visualization | `embedding-viz.html` | 9 | Dark HTML: word relationships in 3D space, cosine distance explanation |
| 7 | Model decision matrix | `model-decision-matrix.png` | 7 | Styled table: Task Type × Subagent × Model × Why |
| 8 | Guardrails checklist | `guardrails-checklist.png` | 7 | Visual checklist of all six guardrail rules |
| 9 | Tools ecosystem | `tools-ecosystem.png` | 4 | Visual: four tools, their roles, and relationships |
| 10 | Interns comparison | `interns-comparison.png` | 5 or 6 | Side-by-side: intern behaviors ↔ agent behaviors |

### Existing Assets

| # | Asset | Filename | Slides | Description |
|---|---|---|---|---|
| 11 | Intern team photo | `interns.jpg` | 5 | Photo of the eight interns (already present) |

### Total: 10 new media assets + 1 existing photo

---

## Supporting Documents

| Document | Status | Purpose |
|---|---|---|
| `PRESENTATION.md` | ✅ This file | Slide plan and media punch list |
| `SPEAKER_NOTES.md` | ✅ Complete | Full speaker cues, timing, and Q&A prep |
| `PUNCHLIST.md` | ✅ Complete | Detailed creation instructions for each media asset |
| `SLIDES.md` | ⬜ To create | Marp-compatible markdown slide deck |

---

## Delivery Order (for presenter)

1. Open `SLIDES.md` in Marp/VS Code for slides
2. Have `SPEAKER_NOTES.md` open in split pane for cues
3. Queue up `mnestic-demo.mp4` for Slide 10
4. Have `embedding-viz.html` and `mnestic-architecture.html` ready to open in browser
5. GIFs (`agent-parallelization.gif`, `guardrails-in-action.gif`) embedded in slides or displayed separately
