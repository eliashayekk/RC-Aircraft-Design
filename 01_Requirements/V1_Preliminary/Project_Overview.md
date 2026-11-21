> **Status: Archived V1 preliminary analysis**  
> This document preserves the assumptions, methods, and results used before the balsa construction method and revised mass budget were introduced. It is retained as design history and should not be treated as the current V2 baseline.

# RC Fixed-Wing Aircraft Design Project: V1 Preliminary Archive

A mechanical-engineering-focused RC aircraft project developed through aerodynamic analysis, engineering trade studies, structural design, manufacturing, and flight testing.

The goal is to design and validate a complete fixed-wing aircraft using a documented engineering process rather than a build-first approach.

---

## V1 Preliminary Design Baseline

| Parameter | Current Value |
|---|---|
| Configuration | Conventional fixed-wing RC aircraft |
| Mission | Recreational manual flight |
| Launch | Hand launch |
| Landing | Belly landing |
| Propulsion | Single tractor propeller |
| Estimated mass | 1.10 kg |
| Target stall speed | 6 m/s |
| Wing planform | Rectangular |
| Airfoil | CR001SM |
| Wing area | ~0.369 m² |
| Aspect ratio | 6.5 |
| Wingspan | ~1.55 m |
| Chord | ~0.238 m |
| Sweep | 0° |
| Twist | 0° |
| Dihedral | 0° preliminary |

---

## V1 Preliminary Aerodynamic Results

### Airfoil Study

CR001SM was selected following a low-Reynolds-number comparison against several candidate airfoils.

Final investigated range:

\[
Re \approx 100,000 - 300,000
\]

Typical CR001SM results:

\[
C_{L_{\max}} \approx 1.35 - 1.37
\]

\[
C_m \approx -0.10 \text{ to } -0.11
\]

Its higher negative pitching moment is being carried forward into the tail and trim design.

### Finite-Wing Study

Aspect ratios evaluated:

\[
AR=5.5,\ 6.0,\ 6.5
\]

At constant wing area, AR 6.5 produced the highest aerodynamic efficiency of the three tested configurations while maintaining similar lift and pitching-moment trends.

Selected baseline:

\[
\boxed{AR=6.5}
\]

Approximate finite-wing maximum efficiency:

\[
\left(\frac{L}{D}\right)_{\max}\approx16-17
\]

at approximately:

\[
\alpha\approx4^\circ-5^\circ
\]

---

## Engineering Workflow

The project follows this sequence:

1. Mission and requirements
2. Mass estimation
3. Airfoil trade study
4. Wing sizing
5. 3D aerodynamic analysis
6. Stability and tail sizing
7. Propulsion analysis
8. Structural design
9. CAD
10. Manufacturing
11. Ground testing
12. Flight testing
13. Experimental validation

---

## Tools

**Aerodynamics**
- XFOIL
- XFLR5

**Data Processing**
- Python
- pandas
- openpyxl

**CAD**
- SolidWorks

---

## V1 Archive Status

### Completed
- preliminary mission definition
- preliminary mass estimate
- airfoil trade study
- CR001SM selection
- wing sizing
- aspect-ratio sensitivity study
- AR 6.5 selection
- initial finite-wing analysis
- automated XFLR5 data-processing workflow

### Next
- detailed mass budget
- horizontal-tail sizing
- longitudinal stability
- center-of-gravity range
- static margin
- vertical-tail sizing
- propulsion analysis

---

## Original V1 Project Structure

```text
RC_Aircraft_Project/
├── 00_Project_Overview/
├── 01_Aerodynamics/
├── 02_XFLR5/
├── 03_Stability/
├── 04_Propulsion/
├── 05_Structures/
├── 06_CAD/
├── 07_Manufacturing/
├── 08_Testing/
└── 09_Final_Report/
```
