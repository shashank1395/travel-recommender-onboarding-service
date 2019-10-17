from db import mongo

def insert_user(user):
    return mongo.db.user.insert_one(user)

def check_if_user_exists(email, name):
    return mongo.db.user.find_one({'email' : email, 'name' : name})