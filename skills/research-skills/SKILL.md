---
name: research-skills
description: Router into the Orchestra AI-Research-SKILLs library (12.7k stars, MIT). Pulls and routes the right sub-skill on demand for ML paper writing (NeurIPS/ICML/ICLR/ACL), academic plotting, conference talks, research ideation, and an English de-AI-tell prose pass. Use when the user asks to draft/revise/structure a paper (research-paper-writing), write an abstract or related work, make publication figures, prepare a talk or poster, brainstorm research ideas, de-AI English prose, or says 写论文 / 润色 / 摘要 / 画图 / 投稿 / talk / ICLR / NeurIPS. Do not preload sub-skills; pull only what the task needs.
---

# research-skills — Orchestra library router

Single entry point into the Orchestra AI-Research-SKILLs repo. Register one router,
not eighty skills: modern models do not need a crowded skill list, so this router
exposes a small Tier-1 set and pulls sub-skill content only on demand.

- Upstream: `https://github.com/Orchestra-Research/AI-Research-SKILLs` (MIT).
  Clone it once to a stable location, for example `~/vendor/AI-Research-SKILLs`.
- Update policy: before heavy use, if HEAD is older than ~30 days run
  `git -C <vendor-dir> pull --ff-only` and re-check `git log -1`. Trust ONLY this
  upstream; before vendoring any other skill source, verify stars (very high),
  recency, and license first.

## Pull protocol (never preload)

1. Match the task to ONE route below.
2. Read that sub-skill's `SKILL.md` under the vendor dir (and only the specific
   `references/*.md` file it points to for the task at hand).
3. Execute the task following that sub-skill's workflow.

## Tier-1 routes (curated)

| Task | Pull from (under `20-ml-paper-writing/`) | Notes |
|---|---|---|
| Draft / revise / structure an ML paper; abstract; intro; related work; checklists; camera-ready (a.k.a. research-paper-writing) | `ml-paper-writing/SKILL.md` | Writing philosophy (Nanda narrative, Farquhar 5-sentence abstract, Gopen & Swan); venue checklists; LaTeX templates in `ml-paper-writing/templates/` |
| De-AI an English prose draft (abstract, README, blog post, paper section) | `references/de-ai-prose.md` (bundled with this router) | Tell checklist condensed from blader/humanizer (MIT). For Chinese prose use a Chinese content-discipline skill instead |
| Citations / BibTeX / literature lookup | `ml-paper-writing/references/citation-workflow.md` | Absolute rule: never generate BibTeX from memory — verify via API, else mark `[CITATION NEEDED: topic]` |
| Publication figures / plots | `academic-plotting/SKILL.md` | matplotlib/seaborn venue styling, diagram workflows |
| Conference talk / poster / slides | `presenting-conference-talks/SKILL.md` | Use after acceptance or for practice talks |
| Systems-venue paper (OSDI/NSDI/ASPLOS/SOSP) | `systems-paper-writing/SKILL.md` | Not for ICLR-track work |
| Research idea brainstorming (post-deadline) | `21-research-ideation/<sub-skill>/SKILL.md` | Not during a submission sprint |

Everything else in the vendored repo (categories 01-19, 22) is Tier-2: browse
by listing the repo root ONLY when a task clearly maps to a category; do not
register or read them speculatively.

## Deliberately not separate skills

- arxiv search: a web search or the venue API covers ad-hoc lookups; a dedicated
  skill would add a trigger without adding capability.
- PowerPoint / plan modes: host agents ship these natively.
- A standalone "research-paper-writing" skill: it duplicates the ml-paper-writing
  route above. Requests with that name land here.
