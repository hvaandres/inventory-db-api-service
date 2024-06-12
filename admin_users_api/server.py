from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List
from fastapi.exceptions import HTTPException
from datetime import datetime
from db import CRUD

app = FastAPI(
    title="Admin User Endpoint - DGM Inventory API",
    description="API for UVU for the department of DGM, and the app is about an inventory system for the department. This is in general to manage admin users.",
    docs_url="/",
)

class AdminUserCreateModel(BaseModel):
    first_name: str
    last_name: str
    uvu_id: str
    title_name: str
    department_name: str
    manager_name: str

class AdminUserUpdateModel(BaseModel):
    first_name: str
    last_name: str
    uvu_id: str
    title_name: str
    department_name: str
    manager_name: str

crud = CRUD()

@app.get("/admin-user")
async def get_all_admin_users():
    try:
        result = crud.list_admin_users()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/admin-user/{admin_user_id}")
async def get_admin_user(admin_user_id: str):
    try:
        result = crud.retrieve_admin_user(admin_user_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@app.post("/admin-users", status_code=201)
async def create_admin_user(admin_user: AdminUserCreateModel):
    try:
        result = crud.create_admin_user(data={
            'first_name': admin_user.first_name,
            'last_name': admin_user.last_name,
            'uvu_id': admin_user.uvu_id,
            'title_name': admin_user.title_name,
            'department_name': admin_user.department_name,
            'manager_name': admin_user.manager_name,
        })
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.patch("/admin-users/{admin_user_id}")
async def update_admin_user(admin_user_id: str, admin_user: AdminUserUpdateModel):
    try:
        data = {k: v for k, v in admin_user.dict().items() if v is not None}
        result = crud.update_admin_user(admin_user_id, data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/admin-users/{admin_user_id}", status_code=204)
async def delete_admin_user(admin_user_id: str):
    try:
        crud.delete_admin_user(admin_user_id)
        return {"message": "Admin user deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
