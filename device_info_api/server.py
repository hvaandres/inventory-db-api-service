import secrets
import sys
import os

# Add the parent directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from fastapi import FastAPI, File, UploadFile, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List
import os
import sys
import json
# Assuming 'client', 'db_id', 'collection_device_id', and 'bucket_id' are defined in 'main' module
from main import client, db_id, collection_device_id, bucket_id
# Initialize Appwrite services
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage
from json import JSONEncoder
from db import CRUD

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Initialize Appwrite services
db = Databases(client)
storage = Storage(client)
crud = CRUD()

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(self, obj)


# Initialize FastAPI app
app = FastAPI(
    title="Device Management Endpoint - DGM Inventory API",
    description="API for UVU for the department of DGM, managing devices inventory.",
    docs_url="/",
)


# Use custom JSON encoder in FastAPI app
app.json_encoder = JSONEncoder

# Define your Pydantic models
class DevicesCreateModel(BaseModel):
    device_name: str
    device_sku: str
    uvu_sku: str
    device_mac_address: str = Field(..., min_length=12, max_length=17)
    funding_source: str
    device_cost: str  # Ensure device_cost is defined as a string
    device_category: str
    serial_number: str
    inventory_status: str
    device_image_id: Optional[str] = None

class DevicesUpdateModel(BaseModel):
    device_name: Optional[str] = None
    device_sku: Optional[str] = None
    uvu_sku: Optional[str] = None
    device_mac_address: Optional[str] = None
    funding_source: Optional[str] = None
    device_cost: Optional[str] = None  # Ensure device_cost is defined as a string
    device_category: Optional[str] = None
    serial_number: Optional[str] = None
    inventory_status: Optional[str] = None
    device_image_id: Optional[str] = None

# Exception handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": str(exc)},
    )

# GET endpoint to retrieve all devices
@app.get("/devices", response_model=List[dict])
async def get_all_devices():
    """Get all devices."""
    try:
        devices = crud.list_devices()
        return devices  # Return the list of devices

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# GET endpoint to retrieve a specific device by ID
@app.get("/devices/{device_id}", response_model=dict)
async def get_device(device_id: str):
    """Get a specific device by ID."""
    try:
        device = crud.retrieve_device(device_id)
        return device  # Return the specific device

    except HTTPException as http_exc:
        raise http_exc

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# POST endpoint to create a device
@app.post("/devices", status_code=status.HTTP_201_CREATED)
async def create_device(device: DevicesCreateModel):
    try:
        result = crud.create_device(data={
            'device_name': device.device_name,
            'device_sku': device.device_sku,
            'uvu_sku': device.uvu_sku,
            'device_mac_address': device.device_mac_address,
            'funding_source': device.funding_source,
            'device_cost': device.device_cost,
            'device_category': device.device_category,
            'serial_number': device.serial_number,
            'inventory_status': device.inventory_status,
            'device_image_id': device.device_image_id
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# PATCH endpoint to update a device
@app.patch("/devices/{device_id}")
async def update_device(device_id: str, device: DevicesUpdateModel):
    """Update an existing device."""
    try:
        # Exclude created_at from the update data
        update_data = device.dict(exclude={"created_at"}, exclude_unset=True)
        
        # Update device in database
        result = crud.update_device(device_id, update_data)
        return result

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# DELETE endpoint to delete a device
@app.delete("/devices/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_device(device_id: str):
    """Delete a device by ID."""
    try:
        crud.delete_device(device_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))