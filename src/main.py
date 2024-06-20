from helpers import read_data

from service.kafka import Kafka
from service.postgresql import PostgresService
from service.es import EsService
from service.mongo import MongoService

import jmespath
import json

def main():
    postgresql = PostgresService()
    postgresql.read_column()

if __name__ == '__main__':
    main()
