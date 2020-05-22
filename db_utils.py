import pymongo

client = pymongo.MongoClient("localhost", 27017)

example_db = client.example

def init():
    for c in example_db.list_collection_names():
        example_db[c].delete_many({})

def get_collection(collection_name):
    return example_db[collection_name]
