from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'wing_polar_6ms.csv'
OUT = ROOT / 'Figures'
OUT.mkdir(exist_ok=True)
# XFLR5 exports include six metadata/blank lines before the header.
df = pd.read_csv(DATA, skiprows=6, skipinitialspace=True)
df.columns = df.columns.str.strip()
df['L_D'] = df['CL'] / df['CD']

series = [
    ('cl_vs_alpha', 'alpha', 'CL', 'Angle of attack (degrees)', 'Lift coefficient, CL', 'Lift curve'),
    ('drag_polar', 'CD', 'CL', 'Drag coefficient, CD', 'Lift coefficient, CL', 'Drag polar'),
    ('ld_vs_alpha', 'alpha', 'L_D', 'Angle of attack (degrees)', 'Lift-to-drag ratio, CL/CD', 'Aerodynamic efficiency'),
    ('cm_vs_alpha', 'alpha', 'Cm', 'Angle of attack (degrees)', 'Pitching moment coefficient, Cm', 'Pitching moment'),
    ('drag_components_vs_alpha', 'alpha', None, 'Angle of attack (degrees)', 'Drag coefficient', 'Drag components'),
]
for name,x,y,xlab,ylab,title in series:
    fig, ax = plt.subplots(figsize=(8.4,5.3), layout='constrained')
    if y is None:
        for key in ('CDi','CDv','CD'):
            ax.plot(df[x], df[key], linewidth=1.8, marker='o', markersize=3, label=key)
        ax.legend()
    else:
        ax.plot(df[x], df[y], linewidth=2, marker='o', markersize=3)
    ax.set(xlabel=xlab, ylabel=ylab, title=f'{title} | Initial Plane, VLM1, V = 6 m/s')
    ax.grid(True, alpha=0.25)
    fig.savefig(OUT/f'{name}.png',dpi=200)
    fig.savefig(OUT/f'{name}.pdf')
    plt.close(fig)
print('Points:',len(df))
peak = df.loc[df['L_D'].idxmax()]
print('Max L/D:',round(peak.L_D,3),'at alpha:',peak.alpha)
