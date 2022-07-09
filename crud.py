from typing import List
from pymongo.database import Database
from bson.objectid import ObjectId

class Crud:
    
    def __init__(self, db : Database) -> None:
        self.db = db

    def insert_one(self, collection_name, document) -> ObjectId:
        collection = self.db.get_collection(collection_name)
        id = collection.insert_one(document).inserted_id
        return id

    def insert_many(self, collection_name, documents) -> List[ObjectId]:
        collection = self.db.get_collection(collection_name)
        id = collection.insert_many(documents).inserted_ids
        return id