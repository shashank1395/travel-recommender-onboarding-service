from collections import namedtuple

class ValidateOTPRequest(namedtuple("ValidateOTPRequest", "name email password user_id otp otp_reference_id")):
    def __new__(cls, name = None, email = None, password = None, user_id = None, otp = None, otp_reference_id = None): 
        return super(ValidateOTPRequest, cls).__new__(cls, name, email, password, user_id, otp, otp_reference_id)

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def get_user_id(self):
        return self.user_id

    def get_otp(self):
        return self.otp

    def get_otp_reference_id(self):
        return self.otp_reference_id