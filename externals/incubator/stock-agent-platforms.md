# Stock Agent Platforms Intake

Date: 2026-08-04

## Candidates

| Project | Pinned revision | License finding | Initial decision |
| --- | --- | --- | --- |
| qilihei/StockAgent | `82fbd6619e92e79172756d7c689bb1ec5dc0f8b6` | MIT repository license; transitive content and service terms pending | `incubating`, `reference_only`, `pending_review` |
| MingyuJ666/Stockagent | `e2a9c052b81694067b1dbed4ccf39be9ab7f392c` | No repository license found; code use and extraction blocked | `incubating`, `reference_only`, `pending_review` |
| ValueCell-ai/valuecell | `9793e9c0563fbf56fc096757d8bb80e209ac7aab` | Apache-2.0 repository license with third-party-component caveat | `incubating`, `reference_only`, `pending_review` |

The v1 manifest is an inventory, not an approval catalog. Pinning records the
source reviewed on this date; it does not approve installation, execution, or
reuse.

## Capability Comparison

qilihei/StockAgent is primarily an A-share full-stack reference: market and
financial data adapters, multi-source news collection, factor definitions,
backtest structure, reports, tool schemas, and a web application. Its named
MCP node is an internal Redis request protocol, not a standards-compliant MCP
transport. Broad lower-bound dependencies, stateful infrastructure, and
destructive maintenance scripts prevent direct execution during intake.

MingyuJ666/Stockagent is a compact academic simulation of LLM investor
behavior under market and external-event conditions. Its useful contribution
is experimental methodology, prompt structure, leakage controls, and behavior
analysis. It has no automated tests and no repository license at the pinned
revision, so it is not a runnable dependency or reusable code source.

ValueCell is the strongest engineering reference for financial-agent
registration, orchestration, A2A wrapping, model-provider configuration,
persistence, tests, and frontend integration. It also contains exchange
credential handling and live cryptocurrency order routing. Trading and secret
paths are excluded from quantools and must never receive qmtq or production
credentials.

## Intended Learning Targets

- qilihei/StockAgent: A-share workflow decomposition and narrow read-only tool schemas.
- MingyuJ666/Stockagent: point-in-time multi-agent simulation methodology and leakage controls.
- ValueCell: agent registry, orchestration, A2A, provider, persistence, and application-shell patterns.

These are learning targets, not approved code-extraction targets.

## Prohibited Use

- No installation, import, service startup, Docker startup, or global Skill registration.
- No QMT, brokerage, exchange, LLM, data-provider, database, or webhook credentials.
- No writing accepted qmtq state, accepted signals, or order instructions.
- No code copying from MingyuJ666/Stockagent while its license is absent.
- No live or paper exchange execution from ValueCell.

## Promotion Gates

- Complete repository and transitive-license review.
- Inspect dependencies, network behavior, secrets, destructive scripts, and prompt-injection surfaces.
- Build offline point-in-time fixtures with future-data leakage checks.
- Compare against Qlib, VectorBT, LEAN, Paper2Quant, and qmtq to avoid duplicate authority.
- Define a first-party versioned adapter contract with deterministic outputs.
- Require qmtq validation and explicit human approval.
