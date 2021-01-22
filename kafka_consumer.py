from kafka import KafkaConsumer

consumer = KafkaConsumer('testo', group_id='my-group', bootstrap_servers=['192.168.1.48:9092'], auto_offset_reset='earliest', enable_auto_commit=False)

def export(text):
    with open("results.txt", "a+") as results:
        results.write(text)

def test():
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
        
        value = message.value
        export(value.decode("utf-8") + "\n")