from pymongo import MongoClient, errors
from common.mongo import load_mongo_config
import json

class MongoService:
    def __init__(self):
        config = load_mongo_config()
        try:
            uri = f"mongodb://{config.MONGO_USER}:{config.MONGO_PASS}@{config.MONGO_HOST}:{config.MONGO_PORT}/{config.MONGO_DB}"
            self.client = MongoClient(uri)
            self.db = MongoClient(uri)[config.MONGO_DB]
        except Exception as e:
            print(f"Error saat menghubungkan ke database: {e}")
            self.db = None

    def read_collection(self, collection):
        if self.db is not None:
            try:
                collection = self.db[collection]
                result = collection.find()
                return list(result)
            except Exception as e:
                print(f"Error saat membaca koleksi {collection}: {e}")
                return []
        else:
            print("Koneksi ke database tidak tersedia")
            return []

    def find_by_id(self, collection, id):
        if self.db is not None:
            try:
                result = self.db[collection].find_one({"_id": id})
                return result
            except Exception as e:
                print(f"Error saat mencari dokumen di koleksi {collection}: {e}")
                return None
        else:
            print("Koneksi ke database tidak tersedia")
            return None

    def insert_many(self, collection, documents):
        if self.db is not None:
            try:
                collection = self.db[collection]
                # if documents.get('_id') is None:
                result = collection.insert_many(documents)
                print(f"Inserted {len(result.inserted_ids)} documents")
            except Exception as e:
                print(f"Error saat memasukkan dokumen ke koleksi {collection}: {e}")
        else:
            print("Koneksi ke database tidak tersedia")

    def search_query(self, collection, query):
        if self.db is not None:
            try:
                collection = self.db[collection]
                result = collection.find(query)
                return list(result)
            except Exception as e:
                print(f"Error saat membaca koleksi {collection}: {e}")
                return []
        else:
            print("Koneksi ke database tidak tersedia")
            return []
    
    def insert_one(self, collection, documents):
        if self.db is not None:
            try:
                collection = self.db[collection]
                result = collection.insert_one(documents)
                response = f"data entered successfully with id : {documents['_id']}"
                print(response)
                return response
            except Exception as e:
                text = f"Error saat memasukkan dokumen ke koleksi {collection}: {e}" 
                print(text)
                return text
        else:
            print("Koneksi ke database tidak tersedia")


    def update_one(self, collection, id, documents):
        if self.db is not None:
            try:
                collection = self.db[collection]
                result = collection.update_one({'_id': id}, {'$set': documents})
                if result.matched_count > 0:
                    return f"Data updated successfully with id: {id}"
                else:
                    return "No document found with the provided id."
            except Exception as e:
                print(e)

    def delete_one(self, collection, id):
        if self.db is not None:
            try:
                collection = self.db[collection]
                result = collection.delete_one({'_id': id})
                return f"Data deleted successfully with id : {id}"
            except Exception as e:
                return f"Failed : {e}"

    def close_connection(self):
        if self.db is not None:
            self.client.close()
