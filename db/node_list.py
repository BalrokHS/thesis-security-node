from .db_entity import DBEntity


class NodeList(DBEntity):
    def __init__(self):
        super().__init__()

    def close(self):
        super().close()

    def get(self):
        self.cursor.execute("SELECT node_address FROM node_list")
        res = self.cursor.fetchall()
        self.close()
        return res

    def check_if_addr_exists(self, addr: str) -> bool:
        self.cursor.execute("SELECT node_address FROM node_list WHERE node_address = % s", addr)
        res = self.cursor.fetchone()
        self.close()
        if res is not None and len(res) == 1:
            return True

        return False

    def add_node(self, addr: str):
        self.cursor.execute("INSERT INTO node_list(node_address) VALUES (% s )", addr)
        self.cursor.connection.commit()
        self.close()
