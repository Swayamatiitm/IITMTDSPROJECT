import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from sklearn.preprocessing import LabelEncoder

app = FastAPI()

# Pydantic model for input data request
class DataRequest(BaseModel):
    file_path: str

# Function to generate a correlation heatmap
def generate_correlation_heatmap(df: pd.DataFrame) -> str:
    correlation_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt='.2f', linewidths=0.5)
    heatmap_filename = "generated_files/correlation_heatmap.png"
    plt.savefig(heatmap_filename)
    plt.close()
    return heatmap_filename

# Function to generate scatter plot for numerical columns
def generate_scatter_plot(df: pd.DataFrame) -> str:
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numerical_columns) < 2:
        return None
    x_col = numerical_columns[0]
    y_col = numerical_columns[1]
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[x_col], y=df[y_col])
    scatter_plot_filename = "generated_files/scatter_plot.png"
    plt.title(f'Scatter Plot: {x_col} vs {y_col}')
    plt.savefig(scatter_plot_filename)
    plt.close()
    return scatter_plot_filename

# Function to handle basic data analysis
def analyze_data(file_path: str) -> Dict:
    df = pd.read_csv(file_path)
    
    # Perform basic data cleaning
    df = df.dropna()  # Drop rows with missing values
    le = LabelEncoder()
    for column in df.select_dtypes(include=['object']).columns:
        df[column] = le.fit_transform(df[column])  # Encoding categorical variables
    
    # Generate analysis report
    summary_statistics = df.describe().to_dict()
    
    # Generate visualizations
    heatmap_file = generate_correlation_heatmap(df)
    scatter_plot_file = generate_scatter_plot(df)
    
    return {
        "report": summary_statistics,
        "heatmap": os.path.basename(heatmap_file),
        "scatter_plot": os.path.basename(scatter_plot_file)
    }

@app.post("/analyze")
def analyze(request: DataRequest):
    file_path = request.file_path
    if not os.path.exists(file_path):
        return {"error": "File not found"}
    
    analysis_result = analyze_data(file_path)
    
    return analysis_result
