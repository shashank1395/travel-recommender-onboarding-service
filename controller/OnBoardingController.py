from flask import jsonify, request, Blueprint
from bson.json_util import dumps
from bson.objectid import ObjectId
from jsonschema import validate, ValidationError
from enums.user_account_status import UserAccountStatus
from enums.response_code import ResponseCode
from schema.register_request_schema import RegisterRequestSchema
import service.user_service as user_service
import models.registration_request as register_request_model
import exceptions.travel_base_exception as travel_exception

onboarding_api = Blueprint('onboarding_api', __name__)

register_request_schema = RegisterRequestSchema()

def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap

@onboarding_api.route('/user', methods=['POST'])
@convert_input_to(register_request_model.RegistrationRequest)
def register_user(registration_request_json):
	validation_error = register_request_schema.validate(request.get_json())
	if validation_error:
		final_error_data = {}
		for key, value in validation_error.items():
			final_error_data[key] = value
		final_error_data['status'] = ResponseCode.REQUEST_VALIDATION_FAILURE.value
		raise ValidationError(str(final_error_data))
	resp = user_service.register_user(registration_request_json)
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