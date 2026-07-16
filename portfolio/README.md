# Drop your portfolio files here

**Folder path:** `/workspace/portfolio/`

## ⚠️ The "Browser" / "Desktop" tabs in the Cloud Agent PR panel are read-only

If you're viewing this via the **Changes / PR / Desktop / Browser** tabs in the Cursor Cloud Agent
sidebar, that file tree is a **review viewer**, not a live file system — dragging files onto it
will not upload anything (this is confirmed; drag-and-drop there does not work).

## What actually works

**Option A — Attach directly in the chat (most reliable):**
Compress your PDF first (see Size tip below), then attach it directly to a chat message here.
Attached chat files are readable by the agent directly — no folder drop needed.

**Option B — Export key pages as images and attach those:**
Export your strongest 5–10 boards as individual JPG/PNG pages (Preview/Acrobat → Export as Image)
and attach those images in chat. Usually smaller and faster than a full PDF, and the agent can
read images natively.

**Option C — If you have git installed on your own machine:**
Clone this branch (`cursor/major-project-tools-c3d6`), copy your PDFs into `portfolio/`, then:
```
git add -f portfolio/*.pdf
git commit -m "Add portfolio PDFs"
git push
```
(`-f` is required because `portfolio/*.pdf` is gitignored by default — see note in `.gitignore`.)

## Suggested file names

| Your studio | Rename to |
|-------------|-----------|
| Marc Gibson / hybrid tectonic / China AM | `01_gibson_hybrid_tectonic.pdf` |
| Alisa Andrasek / vibe code / swarm | `02_andrasek_swarm_ai.pdf` |
| Igor Pantic / coffee waste / HoloLens | `03_pantic_coffee_ar.pdf` |
| RA GFRC facade | `04_ra_gfrc_facade.pdf` |

Optional: also drop `code/` Python-for-Rhino scripts or experiment photos.

## After you drop files

Message me:
> Portfolio files are in `portfolio/` — please review.

## Size tip

Each file ~50MB may be slow. If upload fails, compress to ~15–20MB or upload 1–2 strongest PDFs first.
