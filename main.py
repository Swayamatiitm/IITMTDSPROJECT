import requests
import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

# Define the Pydantic model to handle the incoming request data
class DataRequest(BaseModel):
    file_path: str

app = FastAPI()

# Function to request analysis from the analysis service
def get_data_analysis(file_path: str):
    url = "http://localhost:8000/analyze"
    payload = {"file_path": file_path}
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to analyze the data"}

# Endpoint for triggering data analysis
@app.post("/submit_data/")
def submit_data(request: DataRequest):
    analysis_result = get_data_analysis(request.file_path)
    if "error" in analysis_result:
        return {"error": analysis_result["error"]}
    
    # Returning the report along with the visualizations as files
    report = analysis_result.get("report", "No report generated.")
    heatmap = analysis_result.get("heatmap")
    scatter_plot = analysis_result.get("scatter_plot")
    
    # Return the generated report and files
    return {
        "report": report,
        "heatmap_url": f"/download/{heatmap}",
        "scatter_plot_url": f"/download/{scatter_plot}"
    }

# Endpoint to serve the generated files (e.g., images)
@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join("generated_files", filename)
    return FileResponse(file_path, media_type="image/png")

