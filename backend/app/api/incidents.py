from fastapi import APIRouter
from app.services import storage

router = APIRouter()

@router.get("/")
async def get_incidents():
    return storage.incidents
