# Paper2Quant Independent Repository Design

## Status

Approved on 2026-07-25.

This design supersedes only the Paper2Quant ownership decision in
`2026-07-25-reproducible-externals-design.md`. The third-party external
dependency design remains unchanged.

## Problem

Paper2Quant currently lives as ordinary first-party files inside the
`quantools` meta repository. It already has its own Python package metadata,
CLI, tests, safety boundary, and release version. Keeping it embedded couples
its lifecycle to workspace-only changes and makes reuse by qmtq or other
research environments less explicit.

The empty repository `git@github.com:gyfin/Paper2Quant.git` is available for a
standalone first-party component.

## Decision

Paper2Quant becomes an independent gyfin repository with `main` as its primary
branch. `quantools` retains the ergonomic path `packages/paper2quant`, but that
path becomes a Git submodule pinned to a reviewed Paper2Quant commit.

The submodule URL is recorded as:

```text
../Paper2Quant.git
```

The relative URL resolves through the clone protocol used for `quantools`:

- an SSH clone resolves to `git@github.com:gyfin/Paper2Quant.git`;
- an HTTPS clone resolves to `https://github.com/gyfin/Paper2Quant.git`.

No branch-tracking setting is stored in `.gitmodules`. The root gitlink remains
the authoritative version pin.

## Ownership Boundaries

- `externals/` contains pinned third-party projects.
- `packages/paper2quant` is a pinned first-party submodule.
- `D:\qmtq` remains an independent protocol, evidence, and safety repository.
- qmtq may invoke Paper2Quant explicitly, but Paper2Quant cannot write qmtq
  `research_cache`, approve experiments, produce accepted signals, or access
  live QMT credentials.

## Repository Extraction

The existing package history is extracted with `git subtree split` using
`packages/paper2quant` as the prefix. This produces a standalone tree whose
repository root contains:

```text
.gitignore
README.md
pyproject.toml
paper2quant\
tests\
```

The split commit is pushed to `Paper2Quant/main`. A follow-up standalone commit
may update repository metadata and reader-facing documentation without changing
the safety behavior.

The original working directory is retained under the ignored
`local-backups/` migration area until both remotes and tests are verified.

## Integration

After extraction, the root repository stores:

```text
packages\
  README.md
  paper2quant\  # mode 160000 gitlink
```

Initialize all first-party and third-party components with the existing command:

```powershell
git submodule sync --recursive
git submodule update --init --recursive
```

Paper2Quant changes are committed and pushed from inside its repository first.
The reviewed new commit is then recorded as a gitlink change in `quantools`.

## qmtq Documentation

`D:\qmtq\HANDOFF.md` is updated from the obsolete
`externals\research-intake\paper2quant` path to
`packages\paper2quant`. It records the standalone repository URL and states
that the version consumed by the workspace is pinned by `quantools`.

No qmtq runtime code or safety protocol changes in this migration.

## Verification

The migration is accepted when:

- `Paper2Quant/main` exists and contains only the standalone project tree.
- Paper2Quant tests pass from a fresh checkout.
- `packages/paper2quant` is mode `160000` in the `quantools` index.
- `.gitmodules` uses `../Paper2Quant.git` without a branch setting.
- the Paper2Quant submodule is clean and matches its root gitlink.
- all 12 existing third-party submodules remain unchanged and clean.
- qmtq HANDOFF names the new path and remote without staging unrelated files.
- Paper2Quant, quantools, and qmtq remotes match their corresponding local
  commits after push.
