"""RMIT Major Project Tools — Streamlit application."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.brief_validator import assess_brief, generate_clarifying_questions
from src.config import STAGES, load_brief, save_brief
from src.research import (
    get_external_references,
    get_research_study,
    get_sites,
    get_supervisors,
    rank_supervisors,
)
from src.templates import export_obsidian_vault, generate_eoi_draft, generate_proposal_email

st.set_page_config(
    page_title="RMIT Major Project Tools",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .stage-card { padding: 1rem; border-radius: 8px; border: 1px solid #333; margin-bottom: 0.5rem; }
  .metric-ok { color: #2ecc71; }
    </style>
    """,
    unsafe_allow_html=True,
)


def init_state() -> None:
    if "brief" not in st.session_state:
        st.session_state.brief = load_brief()


def sidebar() -> str:
    st.sidebar.title("🏛️ Major Project Tools")
    st.sidebar.caption("RMIT M.Arch · Computational Design")
    stage = st.sidebar.radio(
        "Workflow stage",
        options=["overview"] + list(STAGES.keys()),
        format_func=lambda k: (
            "Overview — Command Center"
            if k == "overview"
            else f"Stage {k}: {STAGES[k]['title']}"
        ),
    )
    st.sidebar.divider()
    assessment = assess_brief(st.session_state.brief)
    st.sidebar.metric("Brief completeness", f"{assessment['score']}%")
    st.sidebar.caption(
        f"{assessment['completed']}/{assessment['total']} components · "
        f"{assessment['critical_completed']}/{assessment['critical_total']} critical"
    )
    return stage


def page_overview() -> None:
    st.title("RMIT Major Project Command Center")

    from src.config import load_yaml

    reqs = load_yaml("rmit_requirements.yaml")
    st.info(reqs.get("official_definition", "").strip())
    st.caption(reqs.get("program_context", "").strip())

    supervision = reqs.get("supervision_model", {})
    if supervision:
        st.markdown(
            f"**Supervision:** Individual project under your **nominated supervisor**, "
            f"within a **group context** (Major Project cohort). "
            f"{supervision.get('group_context', '').strip()}"
        )

    st.subheader("Capstone requirements")
    pcols = st.columns(3)
    assessment = assess_brief(st.session_state.brief)
    for i, pillar in enumerate(assessment.get("capstone_pillars", [])):
        with pcols[i % 3]:
            icon = "✅" if pillar["complete"] else "⬜"
            st.markdown(f"**{icon} {pillar['label']}**")
            st.caption(pillar["description"][:120] + "…" if len(pillar["description"]) > 120 else pillar["description"])
            if pillar.get("stages"):
                st.caption(f"Stages: {', '.join(pillar['stages'])}")

    st.markdown(
        """
        Your assistant for **computational design**, **algorithms**, **AI/LLM**, **swarm intelligence**,
        **form finding**, **prefabrication**, **off-site construction**, **additive manufacturing**,
        and **cost control** — structured for the RMIT Master of Architecture Major Project.
        """
    )

    cols = st.columns(len(STAGES))
    brief = st.session_state.brief
    for i, (key, meta) in enumerate(STAGES.items()):
        status = brief["stage_status"].get(key, "not_started")
        icon = {"not_started": "⬜", "in_progress": "🟡", "done": "✅"}.get(status, "⬜")
        with cols[i]:
            st.markdown(f"### {icon} {key}")
            st.caption(meta["title"])

    st.divider()
    if assessment["ready_for_proposal"]:
        st.success("Brief has enough core content to draft a proposal email.")
    else:
        st.warning(
            "Brief needs more information before a full proposal. "
            "Use Stage A and the questions below."
        )

    questions = generate_clarifying_questions(brief, assessment)
    if questions:
        st.subheader("Information needed from you")
        for q in questions:
            st.markdown(f"- {q}")

    st.subheader("Approve additional research packs")
    packs = [
        ("pack_supervisors", "Extended supervisor comparison matrix"),
        ("pack_sites", "Australian site deep-dive (Melbourne + national)"),
        ("pack_papers", "Full annotated bibliography (30+ papers)"),
        ("pack_pr", "Australia PR / industry trend brief (prefab, AM, digital construction)"),
        ("pack_python", "Python + swarm starter code templates for form-finding"),
    ]
    approved = brief.get("approved_supplements", [])
    for pid, label in packs:
        checked = st.checkbox(label, value=pid in approved, key=f"appr_{pid}")
        if checked and pid not in approved:
            approved.append(pid)
        elif not checked and pid in approved:
            approved.remove(pid)
    brief["approved_supplements"] = approved
    save_brief(brief)


def page_stage_a() -> None:
    st.header("Stage A — Discovery & Proposal")
    st.caption(STAGES["A"]["description"])
    brief = st.session_state.brief

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Brief core", "Supervisors", "Sites (AU)", "Research study", "Email / EOI"]
    )

    with tab1:
        brief["topic"] = st.text_area("Topic — The What", brief.get("topic", ""), height=100)
        brief["process"] = st.text_area("Process — The How", brief.get("process", ""), height=100)
        brief["site"] = st.text_area("Site — The Where", brief.get("site", ""), height=80)
        c1, c2 = st.columns(2)
        with c1:
            brief["background"]["past_studios"] = st.text_area(
                "Past studios", brief["background"].get("past_studios", ""), height=80
            )
        with c2:
            brief["background"]["work_experience"] = st.text_area(
                "Work experience", brief["background"].get("work_experience", ""), height=80
            )
        brief["research_notes"] = st.text_area(
            "Research notes / papers you already know", brief.get("research_notes", ""), height=80
        )
        brief["revision_notes"] = st.text_area(
            "Revision loops / critical position notes", brief.get("revision_notes", ""), height=80
        )

    with tab2:
        st.subheader("Supervisor fit analysis")
        ranked = rank_supervisors(brief)
        options = {s["id"]: s["name"] for s in get_supervisors()}
        brief["supervisors_shortlist"] = st.multiselect(
            "Your supervisor shortlist",
            options=list(options.keys()),
            default=brief.get("supervisors_shortlist", []),
            format_func=lambda x: options[x],
        )
        for r in ranked:
            with st.expander(f"{r['supervisor']['name']} — fit {r['score']}%"):
                st.write(r["supervisor"].get("lab", ""))
                st.write("**Matches:**", ", ".join(r["matches"]) or "Add topic/process text to improve matching")
                st.info(r["notes"])
                for pub in r["supervisor"].get("key_publications", []):
                    st.markdown(f"- {pub.get('title')} ({pub.get('year', '')})")

        st.subheader("External references (SCI-Arc, ETH, UCL, etc.)")
        for ref in get_external_references():
            st.markdown(f"- **{ref['name']}** ({ref['institution']}): {ref['relevance']}")

    with tab3:
        sites = get_sites()
        for sid, site in sites.items():
            strength = site.get("strength", "")
            badge = "🟢" if strength == "primary" else "🟡" if strength == "high" else "⚪"
            with st.expander(f"{badge} {site['name']} — {site['location']}"):
                st.write(site.get("why", ""))
                if site.get("labs"):
                    st.write("**Labs:**", ", ".join(site["labs"]))
                st.caption(", ".join(site.get("keywords", [])))

    with tab4:
        study = get_research_study()
        for cat, items in study.get("categories", {}).items():
            st.markdown(f"### {cat.replace('_', ' ').title()}")
            for item in items:
                pri = item.get("priority", "")
                st.markdown(
                    f"- [{pri}] **{item.get('author', '')}** — *{item.get('title', '')}* "
                    f"({item.get('year', '')}) {item.get('note', '')}"
                )
        st.markdown("### AI Pioneers")
        for p in study.get("ai_pioneers", []):
            st.markdown(f"- **{p['name']}**: {p['contribution']}")

    with tab5:
        email_type = st.radio("Draft type", ["EOI (limited info)", "Full proposal email"])
        sup_id = st.selectbox(
            "Target supervisor",
            options=[s["id"] for s in get_supervisors()],
            format_func=lambda x: next(s["name"] for s in get_supervisors() if s["id"] == x),
        )
        if email_type.startswith("EOI"):
            draft = generate_eoi_draft(brief)
        else:
            draft = generate_proposal_email(brief, sup_id)
        st.text_area("Draft (edit before sending)", draft, height=420)
        st.caption("Replace [Your Name], attach portfolio PDFs when ready.")

    status = st.selectbox(
        "Stage A status",
        ["not_started", "in_progress", "done"],
        index=["not_started", "in_progress", "done"].index(brief["stage_status"].get("A", "not_started")),
    )
    brief["stage_status"]["A"] = status
    save_brief(brief)
    st.success("Brief saved.")


def page_stage_b() -> None:
    st.header("Stage B — Knowledge Capture (Obsidian)")
    st.caption(STAGES["B"]["description"])
    brief = st.session_state.brief

    st.markdown(
        """
        Export your brief, supervisors, research list, and logs into an **Obsidian-compatible vault**.
        Point Obsidian at the `vault/` folder or copy it into your existing 2nd brain.
        """
    )
    if st.button("Export / refresh Obsidian vault", type="primary"):
        path = export_obsidian_vault(brief)
        st.success(f"Vault exported to `{path}`")
        for md in sorted(path.glob("*.md")):
            st.markdown(f"- `{md.name}`")

    brief["stage_status"]["B"] = st.selectbox(
        "Stage B status",
        ["not_started", "in_progress", "done"],
        index=["not_started", "in_progress", "done"].index(brief["stage_status"].get("B", "not_started")),
    )
    save_brief(brief)


def page_stage_c() -> None:
    st.header("Stage C — Production Log")
    st.caption(STAGES["C"]["description"])
    brief = st.session_state.brief

    with st.form("log_entry"):
        title = st.text_input("Entry title")
        body = st.text_area("What happened / issue / decision / code note", height=120)
        category = st.selectbox(
            "Category",
            ["design", "code", "fabrication", "research", "supervision", "blocker", "resolved"],
        )
        if st.form_submit_button("Add log entry"):
            brief.setdefault("production_log", []).insert(
                0,
                {
                    "date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
                    "title": title,
                    "body": body,
                    "category": category,
                },
            )
            save_brief(brief)
            st.rerun()

    for entry in brief.get("production_log", []):
        with st.expander(f"{entry.get('date')} · [{entry.get('category')}] {entry.get('title')}"):
            st.write(entry.get("body", ""))

    brief["stage_status"]["C"] = st.selectbox(
        "Stage C status",
        ["not_started", "in_progress", "done"],
        index=["not_started", "in_progress", "done"].index(brief["stage_status"].get("C", "not_started")),
    )
    save_brief(brief)


def page_stage_d() -> None:
    st.header("Stage D — Design Development & Fabrication")
    st.caption(STAGES["D"]["description"])
    st.markdown(
        """
        Track your pipeline from **algorithm → geometry → fabrication → cost**.

        | Track | Examples |
        |-------|----------|
        | Form finding | Swarm agents, Kangaroo, topology optimisation |
        | Code | Python, pseudocode, LLM-assisted scripts |
        | Fabrication | Robotic AM, modular prefab, off-site assembly |
        | Cost | DfMA, unit counts, material waste, labour |
        """
    )
    brief = st.session_state.brief
    brief["stage_status"]["D"] = st.selectbox(
        "Stage D status",
        ["not_started", "in_progress", "done"],
        index=["not_started", "in_progress", "done"].index(brief["stage_status"].get("D", "not_started")),
    )
    save_brief(brief)


def page_stage_e() -> None:
    st.header("Stage E — Critical Position & Documentation")
    st.caption(STAGES["E"]["description"])
    brief = st.session_state.brief

    st.markdown("### Revision hierarchy (loops)")
    from src.config import load_yaml

    for item in load_yaml("rmit_requirements.yaml").get("revision_hierarchy", []):
        st.markdown(f"**{item['order']}. {item['lens']}** — {item['question']}")

    brief["stage_status"]["E"] = st.selectbox(
        "Stage E status",
        ["not_started", "in_progress", "done"],
        index=["not_started", "in_progress", "done"].index(brief["stage_status"].get("E", "not_started")),
    )
    save_brief(brief)


def page_stage_f() -> None:
    st.header("Stage F — Festival Review Prep")
    st.caption(STAGES["F"]["description"])
    brief = st.session_state.brief
    assessment = assess_brief(brief)

    checklist = [
        "Pin-up / exhibition layout planned",
        "Physical or digital prototype ready",
        "Critical narrative (spoken + written)",
        "Supervisor WIP feedback incorporated",
        "Building technology resolved",
        "Process documentation (code / algorithm logs)",
        "Panel Q&A anticipated",
    ]
    for item in checklist:
        st.checkbox(item)

    st.metric("Brief completeness for festival", f"{assessment['score']}%")
    if assessment["missing_critical"]:
        st.warning("Still missing critical: " + ", ".join(assessment["missing_critical"]))

    brief["stage_status"]["F"] = st.selectbox(
        "Stage F status",
        ["not_started", "in_progress", "done"],
        index=["not_started", "in_progress", "done"].index(brief["stage_status"].get("F", "not_started")),
    )
    save_brief(brief)


def page_checklist() -> None:
    st.header("RMIT Major Project — Requirements Checklist")
    from src.config import load_yaml

    brief = st.session_state.brief
    assessment = assess_brief(brief)
    reqs = load_yaml("rmit_requirements.yaml")

    st.info(reqs.get("official_definition", "").strip())

    st.subheader("Capstone pillars")
    for pillar in assessment.get("capstone_pillars", []):
        icon = "✅" if pillar["complete"] else "⬜"
        st.markdown(f"{icon} **{pillar['label']}** — Stages {', '.join(pillar.get('stages', []))}")

    st.divider()
    st.subheader("Detailed components")
    st.progress(assessment["score"] / 100)
    for comp in assessment["components"]:
        icon = "✅" if comp["complete"] else "⬜"
        weight = comp["weight"]
        with st.expander(f"{icon} {comp['label']} ({weight})"):
            for p in comp["prompts"]:
                st.markdown(f"- {p}")


def page_ideas() -> None:
    st.header("Idea evaluation — honest assessment")
    from src.config import load_yaml

    data = load_yaml("ideas_evaluation.yaml")
    merged = data.get("merged_thesis", {})

    st.success(f"**Recommended:** {merged.get('title', '')}")
    st.caption(merged.get("subtitle", ""))
    st.markdown(
        f"**Primary supervisor:** {merged.get('primary_supervisor', '')} · "
        f"**Urban framing:** {merged.get('urban_framing', '')}"
    )

    for idea in data.get("ideas", []):
        verdict = idea.get("verdict", "")
        icon = {"pursue": "✅", "merge_into_d": "🔀", "pivot": "⚠️", "drop": "❌"}.get(verdict, "⬜")
        with st.expander(f"{icon} {idea['title']} — {verdict.upper()}"):
            c1, c2, c3 = st.columns(3)
            c1.metric("15wk feasibility", f"{idea.get('feasibility_15wk', '—')}/10")
            c2.metric("AU / PR", f"{idea.get('pr_australia', '—')}/10")
            c3.metric("Nic Bao fit", f"{idea.get('nic_bao_fit', '—')}/10")
            st.write(idea.get("note", ""))

    st.subheader("What Roland Snooks will likely say yes to")
    for item in data.get("what_roland_will_say_yes_to", []):
        st.markdown(f"- {item}")
    st.subheader("What Roland will likely push back on")
    for item in data.get("what_roland_will_likely_push_back_on", []):
        st.markdown(f"- {item}")

    proposal_path = ROOT / "docs" / "proposal-waste-to-pavilion.md"
    if proposal_path.exists():
        st.subheader("Draft proposal (Idea D — merged)")
        st.markdown(proposal_path.read_text(encoding="utf-8"))

    schedule = load_yaml("semester_schedule.yaml")
    st.subheader("15-week schedule")
    for phase in schedule.get("phases", []):
        with st.expander(f"Weeks {phase['weeks']}: {phase['title']}"):
            for t in phase.get("tasks", []):
                st.markdown(f"- {t}")


PAGES = {
    "overview": page_overview,
    "A": page_stage_a,
    "B": page_stage_b,
    "C": page_stage_c,
    "D": page_stage_d,
    "E": page_stage_e,
    "F": page_stage_f,
}


def main() -> None:
    init_state()
    stage = sidebar()
    if stage == "overview":
        page_overview()
    else:
        PAGES[stage]()
    st.sidebar.divider()
    if st.sidebar.button("Requirements checklist"):
        page_checklist()


if __name__ == "__main__":
    main()
