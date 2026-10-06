#!/usr/bin/env python3
"""Plot RL run metrics from a trainer log_history.json: reward, seqlen, clip.

Usage:
  python plot_run_metrics.py --log-history log_history.json \
      --out-dir docs/reports/figs --prefix myrun \
      --eval "61:0.33" "91:0.32" "144:0.47"        # optional held-out probes
      --title "my_trial_cap8k"

Produces <prefix>_reward.png, <prefix>_seqlen.png, <prefix>_clip.png.
Requires matplotlib; no other deps.
"""
import argparse
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


def roll(xs, w=10):
    out = []
    for i in range(len(xs)):
        lo = max(0, i - w + 1)
        out.append(sum(xs[lo:i + 1]) / (i + 1 - lo))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log-history", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--prefix", default="run")
    ap.add_argument("--title", default="")
    ap.add_argument("--eval", nargs="*", default=[],
                    help="held-out probes as step:acc, e.g. 61:0.33 144:0.47")
    a = ap.parse_args()

    H = json.load(open(a.log_history))
    rows = [d for d in H if "reward" in d and "completions/mean_length" in d]
    step = [d["step"] for d in rows]
    rew = [d["reward"] for d in rows]
    meanlen = [d["completions/mean_length"] for d in rows]
    trunc = [d.get("completions/clipped_ratio", 0) for d in rows]
    low = [d.get("clip_ratio/low_mean", 0) for d in rows]
    high = [d.get("clip_ratio/high_mean", 0) for d in rows]
    ent = [d.get("entropy", 0) for d in rows]
    kl = [d.get("kl", 0) for d in rows]
    evals = [tuple(x.split(":")) for x in a.eval]
    os.makedirs(a.out_dir, exist_ok=True)
    T = a.title or a.prefix

    # --- reward + held-out
    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=150)
    ax.plot(step, rew, color="#9ecae1", lw=0.8, label="reward / step")
    ax.plot(step, roll(rew), color="#1f77b4", lw=1.8, label="reward (roll-10)")
    ax.axhline(0, color="#999", lw=0.6, ls=":")
    for s, acc in evals:
        ax.scatter([int(s)], [float(acc)], marker="*", s=90, color="#d62728", zorder=5)
        ax.annotate(f"held-out acc {float(acc):.2f}", (int(s), float(acc)),
                    textcoords="offset points", xytext=(6, 8), fontsize=8, color="#d62728")
    ax.set_xlabel("step"); ax.set_ylabel("reward"); ax.set_title(f"{T} — training reward + held-out probes")
    ax.legend(loc="lower right", fontsize=8); fig.tight_layout()
    fig.savefig(os.path.join(a.out_dir, f"{a.prefix}_reward.png")); plt.close(fig)

    # --- seqlen (log) + truncation
    fig, ax = plt.subplots(figsize=(8, 4.2), dpi=150)
    ax.plot(step, meanlen, color="#9467bd", lw=1.2, label="completions/mean_length")
    ax.set_yscale("log")
    ax.set_xlabel("step"); ax.set_ylabel("mean completion tokens (log)")
    ax2 = ax.twinx()
    ax2.plot(step, trunc, color="#d62728", lw=1.0, alpha=0.8, label="truncated ratio")
    ax2.set_ylabel("truncated ratio", color="#d62728"); ax2.tick_params(axis="y", colors="#d62728")
    ax2.set_ylim(0, 1)
    ax.set_title(f"{T} — completion length vs cap + truncation penalty")
    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper right", fontsize=8)
    fig.tight_layout(); fig.savefig(os.path.join(a.out_dir, f"{a.prefix}_seqlen.png")); plt.close(fig)

    # --- clip ratios + entropy/kl
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), dpi=150)
    ax = axes[0]
    ax.plot(step, low, color="#1f77b4", lw=1.1, label="clip_ratio/low_mean")
    ax.plot(step, high, color="#ff7f0e", lw=1.1, label="clip_ratio/high_mean")
    ax.set_xlabel("step"); ax.set_ylabel("fraction"); ax.set_yscale("log")
    ax.legend(fontsize=8); ax.set_title(f"{T} — sequence clip ratios")
    ax = axes[1]
    ax.plot(step, ent, color="#2ca02c", lw=1.1, label="entropy")
    ax.set_xlabel("step"); ax.set_ylabel("entropy", color="#2ca02c")
    ax2 = ax.twinx()
    ax2.plot(step, kl, color="#888", lw=1.0, ls="--", label="kl")
    ax2.set_ylabel("kl", color="#888")
    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, fontsize=8); ax.set_title(f"{T} — entropy / KL")
    fig.tight_layout(); fig.savefig(os.path.join(a.out_dir, f"{a.prefix}_clip.png")); plt.close(fig)
    print("figures written:", a.prefix, "->", a.out_dir)


if __name__ == "__main__":
    main()
