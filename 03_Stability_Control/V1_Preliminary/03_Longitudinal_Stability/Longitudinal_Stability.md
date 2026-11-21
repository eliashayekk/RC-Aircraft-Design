> **Status: Archived V1 preliminary analysis**  
> This document preserves the assumptions, methods, and results used before the balsa construction method and revised mass budget were introduced. It is retained as design history and should not be treated as the current V2 baseline.

# V1 Preliminary Longitudinal Stability Analysis

## Initial Center of Gravity

Wing mean aerodynamic chord:

c̄ = 0.238 m

Initial CG position:

x_CG = 0.25 c̄

x_CG = 0.0595 m

The initial CG is therefore positioned 59.5 mm aft of the wing leading edge.

This position is used only as the starting point for the longitudinal stability analysis. The final CG location will be determined after evaluating the aircraft neutral point and static margin.

## Initial Static Margin

Using the exported XFLR5 polar over the linear pre-stall region:

dCL/dα = 0.08499 per degree

dCm/dα = -0.01981 per degree

Therefore:

dCm/dCL = -0.233

Static margin:

SM = 23.3%

The initial CG position therefore produces a strongly statically stable configuration.

Status:
Too conservative for final selection. CG sensitivity study required.

| CG position | \(dC_L/d\alpha\) | \(dC_m/d\alpha\) | Static margin |
|---:|---:|---:|---:|
| 25% MAC | 0.08499/° | -0.01981/° | **23.3%** |
| 30% MAC | 0.08499/° | -0.01552/° | **18.3%** |
| 35% MAC | 0.08499/° | -0.01123/° | **13.2%** |
| 40% MAC | 0.08499/° | -0.00694/° | **8.16%** |

## Preliminary Trim Condition

Selected horizontal-tail incidence:

i_H = -2°

At the selected CG position of 35% MAC, the aircraft trims at approximately:

alpha_trim = 3.2°

At trim:

CL ≈ 0.56
CD ≈ 0.039
L/D ≈ 14–15
Cm ≈ 0

For the nominal aircraft mass of 0.934 kg and wing area of 0.369 m², this trim lift coefficient corresponds to a level-flight speed of approximately:

V_trim ≈ 8.5 m/s

Status:
Accepted as the preliminary trim condition.
