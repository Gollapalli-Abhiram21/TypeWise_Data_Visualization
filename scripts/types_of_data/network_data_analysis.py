import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx 
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


def analyze_network_data():
    print("\n\n" + "=" * 80)
    print("NETWORK DATA ANALYSIS")
    print("=" * 80)
    print("\nDATASET: StackNetworkNodes.csv & StackNetworkLinks.csv")
    print("TYPE: Network Data (Nodes and Edges)")
    print("DESCRIPTION: Technology tags and their relationships")
    print("-" * 80)

    print("\nLoading datasets...")
   
    nodes_df = pd.read_csv(DATA_DIR / 'StackNetworkNodes.csv')
    links_df = pd.read_csv(DATA_DIR / 'StackNetworkLinks.csv')

    print("\nDataset Structure:")
    print(f"Nodes: {nodes_df.shape[0]} nodes")
    print(f"Links: {links_df.shape[0]} connections")

    print("\nSample Nodes:")
    print(nodes_df.head())
    print("\nSample Links:")
    print(links_df.head())

    print("\nNetwork Statistics:")
    print(f"Number of groups: {nodes_df['group'].nunique()}")
    print(f"Node size range: {nodes_df['nodesize'].min():.2f} - {nodes_df['nodesize'].max():.2f}")
    print(f"Link strength range: {links_df['value'].min():.2f} - {links_df['value'].max():.2f}")

    print("\nNode Connectivity Analysis:")
    source_counts = links_df['source'].value_counts()
    target_counts = links_df['target'].value_counts()
    all_nodes = pd.concat([source_counts, target_counts], axis=1, keys=['as_source', 'as_target']).fillna(0)
    all_nodes['total_connections'] = all_nodes['as_source'] + all_nodes['as_target']
    print("\nTop 10 Most Connected Nodes:")
    print(all_nodes.nlargest(10, 'total_connections'))

    print("\nTechnology Group Distribution:")
    print(nodes_df.groupby('group').agg({
        'nodesize': ['count', 'mean', 'sum']
    }))

    print("\nCreating Network Visualizations...")

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Network Data Analysis - Stack Overflow Tags', fontsize=16, fontweight='bold')

    axes[0, 0].hist(nodes_df['nodesize'], bins=20, color='teal', edgecolor='black')
    axes[0, 0].set_xlabel('Node Size')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].set_title('Node Size Distribution')
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].hist(links_df['value'], bins=30, color='salmon', edgecolor='black')
    axes[0, 1].set_xlabel('Link Strength')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].set_title('Link Strength Distribution')
    axes[0, 1].grid(True, alpha=0.3)

    top_nodes = nodes_df.nlargest(15, 'nodesize')
    axes[1, 0].barh(top_nodes['name'], top_nodes['nodesize'], color='gold', edgecolor='black')
    axes[1, 0].set_xlabel('Node Size')
    axes[1, 0].set_ylabel('Technology Tag')
    axes[1, 0].set_title('Top 15 Technology Tags by Size')
    axes[1, 0].grid(True, axis='x', alpha=0.3)

    group_counts = nodes_df['group'].value_counts().sort_index()
    axes[1, 1].bar(group_counts.index.astype(str), group_counts.values,
                   color='mediumpurple', edgecolor='black')
    axes[1, 1].set_xlabel('Group ID')
    axes[1, 1].set_ylabel('Number of Nodes')
    axes[1, 1].set_title('Technology Groups Distribution')
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / 'network_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Visualization saved as 'network_analysis.png' in outputs directory")

    try:
        import networkx as nx
        print("\nCreating Network Graph...")

        G = nx.Graph()

        for _, node in nodes_df.head(30).iterrows():
            G.add_node(node['name'], size=node['nodesize'], group=node['group'])

        top_links = links_df.nlargest(50, 'value')
        for _, link in top_links.iterrows():
            if link['source'] in G.nodes() and link['target'] in G.nodes():
                G.add_edge(link['source'], link['target'], weight=link['value'])

        plt.figure(figsize=(14, 10))
        pos = nx.spring_layout(G, k=0.5, iterations=50)

        node_sizes = [G.nodes[node].get('size', 1) * 10 for node in G.nodes()]

        nx.draw_networkx_nodes(G, pos, node_size=node_sizes,
                               node_color='lightblue', alpha=0.7, edgecolors='black')
        nx.draw_networkx_edges(G, pos, alpha=0.3, width=1)
        nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

        plt.title('Stack Overflow Technology Network (Top 30 Nodes, Top 50 Connections)',
                  fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / 'network_graph.png', dpi=300, bbox_inches='tight')
        print("✓ Network graph saved as 'network_graph.png' in outputs directory")

    except ImportError:
        print("\n[NOTE] NetworkX not installed. Skipping network graph visualization.")
        print("To install: pip install networkx")

    return nodes_df, links_df


if __name__ == "__main__":
    analyze_network_data()
    plt.show()
    plt.close()
