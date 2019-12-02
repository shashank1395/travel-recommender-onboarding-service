import exceptions.travel_base_exception as travel_exception

from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import Blueprint, jsonify, request
from jsonschema import ValidationError, validate
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

import models.registration_request as register_request_model
import models.validate_otp_request as validate_otp_request_model
import service.user_service as user_service
from enums.response_code import ResponseCode
from enums.user_account_status import UserAccountStatus
from schema.register_request_schema import RegisterRequestSchema
from schema.validate_otp_request_schema import ValidateOTPSchema

onboarding_api = Blueprint('onboarding_api', __name__)

def convert_input_to(func):
    def wrap(f):
        def decorator(*args):
            obj = func(**request.get_json())
            return f(obj)
        decorator.__name__ = func.__name__
        return decorator
    return wrap

register_request_schema = RegisterRequestSchema()
validate_otp_request_schema = ValidateOTPSchema()

@onboarding_api.route('/user', methods=['POST'])
@convert_input_to(register_request_model.RegistrationRequest)
def register_user(registration_request):
    validation_error = register_request_schema.validate(request.get_json())
    if validation_error:
        final_error_data = {}
        for key, value in validation_error.items():
            final_error_data[key] = value
        final_error_data['status'] = ResponseCode.REQUEST_VALIDATION_FAILURE.value
        raise ValidationError(str(final_error_data))
    resp = user_service.register_user(registration_request)
    return resp

@onboarding_api.route('/validate-otp', methods=['PUT'])
@convert_input_to(validate_otp_request_model.ValidateOTPRequest)
def validate_otp(validate_otp_request):
	validation_error = validate_otp_request_schema.validate(request.get_json())
	if validation_error:
		final_error_data = {}
		for key, value in validation_error.items():
			final_error_data[key] = value
		final_error_data['status'] = ResponseCode.REQUEST_VALIDATION_FAILURE.value
		raise ValidationError(str(final_error_data))
	resp = user_service.validate_otp(validate_otp_request)
	return resp

@onboarding_api.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: '
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@onboarding_api.errorhandler(400)
def invalid_status(status_code):
    message = {
        'status': 400,
        'message': 'Inavlid status : ' + status_code
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@onboarding_api.errorhandler(ValidationError)
def request_validation_failure(validation_error):
	resp = jsonify(eval(validation_error.message))
	resp.status_code = 400
	return resp

@onboarding_api.errorhandler(travel_exception.TravelBaseExcpetion)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
