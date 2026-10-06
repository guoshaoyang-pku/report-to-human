# ASD-STE100 at 80%: rule reference for reporting

Baseline: ASD-STE100 Simplified Technical English, Issue 9 (2025-01-15), maintained by ASD (AeroSpace and Defence Industries Association of Europe).

Karpathy's suggestion is "80% of the way to ASD-STE100": keep the sentence discipline, relax the vocabulary lockdown. 80% is a style choice, not a compliance score. A strict-compliance claim requires checking the official Issue 9 rules and the ~900-word controlled dictionary (free to obtain from asd-ste100.org, not free to redistribute).

## Core rules (80% mode, sufficient for report writing)

**Words and terms**
- One name per concept, consistent across the whole document (rules 1.11 / 9.4). This is the most common AI-output failure: calling the same thing worker, then agent, then executor.
- Replace bureaucratic verbs with plain ones: use←utilize, start←commence, before←prior to, about←approximately.
- Modern technical nouns are allowed (API, cache, checkpoint, reward), but each keeps exactly one meaning in the document.
- Do not verb a technical noun without introducing the usage.

**Sentences**
- Instructions ≤ 20 words, descriptions ≤ 25 words (hard cap 25). Apply the same spirit to other languages: one fact per sentence.
- One instruction per sentence. Two actions only when they happen at the same time.
- Condition first, command second, separated by a comma ("If the run has a cap penalty, report sequence length first.").
- Active voice. Passive only in descriptive text when the actor is unknown.
- No semicolons. No contractions. Use parentheses rarely; parenthesized content counts as one word.

**Paragraphs and structure**
- One topic per paragraph, ≤ 6 sentences. Convert complex material into vertical lists.
- Use explicit connectors between sentences; never make the reader infer the logic.
- Multi-word nouns ≤ 3 words; longer ones get a full introduction plus a defined short form.

**Modality and precision**
- must / can, or an exact condition. Delete should / might / could or convert them into explicit conditions.
- Preserve every number, unit, uncertainty, exception, and qualifier. Deleting a fact to meet a length limit is a violation; split or restructure the sentence instead.
- Alert blocks: WARNING / CAUTION — command or condition first, risk and consequence second.

**Non-English reports**
STE discipline transfers across languages (JAICHANGPARK's STE pane rewrites answers in their own language): short sentences, single term per concept, active voice, one fact per sentence, explicit connectors, all numbers and qualifiers preserved.

## Caveats

- The cheat-sheet image attached to Karpathy's tweet contains errors (it inverts one dictionary rule and approves a verb the standard rejects). See the fact-check: max.nardit.com/articles/karpathy-understanding-llm-outputs. Do not treat the image as the spec; use Issue 9 or the machine-readable references below.
- A prettier format can make an error look more credible. For every format, ask: what does it let the reader verify?

## Open-source implementations (surveyed 2026-10)

| Project | What it is | Notable parts |
| --- | --- | --- |
| [0xpili/simplified-technical-english](https://github.com/0xpili/simplified-technical-english) | Agent skill, 911 stars, predates the tweet (2026-08) | Rules + approved word list + check tool; the README is itself written in STE |
| [ashryaagr/karpathy-output-style](https://github.com/ashryaagr/karpathy-output-style) | Codex/Claude plugin, four-skill set | Mirrors Karpathy's ladder 1:1: clear-writing / explain-diagram (Excalidraw MCP) / explain-webpage / explainer-videos (Manim + ElevenLabs); references/asd-ste100.md maps Issue 9 rules and corrects the tweet image |
| [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) | Claude skill (linked in Karpathy's replies) | Strict / STE-flavored dual mode; deterministic linter `ste-lint.py` (semicolons, phrasal verbs, nominalizations, marketing adjectives, passive voice, long sentences, synonym rotation); `npx skills add danyuchn/asd-ste100-skill` |
| [JAICHANGPARK/ASD-STE100](https://github.com/JAICHANGPARK/ASD-STE100) | Claude Code plugin + mod | `/asd` command, maintenance-manual-style STE pane, strict-100 vs 80% comparison table, `bin/ste.js check` scoring CLI, the "4 cognitive modalities" framing |
| [prithivrajmu/asd-ste100](https://github.com/prithivrajmu/asd-ste100) | Lightweight agent skill | Defaults to 80% mode, compact rules |
| [asdste100foragents.shop](https://asdste100foragents.shop/) | Machine-readable reference site (not a skill) | Independent paraphrase of all 53 rules: `/llms-full.txt` (prompt-ready), `/rules.json`, `/prompt.txt` (drop-in editing prompt) |

## Sources

- Karpathy's post: x.com/karpathy/status/2105819303471976479 (2026-10-02)
- Official standard: asd-ste100.org — Issue 9 PDF: asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf
- Fact-check: max.nardit.com/articles/karpathy-understanding-llm-outputs
- The rule items here are paraphrased from the public secondary sources above. The official dictionary is not redistributed.
