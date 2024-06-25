import asyncio
import uuid
from random import randrange

from order.models.router_model import Status


class Order:
    def __init__(self, repository):
        self.repository = repository

    @staticmethod
    async def gen_rand_delay() -> None:
        delay = randrange(10) * .1
        await asyncio.sleep(delay)

    async def update_status_in_background(self, order_id: str) -> None:
        await Order.gen_rand_delay()

        await self.repository.update_db_entry_status(order_id, Status.executed)

    async def get_all_orders(self) -> dict:
        await Order.gen_rand_delay()

        return await self.repository.get_all_db_entries()

    async def post_new_order(self, stoks: str, quantity: float) -> uuid:
        await Order.gen_rand_delay()

        new_order_id = await self.repository.add_db_entry(stoks, quantity)

        # This task will run in background and will not block POST
        asyncio.create_task(self.update_status_in_background(new_order_id))

        return new_order_id

    async def get_specific_order(self, order_id: str) -> Status:
        await Order.gen_rand_delay()

        return await self.repository.get_specific_db_entry(order_id)

    async def cancel_existing_order(self, order_id: str):
        await Order.gen_rand_delay()

        return await self.repository.update_db_entry_status(order_id, Status.canceled)
