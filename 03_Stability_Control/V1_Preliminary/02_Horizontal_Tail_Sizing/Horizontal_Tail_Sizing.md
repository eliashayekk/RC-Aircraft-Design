> **Status: Archived V1 preliminary analysis**  
> This document preserves the assumptions, methods, and results used before the balsa construction method and revised mass budget were introduced. It is retained as design history and should not be treated as the current V2 baseline.

# V1 Preliminary Horizontal Tail Sizing

## 1. Objective

The purpose of this study is to establish a preliminary horizontal-tail geometry for the aircraft and prepare the configuration for longitudinal stability and trim analysis.

The horizontal tail must provide sufficient stabilizing and control authority while remaining structurally practical and aerodynamically efficient.

This stage defines the initial tail size and geometry. Final validation will be performed through center-of-gravity, neutral-point, static-margin, trim, and XFLR5 stability analysis.

---

## 2. Wing Reference Geometry

The horizontal tail is sized relative to the current wing baseline.

| Parameter | Value |
|---|---:|
| Wing area, \(S_W\) | 0.369 m² |
| Mean aerodynamic chord, \(\bar c\) | 0.238 m |
| Wing aspect ratio, \(AR_W\) | 6.5 |
| Wingspan, \(b_W\) | 1.55 m |
| Wing airfoil | CR001SM |

---

## 3. Horizontal-Tail Volume Coefficient

The initial horizontal-tail sizing uses the conventional tail-volume relation:

\[
V_H = \frac{S_H l_H}{S_W \bar c}
\]

where:

- \(V_H\) = horizontal-tail volume coefficient
- \(S_H\) = horizontal-tail area
- \(l_H\) = horizontal-tail moment arm
- \(S_W\) = wing area
- \(\bar c\) = wing mean aerodynamic chord

A preliminary value of:

\[
\boxed{V_H = 0.55}
\]

was selected as the initial sizing reference.

This value is not treated as the final stability result. It provides a practical starting point that will later be checked against the complete aircraft stability model.

---

## 4. Tail Moment Arm Study

Several preliminary tail moment arms were considered:

\[
l_H = 0.50,\ 0.55,\ 0.60,\ 0.65\text{ m}
\]

Using:

\[
S_H = \frac{V_H S_W \bar c}{l_H}
\]

the corresponding horizontal-tail areas are:

| Tail moment arm \(l_H\) | Required tail area \(S_H\) |
|---:|---:|
| 0.50 m | 0.0966 m² |
| 0.55 m | 0.0878 m² |
| 0.60 m | 0.0805 m² |
| 0.65 m | 0.0743 m² |

A longer tail arm reduces the tail area required for the same tail-volume coefficient.

---

## 5. Preliminary Tail Moment Arm

The selected preliminary tail moment arm is:

\[
\boxed{l_H = 0.60\text{ m}}
\]

This provides a practical compromise between:

- horizontal-tail size
- fuselage length
- structural weight
- pitching leverage
- overall aircraft proportions

The selected value remains subject to validation once the fuselage and center-of-gravity layout are developed in greater detail.

---

## 6. Preliminary Horizontal-Tail Area

For:

\[
V_H = 0.55
\]

and:

\[
l_H = 0.60\text{ m}
\]

the required horizontal-tail area is:

\[
S_H = \frac{0.55(0.369)(0.238)}{0.60}
\]

\[
\boxed{S_H \approx 0.0805\text{ m}^2}
\]

The horizontal-tail area is therefore approximately:

\[
\frac{S_H}{S_W}
=
\frac{0.0805}{0.369}
\approx 0.218
\]

or:

\[
\boxed{\frac{S_H}{S_W}\approx21.8\%}
\]

of the wing area.

---

## 7. Horizontal-Tail Aspect Ratio

The horizontal-tail aspect ratio does not need to match the main-wing aspect ratio.

The wing uses:

\[
AR_W = 6.5
\]

For the horizontal tail, a lower aspect ratio is appropriate because its primary function is stability and pitch control rather than maximizing cruise efficiency.

The selected preliminary horizontal-tail aspect ratio is:

\[
\boxed{AR_H = 4.0}
\]

The corresponding tail-to-wing aspect-ratio ratio is:

\[
\frac{AR_H}{AR_W}
=
\frac{4.0}{6.5}
\approx 0.62
\]

---

## 8. Horizontal-Tail Geometry

For a rectangular horizontal tail:

\[
AR_H = \frac{b_H^2}{S_H}
\]

Therefore:

\[
b_H = \sqrt{AR_H S_H}
\]

Using:

\[
AR_H = 4.0
\]

and:

\[
S_H = 0.0805\text{ m}^2
\]

gives:

\[
b_H = \sqrt{4(0.0805)}
\]

\[
\boxed{b_H \approx 0.567\text{ m}}
\]

The tail chord is then:

\[
c_H = \frac{S_H}{b_H}
\]

\[
\boxed{c_H \approx 0.142\text{ m}}
\]

---

## 9. Current Horizontal-Tail Baseline

| Parameter | Value | Status |
|---|---:|---|
| Tail volume coefficient, \(V_H\) | 0.55 | Preliminary |
| Tail moment arm, \(l_H\) | 0.60 m | Preliminary |
| Tail area, \(S_H\) | 0.0805 m² | Preliminary |
| Tail-to-wing area ratio | 21.8% | Derived |
| Tail aspect ratio, \(AR_H\) | 4.0 | Selected for preliminary analysis |
| Tail span, \(b_H\) | 0.567 m | Derived |
| Tail chord, \(c_H\) | 0.142 m | Derived |
| Planform | Rectangular | Preliminary |

---

## 10. Current Geometry Summary

The current horizontal-tail geometry is therefore approximately:

\[
\boxed{S_H = 0.0805\text{ m}^2}
\]

\[
\boxed{AR_H = 4.0}
\]

\[
\boxed{b_H = 0.567\text{ m}}
\]

\[
\boxed{c_H = 0.142\text{ m}}
\]

\[
\boxed{l_H = 0.60\text{ m}}
\]

These values define the geometry that will be carried into the first longitudinal stability analysis.

---

## 11. Validation Required

The current horizontal-tail geometry is not yet considered a final aircraft design.

The next stages must verify:

- horizontal-tail airfoil selection
- aircraft center of gravity
- wing aerodynamic center
- aircraft neutral point
- static margin
- tail lift requirement
- trim condition
- CR001SM pitching-moment compensation
- elevator authority
- downwash effects
- complete-aircraft longitudinal stability

The geometry may be adjusted if the stability analysis indicates insufficient or excessive tail authority.

---

## 12. Current Design Status

**Horizontal-tail aspect ratio:** selected for preliminary analysis

\[
\boxed{AR_H = 4.0}
\]

**Horizontal-tail area and tail arm:** preliminary

\[
S_H = 0.0805\text{ m}^2
\]

\[
l_H = 0.60\text{ m}
\]

**Next step:** horizontal-tail airfoil selection followed by longitudinal stability analysis.
