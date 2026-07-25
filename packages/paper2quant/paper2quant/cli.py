"""Paper2Quant offline staging CLI."""

from __future__ import annotations

import argparse

from .builder import build_research_package
from .catalog import build_method_catalog


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="paper2quant")
    subparsers = parser.add_subparsers(dest="command", required=True)
    package_parser = subparsers.add_parser("build-package")
    package_parser.add_argument("--spec", required=True)
    package_parser.add_argument("--output-root", required=True)
    package_parser.add_argument("--producer", choices=["manual", "fake"], default="manual")
    catalog_parser = subparsers.add_parser("build-catalog")
    catalog_parser.add_argument("--spec", required=True)
    catalog_parser.add_argument("--output-dir", required=True)
    args = parser.parse_args(argv)
    if args.command == "build-package":
        print(build_research_package(args.spec, args.output_root, producer=args.producer))
        return 0
    if args.command == "build-catalog":
        print(build_method_catalog(args.spec, args.output_dir))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
