import os
from dotenv import load_dotenv

class KafkaConfig:
    def __init__(self, bootstrap_servers, topic, group_id, auto_offset_reset):
        self.KAFKA_BOOTSTRAP_SERVERS = bootstrap_servers
        self.KAFKA_TOPIC = topic
        self.KAFKA_GROUP_ID = group_id
        self.KAFKA_AUTO_OFFSET_RESET = auto_offset_reset

def load_kafka_config():
    load_dotenv()

    KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
    KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
    KAFKA_GROUP_ID = os.getenv('KAFKA_GROUP_ID')
    KAFKA_AUTO_OFFSET_RESET = os.getenv('KAFKA_AUTO_OFFSET_RESET')

    return KafkaConfig(
        KAFKA_BOOTSTRAP_SERVERS,
        KAFKA_TOPIC,
        KAFKA_GROUP_ID,
        KAFKA_AUTO_OFFSET_RESET
    )