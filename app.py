import json

import flask
from flask_cors import CORS

import databaseOperations

app = flask.Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.get('/')
def get_all_data():
    return databaseOperations.get_all_data()

@app.post('/insertData')
def insert_data():
    try:
        body = flask.request.get_json()
    except Exception as error:
        return "Error in body. Please make sure to pass json" + error.__str__()
    return databaseOperations.insert_into_database(body["body"])

@app.post('/insertMultipleData')
def insert_multiple_data():
    try:
        body = flask.request.get_json()
        data = body["body"]
    except Exception as error:
        return "Error in body. Please make sure to pass json" + error.__str__()
    return databaseOperations.insert_multiple_data(data["start"], data["end"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
