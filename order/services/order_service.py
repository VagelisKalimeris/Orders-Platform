import uuid
from random import randrange
from time import sleep

from order.models.router_model import Status


class Order:
    def __init__(self, repository):
        self.repository = repository

    @staticmethod
    def gen_rand_delay() -> None:
        delay = randrange(10) * .1
        sleep(delay)

    async def get_all_orders(self) -> dict:
        return await self.repository.get_all_db_entries()

    async def post_new_order(self, stoks: str, quantity: float) -> uuid:
        new_order_id = await self.repository.add_db_entry(stoks, quantity)

        Order.gen_rand_delay()

        await self.repository.update_db_entry_status(new_order_id, Status.executed)

        return new_order_id

    async def get_specific_order(self, order_id: str) -> Status:
        return await self.repository.get_specific_db_entry(order_id)

    async def cancel_existing_order(self, order_id: str):
        Order.gen_rand_delay()

        return await self.repository.update_db_entry_status(order_id, Status.canceled)
