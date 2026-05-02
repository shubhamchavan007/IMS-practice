import time
from kafka import KafkaConsumer
from app.services.redis_client import r
import json
from app.services import storage
from app.services.mongo_client import signals_collection
from app.services.db import SessionLocal
from app.models.incident import Incident
from datetime import datetime

def start_consumer():
    while True:
        try:
            consumer = KafkaConsumer(
                "signals",
                bootstrap_servers="kafka:9092",
                value_deserializer=lambda m: json.loads(m.decode("utf-8")),
                auto_offset_reset="earliest",
                group_id="ims-group"
            )
            break
        except Exception as e:
            print("Kafka not ready, retrying...")
            time.sleep(5)

    print("Consumer started...")

    for msg in consumer:
        signal = msg.value

        component = signal["component_id"]

        
         # ✅ Store raw signal in MongoDB
        signals_collection.insert_one(signal)

        # 🔍 Debounce check
        existing_incident_id = r.get(component)

        db=SessionLocal()

        if existing_incident_id:
            print("Reusing incident:", existing_incident_id)

            

        else:
            # 🆕 Create new incident
            incident = Incident(

            
                component_id=component,
                status="OPEN",
                severity= signal["severity"],
                start_time=datetime.utcnow()
                
            )

            

            # Save mapping
            db.add(incident)
            db.commit()
            db.refresh(incident)

            # ⏳ Set debounce window (10 sec)
            r.setex(component, 10, incident.id)

            print("New incident created:", incident.id)
        db.close()

