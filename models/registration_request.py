from collections import namedtuple

class RegistrationRequest(namedtuple("RegistrationRequest", "name email password")):
    def __new__(cls, name = None, email = None, password = None): 
        return super(RegistrationRequest, cls).__new__(cls, name, email, password)

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email