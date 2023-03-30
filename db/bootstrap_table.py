from models import TransactionModel
from .db_entity import DBEntity


class BootstrapTable(DBEntity):
    def __init__(self):
        super().__init__()

    def close(self):
        super().close()

    def add_transaction(self, tx: dict):

        self.cursor.execute("INSERT INTO bootstrap_table(block_id, transaction_id, sender_addr, receiver_addr, "
                            " data, category) VALUES (%s, %s, %s, %s, %s, %s)", (tx.get('block_id'),
                                                                                 tx.get('tx_id'),
                                                                                 tx.get('sender'),
                                                                                 tx.get('receiver'),
                                                                                 tx.get('data'),
                                                                                 tx.get('category')))

        self.cursor.connection.commit()
        self.close()
