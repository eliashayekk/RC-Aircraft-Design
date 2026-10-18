
# Airfoil Selection and Aerodynamic Analysis

**Project:** Fixed-Wing RC Aircraft Design  
**Author:** Elias Hayek  
**Software:** XFLR5, Python, Microsoft Excel  
**Status:** Preliminary Analysis Completed

---

## 1. Objective

The objective of this study is to evaluate candidate airfoils for a fixed-wing RC aircraft and identify a suitable configuration based on aerodynamic performance and the aircraft's mission requirements.

The analysis focuses on low-Reynolds-number aerodynamics, particularly lift generation, aerodynamic efficiency, pitching moment characteristics, and performance across different operating conditions.

## 2. Aircraft Design Requirements

The airfoil selection process was guided by the following aircraft requirements:

| Parameter | Target |
|---|---|
| Aircraft Configuration | Mid-wing, rectangular wing |
| Wing Aspect Ratio | 6.5 |
| Target Stall Speed | 6 m/s |
| Flight Characteristics | Stable, maneuverable |
| Launch Method | Hand launch |
| Landing Method | Belly landing |
| Endurance Objective | 30 minutes |

These requirements form the basis for evaluating the aerodynamic suitability of candidate airfoils.

## 3. Airfoil Candidates

The following airfoils were investigated during the preliminary selection process:

- CR001SM
- S1223
- FoilDF-101
- CH10

The final selected airfoil for the current aircraft configuration is **CR001SM**.

## 4. Analysis Methodology

Two-dimensional airfoil simulations were conducted using XFLR5.

The investigated Reynolds numbers included:

- Re = 77,000
- Re = 100,000
- Re = 150,000
- Re = 200,000

The analysis considered the following aerodynamic coefficients:

| Parameter | Description |
|---|---|
| Cl | Lift coefficient |
| Cd | Drag coefficient |
| Cl/Cd | Aerodynamic efficiency |
| Cm | Pitching moment coefficient |
| Alpha | Angle of attack |
| Reynolds Number | Ratio of inertial to viscous forces |

Polar data exported from XFLR5 were processed using Python and Excel.

## 5. Data Processing

A Python script, `analyze_polars.py`, was developed to process exported aerodynamic polar data.

The processing workflow includes:

1. Reading exported XFLR5 polar files.
2. Extracting aerodynamic coefficients.
3. Organizing results across Reynolds numbers.
4. Generating a consolidated aerodynamic summary.
5. Supporting comparison between candidate airfoils.

The processed results are stored in `airfoil_summary.csv`.

The Excel workbook contains additional analysis and visualization of the aerodynamic data.

## 6. Airfoil Selection

**Selected Airfoil: CR001SM**

CR001SM was selected during the preliminary aerodynamic design process.

The selection was made in consideration of the aircraft's intended operating conditions, aerodynamic performance, and handling objectives.

The quantitative justification will be expanded using the simulation results, including:

- Lift generation at relevant operating conditions
- Drag characteristics
- Lift-to-drag performance
- Pitching moment behavior
- Performance sensitivity to Reynolds number

Selection should be revisited if subsequent aircraft-level analysis or flight testing reveals limitations.

## 7. Repository Contents

| File / Folder | Description |
|---|---|
| `raw_polars/` | Original XFLR5 aerodynamic polar exports |
| `airfoil_summary.csv` | Consolidated aerodynamic results |
| `airfoil_analysis.xlsx` | Excel analysis workbook |
| `../Python_Scripts/analyze_polars.py` | Python polar processing script |

## 8. Analysis Limitations

XFLR5 provides numerical aerodynamic predictions rather than experimental measurements.

Potential limitations include:

- Sensitivity to Reynolds number
- Transition and separation modeling assumptions
- Numerical convergence
- Differences between 2D airfoil and 3D wing behavior
- Manufacturing imperfections
- Differences between predicted and actual flight conditions

The results should therefore be evaluated alongside three-dimensional aircraft analysis and eventual flight-test observations.

## 9. Future Work

- [x] Investigate candidate airfoils
- [x] Export XFLR5 polar data
- [x] Develop Python data-processing workflow
- [x] Generate consolidated aerodynamic summary
- [x] Select preliminary wing airfoil
- [ ] Publish quantitative airfoil comparison tables
- [ ] Add lift and drag polar figures
- [ ] Document detailed airfoil selection justification
- [ ] Compare theoretical predictions with flight-test results

## 10. Conclusion

This study establishes the preliminary aerodynamic basis for wing airfoil selection.

The CR001SM airfoil has been selected for further aircraft-level analysis and development.

Future work will focus on quantitative validation, integration with the complete aircraft configuration, and evaluation through physical flight testing.

---

**Elias Hayek**  
Lebanese University  
Fixed-Wing RC Aircraft Engineering Project
