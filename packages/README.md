# First-Party Components

`packages/` contains gyfin-owned components that have an independent repository
and lifecycle but are pinned by the quantools workspace.

## Paper2Quant

- Path: `packages/paper2quant`
- Repository: `git@github.com:gyfin/Paper2Quant.git`
- Root submodule URL: `../Paper2Quant.git`
- Purpose: offline research-source staging and unevaluated method catalogs

The quantools gitlink selects the reviewed Paper2Quant revision. Make and push
Paper2Quant changes inside its repository first, then review and commit the
updated gitlink in quantools.

First-party ownership does not bypass qmtq safety rules. Paper2Quant has no
authority to access live QMT credentials, write `research_cache`, approve
experiments, or create accepted trading signals.
