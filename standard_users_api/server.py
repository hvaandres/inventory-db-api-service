from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from fastapi.exceptions import HTTPException
from datetime import datetime
from db import CRUD

app = FastAPI(
    title="DGM Inventory API",
    description="API for UVU for the department of DGM, and the app is about an inventory system for the department. This is in general to manage standard users.",
    docs_url="/",
)

class standardUserCreateModel(BaseModel):
    first_name: str
    last_name: str
    uvu_id: str
    email_address: str
    degree_program: str
    uvu_status: str

class standardUserUpdateModel(BaseModel):
    first_name: str
    last_name: str
    uvu_id: str
    email_address: str
    degree_program: str
    uvu_status: str

crud = CRUD()

@app.get("/standard-user")
async def get_all_standard_users():
    try:
        result = crud.list_standard_users()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/standard-user/{standard_user_id}")
async def get_standard_user(standard_user_id: str):
    try:
        result = crud.retrieve_standard_user(standard_user_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@app.post("/standard-users", status_code=201)
async def create_standard_user(standard_user: standardUserCreateModel):
    try:
        result = crud.create_standard_user(data={
            'first_name': standard_user.first_name,
            'last_name': standard_user.last_name,
            'uvu_id': standard_user.uvu_id,
            'email_address': standard_user.email_address,
            'degree_program': standard_user.degree_program,
            'uvu_status': standard_user.uvu_status,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.patch("/standard-users/{standard_user_id}")
async def update_standard_user(standard_user_id: str, standard_user: standardUserUpdateModel):
    try:
        data = {k: v for k, v in standard_user.dict().items() if v is not None}
        result = crud.update_standard_user(standard_user_id, data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/standard-users/{standard_user_id}", status_code=204)
async def delete_standard_user(standard_user_id: str):
    try:
        crud.delete_standard_user(standard_user_id)
        return {"message": "standard user deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
