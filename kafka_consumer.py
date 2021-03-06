from kafka import KafkaConsumer
from time import time

consumer = KafkaConsumer('topic1', group_id='my-group',
 bootstrap_servers=['192.168.1.48:9092'],
  auto_offset_reset='earliest', enable_auto_commit=False)

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
        if not message.topic:
            break

def test_and_stop():
    permanent_consumer = KafkaConsumer('topic1', group_id='my-group',
     bootstrap_servers=['192.168.1.48:9092'], auto_offset_reset='earliest',
      enable_auto_commit=False, iter_timeout=10)
    for message in permanent_consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, message.key,
                                            message.value))
        
        value = message.value
        export(value.decode("utf-8") + "\n")

#test()
test_and_stop()