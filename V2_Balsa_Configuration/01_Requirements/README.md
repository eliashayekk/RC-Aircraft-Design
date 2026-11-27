# V2 Requirements

The aircraft is a manual recreational RC fixed-wing design for calm weather. It uses a high wing, a tractor propeller, hand launch and belly landing without landing gear. The airframe is primarily balsa, and aggressive aerobatics are outside the mission.

The final radio is a FlySky FS-i6X transmitter and FS-iA6B receiver. An ESP32 and PS4 controller may be used for temporary testing. The stall-speed target is 6 m/s. Launch and cruise conditions will be established from the V2 wing and propulsion analyses.

| Parameter | Value | Basis |
| --- | --- | --- |
| Design mass | 0.630 kg | Conservative sizing choice |
| Wing planform | Rectangular | Baseline |
| Span | 1.550 m | Baseline |
| Chord and MAC | 0.238 m | Baseline |
| Wing area | 0.3689 m² | Span × chord |
| Aspect ratio | 6.5 nominal (6.513 from baseline dimensions) | Span² / area |
| Taper ratio | 1 | Rectangular planform |
| Sweep, twist and dihedral | 0° each | Baseline |
| Wing leading and trailing edge | x = 220 mm and 458 mm | Firewall datum |
| Mass loading | 17.1 g/dm² | 630 g / 36.89 dm² |

Light wing loading reduces the lift coefficient required at a given speed, which helps with low-speed flight, hand launch and landing. The lighter aircraft can be more sensitive to gusts. Keep the geometry as the baseline for comparing the airfoils. Changing span or chord changes wing loading, Reynolds number or induced drag and would require a fresh comparison.
