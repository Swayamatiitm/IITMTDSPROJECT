from fastapi import FastAPI
from pydantic import BaseModel
import shutil
import os

app = FastAPI()

# Pydantic model for file upload request
class FileUploadRequest(BaseModel):
    file_path: str

# Function to handle file uploads
def upload_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        return "File does not exist"
    
    destination_folder = "uploaded_files"
    os.makedirs(destination_folder, exist_ok=True)
    destination_path = os.path.join(destination_folder, os.path.basename(file_path))
    
    try:
        shutil.copy(file_path, destination_path)
        return f"File uploaded successfully to {destination_path}"
    except Exception as e:
        return f"Error occurred during file upload: {str(e)}"

@app.post("/upload")
def upload(request: FileUploadRequest):
    file_path = request.file_path
    upload_result = upload_file(file_path)
    return {"message": upload_result}
