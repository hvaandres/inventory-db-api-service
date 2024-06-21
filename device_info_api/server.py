import sys
import os
import pydantic
import requests
from datetime import datetime
from typing import Optional
from fastapi import FastAPI, File, UploadFile, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, validator
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage
from db import CRUD

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Assuming 'client', 'db_id', 'collection_device_id', and 'bucket_id' are defined in 'main' module
from main import client, db_id, collection_device_id, bucket_id

db = Databases(client)
storage = Storage(client)
crud = CRUD()

app = FastAPI(
    title="Device Management Endpoint - DGM Inventory API",
    description="API for UVU for the department of DGM, and the app is about an inventory system for the department. This is in general to manage devices.",
    docs_url="/",
)

class DevicesCreateModel(BaseModel):
    device_name: str
    device_sku: str
    uvu_sku: str
    device_mac_address: str = Field(..., min_length=12, max_length=17)  # Validate MAC address format
    funding_source: str
    device_cost: float
    device_category: str
    serial_number: str
    inventory_status: str
    device_image_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class DevicesUpdateModel(BaseModel):
    device_name: Optional[str] = None
    device_sku: Optional[str] = None
    uvu_sku: Optional[str] = None
    device_mac_address: Optional[str] = None
    funding_source: Optional[str] = None
    device_cost: Optional[float] = None
    device_category: Optional[str] = None
    serial_number: Optional[str] = None
    inventory_status: Optional[str] = None
    device_image_id: Optional[str] = None

class Config:
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }


@app.get("/devices")
async def list_devices():
    """Get all devices."""
    try:
        return await crud.list_devices()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/devices/{device_id}")
async def get_device(device_id: str):
    """Get a specific device by ID."""
    try:
        return await crud.retrieve_device(device_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/devices", status_code=status.HTTP_201_CREATED)
async def create_device(device: DevicesCreateModel, file: UploadFile = File(None)):
    try:
        # Pydantic will automatically validate the data
        device_dict = device.dict()

        # ... (rest of your code)

    except Exception as e:
        if isinstance(e, pydantic.ValidationError):
            # Extract specific error messages for each field
            error_messages = [f"{field}: {str(err)}" for field, err in e.errors()]
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                                detail="Invalid device data: " + ", ".join(error_messages))
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))




@app.patch("/devices/{device_id}")
async def update_device(device_id: str, device: DevicesUpdateModel, file: UploadFile = File(None)):
    """Update an existing device."""
    try:
        data = {k: v for k, v in device.dict().items() if v is not None}

        file_id = None
        if file:
            file_id = await storage.create_file(
                bucket=bucket_id,
                data=file.file,
                file_name=file.filename,
                content_type=file.content_type,
                encryption=False
            )
            data['device_image_id'] = file_id

        result = await crud.update_device(device_id, data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/devices/{device_id}", status_code=204)
async def delete_device(device_id: str):
    """Delete a device by ID."""
    try:
        await crud.delete_device(device_id, delete_image=True)
        return {"message": "Device deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
