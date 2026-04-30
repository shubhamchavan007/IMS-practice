from fastapi import FastAPI
from app.api import ingestion, incidents, health

app = FastAPI(title="IMS Backend")

app.include_router(ingestion.router, prefix="/signals", tags=["Signals"])
app.include_router(incidents.router, prefix="/incidents", tags=["Incidents"])
app.include_router(health.router, prefix="/health", tags=["Health"])