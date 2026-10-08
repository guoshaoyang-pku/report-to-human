---
name: blog-deploy
description: >
  Deploy project documents (HTML/markdown) to a GitHub Pages personal site and
  report the live URL. Use when finishing a document/report/panel that needs to
  go online, when asked to "上线/发布/部署" a doc, or when a docs/ artifact should
  be synced to the personal homepage. Covers copying local docs/ files into the
  Pages repo, committing, pushing the build branch, waiting for Pages rebuild,
  and verifying HTTP 200 before reporting success.
---

# Blog Deploy

Publish a single-file artifact from the local project `docs/` directory to a
GitHub Pages site, then verify the page is live and report the URL.

## Locate the Pages repo

Ask once, then remember: the local clone of the GitHub Pages repo (for example
`~/workdir/<user>.github.io`) and the branch Pages builds from (usually `main`;
pushing it auto-triggers a rebuild, no gh-pages branch needed). Destination
subdirectory (for example `blogs/`) and the online URL pattern
`https://<user>.github.io/<dest>/<filename>` follow from it.

## Deployment workflow

### Step 1: Confirm source artifact

Confirm the file exists in the local project `docs/` (single-file artifact
discipline — do not scatter drafts). If it lives elsewhere, decide with the user
whether to move it into `docs/` first.

### Step 2: Copy into the Pages repo

Copy (not move) so the local `docs/` copy stays canonical:

```bash
cp <project>/docs/<file> <BLOG_REPO>/<dest>/<file>
```

### Step 3: Commit and push

Stage only the target file(s) — never touch unrelated untracked directories:

```bash
cd <BLOG_REPO>
git add <dest>/<file>
git commit -m "blog(<dir>): <what changed>"
git push origin <build-branch>
```

### Step 4: Verify deployment

Pages rebuild takes about a minute. Then confirm live:

```bash
sleep 60 && curl -s -o /dev/null -w "%{http_code}" "https://<user>.github.io/<dest>/<file>"
```

**A deployment is only complete when the URL returns 200.** If it returns
404/000, wait and retry; if still failing, report the blocker (do not claim success).

### Step 5: Report

Report the online URL as a markdown link and summarize what changed. Optionally
open it in the embedded browser for preview.

## Rules

- Do not push project-internal notes (for example `agent.md`) to the Pages repo.
- Stage only intended files; leave other untracked files untouched.
- Verify before reporting: HTTP 200 is the completion criterion.
- If the local `docs/` file and the Pages copy diverge, re-copy from `docs/`.
