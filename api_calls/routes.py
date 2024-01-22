from fastapi import APIRouter
from api_calls import auth, master, cases

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(master.router)
api_router.include_router(cases.router)