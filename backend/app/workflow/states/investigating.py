from app.workflow.states.base import IncidentState

class InvestigatingState(IncidentState):
    def next(self, incident, data=None):
        incident.status = "RESOLVED"
