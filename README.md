## 📊 Overview

This project provides a comprehensive exploration of data visualization in Python, focusing on temporal, geospatial, topical (text), and network data. It demonstrates analysis pipelines, dynamic path management using pathlib, and both static and interactive visualization with open-source Python libraries.

---

## 📁 Project Structure
```
TypeWise_Data_Visualization/
├── .venv/                       # Python virtual environment
├── data_sets/                   # Input datasets
│   ├── Cars93.csv
│   ├── IPhoneReview.csv
│   ├── StackNetworkLinks.csv
│   ├── StackNetworkNodes.csv
│   └── volcano_data_2010.csv
│
├── outputs/                     # All generated plots and visual outputs
│   ├── data_types_pngs/         # Grouped by data type
│   │   ├── geospatial_analysis.png
│   │   ├── network_analysis.png
│   │   ├── network_graph.png
│   │   ├── temporal_analysis.png
│   │   └── topical_analysis.png
│   │
│   └── ploted_types_pngs/       # Grouped by visualization type
│       ├── bar_chart.png
│       ├── box_plot.png
│       ├── line_charts.png
│       └── scatter_plot.png
│
├── scripts/                     # All Python source code
│   ├── types_of_data/
│   │   ├── geospatial_data_analysis.py
│   │   ├── network_data_analysis.py
│   │   ├── temporal_data_analysis.py
│   │   ├── topical_data_analysis.py
│   │   └── detailed_script_stepbystep.py
│   │
│   └── types_of_plot/
│       ├── __pycache__/
│       ├── main.py
│       ├── barcharts.py
│       ├── boxplots.py
│       ├── linecharts.py
│       ├── scatter_plot.py
│       ├── quartiles.py
│       ├── summary.py
│       └── outliers1.py
│
├── README.md                    # Project documentation
└── requirements.txt             # Required Python packages
```
---

## 🎯 Data Types Covered

1. **Temporal Data**

- Data measured across time or categories (e.g., sales by year, car prices)

- Dataset: Cars93.csv

2. **Geospatial Data**

- Physical/geographic location data

- Dataset: volcano_data_2010.csv

3. **Topical (Text) Data**

- Text reviews, feedback, or any topic-based data

- Dataset: IPhoneReview.csv

4. **Network Data**

- Nodes and links: e.g., concept graphs, social, or tag networks

- Datasets: StackNetworkNodes.csv + StackNetworkLinks.csv

---

# 📈 Data Classification

1. **Qualitative (Categorical) Data**
- Binary (Yes/No)
- Nominal (Category)
- Ordinal (Ranked groups)

2. **Quantitative (Numerical) Data**
- Discrete (Countable, e.g., units)
- Continuous (Measurable, e.g., weight, price)

---

## 🛠️ Technologies Used

Python 3.x

pandas, numpy, matplotlib, seaborn (visualization, plotting)

plotly (interactive), wordcloud (word clouds)

networkx (network graphs), scikit-image, scipy

---

## 📦 Installation

1. Clone or download project
cd path/to/TypeWise_Visualization

2. Create and activate venv
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1      # (Windows PowerShell)
 or
source .venv/bin/activate         # (Mac/Linux)
```
3. Install dependencies
```
pip install -r requirements.txt
```
All scripts use dynamic paths—no need to adjust file paths for your environment.

---

## 🚀 Running the Scripts  

- All scripts use cross-platform dynamic paths with pathlib. They work from any directory! Example for bar chart analysis:
```
python scripts/types_of_data/network_data_analysis.py
python scripts/types_of_data/geospatial_data_analysis.py
python scripts/types_of_data/temporal_data_analysis.py
python scripts/types_of_data/topical_data_analysis.py
```
- Output files are saved to: `outputs/data_types_pngs/`

---

## 📊 Visualization Types

- Box Plots (outliers, spread)

- Scatter Plots (correlation)

- Line Charts (trend over time)

- Bar Plots (category comparison)

- Histograms (distribution)

- Network Graphs (relations)

- Word Clouds (text analysis)

Interactive Visualizations (HTML via Plotly; code framework included)

---

## 📖 Understanding the Datasets

1. **Cars93.csv**: 93 car models (specs and attributes)

2. **volcano_data_2010.csv**: World volcano events

3. **IPhoneReview.csv**: User review text and ratings

4. **StackNetworkNodes.csv & StackNetworkLinks.csv**: Concept network for tags/tech

---

## 🔧 Troubleshooting

- **Missing files?** Ensure data_sets/ exists and has the needed CSVs.

- **FileNotFoundError?** All scripts now use dynamic root-based paths—no need to run from project root, but data must be where expected.

- **Output images missing?** Check the outputs/data_types_pngs/ directory.

- **Dependency error?** Run pip install -r requirements.txt.

---

## 📚 Learning Resources

Matplotlib, Pandas, Plotly

Data-to-viz (visual best practices)

---

## 👥 Use Cases

- Students: Learn real data viz with Python

- Data Analysts: Explore data type-specific visualizations

- Developers & Researchers: Reusable code for analysis and reporting

---

## 📜 License

Educational use, free to modify.

---

## Author

**Gollapalli Abhiram**

_Last Updated: November 2025_



