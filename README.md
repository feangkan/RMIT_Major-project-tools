# RMIT Major Project Tools

Command center for the **RMIT Master of Architecture Major Project** capstone.

**Official framing (combined):**
- Independent capstone requiring a highly resolved design, design-practice research, a well-argued architectural position, and presentation before a panel of experts.
- At RMIT Architecture: an independent graduating project under your **nominated supervisor**, within a **group context** — an opportunity to demonstrate **new kinds of knowledge and ideas through architecture**.

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

## Obsidian — living second brain

The richest "second brain" content is **already markdown/PDF in this repo** (`docs/`,
`data/`, `portfolio/`) — you don't need a separate export step to see it in Obsidian.

### Setup (one-time)

1. **Clone this repo locally** (or pull it if already cloned) so the files exist on your
   own machine — Obsidian is a local app and can't read directly off GitHub.
   ```bash
   git clone https://github.com/feangkan/RMIT_Major-project-tools.git
   cd RMIT_Major-project-tools
   git checkout cursor/major-project-tools-c3d6
   ```
2. In Obsidian: **Open folder as vault** → select the repo's root folder.
3. Open **`docs/00-dashboard.md`** — this is your home page, linking to every proposal
   draft, narrative doc, portfolio PDF (with specific pages embedded inline), and
   reference data file.

### Staying in sync while we keep developing

Every time the agent updates a doc or data file in this conversation, it's committed
and pushed to the `cursor/major-project-tools-c3d6` branch. To pull the latest into
your local Obsidian vault:

```bash
git pull origin cursor/major-project-tools-c3d6
```

Obsidian will pick up the changes automatically (no need to re-open the vault) —
edited notes just refresh, and any new files appear in the file explorer.

### Optional: also use the app's structured export

**Stage B** in the Streamlit app additionally exports your `brief.json` form fields
(topic/process/site/keywords as filled in the app UI) into `vault/` as a supplementary
set of notes — useful if you're using the app's guided workflow, but not required to
get value from the vault above.

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
