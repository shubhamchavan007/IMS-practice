from app.workflow.states.base import IncidentState

class OpenState(IncidentState):
    def next(self, incident, data=None):
        incident.status = "INVESTIGATING"
