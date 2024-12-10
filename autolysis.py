import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai
import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Set up OpenAI API key (make sure to set it as an environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY")

# FastAPI setup
app = FastAPI()

# Pydantic model to handle incoming requests
class DataRequest(BaseModel):
    file_path: str

def generate_analysis_report(df):
    """
    Generate an analysis report using OpenAI and return a narrative about the data.
    """
    # Use the first few rows of the dataframe as context for the model
    data_sample = df.head(10).to_dict(orient="records")
    
    # Create the prompt to send to OpenAI
    prompt = f"Please provide a detailed analysis and insights about the following dataset:\n{data_sample}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def generate_visualizations(df):
    """
    Generate basic visualizations such as heatmap and scatter plots.
    """
    # Visualization 1: Correlation Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap")
    heatmap_file = "heatmap.png"
    plt.savefig(heatmap_file)
    plt.close()

    # Visualization 2: Scatter Plot of two columns (e.g., Rating vs Reviews Count)
    if "Rating" in df.columns and "Reviews Count" in df.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x="Rating", y="Reviews Count")
        plt.title("Rating vs Reviews Count")
        scatter_file = "scatter_plot.png"
        plt.savefig(scatter_file)
        plt.close()
    
    return heatmap_file, scatter_file

def clean_data(df):
    """
    Clean the data by handling missing values and performing basic preprocessing.
    """
    df = df.dropna()  # Dropping rows with missing values for simplicity
    return df

@app.post("/analyze")
def analyze_data(request: DataRequest):
    """
    Analyze the data and return a report.
    """
    # Read the dataset
    try:
        df = pd.read_csv(request.file_path)
    except Exception as e:
        return {"error": f"Error reading file: {str(e)}"}
    
    # Clean the data
    df_cleaned = clean_data(df)

    # Generate analysis report
    report = generate_analysis_report(df_cleaned)
    
    # Generate visualizations
    heatmap_file, scatter_file = generate_visualizations(df_cleaned)
    
    return {
        "report": report,
        "heatmap": heatmap_file,
        "scatter_plot": scatter_file,
    }

# To run the server with FastAPI
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
