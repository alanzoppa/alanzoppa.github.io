# Presentation Deliverables — Status

CDMX May 28, 2026 — "Architect Vibes."

---

## ✅ Complete

### Slide Deck
- [x] `index.html` — Self-contained 10-slide HTML deck with keyboard nav, progress bar, fullscreen

### Media Assets
- [x] `headshot-8bit.png` — 8-bit pixel art headshot (slide 1)
- [x] `interns.jpg` — Intern team photo (slide 3)
- [x] `tools-ecosystem.png` — Tool ecosystem diagram (slide 5)
- [x] `word_vectors_3d.html` — Standalone 3D word vectors (slide 8)

### Embedded / Inline
- [x] Plotly 3D scatter — PCA/UMAP toggle with inline word-vector data (slide 8)
- [x] YouTube embed `XCLMAZbMCr4` — Mnestic demo screen recording (slide 9)
- [x] `interns-comparison.png` — Included in directory as backup visual

### Docs
- [x] `SPEAKER_NOTES.md` — Full speaker cues, timing (~22-24 min), Q&A prep
- [x] `PRESENTATION.md` — Slide plan with media references

---

## Changed from Original Plan

The original `PRESENTATION.md` / `PUNCHLIST.md` described a Marp-based slide deck with separate media files. The final deliverable is a self-contained `index.html` that embeds everything inline (Plotly data, YouTube, styles). No Marp, no separate `SLIDES.md`.

Original Plan                     Final
--------------------------------  -------------------------------------------
Marp SLIDES.md                    Self-contained index.html
mnestic-demo.mp4                  YouTube embed
mnestic-architecture.html         Removed (no architecture slide)
embedding-viz.html                Inline Plotly in index.html
guardrails-checklist.png          Replaced by thinking/rule pairs (slide 7)
model-decision-matrix.png         Removed (covered in speaker notes)
agent-parallelization.gif         Not needed
guardrails-in-action.gif          Not needed
token-cost-demo.mp4               Not needed (simple table on slide 6)
12 slides                         10 slides

### Structural Changes
- OpenClaw added back to tool ecosystem
- Guardrails reframed as "agent thinking vs. rule" pairs
- del Toro bookends (opening + closing quotes)
- "Won't tell you you're wrong" added to agents-as-interns
- Architecture slide removed — Mnestic explained verbally over demo video
- No separate architecture diagram — demo video shows the UI
