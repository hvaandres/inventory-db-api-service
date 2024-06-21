from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from appwrite.client import Client
from appwrite.services.databases import Databases
from dotenv import load_dotenv
from db import CRUD
import os
import uvicorn

app = FastAPI(
    title="Standard file Endpostr - DGM Inventory API",
    description="API for UVU for the department of DGM, and the app is about an inventory system for the department. This is in general to manage standard files.",
    docs_url="/",
)

class standardFileCreateModel(BaseModel):
    file_name: str
    file_url: str
    file_size: str
    file_description: str
    device_name: str
    device_department: str
    user_upload: str
    upload_date: str

class standardFileUpdateModel(BaseModel):
    file_name: str
    file_url: str
    file_size: str
    file_description: str
    device_name: str
    device_department: str
    user_upload: str
    upload_date: str

crud = CRUD()

@app.get("/standard-file")
async def get_all_standard_files():
    try:
        result = crud.list_standard_files()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/standard-file/{standard_file_id}")
async def retrieve_standard_file(standard_file_id: str):
    try:
        result = crud.retrieve_standard_file(standard_file_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@app.post("/standard-files", status_code=201)
async def create_standard_file(standard_file: standardFileCreateModel):
    try:
        result = crud.create_standard_file(data={
            'file_name': standard_file.file_name,
            'file_url': standard_file.file_url,
            'file_size': standard_file.file_size,
            'file_description': standard_file.file_description,
            'device_name': standard_file.device_name,
            'device_department': standard_file.device_department,
            'user_upload': standard_file.user_upload,
            'upload_date': standard_file.upload_date,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.patch("/standard-files/{standard_file_id}")
async def update_standard_file(standard_file_id: str, standard_file: standardFileUpdateModel):
    try:
        data = {k: v for k, v in standard_file.dict().items() if v is not None}
        result = crud.update_standard_file(standard_file_id, data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/standard-files/{standard_file_id}", status_code=204)
async def delete_standard_file(standard_file_id: str):
    try:
        crud.delete_standard_file(standard_file_id)
        return {"message": "standard file deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
