from db import mongo

def insert_otp_details(otp_details):
    return mongo.db.otp_details.insert_one(otp_details)
