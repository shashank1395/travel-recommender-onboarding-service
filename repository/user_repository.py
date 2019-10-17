from db import mongo
import json
from bson.json_util import dumps

def insert_user(user):
    return mongo.db.user.insert_one(user)
    #return "Hi"

def check_if_user_exists(email, name):
    return mongo.db.user.find_one({'email' : email, 'name' : name})