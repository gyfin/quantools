import hashlib
import json
from pathlib import Path

from paper2quant.builder import build_research_package
from paper2quant.catalog import build_method_catalog


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def test_build_research_package_separates_raw_and_staged_outputs(tmp_path: Path):
    source = tmp_path / "book.txt"
    source.write_text("流动性影响冲击持续时间。", encoding="utf-8")
    excerpt = "流动性影响冲击持续时间"
    spec = {
        "source": {
            "source_id": "book_demo",
            "source_type": "book",
            "title": "量化研究样例",
            "authors": ["研究者"],
            "version": "1",
            "license": "user_supplied",
            "asset_path": str(source),
        },
        "evidence_units": [
            {
                "evidence_id": "e1",
                "evidence_type": "text",
                "locator_type": "page",
                "locator": "1",
                "excerpt": excerpt,
                "content_sha256": sha256_text(excerpt),
                "verification_level": "human_verified",
                "verified_by": "human:researcher",
            }
        ],
        "claims": [
            {
                "claim_id": "cl1",
                "claim_type": "author_claim",
                "statement": "流动性可能影响冲击持续时间。",
                "evidence_refs": ["e1"],
                "inference_steps": [],
            }
        ],
        "research_candidates": [
            {
                "candidate_id": "c1",
                "title": "流动性冲击假设",
                "maturity": "insight",
                "review_status": "staged",
                "evidence_refs": ["e1"],
                "claim_refs": ["cl1"],
                "parent_candidate_ids": [],
                "derivation_type": "direct_reproduction",
                "mechanism": "低流动性延缓价格冲击衰减",
                "failure_conditions": ["不同流动性组没有差异"],
            }
        ],
        "promotion_decisions": [],
    }
    spec_path = tmp_path / "input.json"
    write_json(spec_path, spec)

    staged_dir = build_research_package(spec_path, tmp_path / "output", producer="manual")

    assert staged_dir == tmp_path / "output" / "staged" / "source=book_demo"
    assert (tmp_path / "output" / "raw" / "producer_input.json").exists()
    manifest = json.loads((staged_dir / "source_manifest.json").read_text(encoding="utf-8"))
    assert manifest["source_id"] == "book_demo"
    assert manifest["source_asset"]["path"] == "source.txt"
    assert manifest["forbidden_use"] == ["accepted_signal", "live_trading", "research_cache_write"]
    evidence = json.loads((staged_dir / "evidence_units.jsonl").read_text(encoding="utf-8"))
    assert evidence["source_id"] == "book_demo"


def test_build_method_catalog_keeps_discovery_unadopted(tmp_path: Path):
    methods = [
        {
            "method_id": "paper2agent",
            "name": "Paper2Agent",
            "paper_ref": "https://arxiv.org/abs/2509.06917",
            "repo_url": "https://github.com/jmiao24/Paper2Agent",
            "license": "MIT",
            "commit": "a" * 40,
            "provenance_tier": "official_author",
            "capabilities": ["official_code_execution", "mcp_export"],
            "public_evidence": ["paper:workflow"],
            "runtime_requirements": ["python>=3.10"],
            "safety": {
                "requires_sensitive_access": False,
                "sandboxable": True,
                "skips_permissions": True,
                "audit_outputs": True,
            },
            "known_limitations": ["permission bypass must be removed"],
            "concept_only": False,
        }
    ]
    spec_path = tmp_path / "methods.json"
    write_json(spec_path, {"methods": methods})

    catalog_dir = build_method_catalog(spec_path, tmp_path / "catalog")

    assert json.loads((catalog_dir / "method_catalog.jsonl").read_text())["method_id"] == "paper2agent"
    assert (catalog_dir / "capability_evaluations.jsonl").read_text() == ""
    assert (catalog_dir / "adoption_decisions.jsonl").read_text() == ""
