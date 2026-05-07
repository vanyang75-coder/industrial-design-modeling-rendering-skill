# Sample - KeyShot System Rendering Overview

This public sample summarizes the workflow shape. A complete installation should connect a richer local knowledge base through `INDUSTRIAL_DESIGN_KB`.

## Why KeyShot Extraction Is Different From Rhino

Rhino guidance is usually geometry-first: reference, curves, surfaces, Boolean operations, fillets, details, and cleanup.

KeyShot guidance is image-first: visual target, material behavior, light shape, camera/composition, scene relationship, and output quality.

## Five-Stage Rendering Chain

1. Visual target: decide product mood, reference image, composition ratio, and main selling angle.
2. Material: separate plastic, metal, glass, fabric, leather, labels, transparency, bump, normal, and texture scale.
3. Lighting: use HDRI or environment for base illumination, then shape highlights with area lights, rim lights, and reflectors.
4. Camera / scene: save the camera, tune focal length, view angle, product distance, ground, background, and optional depth of field.
5. Output: test low-cost previews first, then final samples, denoise, resolution, transparent background, and channels.

## Practical Principle

Do not start by changing every render parameter. Diagnose the visible symptom first, then adjust only the current axis:

- If the material looks fake, check highlight and roughness before texture details.
- If the image is flat, shape light and silhouette before increasing exposure.
- If the reference angle is wrong, save a camera and tune focal length/distance before reworking materials.
- If the final image is noisy, separate preview judgment from final output settings.

## Keywords

KeyShot, 系统性, 渲染, 材质, 灯光, 相机, 构图, 场景, 输出, HDRI, 贴图, 凹凸, 景深, 采样, 降噪.
