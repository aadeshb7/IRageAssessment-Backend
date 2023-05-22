import json

from bson import json_util

from util import databaseFactory


client = databaseFactory.get_database_client()
database = client["MongoDB"]
collection = database["IRageData"]

def get_all_data():
    array = []
    for data in collection.find({}, {"_id": 1, "tag1": 1, "tag2": 1, "tag3": 1, "metric1": 1, "metric2": 1 }):
        array.append(data)
    return json.loads(json_util.dumps({"data": array}))

def insert_into_database(body):
    inserted_data = collection.insert_many(body)
    return json.loads(json_util.dumps({"data": inserted_data.inserted_ids}))

def insert_multiple_data(start, end):
    array = []
    for i in range(start, end):
        dict = {
                "tag1": "value" + str(i) + "1",
                "tag3": "value" + str(i) + "1",
                "tag2": "value" + str(i) + "1",
                "metric1": i,
                "metric2": i
        }
        array.append(dict)
    collection.insert_many(array)
    return get_all_data()

