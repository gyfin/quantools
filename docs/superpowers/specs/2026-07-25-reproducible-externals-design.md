# Reproducible Externals Design

## Status

Approved on 2026-07-25. This design supersedes the initial bootstrap decision
in `2026-07-09-quantools-meta-workspace-design.md` to keep `externals/` as
ignored independent checkouts.

## Problem

Ignoring all of `externals/` keeps the root repository small, but it also hides
the dependency inventory, upstream locations, and selected revisions. A clone
of `quantools` cannot reconstruct the research workspace without separate
manual knowledge.

Committing third-party source directly into the root repository would solve the
visibility problem at a high cost. The current checkouts include large histories
and assets, with `QuantsPlaybook` alone occupying roughly 2 GB locally. Vendoring
those files would duplicate upstream history and make upstream updates difficult
to review.

## Goals

- Make every approved third-party dependency visible from the root repository.
- Pin every dependency to the exact revision currently present in the workspace.
- Allow a new clone to populate dependencies with standard Git commands.
- Keep third-party histories separate from first-party `quantools` code.
- Preserve local work during migration.
- Keep generated caches, logs, models, and datasets out of the root history.

## Non-Goals

- Forking or modifying upstream projects as part of this migration.
- Updating dependencies to newer upstream revisions.
- Moving the independent `D:\qmtq` repository into `quantools`.
- Running or trusting third-party research agents automatically.

## Ownership Model

The workspace has three ownership classes:

1. **First-party workspace code**
   - Tracked normally by the `quantools` repository.
   - Includes documentation and `packages/paper2quant`.

2. **Pinned third-party source**
   - Tracked as Git submodules below `externals/`.
   - The root repository records the upstream URL and exact commit.
   - Local edits inside a submodule remain visible as a dirty submodule and are
     never silently folded into the root repository.

3. **Independent sibling systems**
   - `D:\qmtq` remains a separate repository and safety boundary.
   - Integration uses documented paths and adapter contracts.

## Target Layout

```text
D:\quantools
  .gitmodules
  .gitignore
  docs\
  packages\
    paper2quant\
  externals\
    README.md
    manifest.yaml
    qlib\
    vectorbt\
    lean\
    Kronos\
    QuantsPlaybook\
    oskhquant\
    agent-hosts\
      kimi-cli\
      kimi-code\
    research-intake\
      cangjie-skill\
      paper2agent\
      paper2code\
      rd-agent\
```

## Submodule Inventory

The migration preserves the revisions already checked out on 2026-07-25:

| Path | Upstream | Pinned commit |
| --- | --- | --- |
| `externals/qlib` | `https://github.com/microsoft/qlib.git` | `d5379c520f66a39953bad76234a7019a72796fd0` |
| `externals/vectorbt` | `https://github.com/polakowo/vectorbt.git` | `e0e8460dd90aaa0034ee3cffb94bb8de2511358f` |
| `externals/lean` | `https://github.com/QuantConnect/Lean.git` | `e709e62b806c98a766bf7ac3fa1b7fd53272a073` |
| `externals/Kronos` | `https://github.com/shiyu-coder/Kronos.git` | `67b630e67f6a18c9e9be918d9b4337c960db1e9a` |
| `externals/QuantsPlaybook` | `https://github.com/hugo2046/QuantsPlaybook.git` | `87163521c75629a3466564c017ac734a236a9ce4` |
| `externals/oskhquant` | `https://github.com/khscience/OSkhQuant.git` | `7228f55741b445cb25116683e5753f82a5422825` |
| `externals/agent-hosts/kimi-cli` | `https://github.com/MoonshotAI/kimi-cli.git` | `2c34efbbc6c7cfe40770623281e87c138ff8eb6c` |
| `externals/agent-hosts/kimi-code` | `https://github.com/MoonshotAI/kimi-code.git` | `f17a6ecb52907ffabf67a26de65df89572ac515a` |
| `externals/research-intake/cangjie-skill` | `https://github.com/kangarooking/cangjie-skill.git` | `1af4df346114e5a44755e3a6a2d9dd5478ad137b` |
| `externals/research-intake/paper2agent` | `https://github.com/jmiao24/Paper2Agent.git` | `e573687e15f345e3f375cd0851373d588e436be3` |
| `externals/research-intake/paper2code` | `https://github.com/going-doer/paper2code.git` | `ba9169978043d5799c8d4f4a0963e6b66a24c2e1` |
| `externals/research-intake/rd-agent` | `https://github.com/microsoft/RD-Agent.git` | `4f9ecb005881cddc08df0124a2e894c018007679` |

The root gitlinks are the authoritative version pins. `manifest.yaml` describes
roles and policy without duplicating mutable commit fields.

## Local Snapshot Handling

`externals/oskhquant` arrived as a source archive rather than a Git checkout.
A file-by-file audit against upstream commit
`7228f55741b445cb25116683e5753f82a5422825` found identical normalized content;
the only byte differences were line endings or byte-order marks. The original
snapshot is retained in a local migration backup until verification completes,
then the path is replaced by a real checkout of that upstream revision.

`externals/research-intake/paper2quant` has no upstream Git metadata and is
first-party integration code for qmtq research-source protocols. It moves to
`packages/paper2quant` and is tracked normally, including its tests.

## Ignore Policy

The root rule `/externals/` is removed. The root ignore file covers only local
workspace machinery and migration backups. Package-specific Python caches remain
ignored by `packages/paper2quant/.gitignore`. Each submodule applies its own
upstream ignore policy internally.

This makes an unexpected new directory under `externals/` visible to
`git status` instead of silently hiding it.

## Dependency Operations

Populate all dependencies after cloning:

```powershell
git clone --recurse-submodules git@github.com:gyfin/quantools.git
```

Populate dependencies in an existing clone:

```powershell
git submodule sync --recursive
git submodule update --init --recursive
```

Inspect exact revisions and local drift:

```powershell
git submodule status --recursive
git status --short
```

Dependency updates are deliberate root-repository changes. Update one submodule,
review its upstream delta, test integrations, and commit the new gitlink. Do not
use an unreviewed bulk `git submodule update --remote`.

## Verification

The migration is accepted when:

- `.gitmodules` contains exactly the approved inventory.
- Every external path is stored by the root repository with mode `160000`.
- `git submodule status --recursive` reports every path initialized at its pinned
  commit, with no missing, dirty, or merge-conflict prefix.
- `paper2quant` tests pass from its new first-party path.
- `git status --ignored` proves `externals/` itself is no longer ignored.
- The root repository can commit and push the metadata without adding
  third-party blobs to its object database.
