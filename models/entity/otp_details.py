class OTPDetails(object):
    
    def __init__(self):
        self._id = ""
        self.user_id = ""
        self.otp = 0
        self.number_of_validation_attempts = 0
        self.used_at = True
        self.expires_at = 0
        self.created_at = 0

    def set_id(self, _id):
        self._id = _id

    def get_id(self):
        return self._id

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_otp(self):
        return self.otp
    
    def set_otp(self, otp):
        self.otp = otp

    def get_number_of_validation_attempts(self):
        return self.number_of_validation_attempts

    def set_number_of_validation_attempts(self, number_of_validation_attempts):
        self.number_of_validation_attempts = number_of_validation_attempts

    def get_used_at(self):
        return self.used_at

    def set_used_at(self, used_at):
        self.used_at = used_at

    def get_created_at(self):
        return self.created_at

    def set_created_at(self, created_at):
        self.created_at = created_at
    
    def get_expires_at(self):
        return self.expires_at

    def set_expires_at(self, expires_at):
        self.expires_at = expires_at
