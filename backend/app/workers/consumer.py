import time
from kafka import KafkaConsumer
from app.services.redis_client import r
import json
from app.services import storage

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

        # 🔍 Check if incident exists in last 10 sec
        existing_incident_id = r.get(component)

        if existing_incident_id:
            print("Reusing incident:", existing_incident_id)

            # Attach signal to existing incident
            storage.incident_signals.setdefault(existing_incident_id, []).append(signal)

        else:
            # 🆕 Create new incident
            incident_id = str(len(storage.incidents) + 1)

            incident = {
                "id": incident_id,
                "component_id": component,
                "status": "OPEN",
                "severity": signal["severity"]
            }

            storage.incidents.append(incident)

            # Save mapping
            storage.incident_signals[incident_id] = [signal]

            # ⏳ Set debounce window (10 sec)
            r.setex(component, 10, incident_id)

            print("New incident created:", incident_id)

