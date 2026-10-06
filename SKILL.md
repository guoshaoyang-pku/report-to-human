---
name: report-to-human
description: A 4-layer protocol for agent-to-human reporting, inspired by Karpathy's output ladder (Oct 2026). L1 prose at 80% ASD-STE100 strictness, L2 settings and structure as icons and diagrams, L3 an interactive HTML panel as the main reading surface, L4 a chat message that carries only a one-line takeaway and links. Use whenever an agent reports results, experiment analyses, status, or findings to a human. Trigger phrases include "report to human", "brief me", "4-layer report", "ASD-STE100", "STE style", "HTML panel", "iconified settings", "experiment analysis", "trial analysis", "dashboard", "panel".
---

# report-to-human: the 4-layer reporting protocol

Organize everything an agent shows a human into 4 layers. The upper layers carry the content. The chat box is the last and thinnest layer.

Source: Karpathy's output ladder, 2026-10-02 — writing → diagrams → HTML → video ([x.com/karpathy/status/2105819303471976479](https://x.com/karpathy/status/2105819303471976479)). This skill grounds layer 2 as iconified settings and replaces layer 4 (video) with the chat-box entry point.

## Reader language

- Write every human-facing artifact in the reader's language. Match the language the user writes in.
- Keep technical terms, metric names, identifiers, code, paths, and commands in their original English form. Do not translate them. One concept keeps one name everywhere. This is also STE rule 1.11.
- The protocol and the ASD-STE100 rules run as specified in the English canon. Only the output language changes. Apply the same sentence discipline to any language: short sentences, one fact per sentence, consistent terms, active voice.

## The 4 layers

### L1 — Prose: ASD-STE100 at 80% strictness

- One name per concept, used consistently. Never rotate synonyms (worker/agent/executor for the same thing).
- Short sentences: descriptive ≤ 25 words, instructions ≤ 20 words. One fact per sentence.
- Active voice, concrete subjects. Say who does what. One instruction per sentence. Put conditions before actions.
- Plain verbs: use / start / before, not utilize / commence / prior to.
- Modals: must / can, or an exact condition. Do not stack should / might.
- No semicolons. One topic per paragraph, ≤ 6 sentences.
- Preserve every number, unit, uncertainty, exception, and qualifier. Never drop a fact to save length. Split or restructure instead.
- Mark risks as WARNING / CAUTION blocks: command or condition first, consequence second.
- 80% is a style choice, not a compliance claim. Full rule profile, strict-mode deltas, and open-source implementations: `references/asd-ste100-80.md`.

### L2 — Icons and diagrams: settings never travel as prose

- Show configuration as a one-line icon badge row, for example: 🤖 model · 🧮 algorithm · 📈 lr · ✂️ cap · 🖥️ cluster · 📅 date. Markdown: badge line. HTML: chips.
- Prefer diagrams (Mermaid / SVG) over paragraphs for structure and flow.
- Render experiment curves and metrics as figures, stored next to the report (for example `docs/reports/figs/`, embedded by relative path).

### L3 — HTML panel: the main reading surface

- If the project already has a dashboard, use it and link to it.
- Otherwise generate a single self-contained HTML file: data inlined, no build step, no external dependencies. Store it next to the report, hand over a file:// or hosted link, and open it in a browser preview.
- Panel contents: settings badge area, main figures, conclusion area, and a sample browser (for example side-by-side model outputs) when relevant.

### L4 — Chat box: entry point only

- Chat message = name + one-line takeaway + panel link + report file link.
- Do not paste the report body into chat. Do not stack tables or number dumps in chat.

## Domain example: RL trial analysis

Mapping for analyzing an RL training run (any framework with per-step logs, for example a HF-Trainer-style `log_history.json`):

- **L4 chat**: trial name + one-line takeaway + dashboard URL (say which run to select if the dashboard has no URL parameters) + report path. The panel link lives in chat only, never inside the report document.
- **L3 panel**: the training dashboard, or a generated static HTML panel.
- **L1 report** `docs/reports/<trial>.md`: one prose paragraph on metric trends (reward, sequence length, truncation rate, clip ratio, entropy/KL, held-out probes; no bullet lists) → chain-of-thought analysis (early / mid long-vs-short / late-short samples, plus a think-vs-direct contrast arm; quote samples in full under ~1000 characters, otherwise keep head/middle/tail ~500 characters each and mark the elision) → prose conclusions, written last, minimal tables and subsections.
- **L2 figures**: reward, completion length (the protagonist in runs with a length-cap penalty), clip ratio; optional entropy/KL and held-out accuracy. `scripts/plot_run_metrics.py` plots these from any `log_history.json`.
- **Sampling discipline**: generate CoT samples under training-aligned conditions (same temperature/top_p, same thinking flag, same completion cap, held-out question set). Pick mid-training checkpoints where CoT text still appears; late checkpoints that already self-skip make the contrast arm degenerate.

Full worked example with pitfall checklist: `references/domain-example-rl-trial.md`.

## Credits and prior art

- [Karpathy's post](https://x.com/karpathy/status/2105819303471976479) (2026-10-02) — the ladder this skill implements.
- [ASD-STE100 Issue 9](https://www.asd-ste100.org/) — the controlled-language standard behind L1.
- See `references/asd-ste100-80.md` for the open-source implementations surveyed (0xpili, ashryaagr, danyuchn, JAICHANGPARK, asdste100foragents.shop).
