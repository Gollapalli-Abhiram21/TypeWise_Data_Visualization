import numpy as np

def run_quartile_analysis():
    print("\n" + "="*80)
    print("SECTION 2: QUARTILES AND FIVE-NUMBER SUMMARY")
    print("="*80)

    data = np.random.normal(50, 10, 100)
    Q1, Q2, Q3 = np.percentile(data, [25, 50, 75])
    IQR = Q3 - Q1

    print(f"Q1={Q1:.2f}, Q2={Q2:.2f}, Q3={Q3:.2f}, IQR={IQR:.2f}\n")
