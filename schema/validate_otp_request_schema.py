from marshmallow import Schema, fields
from marshmallow.validate import Length, Regexp, Range

class ValidateOTPSchema(Schema):
    name = fields.Str(required=True, validate=Length(min=3, max=30))
    email = fields.Str(required = True, validate = Regexp("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"))
    password = fields.Str(required = True, validate=Length(min=3, max=30))
    otp = fields.Int(required= True, validate= Range(100000, 999999))
    otp_reference_id = fields.Str(required=True)
    user_id = fields.Str(required= True)