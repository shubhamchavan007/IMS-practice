from fastapi import APIRouter, Body
from typing import Optional, Dict
from app.workflow.states.state_factory import get_state
from app.services.db import SessionLocal
from app.models.incident import Incident

router = APIRouter()


@router.post("/{incident_id}/next")
def next_state(incident_id: int, data: Optional[dict] = Body(Default=None)):
    db = SessionLocal()

    incident = db.query(Incident).filter(Incident.id == incident_id).first()

    if not incident:
        db.close()
        return {"error": "Incident not found"}

    state = get_state(incident.status)

    if not state:
        db.close()
        return {"error": "Invalid state"}

    try:
        state.next(incident, data)
        db.commit()
        db.refresh(incident)

        response = {
            "id": incident.id,
            "status": incident.status
        }

        db.close()
        return response

    except Exception as e:
        db.close()
        return {"error": str(e)}
