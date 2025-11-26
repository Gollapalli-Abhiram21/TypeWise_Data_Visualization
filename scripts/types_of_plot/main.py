"""
MAIN SCRIPT: Data Analysis and Visualization Project
----------------------------------------------------
Executes each analysis section sequentially.
"""

from outliers import run_outlier_analysis
from quartiles import run_quartile_analysis
from boxplots import run_boxplot_analysis
from scatterplots import run_scatter_analysis
from linecharts import run_linechart_analysis
from barcharts import run_barchart_analysis
from summary import run_summary

if __name__ == "__main__":
    print("="*80)
    print("DATA ANALYSIS AND VISUALIZATION - EXECUTION START")
    print("="*80)

    run_outlier_analysis()
    run_quartile_analysis()
    run_boxplot_analysis()
    run_scatter_analysis()
    run_linechart_analysis()
    run_barchart_analysis()
    run_summary()

    print("\n" + "="*80)
    print("🎉 Execution completed successfully! All visualizations saved in:")
    print("outputs\\ploted_types_pngs")
    print("="*80)
