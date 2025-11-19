import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path  # Use pathlib for dynamic paths

def run_barchart_analysis():
    print("\n" + "="*80)
    print("BAR CHARTS")
    print("="*80)

    # Define dynamic paths using pathlib
    SCRIPT_DIR = Path(__file__).parent
    PROJECT_ROOT = SCRIPT_DIR.parent.parent     # Go up two levels to project root
    DATA_DIR = PROJECT_ROOT / 'data_sets'
    OUTPUT_DIR = PROJECT_ROOT / 'outputs' / 'ploted_types_pngs'
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load data and plot (example: using Cars93.csv)
    csv_path = DATA_DIR / "Cars93.csv"
    df = pd.read_csv(csv_path)
    counts = df["Type"].value_counts()

    # Save bar chart using dynamic OUTPUT_DIR
    plt.figure(figsize=(8, 5))
    counts.plot(kind="bar", color="skyblue")
    plt.title("Car Count by Type")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "bar_chart.png", dpi=300)
    plt.show()
    plt.close()

    print(f"✓ Saved bar chart at {OUTPUT_DIR / 'bar_chart.png'}\n")
