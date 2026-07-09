# quantools Meta Workspace Design

Date: 2026-07-09

## Goal

Build `D:\quantools` as a meta workspace that connects qmtq, Qlib, VectorBT,
LEAN, and other open-source quant tools without mixing their source code into a
single project.

The workspace should make each tool easy to locate, run, upgrade, and audit.
The valuable custom code lives in adapters, scripts, documentation, and
protocol glue rather than in modified copies of third-party projects.

## Roles

```text
qmtq      = safety boundary, verified data protocol, run bundle, AI audit layer
Qlib      = factor, model, and ML research engine
VectorBT  = fast parameter sweep and idea screening lab
LEAN      = serious matching, order, portfolio, simulation, and execution engine
quantools = meta workspace that connects the tools without owning their cores
```

`D:\qmtq` remains an independent repository. The meta workspace links to it and
uses its public CLI/protocol artifacts. It must not copy qmtq internals into a
new combined source tree.

## Recommended Directory Layout

```text
D:\quantools\
  README.md
  config\
    workspace.yaml
  docs\
    architecture.md
    integration-map.md
    superpowers\
      specs\
        2026-07-09-quantools-meta-workspace-design.md
  externals\
    qlib\
    vectorbt\
    lean\
  adapters\
    qmtq_qlib\
    qmtq_vectorbt\
    qmtq_lean\
  scripts\
    check_workspace.ps1
    sync_qmtq.ps1
    run_qlib_exp.ps1
    run_vectorbt_sweep.ps1
    export_to_lean.ps1
```

Third-party projects under `externals\` are upstream checkouts or git
submodules. They are not edited as part of normal quantools work. Local changes
should be limited to adapters, scripts, and docs unless a deliberate upstream
fork is approved later.

## Linking Strategy

Use one of these modes per dependency:

1. Existing local path reference
   - qmtq starts this way: `qmtq_path: D:\qmtq`.
   - Best for an actively developed sibling repository.

2. Independent git checkout under `externals\`
   - Best for Qlib, VectorBT, LEAN, and other large open-source projects.
   - Keeps each upstream project easy to update and inspect.

3. Git submodule
   - Useful after the workspace needs reproducible pinned revisions.
   - Adds some git management overhead, so it should come after the layout is
     stable.

Windows junctions or symbolic links can be used when a project must stay in an
existing location, but the workspace config remains the source of truth.

## qmtq Boundary

qmtq is the protocol and safety judge:

- qmtq core must not import `xtquant`.
- qmtq core must not parse proprietary QMT `.DAT` files.
- External data must enter through staged manifests and admission checks before
  it can affect accepted research.
- Qlib features, labels, splits, and predictions must return as auditable ML
  experiment artifacts.
- VectorBT sweep results are screening evidence, not accepted qmtq results until
  converted into validated qmtq run bundles or review artifacts.
- LEAN results are execution-grade simulation artifacts, not a replacement for
  qmtq data-quality and review protocols.

## Adapter Contracts

Adapters should be thin, explicit, and file-oriented.

### `qmtq_qlib`

Input:

- qmtq-validated research data or staged ML experiment definitions.
- Declared universe, feature set, label, split, and point-in-time assumptions.

Output:

- Prediction files.
- ML experiment manifest.
- Training metrics and provenance.

qmtq validates the returned artifacts before predictions can influence accepted
signals or backtests.

### `qmtq_vectorbt`

Input:

- qmtq-validated price data exports.
- Parameter grid and strategy idea definition.

Output:

- Sweep table.
- Ranked candidate ideas.
- Diagnostic summary explaining which parameter regions are robust or fragile.

VectorBT is used for fast screening. Final acceptance still requires qmtq or
LEAN validation, depending on the target use.

### `qmtq_lean`

Input:

- qmtq-approved strategy specification.
- Data export compatible with LEAN import requirements.
- Portfolio, order, fee, slippage, and execution assumptions.

Output:

- LEAN backtest or paper/live simulation result bundle.
- Order and fill history.
- Portfolio/equity curve artifacts.

LEAN handles serious execution semantics. qmtq records the provenance and
review context around the result.

## First Implementation Slice

The first slice should avoid full integration complexity and only establish the
workspace skeleton:

1. Initialize `D:\quantools` as a meta workspace.
2. Move or link the existing Qlib checkout to `externals\qlib`.
3. Add placeholder directories for VectorBT and LEAN checkouts.
4. Add `config\workspace.yaml` with paths and ownership notes.
5. Add docs explaining the architecture and integration map.
6. Add a read-only `scripts\check_workspace.ps1` that verifies expected paths.

No adapter should train models, sweep strategies, execute trades, mutate qmtq
run artifacts, or call external providers in this first slice.

## Testing And Verification

The first slice is verified by:

- `scripts\check_workspace.ps1` confirming required paths exist.
- Git status showing only intentional workspace scaffold changes.
- Manual inspection that qmtq remains at `D:\qmtq` and Qlib remains a separate
  upstream checkout.

Future adapter work should add focused tests around artifact conversion and
protocol validation.

## First-Slice Decisions

- `externals\` starts with ordinary independent checkouts and path-based
  configuration, not git submodules.
- The existing Qlib checkout is moved into `externals\qlib` if the destination
  does not already exist.
- VectorBT and LEAN start as documented placeholders with setup notes. Actual
  clones happen in a later step after the skeleton validates cleanly.
- Adapter directories start as contract/documentation folders. They become
  Python packages only when the first real adapter implementation is approved.

## Recommendation

Start with ordinary independent checkouts and path-based configuration. Convert
to submodules only after the workspace layout and dependency versions stabilize.

Keep adapter packages minimal at first. The first valuable milestone is a clean,
auditable workspace map, not a deep integration layer.
