# Knowledge Map

Use this map to retrieve from the local industrial design software knowledge base without loading the entire vault.

## Root

Primary knowledge base:

Use the environment variable `INDUSTRIAL_DESIGN_KB` when available. If it is not set, the bundled search script falls back to:

`~/industrial-design-kb`

Optional companion file:

`AI 产品渲染提示词.md`

## Source Priority

Read `content-audit.md` first for evidence tiers and known gaps. Then use this source map.

## 2026-05-07 Verified Additions

The Rhino tutorial collection index below is newly verified from Bilibili season metadata and should be used as the canonical case-number/BV map before relying on older 31-44 case notes. After the subtitle pass, the new subtitle-derived files should be treated as the first-stop Rhino product modeling corpus for screenshot routing, system techniques, and case analogies. These files are expected to live inside the user's configured knowledge base root, not inside this public skill package:

- `<KB_ROOT>\Rhino 建模\合集索引 - 100个犀牛实战案例建模教程.md`
  - Canonical index for 47 current videos in the collection.
  - Important correction: the collection has 47 entries but only reaches title number 46 because title number 42 appears twice.
  - Use this before updating or citing case notes 31-46.
- `<KB_ROOT>\Rhino 建模\rhino-video-clean-index.json`
  - Machine-readable clean index for the 47 current videos.
  - Use when exact case number, BV, title, or transcript filename matters.
- `<KB_ROOT>\Rhino 建模\Rhino 字幕证据索引 - 100个犀牛实战案例建模教程.md`
  - Canonical subtitle evidence index.
  - Use to locate transcript-backed modeling references, product types, and case evidence before citing older case notes.
- `<KB_ROOT>\Rhino 建模\Rhino 系统性建模技巧总纲 - 字幕归纳版.md`
  - Best current synthesis of repeatable Rhino modeling technique from the subtitle corpus.
  - Use for staged workflows: reference/proportion, blockout, curve/surface transition, Boolean/structure lines, fillet/chamfer, and final detail expression.
- `<KB_ROOT>\Rhino 建模\Rhino 截图问答路由规则 - 字幕证据版.md`
  - Best current routing source for uploaded Rhino screenshots.
  - Use to classify product type, modeling stage, likely issue, and next action.
- `<KB_ROOT>\Rhino 建模\Rhino 案例建模参考卡 - 字幕提取版.md`
  - Product-specific case cards distilled from transcripts.
  - Use for analogies such as hair dryer, bottle/container, handheld tools, and hard-surface consumer electronics.
- `<KB_ROOT>\Rhino 建模\Rhino 47视频字幕建模参考提取 - 当前版.md`
  - Intermediate extraction file.
  - Use only for investigation or traceability; prefer the evidence index, system overview, routing rules, and case cards for answers.
- `<KB_ROOT>\Rhino 建模\Rhino 字幕分析与知识库优化提交报告.md`
  - Completion report for the transcript extraction and knowledge-base optimization pass.
  - Use for verifying what was completed, known limitations, and remaining follow-up work.
- `<KB_ROOT>\Rhino 建模\45-BV1KQ95BpEzj-吹风机建模 2.md`
  - Provisional screenshot-routing card for hair dryer / airflow handheld products.
  - Evidence status: metadata confirmed, detailed video content still needs frame or viewing verification.
- `<KB_ROOT>\Rhino 建模\46-BV1fMoVBCEsL-运动水杯建模.md`
  - Provisional screenshot-routing card for sport bottle / revolved container products.
  - Evidence status: metadata confirmed, detailed video content still needs frame or viewing verification.
- `<KB_ROOT>\Rhino 建模\合集深化记录 - 2026-05-07.md`
  - Maintenance log explaining what was verified, what was backed up, and what should be fixed next.

1. `工业设计软件规则库-v3.0-统一优化版.md`
   - Best first stop for concise Rhino and KeyShot rules.
   - Contains quick Q&A index, rule IDs, parameters, and practical ranges.
   - Known summary: 317 rules from Rhino 44 videos and KeyShot 28 videos.
2. `工业设计问题库 - 问题驱动版.md`
   - Use for symptom-style questions such as partition lines, convergence points, metal feel, plastic feel, key gaps, surface transitions, lighting, camera, output, mold issues.
   - Best when the user describes a design problem rather than naming a command.
3. `Rhino 建模规则库 - 深度分析版.md`
   - Use for detailed Rhino modeling rules with confidence notes and tutorial source IDs.
   - High-value categories: surface modeling, basic modeling, workflow, process parameters, detail handling, product-specific cases.
4. `KeyShot 渲染规则库 -28 视频综合版.md`
   - Use for material, lighting, rendering output, post-processing, and case-based KeyShot recipes.
5. `犀牛 keyshot 教程经验总结.md`
   - Use for high-value troubleshooting such as curve quality, NetworkSrf failure, bevel failure, and surface diagnosis.
6. `规则索引.md`
   - Use for category and rule-code navigation.
   - Contains rule families such as `R-BASIC`, `R-SURFACE`, `R-SOLID`, `R-DETAIL`, `K-MAT`, `K-LIGHT`, `K-CAM`, `K-RENDER`, `C-BASIC`, `C-MAT`, `C-LIGHT`.
7. Software folders:
   - `Rhino 建模\`: case notes and product-specific modeling analyses.
   - `KeyShot 渲染\`: case notes, subtitles, complete KeyShot rule library, and product render analyses.
   - `01-Rhino\`, `02-KeyShot\`, `03-C4D\`: older structured software notes.

Avoid these by default:

- `venv_image_qa\`: local Python environment, not knowledge content.
- `备份\` and `归档\`: historical copies; use only when current files are missing or the user asks for recovery/history.

## Search Commands

Use `rg` first when available:

```powershell
rg -n -i "倒角|圆角|布尔|曲面|收敛点|G2" "<KB_ROOT>" -g "*.md"
rg -n -i "金属|塑料|玻璃|HDRI|三点布光|噪点|采样" "<KB_ROOT>" -g "*.md"
```

Use the bundled script for a compact ranked list:

```powershell
python "scripts\search_kb.py" "倒角 布尔失败" --software rhino
python "scripts\search_kb.py" "截图 问答 路由 下一步" --software rhino
python "scripts\search_kb.py" "系统性 建模 阶段 曲面 布尔 倒角" --software rhino
python "scripts\search_kb.py" "吹风机 手柄 风道 倒角" --software rhino
python "scripts\search_kb.py" "拉丝金属 三点布光 噪点" --software keyshot
python "scripts\search_kb.py" "NetworkSrf 圆角失败 曲线质量" --software rhino
```

## Retrieval Heuristics

For Rhino:

- Command questions: search command names plus product feature words.
- Surface-quality questions: include `曲面`, `G2`, `斑马纹`, `高光`, `连续`, `收敛点`.
- Failure questions: include `失败`, `检查`, `重合面`, `间隙`, `方向`, `封闭`.
- Product analogies: search by product type such as `鼠标`, `手柄`, `耳机`, `剃须刀`, `医疗`.
- Screenshot questions: include both stage words and product words, for example `截图 下一步 曲面 分件` or `吹风机 风道 手柄 倒角`.
- Full-process questions: include `系统性`, `阶段`, and the key operations, then read the system overview before case cards.

For KeyShot:

- Material questions: search material name plus `粗糙度`, `反射`, `折射`, `高光`, `贴图`.
- Lighting questions: search `三点布光`, `HDRI`, `区域光`, `主光`, `辅光`, `轮廓光`.
- Output questions: search `采样`, `降噪`, `通道`, `PNG`, `TIFF`, `分辨率`.
- Realism questions: search product type plus `材质`, `灯光`, `场景`, `相机`.

For C4D:

- Start with `03-C4D\` and `规则索引.md`.
- Use C4D guidance cautiously if the local evidence is thinner than Rhino/KeyShot.

## Grounding Labels

Use these labels internally and, when helpful, in the answer:

- Confirmed from Tier A local KB: directly found in a strong source.
- Confirmed from Tier B local KB: found in a useful but cross-check-needed source.
- Inferred from local KB: not directly stated, but synthesized from related rules.
- General professional advice: useful but not verified in the local KB.

