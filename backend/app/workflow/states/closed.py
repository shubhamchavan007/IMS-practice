from app.workflow.states.base import IncidentState

class ClosedState(IncidentState):
    def next(self, incident, data=None):
        raise Exception("Incident is already CLOSED")
