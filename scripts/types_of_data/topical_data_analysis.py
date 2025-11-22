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


def analyze_topical_data():
    print("\n\n" + "=" * 80)
    print("TOPICAL DATA ANALYSIS")
    print("=" * 80)
    print("\nDATASET: IPhoneReview.csv")
    print("TYPE: Topical/Text Data")
    print("DESCRIPTION: Customer reviews and feedback data")
    print("-" * 80)

    print("\nLoading dataset...")
    reviews_df = pd.read_csv(DATA_DIR / 'IPhoneReview.csv', encoding='latin-1')

    print("\nDataset Structure:")
    print(f"Shape: {reviews_df.shape[0]} rows × {reviews_df.shape[1]} columns")
    print(f"Columns: {list(reviews_df.columns)}")

    print("\nSample Reviews:")
    print(reviews_df.head(3))

    print("\nText Data Characteristics:")
    reviews_df['Review_Length'] = reviews_df['Review'].astype(str).apply(len)
    reviews_df['Word_Count'] = reviews_df['Review'].astype(str).apply(lambda x: len(x.split()))
    print(f"Average review length: {reviews_df['Review_Length'].mean():.2f} characters")
    print(f"Average word count: {reviews_df['Word_Count'].mean():.2f} words")

    print("\nReview Date Analysis:")
    reviews_df['Date'] = pd.to_datetime(reviews_df['Date'], format='%d %b %Y', errors='coerce')
    print(f"Date range: {reviews_df['Date'].min()} to {reviews_df['Date'].max()}")

    print("\nUser Activity:")
    top_users = reviews_df['UserName'].value_counts().head(10)
    print(f"Top 10 Most Active Users:\n{top_users}")

    print("\nCreating Topical Data Visualizations...")

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Topical Data Analysis - iPhone Reviews', fontsize=16, fontweight='bold')

    axes[0, 0].hist(reviews_df['Review_Length'], bins=50, color='skyblue', edgecolor='black')
    axes[0, 0].set_xlabel('Review Length (characters)')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].set_title('Review Length Distribution')
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].hist(reviews_df['Word_Count'], bins=30, color='lightgreen', edgecolor='black')
    axes[0, 1].set_xlabel('Word Count')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].set_title('Word Count Distribution')
    axes[0, 1].grid(True, alpha=0.3)

    if reviews_df['Date'].notna().any():
        reviews_by_date = reviews_df.groupby(reviews_df['Date'].dt.to_period('D')).size()
        axes[1, 0].plot(reviews_by_date.index.astype(str), reviews_by_date.values,
                        color='purple', linewidth=2, marker='o')
        axes[1, 0].set_xlabel('Date')
        axes[1, 0].set_ylabel('Number of Reviews')
        axes[1, 0].set_title('Review Activity Over Time')
        axes[1, 0].tick_params(axis='x', rotation=45)
        axes[1, 0].grid(True, alpha=0.3)

    axes[1, 1].barh(top_users.index[:8], top_users.values[:8], color='orange', edgecolor='black')
    axes[1, 1].set_xlabel('Number of Reviews')
    axes[1, 1].set_ylabel('User Name')
    axes[1, 1].set_title('Top 8 Most Active Users')
    axes[1, 1].grid(True, axis='x', alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'topical_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Visualization saved as 'topical_analysis.png' in outputs directory")

    return reviews_df


if __name__ == "__main__":
    analyze_topical_data()
    plt.show()
    plt.close()
