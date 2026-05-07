# Industrial Design Modeling Rendering Skill

A Codex skill for screenshot-first industrial design modeling and rendering help, focused on Rhino, KeyShot, C4D, product modeling workflows, visual troubleshooting, and local knowledge-base retrieval.

## Full Capability Requirements

This skill is designed as a workflow and retrieval layer. Its full value depends on at least one of the following:

- A strong image recognition / multimodal vision engine for software screenshots, such as a GPT image2 or image2-style visual understanding workflow when available.
- A complete local industrial design modeling and rendering knowledge base connected through `INDUSTRIAL_DESIGN_KB`.

The included `sample-kb/` is only a small sanitized demo corpus. It is useful for testing installation and retrieval, but it is not enough to provide full expert-level Rhino, KeyShot, or C4D guidance.

If you need access to a complete industrial design modeling/rendering knowledge base, contact the maintainer through GitHub Issues.

## What This Publishes

This repository publishes the skill package only:

`industrial-design-modeling-rendering/`

It does not include a private knowledge base, raw subtitles, downloaded videos, audio files, or transcript archives.

## Install

Copy the skill folder into your Codex skills directory:

```text
~/.codex/skills/industrial-design-modeling-rendering
```

Then restart or refresh Codex so the skill list is reloaded.

On Windows, the target is usually:

```text
C:\Users\<you>\.codex\skills\industrial-design-modeling-rendering
```

## Optional Local Knowledge Base

The bundled search script can read a local industrial design knowledge base. Set:

```powershell
$env:INDUSTRIAL_DESIGN_KB = "D:\path\to\industrial-design-kb"
```

Without that variable, the script falls back to:

```text
~/industrial-design-kb
```

## Quick Check

From the repository root, run:

```powershell
python industrial-design-modeling-rendering\scripts\check_install.py --kb-root sample-kb
```

You can also test retrieval directly:

```powershell
python industrial-design-modeling-rendering\scripts\search_kb.py "吹风机 手柄 风道 倒角" --software rhino --root sample-kb
python industrial-design-modeling-rendering\scripts\search_kb.py "塑料 材质 粗糙度" --software keyshot --root sample-kb
```

## Sample Knowledge Base

`sample-kb/` is a tiny sanitized demo corpus for testing. It contains original sample notes only. It is not a transcript archive and does not include private Obsidian content, downloaded videos, audio, or subtitles.

## Included

- `SKILL.md`
- `agents/openai.yaml`
- `references/`
- `scripts/search_kb.py`
- `scripts/check_install.py`
- `sample-kb/`
- `PUBLISH-NOTES.md`
