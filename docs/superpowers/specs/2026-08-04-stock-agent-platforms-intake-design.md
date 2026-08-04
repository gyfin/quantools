# Stock Agent Platforms Controlled Intake Design

Date: 2026-08-04

## 1. Goal

Add three upstream financial-agent repositories to the `quantools` managed
external tree without treating them as trusted dependencies or allowing them
to enter the qmtq validation and execution boundary:

- `qilihei/StockAgent`
- `MingyuJ666/Stockagent`
- `ValueCell-ai/valuecell`

The intake fixes exact upstream revisions, records provenance and license
status, and produces an auditable comparison. It does not install, start, or
adapt the projects in this phase.

## 2. Decision

Use the existing controlled-incubation model:

```text
discover -> register -> pin -> inspect -> evaluate -> approve or retire
```

All three projects enter as `incubating` and `reference_only`. Pinning a
repository records what was reviewed; it does not make the code trusted.
The manifest remains an inventory-only v1 registry, so every candidate also
has `approval_status: pending_review`; none is an approved capability.

The alternatives were rejected for this phase:

- Direct installation would expose the workspace to unbounded dependency,
  network, credential, and execution behavior before an adapter contract
  exists.
- Copying selected source would obscure provenance and create license and
  maintenance risk.

## 3. Pinned Sources and Paths

The root repository will add Git submodules at capability-oriented paths:

| Project | Path | Reviewed upstream revision | Initial role |
| --- | --- | --- | --- |
| qilihei/StockAgent | `externals/a-share-research/qilihei-stockagent` | `82fbd6619e92e79172756d7c689bb1ec5dc0f8b6` | A-share data, news, factor, backtest, and agent-platform reference |
| MingyuJ666/Stockagent | `externals/simulation-engines/mingyu-stockagent` | `e2a9c052b81694067b1dbed4ccf39be9ab7f392c` | LLM investor-behavior and market-simulation research reference |
| ValueCell-ai/valuecell | `externals/agent-platforms/valuecell` | `9793e9c0563fbf56fc096757d8bb80e209ac7aab` | Financial-agent orchestration, registry, A2A, and application-shell reference |

The `.gitmodules` URLs and root gitlinks are authoritative. The manifest
duplicates no revision field because `policy.revision_source` is
`root_gitlink`.

## 4. Registry Metadata

`externals/manifest.yaml` will register each component with:

- `trust_class: untrusted_third_party_financial_agent`
- `lifecycle: incubating`
- `integration_mode: reference_only`
- `approval_status: pending_review`

License records differ by project:

| Project | Repository license result | Intake consequence |
| --- | --- | --- |
| qilihei/StockAgent | MIT license present at the reviewed revision | Repository code may be evaluated; transitive content and service terms remain pending |
| MingyuJ666/Stockagent | No repository license found at the reviewed revision | `NOASSERTION`; use, copying, modification, and adapter extraction remain blocked |
| ValueCell-ai/valuecell | Apache-2.0 license present, with an explicit third-party-components caveat | Repository code may be evaluated; bundled dependencies, APIs, widgets, and service terms require separate review |

Missing or incomplete license coverage does not prevent recording an upstream
gitlink as provenance, but it prevents code reuse and promotion.

## 5. Capability Assessment

### qilihei/StockAgent

Useful references include A-share data adapters, news collection, factor
definitions, backtest structure, report generation, and tool schemas. Its
component named `MCPNode` uses an internal Redis task protocol rather than a
standards-compliant MCP transport, so it cannot be treated as an existing
Paper2Quant or Codex MCP integration. Broad lower-bound dependencies, multiple
stateful services, destructive maintenance scripts, and limited automated
coverage make direct execution inappropriate during intake.

### MingyuJ666/Stockagent

The project is a compact research prototype for simulating LLM-driven investor
behavior and external events. It is useful for experimental design, leakage
controls, prompts, and behavior-analysis ideas. It has no automated test suite
and no repository license at the reviewed revision. It is therefore a research
paper/code reference only, not a runnable dependency or code source.

### ValueCell-ai/valuecell

The project provides the strongest engineering reference for agent registry,
orchestration, A2A wrapping, model-provider configuration, persistence,
frontend integration, and tests. It also contains live cryptocurrency trading,
exchange API-key and private-key handling, and order-routing code. Those paths
are explicitly outside the quantools/qmtq trust boundary and must not be run or
adapted during this phase.

## 6. Safety and Data Flow

The intake has no runtime data flow. The only flow is governance metadata:

```text
upstream repository
  -> reviewed commit hash
  -> root gitlink and manifest entry
  -> incubator assessment
  -> later human promotion decision
```

The three repositories must not:

- receive QMT, brokerage, exchange, LLM, data-provider, database, or webhook
  credentials;
- write qmtq accepted state or emit accepted signals;
- issue paper or live orders;
- be globally installed or imported by first-party packages;
- be started through Docker, PowerShell, shell, frontend, or Python entrypoints;
- access the network as part of intake verification.

## 7. Files Changed in the Intake

The implementation phase will modify only root-governance artifacts and
gitlinks:

- `.gitmodules`
- `externals/manifest.yaml`
- `externals/README.md`
- `externals/incubator/stock-agent-platforms.md`
- `docs/project-status.md`
- three new submodule gitlinks under the paths in section 3

No files inside existing submodules will be changed. The existing local
`packages/paper2quant` gitlink modification is outside this work and must not be
staged or committed.

## 8. Verification

Verification is structural and offline after the initial clones:

1. Confirm each submodule remote URL and checked-out commit match the design.
2. Confirm `.gitmodules` paths and URLs match manifest paths and upstreams.
3. Confirm every new entry contains lifecycle, integration, trust, and license
   metadata.
4. Confirm all incubating projects remain `reference_only` and global
   `live_qmt_access` remains `forbidden`.
5. Confirm documentation links resolve locally.
6. Confirm no third-party install, startup, test, or credentialed command was
   run.
7. Confirm the final staged set excludes `packages/paper2quant`.

## 9. Promotion Gates

Future promotion requires a separate approved design and all applicable gates:

- completed repository and transitive-license review;
- isolated dependency and network-behavior evaluation;
- secret-handling and destructive-operation review;
- reproducible fixtures with point-in-time data and leakage checks;
- comparison against existing Qlib, VectorBT, LEAN, Paper2Quant, and qmtq
  capabilities to avoid duplicate authority;
- a first-party narrow adapter with versioned input/output contracts;
- deterministic qmtq validation and explicit human approval.

The likely extraction targets are tool-schema and A-share workflow ideas from
qilihei/StockAgent, simulation methodology from MingyuJ666/Stockagent, and
orchestration/A2A patterns from ValueCell. None is approved for extraction by
this intake.
