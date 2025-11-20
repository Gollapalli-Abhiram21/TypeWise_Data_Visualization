import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os

def run_boxplot_analysis():
    print("\n" + "="*80)
    print("BOX PLOTS")
    print("="*80)

    # Define dynamic paths using pathlib
    SCRIPT_DIR = Path(__file__).parent
    PROJECT_ROOT = SCRIPT_DIR.parent.parent     # Go up two levels to project root
    DATA_DIR = PROJECT_ROOT / 'data_sets'
    OUTPUT_DIR = PROJECT_ROOT / 'outputs' / 'ploted_types_pngs'
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load data and plot (example: using Cars93.csv)
    csv_path = DATA_DIR / "Cars93.csv"
    data = np.random.normal(50, 10, 100)
    plt.boxplot(data)
    plt.title("Box Plot Example")
    plt.savefig(OUTPUT_DIR / "box_plot.png", dpi=300)
    plt.show()
    plt.close()

    print(f"✓ Saved bar chart at {OUTPUT_DIR / 'box_plot.png'}\n")

