import flask
from flask_pymongo import PyMongo

app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/travel-user"
mongo = PyMongo(app)