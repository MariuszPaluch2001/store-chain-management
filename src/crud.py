from typing import List
from pymongo.database import Database
from pymongo.cursor import Cursor
from bson.objectid import ObjectId

class Crud:
    
    def __init__(self, db : Database) -> None:
        self.db = db

    def insert(self, collection_name, documents):
        if isinstance(documents, (list, tuple)):
            self.__insert_many(collection_name, documents)
        elif isinstance(documents, dict):
            self.__insert_one(collection_name, documents)
        else:
            raise TypeError("Unknown type. Type should be list, tuple or dict.")

    def __insert_one(self, collection_name, document) -> ObjectId:
        collection = self.db.get_collection(collection_name)
        id = collection.insert_one(document).inserted_id
        return id

    def __insert_many(self, collection_name, documents) -> List[ObjectId]:
        collection = self.db.get_collection(collection_name)
        id = collection.insert_many(documents).inserted_ids
        return id

    def query(self, collection_name, query) -> Cursor:
        collection = self.db.get_collection(collection_name)
        return collection.find(query)

    def delete(self, collection_name, filter):
        collection = self.db.get_collection(collection_name)
        collection.delete_many(filter)

    def update(self, collection_name, filter, new_values):
        collection = self.db.get_collection(collection_name)
        collection.update_many(filter, new_values)