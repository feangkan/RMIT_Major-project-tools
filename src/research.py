"""Supervisor alignment and research helpers."""

from __future__ import annotations

from typing import Any

from .config import load_yaml


def get_supervisors() -> list[dict[str, Any]]:
    data = load_yaml("supervisors.yaml")
    return data.get("supervisors", [])


def get_external_references() -> list[dict[str, Any]]:
    data = load_yaml("supervisors.yaml")
    return data.get("external_references", [])


def score_supervisor_fit(brief: dict[str, Any], supervisor: dict[str, Any]) -> dict[str, Any]:
    text = " ".join(
        [
            brief.get("topic", ""),
            brief.get("process", ""),
            brief.get("site", ""),
            " ".join(brief.get("keywords", [])),
            " ".join(brief.get("custom_keywords", [])),
        ]
    ).lower()

    expertise = supervisor.get("expertise", []) + supervisor.get("keywords", [])
    matches: list[str] = []
    for term in expertise:
        token = term.lower()
        if any(word in text for word in token.split() if len(word) > 3):
            matches.append(term)
        elif token in text:
            matches.append(term)

    interest_terms = [
        "swarm", "agent", "algorithm", "computational", "ai", "llm", "python",
        "prefab", "off-site", "offsite", "additive", "fabrication", "robotic",
        "form finding", "form-finding", "cost", "modular", "timber", "tectonic",
    ]
    for term in interest_terms:
        if term in text and term not in [m.lower() for m in matches]:
            for exp in expertise:
                if term in exp.lower():
                    matches.append(exp)
                    break

    score = min(100, 20 + len(set(matches)) * 12)
    if supervisor["id"] in brief.get("supervisors_shortlist", []):
        score = min(100, score + 15)

    return {
        "supervisor": supervisor,
        "score": score,
        "matches": list(dict.fromkeys(matches)),
        "notes": supervisor.get("alignment_notes", ""),
    }


def rank_supervisors(brief: dict[str, Any]) -> list[dict[str, Any]]:
    ranked = [score_supervisor_fit(brief, s) for s in get_supervisors()]
    return sorted(ranked, key=lambda x: x["score"], reverse=True)


def get_sites() -> list[dict[str, Any]]:
    data = load_yaml("sites_australia.yaml")
    return data.get("sites", {})


def get_research_study() -> dict[str, Any]:
    return load_yaml("research_study.yaml")
