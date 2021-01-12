from flask import Response, Flask
import time
from kafka import KafkaConsumer

application = Flask(__name__)

@application.route('/')
def index():
    return "Hello, World!"

@application.route('/realtime/')
def realtime():
    def createGenerator():
        for i in range(1,10):
            yield str(i) + '\n'
            time.sleep(0.2)
    return Response(createGenerator())

@application.route('/kafka/')
def kafkaStream():
    """
    Get request - new messages
    """
    consumer = KafkaConsumer('hello', group_id='my-group',
     bootstrap_servers=['192.168.1.48:9092'], enable_auto_commit=False)
    def events():
        for message in consumer:
            yield message.value.decode("utf-8") + '\n'
    return Response(events())

@application.route('/all/')
def all_msgs():
    """
    Get request - old commited messages
    """
    consumer = KafkaConsumer('hello', group_id='my-group',
     bootstrap_servers=['192.168.1.48:9092'],
      auto_offset_reset='smallest', enable_auto_commit=True,
       auto_commit_interval_ms = 30* 1000)
    def events():
        for message in consumer:
            yield message.value.decode("utf-8") + '\n'
    return Response(events())

if __name__ == '__main__':
    application.run(debug = True)