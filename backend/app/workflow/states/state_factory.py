from app.workflow.states.open import OpenState
from app.workflow.states.investigating import InvestigatingState
from app.workflow.states.resolved import ResolvedState
from app.workflow.states.closed import ClosedState

def get_state(status):
    return {
        "OPEN": OpenState(),
        "INVESTIGATING": InvestigatingState(),
        "RESOLVED": ResolvedState(),
        "CLOSED": ClosedState()
    }[status]
