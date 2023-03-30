from marshmallow import Schema, fields


class TransmissionModel(Schema):
    sender = fields.Str()
    receiver = fields.Str()
    data = fields.Str()
    category = fields.Str()
    timestamp = fields.DateTime()
