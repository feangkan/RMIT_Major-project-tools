"""Generate proposal emails, EOIs, and Obsidian vault exports."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .config import VAULT_DIR, load_yaml
from .research import get_supervisors, rank_supervisors


def _supervisor_by_id(sid: str) -> dict[str, Any] | None:
    for s in get_supervisors():
        if s["id"] == sid:
            return s
    return None


def generate_eoi_draft(brief: dict[str, Any]) -> str:
    ranked = rank_supervisors(brief)
    top = ranked[0]["supervisor"] if ranked else None
    sup_name = top["name"] if top else "[Supervisor Name]"
    keywords = ", ".join((brief.get("keywords") or [])[:8])

    return f"""Subject: Expression of Interest — Major Project (Computational Design / {brief.get('topic') or 'TBC'})

Dear {sup_name.split()[0] if top else 'Professor'},

I am writing to express my interest in undertaking my Master of Architecture Major Project under your supervision at RMIT.

**Provisional topic (The What)**
{brief.get('topic') or '[To be refined — please see attached background]'}

**Proposed approach (The How)**
{brief.get('process') or '[Computational / algorithmic workflow — swarm intelligence, Python, additive manufacturing, prefabrication — to be detailed]'}

**Site / context (The Where)**
{brief.get('site') or '[RMIT Design Hub / Australian industry context — to be confirmed]'}

**Why your supervision**
{ranked[0]['notes'].strip() if ranked else '[Alignment with your lab research to be articulated]'}

**Background**
- Past studios: {brief.get('background', {}).get('past_studios') or 'Available on request (portfolio PDF)'}
- Experience: {brief.get('background', {}).get('work_experience') or 'Available on request'}

**Keywords**
{keywords or 'computational design, algorithmic architecture, fabrication'}

I would welcome a short meeting to discuss whether this direction aligns with your current research and supervision capacity. I am happy to share portfolio work and a more developed brief following your feedback.

Kind regards,
[Your Name]
[Student ID]
[Your email]
"""


def generate_proposal_email(brief: dict[str, Any], supervisor_id: str) -> str:
    sup = _supervisor_by_id(supervisor_id)
    if not sup:
        return generate_eoi_draft(brief)

    ranked = rank_supervisors(brief)
    fit = next((r for r in ranked if r["supervisor"]["id"] == supervisor_id), None)
    matches = ", ".join(fit["matches"][:6]) if fit else ""

    return f"""Subject: Major Project Proposal — {brief.get('topic') or 'Computational Design Research'}

Dear {sup['name'].split()[0]},

Following our earlier correspondence / my EOI, I am submitting a developed Major Project proposal for your consideration as supervisor.

**1. Topic — The What**
{brief.get('topic') or '[Your architectural proposition]'}

**2. Process — The How**
{brief.get('process') or '[Methodology: algorithms, fabrication, documentation]'}

**3. Site — The Where**
{brief.get('site') or '[Site rationale]'}

**4. Alignment with {sup['lab']}**
Your research in {matches or 'computational design and fabrication'} directly informs this project. I aim to extend this through [specific contribution].

**5. Background**
Past studios: {brief.get('background', {}).get('past_studios') or 'See portfolio'}
Professional experience: {brief.get('background', {}).get('work_experience') or 'See CV'}

**6. Deliverables (preview)**
- Computational design pipeline (Python / agent-based / LLM-assisted as appropriate)
- Physical prototype(s) at [scale]
- Critical written component and festival presentation

**7. Research references**
{brief.get('research_notes') or '[Key papers — see reading list]'}

I would appreciate your feedback on scope, feasibility, and any adjustments needed before semester confirmation.

Kind regards,
[Your Name]
"""


def export_obsidian_vault(brief: dict[str, Any]) -> Path:
    """Export brief + reference data as Obsidian-compatible markdown vault."""
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Dashboard
    (VAULT_DIR / "00 Dashboard.md").write_text(
        f"""# RMIT Major Project — Obsidian Vault

> Exported: {now}

## Stages
- [[Stage A - Discovery]]
- [[Stage B - Knowledge]]
- [[Stage C - Production Log]]
- [[Stage D - Fabrication]]
- [[Stage E - Critical Position]]
- [[Stage F - Festival Prep]]

## Core brief
- [[Topic - The What]]
- [[Process - The How]]
- [[Site - The Where]]
- [[Supervisors]]
- [[Keywords]]
- [[Research Study List]]
- [[RMIT Requirements Checklist]]

## Tags
#rmit #major-project #computational-design
""",
        encoding="utf-8",
    )

    (VAULT_DIR / "Topic - The What.md").write_text(
        f"# Topic — The What\n\n{brief.get('topic') or '_Not yet defined_'}\n",
        encoding="utf-8",
    )
    (VAULT_DIR / "Process - The How.md").write_text(
        f"# Process — The How\n\n{brief.get('process') or '_Not yet defined_'}\n",
        encoding="utf-8",
    )
    (VAULT_DIR / "Site - The Where.md").write_text(
        f"# Site — The Where\n\n{brief.get('site') or '_Not yet defined_'}\n",
        encoding="utf-8",
    )

    # Supervisors
    sup_lines = ["# Supervisors\n"]
    for s in get_supervisors():
        sup_lines.append(f"## {s['name']}\n")
        sup_lines.append(f"- Lab: {s.get('lab', 'N/A')}\n")
        sup_lines.append(f"- Email: {s.get('email', '')}\n")
        sup_lines.append(f"- Expertise: {', '.join(s.get('expertise', []))}\n")
        sup_lines.append(f"- Notes: {s.get('alignment_notes', '')}\n\n")
    (VAULT_DIR / "Supervisors.md").write_text("".join(sup_lines), encoding="utf-8")

    # Keywords
    kws = brief.get("keywords", []) + brief.get("custom_keywords", [])
    (VAULT_DIR / "Keywords.md").write_text(
        "# Keywords\n\n" + "\n".join(f"- {k}" for k in kws) + "\n",
        encoding="utf-8",
    )

    # Research list
    study = load_yaml("research_study.yaml")
    rs_lines = ["# Research Study List\n"]
    for cat, items in study.get("categories", {}).items():
        rs_lines.append(f"\n## {cat.replace('_', ' ').title()}\n")
        for item in items:
            rs_lines.append(f"- **{item.get('author', item.get('name', 'Unknown'))}** — {item.get('title', '')} ({item.get('year', '')})\n")
    rs_lines.append("\n## AI Pioneers\n")
    for p in study.get("ai_pioneers", []):
        rs_lines.append(f"- **{p['name']}**: {p['contribution']}\n")
    (VAULT_DIR / "Research Study List.md").write_text("".join(rs_lines), encoding="utf-8")

    # Requirements
    reqs = load_yaml("rmit_requirements.yaml")
    req_lines = ["# RMIT Requirements Checklist\n\n"]
    req_lines.append(f"> {reqs.get('official_definition', '').strip()}\n\n")
    req_lines.append(f"> {reqs.get('program_context', '').strip()}\n\n")
    sup = reqs.get("supervision_model", {})
    if sup:
        req_lines.append("## Supervision model\n\n")
        req_lines.append(f"- **Nominated supervisor:** required\n")
        req_lines.append(f"- **Group context:** {sup.get('group_context', '').strip()}\n\n")
    req_lines.append("## Capstone pillars\n\n")
    for pillar in reqs.get("capstone_pillars", []):
        req_lines.append(f"- [ ] **{pillar['label']}** — {pillar.get('description', '').strip()}\n")
    req_lines.append("\n## Detailed components\n\n")
    for comp in reqs.get("required_components", []):
        req_lines.append(f"- [ ] **{comp['label']}** — {comp['description']}\n")
    (VAULT_DIR / "RMIT Requirements Checklist.md").write_text("".join(req_lines), encoding="utf-8")

    # Production log
    log_lines = ["# Stage C - Production Log\n\n"]
    for entry in brief.get("production_log", []):
        log_lines.append(f"## {entry.get('date', '')} — {entry.get('title', 'Entry')}\n")
        log_lines.append(f"{entry.get('body', '')}\n\n")
    (VAULT_DIR / "Stage C - Production Log.md").write_text("".join(log_lines), encoding="utf-8")

    # Stage stubs
    for name, fname in [
        ("Discovery", "Stage A - Discovery.md"),
        ("Knowledge", "Stage B - Knowledge.md"),
        ("Fabrication", "Stage D - Fabrication.md"),
        ("Critical Position", "Stage E - Critical Position.md"),
        ("Festival Prep", "Stage F - Festival Prep.md"),
    ]:
        (VAULT_DIR / fname).write_text(f"# Stage — {name}\n\n_See dashboard._\n", encoding="utf-8")

    return VAULT_DIR
