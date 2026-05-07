# Screenshot Diagnosis

Use this reference when the user uploads a Rhino, KeyShot, C4D, or related product modeling/rendering screenshot and asks what to do next, what is wrong, or how to continue.

## Vision Capability Policy

Use the best available image understanding path:

1. Inspect the uploaded image directly at the highest detail available.
2. If a stronger image2-style vision recognition engine is available in the runtime, use it for reading UI state, viewport content, small text, icons, panels, and visible artifacts.
3. If text is small or blurry, use OCR when available or ask for a crop of the decisive region.
4. Do not use image generation/editing tools to infer missing UI state.
5. Do not claim exact model topology, hidden objects, material parameters, or render settings unless they are visible or provided by the user.

## First Pass: Identify Context

Extract these fields before giving advice:

- Software: Rhino, KeyShot, C4D, or unknown.
- Workspace area: viewport/modeling, material panel, object/layer tree, render preview, render settings, command line/status bar, error dialog.
- Visible task: creating curves, surfacing, Boolean, bevel/fillet, material assignment, lighting, camera, render output, post-processing.
- Visible state: selected object, active command/prompt, view mode, object type, render noise, over/under exposure, broken material, visible seam, failed operation.
- User intent: next step, problem diagnosis, parameter choice, cleanup, or learning explanation.

If the screenshot has no decisive UI text, infer from geometry/render symptoms but mark it as visual inference.

## Screenshot-To-Query Bridge

Turn visual observations into search keywords:

### Rhino

- Command/status line mentions Boolean, 差集, 并集, 失败 -> search `布尔 失败 重合面 间隙 穿透`.
- Bevel/fillet preview fails, red/odd edges, tiny corners -> search `圆角失败 倒角 半径 边缘 曲面质量`.
- Surface ripples, highlight breaks, zebra issues -> search `曲面质量 G2 斑马纹 曲率梳 NetworkSrf`.
- NetworkSrf/Sweep/Loft workflow -> search `NetworkSrf Sweep2 Loft 曲线质量 方向 相交`.
- Product shell, wall thickness, offset surfaces -> search `抽离 等距面 壁厚 曲面方向`.
- Symmetric product half model -> search `对称 镜像 图层 捕捉`.

### Rhino Product-Type Routing

When a Rhino screenshot shows product geometry rather than only a command dialog, classify both product family and modeling stage before choosing advice. Prefer `Rhino 截图问答路由规则 - 字幕证据版.md`, `Rhino 系统性建模技巧总纲 - 字幕归纳版.md`, and `Rhino 案例建模参考卡 - 字幕提取版.md` for these routes.

Product family cues:

- Hair dryer / airflow handheld product: long handle, nozzle, intake grille, vent slots, trigger/button region -> search `吹风机 风道 手柄 出风口 格栅 壳体 分件`.
- Bottle / revolved container: circular mouth, cap, cylindrical body, bottom foot ring, thickness lip -> search `水杯 旋转容器 瓶盖 瓶口 壁厚 旋转`.
- Handheld electronics or mouse-like shell: palm surface, parting line, side buttons, base shell -> search `鼠标 手持 曲面 分模线 结构线 按键`.
- Shaver / grille body: dense slots, perforated panels, grip shell, end cap -> search `剃须刀 格栅 孔阵列 壳体 倒角`.
- Earphone / wearable small part: small organic shell, soft transitions, mirror symmetry, acoustic holes -> search `耳机 穿戴 小曲面 孔位 圆角`.
- Medical / protection / hard-surface casing: clean casing, protective lip, panel seams, handle and interface detail -> search `医疗 防护 外壳 面板 结构线`.
- Vehicle / motorcycle / transport shell: large continuous body panels, wheel/cover relationship, aerodynamic fairing -> search `交通 摩托 车壳 流线 外壳 分件`.

Modeling stage cues:

- Only reference image or primitive volumes: answer with proportion setup, centerline, blockout layers, and silhouette locking.
- Curves visible but no surfaces: answer with curve hierarchy, fewer control points, section curves, direction, and closed curve checks.
- Main surfaces visible but details missing: answer with surface continuity, trimming/splitting, structure lines, and panel planning.
- Boolean cuts or vents in progress: answer with cutter penetration, closed solids, operation order, duplicate backup, and edge checks.
- Fillets/chamfers failing or not started: answer with large-before-small order, radius reduction, sliver surface cleanup, and zebra/highlight checks.
- Decals, seams, screws, labels, and small slots: answer with separate detail geometry, projection/flow placement, and render-readability scale.

### KeyShot

- Noisy render/preview -> search `噪点 采样 降噪 渲染优化`.
- Metal looks flat or not reflective -> search `金属 粗糙度 反射 各向异性 灯光`.
- Plastic looks fake -> search `塑料 高光 粗糙度 材质`.
- Glass looks black/opaque -> search `玻璃 折射 薄壁 焦散 透明`.
- Overexposed or dull lighting -> search `三点布光 HDRI 区域光 主光 辅光 过曝`.
- Composition/camera issue -> search `相机 焦距 景深 构图 产品渲染`.

### C4D

- Object/generator/deformer state -> search `C4D 参数化 多边形 建模`.
- Material/texture problem -> search `C4D 材质 纹理 Roughness 金属度 缺失贴图`.
- Render/light problem -> search `C4D 灯光 渲染 Redshift Octane 区域光 HDRI`.

## Diagnosis Output Pattern

Use this shape for screenshot answers:

```markdown
我先按截图判断：
- 软件/场景：
- 当前状态：
- 最可能的问题：

下一步建议：
1. ...
2. ...
3. ...

如果这一步失败：
- 检查 ...
- 改成 ...

依据：
- 截图可见：
- 本地知识库：
- 推断边界：
```

For simple "what should I do next?" questions, shorten the answer:

```markdown
下一步先做 X。截图里 Y 还没完成/看起来有问题，所以先不要做 Z。
具体操作：1... 2... 3...
```

## What To Ask For

Ask for more information only when it changes the next action:

- Rhino: command line/status area, selected object properties, layers/object type, close-up of failed edge or curve network.
- KeyShot: material graph/properties, environment/light panel, render settings, close-up of artifact.
- C4D: object manager, attributes panel, material editor, render settings, console/error text.

Prefer one targeted request:

`请再截一下右侧属性/材质面板，或者把问题边缘放大截一张。`

## Common Screenshot Diagnoses

### Rhino

- Boolean failed: likely tool body does not fully intersect, coincident faces, tiny gaps, non-closed solids, wrong operation order. Suggest backup, check intersections, ensure cutter fully penetrates, run edge checks, then retry large operations before small details.
- Fillet failed: likely radius too large, adjacent faces too small/poor quality, sharp angle, bad edge selection, or tolerance mismatch. Suggest reducing radius, splitting edges, improving base surfaces, and beveling large radii before small radii.
- Surface looks wavy: likely poor curve quality, too many control points, non-smooth curve network, or continuity mismatch. Suggest CurvatureGraph/Zebra checks, rebuild curves, align directions, and lower G2 to G1 only when needed.

### KeyShot

- Render noisy: likely low samples, difficult glass/metal/caustics, tiny bright lights, or denoise mismatch. Suggest low-sample testing, final 32-64+ samples as starting range, adjust lighting size, and use denoise carefully.
- Material looks fake: likely roughness/reflection mismatch or lighting not revealing reflections. Suggest material-specific ranges from local KB and adjust HDRI/area lights before over-tweaking material.
- Product has black faces or odd shading: likely normal/material assignment/import issue. Suggest checking normals, part materials, and model cleanup before render settings.

### C4D

- Viewport/render mismatch: likely editor/render visibility, generator state, renderer setting, or material assignment mismatch.
- Lighting too harsh or flat: use area light/HDRI roles and three-point logic, then tune renderer-specific samples.

