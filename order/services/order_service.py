from random import randrange
from time import sleep

from order.models.router_model import Status


class Order:
    def __init__(self, repository):
        self.repository = repository

    @staticmethod
    def gen_rand_delay():
        return randrange(10) * .1

    def get_all_orders(self):
        return self.repository.get_all_db_entries()

    def post_new_order(self, stoks: str, quantity: float):
        new_order_id = self.repository.add_db_entry(stoks, quantity)

        delay = Order.gen_rand_delay()
        sleep(delay)

        self.repository.update_db_entry_status(new_order_id, Status.executed)

        return new_order_id

    def get_specific_order(self, order_id: str):
        return self.repository.get_specific_db_entry(order_id)

    def cancel_existing_order(self, order_id: str):
        delay = Order.gen_rand_delay()
        sleep(delay)

        self.repository.update_db_entry_status(order_id, Status.canceled)
