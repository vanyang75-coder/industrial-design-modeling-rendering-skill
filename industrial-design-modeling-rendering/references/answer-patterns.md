# Answer Patterns

Use these patterns to turn retrieved rules into useful user-facing output.

## Modeling Question

Use when the user asks how to model a feature, product, or Rhino operation.

Structure:

1. One-sentence route: name the modeling strategy.
2. Preconditions: units, reference image, closed curves, symmetry, layers, snaps.
3. Steps: 5-9 numbered actions using Rhino terms.
4. Parameters: only include grounded or safe starting ranges.
5. Checks: geometry closure, continuity, bevel order, normals, zebra/highlight check.
6. Common failures: what to inspect when it breaks.
7. Sources: mention key source file or rule ID if used.

High-value Rhino rules from the current KB:

- Closed curves before extrusion; otherwise Rhino may create surfaces instead of solids.
- Back up original geometry before Boolean operations.
- Boolean order matters: perform large operations before small detail operations.
- Boolean failure often comes from coincident faces or tiny gaps.
- Product edge bevels often start around 0.2-0.5 mm; small details may need around 0.1 mm.
- Bevel large radii before small radii, and external edges before internal edges.
- Use structure curves, offset surfaces, and surface direction checks for wall thickness and surface splitting.
- Use zebra/highlight checks for surface quality and G2-like visual continuity.

## Screenshot Diagnosis

Use when the user uploads software screenshots. Read `screenshot-diagnosis.md` first.

Structure:

1. Visual observation: software, panel/viewport, selected state, visible artifact or active command.
2. Diagnosis: most likely current state or issue, with confidence.
3. Next action: 1-3 concrete steps that the user can do immediately.
4. If it fails: one compact troubleshooting branch.
5. Evidence note: screenshot-visible facts, local KB source, inference boundary.

Keep the answer short unless the user asks for teaching detail. The user is usually mid-operation and needs the next move, not a lecture.

## Rhino Screenshot-First From Subtitle Corpus

Use when the screenshot or reference image is about Rhino product modeling and the user asks how to continue, how to model it, or what is wrong.

Structure:

1. Visual state: name the visible product family and modeling stage.
2. Route: choose a case family from the 47-video Rhino subtitle corpus.
3. Next action: give 1-3 steps for the current stage only.
4. Why now: explain the modeling reason in one sentence.
5. Failure check: give the most likely thing that will break and how to inspect it.
6. Expansion: if the user asked for a detailed process, continue with staged workflow from reference setup to details/render prep.

Short form:

```markdown
我先按截图判断：这是 X 类产品，目前在 Y 阶段。下一步不要急着做 Z，先把 A 做准。

具体做法：
1. ...
2. ...
3. ...

失败时看这里：...
依据：字幕案例里更接近的是 ...；截图里可确认的是 ...；未显示的部分我按常规建模推断。
```

Detailed Rhino case answer:

```markdown
路线：先锁比例和大体块，再分件做主曲面，最后用结构线/布尔/倒角完成工业设计细节。

1. 参考与比例
2. 大体块
3. 主曲面
4. 分件与结构线
5. 孔、槽、格栅、按键
6. 倒角与连续性检查
7. 渲染前清理

关键检查：闭合、穿透、曲线点数、面方向、倒角顺序、斑马纹/高光。
```

Do not turn every screenshot into a full tutorial. Most screenshot help should be a compact next-step diagnosis unless the user explicitly asks for the full modeling flow.

## Rendering Recipe

Use when the user asks for KeyShot material, lighting, camera, output, or realistic product rendering.

Structure:

1. One-sentence visual target.
2. Model prep: normals, broken surfaces, units, part/material naming.
3. Material recipe: material type, reflection, roughness, IOR or maps when relevant.
4. Lighting recipe: HDRI or three-point setup, light roles, color temperature if relevant.
5. Camera/scene: focal length, product height, background, ground plane, depth of field if needed.
6. Render output: sampling, denoise, file format, channels.
7. Troubleshooting: noise, fake material, overexposure, black faces, slow render.

High-value KeyShot rules from the current KB:

- Metal: reflection 80-100%, roughness 0-20%, anisotropy for brushed direction.
- Plastic: base diffuse color, highlight 30-60%, roughness 10-30%.
- Glass: IOR 1.5-1.7, dispersion 30-60, thin-wall option for thin glass.
- Fabric: normal map for weave, fiber direction, roughness 60-80%.
- Three-point lighting: key + fill + rim; common key/fill ratio 2:1 or 3:1.
- Main light often starts around daylight color temperature, with warmer fill if needed.
- Test renders can use low samples; final renders often move to 32-64 samples.
- PNG with transparency is useful for product output; TIFF is useful for print.
- Output useful channels such as reflection, refraction, shadow, ID, and normal when post-processing matters.

## Troubleshooting Flow

Use when the user asks why something failed or looks wrong.

1. Ask what software and operation if unclear.
2. Give a ranked diagnostic checklist.
3. For each likely cause, give one concrete inspection action and one fix.
4. End with a minimal recovery path.
5. If the source is not Tier A, say that the diagnosis is inferred and ask for a screenshot/model state only if it would change the next action.

Rhino failure checklist:

- Curve not closed.
- Surface direction is wrong.
- Coincident faces or tiny gaps.
- Bevel radius is too large for local geometry.
- Operation order created tiny sliver surfaces.
- Object scale or unit mismatch.

KeyShot failure checklist:

- Normals are reversed or broken.
- Material assigned to wrong part or linked parts unexpectedly.
- Roughness/reflection values are extreme.
- HDRI angle does not create useful reflections.
- Too many lights cause overexposure or multi-shadow artifacts.
- Samples are too low or denoise hides fine detail.

## Rule Extraction

Use when the user provides a tutorial, transcript, case note, or asks to expand the knowledge base.

Do not write into the user's configured knowledge base unless explicitly requested or confirmed.

Extract in this format:

```markdown
## Source
- Title:
- URL/file:
- Software:
- Product type:

## Reusable Rules
1. **Rule name**
   - Category:
   - Trigger:
   - Action:
   - Parameter:
   - Failure check:
   - Confidence: high/medium/low

## Case Workflow
1. ...

## Keywords
- ...
```

Prefer problem-oriented categories over only software categories when the rule answers a common design problem.

## Evidence Note

Add a compact evidence note when the answer depends on local KB quality:

```markdown
依据：本地知识库 Tier A / Tier B / 推断
来源：文件名或规则 ID
边界：哪些参数需要按产品尺寸、软件版本或实际模型状态调整
```

Do not overuse source notes for simple answers, but include them for parameter ranges, troubleshooting, manufacturing, or advanced surface decisions.

