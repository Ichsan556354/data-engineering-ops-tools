from elasticsearch import Elasticsearch, helpers

from common.es import load_es_config


class EsService:
    def __init__(self):
        config = load_es_config()
        self.es = Elasticsearch(
            [
                {
                    'host': config.ELASTICSEARCH_HOST,
                    'port': config.ELASTICSEARCH_PORT,
                    'scheme': config.ELASTICSEARCH_SCHEME
                }
            ],
            http_auth=(config.ELASTICSEARCH_USER, config.ELASTICSEARCH_PASSWORD)
        )

    def check_index(self, index_name, body=None):
        if self.es.indices.exists(index=index_name):
            print(f"Index '{index_name}' exsist")
        else:
            print(f"Index '{index_name}' does not exist.")

    def search(self, index_name, query):
        response = self.es.search(index=index_name, body=query)
        hits = response['hits']['hits']

        return hits
        # field_names = set()
        # for hit in hits:
        #     for field in hit['_source'].keys():
        #         field_names.add(field)

    def ingest(self, index_name, query):
        response = self.es.index(index=index_name, document=query)

        return response['result']

    def insert_many(self, index, documents):
        for doc in documents:
            if doc.get('_id') is None:
                response = self.es.index(index=index, document=doc)

            else:
                doc_id = doc.pop('_id')

                actions = [
                    {
                        "_index": index,
                        "_id": doc_id,
                        "_source": doc
                    }
                ]
            # print(actions)
                response = helpers.bulk(self.es, actions)

        return response
