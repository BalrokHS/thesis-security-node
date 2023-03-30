from flask import Flask, request

from db import mysql, NodeList, BootstrapTable
from models import TransactionModel
from http import HTTPStatus

from dotenv import load_dotenv

from utils import transmit_tx_to_receiver_node

load_dotenv()

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'my-secret-pw'
app.config['MYSQL_DATABASE_DB'] = 'bc_bootstrap_node'

mysql.init_app(app)


@app.route('/')
def hello():
    return "This is the security node"


@app.route('/transmit-transaction', methods=['POST'])
def transmit_transaction():
    tx = TransactionModel().loads(request.get_data())
    node_list = NodeList()

    does_sender_exists = node_list.check_if_addr_exists(tx.get('sender'))
    does_receiver_exists = node_list.check_if_addr_exists(tx.get('receiver'))

    if not does_sender_exists or not does_receiver_exists:
        return 'The targets of the transaction were not registered in the network', HTTPStatus.NOT_FOUND

    bs_node = BootstrapTable()
    bs_node.add_transaction(tx)

    transmit_tx_to_receiver_node(tx.get('receiver'), tx)

    return 'The transaction was transmitted successfully', HTTPStatus.OK


@app.route('/register-node', methods=['POST'])
def register_node_to_list():
    node_list = NodeList()

    if node_list.check_if_addr_exists(request.remote_addr) is False:
        node_list.add_node(request.remote_addr)

    return 'Node was added', HTTPStatus.OK


if __name__ == '__main__':
    app.run()
