from fastapi import APIRouter
from app.schemas.signal_schema import Signal
from app.services import storage
from datetime import datetime

router = APIRouter()

@router.post("/")
async def ingest_signal(signal: Signal):
    # Store raw signal
    storage.signals.append(signal)

    # Create incident (simple for now)
    incident = {
        "id": len(storage.incidents) + 1,
        "component_id": signal.component_id,
        "status": "OPEN",
        "created_at": datetime.utcnow(),
        "severity": signal.severity
    }

    storage.incidents.append(incident)

    return {"message": "Signal received", "incident_id": incident["id"]}