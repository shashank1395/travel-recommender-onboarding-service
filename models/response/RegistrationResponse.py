from collections import namedtuple

class RegistrationResponse(namedtuple("RegistrationResponse", "userId otpDetails")):
    def __new__(cls, userId = None, otpDetails = None): 
        return super(RegistrationResponse, cls).__new__(cls, userId, otpDetails)

    def get_user_id(self):
        return self.userId

    def get_otp_details(self):
        return self.otpDetails

    def set_user_id(self, userId):
        self.userId = userId
    
    def set_otp_details(self, otpDetails):
        self.otpDetails = otpDetails