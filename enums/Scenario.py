import enum

class OTPScenario(enum.Enum):
    SIGN_UP = 1
    LOGIN = 2
    RESEND = 3
    UPDATE_EMAIL = 4
    FORGET_PASSWORD = 5
    SOCIAL_SIGN_UP = 6
    SOCIAL_LOG_IN = 7
    CHANGE_PASSWORD = 8

otp_scenario_map = {}

for status in (OTPScenario):
    otp_scenario_map[status.value] = status

def get_status_by_code(status_code):
    if(status_code in otp_scenario_map):
        return otp_scenario_map.get(status_code)
    else:
        return -1