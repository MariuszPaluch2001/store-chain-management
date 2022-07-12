from src.crud import Crud
from pymongo.database import Database
import json

class DB_controller:

    def __init__(self, db : Database) -> None:
        self.db = db
        self.crud = Crud(db)

    def json_load_data(self, filename, collection_name):
        with open(filename, 'r') as f:
            documets = json.load(f)

        self.crud.insert(collection_name, documets)


    