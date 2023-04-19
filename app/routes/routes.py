from fastapi import APIRouter
from app.services.uf_service import home

router = APIRouter()

@router.get("/")
async def read_root():
    return await home()
