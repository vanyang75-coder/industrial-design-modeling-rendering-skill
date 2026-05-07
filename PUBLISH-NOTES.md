# Industrial Design Modeling Rendering - Publish Notes

This release contains the Codex skill package and a small sanitized sample knowledge base:

`industrial-design-modeling-rendering/`

`sample-kb/`

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

This release includes `sample-kb/` for demo and installation testing. It contains original sample notes only and should not be treated as a complete industrial design corpus.

## Install

Copy the folder:

`industrial-design-modeling-rendering`

into the user's Codex skills directory:

`~/.codex/skills/industrial-design-modeling-rendering`

Then restart or refresh Codex so the skill list is reloaded.

## Verify

From the repository root:

```powershell
python industrial-design-modeling-rendering\scripts\check_install.py --kb-root sample-kb
```

## Included Files

- `SKILL.md`
- `agents/openai.yaml`
- `references/answer-patterns.md`
- `references/content-audit.md`
- `references/knowledge-map.md`
- `references/screenshot-diagnosis.md`
- `scripts/search_kb.py`
- `scripts/check_install.py`
- `sample-kb/`
