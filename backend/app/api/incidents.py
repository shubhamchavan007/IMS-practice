from fastapi import APIRouter
from app.services import storage

router = APIRouter()

@router.get("/")
async def get_incidents():
    return storage.incidents
@router.get("/{incident_id}/signals")
def get_signals(incident_id: str):
    return storage.incident_signals.get(incident_id, [])
