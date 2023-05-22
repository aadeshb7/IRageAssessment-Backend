import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://DJChampion:DJChampion@cluster0.e5rdrzu.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
# Send a ping to confirm a successful connection
try:
    database = client["MongoDB"]
    collection = database["IRageData"]

    # collection.delete_many({})
    array = []
    for i in range(101,200):
        dict = {
                "tag1": "value" + str(i) + "1",
                "tag3": "value" + str(i) + "1",
                "tag2": "value" + str(i) + "1",
                "metric1": "metricValue" + str(i) + "1",
                "metric2": "metricValue" + str(i) + "1"
        }
        array.append(dict)
    insertedData = collection.insert_many(array)
    print(insertedData.inserted_ids)

except Exception as e:
    print(e)