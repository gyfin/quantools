"""Build an unevaluated offline method catalog for qmtq selection."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def build_method_catalog(spec_path: str | Path, output_dir: str | Path) -> Path:
    """Stage explicitly supplied method records without searching or adopting them."""
    payload = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("methods"), list):
        raise ValueError("catalog specification must contain a methods list")
    methods = payload["methods"]
    if any(not isinstance(row, dict) for row in methods):
        raise ValueError("each method must be an object")
    method_ids = [str(row.get("method_id") or "") for row in methods]
    if any(not item for item in method_ids) or len(method_ids) != len(set(method_ids)):
        raise ValueError("method_id values must be non-empty and unique")
    output = Path(output_dir).resolve()
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"catalog output is not empty: {output}")
    output.mkdir(parents=True, exist_ok=True)
    _write_jsonl(output / "method_catalog.jsonl", sorted(methods, key=lambda row: str(row["method_id"])))
    _write_jsonl(output / "capability_evaluations.jsonl", [])
    _write_jsonl(output / "adoption_decisions.jsonl", [])
    return output
