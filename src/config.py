"""Load YAML data and manage project brief state."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
BRIEF_PATH = ROOT / "brief.json"
VAULT_DIR = ROOT / "vault"


def load_yaml(name: str) -> dict[str, Any]:
    path = DATA_DIR / name
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_brief() -> dict[str, Any]:
    if BRIEF_PATH.exists():
        with BRIEF_PATH.open(encoding="utf-8") as f:
            return json.load(f)
    return default_brief()


def save_brief(brief: dict[str, Any]) -> None:
    brief["updated_at"] = datetime.now(timezone.utc).isoformat()
    with BRIEF_PATH.open("w", encoding="utf-8") as f:
        json.dump(brief, f, indent=2, ensure_ascii=False)


def default_brief() -> dict[str, Any]:
    reqs = load_yaml("rmit_requirements.yaml")
    return {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": None,
        "stage_status": {
            "A": "not_started",
            "B": "not_started",
            "C": "not_started",
            "D": "not_started",
            "E": "not_started",
            "F": "not_started",
        },
        "topic": "",
        "process": "",
        "site": "",
        "supervisors_shortlist": ["roland_snooks", "nic_bao"],
        "background": {
            "past_studios": "",
            "work_experience": "",
            "pdf_available": False,
        },
        "keywords": reqs.get("default_keywords", []),
        "custom_keywords": [],
        "research_notes": "",
        "revision_notes": "",
        "production_log": [],
        "pending_questions": [],
        "approved_supplements": [],
    }


STAGES = {
    "A": {
        "title": "Discovery & Proposal",
        "subtitle": "Research, EOI, supervisor email",
        "description": (
            "Find research aligned to your interests, map supervisors, draft "
            "Expression of Interest (EOI) or proposal email when information is limited."
        ),
    },
    "B": {
        "title": "Knowledge Capture",
        "subtitle": "Obsidian 2nd brain sync",
        "description": (
            "Collect papers, site notes, supervisor profiles, and brief components "
            "into an Obsidian-compatible vault for long-term reference."
        ),
    },
    "C": {
        "title": "Production Log",
        "subtitle": "Ongoing work & issue tracking",
        "description": (
            "Record design iterations, code experiments, fabrication tests, "
            "blockers, and decisions. Your assistant / dev / production team log."
        ),
    },
    "D": {
        "title": "Design Development & Fabrication",
        "subtitle": "Algorithm → prototype pipeline",
        "description": (
            "Track form-finding runs, pseudocode/Python/LLM workflows, "
            "cost estimates, prefab/AM strategies, and prototype milestones."
        ),
    },
    "E": {
        "title": "Critical Position & Documentation",
        "subtitle": "Argument, drawings, writing",
        "description": (
            "Develop your architectural position, exhibition materials, "
            "and written component for festival review."
        ),
    },
    "F": {
        "title": "Festival Review Prep",
        "subtitle": "WIP → final presentation",
        "description": (
            "Checklist for Major Project Festival: pin-up, prototype, "
            "narrative, panel questions, and deliverable completeness."
        ),
    },
}
