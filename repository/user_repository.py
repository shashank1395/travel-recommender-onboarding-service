from db import mongo

def insert_user(user):
    return mongo.db.user.insert_one(user)

def check_if_user_exists(email, name):
    return mongo.db.user.find_one({'email' : email, 'name' : name})

def find_by_user_id(user_id):
    return mongo.db.user.find_one({'_id':user_id})

def update_user_status(user_id, user_account_status, time):
    query = {"_id":user_id}
    update = {"$set" : {"status" : user_account_status, "updated_at": time}}
    mongo.db.user.update_one(query, update)