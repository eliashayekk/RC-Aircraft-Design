# Repository Layout

## Versioning rule

- `V1_Preliminary` is a frozen archive of the original preliminary configuration.
- [`V2_Balsa_Configuration`](V2_Balsa_Configuration/README.md) is the active balsa-based design. Its requirements, mass and CG, aerodynamics, stability and control, propulsion, structures, CAD, and manufacturing records live together at the repository root. The earlier discipline-level V2 entry points link to this folder.
- Shared reference data belongs in `00_Shared_Resources`.
- Study scripts stay beside their datasets when their paths, outputs, or constants are version-coupled.
- New results must not overwrite V1 files.

## Recommended structure

```text
RC-Aircraft-Design/
├── 00_Shared_Resources/
│   ├── README.md
│   └── Airfoils/
│       ├── Wing_Candidates/
│       └── Tail_Candidates/
│
├── 01_Requirements/
│   ├── Design_Iterations.md
│   ├── V1_Preliminary/
│   │   ├── README.md
│   │   └── Project_Overview.md
│   └── V2_Balsa_Configuration/
│       └── README.md
│
├── 02_Aerodynamics/
│   ├── README.md
│   ├── V1_Preliminary/
│   │   ├── README.md
│   │   ├── 01_Airfoil_Selection/
│   │   │   ├── README.md
│   │   │   ├── Airfoil_Trade_Study.md
│   │   │   ├── analyze_polars.py
│   │   │   ├── airfoil_analysis.xlsx
│   │   │   ├── airfoil_summary.csv
│   │   │   └── data/
│   │   ├── 02_Wing_Aspect_Ratio/
│   │   │   └── Wing_AR_Trade_Study.md
│   │   ├── 03_XFLR5_Wing/
│   │   │   ├── wing.xfl
│   │   │   └── CR001SM_AR6.5_Wing.xml
│   │   └── 04_Performance_Analysis/
│   │       ├── README.md
│   │       └── MATLAB/
│   │           ├── aircraft_analysis.m
│   │           ├── aircraft_parameters.m
│   │           └── T1-6_0 m_s-VLM1.csv
│   └── V2_Balsa_Configuration/
│       └── README.md
│
├── 03_Stability_Control/
│   ├── README.md
│   ├── V1_Preliminary/
│   │   ├── README.md
│   │   ├── 01_Tail_Airfoil_Study/
│   │   │   ├── README.md
│   │   │   ├── analyze_tail_polars.py
│   │   │   ├── Tail_Airfoil_Analysis.xlsx
│   │   │   ├── tail_airfoil_summary.csv
│   │   │   ├── raw_polars/
│   │   │   └── figures/
│   │   ├── 02_Horizontal_Tail_Sizing/
│   │   │   └── Horizontal_Tail_Sizing.md
│   │   ├── 03_Longitudinal_Stability/
│   │   │   ├── Longitudinal_Stability.md
│   │   │   ├── CG_Study/
│   │   │   ├── Trim_Study/
│   │   │   └── figures/
│   │   ├── 04_Control_Surface_Sizing/
│   │   │   ├── Elevator/exported_results/
│   │   │   └── Rudder/exported_results/
│   │   ├── 05_Lateral_Directional_Stability/
│   │   └── 06_XFLR5_Models/
│   └── V2_Balsa_Configuration/
│       └── README.md
│
├── 04_Propulsion/
├── 05_Structures/
├── 06_CAD/
├── 07_Manufacturing/
├── 08_Testing/
├── 09_Reports/
└── V2_Balsa_Configuration/
    ├── 01_Requirements/
    ├── 02_Mass_CG/
    ├── 03_Aerodynamics/
    │   ├── Airfoil_Trade_Study/
    │   └── Wing_3D/
    ├── 04_Stability_Control/
    ├── 05_Propulsion/
    ├── 06_Structures/
    ├── 07_CAD/
    ├── 08_Manufacturing/
    └── README.md
```

## File-handling decisions

- Airfoil coordinate files are shared because they are reference geometry, not version-specific results.
- `analyze_polars.py` remains with the V1 wing-airfoil study because its current input and output paths are tied to that study.
- `analyze_tail_polars.py` remains with the V1 tail-airfoil study because it reads and writes beside its local dataset.
- The MATLAB files remain in V1 because they contain the original mass, geometry, trim constants, and V1 data-file name.
- Raw polars, XFLR5 models, exported results, and workbooks remain in the version that produced them.
- `desktop.ini` is excluded because it is Windows metadata, not project content.
