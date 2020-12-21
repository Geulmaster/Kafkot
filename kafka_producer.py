from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['192.168.1.48:9092'], api_version=(0, 10, 1))
producer.send("testo",key=bytes("lalal", encoding="utf8"), value=bytes("koko", encoding='utf8'))
producer.flush()