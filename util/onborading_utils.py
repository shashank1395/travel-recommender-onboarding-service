def get_signup_response(user_id, otp_reference_id):
    signup_response = {}
    signup_response['user_id'] = user_id
    signup_response['otp_reference_id'] = otp_reference_id
    return signup_response