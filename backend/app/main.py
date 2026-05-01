from fastapi import FastAPI
from app.api import ingestion, incidents, health
import threading
from app.workers.consumer import start_consumer

app = FastAPI(title="IMS Backend")

app.include_router(ingestion.router, prefix="/signals")
app.include_router(incidents.router, prefix="/incidents")
app.include_router(health.router, prefix="/health")

@app.on_event("startup")
def start_worker():
    t = threading.Thread(target=start_consumer)
    t.daemon = True
    t.start()
