from fastapi import APIRouter, Depends, HTTPException
from managers.auth import AuthManager
from schemas.request.user_input_data import UserRole
from schemas.request.case_input_data import CaseCreateRequest
from managers.cases import CasesManager

router = APIRouter(prefix="/cases", tags=["cases"], responses={401: {"user": "Not authorized"}})


# Get all cases not agent
@router.get("/show_all_cases/", description="Allows master and Admin to get all cases")
async def get_all_cases(current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognize")
    elif current_user["user_role"] in [UserRole.master, UserRole.admin]:
        cases = await CasesManager.get_all_cases()
        return cases
    else:
        raise HTTPException(status_code=403, detail="Not authorized to view cases")


# Create a case
@router.post("/create_case/", description="Allows master users to create a new case")
async def create_case(case_data: CaseCreateRequest, current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognize")
    elif current_user["user_role"] in [UserRole.master, UserRole.agent, UserRole.admin]:
        result = await CasesManager.create_case(case_data, current_user)
        return result
    else:
        raise HTTPException(status_code=403, detail="Only Tech Support Users can create new cases")


@router.get("/show_agent_cases/", description="Allows agents to get their cases")
async def get_agent_cases(current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognize")
    else:
        cases = await CasesManager.get_agent_case(current_user)
        return cases

