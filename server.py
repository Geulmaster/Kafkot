from flask import Response, Flask, request
import time
from kafka import KafkaConsumer
from conf import config_reader
import json
from bson import json_util
from kafka import KafkaProducer

application = Flask(__name__)

config = config_reader()


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


@application.route('/new/')
def kafkaStream():
    """
    Get request - new messages
    """
    consumer = KafkaConsumer(config["details"]["topic"], bootstrap_servers = [config["brokers"]["servers"]], enable_auto_commit=False)
    def events():
        for message in consumer:
            yield message.value.decode("utf-8") + '\n'
    return Response(events())


@application.route('/all/')
def all_msgs():
    """
    Get request - old commited messages
    """
    consumer = KafkaConsumer(config["details"]["topic"],
     bootstrap_servers = [config["brokers"]["servers"]],
      auto_offset_reset='smallest', enable_auto_commit=True,
       auto_commit_interval_ms = 30* 1000)
    def events():
        for message in consumer:
            yield message.value.decode("utf-8") + '\n'
    return Response(events())


@application.route("/tail", methods=['GET'])
def tail():
    """
    Receives ID and returns it:
    http://127.0.0.1:5000/tail?num=6 returns last 6 messages
    """
    number = request.args.get('num', None)
    consumer = KafkaConsumer(config["details"]["topic"],
     bootstrap_servers = [config["brokers"]["servers"]])
    msgs = []
    def events():
        while len(msgs) != number:
            for message in consumer:
                msgs.append(message.value.decode("utf-8"))
        return msgs
    return Response(events())


@application.route("/insert", methods=['POST'])
def insert():
    #data = {"first": "cook", "second": "eat"}
    msg = request.get_json()
    producer = KafkaProducer(bootstrap_servers=[config["brokers"]["servers"]],
     api_version=(0, 10, 1))
    producer.send(config["details"]["topic"], key=bytes("lahmi", encoding="utf8"),
     value=json.dumps(msg, default=json_util.default).encode('utf-8'))
    producer.flush()
    return f"{msg} was sent successfully to broker"


if __name__ == '__main__':
    application.run(host='0.0.0.0',debug = True)