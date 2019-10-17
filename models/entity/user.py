from collections import namedtuple


class User(object):
    
    def __init__(self):
        self._id = ""
        self.name = ""
        self.email = ""
        self.password_exists = True
        self.status = 0
        self.created_at = 0
        self.created_by = ""
        self.updated_at = 0
        self.updated_by = ""

    def set_id(self, _id):
        self._id = _id

    def get_id(self):
        return self._id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def is_password_exists(self):
        return self.password_exists

    def set_password_exists(self, password_exists):
        self.password_exists = password_exists

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_created_at(self):
        return self.created_at

    def set_created_at(self, created_at):
        self.created_at = created_at

    def get_created_by(self):
        return self.created_by

    def set_created_by(self, created_by):
        self.created_by = created_by
    
    def get_updated_at(self):
        return self.updated_at

    def set_updated_at(self, updated_at):
        self.updated_at = updated_at

    def get_updated_by(self):
        return self.updated_by

    def set_updated_by(self, updated_by):
        self.updated_by = updated_by
