"""Build a qmtq research intake package from an explicit local specification."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


FORBIDDEN_USE = ["accepted_signal", "live_trading", "research_cache_write"]


def _load_object(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("package specification must be a JSON object")
    return payload


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _with_source_id(rows: Any, source_id: str, name: str) -> list[dict[str, Any]]:
    if not isinstance(rows, list):
        raise ValueError(f"{name} must be a list")
    normalized: list[dict[str, Any]] = []
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise ValueError(f"{name} row {index} must be an object")
        normalized.append({**row, "source_id": str(row.get("source_id") or source_id)})
    return normalized


def build_research_package(spec_path: str | Path, output_root: str | Path, *, producer: str) -> Path:
    """Create raw and staged outputs without interpreting or executing source code."""
    spec_file = Path(spec_path).resolve()
    spec = _load_object(spec_file)
    source = spec.get("source")
    if not isinstance(source, dict):
        raise ValueError("source must be an object")
    source_id = str(source.get("source_id") or "")
    if not source_id:
        raise ValueError("source.source_id is required")
    asset_path = Path(str(source.get("asset_path") or "")).resolve()
    if not asset_path.is_file():
        raise ValueError("source.asset_path must reference a local file")

    output = Path(output_root).resolve()
    staged = output / "staged" / f"source={source_id}"
    if staged.exists():
        raise FileExistsError(f"staged output already exists: {staged}")
    raw = output / "raw"
    _write_json(raw / "producer_input.json", spec)

    suffix = asset_path.suffix.lower() or ".bin"
    staged_asset = staged / f"source{suffix}"
    staged_asset.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(asset_path, staged_asset)
    manifest = {
        "protocol_version": 1,
        "source_id": source_id,
        "source_type": source.get("source_type"),
        "title": source.get("title"),
        "authors": source.get("authors"),
        "version": source.get("version"),
        "license": source.get("license"),
        "source_asset": {"path": staged_asset.name, "sha256": _sha256_file(staged_asset)},
        "repository": source.get("repository"),
        "related_source_ids": source.get("related_source_ids", []),
        "producer": {"name": producer, "mode": "offline_staging"},
        "intended_use": ["research_idea_generation"],
        "forbidden_use": FORBIDDEN_USE,
    }
    _write_json(staged / "source_manifest.json", manifest)
    _write_jsonl(staged / "evidence_units.jsonl", _with_source_id(spec.get("evidence_units"), source_id, "evidence_units"))
    _write_jsonl(staged / "claims.jsonl", _with_source_id(spec.get("claims"), source_id, "claims"))
    _write_jsonl(
        staged / "research_candidates.jsonl",
        _with_source_id(spec.get("research_candidates"), source_id, "research_candidates"),
    )
    decisions = spec.get("promotion_decisions", [])
    if not isinstance(decisions, list) or any(not isinstance(row, dict) for row in decisions):
        raise ValueError("promotion_decisions must be a list of objects")
    _write_jsonl(staged / "promotion_decisions.jsonl", decisions)

    for field, filename in [
        ("method_fingerprint", "method_fingerprint.json"),
        ("reproduction_manifest", "reproduction_manifest.json"),
    ]:
        payload = spec.get(field)
        if payload is not None:
            if not isinstance(payload, dict):
                raise ValueError(f"{field} must be an object")
            _write_json(staged / filename, {**payload, "protocol_version": 1, "source_id": source_id})
    return staged
