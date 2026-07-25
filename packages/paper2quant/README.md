# Paper2Quant

Paper2Quant is an external, offline staging prototype for qmtq research-source
protocols. It copies an explicitly supplied local source into an isolated
staging package or builds an unevaluated method catalog.

It does not search the internet, call an LLM, run third-party code, access QMT,
write `research_cache`, approve experiments, or create trading signals.

```powershell
python -m paper2quant.cli build-package --spec input.json --output-root output --producer manual
python -m paper2quant.cli build-catalog --spec methods.json --output-dir catalog
python -m qmtq.cli validate-research-intake output\staged\source=<source_id>
python -m qmtq.cli evaluate-research-methods catalog
```
