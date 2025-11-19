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





def analyze_geospatial_data():
    print("\n\n" + "=" * 80)
    print("GEOSPATIAL DATA ANALYSIS")
    print("=" * 80)
    print("\nDATASET: volcano_data_2010.csv")
    print("TYPE: Geospatial Data")
    print("DESCRIPTION: Volcano eruptions with latitude/longitude coordinates")
    print("-" * 80)

    print("\nLoading dataset...")
    volcano_df = pd.read_csv(DATA_DIR / 'volcano_data_2010.csv')

    print("\nDataset Structure:")
    print(f"Shape: {volcano_df.shape[0]} rows × {volcano_df.shape[1]} columns")

    print("\nFirst 5 Records:")
    print(volcano_df.head())

    print("\nGeospatial Attributes:")
    print("Key columns: Latitude, Longitude, Country, Name, Elevation")
    print(f"\nCountries with volcanic activity:")
    print(volcano_df['Country'].value_counts())

    print("\nData Quality Check:")
    print(f"Records with valid coordinates: {volcano_df[['Latitude', 'Longitude']].notna().all(axis=1).sum()}")

    print("\nGeospatial Statistics:")
    print(volcano_df[['Latitude', 'Longitude', 'Elevation']].describe())

    print("\nCreating Geospatial Visualizations...")

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle('Geospatial Data Analysis - Volcano Locations 2010', fontsize=16, fontweight='bold')

    scatter = axes[0].scatter(volcano_df['Longitude'], volcano_df['Latitude'],
                              c=volcano_df['Elevation'], cmap='Reds',
                              s=200, alpha=0.6, edgecolors='black', linewidth=1.5)
    axes[0].set_xlabel('Longitude', fontsize=12)
    axes[0].set_ylabel('Latitude', fontsize=12)
    axes[0].set_title('Volcano Locations on World Map (2010)', fontsize=14)
    axes[0].grid(True, alpha=0.3)
    axes[0].axhline(y=0, color='k', linestyle='--', alpha=0.3)
    axes[0].axvline(x=0, color='k', linestyle='--', alpha=0.3)
    cbar = plt.colorbar(scatter, ax=axes[0])
    cbar.set_label('Elevation (m)', fontsize=11)

    country_counts = volcano_df['Country'].value_counts().head(10)
    axes[1].barh(country_counts.index, country_counts.values, color='orangered', edgecolor='black')
    axes[1].set_xlabel('Number of Volcanic Events', fontsize=12)
    axes[1].set_ylabel('Country', fontsize=12)
    axes[1].set_title('Top 10 Countries by Volcanic Activity', fontsize=14)
    axes[1].grid(True, axis='x', alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'geospatial_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Visualization saved as 'geospatial_analysis.png' in outputs directory")

    return volcano_df


if __name__ == "__main__":
    analyze_geospatial_data()
    plt.show()
    plt.close()
