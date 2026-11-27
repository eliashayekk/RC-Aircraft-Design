# V2 Wing Airfoil Trade Study

**Decision:** Advance NACA 4412 to the 3D wing study. Keep NACA 2412 as the comparison for trim and drag. Revisit NACA 4415 if the wing needs more spar depth.

## Why change the section?

V1 used CR001SM to establish the preliminary aerodynamic configuration. For the balsa wing, a standard NACA section makes the rib profile easier to generate and reproduce. The V2 screening covered NACA 0008, 0010, 0012H, 2412, 4412 and 4415.

## Inputs and method

- Design mass 0.630 kg, rectangular wing area 0.3689 m² and chord 0.238 m.
- Assumed air density 1.225 kg/m³ and dynamic viscosity 1.81 × 10⁻⁵ Pa·s.
- The [initial screening workbook](processed/airfoil_comparison.xlsx) records XFLR5 Type 1 section polars with Ncrit = 9 and Mach = 0.00. It includes the combined polar data, summary and comparison charts.
- The initial sweeps sometimes ended before the lift peak was clear. The three finalists were rerun with an approximate requested angle range of −10° to +23°. The extended-sweep summary below comes from the design handoff. Original exports and exact run settings are needed to verify convergence, the angle range actually returned and the points used for interpolation.

Reynolds number is calculated as Re = ρVc/μ. Use the target speeds to select the relevant polar range. The workbook's exported cases are shown separately because its high-speed Reynolds labels differ slightly from the nominal mapping.

| Airspeed | Approximate calculated Re | Initial workbook Re |
| --- | ---: | ---: |
| 6 m/s | 97,000 | 97,000 |
| 8 m/s | 129,000 | 129,000 |
| 10 m/s | 161,000 | 161,000 |
| 12 m/s | 193,000 | 193,000 |
| 15 m/s | 242,000 | 241,000 |
| 20 m/s | 322,000 | 323,000 |
| Around 11.2 m/s | 180,000 | 180,000 (additional case) |

At 6 m/s, the calculated aircraft lift coefficient needed for steady level flight is **0.760** from C_L,req = 2mg/(ρV²S), using g = 9.81 m/s². It serves as the section comparison point. Increased mass or reduced wing area would increase the required lift coefficient. A section lift ratio is a screening metric. The finite wing has varying section lift across its span, and aircraft trim adds a tail load.

## Extended finalist results near Re 97,000

Approximate values reported in the V2 handoff.

| Rank | Airfoil | Section C_l,max | C_l,max / C_L,req | Angle near lift peak | Section L/D at required lift | Approx. section C_m |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | NACA 4412 | 1.482 | 1.95 | 13.5° | 40.3 | −0.105 |
| 2 | NACA 2412 | 1.263 | 1.66 | 11.5° | 44.3 | −0.065 |
| 3 | NACA 4415 | 1.402 | 1.85 | 16° | 35.2 | Unreported |

The handoff does not specify the angle or lift coefficient at which the approximate C_m values were sampled. Keep them as qualitative trim indicators until the extended data and sampling convention are available.

In the initial workbook at Re 97,000, the largest sampled C_l values were 1.3754 for 4412 and 1.3866 for 4415. Both initial angle sweeps ended at 12°, so the initial workbook cannot establish the reported peaks at 13.5° and 16°. Use the handoff ranking as the current selection basis and the workbook as evidence of the initial screening.

## Trade-offs

- **NACA 4412** gives the largest reported low-speed lift margin and a nominal 28.6 mm maximum section thickness at the design chord. Its more negative pitching moment increases the tail and trim burden relative to 2412. Its section L/D at the comparison point is also lower.
- **NACA 2412** has the best reported section L/D at the comparison point and a milder nose-down pitching moment. Selecting it would reduce the reported section lift margin but could improve trimmed aircraft efficiency. Compare both wings with the same geometry, then compare trim with the same tail and CG assumptions.
- **NACA 4415** offers a nominal 35.7 mm maximum section thickness and a higher reported angle at peak lift. Its lower reported efficiency at the comparison point makes it a candidate if the structure needs the additional depth.

## Validation

The 2D results describe isolated sections. The [3D wing study](../Wing_3D/README.md) will check spanwise loading, induced drag, and the limits of the stall prediction. Then the full-aircraft model will check tail load, trim, incidence, static margin and control. The 6 m/s target remains a requirement pending finite-wing analysis and validation.

Archive the original [polar exports](raw_polars/README.md), the matching [analysis script](scripts/README.md) and any separately generated [figures](figures/README.md) with the relevant run.
