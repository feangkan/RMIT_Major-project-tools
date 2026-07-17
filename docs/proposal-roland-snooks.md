← [[00-dashboard|Back to Dashboard]]

# Major Project Proposal — Roland Snooks (Primary)

**Student:** Kankawee Maksomboon (Frank) · s4097770
**Program:** Master of Architecture, RMIT University
**Course:** Major Project (capstone)
**Proposed supervisor:** Professor Roland Snooks — Tectonic Formation Lab
**Secondary preference / consultation:** Dr Dingwen (Nic) Bao — FormX *(if metal/composite material performance needs consultation)*
**Date:** [Date]

---

## 1. Title

**Behavioral Metal: Multi-Agent Growth Formation for Intricate Off-Cut Metal Tectonics**

*Extending behavioral tectonics and agentBody research into recycled/off-cut metal streams — testing whether additive manufacturing's capacity for unique, non-repeating geometry lets swarm-generated intricacy survive to a physical prototype, at Fishermans Bend.*

---

## 1b. Position statement (read this first)

This project is **not** about discrete, standardized, repeatable parts (Retsin/Claypool/AUAR lineage). It takes the **opposite position**, consistent with Kokkugia/Snooks' own argument: swarm-generated form resists hierarchical, discrete articulation — the value of computation here is **intricate, non-repetitive detail emerging from local agent behavior**, not a kit of interchangeable modules.

**Why additive manufacturing specifically:** unlike CNC-cut or cast repeatable parts — where tooling/formwork cost is amortized by making every part identical — 3D printing lets every agent-generated joint, node, or fragment be **geometrically unique at no added fabrication cost**. This is the precise mechanism by which AM lets Behavioral Formation's intricacy survive from algorithm to physical object, instead of being discretized away into a repeatable kit.

---

## 2. Project summary (150 words)

This Major Project tests whether a **self-organizing multi-agent growth process** — building on my own prior space-colonization/differential-growth studio work — can generate **intricate, non-repetitive architectural detail** that survives translation into a physical prototype through **additive manufacturing** and **cold-cast metal**, rather than being resolved into standardized, repeatable components.

The material stream is **recycled/off-cut metal** — referencing Fishermans Bend's identity as a former heavy-manufacturing precinct now undergoing urban renewal. Two fabrication tracks: (1) **metal-filled filament** (bronze/copper composite) printed at joint/node/connector scale on desktop FDM, testing intricate emergent detail at 1:1 resolution; (2) **cold-cast bronze/aluminium** composite for larger envelope fragments, extending my existing silicone/plaster mould-casting workflow.

Building on Roland Snooks' *Behavioral Tectonics* and *agentBody* research, Robert Stuart-Smith's *Behavioural Production*, and my own **"Social Hideout"** multi-agent/LLM-MCP studio pipeline, this project positions Fishermans Bend's material history as the generative logic for its next architectural identity.

---

## 3. Research questions

1. **Behavioral formation:** How does a self-organizing multi-agent growth system (cellular division / differential growth logic — local rules producing emergent global order, not top-down authored form) encode off-cut metal material constraints as agent parameters, rather than applying material choice after form is fixed?
2. **Tectonics:** Can additive manufacturing preserve **intricate, non-repetitive** agent-generated detail at joint/node scale, avoiding the discretization-into-repeatable-parts route taken by Pantic/Klemmt and Retsin/Claypool?
3. **Material behavior:** How do recycled/off-cut metal constraints (via cold-cast bronze/aluminium and metal-filled AM) behave as agent-readable parameters — weight, flow, joint tolerance — rather than a fixed material applied after formation?
4. **Fabrication:** What is the realistic design-to-fabrication workflow using desktop AM (Bambu Lab, 256mm build volume) + manual cold-casting, given no access to industrial robotic AM for this project specifically?
5. **Site:** How does Fishermans Bend's identity as a former/active metal-manufacturing precinct inform the agent system's material-sourcing logic and the architectural proposal's civic role?

---

## 4. Architectural position

**Thesis:** Off-cut and recycled metal in a manufacturing-transition precinct is not scrap to be hidden — it is the **latent material memory of the site**. A self-organizing multi-agent growth process (cellular division / differential growth) negotiates this material's real behavior — weight, flow when cast, joint tolerance when printed — to produce **intricate, non-repetitive tectonic detail**, where computation and small-scale AM/casting **assist** craft rather than replace it.

**Growth and self-organization are the same claim, not two separate ones:** "growth" here does not mean a biological metaphor applied to form — it means the tectonic order of the piece emerges from **local cell-division/interaction rules**, with no centralized or pre-drawn global form imposed from above. This is the same theoretical move Camazine's *Self-Organization in Biological Systems* makes for slime mold and ant trails, that Snooks makes explicit in Behavioral Formation ("self-organisation and emergence" within multi-agent populations), and that Andrasek states directly for her own growth work — *Endemic Interstices* is described as a system with "the capacity to **self structure, adapt and co-evolve**" within its environment. Cellular division is simply the specific growth rule; self-organization is the principle that makes it architecturally meaningful — local rules, global emergent tectonic order, no top-down authored form.

**Against:** Discrete standardized kits-of-parts as the default "buildable" answer to complex computational form; sustainability-as-checkbox; bio-composite material claims that don't hold up under load (see Section 8, material evidence).

**For:** Design-practice research where a site's own industrial material history becomes the generative logic — and the constraint — for a new civic architecture.

**Direct precedent and the gap it leaves open:** Kokkugia's **Brass Swarm** (2015) encoded empirically-tested rod-bending limits directly into the agentBody algorithm, producing an automated generation-to-fabrication workflow in robotically-bent brass rod; the **RMIT Mace** (2015) used ~1 million agents self-organising into an intricate lattice, fabricated by direct titanium SLM printing, with the algorithm tuned to the AM process itself. Both use **uniform, regular stock** — standard rod, standard powder. Neither encodes **irregular, reclaimed, or off-cut material geometry** as an agent constraint. This project asks the same agentBody logic to negotiate non-standard stock instead of uniform material — a specific, citable extension of Kokkugia's own lineage, not a new method invented from nothing.

**Lineage:** Andrasek (multi-agent/LLM studio pipeline) → Gibson/Wark (hybrid tectonics, discrete-element chunk logic) → Snooks/Kokkugia (agentBody, Manifold Swarm, Brass Swarm, RMIT Mace) → **off-cut metal agentBody prototypes at Fishermans Bend**.

---

## 5. Site — The Where

**Site type:** Fishermans Bend Innovation District, Melbourne — Australia's largest urban renewal precinct, built on former heavy-manufacturing and metal-fabrication land, currently transitioning alongside active advanced-manufacturing industry.

**Why this site (not yet a fixed address):** it grounds the "recycled/off-cut metal" material logic in an actual, still-active supply chain rather than an abstract sustainability claim, stays logistically inside Melbourne for repeat site visits/QGIS mapping/DSLR photography, and lets the "abandoned/resource-rich, labour-scarce" research interest live as **contextual framing** (citing precedents such as regional manufacturing-decline towns) without requiring travel to a remote site within the 15-week window.

**Fabrication & research site:** RMIT Design Hub — Tectonic Formation Lab for review/consultation access; personal fabrication via desktop FDM (Bambu Lab) and manual cold-casting, since industrial robotic AM access is not available for this project.

*A specific building footprint/address within Fishermans Bend will be confirmed once the material-sourcing research (Section 8) narrows to a specific fabricator/scrap stream partner.*

---

## 6. Process — The How

| Layer | Method |
|-------|--------|
| **Multi-agent formation** | Python / vibe-coded agent systems, extending my "Social Hideout" pipeline — **cellular division / differential growth as primary logic** (converging support from Andrasek's *Alien Within Familiar*/*Wrinkle in Space* and Pantic's *Discrete Cellular Growth* research); space-colonization, slime-mold aggregation, and Voronoi partitioning as literature context and possible secondary rules. Formation logic also draws on Kokkugia's **agentBody** (bodies that connect to neighbouring bodies, ant-bridge logic) and **Manifold Swarm** (orientation-coordinate self-organisation into continuous surface topology) strategies |
| **Generative AI assist** | **Claude** (briefs, specs, pseudocode) + **Cursor vibe code** → **Python for Rhino/Grasshopper**, extending the MCP-tool-fed LLM-agent loop already built in Social Hideout (text prompts + image references + MCP tools → LLM → script iteration → screenshot feedback) |
| **Real-world data input** | Site/context data (EPW climate data precedent from Social Hideout; extended here to material-availability data — off-cut stock dimensions, scrap-yard inventory logic — as agent parameters) |
| **Material behavior** | Cold-cast bronze/aluminium powder + resin (extending my Pantic-studio silicone/plaster mould workflow); metal-filled bronze/copper FDM filament on Bambu Lab (hardened nozzle already fitted) |
| **Fabrication** | Two-track: (1) intricate joints/nodes at 1:1 via desktop AM; (2) larger rough-cast envelope fragments via manual cold-casting — no industrial robotic AM for this project |
| **AR (optional)** | HoloLens/Fologram-guided mould carving and casting alignment — direct precedent from Pantic studio, redirected to metal composite casting |
| **Resolution** | Rhino work sessions; behavioral tectonic drawings (plan/section/detail); physical agentBody-style prototype fragment combining printed joints + cast fragments |

**Deliverables:** agent codebase + iteration logs, growth-formation studies, tectonic drawings, printed + cast prototype fragment, festival pin-up.

---

## 7. Background — why me for TFL

1. **Alisa Andrasek studio — "Social Hideout":** built and executed a five-script multi-agent pipeline (space colonization, climate-attractor scripting against EPW data, Voronoi + K-means program classification, discrete-element distribution, flocking-boids filtering) with an LLM/MCP-driven vibe-coding workflow. This is not a proposed method — it is prior, demonstrated work. It also follows Andrasek's own practice methodology directly: her built projects run multiple distinct algorithm families — cellular division (*Alien Within Familiar*, *Wrinkle in Space*), multi-agent systems (*Cloud Pergola*, Croatian Pavilion, Venice Biennale 2018), and physics simulation (*Endemic Interstices*, mud-cracking formwork used specifically to avoid material waste) — each chosen for a specific tectonic purpose, sometimes combined within one project. My five-script pipeline is structurally the same approach, not simply borrowed vocabulary. *Cloud Pergola* additionally solved a real fabrication problem — training a robotic arm to track and correct for material tolerance errors in real time during printing — a concrete precedent for "AI assists, responds to real material behavior" rather than a generic claim.

2. **Marc Gibson studio — "Beyond the Monolith":** hybrid tectonic condition merging monolithic and estranged architectural languages via stepping/interlocking/blending transformation logic; large-scale fabrication literacy through VoxelJet 3D sand printing and polymer printing in Nanjing, China; Parts → Chunks → Architecture hierarchy — a design language recurring across all my studio work.

3. **Igor Pantic studio — "Augmented Materiality":** rigorous, ratio-tested material study (gelatin/cornstarch/PVA/polyurethane binders against coffee-ground filler) and a working HoloLens/Fologram AR-guided mould-carving and casting workflow — the direct precedent for the metal cold-casting track proposed here.

4. **RA — Tectonic Formation Lab, Building 45 facade (Marc Gibson, S1 2026):** hands-on execution of a real, built hybrid tectonic facade — cast GFRC + large-format polymer 3D print + metal connectors — through the full pipeline (CNC foam mould, plaster patching, resin/UV cure, GFRC casting, demoulding, bolt-bracket assembly). Demonstrates I can resolve computational geometry to real fabrication tolerance, not only screen-based form.

5. **Currently enrolled — "Circular Tectonics" Hong Kong Travelling Studio (Dr Nic Bao & Harlan Guo, S2 2026):** working with reclaimed construction materials — cataloguing, 3D scanning, and connecting them via custom 3D-printed joints and mixed-reality-guided assembly. Studio runs at RMIT through October, then travels to CUHK Hong Kong in early November to build a full-scale pavilion.

**I am not asking you to supervise a discrete/standardized modular kit thesis, an urban policy project, or a bio-material engineering thesis.** I am proposing **behavioral tectonic research** in off-cut/recycled metal, realised through small-scale AM and cold-casting — directly extending the *Behavioral Formation* and *agentBody* trajectory with a material stream your published research has not yet addressed.

---

## 8. Material evidence and open research (in progress)

**Why not bio-composite (coffee waste) as the primary material:** my own ratio-tested data from the Pantic studio shows real structural limitations — several coffee-composite formulations were brittle when thin, cracked or broke on demoulding, and required long, variable cure times. Best performer (polyurethane:coffee 1:1) was strong but still a biomass-filled composite, not suited to being the primary structural material of an intricate, load-bearing tectonic system.

**Why metal instead:**
- **Cold-cast bronze/aluminium** (fine metal powder + resin, ~1:2 by volume, poured into silicone/plaster moulds) — an established sculpture technique producing genuinely metallic surface quality at room temperature, no foundry required. Directly reuses my proven mould-making pipeline.
- **Metal-filled FDM filament** (bronze/copper composite, 30–50% metal powder in a PLA/PETG base) — prints on my available Bambu Lab X1 Carbon (already fitted with the hardened steel nozzle these abrasive composites require); sanded/polished to a genuine metallic sheen.
- **Stretch option under investigation:** fully sinterable metal filament (e.g. Virtual Foundry Filamet) printed on the same desktop printer, then debound and kiln-sintered to solid metal — pending confirmation of kiln access through RMIT sculpture/ceramics workshops.

**Open material research (continuing in parallel with this proposal):** whether recycled metal swarf/filings/off-cuts can be ground into a usable powder to substitute for commercial bronze/aluminium powder in the cold-cast mix — this would close the loop between the site's material identity (Fishermans Bend off-cut stream) and the actual material in hand, rather than using commercially sourced metal powder. This research is ongoing and will refine the material section ahead of Week 10 lock-in.

---

## 9. What is new (knowledge through architecture)

- Extending the **agentBody algorithm** — proven on uniform stock in Brass Swarm (bent rod) and RMIT Mace (titanium SLM powder) — to **irregular, reclaimed off-cut material geometry** as an agent-level constraint, tested through both cold-casting and metal-filled AM. This is a specific, named gap in Kokkugia's own published lineage, not a generic "behavioral formation" claim.
- A documented **multi-agent + LLM/MCP + desktop AM/cold-cast** pipeline achievable without industrial robotic fabrication access — evidence that intricate, non-repetitive behavioral tectonics research is achievable at accessible/consumer-hardware scale, not only in a robotics lab.
- A site-specific argument connecting a precinct's own industrial material history to its computationally-generated architectural future.

---

## 10. Scope — 15 weeks

**In scope:**
- Multi-agent growth-formation system (space-colonization/differential-growth primary; Python/vibe-coded, extending Social Hideout pipeline)
- One primary material family (metal — cold-cast + metal-filled AM), continuing material R&D through Week 10
- One proto-architectural prototype fragment combining printed joints + cast elements
- Full tectonic drawings + festival presentation
- Site framing at Fishermans Bend (specific footprint confirmed once material-sourcing research narrows)

**Out of scope:**
- Discrete/standardized repeatable-parts kit as the primary tectonic logic
- Bio-composite (coffee waste) as primary structural material — retained only as background material-research evidence
- Industrial robotic AM (no access for this project)
- Moon base / off-world sites
- City-scale masterplan

**Week 10 lock-in** — concept and material family frozen per RMIT briefing.

---

## 11. Why Roland Snooks (and Nic Bao as second)

**Primary — Professor Roland Snooks:** My strongest preparation is multi-agent/swarm design (Andrasek's Social Hideout, already executed with an LLM/MCP pipeline) combined with tectonic and fabrication ambition (Gibson, Pantic, RA GFRC work). TFL's research on behavioral formation and advanced fabrication is the direct intellectual home for testing whether that intricacy can survive into off-cut metal AM/casting.

**Second — Dr Nic Bao:** If metal-composite or cast-material performance needs technical consultation, I would value occasional FormX input on composite behaviour and circular-material precedent. Nic remains my second preference for primary supervision if TFL capacity is limited.

---

## 12. Request

I respectfully request supervision under the **Tectonic Formation Lab** for the above project. I attach portfolio material demonstrating the multi-agent/LLM pipeline (Social Hideout), hybrid tectonic and fabrication experience (Gibson studio, RA GFRC facade work), and material/AR casting research (Pantic studio).

Could we meet to confirm scope, whether off-cut/recycled metal as a behavioral-tectonics material stream fits TFL's current research agenda, and feasibility of desktop AM + cold-casting as the fabrication method for this project?

Kind regards,
**Kankawee Maksomboon (Frank)**

---

## Email subject

`Major Project supervision request — Behavioral tectonics / multi-agent off-cut metal AM (TFL alignment)`

## Short EOI

Dear Roland,

I am writing to request your supervision for my Major Project on **behavioral formation and multi-agent growth simulation** for **off-cut/recycled metal tectonics** — tested through desktop additive manufacturing and cold-casting, sited within Fishermans Bend's manufacturing-transition context.

My preparation includes a working **multi-agent + LLM/MCP pipeline** built in Alisa Andrasek's studio ("Social Hideout" — space-colonization growth, climate-data-driven attractors, discrete-element distribution), **hybrid tectonic and large-scale fabrication experience** with Marc Gibson (VoxelJet sand printing, and hands-on GFRC/polymer facade fabrication as a TFL Research Assistant on Building 45), and a **rigorous material and AR-casting workflow** developed with Igor Pantic, which I am now redirecting from bio-composite toward cold-cast and metal-filled AM.

I believe this extends TFL's *behavioral tectonics* research into a material stream — recycled/off-cut metal — not yet addressed in the published *agentBody* work. **Dr Nic Bao** is my second preference if TFL capacity is limited.

Could we meet to discuss fit and scope?

Kind regards,
Frank (Kankawee Maksomboon)
