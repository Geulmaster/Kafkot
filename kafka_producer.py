import json
from bson import json_util
from kafka import KafkaProducer
from Kafkot.conf import config_reader

data = {"first": "cook", "second": "eat"}

producer = KafkaProducer(bootstrap_servers=[config_reader()["brokers"]["servers"]], api_version=(0, 10, 1))
producer.send("topic1", key=bytes("lahmi", encoding="utf8"), value=json.dumps(data, default=json_util.default).encode('utf-8'))
producer.flush()