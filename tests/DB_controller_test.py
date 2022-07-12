import pytest
from src.crud import Crud
import mongomock
from src.DB_contoller import DB_controller

def test_load_data_from_json():
    db = mongomock.MongoClient().db
    collection = db.collection

    DB_contr = DB_controller(db)

    DB_contr.json_load_data("sample_data/prod_sample_data.json", "collection")
    assert len(list(collection.find({}))) == 10

def test_wrong_json_file_open():
    db = mongomock.MongoClient().db

    DB_contr = DB_controller(db)

    with pytest.raises(FileNotFoundError):
        DB_contr.json_load_data("wrong_file", "collection")
    