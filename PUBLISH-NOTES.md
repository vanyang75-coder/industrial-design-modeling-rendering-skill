# Industrial Design Modeling Rendering - Publish Notes

This release contains only the Codex skill package:

`industrial-design-modeling-rendering/`

It does not include the maintainer's private Obsidian knowledge base, raw subtitles, downloaded videos, audio files, or transcript archives.

## Should the Knowledge Base Be Uploaded?

Default recommendation: no.

Keep the skill and the knowledge base separate:

- The skill is the reusable workflow, routing logic, answer patterns, and search script.
- The knowledge base is user-specific content and may contain private notes, local paths, transcript material, and copyrighted/source-derived text.

For public sharing, publish this skill package only. Users can connect their own local knowledge base by setting:

```powershell
$env:INDUSTRIAL_DESIGN_KB = "D:\path\to\industrial-design-kb"
```

If a public demo corpus is needed later, create a small sanitized sample knowledge base with a few original notes and no raw subtitles or private vault structure.

## Install

Copy the folder:

`industrial-design-modeling-rendering`

into the user's Codex skills directory:

`~/.codex/skills/industrial-design-modeling-rendering`

Then restart or refresh Codex so the skill list is reloaded.

## Included Files

- `SKILL.md`
- `agents/openai.yaml`
- `references/answer-patterns.md`
- `references/content-audit.md`
- `references/knowledge-map.md`
- `references/screenshot-diagnosis.md`
- `scripts/search_kb.py`

