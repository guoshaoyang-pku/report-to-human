# report-to-human

**让 AI 说人话。**

agent 向人汇报的四层协议：正文用航空维修手册的语言写，配置用一行图标交代，细节放进交互面板，聊天框只留一句话结论和链接。

<p align="center">
  <img src="assets/xhs-cover.jpg" width="31%" alt="封面：让 AI 说人话">
  <img src="assets/xhs-layers.jpg" width="31%" alt="四层架构">
  <img src="assets/xhs-effect.jpg" width="31%" alt="前后对比">
</p>

## 安装

把这句话发给 Codex 或 Claude Code：

> 帮我安装这个 skill：github.com/guoshaoyang-pku/report-to-human

**给执行安装的 agent**：把本仓库 clone 到宿主的 skills 目录，文件夹名保持 `report-to-human`，然后让用户开新会话。

| 工具 | 目录 |
| --- | --- |
| Claude Code | `~/.claude/skills/report-to-human` |
| Codex | `~/.codex/skills/report-to-human` |

装好之后，对 agent 说 **"跟我汇报"**。

## 四层

| 层 | 承载 | 规则 |
| --- | --- | --- |
| L1 文字 | 报告正文 | ASD-STE100 的 80% 严格性：短句、一个概念一个名字、主动语态、数字和限定词不丢 |
| L2 图标 | 配置与结构 | 一行 badge；结构用图；曲线出图 |
| L3 panel | 主阅读面 | 单文件 HTML：结论当标题、一节一图、样本浏览器 |
| L4 聊天框 | 入口 | 名称 + 一句话结论 + panel 链接 + 报告链接 |

## v2 三条硬规则

1. **极简**：副标题、KPI 卡、节编号、PID 与状态行、"查看 Markdown"按钮默认删除。首屏只有标题、一句话结论、settings 行。
2. **术语先解释后使用**：项目代号、run 名、公式符号在第一次出现的同一句里用平实的话解释。首屏不出现未解释的词。
3. **统一外观**：panel 从 `assets/panel-template.html` 改起（Anthropic 配色与字体），HTML 里用单色线性图标，图用同一套风格。

交付前用 `scripts/panel_audit.py <panel.html>` 自检前两条。

## 仓库

```
SKILL.md                    # 协议（agent 读的部分，中文）
docs/SKILL.en.md            # 协议英文版
assets/panel-template.html  # 极简 panel 模板
scripts/panel_audit.py      # 交付前自检：多余元素 + 未解释术语
scripts/panel_style.py      # 统一绘图风格
scripts/plot_run_metrics.py # 读任何 log_history.json 出 reward/seqlen/clip 图
references/                 # STE 80% 规则调研 + RL trial 分析示例
```

## 其它

- 出处：[Karpathy 2026-10-02 的输出阶梯](https://x.com/karpathy/status/2105819303471976479)；L1 依据 [ASD-STE100 Issue 9](https://www.asd-ste100.org/)；panel 配色来自 [Anthropic brand-guidelines](https://github.com/anthropics/skills)；绘图规则取自 [Orchestra academic-plotting](https://github.com/Orchestra-Research/AI-Research-SKILLs)。
- MIT，见 [LICENSE](LICENSE)。
