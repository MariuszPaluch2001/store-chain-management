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

schema1 = json.load(open("schemas/producent_schema.json"))
schema2 = json.load(open("schemas/product_schema.json"))
production.create_collection("producent")
production.create_collection("product")
production.command("collMod", "producent", validator = schema1)
production.command("collMod", "product", validator = schema2)

def push_sample_data():
    producent = [
        {
            "Name" : "test",
            "NIP" : "123456789",
            "Address": {
                "Voivodeship" : "Świętokrzyskie",
                "City" : "Sandomierz",
                "Street" : "Kobierniki",
                "Building_Bumber" : "138"
            }
        }
    ]
    pr_id = production.producent.insert_many(producent)
    print(pr_id.inserted_ids)
    product = [
        {
            "Name" : "TEST",
            "Mass" : 100,
            "Mass_Unit" : "kg",
            "Description" : "DUPA",
            "Producent_ID" : pr_id.inserted_ids[0]
        }
    ]
    production.product.insert_many(product)

push_sample_data()