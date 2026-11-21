> **Status: Archived V1 preliminary analysis**  
> This document preserves the assumptions, methods, and results used before the balsa construction method and revised mass budget were introduced. It is retained as design history and should not be treated as the current V2 baseline.

# V1 Preliminary Wing Aspect Ratio Trade Study

## Objective

The objective of this study was to determine a suitable wing aspect ratio for the selected CR001SM wing while maintaining approximately constant wing area.

The aspect ratio needed to balance:

- aerodynamic efficiency
- induced drag
- wingspan
- structural practicality
- wing slenderness
- low-Reynolds-number performance
- suitability for a recreational RC aircraft

---

## Fixed Parameters

The following parameters were held approximately constant throughout the comparison:

| Parameter | Value |
|---|---:|
| Airfoil | CR001SM |
| Wing area | ~0.369 m² |
| Planform | Rectangular |
| Sweep | 0° |
| Dihedral | 0° |
| Twist | 0° |
| Analysis speed | 6 m/s |
| Analysis method | XFLR5 VLM1 |

---

## Configurations Evaluated

Three aspect ratios were investigated:

\[
AR = 5.5
\]

\[
AR = 6.0
\]

\[
AR = 6.5
\]

For a rectangular wing:

\[
AR=\frac{b^2}{S}
\]

and:

\[
c=\frac{S}{b}
\]

The corresponding geometries were approximately:

| AR | Span | Chord |
|---:|---:|---:|
| 5.5 | 1.43 m | 0.259 m |
| 6.0 | 1.49 m | 0.248 m |
| 6.5 | 1.55 m | 0.238 m |

---

## Analysis Method

Each wing was modeled in XFLR5 using the same CR001SM airfoil and approximately the same total wing area.

The analysis was conducted at:

\[
V = 6\text{ m/s}
\]

corresponding approximately to the low-speed design condition.

A pre-stall angle-of-attack sweep was used.

The comparison focused on:

- \(C_L\) vs \(\alpha\)
- \(C_D\) vs \(\alpha\)
- \(C_L/C_D\) vs \(\alpha\)
- \(C_m\) vs \(\alpha\)
- induced drag
- overall finite-wing efficiency

---

## Results

The lift curves for the three configurations were very similar across the investigated pre-stall range.

This indicated that increasing aspect ratio from 5.5 to 6.5 did not strongly alter the lift response of the wing at a given angle of attack.

The main difference appeared in aerodynamic efficiency.

The higher-aspect-ratio configurations showed lower induced drag and a higher maximum lift-to-drag ratio.

The observed ranking was approximately:

\[
AR\ 6.5 > AR\ 6.0 > AR\ 5.5
\]

in terms of maximum finite-wing aerodynamic efficiency.

The pitching-moment curves remained very similar between the three configurations.

---

## Selected Aspect Ratio

The selected preliminary aspect ratio is:

\[
\boxed{AR = 6.5}
\]

The corresponding geometry is approximately:

\[
\boxed{b \approx 1.55\text{ m}}
\]

\[
\boxed{c \approx 0.238\text{ m}}
\]

\[
\boxed{S \approx 0.369\text{ m}^2}
\]

---

## Rationale

AR 6.5 was selected because it provided:

- the highest aerodynamic efficiency of the tested configurations
- reduced induced drag
- a more slender wing geometry
- only minor changes in lift behavior
- no significant additional pitching-moment penalty within the investigated range
- an acceptable overall wingspan for the current aircraft concept

The increase in span relative to AR 5.5 and AR 6.0 was considered acceptable for the current design stage.

---

## Finite-Wing Performance

For the selected AR 6.5 wing, the preliminary three-dimensional analysis indicated a maximum lift-to-drag ratio of approximately:

\[
\left(\frac{L}{D}\right)_{\max}
\approx 16-17
\]

occurring at approximately:

\[
\alpha \approx 4^\circ-5^\circ
\]

These results represent finite-wing performance and are therefore substantially lower than the two-dimensional airfoil \(L/D\) values because induced drag and finite-span effects are included.

---

## Design Decision

**Decision ID:** D-005

**Selected:** AR 6.5

**Status:** Locked for preliminary wing design

**Associated airfoil:** CR001SM

---

## Limitations

The XFLR5 VLM analysis was used primarily in the attached-flow, pre-stall region.

The method is not considered reliable for deep post-stall behavior.

At higher angles of attack, some operating points could not be fully resolved because:

- the local section lift exceeded available viscous polar data
- XFOIL convergence degraded near stall
- the VLM method itself becomes less appropriate once strong separation occurs

For this reason, the aspect-ratio trade study was based primarily on:

- pre-stall lift behavior
- induced drag
- aerodynamic efficiency
- pitching-moment trends

Final stall behavior will require experimental validation.

---

## Current Wing Baseline

The wing is now provisionally defined as:

| Parameter | Value |
|---|---:|
| Airfoil | CR001SM |
| Wing area | ~0.369 m² |
| Aspect ratio | 6.5 |
| Wingspan | ~1.55 m |
| Chord | ~0.238 m |
| Planform | Rectangular |
| Sweep | 0° |
| Dihedral | 0° preliminary |
| Twist | 0° |

---

## Associated Files

Save supporting figures under:

```text
02_Aerodynamics/V1_Preliminary/02_Wing_Aspect_Ratio/
```
