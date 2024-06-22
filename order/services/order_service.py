from order.repositories.in_memory_repository.in_memory_db import InMemDB


class Order:
    @staticmethod
    def get_all_orders():
        return InMemDB.get_all_db_entries()


    @staticmethod
    def post_new_order(stoks: str, quantity: float):
        return InMemDB.add_db_entry(stoks, quantity)


    @staticmethod
    def get_specific_order(order_id: str):
        return InMemDB.get_specific_db_entry(order_id)

    @staticmethod
    def delete_existing_order(order_id: str):
        InMemDB.remove_db_entry(order_id)
