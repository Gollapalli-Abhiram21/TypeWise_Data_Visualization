import numpy as np
import pandas as pd

def run_outlier_analysis():
    print("\n" + "="*80)
    print("OUTLIERS - DETECTION AND HANDLING")
    print("="*80)

    np.random.seed(42)
    normal_data = np.random.normal(loc=50, scale=10, size=100)
    outliers = np.array([5, 95, 100, 3, 98])
    data = np.concatenate([normal_data, outliers])
    df = pd.DataFrame({'values': data})

    print(df.describe())
    print("\nOutlier detection complete.\n")
