from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import json
import os

def collection_create(db, schema):
    db.create_collection(schema["$jsonSchema"]["title"])
    db.command("collMod", schema["$jsonSchema"]["title"], validator = schema)

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    password = os.environ.get("MONGODB_PWD")
    connect_str = f"""mongodb+srv://mariuszpaluch:{password}@myprojects.z9jwiv9.mongodb.net/?retryWrites=true&w=majority&authSource=admin"""
    client= MongoClient(connect_str)

    production = client.production
    colletions = production.list_collection_names()

    local_dir = os.path.dirname(__file__)
    schemas_path = os.path.join(local_dir, "schemas/")
    (_, _, filenames) = os.walk(schemas_path).__next__()
    
    for schema in filenames:
        f = open(schemas_path+schema)
        json_schema = json.load(f)
        if json_schema["$jsonSchema"]["title"] not in colletions:
            collection_create(production, json_schema)
        f.close()
