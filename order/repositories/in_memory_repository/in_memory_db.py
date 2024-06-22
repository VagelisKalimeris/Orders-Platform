import uuid

from pydantic import BaseModel

from order.models.router_model import Status


class InMemDB:
    db = {}

    class Entry(BaseModel):
        stoks: str
        quantity: float
        status: Status

    @staticmethod
    def generate_uuid():
        return uuid.uuid4()

    @staticmethod
    def get_all_db_entries():
        return InMemDB.db

    @staticmethod
    def get_specific_db_entry(order_id: str):
        return InMemDB.db.get(order_id)

    @staticmethod
    def add_db_entry(stoks: str, quantity: float) -> str:
        new_uuid = str(InMemDB.generate_uuid())

        InMemDB.db[new_uuid] = InMemDB.Entry(
            stoks=stoks,
            quantity=quantity,
            status=Status.pending
        )

        return new_uuid

    @staticmethod
    def remove_db_entry(order_id: str):
        del InMemDB.db[order_id]

    @staticmethod
    def update_db_entry_status(order_id: str, new_status: Status):
        if entry := InMemDB.db.get(InMemDB.db[order_id]):
            entry.status = new_status
