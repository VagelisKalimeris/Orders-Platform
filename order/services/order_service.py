class Order:
    def __init__(self, repository):
        self.repository = repository

    def get_all_orders(self):
        return self.repository.get_all_db_entries()


    def post_new_order(self, stoks: str, quantity: float):
        return self.repository.add_db_entry(stoks, quantity)


    def get_specific_order(self, order_id: str):
        return self.repository.get_specific_db_entry(order_id)

    def delete_existing_order(self, order_id: str):
        self.repository.remove_db_entry(order_id)
