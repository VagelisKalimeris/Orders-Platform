from test.order_tests.test_data.orders.order_test_model import Order

sample_orders = [
    Order('banana', 35),
    Order('pear', 15),
    Order('cherry', 5),
    Order('kiwi', 1)
]


"""To be populated by tests"""
sample_order_ids = []


orders_to_delete = [1, 3]


invalid_order_id = 'invalid-order-uuid-must-fail'
