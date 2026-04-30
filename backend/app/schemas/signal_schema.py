from pydantic import BaseModel
from datetime import datetime

class Signal(BaseModel):
    component_id: str
    message: str
    severity: str
    timestamp: datetime