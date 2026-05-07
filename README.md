# Industrial Design Modeling Rendering Skill

A Codex skill for screenshot-first industrial design modeling and rendering help, focused on Rhino, KeyShot, C4D, product modeling workflows, visual troubleshooting, and local knowledge-base retrieval.

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

## Optional Local Knowledge Base

The bundled search script can read a local industrial design knowledge base. Set:

```powershell
$env:INDUSTRIAL_DESIGN_KB = "D:\path\to\industrial-design-kb"
```

Without that variable, the script falls back to:

```text
~/industrial-design-kb
```

## Included

- `SKILL.md`
- `agents/openai.yaml`
- `references/`
- `scripts/search_kb.py`
- `PUBLISH-NOTES.md`

