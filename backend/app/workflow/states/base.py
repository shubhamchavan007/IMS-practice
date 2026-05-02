class IncidentState:
    def next(self, incident, data=None):
        raise NotImplementedError("Must implement next()")
