import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from util import configurationParser, encryptor


def get_database_client():
    config = configurationParser.get_configparser()
    username = config.get("DatabaseSection", "username")
    password = config.get("DatabaseSection", "password")
    uri = config.get("DatabaseSection", "uri")
    return MongoClient(uri.format(username=username, password=encryptor.decrypt_password(password)), server_api=ServerApi('1'), tlsCAFile=certifi.where())

if __name__ == '__main__':
    try:
        client = get_database_client()
        database = client["MongoDB"]
        collection = database["IRageData"]

        # collection.delete_many({})

        array = []
        for i in range(400, 500):
            dict = {
                "tag1": "value" + str(i) + "1",
                "tag2": "value" + str(i) + "2",
                "tag3": "value" + str(i) + "3",
                "metric1": i,
                "metric2": i
            }
            array.append(dict)
        collection.insert_many(array)

        # for x in collection.find():
        #     print(x)
    except Exception as e:
        print("Error while connecting to DB" + e.__str__())
        exit(1)
    finally:
        client.close()

