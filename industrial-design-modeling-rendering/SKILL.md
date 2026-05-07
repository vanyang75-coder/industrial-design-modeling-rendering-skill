---
name: industrial-design-modeling-rendering
description: Screenshot-first industrial design modeling and rendering assistance for Rhino, KeyShot, C4D, uploaded software screenshots, next-step guidance, visual troubleshooting, product modeling workflows, material and lighting recipes, rendering diagnostics, Rhino and KeyShot subtitle-derived evidence, product-type routing, systematic modeling/rendering techniques, rule extraction from tutorials, and questions that should use a local industrial design software knowledge base.
---

# Industrial Design Modeling Rendering

Use this skill to answer practical industrial design modeling and rendering questions, especially when the user uploads a Rhino, KeyShot, or C4D software screenshot and asks what to do next or what is wrong. For Rhino product modeling, prefer the 2026-05-07 subtitle-derived case corpus and its system summaries when the question involves product type, modeling phase, or next-step diagnosis. For KeyShot product rendering, prefer the 2026-05-08 subtitle-derived KeyShot corpus when the question involves material, lighting, camera, scene, output, screenshot routing, or visual troubleshooting.

## Core Workflow

1. Classify the request before answering:
   - Screenshot diagnosis: uploaded software UI, viewport, render preview, command line, material panel, object tree, or error state.
   - Rhino modeling: surfaces, solids, bevels, product structure, command sequence, geometry troubleshooting.
   - KeyShot rendering: materials, lighting, camera, scene setup, output, noise, speed, realism.
   - C4D workflow: modeling, material, lighting/rendering, animation or motion-oriented product visualization.
   - Cross-software workflow: Rhino model preparation plus KeyShot/C4D rendering handoff.
   - Knowledge-base maintenance: extracting reusable rules from tutorials or organizing cases.
2. For uploaded screenshots, read `references/screenshot-diagnosis.md` first. Use the available vision/image understanding capability at high detail when possible. If a future environment exposes a stronger image2-style vision engine, use it for visual state recognition; do not use image generation tools to invent or edit UI evidence.
3. Read `references/content-audit.md` before treating the local knowledge base as authoritative. Use its evidence tiers and known gaps.
4. Ground the response in the local knowledge base whenever the request is about known modeling/rendering practice. Read `references/knowledge-map.md` for source priority and search patterns.
5. Use `scripts/search_kb.py` for quick retrieval when keyword search is enough. Prefer direct file reads after search results identify likely source files.
6. Load `references/answer-patterns.md` before producing detailed modeling steps, render recipes, troubleshooting flows, screenshot diagnoses, or rule-extraction output.
7. Separate what is visually observed, what is inferred, and what is confirmed from the knowledge base.
8. Do not claim to operate Rhino, KeyShot, C4D, or browser/plugin features unless the current environment actually provides that capability. Provide actionable manual steps instead.

## Rhino Screenshot Loop

When the user uploads a Rhino screenshot or product reference image and asks "下一步怎么做 / 这里有什么问题 / 这个产品怎么建":

1. Observe: identify visible software state, selected geometry, curve/surface/solid stage, product type, and the likely operation currently blocked.
2. Route: classify the product into a local case family such as `吹风机/风道手持`, `水杯/旋转容器`, `鼠标/手持曲面`, `耳机/穿戴小件`, `剃须刀/格栅机身`, `医疗/防护硬表面`, `交通/大型外壳`.
3. Retrieve: search the new Rhino subtitle-derived sources first for product analogies and stage workflow, then fall back to older rule libraries.
4. Answer: give the next 1-3 actions, the reason for doing them now, and one compact failure check. Expand into a full modeling sequence only when the user asks for detail.
5. Boundaries: mark hidden topology, exact dimensions, unshown command prompts, and unverified parameters as inference.

## KeyShot Screenshot Loop

When the user uploads a KeyShot screenshot, render preview, or product reference image and asks "下一步怎么调 / 为什么不好看 / 材质或灯光哪里有问题":

1. Observe: identify whether the screenshot shows render preview, material/properties, environment/light panel, camera settings, render settings, or output artifacts.
2. Route: classify the issue into `材质`, `灯光`, `相机/构图`, `场景`, or `输出质量`. KeyShot extraction is visual-symptom driven, not command-sequence driven.
3. Retrieve: search the KeyShot subtitle-derived sources first when a full local KB is connected, then fall back to sample rules and general professional inference.
4. Answer: give the next 1-3 adjustments only for the current axis, with one failure check. Do not list every possible parameter unless the user asks for a full recipe.
5. Boundaries: mark hidden material graph settings, exact numeric values, unavailable render settings, and unshown panels as inference.

## Retrieval Rules

Start broad, then narrow:

1. Use high-confidence sources from `references/content-audit.md` first.
2. Use the unified rule library for first-pass answers.
3. For Rhino product modeling, prioritize these 2026-05-07 subtitle-derived sources:
   - `Rhino 字幕证据索引 - 100个犀牛实战案例建模教程.md`
   - `Rhino 系统性建模技巧总纲 - 字幕归纳版.md`
   - `Rhino 截图问答路由规则 - 字幕证据版.md`
   - `Rhino 案例建模参考卡 - 字幕提取版.md`
   - `rhino-video-clean-index.json`
4. For KeyShot product rendering, prioritize these 2026-05-08 subtitle-derived sources:
   - `KeyShot 字幕证据索引 - 100个KS实战案例渲染教程.md`
   - `KeyShot 系统性渲染技巧总纲 - 字幕归纳版.md`
   - `KeyShot 截图问答路由规则 - 字幕证据版.md`
   - `KeyShot 案例渲染参考卡 - 字幕提取版.md`
   - `keyshot-video-clean-index.json`
5. Use the problem-driven library when the user describes a symptom or practical design problem, but treat it as a taxonomy unless detailed rules are present.
6. Use software-specific folders for detailed examples and product-type analogies.
7. Use rule indexes for category navigation, not as proof that every claimed rule exists in full detail.
8. Avoid backup, archive, and virtual-environment folders unless the user asks for historical recovery or the current sources are missing.
9. If no good match appears, say that the local knowledge base did not contain a close match and provide a reasoned workflow as an inference.

When searching Chinese terms, include synonyms. Examples:

- Rhino: `倒角 圆角 布尔 曲面 流动 抽离 结构线 收敛点 G2 斑马纹 分模线`
- Rhino stage terms: `参考图 比例 块面 放样 双轨 扫掠 曲面过渡 分件 结构线 布尔 倒角 细节`
- KeyShot: `金属 塑料 玻璃 材质 粗糙度 HDRI 三点布光 区域光 噪点 采样 通道`
- KeyShot screenshot route terms: `材质 灯光 相机 构图 场景 输出 贴图 凹凸 法线 透明 景深 分辨率`
- C4D: `参数化 多边形 材质 灯光 渲染 动画 MoGraph Redshift`
- Product types: `鼠标 耳机 手柄 相机 剃须刀 吹风机 风道 水杯 旋转容器 灭火器 医疗 防护 交通 产品`

## Answer Discipline

For user-facing answers, prefer concise Chinese unless the user asks otherwise. Make outputs executable:

- Give the shortest useful route first.
- For screenshots, lead with what is visible, the most likely current state, and the next 1-3 actions.
- Include exact parameter ranges only when grounded or clearly marked as suggested starting values.
- Add common failure checks for geometry/rendering problems.
- Mention source files or rule IDs when they materially support the answer.
- Ask for a crop, higher-resolution screenshot, or second screenshot only when the current view hides decisive information such as the command line, layer/object tree, material panel, render settings, or problem area.

Before writing new notes into the user's configured knowledge base, ask for confirmation unless the user explicitly requested that target.

