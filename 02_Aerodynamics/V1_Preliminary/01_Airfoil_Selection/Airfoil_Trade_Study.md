> **Status: Archived V1 preliminary analysis**  
> This document preserves the assumptions, methods, and results used before the balsa construction method and revised mass budget were introduced. It is retained as design history and should not be treated as the current V2 baseline.

# V1 Preliminary Airfoil Trade Study

## Objective

The objective of this study was to select a suitable wing airfoil for a low-Reynolds-number RC aircraft intended for recreational manual flight.

The selected airfoil needed to provide:

- strong low-speed lift
- good aerodynamic efficiency
- acceptable pitching-moment characteristics
- predictable pre-stall behavior
- consistent performance across the expected Reynolds-number range
- sufficient geometric thickness for practical wing construction

---

## Candidate Airfoils

The following airfoils were evaluated:

- CR001SM
- E205
- NACA 2412
- NACA 23012
- NACA 0012-34
- MH45
- MH60
- CH10
- Clark Y
- additional low-Reynolds-number candidates

---

## Analysis Method

Two-dimensional airfoil polars were generated using XFOIL through XFLR5.

The final comparison focused on the Reynolds-number range:

\[
Re = 100,000,\ 150,000,\ 200,000,\ 250,000,\ 300,000
\]

The same analysis settings were maintained across all candidate airfoils to allow direct comparison.

The primary parameters extracted were:

\[
C_{L_{\max}}
\]

\[
\alpha_{C_{L_{\max}}}
\]

\[
\left(\frac{L}{D}\right)_{\max}
\]

\[
\alpha_{\left(L/D\right)_{\max}}
\]

\[
C_m
\]

A Python post-processing script was used to automate data extraction and reduce manual transcription.

---

## Selection Criteria

The airfoils were compared based on:

1. maximum lift coefficient
2. maximum lift-to-drag ratio
3. pitching-moment coefficient
4. consistency across Reynolds number
5. low-Reynolds-number suitability
6. stall-region behavior
7. structural practicality

No single metric was used in isolation.

---

## Key Findings

### CR001SM

CR001SM produced one of the strongest overall aerodynamic performances across the investigated range.

Typical values were approximately:

\[
C_{L_{\max}} \approx 1.35 - 1.37
\]

with maximum lift-to-drag ratio increasing substantially as Reynolds number increased.

Its main disadvantage was a comparatively negative pitching-moment coefficient:

\[
C_m \approx -0.10 \text{ to } -0.11
\]

This indicates a stronger nose-down pitching tendency than several alternative airfoils.

The penalty was considered manageable and was carried forward into the horizontal-tail and trim design requirements.

---

### E205

E205 produced good aerodynamic efficiency and a significantly smaller negative pitching moment than CR001SM.

Its maximum lift coefficient was lower, making it less attractive for the target low-speed performance.

It remained a strong secondary candidate.

---

### NACA 2412

NACA 2412 provided balanced aerodynamic behavior with moderate lift capability, reasonable efficiency, and manageable pitching moment.

Its overall low-Reynolds-number performance was weaker than CR001SM in the investigated operating range.

---

### MH45 and MH60

The MH-series airfoils showed relatively small pitching-moment coefficients.

This was favorable from a trim perspective, but their overall lift-to-drag performance did not exceed CR001SM over the design range.

---

### NACA 0012-34

The symmetric NACA 0012-34 showed substantially lower maximum lift capability.

This would require greater wing area or a higher stall speed for the same aircraft mass.

It was therefore not preferred for the current mission.

---

### CH10

CH10 demonstrated high maximum lift capability, but its low-Reynolds-number aerodynamic efficiency was poor relative to the main candidates.

It also showed a substantially more negative pitching-moment coefficient.

For the current aircraft, the gain in maximum lift did not justify the associated drag and trim penalties.

CH10 was therefore removed from the shortlist.

---

## Final Shortlist

The final shortlist consisted of:

- CR001SM
- E205
- NACA 2412

These airfoils provided the strongest overall balance for the aircraft mission.

---

## Selected Airfoil

The selected wing airfoil is:

\[
\boxed{\text{CR001SM}}
\]

The selection was based on:

- high maximum lift coefficient
- strong aerodynamic efficiency
- good consistency across the Reynolds-number range
- favorable low-speed performance
- suitability for the required stall-speed target

The primary design penalty is its relatively negative pitching-moment coefficient.

This penalty will be addressed during:

- horizontal-tail sizing
- center-of-gravity placement
- static-margin selection
- trim analysis

---

## Design Decision

**Decision ID:** D-004

**Selected:** CR001SM

**Status:** Locked for preliminary aircraft design

**Next validation stage:** finite-wing analysis and longitudinal stability design

---

## Limitations

The airfoil study is based on numerical XFOIL/XFLR5 analysis.

At low Reynolds numbers and near stall, solver convergence becomes less reliable due to increased flow separation.

Therefore:

- unconverged points were not treated as reliable data
- post-stall behavior was not used as a primary design basis
- final stall characteristics will require experimental validation
- airfoil-level results are not equivalent to full finite-wing performance

Finite-wing effects are analyzed separately using three-dimensional XFLR5 models.

---

## Associated Files

```text
02_Aerodynamics/V1_Preliminary/01_Airfoil_Selection/
├── Airfoil_Trade_Study.md
├── airfoil_analysis.xlsx
├── airfoil_summary.csv
├── analyze_polars.py
└── data/
```
