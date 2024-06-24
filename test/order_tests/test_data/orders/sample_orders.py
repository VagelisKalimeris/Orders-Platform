from test.order_tests.test_data.orders.order_test_model import Order

sample_orders = [
    Order('EURUSD', 35.09),
    Order('USDJPY', 15.23),
    Order('GBPUSD', 05.03),
    Order('USDCHF', 1.00)
]


"""To be populated by tests"""
sample_order_ids = []


orders_to_delete = [1, 3]


invalid_order_id = 'invalid-order-uuid-must-fail'
