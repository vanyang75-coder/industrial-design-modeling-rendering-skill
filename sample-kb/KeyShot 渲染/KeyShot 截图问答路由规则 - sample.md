# Sample - KeyShot Screenshot Routing Rules

This is a small public sample. It demonstrates the routing shape only; it is not the full private subtitle-derived knowledge base.

## First Route

When a user uploads a KeyShot screenshot, classify the visible problem before giving parameters:

1. Material: material properties, texture scale, roughness, reflection, bump, normal, transparency.
2. Lighting: HDRI, area lights, highlight shape, rim separation, shadow direction.
3. Camera / composition: focal length, view angle, depth of field, product placement, output ratio.
4. Scene: ground, background, props, interior or studio relationship.
5. Output quality: samples, denoise, GPU, noise, channels, final file format.

## Symptom To Action

| Screenshot symptom | Route axis | Next action | Failure check |
|---|---|---|---|
| Plastic looks flat | Material + lighting | Make one readable soft highlight first, then adjust roughness | If lighting is flat, material tuning will not show shape |
| Metal is not shiny | Material + lighting | Check reflection/roughness and rotate HDRI or add an area light | Do not judge metal under a dull environment |
| Product blends into background | Lighting + scene | Add rim light or separate background brightness | Increasing exposure alone can flatten the image |
| Transparent bottle looks gray | Material + scene | Check transparency, refraction, label opacity, and background contrast | Label mapping errors can look like material errors |
| Render is noisy | Output | Increase final samples and use denoise carefully | Low samples hide fine material and highlight details |

## Keywords

KeyShot, 截图, 路由, 材质, 灯光, 相机, 构图, 场景, 输出, 粗糙度, 反射, HDRI, 采样, 降噪.
