# External Dependencies

`externals/` is a managed dependency tree. It is not a dump directory and it is
not ignored by the root repository.

Every source project below this directory is a Git submodule. The root
`quantools` commit records both:

- the canonical public URL in `.gitmodules`;
- the exact upstream revision in the submodule gitlink.

`externals/manifest.yaml` adds role and trust metadata. Gitlinks remain the
authoritative revision pins.

## Initialize

For a new clone:

```powershell
git clone --recurse-submodules git@github.com:gyfin/quantools.git
```

For an existing clone:

```powershell
git submodule sync --recursive
git submodule update --init --recursive
```

## Inspect

```powershell
git submodule status --recursive
git status --short
```

A leading space in `git submodule status` means the checkout matches the pinned
revision. Other prefixes require attention:

- `-`: not initialized;
- `+`: checked out at a different revision;
- `U`: merge conflict.

## Update One Dependency

Dependency updates are reviewed changes, not an automatic bulk operation:

```powershell
git -C externals\qlib fetch origin
git -C externals\qlib checkout <reviewed-commit>
git diff --submodule=log
```

Run the relevant integration checks, then commit the changed gitlink in the root
repository. Avoid unreviewed `git submodule update --remote` across the entire
workspace.

If an upstream patch is required, create an intentional fork and record that
decision. Do not leave unpublished edits inside a detached submodule checkout.

## Ownership And Safety

- Qlib, VectorBT, Kronos, and QuantsPlaybook are research inputs.
- LEAN and OSkhQuant provide execution or A-share integration reference code.
- Paper2Agent, paper2code, RD-Agent, and cangjie-skill are research-intake
  experiments.
- kimi-cli and kimi-code are optional agent hosts, not trading authorities.
- First-party `paper2quant` lives at `packages/paper2quant`.
- `D:\qmtq` remains an independent sibling repository and the QMT protocol,
  evidence, and safety boundary.

Being pinned does not make third-party code trusted. Do not give external agents
live QMT credentials, bypass qmtq validation, or promote generated factors and
signals without review, provenance, and reproducible evaluation.
