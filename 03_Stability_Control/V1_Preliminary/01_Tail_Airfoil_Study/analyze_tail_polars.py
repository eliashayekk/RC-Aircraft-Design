from pathlib import Path
import re

import numpy as np
import pandas as pd


# ============================================================
# PATHS
# ============================================================

SCRIPT_FOLDER = Path(__file__).resolve().parent

DATA_FOLDER = SCRIPT_FOLDER / "raw_polars"

OUTPUT_CSV = SCRIPT_FOLDER / "tail_airfoil_summary.csv"
OUTPUT_EXCEL = SCRIPT_FOLDER / "Tail_Airfoil_Analysis.xlsx"


# ============================================================
# SETTINGS
# ============================================================

# Range used to estimate the linear lift-curve slope dCL/dalpha
LINEAR_ALPHA_MIN = -4.0
LINEAR_ALPHA_MAX = 4.0

# Tail lift coefficients where drag will be evaluated
TARGET_CL_VALUES = [-0.4, -0.2, 0.0, 0.2, 0.4]


# ============================================================
# FILE INFORMATION
# ============================================================

def extract_airfoil_name(filename: str) -> str:
    """
    Attempts to extract a readable airfoil name from the filename.

    Examples:
        NACA0010_Re060k.txt -> NACA0010
        NACA0012_Re120k.txt -> NACA0012
    """

    stem = Path(filename).stem

    match = re.search(r"(NACA[\-_ ]?\d+)", stem, re.IGNORECASE)

    if match:
        return match.group(1).upper().replace("_", "").replace("-", "").replace(" ", "")

    # Fallback: everything before Reynolds-number notation
    stem = re.split(r"[_\-]?Re", stem, flags=re.IGNORECASE)[0]

    return stem.strip()


def extract_reynolds_number(filename: str):
    """
    Extract Reynolds number from names such as:

        Re060k
        Re60k
        Re90000
        Re0.060
    """

    stem = Path(filename).stem

    # Example: Re060k
    match = re.search(r"Re[_\- ]?(\d+(?:\.\d+)?)k", stem, re.IGNORECASE)

    if match:
        return float(match.group(1)) * 1000


    # Example: Re90000
    match = re.search(r"Re[_\- ]?(\d{4,})", stem, re.IGNORECASE)

    if match:
        return float(match.group(1))


    # Example: Re0.060 means 0.060 million
    match = re.search(r"Re[_\- ]?(0\.\d+)", stem, re.IGNORECASE)

    if match:
        return float(match.group(1)) * 1_000_000


    return np.nan


# ============================================================
# XFLR5 POLAR READER
# ============================================================

def read_xflr5_polar(filepath: Path):
    """
    Reads an exported XFLR5 / XFOIL polar text file.

    Looks for the table containing columns such as:

        alpha
        CL
        CD
        CDp
        Cm
        Top_Xtr
        Bot_Xtr
    """

    lines = filepath.read_text(
        encoding="utf-8",
        errors="ignore"
    ).splitlines()

    header_index = None

    for i, line in enumerate(lines):

        lower = line.lower()

        if (
            "alpha" in lower
            and "cl" in lower
            and "cd" in lower
        ):
            header_index = i
            break

    if header_index is None:
        raise ValueError("Could not find XFLR5 polar table header.")


    header = lines[header_index].split()

    data_rows = []

    for line in lines[header_index + 1:]:

        stripped = line.strip()

        if not stripped:
            continue

        # Ignore separator lines
        if set(stripped) <= {"-", " "}:
            continue

        parts = stripped.split()

        if len(parts) < len(header):
            continue

        try:
            values = [float(x) for x in parts[:len(header)]]
        except ValueError:
            continue

        data_rows.append(values)


    if not data_rows:
        raise ValueError("No numerical polar data found.")


    df = pd.DataFrame(
        data_rows,
        columns=header
    )

    # Standardize useful column names
    rename_map = {}

    for col in df.columns:

        low = col.lower()

        if low == "alpha":
            rename_map[col] = "alpha"

        elif low == "cl":
            rename_map[col] = "CL"

        elif low == "cd":
            rename_map[col] = "CD"

        elif low == "cm":
            rename_map[col] = "Cm"

    df = df.rename(columns=rename_map)


    required = ["alpha", "CL", "CD"]

    for col in required:

        if col not in df.columns:
            raise ValueError(
                f"Required column '{col}' not found."
            )

    return df


# ============================================================
# ENGINEERING METRICS
# ============================================================

def nearest_value_at_cl(df, target_cl):
    """
    Returns CD and alpha at the point whose CL is closest
    to the requested target CL.
    """

    idx = (df["CL"] - target_cl).abs().idxmin()

    return {
        "CD": df.loc[idx, "CD"],
        "alpha": df.loc[idx, "alpha"],
        "actual_CL": df.loc[idx, "CL"]
    }


def calculate_lift_curve_slope(df):
    """
    Calculates dCL/dalpha using a linear regression
    between LINEAR_ALPHA_MIN and LINEAR_ALPHA_MAX.

    Units:
        CL per degree
    """

    linear = df[
        (df["alpha"] >= LINEAR_ALPHA_MIN)
        &
        (df["alpha"] <= LINEAR_ALPHA_MAX)
    ].copy()


    if len(linear) < 3:
        return np.nan


    slope, intercept = np.polyfit(
        linear["alpha"],
        linear["CL"],
        1
    )

    return slope


def calculate_zero_lift_angle(df):
    """
    Estimates zero-lift angle using the linear lift-curve fit.
    """

    linear = df[
        (df["alpha"] >= LINEAR_ALPHA_MIN)
        &
        (df["alpha"] <= LINEAR_ALPHA_MAX)
    ].copy()


    if len(linear) < 3:
        return np.nan


    slope, intercept = np.polyfit(
        linear["alpha"],
        linear["CL"],
        1
    )


    if abs(slope) < 1e-9:
        return np.nan


    return -intercept / slope


def analyze_polar(df):
    """
    Calculates tail-specific aerodynamic metrics.
    """

    results = {}


    # --------------------------------------------------------
    # Maximum positive lift
    # --------------------------------------------------------

    idx_cl_max = df["CL"].idxmax()

    results["CL_max"] = df.loc[idx_cl_max, "CL"]
    results["alpha_CL_max_deg"] = df.loc[idx_cl_max, "alpha"]


    # --------------------------------------------------------
    # Maximum negative lift
    # --------------------------------------------------------

    idx_cl_min = df["CL"].idxmin()

    results["CL_min"] = df.loc[idx_cl_min, "CL"]
    results["alpha_CL_min_deg"] = df.loc[idx_cl_min, "alpha"]


    # --------------------------------------------------------
    # Positive / negative lift symmetry
    # --------------------------------------------------------

    positive_limit = abs(results["CL_max"])
    negative_limit = abs(results["CL_min"])

    average_limit = (positive_limit + negative_limit) / 2


    if average_limit > 0:

        results["lift_symmetry_error_percent"] = (
            abs(positive_limit - negative_limit)
            / average_limit
            * 100
        )

    else:
        results["lift_symmetry_error_percent"] = np.nan


    # --------------------------------------------------------
    # L/D
    # --------------------------------------------------------

    valid_drag = df["CD"] > 0

    df_ld = df.loc[valid_drag].copy()

    df_ld["L_over_D"] = df_ld["CL"] / df_ld["CD"]


    idx_ld_max = df_ld["L_over_D"].idxmax()

    results["LD_max_positive"] = df_ld.loc[
        idx_ld_max,
        "L_over_D"
    ]

    results["alpha_LD_max_deg"] = df_ld.loc[
        idx_ld_max,
        "alpha"
    ]


    # --------------------------------------------------------
    # Absolute L/D
    #
    # Useful for a symmetric tail because the tail may
    # produce either positive or negative lift.
    # --------------------------------------------------------

    df_ld["abs_L_over_D"] = (
        df_ld["CL"].abs()
        / df_ld["CD"]
    )

    idx_abs_ld = df_ld["abs_L_over_D"].idxmax()

    results["abs_LD_max"] = df_ld.loc[
        idx_abs_ld,
        "abs_L_over_D"
    ]

    results["alpha_abs_LD_max_deg"] = df_ld.loc[
        idx_abs_ld,
        "alpha"
    ]


    # --------------------------------------------------------
    # Lift-curve slope
    # --------------------------------------------------------

    results["dCL_dalpha_per_deg"] = calculate_lift_curve_slope(df)


    # --------------------------------------------------------
    # Zero-lift angle
    # --------------------------------------------------------

    results["alpha_zero_lift_deg"] = calculate_zero_lift_angle(df)


    # --------------------------------------------------------
    # Pitching moment
    # --------------------------------------------------------

    if "Cm" in df.columns:

        results["Cm_mean"] = df["Cm"].mean()

        idx_cl_zero = df["CL"].abs().idxmin()

        results["Cm_near_CL0"] = df.loc[
            idx_cl_zero,
            "Cm"
        ]

    else:

        results["Cm_mean"] = np.nan
        results["Cm_near_CL0"] = np.nan


    # --------------------------------------------------------
    # Drag at important tail lift coefficients
    # --------------------------------------------------------

    for target_cl in TARGET_CL_VALUES:

        point = nearest_value_at_cl(
            df,
            target_cl
        )

        label = (
            f"{target_cl:+.1f}"
            .replace("+", "p")
            .replace("-", "m")
            .replace(".", "_")
        )

        results[f"CD_at_CL_{label}"] = point["CD"]

        results[f"actual_CL_for_{label}"] = point[
            "actual_CL"
        ]


    return results


# ============================================================
# MAIN PROCESSING
# ============================================================

def main():

    print()
    print("=" * 70)
    print("HORIZONTAL TAIL AIRFOIL POLAR ANALYSIS")
    print("=" * 70)
    print()


    if not DATA_FOLDER.exists():

        print(
            f"ERROR: raw_polars folder does not exist:\n"
            f"{DATA_FOLDER}"
        )

        return


    files = sorted(
        DATA_FOLDER.glob("*.txt")
    )


    if not files:

        print(
            f"No .txt polar files found in:\n"
            f"{DATA_FOLDER}"
        )

        return


    print(
        f"Found {len(files)} polar files."
    )

    print()


    summary_rows = []

    raw_data = {}


    for filepath in files:

        print(
            f"Processing: {filepath.name}"
        )


        try:

            df = read_xflr5_polar(filepath)

            airfoil = extract_airfoil_name(
                filepath.name
            )

            reynolds = extract_reynolds_number(
                filepath.name
            )

            metrics = analyze_polar(df)


            row = {
                "Airfoil": airfoil,
                "Reynolds": reynolds,
                "File": filepath.name,
                **metrics
            }


            summary_rows.append(row)


            sheet_name = (
                f"{airfoil}_"
                f"{int(reynolds / 1000):03d}k"
                if not np.isnan(reynolds)
                else airfoil
            )

            sheet_name = sheet_name[:31]

            raw_data[sheet_name] = df


        except Exception as error:

            print(
                f"  ERROR: {error}"
            )


    if not summary_rows:

        print(
            "No valid polar files were processed."
        )

        return


    # ========================================================
    # SUMMARY DATAFRAME
    # ========================================================

    summary = pd.DataFrame(
        summary_rows
    )


    summary = summary.sort_values(
        by=["Airfoil", "Reynolds"]
    ).reset_index(
        drop=True
    )


    # ========================================================
    # EXPORT CSV
    # ========================================================

    summary.to_csv(
        OUTPUT_CSV,
        index=False
    )


    # ========================================================
    # EXPORT EXCEL
    # ========================================================

    with pd.ExcelWriter(
        OUTPUT_EXCEL,
        engine="openpyxl"
    ) as writer:


        summary.to_excel(
            writer,
            sheet_name="Tailfoil Summary",
            index=False
        )


        for sheet_name, df in raw_data.items():

            df.to_excel(
                writer,
                sheet_name=sheet_name,
                index=False
            )


    # ========================================================
    # FORMAT EXCEL
    # ========================================================

    from openpyxl import load_workbook
    from openpyxl.styles import Font, Alignment
    from openpyxl.utils import get_column_letter


    workbook = load_workbook(
        OUTPUT_EXCEL
    )


    for worksheet in workbook.worksheets:

        # Header formatting
        for cell in worksheet[1]:

            cell.font = Font(
                bold=True
            )

            cell.alignment = Alignment(
                horizontal="center"
            )


        worksheet.freeze_panes = "A2"


        # Automatically size columns
        for column_cells in worksheet.columns:

            max_length = 0

            column_number = column_cells[0].column

            for cell in column_cells:

                try:

                    length = len(
                        str(cell.value)
                    )

                    if length > max_length:
                        max_length = length

                except Exception:
                    pass


            adjusted_width = min(
                max_length + 2,
                25
            )

            worksheet.column_dimensions[
                get_column_letter(
                    column_number
                )
            ].width = adjusted_width


    workbook.save(
        OUTPUT_EXCEL
    )


    # ========================================================
    # TERMINAL SUMMARY
    # ========================================================

    print()
    print("=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)

    print()
    print(
        f"CSV saved to:\n{OUTPUT_CSV}"
    )

    print()
    print(
        f"Excel saved to:\n{OUTPUT_EXCEL}"
    )

    print()


    display_columns = [
        "Airfoil",
        "Reynolds",
        "CL_max",
        "CL_min",
        "dCL_dalpha_per_deg",
        "Cm_near_CL0",
        "lift_symmetry_error_percent"
    ]


    existing_columns = [
        col
        for col in display_columns
        if col in summary.columns
    ]


    print(
        summary[
            existing_columns
        ].to_string(
            index=False
        )
    )


if __name__ == "__main__":
    main()