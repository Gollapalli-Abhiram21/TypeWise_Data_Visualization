import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os

def run_linechart_analysis():
    print("\n" + "="*80)
    print("LINE CHARTS")
    print("="*80)

# Define dynamic paths using pathlib
    SCRIPT_DIR = Path(__file__).parent
    PROJECT_ROOT = SCRIPT_DIR.parent.parent     # Go up two levels to project root
    DATA_DIR = PROJECT_ROOT / 'data_sets'
    OUTPUT_DIR = PROJECT_ROOT / 'outputs' / 'ploted_types_pngs'
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load data and plot (example: using Cars93.csv)
    csv_path = DATA_DIR / "Cars93.csv"
    dates = pd.date_range("2024-01-01", periods=100)
    values = np.random.normal(0, 1, 100).cumsum()

    plt.plot(dates, values, color="green")
    plt.title("Example Time Series Line Chart")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "line_charts.png", dpi=300)
    plt.show()
    plt.close()

    print(f"✓ Saved bar chart at {OUTPUT_DIR / 'line_charts.png'}\n")
