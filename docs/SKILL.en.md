---
name: report-to-human
description: A 4-layer protocol for agent-to-human reporting, v2, inspired by Karpathy's output ladder (Oct 2026). L1 prose at 80% ASD-STE100 strictness, L2 settings and structure as icons and diagrams, L3 an interactive HTML panel as the main reading surface, L4 a chat message that carries only a one-line takeaway and links. v2 adds three hard rules - minimalism (no subtitles, KPI cards, status banners), explain every term before using it, and a shared Anthropic-palette panel template and figure style - plus a pre-delivery audit script. Use whenever an agent reports results, experiment analyses, status, or findings to a human, or builds a report page, HTML panel, or dashboard. Trigger phrases include "report to human", "brief me", "4-layer report", "make a panel", "ASD-STE100", "STE style", "HTML panel", "iconified settings", "experiment analysis", "trial analysis", "dashboard", "panel".
---

# report-to-human v2: the 4-layer reporting protocol

Organize everything an agent shows a human into 4 layers. The upper layers carry the content. The chat box is the last and thinnest layer.

Source: Karpathy's output ladder, 2026-10-02 — writing → diagrams → HTML → video ([post](https://x.com/karpathy/status/2105819303471976479)). This skill grounds layer 2 as iconified settings and replaces layer 4 (video) with the chat-box entry point.

## Three hard rules (v2, override everything below)

### 1. Minimalism: delete what the reader does not need

Deletion test: for each element, ask "if I delete this, does the reader lose a fact they need?" If you cannot name the fact, delete it.

Delete by default, unless the user asks for it:

- Subtitles, taglines, and descriptor lines under the title.
- KPI cards, big-number cards, metric tiles, score badges. Put numbers into conclusion sentences or figures.
- Section numbers ("0 · Lineage") and gray explainer text beside section headings.
- Status data: PIDs, process liveness, "running / archived" labels, snapshot and build times, SHA256, line counts. At most one footer line with source and date.
- The page talking about itself: "this page is a static snapshot", "reading scope", "how to use this page".
- Tables of contents, skip links, and "view / download Markdown" or "print" buttons on short pages.
- Table columns where every value is the same.
- Captions that repeat the prose, prose that repeats the figure.

The first screen (everything before the first h2) holds exactly three things: a plain-language title that states the conclusion, a one-sentence conclusion, and one settings row.

Write each h2 as a finding ("Completion length drops sharply near step 120"), not a topic label ("Length analysis").

### 2. Terms: explain first, use second

The reader knows the field's common vocabulary but did not work on this project. Common terms (token, loss, SGD, reward, KL) need no explanation. Explain these in plain words where they first appear:

- Project-coined concepts and abbreviations.
- Formula symbols. First use: "D (frozen difficulty: the loss of the pre-training model on this batch)".
- Internal codenames, run names, round IDs. In prose, use a plain name ("the first synchronous-loop run"). Put the codename after it as a small monospace tag, or leave it out.

Rules:

- The title and the first screen contain zero unexplained terms. If you cannot explain a term there, replace it with a plain phrase.
- Put the explanation next to the term, in the same sentence, in parentheses or after a colon. Do not move explanations to a glossary at the end.
- One concept, one name, everywhere (STE rule 1.11). After you choose the plain name, do not switch back to the codename.
- State in one sentence what a formula computes before you show the formula.

### 3. Looks: start from the template, one style

- Build HTML panels from `assets/panel-template.html`. Do not write CSS from scratch. The template uses Anthropic brand-guidelines colors and type: background #faf9f5, text #141413, primary accent orange #d97757 (the main result), blue #6a9bcc and green #788c5d for comparisons, gray #b0aea5 / #e8e6dc for borders and grids. Headings in Poppins, body in Lora, with CJK fallbacks. Single 760px column.
- In HTML, settings icons are monochrome line SVGs (examples in the template), never color emoji. Color emoji are for chat and markdown only.
- Data figures use `scripts/panel_style.py`: same palette, no top/right spines, light grid, frameless legend, main result always orange. Export SVG (for the panel) and 2x PNG. No titles inside figures; the h2 states the finding.
- Chart choice and plotting details follow the Orchestra AI-Research-SKILLs academic-plotting rules: line plots for step axes, grouped bars for N methods × M benchmarks, no pie charts, highlight the main result, split the figure or switch to Okabe-Ito colors beyond 5 series.

## Reader language

- Write every human-facing artifact in the reader's language. Match the language the user writes in.
- Keep technical terms, metric names, identifiers, code, paths, and commands in their original English form.
- The protocol and the ASD-STE100 rules run as specified in the English canon. Only the output language changes.

## The 4 layers

### L1 — Prose: ASD-STE100 at 80% strictness

- One name per concept, used consistently. Never rotate synonyms.
- Short sentences: descriptive ≤ 25 words, instructions ≤ 20 words. One fact per sentence.
- Active voice, concrete subjects. Conditions before actions.
- Plain verbs: use / start / before, not utilize / commence / prior to.
- Modals: must / can, or an exact condition. Do not stack should / might.
- No semicolons. One topic per paragraph, ≤ 6 sentences.
- Preserve every number, unit, uncertainty, exception, and qualifier. Split sentences instead of dropping facts.
- Mark risks as caution blocks: condition first, consequence second.
- Full rule profile and open-source implementations: `references/asd-ste100-80.md`.

### L2 — Icons and diagrams: settings never travel as prose

- Show configuration as one row of "icon + name + value": model, algorithm, data, key hyperparameters, date. Only items the reader needs to judge the conclusion, usually ≤ 6.
- Prefer diagrams (Mermaid / SVG) over paragraphs for structure and flow.
- Render curves and metrics as figures.

### L3 — HTML panel: the main reading surface

- If the project already has a dashboard, use it and link to it.
- Otherwise copy `assets/panel-template.html`: single file, data inlined, no build step, no external dependencies. Store it next to the report and open it in a browser preview.
- Structure: first screen (title, one-sentence conclusion, settings row) → per section one finding-sentence h2 + one paragraph + one figure → a sample browser when relevant → detail numbers folded into `<details>` → one footer line with the source.

### L4 — Chat box: entry point only

- Chat message = name + one-line takeaway + panel link + report file link.
- Do not paste the report body into chat. Do not stack tables or number dumps in chat.

## Pre-delivery audit (required)

1. Run `python scripts/panel_audit.py <panel.html> --allow <common terms the reader knows>`. It lists, in reading order: extra elements, first-screen block count, and terms with no nearby explanation at first appearance.
2. Fix each item: delete extra elements, explain terms or replace them with plain phrases. Add terms that need no change to `--allow`.
3. Rerun until nothing you would change remains.
4. Screenshot the first screen: only the title, the one-sentence conclusion, and the settings row, with no word the reader does not know.

## Domain example: RL trial analysis

- **L4 chat**: trial name + one-line takeaway + dashboard URL (say which run to select if the dashboard has no URL parameters) + report path.
- **L3 panel**: the training dashboard, or a static panel built from the template.
- **L1 report**: one prose paragraph on metric trends → chain-of-thought analysis (early / mid long-vs-short / late samples, plus a think-vs-direct contrast; quote samples in full under ~1000 characters, otherwise head/middle/tail ~500 each with the elision marked) → conclusions, written last.
- **L2 figures**: `scripts/plot_run_metrics.py` plots reward, completion length with truncation, clip ratio and entropy/KL from any `log_history.json`, already in panel style.
- **Sampling discipline**: generate CoT samples under training-aligned conditions (same temperature/top_p, thinking flag, completion cap, held-out set). Pick mid-training checkpoints where CoT text still appears.

Full worked example with pitfall checklist: `references/domain-example-rl-trial.md`.

## Credits and prior art

- [Karpathy's post](https://x.com/karpathy/status/2105819303471976479) (2026-10-02) — the ladder this skill implements.
- [ASD-STE100 Issue 9](https://www.asd-ste100.org/) — the controlled-language standard behind L1.
- [Anthropic skills · brand-guidelines](https://github.com/anthropics/skills) — panel palette and type.
- [Orchestra AI-Research-SKILLs · academic-plotting](https://github.com/Orchestra-Research/AI-Research-SKILLs) — plotting rules.
- Surveyed ASD-STE100 implementations: `references/asd-ste100-80.md`.
