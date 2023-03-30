from requests import post

from models import TransmissionModel


def transmit_tx_to_receiver_node(receiver: str, tx: dict) -> None:
    data = TransmissionModel().dumps(tx)
    post(url="http://" + receiver + ":5000/receive-tx", data=data)
