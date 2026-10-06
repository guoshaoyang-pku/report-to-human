# report-to-human

**让你的 Agent 学会 REPORT TO HUMAN。让 AI 说人话。**

A 4-layer reporting protocol for AI agents, inspired by [Karpathy's output ladder](https://x.com/karpathy/status/2105819303471976479) (2026-10-02): writing → diagrams → HTML → video.

Your agent should not dump three screens of markdown into the chat box. The chat box is the thinnest layer. The content lives in the layers above it.

| Layer | Carries | Rule |
| --- | --- | --- |
| **L1 Prose** | reports & analysis | ASD-STE100 at **80% strictness** — the controlled language built for aircraft maintenance manuals. Short sentences, one name per concept, active voice, every number and qualifier preserved |
| **L2 Icons & diagrams** | settings & structure | config as a one-line icon badge row (🤖 model · 🧮 algorithm · 📈 lr · ✂️ cap · 🖥️ cluster), structure as diagrams, curves as figures |
| **L3 HTML panel** | the main reading surface | one self-contained interactive HTML file: settings chips, main figures, conclusions, sample browser |
| **L4 Chat box** | entry point only | name + one-line takeaway + panel link + report link. Nothing else |

```mermaid
flowchart TB
    subgraph content["where the content lives"]
        direction LR
        L1["L1 · Prose\nASD-STE100 @ 80%"]
        L2["L2 · Icons & diagrams\nsettings · structure · curves"]
        L3["L3 · HTML panel\nmain reading surface"]
    end
    L4["L4 · Chat box\none-line takeaway + links"] --> content
```

## Why ASD-STE100?

ASD-STE100 is the controlled language the aerospace industry built so a mechanic anywhere in the world reads a step once and gets it right: ~900 approved words, one meaning each, short sentences, active voice, one instruction per sentence. Karpathy's tip: ask for **"80% of the way to ASD-STE100"** — keep the discipline, relax the vocabulary lockdown. It fixes the exact things AI prose breaks: synonym rotation (worker → agent → executor), hedge stacks (should/might/could), 60-word sentences, and decorative filler.

Full rule profile: [`references/asd-ste100-80.md`](references/asd-ste100-80.md).

## Install

Any agent that loads skills (Claude Code, Codex, Verdent, ...):

```bash
# via the skills CLI
npx skills add guoshaoyang-pku/report-to-human

# or clone into your skills directory
git clone https://github.com/guoshaoyang-pku/report-to-human ~/.claude/skills/report-to-human
```

Then just say: **"report to human"** / **"跟我汇报"** / "brief me on this run in 4 layers".

## Repo layout

```
SKILL.md                              # the protocol (what agents load)
references/asd-ste100-80.md           # 80% rule profile + open-source survey
references/domain-example-rl-trial.md # worked example: RL training-run analysis
scripts/plot_run_metrics.py           # reward/seqlen/clip figures from any log_history.json
```

## Reader language

The protocol is language-agnostic: write artifacts in the reader's language, keep technical terms in English, apply the same sentence discipline anywhere. (Author's default: 中文汇报，术语保留英文。)

---

## 中文说明

**report-to-human：4 层汇报体系。** 一切"给人看"的产出按 4 层组织，聊天框是最后、最薄的一层。

- **L1 文字层**：用 ASD-STE100 的 80% 严格性写散文——航空维修手册级的受控语言。短句、一个概念一个名字、主动语态、数字和限定词全保留。治好 AI 输出的老毛病：同义词轮换、should/might 堆叠、60 词长句、装饰性废话。
- **L2 图标/图示层**：settings 用一行图标 badge 展示（🤖 模型 · 🧮 算法 · 📈 lr · ✂️ cap · 🖥️ 集群），结构用图，曲线出图，不靠散文交代配置。
- **L3 HTML panel 层**：主阅读面。单文件自包含 HTML：settings chip、主曲线、结论区、样本浏览器。有现成 dashboard 就直接用。
- **L4 聊天框层**：只留入口——名称 + 一句话结论 + panel 链接 + 报告链接。不贴正文，不堆表格。

来源：Karpathy 2026-10-02 的输出阶梯（writing → diagrams → HTML → video）。本 skill 把第 2 层落地为 settings 图标化，把第 4 层替换为聊天框入口。

内置领域示例：RL 训练 trial 分析（reward/seqlen/clip 曲线 + 思维链演变抽查 + think-vs-direct 对照臂 + 完整避坑清单），附通用绘图脚本 `scripts/plot_run_metrics.py`（读任何 HF-Trainer 风格的 `log_history.json`）。

## Credits & prior art

- [Karpathy's post](https://x.com/karpathy/status/2105819303471976479) — the ladder.
- [ASD-STE100 Issue 9](https://www.asd-ste100.org/) — the standard behind L1. Not redistributed here; rule items are independent paraphrases from public secondary sources.
- [0xpili/simplified-technical-english](https://github.com/0xpili/simplified-technical-english) · [ashryaagr/karpathy-output-style](https://github.com/ashryaagr/karpathy-output-style) · [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) · [JAICHANGPARK/ASD-STE100](https://github.com/JAICHANGPARK/ASD-STE100) — surveyed implementations, see the table in `references/asd-ste100-80.md`.
- Note: the cheat-sheet image attached to the original tweet contains errors ([fact-check](https://max.nardit.com/articles/karpathy-understanding-llm-outputs)). This repo follows Issue 9, not the image.

## License

MIT — see [LICENSE](LICENSE).
