#!/usr/bin/env python3
"""Search the local industrial design modeling/rendering knowledge base."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Iterable


DEFAULT_ROOT = Path(os.environ.get("INDUSTRIAL_DESIGN_KB", str(Path.home() / "industrial-design-kb")))
SOFTWARE_HINTS = {
    "rhino": ["rhino", "犀牛", "Rhino 建模", "01-Rhino"],
    "keyshot": ["keyshot", "KeyShot 渲染", "02-KeyShot"],
    "c4d": ["c4d", "cinema", "03-C4D"],
}
CORE_FILES = {
    "工业设计软件规则库-v3.0-统一优化版.md",
    "工业设计问题库 - 问题驱动版.md",
    "犀牛 keyshot 教程经验总结.md",
    "规则索引.md",
    "rhino-video-clean-index.json",
    "Rhino 字幕证据索引 - 100个犀牛实战案例建模教程.md",
    "Rhino 系统性建模技巧总纲 - 字幕归纳版.md",
    "Rhino 截图问答路由规则 - 字幕证据版.md",
    "Rhino 案例建模参考卡 - 字幕提取版.md",
}
QUERY_EXPANSIONS = {
    "吹风机": ["风道", "出风口", "进风口", "手柄", "格栅"],
    "水杯": ["旋转容器", "瓶口", "瓶盖", "壁厚", "杯底"],
    "瓶": ["旋转容器", "瓶口", "瓶盖", "壁厚"],
    "鼠标": ["手持", "曲面", "分模线", "按键"],
    "耳机": ["穿戴", "小曲面", "孔位", "圆角"],
    "剃须刀": ["格栅", "孔阵列", "壳体", "倒角"],
    "摩托": ["交通", "车壳", "流线", "外壳", "分件"],
    "截图": ["路由", "下一步", "诊断", "阶段"],
    "倒角": ["圆角", "半径", "边缘", "顺序"],
    "布尔": ["切割", "穿透", "闭合", "重合面"],
    "曲面": ["连续", "G2", "斑马纹", "高光"],
}
ENCODINGS = ("utf-8-sig", "utf-8", "gb18030")


def read_text(path: Path) -> str:
    for encoding in ENCODINGS:
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="ignore")


def is_ignored(path: Path, include_backups: bool) -> bool:
    parts = {part.lower() for part in path.parts}
    if "venv_image_qa".lower() in parts:
        return True
    if not include_backups and ({"备份", "归档"} & set(path.parts)):
        return True
    return False


def matches_software(path: Path, software: str | None) -> bool:
    if not software:
        return True
    if path.name in CORE_FILES:
        return True
    hay_path = str(path).lower()
    return any(hint.lower() in hay_path for hint in SOFTWARE_HINTS.get(software, []))


def iter_files(root: Path, software: str | None, include_backups: bool) -> Iterable[Path]:
    for path in root.rglob("*"):
        if is_ignored(path, include_backups):
            continue
        if not matches_software(path, software):
            continue
        if path.is_file() and path.suffix.lower() in {".md", ".txt", ".json"}:
            yield path


def score_file(path: Path, text: str, terms: list[str], software: str | None) -> int:
    hay_path = str(path).lower()
    hay_text = text.lower()
    score = 0
    for term in terms:
        needle = term.lower()
        if not needle:
            continue
        score += hay_path.count(needle) * 12
        score += hay_text.count(needle)
    if software:
        for hint in SOFTWARE_HINTS.get(software, []):
            if hint.lower() in hay_path:
                score += 20
    important_names = [
        "工业设计软件规则库-v3.0-统一优化版",
        "工业设计问题库 - 问题驱动版",
        "Rhino 建模规则库 - 深度分析版",
        "KeyShot 渲染规则库 -28 视频综合版",
        "Rhino 字幕证据索引 - 100个犀牛实战案例建模教程",
        "Rhino 系统性建模技巧总纲 - 字幕归纳版",
        "Rhino 截图问答路由规则 - 字幕证据版",
        "Rhino 案例建模参考卡 - 字幕提取版",
        "rhino-video-clean-index",
        "规则索引",
    ]
    if any(name.lower() in hay_path for name in important_names):
        score += 30
    priority_names = [
        "Rhino 字幕证据索引 - 100个犀牛实战案例建模教程",
        "Rhino 系统性建模技巧总纲 - 字幕归纳版",
        "Rhino 截图问答路由规则 - 字幕证据版",
        "Rhino 案例建模参考卡 - 字幕提取版",
        "rhino-video-clean-index",
    ]
    if software == "rhino" and any(name.lower() in hay_path for name in priority_names):
        score += 35
    term_set = {term.lower() for term in terms}
    if software == "rhino":
        if {"系统性", "总纲"} & term_set and "Rhino 系统性建模技巧总纲 - 字幕归纳版".lower() in hay_path:
            score += 420
        elif {"阶段"} & term_set and "Rhino 系统性建模技巧总纲 - 字幕归纳版".lower() in hay_path:
            score += 160
        if {"截图", "路由", "下一步", "诊断"} & term_set and "Rhino 截图问答路由规则 - 字幕证据版".lower() in hay_path:
            score += 300
        if {"字幕", "证据", "bv", "索引"} & term_set and "Rhino 字幕证据索引 - 100个犀牛实战案例建模教程".lower() in hay_path:
            score += 180
    if "Rhino 47视频字幕建模参考提取 - 当前版".lower() in hay_path:
        score -= 180
    return score


def expand_terms(terms: list[str]) -> list[str]:
    expanded = list(terms)
    seen = {term.lower() for term in expanded}
    for term in terms:
        for extra in QUERY_EXPANSIONS.get(term, []):
            key = extra.lower()
            if key not in seen:
                expanded.append(extra)
                seen.add(key)
    return expanded


def snippet(text: str, terms: list[str], width: int = 180) -> str:
    lower = text.lower()
    positions = [lower.find(term.lower()) for term in terms if term and lower.find(term.lower()) >= 0]
    start = max(min(positions) - 60, 0) if positions else 0
    raw = " ".join(text[start : start + width].split())
    return raw


def safe_print(value: str) -> None:
    try:
        print(value)
    except UnicodeEncodeError:
        encoding = sys.stdout.encoding or "utf-8"
        print(value.encode(encoding, errors="replace").decode(encoding, errors="replace"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Search industrial design modeling/rendering KB.")
    parser.add_argument("query", help="Search query, e.g. '倒角 布尔失败' or '拉丝金属 三点布光'")
    parser.add_argument("--root", default=os.environ.get("INDUSTRIAL_DESIGN_KB", str(DEFAULT_ROOT)))
    parser.add_argument("--software", choices=sorted(SOFTWARE_HINTS), default=None)
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    parser.add_argument("--include-backups", action="store_true", help="Include backup and archive folders.")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"Knowledge base root not found: {root}")

    terms = [part.strip() for part in args.query.replace("|", " ").split() if part.strip()]
    terms = expand_terms(terms)
    results = []
    for path in iter_files(root, args.software, args.include_backups):
        text = read_text(path)
        score = score_file(path, text, terms, args.software)
        if score > 0:
            results.append(
                {
                    "score": score,
                    "path": str(path),
                    "snippet": snippet(text, terms),
                }
            )

    results.sort(key=lambda item: item["score"], reverse=True)
    results = results[: args.top]

    if args.json:
        safe_print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for index, item in enumerate(results, 1):
            safe_print(f"{index}. score={item['score']} {item['path']}")
            if item["snippet"]:
                safe_print(f"   {item['snippet']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

