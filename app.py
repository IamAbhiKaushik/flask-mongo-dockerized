from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime


app = Flask(__name__)
mongo = MongoClient('mongodb://mongo/test').db
# mongo = MongoClient('mongodb://localhost:27017').db
BASE_URL = "http://localhost:5000"

@app.route("/")
def home():
	return dumps({'Version': 1.2, 'health': 'Working Fine'})

@app.route("/insert")
def insert():
	insert_response = mongo.record_table.insert_one({
			"updated_at": datetime.utcnow(),
			'data': 'Test data'
			})
	response = mongo.record_table.find_one({"_id": insert_response.inserted_id})
	return dumps(response)

@app.route("/find")
def find():
	return dumps(mongo.record_table.find())

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')