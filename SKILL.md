---
name: report-to-human
description: 面向人的 4 层汇报体系（源自 Karpathy 2026-10 的输出阶梯）。L1 用 ASD-STE100 的 80% 严格性写散文，L2 用图标和图示展示 settings 与结构，L3 用交互式 HTML panel 作为主阅读面，L4 聊天框只留一句话结论和链接。默认用中文汇报，术语保留英文。agent 向人汇报结果、实验分析、进度或发现时使用。触发词：跟我汇报、汇报一下、report to human、4层汇报、ASD-STE100、STE 风格、HTML panel、settings 图标化、实验分析、trial 分析、dashboard、panel。
---

# report-to-human：4 层汇报体系

agent 给人看的所有产出，都按 4 层组织。内容放在上面三层。聊天框是最后、最薄的一层。

来源：Karpathy 2026-10-02 的输出阶梯：writing → diagrams → HTML → video（[原帖](https://x.com/karpathy/status/2105819303471976479)）。本 skill 把第 2 层落地为 settings 图标化，把第 4 层从视频换成聊天框入口。

## 语言

- 默认用中文写所有面向人的产出：报告正文、badge 与图内文案、HTML panel 界面、聊天消息。
- 如果用户用其他语言提问，就用用户的语言。
- 技术术语、指标名、标识符、代码、路径、命令保留英文原样，不翻译。一个概念全文只用一个名字（STE 规则 1.11）。
- 四层协议和 ASD-STE100 规则按英文规范执行，只改变产出语言。中文同样遵守句式纪律：短句、一句一事、术语一致、主动语态。

## 四层协议

### L1 文字层：ASD-STE100，80% 严格性

- 一个概念一个名字，全文一致。不要同义词轮换（同一个东西先叫 worker，再叫 agent，又叫 executor）。
- 短句。英文描述句 ≤25 词，指令句 ≤20 词。中文一句只讲一个事实，不堆从句。
- 主动语态，主语具体，说清谁做什么。一句一条指令。条件在前，动作在后。
- 用平实的词：use / start / before，不用 utilize / commence / prior to。中文同理，不用"赋能、抓手、闭环"这类词。
- 情态词只用 must / can，或者写出精确条件。不堆 should / might。
- 不用分号。每段一个主题，≤6 句。
- 数字、单位、不确定性、例外和限定词全部保留。不为缩短篇幅删事实，宁可拆句。
- 风险写成 WARNING / CAUTION 块：先写命令或条件，再写后果。
- 80% 是风格选择，不是合规认证。完整规则、strict 模式差异和开源实现清单见 `references/asd-ste100-80.md`。

### L2 图标/图示层：settings 不靠散文交代

- 配置用一行图标 badge 展示，例如：🤖 模型 · 🧮 算法 · 📈 lr · ✂️ cap · 🖥️ 集群 · 📅 日期。markdown 里用 badge 行，HTML 里用 chip。
- 结构和流程优先用图示（Mermaid / SVG），不用成段文字描述。
- 实验曲线和指标一律出图，图放在报告旁边（例如 `docs/reports/figs/`），用相对路径嵌入。

### L3 HTML panel 层：主阅读面

- 项目已有 dashboard 就直接用，并给出链接。
- 没有 dashboard 时，生成单文件自包含 HTML：数据内联，不需要构建，没有外部依赖。文件放在报告旁边，给出 file:// 或线上链接，并在浏览器里打开预览。
- panel 内容：settings badge 区、主图、结论区。需要时加样本浏览器（例如模型输出并排对照）。

### L4 聊天框层：只留入口

- 聊天消息 = 名称 + 一句话结论 + panel 链接 + 报告文件链接。
- 不在聊天里贴报告正文，不在聊天里堆表格和数字清单。

## 领域示例：RL trial 分析

分析一次 RL 训练 run 时，四层这样落位（适用于有逐步日志的任何框架，例如 HF-Trainer 风格的 `log_history.json`）：

- **L4 聊天**：trial 名 + 一句话结论 + dashboard 地址（如果 dashboard 没有 URL 参数，说明要在下拉框里选哪个 run）+ 报告路径。panel 链接只放在聊天里，不写进报告。
- **L3 panel**：训练 dashboard，或者生成的静态 HTML panel。
- **L1 报告** `docs/reports/<trial>.md`：先用一段散文讲指标走势（reward、序列长度、截断率、clip ratio、entropy/KL、held-out 探针，不列条目）。然后是思维链分析：早期样本、中期长短样本对比、末期短样本，再加 think-vs-direct 对照臂。样本 ≤1000 字全文放出，更长的保留头、中、尾各约 500 字，并标明省略。分析结论最后写，少用表格和小节。
- **L2 图**：reward、completion length（带长度惩罚的 run 里它是主角）、clip ratio。可选 entropy/KL 和 held-out accuracy。`scripts/plot_run_metrics.py` 可以从任何 `log_history.json` 画出这些图。
- **采样纪律**：生成思维链样本时，条件必须和训练一致：同样的 temperature/top_p、同样的 thinking 开关、同样的 completion cap、held-out 题集。对照臂要选中期 checkpoint，那时思维链文本还会出现。末期模型已经自己跳过思考，两臂都接近直接作答，对照没有信息量。

完整示例和避坑清单见 `references/domain-example-rl-trial.md`。

## 致谢与前人工作

- [Karpathy 原帖](https://x.com/karpathy/status/2105819303471976479)（2026-10-02）：本 skill 实现的输出阶梯。
- [ASD-STE100 Issue 9](https://www.asd-ste100.org/)：L1 背后的受控语言标准。
- 调研过的开源实现（0xpili、ashryaagr、danyuchn、JAICHANGPARK、asdste100foragents.shop）见 `references/asd-ste100-80.md`。
- 英文版协议：`docs/SKILL.en.md`。
