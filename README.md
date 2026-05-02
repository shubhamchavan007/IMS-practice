🧾 Project Title

Incident Management System (IMS)

🎯 Objective

A scalable system to ingest high-volume signals, process them asynchronously, and manage incident lifecycle with RCA and MTTR tracking.

🧠 Architecture
FastAPI → Kafka → Consumer → Redis → DBs
⚙️ Tech Stack
Backend: FastAPI
Queue: Apache Kafka
Cache: Redis
NoSQL: MongoDB
RDBMS: PostgreSQL
Containerization: Docker
🚀 Setup Instructions
git clone <repo>
cd ims-project
docker-compose up --build

Open:

http://<EC2-IP>:8000/docs
🔄 Workflow
OPEN → INVESTIGATING → RESOLVED → CLOSED
RCA mandatory before closing
MTTR auto-calculated
⚡ Backpressure Handling
Kafka buffers incoming signals
Consumer processes asynchronously
Redis debounces duplicate signals
🧪 Sample Test

POST /signals:

{
  "component_id": "CACHE_01",
  "message": "failure",
  "severity": "P2",
  "timestamp": "2026-04-30T10:00:00"
}
📊 Features

✔ Async processing
✔ Debouncing (10 sec window)
✔ RCA enforcement
✔ MTTR calculation
✔ Multi-database architecture

🧪 SAMPLE DATA SCRIPT
sample_data/simulate_failure.py
import requests
import time

url = "http://localhost:8000/signals"

payload = {
    "component_id": "DB_01",
    "message": "connection error",
    "severity": "P0",
    "timestamp": "2026-04-30T10:00:00"
}

for _ in range(10):
    requests.post(url, json=payload)
    time.sleep(0.5)
