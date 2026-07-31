# Open Source Incubator

This directory records how candidate open-source capabilities are evaluated.
Source repositories remain in stable capability-oriented submodule paths; they
are not copied here.

## Lifecycle

1. Discover the candidate and define the capability gap it may fill.
2. Register its upstream URL, pinned commit, license, trust class, and intended
   role in `../manifest.yaml`.
3. Inspect code, prompts, dependencies, network behavior, and credential use.
4. Evaluate it against reproducible fixtures and an existing baseline.
5. Promote it to `approved_reference` or `integrated` only with human approval
   and an owned adapter or wrapper.
6. Re-evaluate upstream updates before changing the root gitlink.
7. Mark abandoned or superseded projects `retired`; preserve their provenance.

`incubating` and `reference_only` projects must not receive live QMT
credentials, write accepted qmtq state, or issue trading instructions.
