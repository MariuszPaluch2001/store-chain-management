from genericpath import isfile
import pytest
from src.crud import Crud
import mongomock
from src.DB_contoller import DB_controller
from copy import deepcopy
def test_load_data_from_json():
    db = mongomock.MongoClient().db
    collection = db.collection

    DB_contr = DB_controller(db)

    DB_contr.load_json_to_database("sample_data/prod_sample_data.json", "collection")
    assert len(list(collection.find({}))) == 10

def test_wrong_json_file_open():
    db = mongomock.MongoClient().db

    DB_contr = DB_controller(db)

    with pytest.raises(FileNotFoundError):
        DB_contr.json_load_data("wrong_file")
    
def test_json_export_file():
    db = mongomock.MongoClient().db
    collection = db.collection
    DB_contr = DB_controller(db)
    test_docs = [
            {
                "Attr1" : 1,
                "Attr2" : 2
            },
            {
                "Attr1" : 1,
                "Attr2" : 4
            },
            {
                "Attr1" : 5,
                "Attr2" : 6
            }
    ]
    DB_contr.crud.insert("collection", deepcopy(test_docs))
    DB_contr.json_export_data("bin/test_export.json","collection", {})

    assert isfile("bin/test_export.json")

    docs = DB_contr.json_load_data("bin/test_export.json")
    assert docs == test_docs

