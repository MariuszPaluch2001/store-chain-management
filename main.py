import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import json
load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
connect_str = f"""mongodb+srv://mariuszpaluch:{password}@myprojects.z9jwiv9.mongodb.net/?retryWrites=true&w=majority&authSource=admin"""

client= MongoClient(connect_str)
production = client.production
colletions = production.list_collection_names()

schema = json.load(open("schemas/producent_schema.json"))
production.create_collection("producent")
production.command("collMod", "producent", validator = schema)