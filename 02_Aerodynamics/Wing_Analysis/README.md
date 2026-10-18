
# Three-Dimensional Wing Aerodynamic Analysis

**Project:** Fixed-Wing RC Aircraft Design  
**Author:** Elias Hayek  
**Institution:** Lebanese University  
**Software:** XFLR5  
**Analysis Method:** Vortex Lattice Method (VLM1)  
**Analysis Velocity:** 6 m/s  
**Status:** Preliminary Numerical Analysis

---

## 1. Project Overview

This study investigates the three-dimensional aerodynamic characteristics of the main wing designed for a manually controlled fixed-wing RC aircraft.

The analysis forms part of a broader aircraft development project involving aerodynamic design, stability and control, structural modeling, manufacturing, and experimental flight testing.

The objective is to evaluate the wing's aerodynamic behavior under the selected simulation conditions and use the results to support subsequent design decisions.

Although the XFLR5 model is named "Initial Plane", the exported aerodynamic results represent the isolated main wing rather than the complete aircraft.

## 2. Analysis Objectives

The primary objectives are to:

- Investigate the relationship between lift coefficient and angle of attack.
- Evaluate aerodynamic drag characteristics.
- Determine the maximum simulated lift-to-drag ratio.
- Examine pitching moment behavior.
- Assess the contribution of different drag components.
- Identify limitations requiring further analysis.
- Support the development of the complete aircraft configuration.

## 3. Wing Configuration

| Parameter | Current Configuration |
|---|---|
| Aircraft type | Fixed-wing RC aircraft |
| Wing position | Mid-wing (planned aircraft installation) |
| Wing planform | Rectangular |
| Wing aspect ratio | 6.5 |
| Selected airfoil | CR001SM |
| Wing configuration | Isolated main wing |
| Analysis velocity | 6 m/s |
| Aerodynamic software | XFLR5 |
| Numerical method | VLM1 |

The configuration is part of an ongoing design process. Wing dimensions, structural details, and manufacturing parameters may be revised during development.

## 4. Numerical Methodology

### 4.1 Simulation Setup

Aerodynamic simulations were performed using XFLR5 with the Vortex Lattice Method (VLM1).

The analysis was conducted at a constant freestream velocity of 6 m/s.

The angle of attack was varied to investigate the wing's aerodynamic response.

### 4.2 Simulation Conditions

| Parameter | Value |
|---|---|
| Analysis method | VLM1 |
| Freestream velocity | 6 m/s |
| Angle-of-attack range | -5° to 11° |
| Number of recorded points | 33 |
| Wing airfoil | CR001SM |

### 4.3 Evaluated Parameters

The exported results were used to investigate:

- Lift coefficient (CL)
- Drag coefficient (CD)
- Lift-to-drag ratio (CL/CD)
- Pitching moment coefficient (Cm)
- Angle of attack
- Drag components

The numerical data were exported from XFLR5 and processed using Python to generate comparison plots.

## 5. Results and Discussion

### 5.1 Lift Characteristics

![Lift Coefficient vs Angle of Attack](Figures/cl_vs_alpha.png)

**Figure 1:** Lift coefficient as a function of angle of attack.

The wing demonstrates an increasing lift coefficient over the investigated angle-of-attack range.

At an angle of attack of 0°, the simulated lift coefficient is approximately:

**CL = 0.353**

The highest recorded lift coefficient is approximately:

**CL = 1.175 at α = 11°**

This represents the maximum value recorded within the simulation range, not a verified stall lift coefficient.

Because VLM does not reliably model flow separation and stall, the true maximum lift coefficient cannot be determined from these results alone.

### 5.2 Drag Characteristics

![Drag Polar](Figures/drag_polar.png)

**Figure 2:** Wing drag polar showing the relationship between drag coefficient and lift coefficient.

The drag polar illustrates how aerodynamic drag varies with lift generation.

As lift increases, induced drag generally increases because of the finite wingspan.

The drag polar provides useful information for evaluating aerodynamic performance and identifying operating conditions associated with relatively low drag.

The results should be interpreted within the assumptions of the numerical model.

### 5.3 Aerodynamic Efficiency

![Lift-to-Drag Ratio](Figures/ld_vs_alpha.png)

**Figure 3:** Lift-to-drag ratio as a function of angle of attack.

The highest simulated lift-to-drag ratio is approximately:

**(L/D)max = 16.62**

This value occurs at:

**α = 4.5°**

The result identifies the most aerodynamically efficient operating point among the simulated conditions.

However, this does not automatically establish the final aircraft's cruise condition, since the complete aircraft will include additional aerodynamic components and may operate at different lift coefficients.

### 5.4 Pitching Moment Characteristics

![Pitching Moment](Figures/cm_vs_alpha.png)

**Figure 4:** Pitching moment coefficient as a function of angle of attack.

The pitching moment coefficient describes the aerodynamic moment about the reference point used in the simulation.

This result contributes to understanding the wing's pitching behavior.

However, the pitching moment of an isolated wing does not determine the longitudinal stability of the complete aircraft.

A full stability assessment requires consideration of:

- Aircraft center of gravity
- Horizontal tail geometry
- Tail moment arm
- Tail incidence
- Complete aircraft pitching moment
- Static margin

Consequently, the present results should not be used alone to establish aircraft longitudinal stability.

### 5.5 Drag Components

![Drag Components](Figures/drag_components_vs_alpha.png)

**Figure 5:** Simulated drag components as functions of angle of attack.

The graph illustrates the variation of the drag contributions reported by XFLR5.

These results help identify the aerodynamic penalties associated with increasing lift and provide useful information for subsequent wing performance evaluation.

The interpretation of each component depends on the aerodynamic model and its treatment of viscous and induced drag.

## 6. Summary of Numerical Results

| Parameter | Recorded Result |
|---|---|
| Analysis method | VLM1 |
| Freestream velocity | 6 m/s |
| Angle-of-attack range | -5° to 11° |
| Number of data points | 33 |
| CL at α = 0° | 0.353 |
| Highest recorded CL | 1.175 |
| Angle at highest recorded CL | 11° |
| Maximum simulated L/D | 16.62 |
| Angle at maximum L/D | 4.5° |

All values represent numerical results under the specified simulation conditions.

They have not yet been validated through physical experiments.

## 7. Engineering Interpretation

The numerical results provide an initial assessment of the aerodynamic behavior of the selected wing configuration.

The principal observations are:

1. The wing generates positive lift at zero geometric angle of attack.

2. Lift increases over the investigated positive angle-of-attack range.

3. The maximum simulated aerodynamic efficiency occurs at approximately 4.5°.

4. The finite-span wing exhibits aerodynamic behavior that differs from the corresponding two-dimensional airfoil.

5. The isolated-wing results provide useful input for subsequent aircraft sizing and stability analysis.

The analysis supports continued investigation of the selected wing configuration but does not establish final aircraft performance.

## 8. Numerical Limitations

The Vortex Lattice Method is a potential-flow-based approach primarily suitable for attached-flow aerodynamic analysis.

Important limitations include:

- Inability to reliably predict viscous flow separation.
- Inability to independently determine the physical stall angle.
- Sensitivity to discretization and geometric assumptions.
- Dependence on the reference quantities used for aerodynamic coefficients.
- Limited representation of complex three-dimensional viscous effects.
- Exclusion of complete-aircraft aerodynamic interactions.

The analysis velocity of 6 m/s must not be interpreted as a verified stall speed.

The aircraft's stall-speed target will require further aerodynamic investigation and experimental validation.

## 9. Future Work

- [x] Develop preliminary wing geometry.
- [x] Select the CR001SM airfoil.
- [x] Perform initial XFLR5 VLM analysis.
- [x] Export aerodynamic polar data.
- [x] Generate aerodynamic performance plots.
- [ ] Document final wing dimensions and reference quantities.
- [ ] Investigate mesh convergence and numerical sensitivity.
- [ ] Compare aerodynamic results across operating speeds.
- [ ] Evaluate complete-aircraft longitudinal stability.
- [ ] Estimate stall speed using an appropriate maximum lift coefficient.
- [ ] Manufacture the wing.
- [ ] Conduct structural and aerodynamic testing.
- [ ] Compare simulations with experimental observations.

## 10. Repository Contents

| File / Folder | Description |
|---|---|
| `README.md` | Technical analysis and interpretation |
| `wing_polar_6ms.csv` | Exported XFLR5 aerodynamic results |
| `plot_wing_polars.py` | Python plotting script |
| `Figures/` | Aerodynamic figures in PNG and PDF formats |

## 11. Conclusion

The three-dimensional aerodynamic analysis establishes an initial numerical performance assessment of the main wing developed for the RC aircraft.

Under the simulated conditions, the wing achieved a maximum recorded lift-to-drag ratio of approximately 16.62 at an angle of attack of 4.5°.

The highest recorded lift coefficient was approximately 1.175 at 11°, representing the upper end of the investigated angle-of-attack range rather than a verified stall condition.

The results provide a foundation for continued wing development, aircraft-level aerodynamic analysis, structural design, and experimental validation.

Further work will focus on investigating numerical sensitivity, evaluating the complete aircraft configuration, and comparing theoretical predictions with measured flight performance.

---

**Elias Hayek**  
Engineering Student | Lebanese University  
Fixed-Wing RC Aircraft Design Project
