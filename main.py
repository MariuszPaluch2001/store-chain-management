import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import json
from datetime import datetime
load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
connect_str = f"""mongodb+srv://mariuszpaluch:{password}@myprojects.z9jwiv9.mongodb.net/?retryWrites=true&w=majority&authSource=admin"""

client= MongoClient(connect_str)
production = client.production
colletions = production.list_collection_names()

schema1 = json.load(open("schemas/producent_schema.json"))
schema2 = json.load(open("schemas/product_schema.json"))
schema3 = json.load(open("schemas/store_schema.json"))
schema4 = json.load(open("schemas/product_delivery.json"))

production.create_collection("producent")
production.create_collection("product")
production.create_collection("store")
production.create_collection("product_delivery")

production.command("collMod", "producent", validator = schema1)
production.command("collMod", "product", validator = schema2)
production.command("collMod", "store", validator = schema3)
production.command("collMod", "product_delivery", validator = schema4)

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
    producent_id = production.producent.insert_many(producent).inserted_ids[0]
    product = [
        {
            "Name" : "TEST",
            "Mass" : 100,
            "Mass_Unit" : "kg",
            "Description" : "DUPA",
            "Producent_ID" : producent_id
        }
    ]
    product_id = production.product.insert_many(product).inserted_ids[0]

    store = [
        {
            "Name" : "TEST",
            "Description" : "TEST",
            "Manager" : {
                "First_Name" : "TESTOWY",
                "Name" : "TEST",
                "Employment_Date" : datetime.now(),
                "Telephone_Number" : "123123123123"
            },
            "Description" : "DUPA",
            "Address": {
                "Voivodeship" : "Świętokrzyskie",
                "City" : "Sandomierz",
                "Street" : "Kobierniki",
                "Building_Bumber" : "138"
            }
        }
    ]
    store_id = production.store.insert_many(store).inserted_ids[0]

    product_delivery = [
        {
            "Amount" : 2,
            "Delivery_Date" : datetime.now(),
            "Expiration_Date" : datetime.now(),
            "Product_id" : product_id,
            "Store_id" : store_id
        }
    ]

    product_delivery_id = production.product_delivery.insert_many(product_delivery).inserted_ids[0]
push_sample_data()