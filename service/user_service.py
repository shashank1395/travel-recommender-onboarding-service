import exceptions.travel_base_exception as travel_base_exception
import json
import math
import random
import smtplib
import time
from configparser import ConfigParser

from bson.json_util import dumps
from flask import jsonify
from passlib.hash import pbkdf2_sha256 as sha256

import repository.otp_details_repository as otp_details_repository
import repository.user_repository as user_repository
import util.onborading_utils as onborading_utils
from enums.response_code import ResponseCode
from enums.user_account_status import UserAccountStatus
from models.entity.otp_details import OTPDetails
from models.entity.user import User

config_file_path = 'app_config.ini'

app_config = ConfigParser()
app_config.read(config_file_path)

def register_user(registration_request):
    user = User()
    user = user_repository.check_if_user_exists(registration_request.email, registration_request.name)
    if user != None :
        print(user['status'])
        if user['status'] == UserAccountStatus.ACTIVE.value or user['status'] == UserAccountStatus.SUSPENDED.value:
            raise travel_base_exception.TravelBaseExcpetion(str(ResponseCode.USER_ALREADY_EXISTS.name), 400, ResponseCode.USER_ALREADY_EXISTS.value)
        if user['status'] == UserAccountStatus.BANNED.value:
            raise travel_base_exception.TravelBaseExcpetion(str(ResponseCode.USER_BANNED.name), 400, ResponseCode.USER_BANNED.value)
    current_time = int(time.time() * 1000)
    user_id = str("USER-" + str(current_time))
    user_data = User()
    user_data.set_id(user_id)
    user_data.set_name(registration_request.get_name())
    user_data.set_email(registration_request.get_email())
    #user_data.user_id = sha256.hash(registration_request.password)
    user_data.set_status(UserAccountStatus.ACTIVE.value)
    if not registration_request.get_password():
       user_data.set_password_exists(False)
    user_data.set_created_at(current_time)
    user_data.set_created_by(user_id)
    user_data.set_updated_at(current_time)
    user_data.set_updated_by(user_id)
    user_repository.insert_user(user_data.__dict__)
    otp_generation_map = generate_one_time_password(user_id)
    __send_mail_for_otp__(registration_request.get_email(), registration_request.get_name(), otp_generation_map['one_time_password'])
    resp = jsonify(onborading_utils.get_signup_response(user_id, otp_generation_map['otp_reference_id']))
    return resp

def generate_one_time_password(user_id):
    current_time = int(time.time() * 1000)
    digits = "0123456789"
    one_time_password = ""
    for i in range(6) : 
        one_time_password += digits[math.floor(random.random() * 10)]
    otp_details = OTPDetails()
    otp_reference_id = "OTP-" + str(current_time)
    otp_details.set_id(otp_reference_id)
    otp_details.set_created_at(current_time)
    otp_details.set_expires_at(current_time + (5 * 60 * 1000))
    otp_details.set_number_of_validation_attempts(0)
    otp_details.set_otp(int(one_time_password))
    otp_details.set_used_at(0)
    otp_details.set_user_id(user_id)
    otp_details_repository.insert_otp_details(otp_details.__dict__)
    otp_generation_map = {}
    otp_generation_map['one_time_password'] = int(one_time_password)
    otp_generation_map['otp_reference_id'] = otp_reference_id
    return otp_generation_map

def __send_mail_for_otp__(receipient_mail, name, one_time_password):
    header = 'To:' + receipient_mail + '\n' + 'From: ' + app_config.get(
        'smtp_configuration', 'sender_id') + '\n' + 'Subject:' + app_config.get('smtp_configuration', 'subject') + str(one_time_password) + ' \n'
    message = header + '\n' + app_config.get('smtp_configuration', 'body_prefix').replace('[name]', name).replace('[otp]', str(one_time_password)) + '\n'

    server = smtplib.SMTP(app_config.get('smtp_configuration', 'host'), int(
        app_config.get('smtp_configuration', 'port')))

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(app_config.get('smtp_configuration', 'username'),
                 app_config.get('smtp_configuration', 'password'))
    server.sendmail(app_config.get('smtp_configuration', 'sender_id'), receipient_mail.split(', '), message)

    server.close()
