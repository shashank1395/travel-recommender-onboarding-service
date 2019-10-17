import enum

class ResponseCode(enum.Enum):
    REQUEST_VALIDATION_FAILURE = 2000
    USER_ALREADY_EXISTS = 2010
    USER_BANNED = 2020