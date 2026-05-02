from app.workflow.states.base import IncidentState
from datetime import datetime
class ResolvedState(IncidentState):
    def next(self, incident, data=None):
        if not data or "rca" not in data or not data["rca"]:
            raise Exception("RCA required before closing incident")

        # ✅ Save RCA
        incident.rca = data["rca"]

        # ✅ Set end time
        incident.end_time = datetime.utcnow()

        # ✅ Calculate MTTR (seconds)
        if incident.start_time:
            incident.mttr = int(
                (incident.end_time - incident.start_time).total_seconds()
            )

        incident.status = "CLOSED"
