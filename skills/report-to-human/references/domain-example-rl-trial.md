# Domain example: RL trial analysis report

A worked example of applying the 4-layer protocol to an RL training run. Assumes per-step training logs (for example a HF-Trainer-style `log_history.json`) and optional held-out evaluations. Everything here is framework-agnostic; paths are relative to your project.

## Report structure (mapped to the 4 layers)

1. **Trial name + panel link (L4)**. The report document states only the trial name. The panel link goes into the chat message, never into the document.
2. **One prose paragraph on metric trends (L1)**. Cover reward, completion length, truncation rate, clip ratio, entropy/KL, plus held-out probes if they exist. One paragraph, no bullet lists, STE sentence discipline.
3. **Main figures (L2)**. Reward curve, completion-length curve (the protagonist in runs with a length-cap penalty — always include it), clip ratio. Optional: entropy/KL, held-out accuracy. Figures live in `docs/reports/figs/`, embedded by relative path. Use `scripts/plot_run_metrics.py`.
4. **Chain-of-thought analysis (the core, L1 + L3 sample browser)**:
   - Early CoT: the init model or the earliest checkpoint. Watch out for `save_total_limit` rotation — early checkpoints are often deleted; reproduce step-0 behavior from the init model instead.
   - Mid-training CoT at the point where completion length drops sharply: **show both long and short samples**.
   - Final stable short CoT.
   - Sampling must match training conditions: same temperature/top_p (usually T=1.0), same thinking flag (for example `enable_thinking=True`), same completion cap, held-out question set.
   - **Contrast arm (strongly recommended)**: run think-on vs think-off (or CoT vs direct) on the same checkpoint with identical sampling and paired win/loss counting. Pick a checkpoint where CoT text still appears (mid-training). A late checkpoint that already self-skips makes both arms degenerate to direct answers.
5. **Sample quoting rule**. Quote samples in full when ≤ 1000 characters. For longer samples keep head/middle/tail ~500 characters each and mark the elision explicitly (`…(N characters elided)…`).
6. **Analysis prose, written last (L1)**. Minimal tables and subsections. Short. Written for a human reader.

## Panel notes (L3)

- If your training framework ships a dashboard, run it and link it. Note in chat how to select the run when the dashboard has no URL parameters (dropdown + localStorage is common).
- Dashboards that filter runs by minimum step count can silently hide short trials — check the filter first when a run "disappears".
- For local-only clusters, an SSH tunnel (`ssh -f -N -L <port>:localhost:<port> <host>`) is usually enough. Do not combine it with forwarding-failure options that tear the tunnel down on harmless warnings.
- When no dashboard exists, generate a single self-contained HTML panel: settings chips, main curves, conclusions, and a CoT sample browser with the contrast arm side by side.

## Pitfall checklist

- **Reward is not accuracy.** With mixed-format rewards (for example truncated / unparseable / wrong / correct mapped to different values), per-step reward is not comparable across steps if the training pool serves questions in blocks.
- **Mean completion length is dragged by the long tail.** Report the median or the distribution, not only the mean.
- **"Empty think + direct answer" is behavioral evidence only.** It does not prove the model computes nothing internally. Keep the wording precise about which of the two claims you make.
- **Mid-training "long-CoT resurgences"** (truncation rate ticking back up on some steps) deserve a separate callout. They are often degenerate-token repetition attractors, not recovered reasoning — inspect long samples for repetition patterns first.
- **Check whether CoT is question-specific** (quotes content of the actual question) or generic boilerplate. Answers contradicting their own "analysis", broken answer formats, and language drift (switching between languages) are evidence of templating, not reasoning.
- **Report the letter-collapse baseline for held-out multiple-choice** (accuracy of always picking A). A single accuracy number without it is meaningless.
- **Precomputed no-CoT contrast fields may be empty** (field present, values never filled). Count non-empty entries before using them; if empty, run your own contrast arm.
- **Length-bucketed accuracy** (≤20 / 21–100 / 101–500 / >500 think tokens) is the cheapest test of "does the CoT carry the answer". A negative correlation suggests think text traces confusion rather than reasoning. Confound: hard questions naturally induce longer output; read this together with the boilerplate evidence.
- **Base-model slices under a completion cap are usually near-all-wrong** (truncation = no valid answer). When reporting per-slice correct counts, attach the truncation count, and parse `<answer>` tags programmatically instead of eyeballing.
