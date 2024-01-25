from fastapi import APIRouter, Depends, HTTPException
from managers.auth import AuthManager
from schemas.request.user_input_data import UserRole, UserStatus
from managers.master import MasterManager

router = APIRouter(prefix="/master", tags=["master"], responses={401: {"user": "Not authorized"}})

"""
Master API Calls
"""


# Update User Role
@router.put("/update_user_role/{user_id}", description="Allows master to update user role")
async def update_user_role(user_id: int, new_role: UserRole,
                           current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognized")

    elif current_user["user_role"] == UserRole.master:
        result = await MasterManager.update_role(user_id, new_role)
        return result

    else:
        raise HTTPException(status_code=403, detail="Only Master Users can update user roles")


# Update User Status
@router.put("/update_user_status/{user_id}", description="Allows master to update user status")
async def update_user_status(user_id: int, new_status: UserStatus,
                             current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognized")

    elif current_user["user_role"] == UserRole.master:
        result = await MasterManager.update_status(user_id, new_status)
        return result

    else:
        raise HTTPException(status_code=403, detail="Only Master Users can update user roles")
