# Pages

Static HTML pages hosted via GitHub Pages.

## URL

<https://alanzoppa.github.io/pages/>

## Structure

Each page lives in its own subfolder:

```
pages/
├── index.html          # Directory listing
├── skinkedin/
│   └── index.html      # 🦎 SkinkedIn
├── your-new-page/
│   └── index.html      # Future page
└── template.html       # Copy this to start
```

## Adding New Pages

1. Create a new folder: `mkdir my-new-page`
2. Copy template: `cp template.html my-new-page/index.html`
3. Edit `my-new-page/index.html` with your content
4. Add a link in root `index.html`
5. Commit and push — GitHub Pages auto-deploys

## Current Pages

- `skinkedin/` — 🦎 SkinkedIn (LinkedIn for skinks)

## Local Testing

Open any HTML file directly in a browser:
```bash
open skinkedin/index.html
```

Or serve with a simple HTTP server:
```bash
python3 -m http.server 8000
```
Then visit `http://localhost:8000`
