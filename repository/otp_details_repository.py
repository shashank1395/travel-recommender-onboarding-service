from db import mongo

def insert_otp_details(otp_details):
    return mongo.db.otp_details.insert_one(otp_details)

def check_if_otp_details_exists(user_id, otp_reference_id):
    return mongo.db.otp_details.find_one({'user_id':user_id,'_id':otp_reference_id})

def update_otp_details(user_id, otp_reference_id,otp, current_time, number_of_validation_attempts):
    query = {"user_id":user_id, "_id":otp_reference_id, "otp":otp}
    update = {"$set" : {"used_at":current_time, "number_of_validation_attempts" : number_of_validation_attempts + 1}}
    mongo.db.otp_details.update_one(query, update)