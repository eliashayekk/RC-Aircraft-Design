# Stability and Control

| Baseline input | Horizontal tail | Vertical tail |
| --- | --- | --- |
| Airfoil | NACA 0010 | NACA 0010 |
| Area | 0.0805 m² | 0.038 m² |
| Span or height | 567 mm span | 262 mm height |
| Chord | 142 mm | 145 mm |
| Leading-edge station | x ≈ 820 mm | Pending layout confirmation |
| Aspect ratio | 4 | Pending reference convention |
| Control surface | Elevator chord ≈ 43 mm, movable span ≈ 482 mm | Rudder chord ≈ 44 mm |

The previous horizontal-tail incidence of −1.5° is an initial setup value. Start with the [preliminary V2 CG](../02_Mass_CG/CG_Analysis/README.md), then find trim and evaluate the pitching-moment slope, neutral point and static margin. Adjust incidence and reassess elevator and rudder authority. Wing airfoil and trim loads affect the required tail setting. A forward CG generally increases static margin and may increase the elevator authority needed for trim and low-speed control.

The V1 stability archive contains the previous trim and static-margin results. V2 values will come from the revised full-aircraft model.
