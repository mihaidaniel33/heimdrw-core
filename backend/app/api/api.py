from fastapi import APIRouter
from app.api.endpoints import upload, saft

api_router = APIRouter()
api_router.include_router(upload.router, tags=["upload"])
api_router.include_router(saft.router, prefix="/saft", tags=["saft"]) 