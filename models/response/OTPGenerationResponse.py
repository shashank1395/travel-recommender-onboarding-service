from collections import namedtuple

class OTPGenerationResponse(namedtuple("OTPGenerationResponse", "userId email waitingTime scenario")):
    def __new__(cls, referenceId = None, email = None, waitingTime = None, scenario = None): 
        return super(OTPGenerationResponse, cls).__new__(cls, referenceId, email, waitingTime, scenario)

    def get_reference_id(self):
        return self.referenceId

    def get_email(self):
        return self.email

    def get_waiting_time(self):
        return self.waitingTime

    def get_scenario(self):
        return self.scenario

    def set_reference_id(self, referenceId):
        self.referenceId = referenceId
    
    def set_email(self, email):
        self.email = email

    def set_waiting_time(self, waitingTime):
        self.waitingTime = waitingTime

    def set_scenario(self, scenario):
        self.scenario = scenario