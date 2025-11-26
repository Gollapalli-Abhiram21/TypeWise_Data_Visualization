import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import os

def run_scatter_analysis():
    print("\n" + "="*80)
    print("SCATTER PLOTS")
    print("="*80)
    
    # Define dynamic paths using pathlib
    SCRIPT_DIR = Path(__file__).parent
    PROJECT_ROOT = SCRIPT_DIR.parent.parent     # Go up two levels to project root
    DATA_DIR = PROJECT_ROOT / 'data_sets'
    OUTPUT_DIR = PROJECT_ROOT / 'outputs' / 'ploted_types_pngs'
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load data and plot (example: using Cars93.csv)
    csv_path = DATA_DIR / "Cars93.csv"
    data = pd.read_csv("data_sets/Cars93.csv")
    plt.scatter(data["Horsepower"], data["Price"], color="blue", alpha=0.6)
    plt.xlabel("Horsepower")
    plt.ylabel("Price")
    plt.title("Horsepower vs Price")
    plt.savefig(OUTPUT_DIR / "scatter_plot.png", dpi=300)
    plt.show()
    plt.close()

    print(f"✓ Saved bar chart at {OUTPUT_DIR / 'line_charts.png'}\n")
