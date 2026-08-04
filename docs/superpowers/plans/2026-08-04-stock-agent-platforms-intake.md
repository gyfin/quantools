# Stock Agent Platforms Controlled Intake Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Pin and register qilihei/StockAgent, MingyuJ666/Stockagent, and ValueCell-ai/valuecell as isolated, reference-only external capabilities in quantools.

**Architecture:** Each upstream remains an independent Git submodule at a capability-oriented path, while the root manifest owns trust, lifecycle, integration, and license metadata. An incubator record captures the comparative assessment and promotion gates; no third-party code is installed, started, imported, or given credentials.

**Tech Stack:** Git submodules, YAML registry, Markdown governance documents, PowerShell verification

---

## File Map

- Modify: `.gitmodules` — canonical upstream URLs and submodule paths.
- Create gitlink: `externals/a-share-research/qilihei-stockagent` — pinned qilihei/StockAgent checkout.
- Create gitlink: `externals/simulation-engines/mingyu-stockagent` — pinned MingyuJ666/Stockagent checkout.
- Create gitlink: `externals/agent-platforms/valuecell` — pinned ValueCell-ai/valuecell checkout.
- Modify: `externals/manifest.yaml` — governance metadata for all three projects.
- Modify: `externals/README.md` — ownership and safety summary.
- Create: `externals/incubator/stock-agent-platforms.md` — source-backed intake comparison and promotion gates.
- Modify: `docs/project-status.md` — current-state snapshot.
- Modify: `docs/superpowers/specs/2026-08-04-stock-agent-platforms-intake-design.md` — align the approved design with qmtq's inventory-only `pending_review` rule.
- Existing unrelated change: `packages/paper2quant` — never stage or commit as part of this plan.

### Task 1: Pin qilihei/StockAgent

**Files:**
- Modify: `.gitmodules`
- Create gitlink: `externals/a-share-research/qilihei-stockagent`

- [ ] **Step 1: Verify the reviewed revision is still reachable**

Run:

```powershell
git ls-remote https://github.com/qilihei/StockAgent.git HEAD
```

Expected: HEAD resolves to `82fbd6619e92e79172756d7c689bb1ec5dc0f8b6` at intake time. If it has moved, retain the reviewed revision and verify it exists after cloning; do not silently adopt the new HEAD.

- [ ] **Step 2: Add the submodule without running upstream code**

Run:

```powershell
git submodule add https://github.com/qilihei/StockAgent.git externals/a-share-research/qilihei-stockagent
git -C externals/a-share-research/qilihei-stockagent checkout --detach 82fbd6619e92e79172756d7c689bb1ec5dc0f8b6
```

Expected: the checkout reports detached HEAD at the reviewed commit. Do not install dependencies or invoke any repository script.

- [ ] **Step 3: Verify the URL and gitlink candidate**

Run:

```powershell
git config -f .gitmodules --get submodule.externals/a-share-research/qilihei-stockagent.url
git -C externals/a-share-research/qilihei-stockagent rev-parse HEAD
git -C externals/a-share-research/qilihei-stockagent status --short
```

Expected:

```text
https://github.com/qilihei/StockAgent.git
82fbd6619e92e79172756d7c689bb1ec5dc0f8b6
```

The final command must produce no output.

- [ ] **Step 4: Commit only the first pin**

Run:

```powershell
git add -- .gitmodules externals/a-share-research/qilihei-stockagent
git diff --cached --check
git diff --cached --name-only
git commit -m "chore: 固定 qilihei StockAgent 参考版本"
```

Expected staged names: only `.gitmodules` and `externals/a-share-research/qilihei-stockagent`. In particular, `packages/paper2quant` must not appear.

### Task 2: Pin MingyuJ666/Stockagent

**Files:**
- Modify: `.gitmodules`
- Create gitlink: `externals/simulation-engines/mingyu-stockagent`

- [ ] **Step 1: Verify the reviewed revision is reachable**

Run:

```powershell
git ls-remote https://github.com/MingyuJ666/Stockagent.git HEAD
```

Expected: HEAD resolves to `e2a9c052b81694067b1dbed4ccf39be9ab7f392c` at intake time. If it has moved, retain the reviewed revision and verify it exists after cloning; do not silently adopt the new HEAD.

- [ ] **Step 2: Add and detach at the reviewed revision**

Run:

```powershell
git submodule add https://github.com/MingyuJ666/Stockagent.git externals/simulation-engines/mingyu-stockagent
git -C externals/simulation-engines/mingyu-stockagent checkout --detach e2a9c052b81694067b1dbed4ccf39be9ab7f392c
```

Expected: detached HEAD at `e2a9c052b81694067b1dbed4ccf39be9ab7f392c`. Do not install its unpinned requirements or use its prompts/code.

- [ ] **Step 3: Verify URL, revision, and clean state**

Run:

```powershell
git config -f .gitmodules --get submodule.externals/simulation-engines/mingyu-stockagent.url
git -C externals/simulation-engines/mingyu-stockagent rev-parse HEAD
git -C externals/simulation-engines/mingyu-stockagent status --short
```

Expected URL `https://github.com/MingyuJ666/Stockagent.git`, the reviewed hash, and no status output.

- [ ] **Step 4: Commit only the second pin**

Run:

```powershell
git add -- .gitmodules externals/simulation-engines/mingyu-stockagent
git diff --cached --check
git diff --cached --name-only
git commit -m "chore: 固定 StockAgent 模拟参考版本"
```

Expected staged names: only `.gitmodules` and `externals/simulation-engines/mingyu-stockagent`.

### Task 3: Pin ValueCell

**Files:**
- Modify: `.gitmodules`
- Create gitlink: `externals/agent-platforms/valuecell`

- [ ] **Step 1: Verify the reviewed revision is reachable**

Run:

```powershell
git ls-remote https://github.com/ValueCell-ai/valuecell.git HEAD
```

Expected: HEAD resolves to `9793e9c0563fbf56fc096757d8bb80e209ac7aab` at intake time. If upstream moved, keep the reviewed revision.

- [ ] **Step 2: Add and detach at the reviewed revision**

Run:

```powershell
git submodule add https://github.com/ValueCell-ai/valuecell.git externals/agent-platforms/valuecell
git -C externals/agent-platforms/valuecell checkout --detach 9793e9c0563fbf56fc096757d8bb80e209ac7aab
```

Expected: detached HEAD at the reviewed revision. Do not execute `start.ps1`, `start.sh`, Docker, Python, frontend, exchange, or credential commands.

- [ ] **Step 3: Verify URL, revision, and clean state**

Run:

```powershell
git config -f .gitmodules --get submodule.externals/agent-platforms/valuecell.url
git -C externals/agent-platforms/valuecell rev-parse HEAD
git -C externals/agent-platforms/valuecell status --short
```

Expected URL `https://github.com/ValueCell-ai/valuecell.git`, the reviewed hash, and no status output.

- [ ] **Step 4: Commit only the third pin**

Run:

```powershell
git add -- .gitmodules externals/agent-platforms/valuecell
git diff --cached --check
git diff --cached --name-only
git commit -m "chore: 固定 ValueCell 代理平台参考版本"
```

Expected staged names: only `.gitmodules` and `externals/agent-platforms/valuecell`.

### Task 4: Register Trust, Lifecycle, and License Metadata

**Files:**
- Modify: `externals/manifest.yaml`

- [ ] **Step 1: Run the pre-registration check**

Before applying the YAML edit, this command must report the three missing IDs,
proving the check detects absent registrations:

```powershell
$manifest = Get-Content -Raw externals/manifest.yaml
@('qilihei_stockagent','mingyu_stockagent','valuecell') | Where-Object { $manifest -notmatch "id: $_" }
```

Expected: all three IDs.

- [ ] **Step 2: Add the three manifest components**

Append these entries under `components`:

```yaml
  - id: qilihei_stockagent
    path: externals/a-share-research/qilihei-stockagent
    upstream: https://github.com/qilihei/StockAgent.git
    category: a_share_research
    role: a_share_data_news_factor_backtest_and_agent_platform_reference
    trust_class: untrusted_third_party_financial_agent
    lifecycle: incubating
    integration_mode: reference_only
    approval_status: pending_review
    license_spdx: MIT
    license_review: repository_license_verified_transitive_content_and_service_terms_pending

  - id: mingyu_stockagent
    path: externals/simulation-engines/mingyu-stockagent
    upstream: https://github.com/MingyuJ666/Stockagent.git
    category: simulation_engine
    role: llm_investor_behavior_and_market_simulation_reference
    trust_class: untrusted_third_party_financial_agent
    lifecycle: incubating
    integration_mode: reference_only
    approval_status: pending_review
    license_spdx: NOASSERTION
    license_review: repository_license_missing_code_use_and_extraction_blocked

  - id: valuecell
    path: externals/agent-platforms/valuecell
    upstream: https://github.com/ValueCell-ai/valuecell.git
    category: agent_platform
    role: financial_agent_orchestration_registry_a2a_and_application_reference
    trust_class: untrusted_third_party_financial_agent
    lifecycle: incubating
    integration_mode: reference_only
    approval_status: pending_review
    license_spdx: Apache-2.0
    license_review: repository_license_verified_third_party_components_and_service_terms_pending
```

Run the same pre-registration command again. Expected after the edit: no output.

- [ ] **Step 3: Verify policy fields and registry uniqueness**

Run:

```powershell
$manifest = Get-Content -Raw externals/manifest.yaml
foreach ($id in @('qilihei_stockagent','mingyu_stockagent','valuecell')) {
    if (($manifest | Select-String -AllMatches "(?m)^  - id: $id$").Matches.Count -ne 1) {
        throw "manifest id count invalid: $id"
    }
}
foreach ($required in @('default_trust: untrusted_third_party','live_qmt_access: forbidden','lifecycle: incubating','integration_mode: reference_only','approval_status: pending_review')) {
    if ($manifest -notmatch [regex]::Escape($required)) { throw "missing policy: $required" }
}
```

Expected: exit code 0 with no output.

- [ ] **Step 4: Commit the registry update**

Run:

```powershell
git add -- externals/manifest.yaml
git diff --cached --check
git diff --cached --name-only
git commit -m "chore: 登记孵化中的股票代理平台"
```

Expected staged name: only `externals/manifest.yaml`.

### Task 5: Record the Comparative Intake Assessment

**Files:**
- Create: `externals/incubator/stock-agent-platforms.md`

- [ ] **Step 1: Create the assessment document**

Write the document with these sections and conclusions:

```markdown
# Stock Agent Platforms Intake

Date: 2026-08-04

## Candidates

| Project | Pinned revision | License finding | Initial decision |
| --- | --- | --- | --- |
| qilihei/StockAgent | `82fbd6619e92e79172756d7c689bb1ec5dc0f8b6` | MIT repository license; transitive content and service terms pending | `incubating`, `reference_only` |
| MingyuJ666/Stockagent | `e2a9c052b81694067b1dbed4ccf39be9ab7f392c` | No repository license found; code use and extraction blocked | `incubating`, `reference_only` |
| ValueCell-ai/valuecell | `9793e9c0563fbf56fc096757d8bb80e209ac7aab` | Apache-2.0 repository license with third-party-component caveat | `incubating`, `reference_only` |

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
```

- [ ] **Step 2: Verify required warnings are present**

Run:

```powershell
$doc = Get-Content -Raw externals/incubator/stock-agent-platforms.md
foreach ($term in @('reference_only','No repository license found','not a standards-compliant MCP','live cryptocurrency order routing','No QMT')) {
    if ($doc -notmatch [regex]::Escape($term)) { throw "assessment missing: $term" }
}
```

Expected: exit code 0 with no output.

- [ ] **Step 3: Commit the assessment**

Run:

```powershell
git add -- externals/incubator/stock-agent-platforms.md
git diff --cached --check
git diff --cached --name-only
git commit -m "docs: 记录股票代理平台评估"
```

Expected staged name: only `externals/incubator/stock-agent-platforms.md`.

### Task 6: Update Workspace Documentation

**Files:**
- Modify: `externals/README.md`
- Modify: `docs/project-status.md`
- Modify: `docs/superpowers/specs/2026-08-04-stock-agent-platforms-intake-design.md`
- Existing plan file: `docs/superpowers/plans/2026-08-04-stock-agent-platforms-intake.md`

- [ ] **Step 1: Update external ownership and safety documentation**

Add these bullets to the relevant sections of `externals/README.md`:

```markdown
- qilihei/StockAgent is an incubating A-share workflow and tool-schema
  reference; its internal Redis tool protocol is not an approved MCP adapter.
- MingyuJ666/Stockagent is an incubating market-simulation methodology
  reference; missing repository licensing blocks code use and extraction.
- ValueCell is an incubating financial-agent orchestration and A2A reference;
  its exchange execution and credential paths are outside the trust boundary.
```

- [ ] **Step 2: Update the project status snapshot**

Set the status date to `2026-08-04`, add a “Stock Agent Platforms” subsection
under open-source capabilities, and record these facts:

```markdown
| Project | Current position |
| --- | --- |
| qilihei/StockAgent | A-share workflow, data/news, factor, backtest, and tool-schema reference |
| MingyuJ666/Stockagent | LLM investor-behavior and market-simulation methodology reference; license blocked |
| ValueCell | Agent registry, orchestration, A2A, persistence, and application-shell reference; trading excluded |

All three are pinned as `incubating`, `reference_only`, and `pending_review`.
The manifest is an inventory, not an approval catalog. They have not been
installed, started, or connected to qmtq. No credentialed or trading path has
been enabled.
```

Add a status-matrix row:

```markdown
| StockAgent and ValueCell controlled source intake | Completed and pinned; evaluation only |
```

- [ ] **Step 3: Verify local documentation references and prohibited claims**

Run:

```powershell
foreach ($path in @(
    'externals/incubator/stock-agent-platforms.md',
    'docs/superpowers/specs/2026-08-04-stock-agent-platforms-intake-design.md',
    'docs/superpowers/plans/2026-08-04-stock-agent-platforms-intake.md'
)) {
    if (-not (Test-Path -LiteralPath $path)) { throw "missing document: $path" }
}
rg -n "integrated|approved_reference|production-ready|实盘已接入" externals/README.md docs/project-status.md externals/incubator/stock-agent-platforms.md
```

Expected: all paths exist. Review any search match manually; no text may claim these projects are integrated, approved, production-ready, or connected to live trading.

- [ ] **Step 4: Commit documentation and the implementation plan**

Run:

```powershell
git add -- externals/README.md docs/project-status.md docs/superpowers/specs/2026-08-04-stock-agent-platforms-intake-design.md docs/superpowers/plans/2026-08-04-stock-agent-platforms-intake.md
git diff --cached --check
git diff --cached --name-only
git commit -m "docs: 更新股票代理接入状态"
```

Expected staged names: exactly the four paths above.

### Task 7: Run Final Structural Verification

**Files:**
- Verify: `.gitmodules`
- Verify: `externals/manifest.yaml`
- Verify: three new gitlinks and documentation

- [ ] **Step 1: Verify all new gitlinks, URLs, and manifest mappings**

Run:

```powershell
$expected = @(
    @{ Id='qilihei_stockagent'; Path='externals/a-share-research/qilihei-stockagent'; Url='https://github.com/qilihei/StockAgent.git'; Rev='82fbd6619e92e79172756d7c689bb1ec5dc0f8b6' },
    @{ Id='mingyu_stockagent'; Path='externals/simulation-engines/mingyu-stockagent'; Url='https://github.com/MingyuJ666/Stockagent.git'; Rev='e2a9c052b81694067b1dbed4ccf39be9ab7f392c' },
    @{ Id='valuecell'; Path='externals/agent-platforms/valuecell'; Url='https://github.com/ValueCell-ai/valuecell.git'; Rev='9793e9c0563fbf56fc096757d8bb80e209ac7aab' }
)
$manifest = Get-Content -Raw externals/manifest.yaml
foreach ($item in $expected) {
    $url = git config -f .gitmodules --get "submodule.$($item.Path).url"
    $rev = git -C $item.Path rev-parse HEAD
    $dirty = git -C $item.Path status --short
    if ($url -ne $item.Url) { throw "URL mismatch: $($item.Path)" }
    if ($rev -ne $item.Rev) { throw "revision mismatch: $($item.Path)" }
    if ($dirty) { throw "dirty submodule: $($item.Path)" }
    if ($manifest -notmatch [regex]::Escape("id: $($item.Id)")) { throw "manifest missing: $($item.Id)" }
    if ($manifest -notmatch [regex]::Escape("path: $($item.Path)")) { throw "manifest path missing: $($item.Path)" }
}
```

Expected: exit code 0 with no output.

- [ ] **Step 2: Verify submodule state and documentation diff quality**

Run:

```powershell
git submodule status -- externals/a-share-research/qilihei-stockagent externals/simulation-engines/mingyu-stockagent externals/agent-platforms/valuecell
git diff --check HEAD~6..HEAD
```

Expected: each submodule line begins with a space and shows the reviewed hash; diff check produces no output. If commit grouping differs, replace `HEAD~6` with the first intake commit's parent.

- [ ] **Step 3: Confirm no unrelated change was committed**

Run:

```powershell
git log --name-only --format= HEAD~6..HEAD | Where-Object { $_ } | Sort-Object -Unique
git status --short
```

Expected committed paths are limited to the file map in this plan. The status may still show the pre-existing `M packages/paper2quant`; that modification must remain uncommitted and otherwise untouched.

- [ ] **Step 4: Record the verification boundary**

In the delivery report, state explicitly:

```text
Verified: exact gitlinks, upstream URLs, clean external checkouts, manifest and documentation consistency.
Not executed: third-party installation, tests, services, network features, LLM calls, data collection, trading, or credential paths.
```

Do not claim runtime compatibility or functional correctness from structural intake verification.
