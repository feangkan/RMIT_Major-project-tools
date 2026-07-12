# RMIT Major Project Tools

Command center for the **RMIT Master of Architecture Major Project** capstone — the independent research and design project requiring a highly resolved design, design-practice research, a unique architectural position, and presentation before a panel of experts at the Major Project Festival.

## Features

| Stage | Purpose |
|-------|---------|
| **A** | Discovery & proposal — research, supervisor fit, EOI/proposal email drafts |
| **B** | Knowledge capture — export Obsidian-compatible vault (2nd brain) |
| **C** | Production log — ongoing work, code, fabrication, blockers |
| **D** | Design development & fabrication pipeline |
| **E** | Critical position & documentation |
| **F** | Major Project Festival review prep |

Also includes:
- RMIT major project **requirements checklist** with completeness score
- **Supervisor alignment** (Roland Snooks, Nic Bao, Jan van Schaik + external refs)
- **Australian site** research notes (Design Hub, Fishermans Bend, etc.)
- Curated **reading list** and AI pioneers
- **EOI / proposal email** templates

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the URL shown in the terminal (default `http://localhost:8501`).

## Obsidian

Use **Stage B** in the app to export markdown files into `vault/`. In Obsidian:

1. Open folder as vault → select `vault/`
2. Or copy exported files into your existing 2nd brain

## Data files

- `data/supervisors.yaml` — RMIT supervisors and external references
- `data/sites_australia.yaml` — Australian site intelligence
- `data/research_study.yaml` — papers and AI pioneers
- `data/rmit_requirements.yaml` — M.Arch major project components

Your brief is saved locally in `brief.json` (gitignored).

## Your next steps

1. Run the app and fill **Stage A** (Topic, Process, Site, background).
2. Approve supplemental research packs on the Overview page.
3. Share your draft proposal when ready — paste into Stage A or production log.
4. Upload PDF portfolio / studio work when available.
