# Automated Data Analysis and Visualization

This project involves automating the process of analyzing a given dataset, visualizing key insights, and narrating a story about the data. The Python script generates detailed summaries, visualizations, and insights based on the provided CSV file, all wrapped in a well-structured Markdown report. 

## Project Overview

The project accepts a CSV file and performs an automated analysis using AI, focusing on general data exploration techniques like summary statistics, correlation analysis, outlier detection, clustering, and visualizations. After analyzing the dataset, the script generates a comprehensive report and supporting charts to narrate the story of the data.

### Key Features:
- **Automated Data Analysis**: Generates summary statistics, handles missing values, performs correlation analysis, and identifies outliers and clusters.
- **Visualization**: Automatically generates 1-3 visualizations based on the analysis (e.g., heatmaps, bar charts, scatter plots).
- **Storytelling**: Uses an LLM to create a Markdown report with a coherent narrative about the data, its analysis, insights, and implications.
- **Flexibility**: Works with any valid CSV file without assumptions about the data structure.

## How to Run

### Prerequisites
- **Python 3.x** installed on your system.
- Required libraries:
    - `pandas`
    - `seaborn`
    - `matplotlib`
    - `openai`
    - `uvicorn`
  
  You can install them using:
  
  ```bash
  pip install pandas seaborn matplotlib openai uvicorn
