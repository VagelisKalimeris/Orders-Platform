import uuid

from pydantic import BaseModel

from order.models.router_model import Status


class InMemDB:
    db = {}

    def __init__(self):
        self.db = InMemDB.db

    class Entry(BaseModel):
        stoks: str
        quantity: float
        status: Status

    @staticmethod
    def generate_uuid():
        return uuid.uuid4()

    def get_all_db_entries(self):
        return self.db

    def get_specific_db_entry(self, order_id: str):
        return self.db.get(order_id)

    def add_db_entry(self, stoks: str, quantity: float) -> str:
        new_uuid = str(self.generate_uuid())

        self.db[new_uuid] = self.Entry(
            stoks=stoks,
            quantity=quantity,
            status=Status.pending
        )

        return new_uuid

    def remove_db_entry(self, order_id: str):
        del self.db[order_id]

    def update_db_entry_status(self, order_id: str, new_status: Status):
        if entry := self.db.get(self.db[order_id]):
            entry.status = new_status
