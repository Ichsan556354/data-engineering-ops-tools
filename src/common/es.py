import os
from dotenv import load_dotenv

class ESConfig:
    def __init__(self, host, port, user, password, scheme='http'):
        self.ELASTICSEARCH_HOST = host
        self.ELASTICSEARCH_PORT = int(port)
        self.ELASTICSEARCH_USER = user
        self.ELASTICSEARCH_PASSWORD = password
        self.ELASTICSEARCH_SCHEME = scheme

def load_es_config():
    load_dotenv()
    
    ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST')
    ELASTICSEARCH_PORT = os.getenv('ELASTICSEARCH_PORT')
    ELASTICSEARCH_USER = os.getenv('ELASTICSEARCH_USER')
    ELASTICSEARCH_PASSWORD = os.getenv('ELASTICSEARCH_PASSWORD')
    ELASTICSEARCH_SCHEME = os.getenv('ELASTICSEARCH_SCHEME', 'http')


    return ESConfig(
        ELASTICSEARCH_HOST,
        ELASTICSEARCH_PORT,
        ELASTICSEARCH_USER,
        ELASTICSEARCH_PASSWORD,
        ELASTICSEARCH_SCHEME
    )