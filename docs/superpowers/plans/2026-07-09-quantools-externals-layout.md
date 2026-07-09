# quantools Externals Layout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Put the required open-source quant libraries under the agreed `D:\quantools\externals` structure without committing third-party source into the root meta repository.

**Architecture:** `D:\quantools` remains a meta repository. Third-party projects live as independent git checkouts under `externals\`, while the root repository tracks only workspace docs, config, adapter contracts, and scripts.

**Tech Stack:** Git, PowerShell, independent upstream checkouts for Qlib, VectorBT, and LEAN.

---

### Task 1: Protect Root Repository Tracking

**Files:**
- Create: `.gitignore`

- [ ] **Step 1: Add root ignore rules**

```gitignore
/.worktrees/
/externals/
/OSkhQuant-main/
```

- [ ] **Step 2: Verify root status**

Run: `git status --short --branch`

Expected: `.gitignore` and this plan are tracked changes; third-party source
directories are not staged.

### Task 2: Create External Source Layout

**Files:**
- Directory: `externals\qlib`
- Directory: `externals\vectorbt`
- Directory: `externals\lean`

- [ ] **Step 1: Create `externals`**

Run: `New-Item -ItemType Directory -Force -Path .\externals`

- [ ] **Step 2: Move existing Qlib checkout**

Run: move `D:\quantools\Qlib` to `D:\quantools\externals\qlib` only if the
source exists and the destination does not exist.

- [ ] **Step 3: Clone VectorBT**

Run: `git clone https://github.com/polakowo/vectorbt.git .\externals\vectorbt`

- [ ] **Step 4: Clone LEAN**

Run: `git clone https://github.com/QuantConnect/Lean.git .\externals\lean`

### Task 3: Verify External Checkouts

**Files:**
- Read: `externals\qlib\.git`
- Read: `externals\vectorbt\.git`
- Read: `externals\lean\.git`

- [ ] **Step 1: Verify git remotes**

Run:

```powershell
git -C .\externals\qlib remote -v
git -C .\externals\vectorbt remote -v
git -C .\externals\lean remote -v
```

Expected:

- Qlib remote points to `github.com:microsoft/qlib.git` or `github.com/microsoft/qlib.git`.
- VectorBT remote points to `github.com/polakowo/vectorbt.git`.
- LEAN remote points to `github.com/QuantConnect/Lean.git`.

- [ ] **Step 2: Verify root repository remains clean except workspace files**

Run: `git status --short --branch`

Expected: root status shows only intentional meta-workspace files, not the full
third-party source trees.
