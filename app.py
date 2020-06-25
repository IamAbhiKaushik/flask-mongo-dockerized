from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
mongo = MongoClient('mongodb://mongo/test').db
# mongo = MongoClient('mongodb://localhost:27017').db
BASE_URL = "http://localhost:5000"

@app.route("/")
def home():
	return dumps({'Version': 1.2, 'health': 'Working Fine'})


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')