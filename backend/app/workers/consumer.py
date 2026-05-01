import time
from kafka import KafkaConsumer
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

        print("Processed signal:", signal)

        # ✅ Create incident here
        incident = {
            "id": len(storage.incidents) + 1,
            "component_id": signal["component_id"],
            "status": "OPEN",
            "severity": signal["severity"]
        }

        storage.incidents.append(incident)

