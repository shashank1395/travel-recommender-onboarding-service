from marshmallow import Schema, fields
from marshmallow.validate import Length, Regexp, Range

class RegisterRequestSchema(Schema):
    name = fields.Str(required=True, validate=Length(min=3, max=30))
    email = fields.Str(required = True, validate = Regexp("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"))
    password = fields.Str(required = False, validate=Length(min=3, max=30))