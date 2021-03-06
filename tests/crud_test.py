import pytest
from src.db.crud import Crud
import mongomock

TEST_DOCUMENTS = [
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

def test_one_insert():
    db = mongomock.MongoClient().db
    collection = db.collection
    cr = Crud(db)

    test_document = {
        "Attr1" : 1,
        "Attr2" : 2
    }

    cr.insert("collection", test_document)

    result_document = collection.find_one(filter=test_document)
    
    assert test_document == result_document

def test_bulk_insert():
    db = mongomock.MongoClient().db
    collection = db.collection
    cr = Crud(db)

    cr.insert("collection", TEST_DOCUMENTS)
    result_objs = list(collection.find())

    assert len(result_objs) == 3

def test_unknown_type():
    db = mongomock.MongoClient().db
    cr = Crud(db)

    with pytest.raises(TypeError):
        cr.insert("collection", None)

    with pytest.raises(TypeError):
        cr.insert("collection", "TEST")

def test_simple_query():
    db = mongomock.MongoClient().db
    cr = Crud(db)

    cr.insert("collection", TEST_DOCUMENTS)

    simple_query = {"Attr1" : 1}

    results = cr.get_collection("collection").find(simple_query)

    assert len(list(results)) == 2
    for res in results: assert(res["Attr1"] == 1)

def test_advanced_query():
    db = mongomock.MongoClient().db
    cr = Crud(db)

    cr.insert("collection", TEST_DOCUMENTS)

    advanced_query = {"Attr2" : { "$gt": 2 }}

    results = cr.get_collection("collection").find(advanced_query)

    assert len(list(results)) == 2
    for res in results: assert(res["Attr2"] > 2)

def test_delete():
    db = mongomock.MongoClient().db
    cr = Crud(db)

    cr.insert("collection", TEST_DOCUMENTS)
    
    delete_rule = {"Attr1" : 1}

    cr.delete("collection", delete_rule)
    
    results = cr.get_collection("collection").find({})

    assert len(list(results)) == 1

    results = cr.get_collection("collection").find(delete_rule)

    assert len(list(results)) == 0

def test_update():
    db = mongomock.MongoClient().db
    cr = Crud(db)

    cr.insert("collection", TEST_DOCUMENTS)

    query = { "Attr1": 1 }
    new_value = { "$set": { "Attr1": 10 } }
    cr.update("collection", query, new_value)

    results = cr.get_collection("collection").find({"Attr1" : 10})

    assert len(list(results)) == 2