from src.db.crud import Crud
from pymongo.database import Database
import json

class DB_controller:

    def __init__(self, db : Database) -> None:
        self.db = db
        self.crud = Crud(db)

    def json_load_data(self, filename):
        with open(filename, 'r') as f:
            documets = json.load(f)

        return documets

    def load_json_to_database(self, filename, collection_name):
        self.crud.insert(collection_name, self.json_load_data(filename))

    def json_export_data(self, filename, collection_name, query):
        query = self.crud.get_collection(collection_name).find(query, {'_id': False})
        query = list(query)
        with open(filename, 'w') as f:
            json.dump(query,f, indent=2)

