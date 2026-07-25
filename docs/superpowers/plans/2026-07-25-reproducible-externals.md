# Reproducible Externals Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the blanket `externals/` ignore rule with pinned Git submodules while moving first-party `paper2quant` into the root repository.

**Architecture:** Third-party repositories remain independent upstream histories and are represented by root gitlinks plus `.gitmodules`. First-party protocol adapters are tracked normally under `packages/`, while `D:\qmtq` remains an independent sibling repository.

**Tech Stack:** Git submodules, PowerShell, YAML metadata, Python, pytest

---

### Task 1: Record the Migration Policy

**Files:**
- Create: `docs/superpowers/specs/2026-07-25-reproducible-externals-design.md`
- Create: `docs/superpowers/plans/2026-07-25-reproducible-externals.md`
- Modify: `docs/superpowers/specs/2026-07-09-quantools-meta-workspace-design.md`

- [ ] **Step 1: Add the approved design and implementation plan**

Document the ownership model, exact submodule inventory, local snapshot audit,
ignore policy, bootstrap commands, and acceptance checks.

- [ ] **Step 2: Mark the bootstrap decision as superseded**

Add this note below the title of the 2026-07-09 design:

```markdown
> **Status update (2026-07-25):** The initial ignored independent-checkout
> policy has been superseded by
> `2026-07-25-reproducible-externals-design.md`. Third-party repositories are
> now pinned as Git submodules.
```

- [ ] **Step 3: Validate the documents**

Run:

```powershell
git diff --check
rg -n "T[B]D|T[O]DO|implement[ ]later|fill[ ]in" docs\superpowers\specs\2026-07-25-reproducible-externals-design.md docs\superpowers\plans\2026-07-25-reproducible-externals.md
```

Expected: `git diff --check` exits successfully and the placeholder scan returns
no matches.

- [ ] **Step 4: Commit the approved migration documents**

Run:

```powershell
git add docs/superpowers
git commit -m "docs: design reproducible external dependencies"
```

Expected: one documentation commit with no external source staged.

### Task 2: Move First-Party Paper2Quant

**Files:**
- Move: `externals/research-intake/paper2quant` to `packages/paper2quant`
- Track: `packages/paper2quant/pyproject.toml`
- Track: `packages/paper2quant/paper2quant/*.py`
- Track: `packages/paper2quant/tests/test_builder.py`
- Track: `packages/paper2quant/.gitignore`

- [ ] **Step 1: Establish the test baseline**

Run:

```powershell
Push-Location externals\research-intake\paper2quant
try { python -m pytest -q } finally { Pop-Location }
```

Expected: two tests pass.

- [ ] **Step 2: Move the package without caches**

Move the project directory to `packages/paper2quant`. Keep `.pytest_cache`,
`__pycache__`, and `*.pyc` ignored and unstaged.

- [ ] **Step 3: Run tests at the new path**

Run:

```powershell
Push-Location packages\paper2quant
try { python -m pytest -q } finally { Pop-Location }
```

Expected: the same two tests pass.

### Task 3: Register Existing Git Checkouts as Submodules

**Files:**
- Create: `.gitmodules`
- Add gitlinks below: `externals/`

- [ ] **Step 1: Remove the blanket ignore rule**

Replace `.gitignore` with:

```gitignore
/.worktrees/
/local-backups/
```

- [ ] **Step 2: Register each existing clean checkout**

Run `git submodule add --force <url> <path>` for:

```text
https://github.com/microsoft/qlib.git externals/qlib
https://github.com/polakowo/vectorbt.git externals/vectorbt
https://github.com/QuantConnect/Lean.git externals/lean
https://github.com/shiyu-coder/Kronos.git externals/Kronos
https://github.com/hugo2046/QuantsPlaybook.git externals/QuantsPlaybook
https://github.com/MoonshotAI/kimi-cli.git externals/agent-hosts/kimi-cli
https://github.com/MoonshotAI/kimi-code.git externals/agent-hosts/kimi-code
https://github.com/kangarooking/cangjie-skill.git externals/research-intake/cangjie-skill
https://github.com/jmiao24/Paper2Agent.git externals/research-intake/paper2agent
https://github.com/going-doer/paper2code.git externals/research-intake/paper2code
https://github.com/microsoft/RD-Agent.git externals/research-intake/rd-agent
```

Expected: each existing checkout is added as a gitlink without changing its
checked-out commit.

- [ ] **Step 3: Canonicalize public submodule URLs**

Run:

```powershell
git config -f .gitmodules submodule.externals/qlib.url https://github.com/microsoft/qlib.git
git config -f .gitmodules submodule.externals/QuantsPlaybook.url https://github.com/hugo2046/QuantsPlaybook.git
git submodule sync --recursive
```

Expected: all public dependencies are clonable over HTTPS without requiring an
SSH identity.

### Task 4: Convert the Audited OSkhQuant Snapshot

**Files:**
- Replace local snapshot: `externals/oskhquant`
- Add gitlink: `externals/oskhquant`
- Preserve local backup: `local-backups/oskhquant-pre-submodule-20260725`

- [ ] **Step 1: Verify the snapshot audit result**

Compare all 55 upstream-tracked files against commit
`7228f55741b445cb25116683e5753f82a5422825`, normalizing UTF-8 byte-order marks
and line endings.

Expected: 14 files are byte-identical, 41 differ only by line endings or
byte-order marks, and no files are missing or extra.

- [ ] **Step 2: Preserve the original snapshot**

Move `externals/oskhquant` to
`local-backups/oskhquant-pre-submodule-20260725`. Verify the resolved source and
destination are both below `D:\quantools` before moving.

- [ ] **Step 3: Put the audited upstream checkout in place**

Use the audited clone of `https://github.com/khscience/OSkhQuant.git`, verify its
HEAD is `7228f55741b445cb25116683e5753f82a5422825`, and move it to
`externals/oskhquant`.

- [ ] **Step 4: Register OSkhQuant**

Run:

```powershell
git submodule add --force https://github.com/khscience/OSkhQuant.git externals/oskhquant
```

Expected: the root index contains a gitlink at the audited commit.

### Task 5: Add Reader-Facing Dependency Metadata

**Files:**
- Create: `externals/README.md`
- Create: `externals/manifest.yaml`

- [ ] **Step 1: Add the external dependency guide**

Explain ownership, initialization, status inspection, safe update procedure, and
the distinction between research inputs and trusted production code.

- [ ] **Step 2: Add the metadata manifest**

List every submodule with a stable identifier, path, upstream URL, functional
role, and trust class. Keep revision pins out of the manifest because root
gitlinks are authoritative.

### Task 6: Verify and Publish

**Files:**
- Verify: `.gitignore`
- Verify: `.gitmodules`
- Verify: `externals/manifest.yaml`
- Verify: `packages/paper2quant`

- [ ] **Step 1: Verify submodule registration**

Run:

```powershell
git submodule sync --recursive
git submodule update --init --recursive
git submodule status --recursive
git ls-files --stage externals
```

Expected: 12 initialized submodules, each root index entry uses mode `160000`,
and no status line begins with `-`, `+`, or `U`.

- [ ] **Step 2: Verify ignore behavior**

Run:

```powershell
git check-ignore -q externals
if ($LASTEXITCODE -eq 0) { throw "externals must not be ignored" }
git status --short --ignored
```

Expected: `externals` is not ignored; local backups and Python caches are
ignored.

- [ ] **Step 3: Verify first-party tests and repository hygiene**

Run:

```powershell
Push-Location packages\paper2quant
try { python -m pytest -q } finally { Pop-Location }
git diff --check
git status --short
```

Expected: two tests pass, no whitespace errors are reported, and only the
planned migration files are changed.

- [ ] **Step 4: Commit the migration**

Run:

```powershell
git add .gitignore .gitmodules externals packages docs
git commit -m "chore: pin external dependencies as submodules"
```

Expected: the commit contains 12 gitlinks, metadata, and first-party
`paper2quant`, but no vendored third-party blobs.

- [ ] **Step 5: Push and verify the remote**

Run:

```powershell
git push origin master
git status --short --branch
git rev-parse HEAD
git rev-parse origin/master
```

Expected: local `master` and `origin/master` resolve to the same commit and the
worktree is clean.
