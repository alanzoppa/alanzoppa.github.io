# Presentation Deliverables Punchlist

CDMX May 28, 2026 — "Writing Code Like an Architect: A Personal Experiment in Vibe Coding"

---

## Screen Recordings & GIFs

- [ ] **mnestic-demo.mp4** — 2-3 minute screen recording of Mnestic in action:
  - Open the Mnestic web UI showing the note cloud with >75% similarity clusters
  - Navigate between connected notes showing meaningful cluster groupings
  - Show an agent querying Mnestic via MCP (Hermes or OpenCode using `mcp_mnestic_*` tools)
  - Demonstrate cross-session memory: "Alan promised to send Ale an email, did he remember?"
  - Show Zoom transcript → Claude → Mnestic pipeline result

- [ ] **agent-parallelization.gif** — 30-60 second GIF showing OpenCode dispatching subagents:
  - Show the AGENTS.md decision matrix being followed
  - Show a complex task broken into subagent dispatches
  - Highlight the "MUST parallelize" guardrail in action

- [ ] **guardrails-in-action.gif** — 30-second GIF showing agent guardrails:
  - Agent auto-running tests before push
  - Agent committing + pushing after green tests
  - Agent respecting the "don't reinvent the wheel" rule (using a library instead of raw regex)

- [ ] **token-cost-demo.mp4** (optional) — 1-minute recording:
  - Ollama Pro dashboard showing token usage over a heavy week
  - OpenRouter billing showing embedding cost (~$0.01 for 1600 docs)
  - OpenCode Go subscription page

---

## Images & Diagrams

- [ ] **mnestic-architecture.html** — Architecture diagram (dark-themed SVG, self-contained HTML):
  - Notes sources (Zoom transcripts, manual notes, work logs)
  - Claude processing pipeline (transcript → styleguide → structured notes)
  - OpenViking/Mnestic ingestion (ChromaDB with qwen3-embedding-8b, 4096-dim)
  - MCP server frontend
  - Agent consumers (Hermes, OpenCode, Openclaw) querying via MCP
  - Similarity cloud visualization (notes clustered by cosine distance)

- [ ] **embedding-viz.html** — Embeddings explanation visual (dark-themed HTML):
  - Show the "uncle → aunt :: man → woman" relationship visually
  - 3D-reduced embedding space showing these four words
  - Cosine distance explanation with annotated arrows
  - Simple, clear, no math heavy — intuitive visual

- [ ] **model-decision-matrix.png** — Clean rendering of the model assignment table:
  - | Task Type | Subagent | Model | Why |
  - Styled as a dark-themed table or info card

- [ ] **guardrails-checklist.png** — The guardrails as a visual checklist:
  - MUST parallelize with subagents
  - Push after successful complex changes
  - Test new functionality
  - Always specify subagent type
  - Type safety preferred
  - Don't reinvent the wheel

- [ ] **tools-ecosystem.png** — Visual showing the tool ecosystem:
  - Ollama Pro (tokens), OpenCode (coding agent), Openclaw (personal assistant)
  - Hermes Agent (devops), agent-browser (web automation), OpenRouter (embeddings)
  - How they connect and what each is best for

- [ ] **interns-comparison.png** — The intern analogy visual:
  - Side-by-side: intern behaviors vs agent behaviors
  - "Picks ridiculous team name" ↔ "Solves with regex tangle"
  - "Stores gym clothes in office" ↔ "Commits secrets to git"
  - "Doesn't show up to meetings" ↔ "Doesn't run tests before push"

---

## Speaker Notes

- [ ] **SPEAKER_NOTES.md** — Comprehensive speaker notes covering ALL sections:
  - Introduction: the architect/vibe-coding framing
  - The three research questions
  - Tokens: cost breakdown and pricing landscape
  - Tools: OpenCode, Openclaw, Hermes Agent, agent-browser
  - Managing Interns: the story and connection to agents
  - Coding Agents as Interns: specific behavioral parallels
  - Guardrails: each guardrail with rationale
  - Code I Wouldn't Have Bothered to Write: Mnestic origin story
  - Embedding How-To: simplified, intuitive explanation
  - Mnestic Demo: cues, transition timings, what to highlight
  - Closing: open models, $20/month, results without slop

---

## Slides

- [ ] **SLIDES.md** — Marp-compatible markdown slide deck:
  - Title slide
  - The Three Questions
  - Token Economics (costs)
  - Tool Ecosystem
  - Managing Interns (story + photo)
  - Coding Agents as Interns
  - Guardrails
  - Mnestic Architecture
  - Embeddings Explained
  - Mnestic Demo (placeholder for live/recorded)
  - Closing: Code I Wouldn't Have Bothered to Write

---

## Files Present (for reference)

- `PRESENTATION.md` — Raw notes (source material)
- `interns.jpg` — Photo of the intern team (used in Managing Interns section)

---

## Delivery Order (for presenter)

1. Open `SLIDES.md` in Marp/VS Code for slides
2. Have `SPEAKER_NOTES.md` open in split pane for cues
3. Queue up `mnestic-demo.mp4` for the demo section
4. Have `embedding-viz.html` and `mnestic-architecture.html` ready to open in browser
5. GIFs (`agent-parallelization.gif`, `guardrails-in-action.gif`) for slides or separate display
