from flask import jsonify
from passlib.hash import pbkdf2_sha256 as sha256
from enums.user_account_status import UserAccountStatus
import repository.user_repository as user_repository
from models.entity.user import User
from enums.response_code import ResponseCode
import exceptions.travel_base_exception as travel_base_exception
from bson.json_util import dumps
import time
import json
from configparser import ConfigParser
import smtplib

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
    __send_mail_for_otp__(registration_request.get_email(), registration_request.get_name())
    resp = jsonify(user_data.__dict__)
    return resp

def __send_mail_for_otp__(receipient_mail, name):
    header = 'To:' + receipient_mail + '\n' + 'From: ' + app_config.get(
        'smtp_configuration', 'sender_id') + '\n' + 'Subject:' + app_config.get('smtp_configuration', 'subject') + '4739474' + ' \n'
    message = header + '\n' + app_config.get('smtp_configuration', 'body_prefix').replace('[name]', name).replace('[otp]', '4739474') + '\n'

    server = smtplib.SMTP(app_config.get('smtp_configuration', 'host'), int(
        app_config.get('smtp_configuration', 'port')))

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(app_config.get('smtp_configuration', 'username'),
                 app_config.get('smtp_configuration', 'password'))
    server.sendmail(app_config.get('smtp_configuration', 'sender_id'), receipient_mail.split(', '), message)

    server.close()