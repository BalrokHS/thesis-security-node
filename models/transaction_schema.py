from marshmallow import Schema, fields
from .transmission_schema import TransmissionModel


class TransactionModel(TransmissionModel):
    block_id = fields.Integer()
    tx_id = fields.Integer()

