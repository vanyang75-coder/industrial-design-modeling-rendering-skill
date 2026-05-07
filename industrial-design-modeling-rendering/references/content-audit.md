# Content Audit

Use this audit to judge whether the local OpenClaw industrial design software knowledge base is sufficient for a specific answer.

## Current State

Audited root:

`<KB_ROOT>`

The root contains many files, but most are not knowledge content. A local Python virtual environment (`venv_image_qa`) dominates the file count and should be ignored for modeling/rendering answers. Excluding that environment, the useful corpus is mainly Markdown notes: about 179 `.md` files plus a few `.txt`, `.json`, and `.html` files.

## Evidence Tiers

### Tier A: Strong First-Use Sources

Use these as the primary base for practical answers:

- `工业设计软件规则库-v3.0-统一优化版.md`
  - Concise, current, and directly useful for Rhino and KeyShot.
  - Good for quick parameter ranges and common Q&A such as Boolean failure, bevels, metal, glass, three-point lighting, samples, denoise.
- `Rhino 建模规则库 - 深度分析版.md`
  - Best Rhino rule source with confidence notes and tutorial source IDs.
  - Good for failure diagnosis and repeatable modeling principles.
- `KeyShot 渲染规则库 -28 视频综合版.md`
  - Best KeyShot source for material, lighting, render settings, post-processing, and cases.
- `犀牛 keyshot 教程经验总结.md`
  - Strong troubleshooting content for Rhino curve/surface quality, NetworkSrf failure, bevel failure, and practical causes.
- `<KB_ROOT>\Rhino 建模\rhino-video-clean-index.json`
  - Strong metadata source for the 47 current Rhino tutorial videos.
  - Use for exact case number, BV, title, and transcript filename alignment.
- `<KB_ROOT>\Rhino 建模\Rhino 字幕证据索引 - 100个犀牛实战案例建模教程.md`
  - Strong first-use source for transcript-backed Rhino case references.
  - Use before older case files when case numbering, BV/title alignment, or video-derived evidence matters.

### Tier B: Useful but Needs Cross-Checking

Use these to enrich answers after a Tier A source is found:

- `<KB_ROOT>\Rhino 建模\Rhino 系统性建模技巧总纲 - 字幕归纳版.md`
  - Best current synthesis of repeatable Rhino modeling techniques from the transcript corpus.
  - Use for workflow logic and product-type strategy; cross-check exact parameters or command names when precision matters.
- `<KB_ROOT>\Rhino 建模\Rhino 截图问答路由规则 - 字幕证据版.md`
  - Best current source for screenshot-first Rhino question routing.
  - Use to classify screenshot stage, product family, likely issue, and next action.
- `<KB_ROOT>\Rhino 建模\Rhino 案例建模参考卡 - 字幕提取版.md`
  - Useful product analogy source distilled from transcripts.
  - Use to enrich answers with case families, but treat it as a summary rather than a verbatim transcript.
- `<KB_ROOT>\Rhino 建模\合集索引 - 100个犀牛实战案例建模教程.md`
  - Newly verified Bilibili season index for the Rhino 100-case tutorial series.
  - Use as the canonical BV/title map for cases 31-46 before citing older case notes.
  - It is metadata, not a full content transcript.
- `<KB_ROOT>\Rhino 建模\45-BV1KQ95BpEzj-吹风机建模 2.md`
  - Useful provisional routing card for hair dryer screenshots.
  - Cross-check before treating command sequence or parameters as confirmed video content.
- `<KB_ROOT>\Rhino 建模\46-BV1fMoVBCEsL-运动水杯建模.md`
  - Useful provisional routing card for sport bottle screenshots.
  - Cross-check before treating command sequence or parameters as confirmed video content.

- `工业设计问题库 - 问题驱动版.md`
  - Strong taxonomy of real design questions: partition lines, convergence points, metal/plastic feel, keys, surface transitions, interfaces, lighting, camera, mold, structure, finish, color.
  - Some entries are problem headings with counts rather than full solutions; cross-check with rule files before giving detailed steps.
- `04-问答流程\02-案例库.md`
  - Useful examples of answer shape and beginner-to-advanced cases.
  - Some content is template-like and should not be treated as verified production guidance by itself.
- `01-Rhino\`, `02-KeyShot\`, `03-C4D\`
  - Useful structured notes and command/reference material.
  - Cross-check parameters with Tier A when possible.
- `Rhino 建模\` and `KeyShot 渲染\`
  - Useful product-specific analogies and tutorial-derived notes.
  - Some notes were produced by rapid analysis and may include incomplete metadata.

### Tier C: Use Carefully

- `<KB_ROOT>\Rhino 建模\Rhino 47视频字幕建模参考提取 - 当前版.md`
  - Intermediate extraction file from the subtitle analysis pass.
  - Useful for tracing rough extraction results, but may contain ASR noise and should not be the main answer source.
- `规则索引.md` and `学习路线图.md`
  - Useful navigation and learning-plan documents.
  - They claim larger totals such as 1580 rules, but detailed accessible current rules are not equally complete across all categories.
- `AI 产品渲染提示词.md`
  - Useful for AI image generation / Stable Diffusion style scene prompts.
  - It is not KeyShot parameter guidance and should not be mixed into KeyShot recipes unless the user asks for AI image prompts.
- `备份\`, `归档\`, old v1/v2 rule libraries
  - Use only for historical recovery, missing content, or comparison.
  - Prefer current top-level files first.

## Known Gaps and Risks

- C4D coverage is thinner than Rhino and KeyShot. It has useful structured guides, but less tutorial-backed evidence.
- The knowledge base has inconsistent rule-count claims: current v3 unified library has 317 rules, while route/index documents mention larger totals such as 1580. Treat large totals as roadmap/index claims, not guaranteed detailed rule availability.
- Many Rhino case notes have `待确认` metadata or mention rapid analysis such as `极速冲刺流程`. Use them for analogy, not as sole evidence for precise steps.
- The 2026-05-07 Bilibili collection check found that older Rhino case notes 31-44 may have sequence/BV/title mismatches. Use the new collection index as the source of truth before citing those cases.
- The 2026-05-07 local Whisper pass completed corrected transcripts for indexes 01-47, but ASR terminology errors can remain. Use transcript-derived summaries as strong workflow evidence, but cross-check exact command names, dimensions, and timestamps when precision matters.
- Some files are duplicated in `备份\`; avoid double-counting or ranking backup copies as stronger evidence.
- Some early index files contain placeholders such as `第一步...`; do not rely on placeholder sections.
- Manufacturing/structure topics such as draft angle, snap fits, screw bosses, waterproofing, shrink marks, and surface finishing are present as categories, but often need professional inference or external/user-provided constraints for exact dimensions.
- Real software operation cannot be performed unless the environment exposes Rhino, KeyShot, C4D, or a relevant automation tool. Give manual steps and checks.

## Adequacy Decision

Use the local knowledge base as sufficient when:

- The request is about Rhino modeling fundamentals, Boolean/bevel/surface workflow, surface continuity checks, or product-case analogies.
- The request is about KeyShot materials, lighting, camera, render settings, output, noise, or common product rendering recipes.
- The user wants a learning route or local-KB-based rule lookup.

Treat the answer as partial and clearly mark inference when:

- The request requires exact engineering dimensions, mold/manufacturing validation, material science, production tolerances, or vendor-specific settings.
- The request is C4D-heavy, plugin-specific, or version-specific beyond general guidance.
- The request asks for a precise command sequence for a product type not represented in the local cases.
- Search only finds backup/old files, question headings, or files with incomplete metadata.

## Update Policy

When adding new rules later:

1. Prefer problem-driven categories plus software-specific tags.
2. Record source, product type, software, confidence, trigger, action, parameter, and failure check.
3. Avoid writing into the user's configured knowledge base without explicit confirmation.

