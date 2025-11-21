import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Define dynamic paths

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent     # Go up two levels
DATA_DIR = PROJECT_ROOT / 'data_sets'
OUTPUT_DIR = PROJECT_ROOT / 'outputs' / 'data_types_pngs'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def analyze_temporal_data():
    print("=" * 80)
    print("TEMPORAL DATA ANALYSIS")
    print("=" * 80)
    print("\nDATASET: Cars93.csv")
    print("TYPE: Temporal/Quantitative Data")
    print("DESCRIPTION: Car specifications data that can show patterns over time/categories")
    print("-" * 80)

    print("\nLoading dataset...")
    cars_df = pd.read_csv(DATA_DIR / 'Cars93.csv')

    print("\nDataset Structure:")
    print(f"Shape: {cars_df.shape[0]} rows × {cars_df.shape[1]} columns")
    print(f"\nColumn Names:\n{list(cars_df.columns)}")

    print("\nFirst 5 Records:")
    print(cars_df.head())

    print("\nData Types:")
    print(cars_df.dtypes)

    print("\nMissing Values:")
    missing = cars_df.isnull().sum()
    print(missing[missing > 0])
    if missing.sum() == 0:
        print("No missing values found!")

    print("\nColumn Classification:")
    numerical_cols = cars_df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = cars_df.select_dtypes(include=['object']).columns.tolist()
    print(f"Numerical Columns ({len(numerical_cols)}): {numerical_cols}")
    print(f"Categorical Columns ({len(categorical_cols)}): {categorical_cols}")

    print("\nDescriptive Statistics (Numerical Data):")
    print(cars_df.describe())

    print("\nCategorical Data Analysis:")
    print(f"\nCar Types Distribution:")
    print(cars_df['Type'].value_counts())
    print(f"\nOrigin Distribution:")
    print(cars_df['Origin'].value_counts())

    print("\nCreating Visualizations...")

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Temporal/Quantitative Data Analysis - Cars93', fontsize=16, fontweight='bold')

    axes[0, 0].hist(cars_df['Price'], bins=20, color='steelblue', edgecolor='black')
    axes[0, 0].set_xlabel('Price ($1000)')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].set_title('Price Distribution (Continuous Data)')
    axes[0, 0].grid(True, alpha=0.3)

    type_counts = cars_df['Type'].value_counts()
    axes[0, 1].bar(type_counts.index, type_counts.values, color='coral', edgecolor='black')
    axes[0, 1].set_xlabel('Car Type')
    axes[0, 1].set_ylabel('Count')
    axes[0, 1].set_title('Car Type Distribution (Nominal Data)')
    axes[0, 1].tick_params(axis='x', rotation=45)

    cylinders_numeric = pd.to_numeric(cars_df['Cylinders'], errors='coerce')
    axes[1, 0].scatter(cars_df['Horsepower'], cars_df['Price'],
                       c=cylinders_numeric, cmap='viridis',
                       s=100, alpha=0.6, edgecolors='black')
    axes[1, 0].set_xlabel('Horsepower')
    axes[1, 0].set_ylabel('Price ($1000)')
    axes[1, 0].set_title('Price vs Horsepower (Continuous Data Relationship)')
    axes[1, 0].grid(True, alpha=0.3)
    cbar = plt.colorbar(axes[1, 0].collections[0], ax=axes[1, 0])
    cbar.set_label('Cylinders')

    origin_groups = [cars_df[cars_df['Origin'] == origin]['Price'] for origin in cars_df['Origin'].unique()]
    axes[1, 1].boxplot(origin_groups, labels=cars_df['Origin'].unique(), patch_artist=True)
    axes[1, 1].set_xlabel('Origin')
    axes[1, 1].set_ylabel('Price ($1000)')
    axes[1, 1].set_title('Price Distribution by Origin (Categorical Comparison)')
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'temporal_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Visualization saved as 'temporal_analysis.png' in outputs directory")

    return cars_df


if __name__ == "__main__":
    analyze_temporal_data()
    plt.show()
    plt.close()
