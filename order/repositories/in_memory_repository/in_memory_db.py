import uuid
from asyncio import Lock

from pydantic import BaseModel

from order.models.router_model import Status


class InMemDB:
    # Class variables
    db = {}
    db_lock = Lock()

    # def __init__(self):
    #     self.db = InMemDB.db

    class Entry(BaseModel):
        stoks: str
        quantity: float
        status: Status

    def generate_unique_uuid(self):
        # Produce unique order id
        while True:
            new_uuid = str(uuid.uuid4())
            if not self.db.get(new_uuid):
                return new_uuid

    async def get_all_db_entries(self):
        async with self.db_lock:
            return self.db

    async def get_specific_db_entry(self, order_id: str):
        async with self.db_lock:
            return self.db.get(order_id)

    async def add_db_entry(self, stoks: str, quantity: float) -> str:
        async with self.db_lock:
            new_uuid = self.generate_unique_uuid()

            self.db[new_uuid] = self.Entry(
                stoks=stoks,
                quantity=quantity,
                status=Status.pending
            )

        return new_uuid

    async def update_db_entry_status(self, order_id: str, new_status: Status):
        async with self.db_lock:
            if entry := self.db.get(order_id):
                entry.status = new_status
