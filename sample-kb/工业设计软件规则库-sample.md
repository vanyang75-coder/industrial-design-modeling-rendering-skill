# Industrial Design Software Rules - Sample

This is a tiny sanitized sample knowledge base for testing the skill. It is original demo content and is not a transcript archive.

## Rhino General Rules

### Boolean Before Fillet

- Trigger: shell or product body needs vents, slots, or panel cuts.
- Action: finish large Boolean cuts before small fillets.
- Failure check: confirm cutters fully penetrate the body and the target is a closed solid.
- Keywords: Rhino, 布尔, 倒角, 圆角, 闭合, 穿透.

### Surface Quality Before Detail

- Trigger: the main shell has visible waves, broken highlights, or uneven transitions.
- Action: simplify curves, check curve direction, and inspect the surface with zebra or highlight analysis before adding panel lines.
- Failure check: reduce control points and rebuild the curve network before trying smaller details.
- Keywords: 曲面, G2, 斑马纹, 高光, 曲线质量.

## KeyShot General Rules

### Plastic Material First Pass

- Trigger: plastic looks flat, fake, or too glossy.
- Action: adjust roughness and reflection after lighting has a clear highlight direction.
- Suggested starting point: medium roughness with soft area light reflection.
- Failure check: if the product still looks flat, rotate the HDRI or add a rim light before over-tuning the material.
- Keywords: KeyShot, 塑料, 材质, 粗糙度, 反射, 区域光.

