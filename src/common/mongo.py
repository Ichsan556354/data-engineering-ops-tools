import os
from dotenv import load_dotenv

class PostgreConfig:
    def __init__(self, database, user, password, host, port):
        self.MONGO_DB = database
        self.MONGO_USER = user
        self.MONGO_PASS = password
        self.MONGO_HOST = host
        self.MONGO_PORT = port


def load_mongo_config():
    load_dotenv()  # Load environment variables from a .env file if it exists

    MONGO_DB = os.getenv('MONGO_DB')
    MONGO_USER = os.getenv('MONGO_USER')
    MONGO_PASS = os.getenv('MONGO_PASS')
    MONGO_HOST = os.getenv('MONGO_HOST')
    MONGO_PORT = os.getenv('MONGO_PORT')

    return PostgreConfig(
        MONGO_DB, 
        MONGO_USER, 
        MONGO_PASS, 
        MONGO_HOST, 
        MONGO_PORT
    )
