import json
from bson import json_util
from kafka import KafkaProducer

data = {"first": "cook", "second": "eat"}

producer = KafkaProducer(bootstrap_servers=['192.168.1.48:9092'], api_version=(0, 10, 1))
producer.send("testo", key=bytes("lahmi", encoding="utf8"), value=json.dumps(data, default=json_util.default).encode('utf-8'))
producer.flush()