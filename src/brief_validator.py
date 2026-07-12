"""Validate brief completeness against RMIT major project components."""

from __future__ import annotations

from typing import Any

from .config import load_yaml


def _filled(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return len(value) > 0
    if isinstance(value, dict):
        return any(_filled(v) for v in value.values())
    return bool(value)


def assess_brief(brief: dict[str, Any]) -> dict[str, Any]:
    reqs = load_yaml("rmit_requirements.yaml")
    components = reqs["required_components"]
    results: list[dict[str, Any]] = []

    field_map = {
        "topic_what": brief.get("topic"),
        "process_how": brief.get("process"),
        "site_where": brief.get("site"),
        "supervisor": brief.get("supervisors_shortlist"),
        "background": brief.get("background"),
        "keywords": brief.get("keywords") or brief.get("custom_keywords"),
        "critical_position": brief.get("revision_notes"),
        "design_practice_research": brief.get("research_notes") or brief.get("production_log"),
        "resolved_design": brief.get("process") or brief.get("production_log"),
        "new_knowledge": brief.get("topic") and brief.get("revision_notes"),
        "panel_review": brief.get("stage_status", {}).get("F") == "done",
        "group_context": brief.get("revision_notes"),
        "building_technology": brief.get("process"),
        "communication": brief.get("production_log"),
        "research_literature": brief.get("research_notes"),
        "pr_pathway": brief.get("revision_notes"),
    }

    for comp in components:
        cid = comp["id"]
        value = field_map.get(cid)
        complete = _filled(value)
        if cid == "background":
            complete = _filled(brief.get("background", {}).get("past_studios")) or _filled(
                brief.get("background", {}).get("work_experience")
            )
        results.append(
            {
                "id": cid,
                "label": comp["label"],
                "weight": comp["weight"],
                "complete": complete,
                "prompts": comp.get("prompts", []),
            }
        )

    critical = [r for r in results if r["weight"] == "critical"]
    critical_done = sum(1 for r in critical if r["complete"])
    total_done = sum(1 for r in results if r["complete"])
    score = round(100 * total_done / len(results)) if results else 0

    missing_critical = [r["label"] for r in critical if not r["complete"]]
    missing_all = [r["label"] for r in results if not r["complete"]]

    pillars = reqs.get("capstone_pillars", [])
    pillar_to_component = {
        "resolved_design": "resolved_design",
        "design_practice_research": "design_practice_research",
        "unique_position": "critical_position",
        "new_knowledge": "new_knowledge",
        "panel_presentation": "panel_review",
    }
    results_by_id = {r["id"]: r for r in results}
    pillar_status = []
    for pillar in pillars:
        comp_id = pillar_to_component.get(pillar["id"], "")
        linked = results_by_id.get(comp_id)
        pillar_status.append({
            "id": pillar["id"],
            "label": pillar["label"],
            "complete": linked["complete"] if linked else False,
            "description": pillar.get("description", "").strip(),
            "stages": pillar.get("maps_to_stages", []),
        })

    pillars_done = sum(1 for p in pillar_status if p["complete"])

    return {
        "score": score,
        "total": len(results),
        "completed": total_done,
        "critical_completed": critical_done,
        "critical_total": len(critical),
        "components": results,
        "missing_critical": missing_critical,
        "missing_all": missing_all,
        "capstone_pillars": pillar_status,
        "pillars_completed": pillars_done,
        "pillars_total": len(pillar_status),
        "ready_for_proposal": critical_done >= len(critical) - 1 and _filled(brief.get("topic")),
    }


def generate_clarifying_questions(brief: dict[str, Any], assessment: dict[str, Any]) -> list[str]:
    questions: list[str] = []
    if not _filled(brief.get("topic")):
        questions.append(
            "What is your core research question or architectural proposition (The What)?"
        )
    if not _filled(brief.get("process")):
        questions.append(
            "Which computational workflow will you use — swarm agents, Python, LLM-assisted "
            "design, parametric, or hybrid? Describe The How."
        )
    if not _filled(brief.get("site")):
        questions.append(
            "Where will the project be situated — RMIT Design Hub lab, urban site, "
            "industry partner, or speculative site in Australia?"
        )
    bg = brief.get("background", {})
    if not _filled(bg.get("past_studios")) and not _filled(bg.get("work_experience")):
        questions.append(
            "Please share past studio work and professional experience (PDFs welcome) "
            "so we can align your background with the proposal."
        )
    if not brief.get("supervisors_shortlist"):
        questions.append(
            "Which supervisor is your first preference — Roland Snooks, Nic Bao, or other?"
        )
    if assessment["score"] < 40:
        questions.append(
            "Do you have a draft proposal or EOI to share? You mentioned providing one later."
        )
    if not _filled(brief.get("research_notes")):
        questions.append(
            "Are there specific papers, precedents, or AI pioneers you already want to build on?"
        )
    return questions
