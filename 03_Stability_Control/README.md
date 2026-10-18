
# Aircraft Stability and Control Analysis

**Project:** Fixed-Wing RC Aircraft Design  
**Author:** Elias Hayek  
**Software:** XFLR5  
**Status:** Preliminary Analysis

## 1. Objective

This study investigates the longitudinal stability and control characteristics of a fixed-wing RC aircraft with a conventional tail configuration.

The analysis focuses on the aircraft's pitching moment behavior, center of gravity, horizontal tail configuration, and longitudinal trim.

## 2. Aircraft Configuration

| Parameter | Configuration |
|---|---|
| Wing position | Mid-wing |
| Wing aspect ratio | 6.5 |
| Wing airfoil | CR001SM |
| Tail configuration | Conventional |
| Horizontal tail aspect ratio | 4 |
| Control system | Manual RC |

## 3. Stability Analysis

Longitudinal static stability is evaluated by examining the variation of pitching moment coefficient with angle of attack.

For the conventional sign convention, a negative pitching moment slope indicates a restoring pitching moment near the operating condition.

The principal stability criterion is:

dCm/dα < 0

This criterion is necessary for longitudinal static stability under the stated assumptions.

## 4. Aircraft Trim

Longitudinal trim occurs when the net pitching moment about the center of gravity is zero.

Cm = 0

Trim alone does not guarantee stability.

A complete evaluation requires both the trim condition and the pitching moment slope.

## 5. Horizontal Tail Incidence

Different horizontal tail incidence angles have been investigated in XFLR5 to evaluate their influence on aircraft pitching moment and trim.

The analysis will compare:

- Pitching moment curves
- Trim angle of attack
- Pitching moment slope
- Sensitivity to tail incidence

## 6. Center of Gravity and Static Margin

The aircraft center of gravity and neutral point will be evaluated to estimate longitudinal static margin.

Static Margin = (Neutral Point - CG) / MAC

A positive static margin generally indicates longitudinal static stability under the conventional coordinate definition.

The acceptable CG range will be established through analysis and testing.

## 7. Limitations

The preliminary simulation results depend on aerodynamic assumptions, reference geometry, aircraft mass properties, and center-of-gravity position.

Numerical predictions will require further verification through additional simulations and physical flight testing.

## 8. Future Work

- [x] Establish conventional tail configuration
- [x] Perform initial tail incidence studies
- [ ] Export pitching moment polar data
- [ ] Compare trim and stability across tail settings
- [ ] Determine center of gravity limits
- [ ] Estimate static margin
- [ ] Evaluate elevator control authority
- [ ] Conduct ground checks and flight tests
- [ ] Compare simulation results with experiments
