import os
from dotenv import load_dotenv

class PostgreConfig:
    def __init__(self, database, user, password, host, port):
        self.PG_DB = database
        self.PG_USER = user
        self.PG_PASS = password
        self.PG_HOST = host
        self.PG_PORT = port


def load_postgre_config():
    load_dotenv()  # Load environment variables from a .env file if it exists

    PG_DB = os.getenv('PG_DB')
    PG_USER = os.getenv('PG_USER')
    PG_PASS = os.getenv('PG_PASS')
    PG_HOST = os.getenv('PG_HOST')
    PG_PORT = os.getenv('PG_PORT')

    return PostgreConfig(
        PG_DB, 
        PG_USER, 
        PG_PASS, 
        PG_HOST, 
        PG_PORT
    )
