from flask import jsonify

class TravelBaseExcpetion(Exception):
    status_code = 400
    def __init__(self, message, status_code=None, service_status_code = None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.service_status_code = service_status_code

    def to_dict(self):
        payload = {}
        payload['message'] = self.message
        payload['status'] = self.service_status_code
        return payload