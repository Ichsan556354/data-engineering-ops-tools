from confluent_kafka import Producer, Consumer, KafkaException, KafkaError
import json

from common.kafka import load_kafka_config


class Kafka:
    def __init__(self):
        config = load_kafka_config()
        self.producer = Producer({
            'bootstrap.servers': config.KAFKA_BOOTSTRAP_SERVERS
        })
        self.consumer = Consumer({
            'bootstrap.servers': config.KAFKA_BOOTSTRAP_SERVERS,
            'group.id': config.KAFKA_GROUP_ID,
            'auto.offset.reset': config.KAFKA_AUTO_OFFSET_RESET
        })
        self.topic = config.KAFKA_TOPIC

    def produce_message(self, message):
        self.producer.produce(self.topic, value=message)
        self.producer.flush()

    def read_json(self):
        with open ('data/data.json', 'r') as file:
            data_json = json.load(file)
        return data_json

    def produce(self):
        data_json = self.read_json()
        for player in data_json['players']:
            player = json.dumps(player)
            self.produce_message(player)

    def consume(self):
        self.consumer.subscribe([self.topic])
        try:
            while True:
                msg = self.consumer.poll(timeout=1.0)

                try:
                    if msg is None:
                        continue
                    if msg.error():
                        if msg.error().code() == KafkaError._PARTITION_EOF:
                            print(f"End of partition reached {msg.partition()}")
                        elif msg.error():
                            raise KafkaException(msg.error())
                    else:
                        print(f"Received message: {msg.value().decode('utf-8')}")
                    print(msg)
                except KeyboardInterrupt:
                    print(msg)
        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()
