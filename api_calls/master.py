from fastapi import APIRouter, Depends, HTTPException
from managers.auth import AuthManager
from models.enums import UserRole
from models.schemas.request.vertical_input_data import VerticalCreateRequest
from managers.master import MasterManager

router = APIRouter(prefix="/master", tags=["master"], responses={401: {"user": "Not authorized"}})

"""
Vertical API Calls
"""


@router.get("/show_all_verticals/", description="Allows master to get all verticals")
async def get_all_verticals(current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognize")
    elif current_user["user_role"] == UserRole.master:
        verticals = await MasterManager.get_verticals()
        return verticals
    else:
        raise HTTPException(status_code=403, detail="Not authorized to view verticals")


@router.post("/create_vertical/", description="Allows master users to create a new vertical")
async def create_vertical(vertical_data: VerticalCreateRequest,
                          current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognize")
    elif current_user["user_role"] == UserRole.master:
        result = await MasterManager.create_vertical(vertical_data.vertical_name)
        return result
    else:
        raise HTTPException(status_code=403, detail="Only master users can create verticals")


@router.put("/update_vertical/{vertical_id}", description="Allows master users to update an existing vertical")
async def update_vertical(vertical_data: VerticalCreateRequest, vertical_id: int,
                          current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognize")
    elif current_user["user_role"] == UserRole.master:
        result = await MasterManager.update_vertical(vertical_id, vertical_data.vertical_name)
        return result
    else:
        raise HTTPException(status_code=403, detail="Only master users can update verticals")


@router.delete("/delete_vertical/{vertical_id}", description="Allows master users to delete a vertical")
async def delete_vertical(vertical_id: int, current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognize")
    elif current_user["user_role"] == UserRole.master:
        result = await MasterManager.delete_vertical(vertical_id)
        return result
    else:
        raise HTTPException(status_code=403, detail="Only master users can delete verticals")
