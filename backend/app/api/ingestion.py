from fastapi import APIRouter
from app.services.kafka_producer import send_signal
from app.schemas.signal_schema import Signal
router = APIRouter()

@router.post("/")
async def ingest(signal: Signal):
    send_signal(signal.model_dump(mode="json"))
    return {"message": "queued in kafka"}
