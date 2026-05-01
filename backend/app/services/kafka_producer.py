import time
from kafka import KafkaProducer
import json

producer = None

while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers="kafka:9092",
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        break
    except:
        print("Kafka not ready for producer...")
        time.sleep(5)

def send_signal(signal):
    producer.send("signals", signal)
    producer.flush()
