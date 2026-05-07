#!/usr/bin/env python3
"""Validate a local installation of the industrial design modeling skill."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "references/answer-patterns.md",
    "references/content-audit.md",
    "references/knowledge-map.md",
    "references/screenshot-diagnosis.md",
    "scripts/search_kb.py",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[ OK ] {message}")


def warn(message: str) -> None:
    print(f"[WARN] {message}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def validate_skill_root(skill_root: Path) -> bool:
    passed = True
    if not skill_root.exists():
        fail(f"Skill root not found: {skill_root}")
        return False

    ok(f"Skill root found: {skill_root}")
    for relative in REQUIRED_FILES:
        path = skill_root / relative
        if path.is_file():
            ok(f"Required file exists: {relative}")
        else:
            fail(f"Required file missing: {relative}")
            passed = False

    skill_md = skill_root / "SKILL.md"
    if skill_md.is_file():
        text = read_text(skill_md)
        if text.lstrip().startswith("---") and "name: industrial-design-modeling-rendering" in text and "description:" in text:
            ok("SKILL.md frontmatter looks valid")
        else:
            fail("SKILL.md frontmatter is missing name or description")
            passed = False

    return passed


def validate_kb(kb_root: Path | None) -> bool:
    if kb_root is None:
        warn("No knowledge base path supplied. Set INDUSTRIAL_DESIGN_KB or pass --kb-root.")
        return True
    if kb_root.exists():
        ok(f"Knowledge base root found: {kb_root}")
        return True
    fail(f"Knowledge base root not found: {kb_root}")
    return False


def run_search_probe(skill_root: Path, kb_root: Path | None) -> bool:
    search_script = skill_root / "scripts" / "search_kb.py"
    if not search_script.is_file():
        fail("Cannot run search probe because scripts/search_kb.py is missing")
        return False

    probes = [
        ("Rhino screenshot route", "截图 路由 下一步", "rhino"),
        ("KeyShot render route", "KeyShot 截图 材质 灯光 相机 输出", "keyshot"),
    ]
    env = os.environ.copy()
    passed = True
    for label, query, software in probes:
        command = [
            sys.executable,
            str(search_script),
            query,
            "--software",
            software,
            "--top",
            "3",
        ]
        if kb_root is not None:
            command.extend(["--root", str(kb_root)])

        result = subprocess.run(command, text=True, capture_output=True, env=env)
        if result.returncode != 0:
            fail(f"{label} search probe failed")
            if result.stderr.strip():
                print(result.stderr.strip())
            passed = False
            continue

        if result.stdout.strip():
            ok(f"{label} search probe returned results")
            print(result.stdout.strip())
        else:
            warn(f"{label} search probe ran but returned no results")
    return passed


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate this Codex skill installation.")
    parser.add_argument(
        "--skill-root",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Path to the industrial-design-modeling-rendering skill folder.",
    )
    parser.add_argument(
        "--kb-root",
        default=os.environ.get("INDUSTRIAL_DESIGN_KB"),
        type=Path,
        help="Path to a local industrial design knowledge base.",
    )
    parser.add_argument("--skip-search", action="store_true", help="Only validate files and metadata.")
    args = parser.parse_args()

    skill_root = args.skill_root.resolve()
    kb_root = args.kb_root.resolve() if args.kb_root else None

    passed = validate_skill_root(skill_root)
    passed = validate_kb(kb_root) and passed
    if not args.skip_search:
        passed = run_search_probe(skill_root, kb_root) and passed

    if passed:
        ok("Installation check completed")
        return 0
    fail("Installation check found problems")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

