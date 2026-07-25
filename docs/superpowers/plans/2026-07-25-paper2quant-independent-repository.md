# Paper2Quant Independent Repository Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extract Paper2Quant into `gyfin/Paper2Quant` and replace its embedded quantools files with a pinned first-party submodule.

**Architecture:** Paper2Quant owns its Python package, tests, and version history in an independent repository. Quantools keeps the stable `packages/paper2quant` path as a relative-URL submodule, while qmtq remains a separate safety-boundary repository and only updates its handoff documentation.

**Tech Stack:** Git subtree, Git submodules, Python 3.10+, pytest, PowerShell

---

### Task 1: Record And Verify The Migration Baseline

**Files:**
- Create: `docs/superpowers/specs/2026-07-25-paper2quant-independent-repository-design.md`
- Create: `docs/superpowers/plans/2026-07-25-paper2quant-independent-repository.md`

- [ ] **Step 1: Confirm repository state**

Run:

```powershell
git status --short --branch
git ls-remote git@github.com:gyfin/Paper2Quant.git
```

Expected: quantools is clean and synchronized; the target repository is
reachable and has no refs.

- [ ] **Step 2: Run the embedded package baseline**

Run from `packages\paper2quant`:

```powershell
python -m pytest -q
python -m paper2quant.cli --help
```

Expected: two tests pass and CLI help exits successfully.

- [ ] **Step 3: Validate and commit the design**

Run:

```powershell
git diff --check
rg -n "T[B]D|T[O]DO|implement[ ]later|fill[ ]in" docs\superpowers\specs\2026-07-25-paper2quant-independent-repository-design.md docs\superpowers\plans\2026-07-25-paper2quant-independent-repository.md
git add docs\superpowers
git commit -m "docs: design standalone Paper2Quant repository"
```

Expected: no whitespace or placeholder errors and one documentation commit.

### Task 2: Initialize The Paper2Quant Remote

**Files:**
- Extract prefix: `packages/paper2quant`
- Push remote: `git@github.com:gyfin/Paper2Quant.git`

- [ ] **Step 1: Create a subtree split commit**

Run:

```powershell
$split = (git subtree split --prefix=packages/paper2quant).Trim()
git ls-tree -r --name-only $split
```

Expected: the tree has eight tracked files rooted at `.gitignore`, `README.md`,
`pyproject.toml`, `paper2quant/`, and `tests/`; it has no `packages/` prefix.

- [ ] **Step 2: Push the split commit**

Run:

```powershell
git push git@github.com:gyfin/Paper2Quant.git "${split}:refs/heads/main"
git ls-remote git@github.com:gyfin/Paper2Quant.git refs/heads/main
```

Expected: remote `main` resolves to the split commit.

### Task 3: Prepare The Standalone Checkout

**Files:**
- Preserve: `local-backups/paper2quant-pre-submodule-20260725`
- Clone: `packages/paper2quant`
- Modify in Paper2Quant: `README.md`
- Modify in Paper2Quant: `pyproject.toml`

- [ ] **Step 1: Preserve the embedded working directory**

Verify the resolved source and backup paths are under `D:\quantools`, then move
`packages\paper2quant` to
`local-backups\paper2quant-pre-submodule-20260725`.

- [ ] **Step 2: Stage removal of embedded files**

Run:

```powershell
git add -u -- packages/paper2quant
```

Expected: the eight embedded project files are staged as deletions.

- [ ] **Step 3: Clone the standalone repository**

Run:

```powershell
git clone --branch main git@github.com:gyfin/Paper2Quant.git packages\paper2quant
```

Expected: the checkout HEAD equals remote `main`.

- [ ] **Step 4: Add standalone repository metadata**

Update the README to identify Paper2Quant as a standalone gyfin project and add
test and installation commands. Add these project URLs to `pyproject.toml`:

```toml
[project.urls]
Repository = "https://github.com/gyfin/Paper2Quant"
Issues = "https://github.com/gyfin/Paper2Quant/issues"
```

- [ ] **Step 5: Test, commit, and push Paper2Quant**

Run inside `packages\paper2quant`:

```powershell
python -m pytest -q
python -m paper2quant.cli --help
git diff --check
git add README.md pyproject.toml
git commit -m "docs: prepare standalone Paper2Quant repository"
git push origin main
```

Expected: two tests pass and local `main` matches `origin/main`.

### Task 4: Register The First-Party Submodule

**Files:**
- Modify: `.gitmodules`
- Replace: `packages/paper2quant` with a mode `160000` gitlink
- Create: `packages/README.md`
- Modify: `externals/README.md`
- Modify: `docs/superpowers/specs/2026-07-25-reproducible-externals-design.md`

- [ ] **Step 1: Register the existing checkout**

Run:

```powershell
git submodule add --force ../Paper2Quant.git packages/paper2quant
```

Expected: `.gitmodules` stores the relative URL and the index stores a gitlink
at the current Paper2Quant commit.

- [ ] **Step 2: Document first-party package ownership**

Add `packages/README.md`, update `externals/README.md`, and mark the former
"tracked normally" Paper2Quant statement in the externals design as superseded.

- [ ] **Step 3: Verify all submodules**

Run:

```powershell
git submodule sync --recursive
git submodule update --init --recursive
git submodule status --recursive
git ls-files --stage packages/paper2quant
```

Expected: 13 initialized submodules in total, with Paper2Quant mode `160000` and
the original 12 external pins unchanged.

### Task 5: Update qmtq Handoff Documentation

**Files:**
- Modify: `D:\qmtq\HANDOFF.md`

- [ ] **Step 1: Replace the obsolete path**

Record:

```text
D:\quantools\packages\paper2quant
git@github.com:gyfin/Paper2Quant.git
```

State that quantools pins the consumed revision and retain the existing safety
limitations.

- [ ] **Step 2: Commit only HANDOFF**

Run:

```powershell
git -C D:\qmtq diff --check -- HANDOFF.md
git -C D:\qmtq add HANDOFF.md
git -C D:\qmtq commit -m "docs: update standalone Paper2Quant location"
```

Expected: `.codex-remote-attachments/` remains untracked and unstaged.

### Task 6: Verify And Publish

**Files:**
- Verify: Paper2Quant repository
- Verify: quantools repository
- Verify: qmtq repository

- [ ] **Step 1: Run final package and submodule checks**

Run Paper2Quant tests and verify the gitlink, relative URL, clean submodule
status, manifest consistency, and unchanged 12 external commits.

- [ ] **Step 2: Commit quantools**

Run:

```powershell
git add .gitmodules packages externals\README.md docs\superpowers
git diff --cached --check
git commit -m "chore: track Paper2Quant as first-party submodule"
```

Expected: Paper2Quant source blobs are removed from quantools and replaced by
one mode `160000` entry.

- [ ] **Step 3: Push qmtq and quantools**

Fetch each remote, verify it is an ancestor of the corresponding local branch,
then run:

```powershell
git -C D:\qmtq push origin main
git push origin master
```

- [ ] **Step 4: Verify all remotes**

Expected:

- `Paper2Quant/main` matches the Paper2Quant checkout.
- `quantools/master` matches the quantools checkout.
- `qmtq/main` matches the qmtq checkout.
- quantools is clean; qmtq retains only its pre-existing untracked attachment
  directory.
