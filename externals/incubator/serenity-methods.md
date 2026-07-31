# Serenity Supply-Chain Methods Intake

Date: 2026-07-31

## Candidates

| Project | Pinned role | Initial decision |
| --- | --- | --- |
| BestSerenitySkillFromAT | Broad synthesis, templates, and market adaptation | `incubating`, `reference_only` |
| serenity-bottleneck-hunter | Focused reverse supply-chain bottleneck workflow | `incubating`, `reference_only` |

Both repositories contain an MIT license at the pinned revisions. Reused or
distilled upstream material still needs a transitive provenance review before
we copy it into a first-party implementation. They are method and prompt
references, not verified data sources, forecasting engines, or trading
authorities.

## Intended Use

The useful shared pattern is:

```text
market narrative
  -> physical or economic system change
  -> supply-chain layers
  -> scarce constraint
  -> listed-company exposure
  -> evidence and counter-evidence
  -> measurable research candidate
```

A future first-party wrapper should emit a versioned
`SupplyChainThesisBundle` containing the theme, value-chain graph, bottleneck
claim, company exposure, cited evidence, timestamps, measurable proxies,
falsification rules, and unresolved checks. Paper2Quant may enrich its evidence;
qmtq remains responsible for validation and admission.

## Promotion Gates

- Review prompts and scripts for unsafe tool use and prompt injection paths.
- Run point-in-time case studies on at least three historical themes.
- Grade primary evidence separately from narrative inference.
- Require explicit counter-theses, substitution risk, capacity response,
  valuation/crowding, and "already priced" checks.
- Compare results with an analyst baseline and record rejected candidates.
- Integrate through a project-owned wrapper with pinned method versions.

Until these gates pass, neither project is installed globally as an active
Codex skill and neither output may enter the accepted research or execution
chain directly.
